"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useSession, signOut } from "@/lib/auth/client";
import { Button, buttonVariants } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Shield, User, LogOut, Menu, X } from "lucide-react";
import { useState } from "react";
import { cn } from "@/lib/utils";

function getRoleDashboardPath(role: string) {
  switch (role) {
    case "administrator":
      return "/admin";
    case "staff":
      return "/staff";
    case "agronomist":
      return "/agronomist";
    default:
      return "/";
  }
}

export function Navbar() {
  const { data: session } = useSession();
  const router = useRouter();
  const [mobileOpen, setMobileOpen] = useState(false);

  const handleSignOut = async () => {
    await signOut();
    router.push("/login");
  };

  const initials = session?.user?.name
    ? session.user.name
        .split(" ")
        .map((n) => n[0])
        .join("")
        .toUpperCase()
        .slice(0, 2)
    : "U";

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto flex h-16 items-center justify-between px-4">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2 font-bold text-lg">
          <Shield className="h-6 w-6 text-emerald-600" />
          <span className="hidden sm:inline">Biosecurity Guide</span>
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden md:flex items-center gap-6">
          <Link
            href="/"
            className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Home
          </Link>
          <Link
            href="/sources"
            className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Sources
          </Link>

          {session?.user ? (
            <DropdownMenu>
              <DropdownMenuTrigger className="relative h-9 w-9 rounded-full cursor-pointer">
                <Avatar className="h-9 w-9">
                  <AvatarFallback className="bg-emerald-100 text-emerald-700 font-semibold text-sm">
                    {initials}
                  </AvatarFallback>
                </Avatar>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="w-56">
                <div className="px-2 py-1.5">
                  <p className="text-sm font-medium">{session.user.name}</p>
                  <p className="text-xs text-muted-foreground capitalize">
                    {session.user.role}
                  </p>
                </div>
                <DropdownMenuSeparator />
                <DropdownMenuItem
                  onClick={() => router.push(getRoleDashboardPath(session.user.role))}
                >
                  <User className="mr-2 h-4 w-4" />
                  Dashboard
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={handleSignOut}>
                  <LogOut className="mr-2 h-4 w-4" />
                  Sign Out
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          ) : (
            <div className="flex items-center gap-2">
              <Link
                href="/login"
                className={cn(buttonVariants({ variant: "ghost", size: "sm" }))}
              >
                Sign In
              </Link>
              <Link
                href="/register/agronomist"
                className={cn(
                  buttonVariants({ size: "sm" }),
                  "bg-emerald-600 hover:bg-emerald-700"
                )}
              >
                Register
              </Link>
            </div>
          )}
        </nav>

        {/* Mobile Toggle */}
        <Button
          variant="ghost"
          size="icon"
          className="md:hidden"
          onClick={() => setMobileOpen(!mobileOpen)}
        >
          {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </Button>
      </div>

      {/* Mobile Nav */}
      {mobileOpen && (
        <div className="md:hidden border-t bg-background px-4 py-4 space-y-3">
          <Link
            href="/"
            className="block text-sm font-medium"
            onClick={() => setMobileOpen(false)}
          >
            Home
          </Link>
          <Link
            href="/sources"
            className="block text-sm font-medium"
            onClick={() => setMobileOpen(false)}
          >
            Sources
          </Link>
          {session?.user ? (
            <>
              <Link
                href={getRoleDashboardPath(session.user.role)}
                className="block text-sm font-medium"
                onClick={() => setMobileOpen(false)}
              >
                Dashboard
              </Link>
              <Button variant="outline" size="sm" className="w-full" onClick={handleSignOut}>
                Sign Out
              </Button>
            </>
          ) : (
            <div className="flex gap-2">
              <Link
                href="/login"
                className={cn(buttonVariants({ variant: "outline", size: "sm" }), "flex-1 text-center")}
              >
                Sign In
              </Link>
              <Link
                href="/register/agronomist"
                className={cn(
                  buttonVariants({ size: "sm" }),
                  "flex-1 text-center bg-emerald-600 hover:bg-emerald-700"
                )}
              >
                Register
              </Link>
            </div>
          )}
        </div>
      )}
    </header>
  );
}
