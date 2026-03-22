import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { agronomists, staffAndAdministrators } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { auth } from "@/lib/auth";

export async function GET(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const role = session.user.role;

  if (role === "agronomist") {
    const [profile] = await db
      .select()
      .from(agronomists)
      .where(eq(agronomists.userId, session.user.id));
    return NextResponse.json({ role, profile });
  }

  const [profile] = await db
    .select()
    .from(staffAndAdministrators)
    .where(eq(staffAndAdministrators.userId, session.user.id));
  return NextResponse.json({ role, profile });
}

export async function PUT(request: NextRequest) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await request.json();
  const { field, value } = body;
  const role = session.user.role;

  if (role === "agronomist") {
    const allowedFields = ["first_name", "last_name", "email", "phone_number", "address"];
    if (!allowedFields.includes(field)) {
      return NextResponse.json({ error: "Invalid field" }, { status: 400 });
    }

    await db
      .update(agronomists)
      .set({ [camelCase(field)]: value })
      .where(eq(agronomists.userId, session.user.id));
  } else {
    const allowedFields = [
      "first_name", "last_name", "email", "work_phone_number", "position", "department",
    ];
    if (!allowedFields.includes(field)) {
      return NextResponse.json({ error: "Invalid field" }, { status: 400 });
    }

    await db
      .update(staffAndAdministrators)
      .set({ [camelCase(field)]: value })
      .where(eq(staffAndAdministrators.userId, session.user.id));
  }

  return NextResponse.json({ success: true });
}

function camelCase(snakeStr: string): string {
  return snakeStr.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
}
