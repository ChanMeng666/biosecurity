import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { agronomists } from "@/lib/db/schema";
import { ilike, count, sql } from "drizzle-orm";
import { auth } from "@/lib/auth";

export async function GET(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || !["administrator", "staff"].includes(session.user.role)) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { searchParams } = new URL(request.url);
  const page = parseInt(searchParams.get("page") || "1");
  const perPage = parseInt(searchParams.get("perPage") || "20");
  const searchField = searchParams.get("field");
  const searchValue = searchParams.get("q");

  const conditions = [];
  if (searchField && searchValue) {
    const allowedFields = ["first_name", "last_name", "email", "phone_number", "address"];
    if (allowedFields.includes(searchField)) {
      conditions.push(ilike(sql.raw(`"${searchField}"`), `%${searchValue}%`));
    }
  }

  const whereClause = conditions.length > 0
    ? sql`${sql.join(conditions, sql` AND `)}`
    : undefined;

  const [agronomistList, totalResult] = await Promise.all([
    db
      .select()
      .from(agronomists)
      .where(whereClause)
      .limit(perPage)
      .offset((page - 1) * perPage)
      .orderBy(agronomists.agronomistId),
    db.select({ count: count() }).from(agronomists).where(whereClause),
  ]);

  return NextResponse.json({
    items: agronomistList,
    totalPages: Math.ceil(totalResult[0].count / perPage),
    currentPage: page,
    totalItems: totalResult[0].count,
  });
}

export async function POST(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await request.json();

  const [newAgronomist] = await db
    .insert(agronomists)
    .values({
      userId: session.user.id,
      firstName: body.firstName,
      lastName: body.lastName,
      email: body.email,
      phoneNumber: body.phoneNumber || null,
      address: body.address || null,
    })
    .returning();

  return NextResponse.json(newAgronomist, { status: 201 });
}
