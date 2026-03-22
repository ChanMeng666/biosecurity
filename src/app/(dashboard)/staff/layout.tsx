"use client";

import { DashboardShell } from "@/components/layout/dashboard-shell";
import { User, BookOpen, Sprout } from "lucide-react";

const staffTabs = [
  { label: "My Profile", href: "/staff", icon: <User className="h-4 w-4" /> },
  {
    label: "Manage Guides",
    href: "/staff/manage-guides",
    icon: <BookOpen className="h-4 w-4" />,
  },
  {
    label: "View Agronomists",
    href: "/staff/view-agronomists",
    icon: <Sprout className="h-4 w-4" />,
  },
];

export default function StaffLayout({ children }: { children: React.ReactNode }) {
  return (
    <DashboardShell
      title="Staff Dashboard"
      description="Manage biosecurity guides and view agronomists"
      tabs={staffTabs}
    >
      {children}
    </DashboardShell>
  );
}
