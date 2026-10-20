> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/dashboard/index.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Getting started with the Qbox Dashboard

*What the Qbox Dashboard does, how organizations work, and what each plan includes.*

The [Qbox Dashboard](https://dashboard.qbox.re/) is one place to run the services around your FiveM server: media hosting, database backups, your own Grafana and Loki for logs, a managed voice server, whitelist applications, and access for your staff team.

## Signing in

Open [dashboard.qbox.re](https://dashboard.qbox.re/) and choose **Continue with Google**, **Continue with Discord**, or sign in with your email or username and a password. New here? Press **Create account**.

> **Consejo: Link your Discord account**
>
> Several features work through Discord: staff getting access from their Discord roles, connecting your Discord server, and whitelist applications.
> Sign in with Discord, or link it afterwards under **Profile > Connected accounts**.

## Organizations

Everything you set up belongs to an **organization**, usually one per FiveM server or community. The person who creates it is the **owner**.

- You can own up to three organizations, and be a member of as many as you are invited to.
- Switch between them with the organization picker at the top of the sidebar.
- The owner can rename the organization, change its logo or delete it under **Organization settings**. The web address (slug) cannot be changed.
- Only the owner can see **Billing** and **Organization settings**. Ownership can be handed to another member from the **Members** page.

Your staff join your organization as members, and you decide what each of them can open. See [Team & Access](team/index.md) and the step-by-step guide [Enroll your staff](team/enroll-staff.md).

## What is in the sidebar

| Page | What it is for |
| --- | --- |
| Overview, Media, Retention & cleanup, API keys | Hosting images, video and audio for phone scripts and other resources. See [CDN](cdn/index.md). |
| Database backups | Automatic off-site backups of your game database. See [Database Backups](database-backups/index.md). |
| Logging | Your own Grafana and Loki for server logs. See [Logging](logging/index.md). |
| Nucleus | A free replacement for the retired Cfx.re Nucleus web address. See [Nucleus](nucleus/index.md). |
| Zumble | A managed voice (Mumble) server. See [Zumble](zumble/index.md). |
| Resource cache | A global CDN for the resources players download when they join. See [Resource Cache](resource-cache/index.md). |
| Applications | Whitelist and staff application forms. See [Applications](applications/index.md). |
| Discord | The Discord servers connected to your organization. See [Discord](discord/index.md). |
| Members, Roles, Audit log | Who is in your team and what they can do. See [Team & Access](team/index.md). |
| Organization settings, Billing | Owner only. |

Members only see the pages their roles give them access to.

## Plans

The owner picks a plan under **Billing**. Monthly and yearly billing are both available.

| | Free | Ducklin | Duck | Qboxxer |
| --- | --- | --- | --- | --- |
| CDN storage | 2 GB | 20 GB | 60 GB | 120 GB |
| Database backup storage | 1 GB | 2 GB | 4 GB | 8 GB |
| Nucleus | Yes | Yes | Yes | Yes |
| Logging (Grafana and Loki) | No | 2 GB RAM, 20 GB disk | 2 GB RAM, 30 GB disk | 3 GB RAM, 40 GB disk |
| Zumble voice server | No | No | Yes | Yes |
| Resource cache | No | No | No | Yes |
| Application forms | No | 1 | 5 | Unlimited |
| Discord servers | No | 1 | 3 | 10 |

> **Nota: Discord staff access needs a connected Discord server**
>
> Giving staff access through their Discord roles requires a connected Discord server, which starts at the Ducklin plan.
> On the Free plan you can still add staff by [inviting them by email](team/inviting-by-email.md).

## Where to go next

- [Enroll your staff](team/enroll-staff.md), so your team can use the dashboard and your Grafana.
- [Set up database backups](database-backups/index.md). It takes five minutes and works on every plan.
- [Start with logging](logging/getting-started.md) on a paid plan.
