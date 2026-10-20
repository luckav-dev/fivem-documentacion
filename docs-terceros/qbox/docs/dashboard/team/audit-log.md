> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/dashboard/team/audit-log.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Audit log

*See who invited, removed or changed which members and roles, and which application decisions were made.*

The **Audit log** page records who changed what in your team and your applications, so you can answer "who gave this person admin?" or "who denied this application?".

You need **Audit log** set to **View**. The owner and the built-in **Admin** role have it; **Member** and **Viewer** do not.

## What is recorded

- **Members:** invitations sent, resent and revoked, members added, their roles changed, members removed, ownership transferred, and people who joined through the Discord join link.
- **Roles:** roles created, changed and deleted.
- **Discord:** Discord servers connected and disconnected, and changes to which Discord roles give dashboard access.
- **Applications:** forms created, changed, published, opened or closed and deleted, portal page changes, decisions (in review, interview, accepted, denied) and messages sent to applicants.
- **Questionnaires:** created, changed, published, reopened and closed.

Votes, internal notes and applicants withdrawing are not recorded. Neither are media uploads, API keys, backups, or changes to the logging, Nucleus and Zumble servers.

## Reading it

Use the filter at the top (**All activity**) to show one kind of event.
Each entry shows who did it. Some have a badge instead of a person:

| Badge | Meaning |
| --- | --- |
| **Discord** | Done automatically because of a Discord role, for example someone removed after losing their staff role |
| **Applicant** | Done by an applicant on your application portal |
| **System** | Done automatically by the dashboard |
| **Platform admin** | Done by the Qbox team |

Decisions made with the buttons in Discord show the person's name followed by "(via Discord)".
