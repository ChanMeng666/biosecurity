"use client";

import { DashboardShell } from "@/components/layout/dashboard-shell";
import { User, Users, Sprout, BookOpen } from "lucide-react";

const adminTabs = [
  { label: "My Profile", href: "/admin", icon: <User className="h-4 w-4" /> },
  { label: "Manage Staff", href: "/admin/manage-staff", icon: <Users className="h-4 w-4" /> },
  {
    label: "Manage Agronomists",
    href: "/admin/manage-agronomists",
    icon: <Sprout className="h-4 w-4" />,
  },
  {
    label: "Manage Guides",
    href: "/admin/manage-guides",
    icon: <BookOpen className="h-4 w-4" />,
  },
];

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  return (
    <DashboardShell
      title="Administrator Dashboard"
      description="Manage staff, agronomists, and biosecurity guides"
      tabs={adminTabs}
    >
      {children}
    </DashboardShell>
  );
}
