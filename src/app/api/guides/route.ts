import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { agricultureItems, images } from "@/lib/db/schema";
import { eq, ilike, count, sql } from "drizzle-orm";
import { auth } from "@/lib/auth";
import { guideSchema } from "@/lib/validators/guides";

export async function GET(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { searchParams } = new URL(request.url);
  const page = parseInt(searchParams.get("page") || "1");
  const perPage = parseInt(searchParams.get("perPage") || "20");
  const searchField = searchParams.get("field");
  const searchValue = searchParams.get("q");
  const itemType = searchParams.get("type");

  const conditions = [];
  if (searchField && searchValue) {
    const allowedFields = ["common_name", "scientific_name", "key_characteristics", "biology", "impacts", "control"];
    if (allowedFields.includes(searchField)) {
      conditions.push(ilike(sql.raw(`"${searchField}"`), `%${searchValue}%`));
    }
  }
  if (itemType && (itemType === "pest" || itemType === "weed")) {
    conditions.push(eq(agricultureItems.itemType, itemType));
  }

  const whereClause = conditions.length > 0
    ? sql`${sql.join(conditions, sql` AND `)}`
    : undefined;

  const [items, totalResult] = await Promise.all([
    db
      .select()
      .from(agricultureItems)
      .where(whereClause)
      .limit(perPage)
      .offset((page - 1) * perPage)
      .orderBy(agricultureItems.agricultureId),
    db
      .select({ count: count() })
      .from(agricultureItems)
      .where(whereClause),
  ]);

  // Fetch images for these items
  const itemIds = items.map((i) => i.agricultureId);
  const itemImages =
    itemIds.length > 0
      ? await db
          .select()
          .from(images)
          .where(sql`${images.agricultureId} IN (${sql.join(itemIds.map(id => sql`${id}`), sql`, `)})`)
      : [];

  const itemsWithImages = items.map((item) => ({
    ...item,
    images: itemImages.filter((img) => img.agricultureId === item.agricultureId),
  }));

  return NextResponse.json({
    items: itemsWithImages,
    totalPages: Math.ceil(totalResult[0].count / perPage),
    currentPage: page,
    totalItems: totalResult[0].count,
  });
}

export async function POST(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || !["administrator", "staff"].includes(session.user.role)) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const body = await request.json();
  const parsed = guideSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json({ error: parsed.error.flatten() }, { status: 400 });
  }

  const { images: imageData, ...guideData } = parsed.data;

  const [newItem] = await db
    .insert(agricultureItems)
    .values(guideData)
    .returning();

  if (imageData && imageData.length > 0) {
    await db.insert(images).values(
      imageData.map((img) => ({
        agricultureId: newItem.agricultureId,
        imagePath: img.imagePath,
        isPrimary: img.isPrimary,
      }))
    );
  }

  return NextResponse.json(newItem, { status: 201 });
}
