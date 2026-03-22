"use client";

import { useEffect, useState, useCallback } from "react";
import { DataTable } from "@/components/shared/data-table";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Badge } from "@/components/ui/badge";
import { Plus, Pencil } from "lucide-react";
import Link from "next/link";

interface Guide {
  agricultureId: number;
  itemType: string;
  commonName: string;
  scientificName: string | null;
  [key: string]: unknown;
}

export default function StaffManageGuidesPage() {
  const [data, setData] = useState<Guide[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(true);
  const [searchField, setSearchField] = useState("");
  const [searchValue, setSearchValue] = useState("");

  const fetchData = useCallback(async () => {
    setLoading(true);
    const params = new URLSearchParams({ page: String(page) });
    if (searchField && searchValue) {
      params.set("field", searchField);
      params.set("q", searchValue);
    }
    const res = await fetch(`/api/guides?${params}`);
    const json = await res.json();
    setData(json.items || []);
    setTotalPages(json.totalPages || 1);
    setLoading(false);
  }, [page, searchField, searchValue]);

  useEffect(() => { fetchData(); }, [fetchData]);

  const columns = [
    {
      key: "itemType",
      header: "Type",
      render: (item: Guide) => (
        <Badge variant={item.itemType === "pest" ? "destructive" : "secondary"}>
          {item.itemType}
        </Badge>
      ),
    },
    { key: "commonName", header: "Common Name" },
    { key: "scientificName", header: "Scientific Name" },
  ];

  const searchFields = [
    { value: "common_name", label: "Common Name" },
    { value: "scientific_name", label: "Scientific Name" },
    { value: "key_characteristics", label: "Characteristics" },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">Agriculture Guides</h2>
        <Link href="/staff/manage-guides/add" className={cn(buttonVariants(), "bg-emerald-600 hover:bg-emerald-700")}>
            <Plus className="h-4 w-4 mr-1" /> Add Guide
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
        actions={(item: Guide) => (
          <Link href={`/staff/manage-guides/${item.agricultureId}/edit`} className={cn(buttonVariants({ variant: "ghost", size: "icon" }), "h-8 w-8")}>
              <Pencil className="h-3.5 w-3.5" />
          </Link>
        )}
      />
    </div>
  );
}
