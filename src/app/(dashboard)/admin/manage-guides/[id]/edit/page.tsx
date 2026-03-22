"use client";

import { useEffect, useState, use } from "react";
import { GuideForm } from "@/components/guides/guide-form";

export default function EditGuidePage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  const [guide, setGuide] = useState<null | Record<string, unknown>>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/guides/${id}`)
      .then((r) => r.json())
      .then((data) => {
        setGuide(data);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <div className="py-8 text-center text-muted-foreground">Loading...</div>;
  if (!guide) return <div className="py-8 text-center text-muted-foreground">Guide not found</div>;

  return (
    <div className="max-w-3xl">
      <h2 className="text-lg font-semibold mb-6">Edit Guide</h2>
      <GuideForm
        initialData={{
          itemType: guide.itemType as string,
          commonName: guide.commonName as string,
          scientificName: guide.scientificName as string | null,
          keyCharacteristics: guide.keyCharacteristics as string | null,
          biology: guide.biology as string | null,
          impacts: guide.impacts as string | null,
          control: guide.control as string | null,
          images: (guide.images as { imagePath: string; isPrimary: boolean }[]) || [],
        }}
        submitUrl={`/api/guides/${id}`}
        method="PUT"
        returnUrl="/admin/manage-guides"
      />
    </div>
  );
}
