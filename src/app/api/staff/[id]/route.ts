import { NextRequest, NextResponse } from "next/server";
import { db } from "@/lib/db";
import { staffAndAdministrators, user } from "@/lib/db/schema";
import { eq } from "drizzle-orm";
import { auth } from "@/lib/auth";

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const session = await auth.api.getSession({ headers: request.headers });
  if (!session || session.user.role !== "administrator") {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  const { id } = await params;
  const staffNumber = parseInt(id);

  const [staff] = await db
    .select()
    .from(staffAndAdministrators)
    .where(eq(staffAndAdministrators.staffNumber, staffNumber));

  if (!staff) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  return NextResponse.json(staff);
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
  const staffNumber = parseInt(id);
  const body = await request.json();

  const [updated] = await db
    .update(staffAndAdministrators)
    .set({
      firstName: body.firstName,
      lastName: body.lastName,
      email: body.email,
      workPhoneNumber: body.workPhoneNumber,
      position: body.position,
      department: body.department,
      status: body.status,
    })
    .where(eq(staffAndAdministrators.staffNumber, staffNumber))
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
  const staffNumber = parseInt(id);

  // Get userId first to delete from user table (cascades)
  const [staff] = await db
    .select()
    .from(staffAndAdministrators)
    .where(eq(staffAndAdministrators.staffNumber, staffNumber));

  if (!staff) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  // Delete from user table - cascade will handle staff_and_administrators
  await db.delete(user).where(eq(user.id, staff.userId));

  return NextResponse.json({ success: true });
}
