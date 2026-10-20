# Quick note on using built-in ACL/security

> Fuente original: https://docs.fivem.net/docs/cookbook/2021/07/17/quick-note-on-using-built-in-acl-security/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia — Cookbook Archive**
>
> **Note:** This Cookbook article was originally published on **July 17, 2021**. Newer information may exist.


Ever since the built-in ACL system exists (`add_ace` and similar), it has somehow not seen people use it to its full potential, often adding dependencies on 'frameworks' to resources solely in order to check if a player is currently on a particular 'job' in said 'framework'.

A lesser-known feature of the ACL system is the ability to have its configuration defined at runtime (in fact, there's no persistence layer at all - the expectation has been for the community to build one), allowing you to do stuff as follows for example:

```shell
# server.cfg, required for access to ExecuteCommand
add_ace resource.myframework command.add_principal allow
add_ace resource.myframework command.remove_principal allow

# alternately, predefine ACEs here
add_ace resource.myframework command.add_ace allow
```

```js
// server-side code in myframework
on('myframework:jobRegistered', (job) => {
    ExecuteCommand(`add_ace "job.${job}" "jobProbe.${job}" allow`);
});

on('myframework:jobAssigned', (source, job) => {
    ExecuteCommand(`add_principal "player.${source}" "job.${job}"`);
});

on('playerDropped', () => {
    const source = source;
    for (const job of myfw.getPlayerJobs(source)) {
        ExecuteCommand(`remove_principal "player.${source}" "job.${job}"`);
    }
});
```

... and then a resource that one would want to add a job check to - or a chat mode's `seObject`, or an existing resource - can just check for the `jobProbe.mechanic` privilege using native commands such as [IsPlayerAceAllowed](../../../../../natives/cfx/servidor.md#isplayeraceallowed), without taking a dependency on `myframework` or any of its inner workings.

---

*Original discussion thread: [https://forum.fivem.net/t/quick-note-on-using-built-in-acl-security/3958985](https://forum.fivem.net/t/quick-note-on-using-built-in-acl-security/3958985)*
