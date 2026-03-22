"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { signUp } from "@/lib/auth/client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Sprout, Loader2 } from "lucide-react";
import { toast } from "sonner";

export default function RegisterAgronomistPage() {
  const router = useRouter();
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);

    const fd = new FormData(e.currentTarget);
    const firstName = fd.get("firstName") as string;
    const lastName = fd.get("lastName") as string;

    const { error } = await signUp.email({
      email: fd.get("email") as string,
      password: fd.get("password") as string,
      name: `${firstName} ${lastName}`,
      username: fd.get("username") as string,
      role: "agronomist",
      status: "active",
    });

    if (error) {
      toast.error(error.message || "Registration failed");
      setLoading(false);
      return;
    }

    // Create agronomist profile
    const res = await fetch("/api/agronomists", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        firstName,
        lastName,
        email: fd.get("email") as string,
        phoneNumber: fd.get("phoneNumber") as string,
        address: fd.get("address") as string,
      }),
    });

    if (!res.ok) {
      toast.error("Failed to create agronomist profile");
      setLoading(false);
      return;
    }

    toast.success("Registration successful!");
    router.push("/agronomist");
    router.refresh();
  }

  return (
    <div className="flex-1 flex items-center justify-center px-4 py-12 bg-gradient-to-br from-emerald-50 via-white to-teal-50">
      <Card className="w-full max-w-lg shadow-lg">
        <CardHeader className="text-center space-y-2">
          <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-emerald-100">
            <Sprout className="h-6 w-6 text-emerald-600" />
          </div>
          <CardTitle className="text-2xl">Register as Agronomist</CardTitle>
          <CardDescription>
            Create your account to browse biosecurity guides
          </CardDescription>
        </CardHeader>
        <form onSubmit={handleSubmit}>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="firstName">First Name</Label>
                <Input id="firstName" name="firstName" required />
              </div>
              <div className="space-y-2">
                <Label htmlFor="lastName">Last Name</Label>
                <Input id="lastName" name="lastName" required />
              </div>
            </div>
            <div className="space-y-2">
              <Label htmlFor="username">Username</Label>
              <Input id="username" name="username" required minLength={3} />
            </div>
            <div className="space-y-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" name="email" type="email" required />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" name="password" type="password" required minLength={8} />
              <p className="text-xs text-muted-foreground">
                Min 8 chars with uppercase, lowercase, number, and special character
              </p>
            </div>
            <div className="space-y-2">
              <Label htmlFor="phoneNumber">Phone Number</Label>
              <Input id="phoneNumber" name="phoneNumber" />
            </div>
            <div className="space-y-2">
              <Label htmlFor="address">Address</Label>
              <Textarea id="address" name="address" rows={2} />
            </div>
          </CardContent>
          <CardFooter className="flex flex-col gap-4">
            <Button
              type="submit"
              className="w-full bg-emerald-600 hover:bg-emerald-700"
              disabled={loading}
            >
              {loading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
              Create Account
            </Button>
            <p className="text-sm text-muted-foreground text-center">
              Already have an account?{" "}
              <Link href="/login" className="text-emerald-600 hover:underline font-medium">
                Sign In
              </Link>
            </p>
          </CardFooter>
        </form>
      </Card>
    </div>
  );
}
