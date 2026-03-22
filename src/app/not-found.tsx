import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import { FileQuestion } from "lucide-react";

export default function NotFound() {
  return (
    <div className="flex-1 flex items-center justify-center px-4 py-24">
      <div className="text-center">
        <FileQuestion className="h-16 w-16 text-muted-foreground mx-auto mb-4" />
        <h1 className="text-4xl font-bold mb-2">404</h1>
        <p className="text-muted-foreground mb-6">
          The page you&apos;re looking for doesn&apos;t exist or has been moved.
        </p>
        <Link href="/" className={buttonVariants()}>
          Go Home
        </Link>
      </div>
    </div>
  );
}
