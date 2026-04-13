# Biosecurity Guide - Project Context

@AGENTS.md

## Project Overview

Full-stack biosecurity information system for agricultural pest and weed management.
- **Live URL**: https://biosecurity.chanmeng-dev.workers.dev
- **Repository**: https://github.com/ChanMeng666/biosecurity

## Tech Stack

- **Framework**: Next.js 16.2.1 (App Router) + React 19.2.4
- **Language**: TypeScript 5
- **Auth**: Better Auth 1.5.5 (email/password, DB-backed sessions via Drizzle adapter)
- **ORM**: Drizzle ORM 0.45.1 with Neon PostgreSQL serverless HTTP driver
- **Styling**: Tailwind CSS 4 + shadcn/ui (Base UI React)
- **Deployment**: Cloudflare Workers via `@opennextjs/cloudflare` adapter
- **Build**: Webpack (NOT Turbopack — Turbopack produces chunk filenames with `[root-of-the-server]` that break on Cloudflare)

## Key Architecture Decisions

### Cloudflare Workers Deployment
- Uses `@opennextjs/cloudflare` adapter with `nodejs_compat` flag
- `output: "standalone"` is required in `next.config.ts`
- Build must use `--webpack` flag (set in `package.json` build script)
- Custom image loader (`src/lib/image-loader.ts`) — pass-through since images are external URLs
- Static assets served from Cloudflare CDN, SSR runs in Workers runtime
- R2 bucket (`biosecurity-opennext-cache`) for incremental cache
- Secrets (`DATABASE_URL`, `BETTER_AUTH_SECRET`) set via `wrangler secret put`

### Database
- Neon PostgreSQL with HTTP driver (`@neondatabase/serverless`) — edge-compatible, no TCP connections
- Connection in `src/lib/db/index.ts` — single `drizzle()` instance with schema
- Schema in `src/lib/db/schema.ts` — Better Auth tables + app tables (agriculture_items, images, agronomists, staff_and_administrators)
- Migrations managed by Drizzle Kit

### Authentication
- Better Auth with Drizzle adapter in `src/lib/auth/index.ts`
- Client-side auth in `src/lib/auth/client.ts` — uses `NEXT_PUBLIC_APP_URL` (build-time inlined)
- Middleware (`src/middleware.ts`) only checks session cookies — no DB calls, edge-safe
- API routes use `auth.api.getSession({ headers: request.headers })` for server-side auth
- Three roles: administrator, staff, agronomist

### Routing
- Public: `/`, `/login`, `/register/*`, `/sources`
- Protected: `/admin/*`, `/staff/*`, `/agronomist/*`
- API: `/api/auth/[...all]`, `/api/guides`, `/api/agronomists`, `/api/staff`, `/api/profile`

## Important Files

| File | Purpose |
|------|---------|
| `wrangler.jsonc` | Cloudflare Worker config (account, bindings, vars) |
| `open-next.config.ts` | OpenNext Cloudflare adapter config |
| `next.config.ts` | Next.js config (standalone output, custom image loader) |
| `src/lib/db/index.ts` | Database connection (Neon HTTP) |
| `src/lib/db/schema.ts` | Full database schema |
| `src/lib/auth/index.ts` | Better Auth server config |
| `src/lib/auth/client.ts` | Better Auth client (uses NEXT_PUBLIC_APP_URL) |
| `src/middleware.ts` | Route protection (cookie check only) |
| `drizzle.config.ts` | Drizzle Kit config for migrations |

## Scripts

```bash
npm run dev          # Local dev server (Next.js, port 3000)
npm run build        # Production build (webpack)
npm run build:worker # Build for Cloudflare Workers
npm run preview      # Preview Cloudflare build locally
npm run cf:deploy    # Build + deploy to Cloudflare Workers
npm run db:generate  # Generate Drizzle migration files
npm run db:push      # Push schema to database
npm run db:studio    # Drizzle Studio GUI
```

## Environment Variables

| Variable | Where | Notes |
|----------|-------|-------|
| `DATABASE_URL` | Cloudflare secret / `.env.local` | Neon PostgreSQL connection string |
| `BETTER_AUTH_SECRET` | Cloudflare secret / `.env.local` | 32+ char random string |
| `BETTER_AUTH_URL` | `wrangler.jsonc` vars / `.env.local` | Must match production URL |
| `NEXT_PUBLIC_APP_URL` | Build env / `.env.local` | Inlined at build time into client JS |

## Deploy Commands

```bash
# Set secrets (first time)
CLOUDFLARE_ACCOUNT_ID=c87dca24333f7ed5d643f731f6308fec wrangler secret put DATABASE_URL
CLOUDFLARE_ACCOUNT_ID=c87dca24333f7ed5d643f731f6308fec wrangler secret put BETTER_AUTH_SECRET

# Build and deploy
NEXT_PUBLIC_APP_URL=https://biosecurity.chanmeng-dev.workers.dev npm run cf:deploy
```

## Known Issues

- **Windows + Turbopack**: Turbopack generates chunk files named `[root-of-the-server]__*.js` which cause `ChunkLoadError` on Cloudflare Workers. Always use `--webpack` for builds.
- **OpenNext Windows warning**: "OpenNext is not fully compatible with Windows" — builds work with `--webpack` but consider WSL or Linux CI for production builds.
- **`NEXT_PUBLIC_APP_URL`**: Must be set as an environment variable at build time, not just in `wrangler.jsonc`, because Next.js inlines it into client bundles.
