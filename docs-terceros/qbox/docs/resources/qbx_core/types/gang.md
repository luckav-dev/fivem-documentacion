> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/types/gang.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Gangs

## GangData

**Fields**

- label: `string`

## Gang

Extends [`GangData`](#gangdata)

**Fields**

- grades: [`table<integer, GangGradeData>`](#ganggradedata)

## GangGradeData

**Fields**

- name: `string`
- isboss?: `boolean`
- bankAuth?: `boolean`
