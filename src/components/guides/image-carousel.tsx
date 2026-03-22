"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";

interface ImageCarouselProps {
  images: { imageId: number; imagePath: string; isPrimary: boolean }[];
  alt: string;
}

export function ImageCarousel({ images, alt }: ImageCarouselProps) {
  const sorted = [...images].sort((a, b) => (b.isPrimary ? 1 : 0) - (a.isPrimary ? 1 : 0));
  const [current, setCurrent] = useState(0);

  if (sorted.length === 0) {
    return (
      <div className="aspect-video bg-muted rounded-lg flex items-center justify-center">
        <p className="text-muted-foreground">No images available</p>
      </div>
    );
  }

  return (
    <div className="relative aspect-video bg-muted rounded-lg overflow-hidden">
      <img
        src={sorted[current].imagePath}
        alt={`${alt} - Image ${current + 1}`}
        className="object-cover w-full h-full"
      />
      {sorted.length > 1 && (
        <>
          <Button
            variant="secondary"
            size="icon"
            className="absolute left-2 top-1/2 -translate-y-1/2 h-8 w-8 rounded-full opacity-80 hover:opacity-100"
            onClick={() => setCurrent((c) => (c - 1 + sorted.length) % sorted.length)}
          >
            <ChevronLeft className="h-4 w-4" />
          </Button>
          <Button
            variant="secondary"
            size="icon"
            className="absolute right-2 top-1/2 -translate-y-1/2 h-8 w-8 rounded-full opacity-80 hover:opacity-100"
            onClick={() => setCurrent((c) => (c + 1) % sorted.length)}
          >
            <ChevronRight className="h-4 w-4" />
          </Button>
          <div className="absolute bottom-2 left-1/2 -translate-x-1/2 flex gap-1.5">
            {sorted.map((_, idx) => (
              <button
                key={idx}
                onClick={() => setCurrent(idx)}
                className={`h-2 w-2 rounded-full transition-colors ${
                  idx === current ? "bg-white" : "bg-white/50"
                }`}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
}
