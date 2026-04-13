<div align="center"><a name="readme-top"></a>

# Biosecurity Guide for Agricultural Pests & Weeds

A comprehensive digital platform for identifying, understanding, and managing agricultural pests and weeds.<br/>
Built for agronomists, staff, and administrators with role-based access control and a growing guide library.<br/>

**[Live Demo](https://biosecurity.chanmeng-dev.workers.dev)** | [Issues][github-issues-link]

<br/>

<!-- SHIELD GROUP -->

[![][github-contributors-shield]][github-contributors-link]
[![][github-forks-shield]][github-forks-link]
[![][github-stars-shield]][github-stars-link]
[![][github-issues-shield]][github-issues-link]
[![][github-license-shield]][github-license-link]

**Share Project Repository**

[![][share-x-shield]][share-x-link]
[![][share-telegram-shield]][share-telegram-link]
[![][share-whatsapp-shield]][share-whatsapp-link]
[![][share-reddit-shield]][share-reddit-link]
[![][share-weibo-shield]][share-weibo-link]
[![][share-mastodon-shield]][share-mastodon-link]
[![][share-linkedin-shield]][share-linkedin-link]

**Tech Stack:**

<img src="https://img.shields.io/badge/next.js-%23000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB"/>
<img src="https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwindcss&logoColor=white"/>
<img src="https://img.shields.io/badge/postgresql-%23336791.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/drizzle-%23C5F74F.svg?style=for-the-badge&logo=drizzle&logoColor=black"/>
<img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white"/>

</div>

> [!IMPORTANT]
> This project is a modern full-stack biosecurity information system built with Next.js 16, React 19, Better Auth, Drizzle ORM, and Neon PostgreSQL. It is deployed on Cloudflare Workers via the `@opennextjs/cloudflare` adapter for global edge performance. It provides role-based dashboards for administrators, staff, and agronomists to manage and browse pest and weed identification guides with detailed scientific data, images, and control methods.

<details>
<summary><kbd>Table of Contents</kbd></summary>

#### TOC

- [Introduction](#-introduction)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Installation](#quick-installation)
  - [Environment Setup](#environment-setup)
  - [Database Setup](#database-setup)
  - [Development Mode](#development-mode)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#%EF%B8%8F-author)

####

<br/>

</details>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Introduction

<table>
<tr>
<td>

<h4>About This Project</h4>

The **Biosecurity Guide** is a comprehensive digital platform designed to support agricultural professionals in identifying, understanding, and managing pests and weeds. The system provides a centralized guide library with detailed information on pest and weed characteristics, biology, impacts, and control methods — all backed by visual references.

The platform supports three distinct user roles — **Administrator**, **Staff**, and **Agronomist** — each with tailored dashboards and capabilities, ensuring the right level of access for every user.

<h4>Why This Project Exists</h4>

Agricultural biosecurity is critical for protecting crops, ecosystems, and food supply chains. Agronomists and field workers need quick, reliable access to pest and weed identification data to make timely decisions. This platform consolidates that information into a searchable, managed, and role-protected system — replacing scattered documents and outdated references with a modern, responsive web application.

<h4>Goals</h4>

- Provide a centralized, searchable library of pest and weed identification guides
- Enable role-based management of biosecurity information across organizations
- Deliver a modern, responsive web experience for field and office use
- Support data-driven decision making with structured scientific information

</td>
</tr>
</table>

> [!NOTE]
> - Node.js >= 18.0 required
> - Neon PostgreSQL account required for database
> - Cloudflare account required for deployment

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Key Features

### `1` Pest Identification

Detailed guides on agricultural pests including common and scientific names, key characteristics, biology, impacts, and control methods — all with visual image references to aid field identification.

Key capabilities:
- Comprehensive pest profiles with scientific data
- Multiple image support per guide entry
- Structured control method recommendations
- Impact assessment information

### `2` Weed Management

Comprehensive weed identification and control guides to protect agricultural productivity and biodiversity. Each entry includes lifecycle data, distinguishing characteristics, and recommended management strategies.

### `3` Role-Based Access Control

Three distinct user roles with tailored dashboards and permissions:

| Role | Capabilities |
|------|-------------|
| **Administrator** | Full platform access — manage guides, staff, agronomists, and all system settings |
| **Staff** | Create, edit, and delete guides; view agronomist profiles; manage own profile |
| **Agronomist** | Browse and search the guide library; manage own profile |

### `4` Guide Library & Smart Search

Browse and search through the guide library with powerful filtering capabilities:

- Field-specific filtering (common name, scientific name, characteristics, biology, impacts, control)
- Case-insensitive search matching
- Pagination for large datasets
- Filter by type (pest or weed)

### `*` Additional Features

- [x] Secure authentication with server-side sessions (Better Auth)
- [x] Image carousel for visual guide references
- [x] Responsive design for desktop and mobile use
- [x] Light/dark theme support
- [x] Profile management for all user roles
- [x] Form validation with Zod schemas
- [x] Modern UI with shadcn/ui components

<div align="right">

[![][back-to-top]](#readme-top)

</div>

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Architecture

### System Overview

```mermaid
graph TB
    subgraph Client["Client (Browser)"]
        UI[React 19 UI<br/>shadcn/ui + Tailwind CSS 4]
        AuthClient[Better Auth Client]
    end

    subgraph CloudflareEdge["Cloudflare Workers (Edge)"]
        Worker[OpenNext Worker]
        Middleware[Next.js Middleware<br/>Session Cookie Check]
        SSR[Next.js SSR<br/>App Router]
        API[API Routes<br/>REST Endpoints]
        Assets[Static Assets<br/>Cloudflare CDN]
    end

    subgraph ExternalServices["External Services"]
        NeonDB[(Neon PostgreSQL<br/>Serverless HTTP)]
        R2[Cloudflare R2<br/>Incremental Cache]
        Pixabay[Pixabay CDN<br/>Guide Images]
    end

    UI -->|HTTPS| Worker
    AuthClient -->|Auth API| API
    Worker --> Middleware
    Middleware -->|Protected Routes| SSR
    Middleware -->|Public Routes| SSR
    Worker -->|Static Files| Assets
    SSR --> API
    API -->|Drizzle ORM| NeonDB
    API -->|Better Auth| NeonDB
    Worker -->|Cache| R2
    UI -->|Images| Pixabay
```

### Request Flow

```mermaid
sequenceDiagram
    actor User
    participant CF as Cloudflare Worker
    participant MW as Middleware
    participant Page as Next.js Page
    participant API as API Route
    participant Auth as Better Auth
    participant DB as Neon PostgreSQL

    User->>CF: HTTPS Request
    CF->>MW: Route Request

    alt Static Asset
        CF-->>User: Serve from CDN Cache
    else Public Route (/, /login, /sources)
        MW->>Page: Allow Access
        Page-->>User: Render Page
    else Protected Route (/admin/*, /staff/*, etc.)
        MW->>MW: Check Session Cookie
        alt No Session Cookie
            MW-->>User: Redirect to /login
        else Has Session Cookie
            MW->>Page: Allow Access
            Page->>API: Fetch Data
            API->>Auth: Verify Session
            Auth->>DB: Query Session
            DB-->>Auth: Session Data
            API->>DB: Query Data
            DB-->>API: Results
            API-->>Page: JSON Response
            Page-->>User: Render Page
        end
    end
```

### Database Schema

```mermaid
erDiagram
    user {
        text id PK
        text name
        text email UK
        text username UK
        text role "administrator | staff | agronomist"
        text status "active | inactive"
        boolean emailVerified
        text image
        timestamp createdAt
        timestamp updatedAt
    }

    session {
        text id PK
        text userId FK
        text token UK
        text ipAddress
        text userAgent
        timestamp expiresAt
        timestamp createdAt
        timestamp updatedAt
    }

    account {
        text id PK
        text userId FK
        text accountId
        text providerId
    }

    verification {
        text id PK
        text identifier
        text value
        timestamp expiresAt
        timestamp createdAt
        timestamp updatedAt
    }

    agronomists {
        serial id PK
        text userId FK
        text firstName
        text lastName
        text phoneNumber
        text address
    }

    staff_and_administrators {
        serial id PK
        text userId FK
        text firstName
        text lastName
        text position
        text department
    }

    agriculture_items {
        serial id PK
        enum itemType "pest | weed"
        text commonName
        text scientificName
        text keyCharacteristics
        text biology
        text impacts
        text control
        text source
    }

    images {
        serial id PK
        integer itemId FK
        text url
        text altText
        boolean isPrimary
    }

    user ||--o{ session : "has"
    user ||--o{ account : "has"
    user ||--o| agronomists : "profile"
    user ||--o| staff_and_administrators : "profile"
    agriculture_items ||--o{ images : "has"
```

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Tech Stack

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/nextdotjs" width="48" height="48" alt="Next.js" />
        <br>Next.js 16
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/react" width="48" height="48" alt="React" />
        <br>React 19
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/typescript" width="48" height="48" alt="TypeScript" />
        <br>TypeScript 5
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/tailwindcss" width="48" height="48" alt="Tailwind CSS" />
        <br>Tailwind CSS 4
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/postgresql" width="48" height="48" alt="PostgreSQL" />
        <br>Neon PostgreSQL
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/drizzle" width="48" height="48" alt="Drizzle" />
        <br>Drizzle ORM
      </td>
      <td align="center" width="96">
        <img src="https://cdn.simpleicons.org/cloudflare" width="48" height="48" alt="Cloudflare" />
        <br>Cloudflare
      </td>
    </tr>
  </table>
</div>

**Frontend:**
- **Framework**: Next.js 16 with App Router
- **Language**: TypeScript for type safety
- **Styling**: Tailwind CSS 4 + tw-animate-css
- **UI Components**: shadcn/ui (Base UI React)
- **Icons**: Lucide React
- **Themes**: next-themes for light/dark mode
- **Notifications**: Sonner toast system

**Backend:**
- **Runtime**: Next.js API Routes on Cloudflare Workers (edge)
- **Authentication**: Better Auth with email/password and server-side sessions
- **Database ORM**: Drizzle ORM with type-safe queries
- **Validation**: Zod schema validation

**Database:**
- **Provider**: Neon serverless PostgreSQL (HTTP driver, edge-compatible)
- **Migrations**: Drizzle Kit
- **Schema**: Custom tables for users, guides, images, profiles with role-based enums

**Infrastructure:**
- **Hosting**: Cloudflare Workers via `@opennextjs/cloudflare` adapter
- **Static Assets**: Cloudflare CDN (automatic edge caching)
- **Incremental Cache**: Cloudflare R2 bucket
- **Build**: Webpack bundler (required for Cloudflare compatibility)

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Getting Started

### Prerequisites

> [!IMPORTANT]
> Ensure you have the following installed:

- Node.js 18.0+ ([Download](https://nodejs.org/))
- npm package manager
- Git ([Download](https://git-scm.com/))
- A [Neon](https://neon.tech/) PostgreSQL database account
- A [Cloudflare](https://dash.cloudflare.com/) account (for deployment)

### Quick Installation

**1. Clone Repository**

```bash
git clone https://github.com/ChanMeng666/biosecurity.git
cd biosecurity
```

**2. Install Dependencies**

```bash
npm install
```

### Environment Setup

**3. Configure Environment Variables**

```bash
# Copy environment template
cp .env.example .env.local

# Edit environment variables
nano .env.local
```

Create `.env.local` with the following variables:

```bash
# Neon Database (get from neonctl connection-string)
DATABASE_URL=postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/neondb?sslmode=require

# Better Auth (generate a random 32+ character secret)
BETTER_AUTH_SECRET=your-random-secret-here
BETTER_AUTH_URL=http://localhost:3000

# App URL
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

**Quick Reference:**

| Variable | Required | Purpose |
|----------|----------|---------|
| `DATABASE_URL` | Yes | Neon PostgreSQL connection string |
| `BETTER_AUTH_SECRET` | Yes | Auth encryption key (32+ chars) |
| `BETTER_AUTH_URL` | Yes | Auth base URL |
| `NEXT_PUBLIC_APP_URL` | Yes | Public-facing app URL (inlined at build time) |

> [!TIP]
> Use `openssl rand -base64 32` to generate a secure random secret for `BETTER_AUTH_SECRET`.

### Database Setup

**4. Run Database Migrations**

```bash
# Generate migration files from schema
npm run db:generate

# Push schema to database
npm run db:push
```

> [!TIP]
> Use `npm run db:studio` to open the Drizzle Studio GUI for browsing your database.

### Development Mode

**5. Start Development Server**

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the application.

**Available Scripts:**

```bash
npm run dev          # Start dev server with hot reload
npm run build        # Production build (webpack)
npm run start        # Start production server (local Node.js)
npm run build:worker # Build for Cloudflare Workers
npm run preview      # Preview Cloudflare build locally
npm run cf:deploy    # Build and deploy to Cloudflare Workers
npm run lint         # Run ESLint
npm run db:generate  # Generate Drizzle migration files
npm run db:push      # Push schema changes to database
npm run db:migrate   # Run pending migrations
npm run db:studio    # Open Drizzle Studio database GUI
```

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Deployment

This project is deployed on **Cloudflare Workers** using the [`@opennextjs/cloudflare`](https://opennext.js.org/cloudflare) adapter.

**Live URL:** https://biosecurity.chanmeng-dev.workers.dev

### Deployment Architecture

```mermaid
graph LR
    subgraph Build["Build Pipeline"]
        Next["next build --webpack"]
        OpenNext["opennextjs-cloudflare build"]
        Next --> OpenNext
    end

    subgraph Output["Build Output (.open-next/)"]
        WorkerJS["worker.js<br/>Entry Point"]
        ServerFn["server-functions/<br/>SSR + API"]
        StaticAssets["assets/<br/>CSS, JS, Fonts"]
    end

    subgraph Cloudflare["Cloudflare Edge Network"]
        CDN["CDN<br/>Static Assets"]
        Workers["Workers Runtime<br/>nodejs_compat"]
        R2["R2 Bucket<br/>Incremental Cache"]
    end

    subgraph External["External"]
        Neon["Neon PostgreSQL<br/>HTTP Driver"]
    end

    OpenNext --> WorkerJS
    OpenNext --> ServerFn
    OpenNext --> StaticAssets

    StaticAssets -->|wrangler deploy| CDN
    WorkerJS -->|wrangler deploy| Workers
    ServerFn -->|bundled into| Workers
    Workers -->|Cache Read/Write| R2
    Workers -->|SQL over HTTP| Neon
```

### Deploy Steps

```bash
# 1. Set Cloudflare secrets (first time only)
wrangler secret put DATABASE_URL
wrangler secret put BETTER_AUTH_SECRET

# 2. Build and deploy
NEXT_PUBLIC_APP_URL=https://biosecurity.chanmeng-dev.workers.dev npm run cf:deploy
```

> [!NOTE]
> - `NEXT_PUBLIC_APP_URL` must be set at build time (it is inlined into client JavaScript bundles).
> - The build uses `--webpack` instead of Turbopack for Cloudflare compatibility.
> - The `nodejs_compat` compatibility flag is enabled in `wrangler.jsonc` to support Node.js APIs used by Better Auth.

### Key Configuration Files

| File | Purpose |
|------|---------|
| `wrangler.jsonc` | Cloudflare Worker configuration (bindings, compatibility flags, env vars) |
| `open-next.config.ts` | OpenNext adapter configuration |
| `next.config.ts` | Next.js config (`standalone` output, custom image loader) |
| `src/lib/image-loader.ts` | Custom image loader for Cloudflare (pass-through for external URLs) |

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Project Structure

```
biosecurity/
├── src/
│   ├── app/                          # Next.js App Router
│   │   ├── (auth)/                   # Authentication routes
│   │   │   ├── login/                # Login page
│   │   │   └── register/             # Registration pages
│   │   │       ├── admin/            # Admin registration
│   │   │       ├── agronomist/       # Agronomist registration
│   │   │       └── staff/            # Staff registration
│   │   ├── (dashboard)/              # Protected dashboard routes
│   │   │   ├── admin/                # Admin dashboard
│   │   │   │   ├── manage-guides/    # Guide CRUD management
│   │   │   │   ├── manage-agronomists/ # Agronomist management
│   │   │   │   └── manage-staff/     # Staff management
│   │   │   ├── agronomist/           # Agronomist dashboard
│   │   │   │   └── guides/           # Guide browsing
│   │   │   └── staff/                # Staff dashboard
│   │   │       ├── manage-guides/    # Guide CRUD management
│   │   │       └── view-agronomists/ # View agronomist profiles
│   │   ├── api/                      # API routes
│   │   │   ├── auth/[...all]/        # Better Auth handler
│   │   │   ├── guides/               # Guide CRUD endpoints
│   │   │   ├── agronomists/          # Agronomist endpoints
│   │   │   ├── staff/                # Staff endpoints
│   │   │   └── profile/              # Profile endpoints
│   │   └── sources/                  # Sources & credits page
│   ├── components/
│   │   ├── ui/                       # shadcn/ui base components
│   │   ├── guides/                   # Guide-specific components
│   │   ├── layout/                   # Navbar, dashboard shell
│   │   ├── shared/                   # Confirm dialog, data table
│   │   └── users/                    # Profile editor
│   └── lib/
│       ├── auth/                     # Better Auth config & helpers
│       ├── db/                       # Drizzle ORM, schema, migrations
│       ├── image-loader.ts           # Custom Cloudflare image loader
│       └── validators/               # Zod validation schemas
├── wrangler.jsonc                    # Cloudflare Worker configuration
├── open-next.config.ts               # OpenNext adapter configuration
├── next.config.ts                    # Next.js configuration
├── drizzle.config.ts                 # Drizzle ORM configuration
├── package.json                      # Dependencies and scripts
└── tsconfig.json                     # TypeScript configuration
```

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

**Guidelines:**
- Follow TypeScript best practices
- Use the existing code style and ESLint configuration
- Test your changes locally before submitting
- Write clear commit messages

[![][pr-welcome-shield]][pr-welcome-link]

### Contributors

<a href="https://github.com/ChanMeng666/biosecurity/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ChanMeng666/biosecurity" />
</a>

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Author

**Chan Meng**

<p>
  <a href="https://www.linkedin.com/in/chanmeng666/">
    <img src="https://img.shields.io/badge/LinkedIn-chanmeng666-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/ChanMeng666">
    <img src="https://img.shields.io/badge/GitHub-ChanMeng666-181717?style=flat&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  <a href="mailto:chanmeng.dev@gmail.com">
    <img src="https://img.shields.io/badge/Email-chanmeng.dev@gmail.com-EA4335?style=flat&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://chanmeng.org/">
    <img src="https://img.shields.io/badge/Website-chanmeng.org-4285F4?style=flat&logo=googlechrome&logoColor=white" alt="Website"/>
  </a>
</p>

---

<div align="center">
<strong>Protecting Agriculture Through Knowledge</strong>
<br/>
<em>A comprehensive biosecurity guide for agricultural pest and weed management</em>
<br/><br/>

<img src="https://img.shields.io/github/stars/ChanMeng666/biosecurity?style=social" alt="GitHub stars">
<img src="https://img.shields.io/github/forks/ChanMeng666/biosecurity?style=social" alt="GitHub forks">
<img src="https://img.shields.io/github/watchers/ChanMeng666/biosecurity?style=social" alt="GitHub watchers">

</div>

---

<!-- LINK DEFINITIONS -->

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square

<!-- GitHub Links -->
[github-issues-link]: https://github.com/ChanMeng666/biosecurity/issues
[github-stars-link]: https://github.com/ChanMeng666/biosecurity/stargazers
[github-forks-link]: https://github.com/ChanMeng666/biosecurity/forks
[github-contributors-link]: https://github.com/ChanMeng666/biosecurity/contributors
[github-license-link]: https://github.com/ChanMeng666/biosecurity/blob/main/LICENSE
[pr-welcome-link]: https://github.com/ChanMeng666/biosecurity/pulls

<!-- Shield Badges -->
[github-contributors-shield]: https://img.shields.io/github/contributors/ChanMeng666/biosecurity?color=c4f042&labelColor=black&style=flat-square
[github-forks-shield]: https://img.shields.io/github/forks/ChanMeng666/biosecurity?color=8ae8ff&labelColor=black&style=flat-square
[github-stars-shield]: https://img.shields.io/github/stars/ChanMeng666/biosecurity?color=ffcb47&labelColor=black&style=flat-square
[github-issues-shield]: https://img.shields.io/github/issues/ChanMeng666/biosecurity?color=ff80eb&labelColor=black&style=flat-square
[github-license-shield]: https://img.shields.io/badge/license-MIT-white?labelColor=black&style=flat-square
[pr-welcome-shield]: https://img.shields.io/badge/PRs_welcome-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge

<!-- Social Share Links -->
[share-x-link]: https://x.com/intent/tweet?hashtags=biosecurity%2Cagriculture&text=Check%20out%20this%20Biosecurity%20Guide%20for%20Agricultural%20Pests%20%26%20Weeds&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-telegram-link]: https://t.me/share/url?text=Biosecurity%20Guide%20for%20Agricultural%20Pests%20%26%20Weeds&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-whatsapp-link]: https://api.whatsapp.com/send?text=Check%20out%20this%20Biosecurity%20Guide%20https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-reddit-link]: https://www.reddit.com/submit?title=Biosecurity%20Guide%20for%20Agricultural%20Pests%20%26%20Weeds&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-weibo-link]: http://service.weibo.com/share/share.php?title=Biosecurity%20Guide%20for%20Agricultural%20Pests%20%26%20Weeds&url=https%3A%2F%2Fgithub.com%2FChanMeng666%2Fbiosecurity
[share-mastodon-link]: https://mastodon.social/share?text=Biosecurity%20Guide%20for%20Agricultural%20Pests%20%26%20Weeds%20https://github.com/ChanMeng666/biosecurity
[share-linkedin-link]: https://linkedin.com/sharing/share-offsite/?url=https://github.com/ChanMeng666/biosecurity

[share-x-shield]: https://img.shields.io/badge/-share%20on%20x-black?labelColor=black&logo=x&logoColor=white&style=flat-square
[share-telegram-shield]: https://img.shields.io/badge/-share%20on%20telegram-black?labelColor=black&logo=telegram&logoColor=white&style=flat-square
[share-whatsapp-shield]: https://img.shields.io/badge/-share%20on%20whatsapp-black?labelColor=black&logo=whatsapp&logoColor=white&style=flat-square
[share-reddit-shield]: https://img.shields.io/badge/-share%20on%20reddit-black?labelColor=black&logo=reddit&logoColor=white&style=flat-square
[share-weibo-shield]: https://img.shields.io/badge/-share%20on%20weibo-black?labelColor=black&logo=sinaweibo&logoColor=white&style=flat-square
[share-mastodon-shield]: https://img.shields.io/badge/-share%20on%20mastodon-black?labelColor=black&logo=mastodon&logoColor=white&style=flat-square
[share-linkedin-shield]: https://img.shields.io/badge/-share%20on%20linkedin-black?labelColor=black&logo=linkedin&logoColor=white&style=flat-square
