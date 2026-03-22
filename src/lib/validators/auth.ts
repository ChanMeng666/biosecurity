import { z } from "zod";

const passwordSchema = z
  .string()
  .min(8, "Password must be at least 8 characters")
  .regex(/[a-z]/, "Must contain a lowercase letter")
  .regex(/[A-Z]/, "Must contain an uppercase letter")
  .regex(/[0-9]/, "Must contain a number")
  .regex(/[^A-Za-z0-9]/, "Must contain a special character");

export const loginSchema = z.object({
  email: z.string().email("Invalid email address"),
  password: z.string().min(1, "Password is required"),
});

export const registerAgronomistSchema = z.object({
  username: z.string().min(3, "Username must be at least 3 characters"),
  email: z.string().email("Invalid email"),
  password: passwordSchema,
  firstName: z.string().min(1, "First name is required"),
  lastName: z.string().min(1, "Last name is required"),
  phoneNumber: z.string().optional(),
  address: z.string().optional(),
});

export const registerStaffSchema = z.object({
  username: z.string().min(3, "Username must be at least 3 characters"),
  email: z.string().email("Invalid email"),
  password: passwordSchema,
  firstName: z.string().min(1, "First name is required"),
  lastName: z.string().min(1, "Last name is required"),
  workPhoneNumber: z.string().optional(),
  position: z.string().optional(),
  department: z.string().optional(),
});

export type LoginInput = z.infer<typeof loginSchema>;
export type RegisterAgronomistInput = z.infer<typeof registerAgronomistSchema>;
export type RegisterStaffInput = z.infer<typeof registerStaffSchema>;
