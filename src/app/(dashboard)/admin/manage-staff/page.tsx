"use client";

import { useEffect, useState, useCallback } from "react";
import { DataTable } from "@/components/shared/data-table";
import { ConfirmDialog } from "@/components/shared/confirm-dialog";
import { Button, buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Badge } from "@/components/ui/badge";
import { Pencil, Trash2 } from "lucide-react";
import { toast } from "sonner";
import Link from "next/link";

interface Staff {
  staffNumber: number;
  userId: string;
  firstName: string;
  lastName: string;
  email: string;
  workPhoneNumber: string | null;
  position: string | null;
  department: string | null;
  status: string;
  hireDate: string | null;
  [key: string]: unknown;
}

export default function ManageStaffPage() {
  const [data, setData] = useState<Staff[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(true);
  const [searchField, setSearchField] = useState("");
  const [searchValue, setSearchValue] = useState("");
  const [deleteTarget, setDeleteTarget] = useState<Staff | null>(null);
  const [deleting, setDeleting] = useState(false);

  const fetchData = useCallback(async () => {
    setLoading(true);
    const params = new URLSearchParams({ page: String(page) });
    if (searchField && searchValue) {
      params.set("field", searchField);
      params.set("q", searchValue);
    }
    const res = await fetch(`/api/staff?${params}`);
    const json = await res.json();
    setData(json.items || []);
    setTotalPages(json.totalPages || 1);
    setLoading(false);
  }, [page, searchField, searchValue]);

  useEffect(() => { fetchData(); }, [fetchData]);

  async function handleDelete() {
    if (!deleteTarget) return;
    setDeleting(true);
    const res = await fetch(`/api/staff/${deleteTarget.staffNumber}`, { method: "DELETE" });
    if (res.ok) {
      toast.success("Staff member deleted");
      fetchData();
    } else {
      toast.error("Failed to delete");
    }
    setDeleting(false);
    setDeleteTarget(null);
  }

  const columns = [
    { key: "firstName", header: "First Name" },
    { key: "lastName", header: "Last Name" },
    { key: "email", header: "Email" },
    { key: "position", header: "Position" },
    { key: "department", header: "Department" },
    {
      key: "status",
      header: "Status",
      render: (item: Staff) => (
        <Badge variant={item.status === "active" ? "default" : "secondary"} className="capitalize">
          {item.status}
        </Badge>
      ),
    },
  ];

  const searchFields = [
    { value: "first_name", label: "First Name" },
    { value: "last_name", label: "Last Name" },
    { value: "email", label: "Email" },
    { value: "position", label: "Position" },
    { value: "department", label: "Department" },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">Staff Members</h2>
        <Link href="/register/staff" className={cn(buttonVariants(), "bg-emerald-600 hover:bg-emerald-700")}>
          Add Staff
        </Link>
      </div>

      <DataTable
        columns={columns}
        data={data}
        totalPages={totalPages}
        currentPage={page}
        onPageChange={setPage}
        searchFields={searchFields}
        onSearch={(f, v) => { setSearchField(f); setSearchValue(v); setPage(1); }}
        loading={loading}
        actions={(item: Staff) => (
          <div className="flex gap-1">
            <Link href={`/admin/manage-staff?edit=${item.staffNumber}`} className={cn(buttonVariants({ variant: "ghost", size: "icon" }), "h-8 w-8")}>
                <Pencil className="h-3.5 w-3.5" />
            </Link>
            <Button
              variant="ghost"
              size="icon"
              className="h-8 w-8 text-red-500"
              onClick={() => setDeleteTarget(item)}
            >
              <Trash2 className="h-3.5 w-3.5" />
            </Button>
          </div>
        )}
      />

      <ConfirmDialog
        open={!!deleteTarget}
        onOpenChange={() => setDeleteTarget(null)}
        title="Delete Staff Member"
        description={`Are you sure you want to delete ${deleteTarget?.firstName} ${deleteTarget?.lastName}? This action cannot be undone.`}
        onConfirm={handleDelete}
        loading={deleting}
      />
    </div>
  );
}
