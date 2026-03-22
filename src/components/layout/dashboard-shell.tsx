"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

interface DashboardTab {
  label: string;
  href: string;
  icon?: React.ReactNode;
}

interface DashboardShellProps {
  tabs: DashboardTab[];
  children: React.ReactNode;
  title: string;
  description?: string;
}

export function DashboardShell({ tabs, children, title, description }: DashboardShellProps) {
  const pathname = usePathname();

  return (
    <div className="flex-1">
      {/* Header */}
      <div className="border-b bg-gradient-to-r from-emerald-50 to-teal-50">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-2xl font-bold text-gray-900">{title}</h1>
          {description && (
            <p className="mt-1 text-sm text-muted-foreground">{description}</p>
          )}
        </div>

        {/* Tab Navigation */}
        <div className="container mx-auto px-4">
          <nav className="-mb-px flex gap-6 overflow-x-auto">
            {tabs.map((tab) => {
              const isActive =
                pathname === tab.href ||
                (tab.href !== tabs[0].href && pathname.startsWith(tab.href));
              return (
                <Link
                  key={tab.href}
                  href={tab.href}
                  className={cn(
                    "flex items-center gap-2 whitespace-nowrap border-b-2 px-1 py-3 text-sm font-medium transition-colors",
                    isActive
                      ? "border-emerald-600 text-emerald-600"
                      : "border-transparent text-muted-foreground hover:border-gray-300 hover:text-foreground"
                  )}
                >
                  {tab.icon}
                  {tab.label}
                </Link>
              );
            })}
          </nav>
        </div>
      </div>

      {/* Content */}
      <div className="container mx-auto px-4 py-6">{children}</div>
    </div>
  );
}
