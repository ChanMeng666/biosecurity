import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { agronomists, user } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { auth } from "@/lib/auth";

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || !["administrator", "staff"].includes(session.user.role)) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { id } = await params;
  const agronomistId = parseInt(id);

  const [agronomist] = await db
    .select()
    .from(agronomists)
    .where(eq(agronomists.agronomistId, agronomistId));

  if (!agronomist) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  return NextResponse.json(agronomist);
}

export async function PUT(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || session.user.role !== "administrator") {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { id } = await params;
  const agronomistId = parseInt(id);
  const body = await request.json();

  const [updated] = await db
    .update(agronomists)
    .set({
      firstName: body.firstName,
      lastName: body.lastName,
      email: body.email,
      phoneNumber: body.phoneNumber,
      address: body.address,
      status: body.status,
    })
    .where(eq(agronomists.agronomistId, agronomistId))
    .returning();

  if (!updated) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
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
  const agronomistId = parseInt(id);

  const [agro] = await db
    .select()
    .from(agronomists)
    .where(eq(agronomists.agronomistId, agronomistId));

  if (!agro) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  // Delete from user table - cascade handles agronomists
  await db.delete(user).where(eq(user.id, agro.userId));

  return NextResponse.json({ success: true });
}
