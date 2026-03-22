import { NextRequest, NextResponse } from "next/server";
import { getSessionCookie } from "better-auth/cookies";

export async function middleware(request: NextRequest) {
  const sessionCookie = getSessionCookie(request);
  const { pathname } = request.nextUrl;

  const publicPaths = ["/", "/login", "/register", "/sources"];
  const isPublic =
    publicPaths.includes(pathname) || pathname.startsWith("/register/");

  // Redirect logged-in users away from auth pages
  if (sessionCookie && (pathname === "/login" || pathname.startsWith("/register"))) {
    return NextResponse.redirect(new URL("/admin", request.url));
  }

  // Allow public routes
  if (isPublic) {
    return NextResponse.next();
  }

  // Protect dashboard routes
  if (!sessionCookie) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
