"use client";

import { useEffect, useState, useCallback } from "react";
import { GuideCard } from "@/components/guides/guide-card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { ChevronLeft, ChevronRight, Search } from "lucide-react";

interface GuideImage {
  imageId: number;
  imagePath: string;
  isPrimary: boolean;
}

interface Guide {
  agricultureId: number;
  itemType: string;
  commonName: string;
  scientificName: string | null;
  images: GuideImage[];
}

export default function AgronomistGuidesPage() {
  const [guides, setGuides] = useState<Guide[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(true);
  const [typeFilter, setTypeFilter] = useState<string>("all");
  const [searchValue, setSearchValue] = useState("");

  const fetchGuides = useCallback(async () => {
    setLoading(true);
    const params = new URLSearchParams({ page: String(page), perPage: "12" });
    if (typeFilter !== "all") params.set("type", typeFilter);
    if (searchValue) {
      params.set("field", "common_name");
      params.set("q", searchValue);
    }
    const res = await fetch(`/api/guides?${params}`);
    const json = await res.json();
    setGuides(json.items || []);
    setTotalPages(json.totalPages || 1);
    setLoading(false);
  }, [page, typeFilter, searchValue]);

  useEffect(() => { fetchGuides(); }, [fetchGuides]);

  return (
    <div className="space-y-6">
      {/* Filters */}
      <div className="flex items-center gap-3 flex-wrap">
        <Select value={typeFilter} onValueChange={(v) => { if (v) { setTypeFilter(v); setPage(1); } }}>
          <SelectTrigger className="w-[140px]">
            <SelectValue />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">All Types</SelectItem>
            <SelectItem value="pest">Pests</SelectItem>
            <SelectItem value="weed">Weeds</SelectItem>
          </SelectContent>
        </Select>
        <div className="relative flex-1 max-w-sm">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search by name..."
            value={searchValue}
            onChange={(e) => setSearchValue(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter") { setPage(1); fetchGuides(); } }}
            className="pl-9"
          />
        </div>
        <Button
          variant="secondary"
          size="sm"
          onClick={() => { setPage(1); fetchGuides(); }}
        >
          Search
        </Button>
      </div>

      {/* Grid */}
      {loading ? (
        <div className="py-12 text-center text-muted-foreground">Loading guides...</div>
      ) : guides.length === 0 ? (
        <div className="py-12 text-center text-muted-foreground">No guides found.</div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {guides.map((guide) => (
            <GuideCard
              key={guide.agricultureId}
              agricultureId={guide.agricultureId}
              itemType={guide.itemType}
              commonName={guide.commonName}
              scientificName={guide.scientificName}
              images={guide.images}
              detailHref={`/agronomist/guides/${guide.agricultureId}`}
            />
          ))}
        </div>
      )}

      {/* Pagination */}
      {totalPages > 1 && (
        <div className="flex items-center justify-between">
          <p className="text-sm text-muted-foreground">Page {page} of {totalPages}</p>
          <div className="flex gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setPage((p) => p - 1)}
              disabled={page <= 1}
            >
              <ChevronLeft className="h-4 w-4" /> Previous
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setPage((p) => p + 1)}
              disabled={page >= totalPages}
            >
              Next <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
