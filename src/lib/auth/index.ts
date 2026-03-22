import { betterAuth } from "better-auth";
import { drizzleAdapter } from "better-auth/adapters/drizzle";
import { db } from "@/lib/db";

export const auth = betterAuth({
  database: drizzleAdapter(db, {
    provider: "pg",
  }),
  emailAndPassword: {
    enabled: true,
    requireEmailVerification: false,
    minPasswordLength: 8,
  },
  user: {
    additionalFields: {
      username: {
        type: "string",
        required: true,
        unique: true,
        input: true,
      },
      role: {
        type: "string",
        required: true,
        defaultValue: "agronomist",
        input: true,
      },
      status: {
        type: "string",
        required: false,
        defaultValue: "active",
        input: true,
      },
    },
  },
  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
    updateAge: 60 * 60 * 24, // refresh daily
  },
});

export type Session = typeof auth.$Infer.Session;
