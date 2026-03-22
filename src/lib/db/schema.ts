import {
  pgTable,
  pgEnum,
  text,
  timestamp,
  boolean,
  serial,
  integer,
  varchar,
  date,
} from "drizzle-orm/pg-core";

// ─── Enums ──────────────────────────────────────────────
export const itemTypeEnum = pgEnum("item_type", ["pest", "weed"]);
export const statusEnum = pgEnum("status", ["active", "inactive"]);

// ─── Better Auth core tables ────────────────────────────
// These are managed by Better Auth but we define them here
// so Drizzle can reference them in relations and migrations.

export const user = pgTable("user", {
  id: text("id").primaryKey(),
  name: text("name").notNull(),
  email: text("email").notNull().unique(),
  emailVerified: boolean("email_verified").notNull().default(false),
  image: text("image"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
  // Additional fields for our app
  username: text("username").notNull().unique(),
  role: text("role").notNull().default("agronomist"),
  status: text("status").notNull().default("active"),
});

export const session = pgTable("session", {
  id: text("id").primaryKey(),
  expiresAt: timestamp("expires_at").notNull(),
  token: text("token").notNull().unique(),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
  ipAddress: text("ip_address"),
  userAgent: text("user_agent"),
  userId: text("user_id")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" }),
});

export const account = pgTable("account", {
  id: text("id").primaryKey(),
  accountId: text("account_id").notNull(),
  providerId: text("provider_id").notNull(),
  userId: text("user_id")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" }),
  accessToken: text("access_token"),
  refreshToken: text("refresh_token"),
  idToken: text("id_token"),
  accessTokenExpiresAt: timestamp("access_token_expires_at"),
  refreshTokenExpiresAt: timestamp("refresh_token_expires_at"),
  scope: text("scope"),
  password: text("password"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export const verification = pgTable("verification", {
  id: text("id").primaryKey(),
  identifier: text("identifier").notNull(),
  value: text("value").notNull(),
  expiresAt: timestamp("expires_at").notNull(),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

// ─── App-specific tables ────────────────────────────────

export const agronomists = pgTable("agronomists", {
  agronomistId: serial("agronomist_id").primaryKey(),
  userId: text("user_id")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" }),
  firstName: varchar("first_name", { length: 255 }).notNull(),
  lastName: varchar("last_name", { length: 255 }).notNull(),
  email: varchar("email", { length: 255 }).notNull(),
  phoneNumber: varchar("phone_number", { length: 50 }),
  address: text("address"),
  dateJoined: date("date_joined").defaultNow(),
  status: statusEnum("status").notNull().default("active"),
});

export const staffAndAdministrators = pgTable("staff_and_administrators", {
  staffNumber: serial("staff_number").primaryKey(),
  userId: text("user_id")
    .notNull()
    .references(() => user.id, { onDelete: "cascade" }),
  firstName: varchar("first_name", { length: 255 }).notNull(),
  lastName: varchar("last_name", { length: 255 }).notNull(),
  email: varchar("email", { length: 255 }).notNull(),
  workPhoneNumber: varchar("work_phone_number", { length: 50 }),
  hireDate: date("hire_date").defaultNow(),
  position: varchar("position", { length: 255 }),
  department: varchar("department", { length: 255 }),
  status: statusEnum("status").notNull().default("active"),
});

export const agricultureItems = pgTable("agriculture_items", {
  agricultureId: serial("agriculture_id").primaryKey(),
  itemType: itemTypeEnum("item_type").notNull(),
  commonName: varchar("common_name", { length: 255 }).notNull(),
  scientificName: varchar("scientific_name", { length: 255 }),
  keyCharacteristics: text("key_characteristics"),
  biology: text("biology"),
  impacts: text("impacts"),
  control: text("control"),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export const images = pgTable("images", {
  imageId: serial("image_id").primaryKey(),
  agricultureId: integer("agriculture_id")
    .notNull()
    .references(() => agricultureItems.agricultureId, { onDelete: "cascade" }),
  imagePath: varchar("image_path", { length: 500 }).notNull(),
  isPrimary: boolean("is_primary").notNull().default(false),
});
