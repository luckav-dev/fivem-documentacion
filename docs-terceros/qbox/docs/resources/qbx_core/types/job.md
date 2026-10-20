> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/types/job.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Jobs

## JobData

**Fields**

- label: `string`
- type?: `string`
- defaultDuty: `boolean`
- offDutyPay: `boolean`

## Job

Extends [`JobData`](#jobdata)

**Fields**

- grades: [`table<integer, JobGradeData>`](#jobgradedata)

## JobGradeData

**Fields**

- name: `string`
- isboss?: `boolean`
- bankAuth?: `boolean`
- payment: `number`
