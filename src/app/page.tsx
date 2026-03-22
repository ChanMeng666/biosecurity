import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Shield, Bug, Leaf, Users, BookOpen, Search } from "lucide-react";

export default function HomePage() {
  return (
    <div className="flex-1">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-emerald-600 via-emerald-700 to-teal-800 text-white">
        <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHZpZXdCb3g9IjAgMCA2MCA2MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPjxnIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iMC4wNSI+PHBhdGggZD0iTTM2IDM0djZoLTZ2LTZIMTJ2Nmg2djZoNnYtNmg2di02aC02em0wLTMwdjZoLTZ2LTZIMTJWMTBoNnY2aDZ2LTZoNlYwaDZWNGgtNnoiLz48L2c+PC9nPjwvc3ZnPg==')] opacity-30" />
        <div className="container mx-auto px-4 py-24 md:py-32 relative">
          <div className="max-w-3xl">
            <div className="flex items-center gap-3 mb-6">
              <Shield className="h-10 w-10" />
              <span className="text-emerald-200 text-sm font-medium uppercase tracking-wider">
                Agricultural Biosecurity
              </span>
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold leading-tight mb-6">
              Biosecurity Guide for Agricultural Pests & Weeds
            </h1>
            <p className="text-lg md:text-xl text-emerald-100 mb-8 max-w-2xl">
              A comprehensive digital platform for identifying, understanding, and managing
              agricultural pests and weeds. Built for agronomists, staff, and administrators.
            </p>
            <div className="flex flex-wrap gap-4">
              <Link href="/register/agronomist" className={cn(buttonVariants({ size: "lg" }), "bg-white text-emerald-700 hover:bg-emerald-50")}>
                Get Started
              </Link>
              <Link href="/login" className={cn(buttonVariants({ size: "lg", variant: "outline" }), "border-white/30 text-white hover:bg-white/10")}>
                Sign In
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">Platform Features</h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Our platform provides tools for managing biosecurity information across
              different user roles with specialized capabilities.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto">
            <Card className="border-0 shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-red-100 mb-2">
                  <Bug className="h-6 w-6 text-red-600" />
                </div>
                <CardTitle className="text-lg">Pest Identification</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Detailed guides on agricultural pests including key characteristics,
                  biology, impacts, and control methods with visual references.
                </p>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-emerald-100 mb-2">
                  <Leaf className="h-6 w-6 text-emerald-600" />
                </div>
                <CardTitle className="text-lg">Weed Management</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Comprehensive weed identification and control guides to protect
                  agricultural productivity and biodiversity.
                </p>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-blue-100 mb-2">
                  <Users className="h-6 w-6 text-blue-600" />
                </div>
                <CardTitle className="text-lg">Role-Based Access</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Three distinct user roles — administrators, staff, and agronomists — each
                  with tailored dashboards and capabilities.
                </p>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-purple-100 mb-2">
                  <BookOpen className="h-6 w-6 text-purple-600" />
                </div>
                <CardTitle className="text-lg">Guide Library</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Browse and search through a growing library of biosecurity guides with
                  images, scientific data, and management strategies.
                </p>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-amber-100 mb-2">
                  <Search className="h-6 w-6 text-amber-600" />
                </div>
                <CardTitle className="text-lg">Smart Search</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Powerful search capabilities across all guides with field-specific
                  filtering and case-insensitive matching.
                </p>
              </CardContent>
            </Card>

            <Card className="border-0 shadow-md hover:shadow-lg transition-shadow">
              <CardHeader>
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-teal-100 mb-2">
                  <Shield className="h-6 w-6 text-teal-600" />
                </div>
                <CardTitle className="text-lg">Secure Platform</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  Built with modern security practices including server-side sessions,
                  encrypted passwords, and role-based authorization.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-2xl font-bold mb-4">Ready to Get Started?</h2>
          <p className="text-muted-foreground mb-8 max-w-xl mx-auto">
            Register as an agronomist to browse the guide library, or sign in if you
            already have an account.
          </p>
          <div className="flex justify-center gap-4">
            <Link href="/register/agronomist" className={cn(buttonVariants({ size: "lg" }), "bg-emerald-600 hover:bg-emerald-700")}>
              Register Now
            </Link>
            <Link href="/login" className={buttonVariants({ size: "lg", variant: "outline" })}>
              Sign In
            </Link>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t bg-gray-50 py-8">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <Shield className="h-5 w-5 text-emerald-600" />
              <span className="font-semibold">Biosecurity Guide</span>
            </div>
            <p className="text-sm text-muted-foreground">
              &copy; {new Date().getFullYear()} Biosecurity Guide for Agricultural Pests and Weeds.
              All rights reserved.
            </p>
            <Link
              href="/sources"
              className="text-sm text-muted-foreground hover:text-foreground"
            >
              Sources & Credits
            </Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
