"use client";

import { useEffect, useState, use } from "react";
import { ImageCarousel } from "@/components/guides/image-carousel";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { ArrowLeft } from "lucide-react";
import Link from "next/link";

interface GuideDetail {
  agricultureId: number;
  itemType: string;
  commonName: string;
  scientificName: string | null;
  keyCharacteristics: string | null;
  biology: string | null;
  impacts: string | null;
  control: string | null;
  images: { imageId: number; imagePath: string; isPrimary: boolean }[];
}

export default function GuideDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  const [guide, setGuide] = useState<GuideDetail | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/guides/${id}`)
      .then((r) => r.json())
      .then((data) => {
        setGuide(data);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <div className="py-12 text-center text-muted-foreground">Loading...</div>;
  if (!guide) return <div className="py-12 text-center text-muted-foreground">Guide not found</div>;

  const sections = [
    { title: "Key Characteristics", content: guide.keyCharacteristics },
    { title: "Biology", content: guide.biology },
    { title: "Impacts", content: guide.impacts },
    { title: "Control", content: guide.control },
  ];

  return (
    <div className="max-w-4xl space-y-6">
      <Link href="/agronomist/guides" className={cn(buttonVariants({ variant: "ghost", size: "sm" }))}>
          <ArrowLeft className="h-4 w-4 mr-1" /> Back to Guides
      </Link>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Image Carousel */}
        <ImageCarousel images={guide.images} alt={guide.commonName} />

        {/* Basic Info */}
        <div className="space-y-4">
          <div>
            <div className="flex items-center gap-2 mb-2">
              <Badge variant={guide.itemType === "pest" ? "destructive" : "secondary"}>
                {guide.itemType}
              </Badge>
            </div>
            <h2 className="text-2xl font-bold">{guide.commonName}</h2>
            {guide.scientificName && (
              <p className="text-lg text-muted-foreground italic">{guide.scientificName}</p>
            )}
          </div>
        </div>
      </div>

      {/* Detail Sections */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {sections.map(
          (section) =>
            section.content && (
              <Card key={section.title}>
                <CardHeader className="pb-2">
                  <CardTitle className="text-base">{section.title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground whitespace-pre-wrap">
                    {section.content}
                  </p>
                </CardContent>
              </Card>
            )
        )}
      </div>
    </div>
  );
}
