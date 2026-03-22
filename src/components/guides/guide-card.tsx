import Link from "next/link";
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { buttonVariants } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { ArrowRight, Bug, Leaf } from "lucide-react";

interface GuideImage {
  imageId: number;
  imagePath: string;
  isPrimary: boolean;
}

interface GuideCardProps {
  agricultureId: number;
  itemType: string;
  commonName: string;
  scientificName: string | null;
  images: GuideImage[];
  detailHref: string;
}

export function GuideCard({
  itemType,
  commonName,
  scientificName,
  images,
  detailHref,
}: GuideCardProps) {
  const primaryImage = images.find((img) => img.isPrimary) || images[0];

  return (
    <Card className="overflow-hidden group hover:shadow-lg transition-shadow">
      <div className="aspect-[4/3] bg-muted relative overflow-hidden">
        {primaryImage ? (
          <img
            src={primaryImage.imagePath}
            alt={commonName}
            className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-300"
          />
        ) : (
          <div className="flex items-center justify-center h-full">
            {itemType === "pest" ? (
              <Bug className="h-12 w-12 text-muted-foreground/40" />
            ) : (
              <Leaf className="h-12 w-12 text-muted-foreground/40" />
            )}
          </div>
        )}
      </div>
      <CardHeader className="pb-2">
        <div className="flex items-center justify-between">
          <h3 className="font-semibold text-base line-clamp-1">{commonName}</h3>
          <Badge
            variant={itemType === "pest" ? "destructive" : "secondary"}
            className="ml-2 shrink-0"
          >
            {itemType}
          </Badge>
        </div>
      </CardHeader>
      <CardContent className="pb-2">
        {scientificName && (
          <p className="text-sm text-muted-foreground italic line-clamp-1">
            {scientificName}
          </p>
        )}
      </CardContent>
      <CardFooter>
        <Link href={detailHref} className={cn(buttonVariants({ variant: "ghost", size: "sm" }), "ml-auto text-emerald-600")}>
            View Details <ArrowRight className="ml-1 h-4 w-4" />
        </Link>
      </CardFooter>
    </Card>
  );
}
