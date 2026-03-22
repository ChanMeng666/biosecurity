"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Loader2, Plus, Trash2 } from "lucide-react";
import { toast } from "sonner";

interface ImageInput {
  imagePath: string;
  isPrimary: boolean;
}

interface GuideFormProps {
  initialData?: {
    itemType: string;
    commonName: string;
    scientificName?: string | null;
    keyCharacteristics?: string | null;
    biology?: string | null;
    impacts?: string | null;
    control?: string | null;
    images?: ImageInput[];
  };
  submitUrl: string;
  method: "POST" | "PUT";
  returnUrl: string;
}

export function GuideForm({ initialData, submitUrl, method, returnUrl }: GuideFormProps) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [images, setImages] = useState<ImageInput[]>(
    initialData?.images || [{ imagePath: "", isPrimary: true }]
  );

  function addImage() {
    setImages([...images, { imagePath: "", isPrimary: false }]);
  }

  function removeImage(idx: number) {
    setImages(images.filter((_, i) => i !== idx));
  }

  function updateImage(idx: number, field: keyof ImageInput, value: string | boolean) {
    const updated = [...images];
    if (field === "isPrimary" && value === true) {
      updated.forEach((img) => (img.isPrimary = false));
    }
    updated[idx] = { ...updated[idx], [field]: value };
    setImages(updated);
  }

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);

    const fd = new FormData(e.currentTarget);
    const payload = {
      itemType: fd.get("itemType"),
      commonName: fd.get("commonName"),
      scientificName: fd.get("scientificName") || undefined,
      keyCharacteristics: fd.get("keyCharacteristics") || undefined,
      biology: fd.get("biology") || undefined,
      impacts: fd.get("impacts") || undefined,
      control: fd.get("control") || undefined,
      images: images.filter((img) => img.imagePath.trim()),
    };

    const res = await fetch(submitUrl, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const err = await res.json();
      toast.error(err.error?.fieldErrors ? "Validation error" : "Failed to save");
      setLoading(false);
      return;
    }

    toast.success(method === "POST" ? "Guide created" : "Guide updated");
    router.push(returnUrl);
    router.refresh();
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="space-y-6">
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Guide Information</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="itemType">Type</Label>
                <Select name="itemType" defaultValue={initialData?.itemType || "pest"}>
                  <SelectTrigger>
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="pest">Pest</SelectItem>
                    <SelectItem value="weed">Weed</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              <div className="space-y-2">
                <Label htmlFor="commonName">Common Name</Label>
                <Input
                  id="commonName"
                  name="commonName"
                  defaultValue={initialData?.commonName}
                  required
                />
              </div>
            </div>
            <div className="space-y-2">
              <Label htmlFor="scientificName">Scientific Name</Label>
              <Input
                id="scientificName"
                name="scientificName"
                defaultValue={initialData?.scientificName || ""}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="keyCharacteristics">Key Characteristics</Label>
              <Textarea
                id="keyCharacteristics"
                name="keyCharacteristics"
                rows={3}
                defaultValue={initialData?.keyCharacteristics || ""}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="biology">Biology</Label>
              <Textarea
                id="biology"
                name="biology"
                rows={3}
                defaultValue={initialData?.biology || ""}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="impacts">Impacts</Label>
              <Textarea
                id="impacts"
                name="impacts"
                rows={3}
                defaultValue={initialData?.impacts || ""}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="control">Control</Label>
              <Textarea
                id="control"
                name="control"
                rows={3}
                defaultValue={initialData?.control || ""}
              />
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between">
            <CardTitle className="text-lg">Images</CardTitle>
            <Button type="button" variant="outline" size="sm" onClick={addImage}>
              <Plus className="h-4 w-4 mr-1" /> Add Image
            </Button>
          </CardHeader>
          <CardContent className="space-y-3">
            {images.map((img, idx) => (
              <div key={idx} className="flex items-center gap-3">
                <Input
                  placeholder="Image URL"
                  value={img.imagePath}
                  onChange={(e) => updateImage(idx, "imagePath", e.target.value)}
                  className="flex-1"
                />
                <label className="flex items-center gap-1.5 text-sm whitespace-nowrap">
                  <input
                    type="radio"
                    name="primaryImage"
                    checked={img.isPrimary}
                    onChange={() => updateImage(idx, "isPrimary", true)}
                    className="accent-emerald-600"
                  />
                  Primary
                </label>
                <Button
                  type="button"
                  variant="ghost"
                  size="icon"
                  className="h-8 w-8 text-red-500"
                  onClick={() => removeImage(idx)}
                >
                  <Trash2 className="h-4 w-4" />
                </Button>
              </div>
            ))}
          </CardContent>
        </Card>

        <div className="flex justify-end gap-3">
          <Button
            type="button"
            variant="outline"
            onClick={() => router.back()}
          >
            Cancel
          </Button>
          <Button
            type="submit"
            className="bg-emerald-600 hover:bg-emerald-700"
            disabled={loading}
          >
            {loading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            {method === "POST" ? "Create Guide" : "Update Guide"}
          </Button>
        </div>
      </div>
    </form>
  );
}
