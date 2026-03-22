import { z } from "zod";

export const guideSchema = z.object({
  itemType: z.enum(["pest", "weed"], { message: "Item type is required" }),
  commonName: z.string().min(1, "Common name is required"),
  scientificName: z.string().optional(),
  keyCharacteristics: z.string().optional(),
  biology: z.string().optional(),
  impacts: z.string().optional(),
  control: z.string().optional(),
  images: z
    .array(
      z.object({
        imagePath: z.string().url("Must be a valid URL"),
        isPrimary: z.boolean().default(false),
      })
    )
    .optional(),
});

export type GuideInput = z.infer<typeof guideSchema>;
