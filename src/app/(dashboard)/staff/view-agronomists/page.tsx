"use client";

import { useEffect, useState, useCallback } from "react";
import { DataTable } from "@/components/shared/data-table";
import { Badge } from "@/components/ui/badge";

interface Agronomist {
  agronomistId: number;
  firstName: string;
  lastName: string;
  email: string;
  phoneNumber: string | null;
  address: string | null;
  status: string;
  [key: string]: unknown;
}

export default function StaffViewAgronomistsPage() {
  const [data, setData] = useState<Agronomist[]>([]);
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
    const res = await fetch(`/api/agronomists?${params}`);
    const json = await res.json();
    setData(json.items || []);
    setTotalPages(json.totalPages || 1);
    setLoading(false);
  }, [page, searchField, searchValue]);

  useEffect(() => { fetchData(); }, [fetchData]);

  const columns = [
    { key: "firstName", header: "First Name" },
    { key: "lastName", header: "Last Name" },
    { key: "email", header: "Email" },
    { key: "phoneNumber", header: "Phone" },
    { key: "address", header: "Address" },
    {
      key: "status",
      header: "Status",
      render: (item: Agronomist) => (
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
  ];

  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">Agronomists</h2>
      <DataTable
        columns={columns}
        data={data}
        totalPages={totalPages}
        currentPage={page}
        onPageChange={setPage}
        searchFields={searchFields}
        onSearch={(f, v) => { setSearchField(f); setSearchValue(v); setPage(1); }}
        loading={loading}
      />
    </div>
  );
}
