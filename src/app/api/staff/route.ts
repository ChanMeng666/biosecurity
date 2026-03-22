import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { staffAndAdministrators, user } from "@/lib/db/schema";
import { eq, ilike, count, sql } from "drizzle-orm";
import { auth } from "@/lib/auth";

export async function GET(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || session.user.role !== "administrator") {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { searchParams } = new URL(request.url);
  const page = parseInt(searchParams.get("page") || "1");
  const perPage = parseInt(searchParams.get("perPage") || "20");
  const searchField = searchParams.get("field");
  const searchValue = searchParams.get("q");

  const conditions = [];
  if (searchField && searchValue) {
    const allowedFields = ["first_name", "last_name", "email", "position", "department"];
    if (allowedFields.includes(searchField)) {
      conditions.push(ilike(sql.raw(`"${searchField}"`), `%${searchValue}%`));
    }
  }

  const whereClause = conditions.length > 0
    ? sql`${sql.join(conditions, sql` AND `)}`
    : undefined;

  const [staffList, totalResult] = await Promise.all([
    db
      .select({
        staffNumber: staffAndAdministrators.staffNumber,
        userId: staffAndAdministrators.userId,
        firstName: staffAndAdministrators.firstName,
        lastName: staffAndAdministrators.lastName,
        email: staffAndAdministrators.email,
        workPhoneNumber: staffAndAdministrators.workPhoneNumber,
        hireDate: staffAndAdministrators.hireDate,
        position: staffAndAdministrators.position,
        department: staffAndAdministrators.department,
        status: staffAndAdministrators.status,
        role: user.role,
      })
      .from(staffAndAdministrators)
      .innerJoin(user, eq(staffAndAdministrators.userId, user.id))
      .where(whereClause ? sql`${whereClause} AND ${user.role} = 'staff'` : eq(user.role, "staff"))
      .limit(perPage)
      .offset((page - 1) * perPage)
      .orderBy(staffAndAdministrators.staffNumber),
    db
      .select({ count: count() })
      .from(staffAndAdministrators)
      .innerJoin(user, eq(staffAndAdministrators.userId, user.id))
      .where(whereClause ? sql`${whereClause} AND ${user.role} = 'staff'` : eq(user.role, "staff")),
  ]);

  return NextResponse.json({
    items: staffList,
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

  const [newStaff] = await db
    .insert(staffAndAdministrators)
    .values({
      userId: session.user.id,
      firstName: body.firstName,
      lastName: body.lastName,
      email: body.email,
      workPhoneNumber: body.workPhoneNumber || null,
      position: body.position || null,
      department: body.department || null,
    })
    .returning();

  return NextResponse.json(newStaff, { status: 201 });
}
