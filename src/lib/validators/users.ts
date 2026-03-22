import { z } from "zod";

export const updateProfileSchema = z.object({
  field: z.string(),
  value: z.string(),
});

export const staffProfileSchema = z.object({
  firstName: z.string().min(1),
  lastName: z.string().min(1),
  email: z.string().email(),
  workPhoneNumber: z.string().optional(),
  position: z.string().optional(),
  department: z.string().optional(),
});

export const agronomistProfileSchema = z.object({
  firstName: z.string().min(1),
  lastName: z.string().min(1),
  email: z.string().email(),
  phoneNumber: z.string().optional(),
  address: z.string().optional(),
});

export type UpdateProfileInput = z.infer<typeof updateProfileSchema>;
