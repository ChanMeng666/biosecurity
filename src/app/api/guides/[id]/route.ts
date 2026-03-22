import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { agricultureItems, images } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { auth } from "@/lib/auth";
import { guideSchema } from "@/lib/validators/guides";

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { id } = await params;
  const agricultureId = parseInt(id);

  const [item] = await db
    .select()
    .from(agricultureItems)
    .where(eq(agricultureItems.agricultureId, agricultureId));

  if (!item) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  const itemImages = await db
    .select()
    .from(images)
    .where(eq(images.agricultureId, agricultureId));

  return NextResponse.json({ ...item, images: itemImages });
}

export async function PUT(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || !["administrator", "staff"].includes(session.user.role)) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { id } = await params;
  const agricultureId = parseInt(id);
  const body = await request.json();
  const parsed = guideSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json({ error: parsed.error.flatten() }, { status: 400 });
  }

  const { images: imageData, ...guideData } = parsed.data;

  const [updated] = await db
    .update(agricultureItems)
    .set({ ...guideData, updatedAt: new Date() })
    .where(eq(agricultureItems.agricultureId, agricultureId))
    .returning();

  if (!updated) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  // Replace images if provided
  if (imageData) {
    await db.delete(images).where(eq(images.agricultureId, agricultureId));
    if (imageData.length > 0) {
      await db.insert(images).values(
        imageData.map((img) => ({
          agricultureId,
          imagePath: img.imagePath,
          isPrimary: img.isPrimary,
        }))
      );
    }
  }

  return NextResponse.json(updated);
}

export async function DELETE(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || session.user.role !== "administrator") {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { id } = await params;
  const agricultureId = parseInt(id);

  const [deleted] = await db
    .delete(agricultureItems)
    .where(eq(agricultureItems.agricultureId, agricultureId))
    .returning();

  if (!deleted) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  return NextResponse.json({ success: true });
}
