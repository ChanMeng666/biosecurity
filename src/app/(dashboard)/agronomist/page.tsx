"use client";

import { useEffect, useState } from "react";
import { useSession } from "@/lib/auth/client";
import { ProfileEditor } from "@/components/users/profile-editor";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Sprout } from "lucide-react";

interface AgronomistProfile {
  agronomistId: number;
  firstName: string;
  lastName: string;
  email: string;
  phoneNumber: string | null;
  address: string | null;
  dateJoined: string | null;
  status: string;
}

export default function AgronomistProfilePage() {
  const { data: session } = useSession();
  const [profile, setProfile] = useState<AgronomistProfile | null>(null);

  useEffect(() => {
    fetch("/api/profile")
      .then((r) => r.json())
      .then((data) => setProfile(data.profile));
  }, []);

  async function handleUpdate(field: string, value: string) {
    const res = await fetch("/api/profile", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ field, value }),
    });
    if (!res.ok) throw new Error("Update failed");
    setProfile((prev) => (prev ? { ...prev, [camelCase(field)]: value } : prev));
  }

  if (!profile) return <div className="py-8 text-center text-muted-foreground">Loading...</div>;

  const fields = [
    { key: "first_name", label: "First Name", value: profile.firstName },
    { key: "last_name", label: "Last Name", value: profile.lastName },
    { key: "email", label: "Email", value: profile.email },
    { key: "phone_number", label: "Phone", value: profile.phoneNumber || "" },
    { key: "address", label: "Address", value: profile.address || "" },
  ];

  return (
    <div className="space-y-6">
      <Card>
        <CardHeader className="flex flex-row items-center gap-4">
          <div className="flex h-12 w-12 items-center justify-center rounded-full bg-emerald-100">
            <Sprout className="h-6 w-6 text-emerald-600" />
          </div>
          <div>
            <CardTitle>{session?.user?.name}</CardTitle>
            <div className="flex gap-2 mt-1">
              <Badge className="bg-emerald-100 text-emerald-700">Agronomist</Badge>
              <Badge variant="outline" className="capitalize">{profile.status}</Badge>
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground">
            Username: {session?.user?.username} &middot; Joined:{" "}
            {profile.dateJoined ? new Date(profile.dateJoined).toLocaleDateString() : "—"}
          </p>
        </CardContent>
      </Card>
      <ProfileEditor fields={fields} onUpdate={handleUpdate} />
    </div>
  );
}

function camelCase(s: string) {
  return s.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
}
