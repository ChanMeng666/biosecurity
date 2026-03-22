"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Pencil, Check, X } from "lucide-react";
import { toast } from "sonner";

interface ProfileField {
  key: string;
  label: string;
  value: string;
  editable?: boolean;
}

interface ProfileEditorProps {
  fields: ProfileField[];
  onUpdate: (field: string, value: string) => Promise<void>;
}

export function ProfileEditor({ fields, onUpdate }: ProfileEditorProps) {
  const [editingField, setEditingField] = useState<string | null>(null);
  const [editValue, setEditValue] = useState("");
  const [loading, setLoading] = useState(false);

  function startEdit(field: ProfileField) {
    setEditingField(field.key);
    setEditValue(field.value);
  }

  async function saveEdit(key: string) {
    setLoading(true);
    try {
      await onUpdate(key, editValue);
      toast.success("Profile updated");
      setEditingField(null);
    } catch {
      toast.error("Failed to update");
    }
    setLoading(false);
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-lg">Profile Information</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {fields.map((field) => (
          <div key={field.key} className="flex items-center gap-4">
            <Label className="w-40 text-sm font-medium text-muted-foreground shrink-0">
              {field.label}
            </Label>
            {editingField === field.key ? (
              <div className="flex items-center gap-2 flex-1">
                <Input
                  value={editValue}
                  onChange={(e) => setEditValue(e.target.value)}
                  className="flex-1"
                  autoFocus
                />
                <Button
                  size="icon"
                  variant="ghost"
                  className="h-8 w-8 text-emerald-600"
                  onClick={() => saveEdit(field.key)}
                  disabled={loading}
                >
                  <Check className="h-4 w-4" />
                </Button>
                <Button
                  size="icon"
                  variant="ghost"
                  className="h-8 w-8 text-red-500"
                  onClick={() => setEditingField(null)}
                >
                  <X className="h-4 w-4" />
                </Button>
              </div>
            ) : (
              <div className="flex items-center gap-2 flex-1">
                <span className="text-sm">{field.value || "—"}</span>
                {field.editable !== false && (
                  <Button
                    size="icon"
                    variant="ghost"
                    className="h-8 w-8 ml-auto"
                    onClick={() => startEdit(field)}
                  >
                    <Pencil className="h-3.5 w-3.5" />
                  </Button>
                )}
              </div>
            )}
          </div>
        ))}
      </CardContent>
    </Card>
  );
}
