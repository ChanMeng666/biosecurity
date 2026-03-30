<div align="center"><a name="readme-top"></a>

# Biosecurity Guide for Agricultural Pests & Weeds

A comprehensive digital platform for identifying, understanding, and managing agricultural pests and weeds.<br/>
Built for agronomists, staff, and administrators with role-based access control and a growing guide library.<br/>

[Issues][github-issues-link]

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

</div>

> [!IMPORTANT]
> This project is a modern full-stack biosecurity information system built with Next.js 16, React 19, Better Auth, Drizzle ORM, and Neon PostgreSQL. It provides role-based dashboards for administrators, staff, and agronomists to manage and browse pest and weed identification guides with detailed scientific data, images, and control methods.

<details>
<summary><kbd>Table of Contents</kbd></summary>

#### TOC

- [Introduction](#-introduction)
- [Key Features](#-key-features)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Installation](#quick-installation)
  - [Environment Setup](#environment-setup)
  - [Database Setup](#database-setup)
  - [Development Mode](#development-mode)
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
> - Better Auth secret required for authentication

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
- **Runtime**: Next.js API Routes (Node.js)
- **Authentication**: Better Auth with email/password and server-side sessions
- **Database ORM**: Drizzle ORM with type-safe queries
- **Validation**: Zod schema validation

**Database:**
- **Provider**: Neon serverless PostgreSQL
- **Migrations**: Drizzle Kit
- **Schema**: Custom tables for users, guides, images, profiles with role-based enums

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
| `NEXT_PUBLIC_APP_URL` | Yes | Public-facing app URL |

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
npm run build        # Production build
npm run start        # Start production server
npm run lint         # Run ESLint
npm run db:generate  # Generate Drizzle migration files
npm run db:push      # Push schema changes to database
npm run db:migrate   # Run pending migrations
npm run db:studio    # Open Drizzle Studio database GUI
```

[![][back-to-top]](#readme-top)

<!-- ═══════════════════════════════════════════════════════════════════════════ -->

## Project Structure

```
src/
├── app/                          # Next.js App Router
│   ├── (auth)/                   # Authentication routes
│   │   ├── login/                # Login page
│   │   └── register/             # Registration pages
│   │       ├── admin/            # Admin registration
│   │       ├── agronomist/       # Agronomist registration
│   │       └── staff/            # Staff registration
│   ├── (dashboard)/              # Protected dashboard routes
│   │   ├── admin/                # Admin dashboard
│   │   │   ├── manage-guides/    # Guide CRUD management
│   │   │   ├── manage-agronomists/ # Agronomist management
│   │   │   └── manage-staff/     # Staff management
│   │   ├── agronomist/           # Agronomist dashboard
│   │   │   └── guides/           # Guide browsing
│   │   └── staff/                # Staff dashboard
│   │       ├── manage-guides/    # Guide CRUD management
│   │       └── view-agronomists/ # View agronomist profiles
│   ├── api/                      # API routes
│   │   ├── auth/[...all]/        # Better Auth handler
│   │   ├── guides/               # Guide CRUD endpoints
│   │   ├── agronomists/          # Agronomist endpoints
│   │   ├── staff/                # Staff endpoints
│   │   └── profile/              # Profile endpoints
│   └── sources/                  # Sources & credits page
├── components/
│   ├── ui/                       # shadcn/ui base components
│   ├── guides/                   # Guide-specific components
│   ├── layout/                   # Navbar, dashboard shell
│   ├── shared/                   # Confirm dialog, data table
│   └── users/                    # Profile editor
└── lib/
    ├── auth/                     # Better Auth config & helpers
    ├── db/                       # Drizzle ORM, schema, migrations
    └── validators/               # Zod validation schemas
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
