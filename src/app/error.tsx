"use client";

import { Button } from "@/components/ui/button";
import { AlertTriangle } from "lucide-react";

export default function Error({
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="flex-1 flex items-center justify-center px-4 py-24">
      <div className="text-center">
        <AlertTriangle className="h-16 w-16 text-destructive mx-auto mb-4" />
        <h1 className="text-3xl font-bold mb-2">Something went wrong</h1>
        <p className="text-muted-foreground mb-6">
          An unexpected error occurred. Please try again.
        </p>
        <Button onClick={reset}>Try Again</Button>
      </div>
    </div>
  );
}
