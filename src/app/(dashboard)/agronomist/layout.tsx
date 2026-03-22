"use client";

import { DashboardShell } from "@/components/layout/dashboard-shell";
import { User, BookOpen } from "lucide-react";

const agronomistTabs = [
  { label: "My Profile", href: "/agronomist", icon: <User className="h-4 w-4" /> },
  {
    label: "View Guides",
    href: "/agronomist/guides",
    icon: <BookOpen className="h-4 w-4" />,
  },
];

export default function AgronomistLayout({ children }: { children: React.ReactNode }) {
  return (
    <DashboardShell
      title="Agronomist Dashboard"
      description="Browse and view biosecurity guides for agricultural pests and weeds"
      tabs={agronomistTabs}
    >
      {children}
    </DashboardShell>
  );
}
