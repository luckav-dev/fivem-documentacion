# Natives de GTA V — STATS

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `STATS`: **311** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`GetNgstatBoolHash`](#getngstatboolhash) · [`GetNgstatIntHash`](#getngstatinthash) · [`GetPackedBoolStatKey`](#getpackedboolstatkey) · [`GetPackedIntStatKey`](#getpackedintstatkey) · [`GetPackedTuBoolStatKey`](#getpackedtuboolstatkey) · [`GetPackedTuIntStatKey`](#getpackedtuintstatkey) · [`HiredLimo`](#hiredlimo) · [`Leaderboards2ReadByHandle`](#leaderboards2readbyhandle) · [`Leaderboards2ReadByPlatform`](#leaderboards2readbyplatform) · [`Leaderboards2ReadByRadius`](#leaderboards2readbyradius) · [`Leaderboards2ReadByRank`](#leaderboards2readbyrank) · [`Leaderboards2ReadByRow`](#leaderboards2readbyrow) · [`Leaderboards2ReadByScoreFloat`](#leaderboards2readbyscorefloat) · [`Leaderboards2ReadByScoreInt`](#leaderboards2readbyscoreint) · [`Leaderboards2ReadFriendsByRow`](#leaderboards2readfriendsbyrow) · [`Leaderboards2ReadRankPrediction`](#leaderboards2readrankprediction) · [`Leaderboards2WriteData`](#leaderboards2writedata) · [`Leaderboards2WriteDataForEventType`](#leaderboards2writedataforeventtype) · [`LeaderboardsCacheDataRow`](#leaderboardscachedatarow) · [`LeaderboardsClearCacheData`](#leaderboardsclearcachedata) · [`LeaderboardsDeaths`](#leaderboardsdeaths) · [`LeaderboardsGetCacheDataRow`](#leaderboardsgetcachedatarow) · [`LeaderboardsGetCacheExists`](#leaderboardsgetcacheexists) · [`LeaderboardsGetCacheNumberOfRows`](#leaderboardsgetcachenumberofrows) · [`LeaderboardsGetCacheTime`](#leaderboardsgetcachetime) · [`LeaderboardsGetColumnId`](#leaderboardsgetcolumnid) · [`LeaderboardsGetColumnType`](#leaderboardsgetcolumntype) · [`LeaderboardsGetNumberOfColumns`](#leaderboardsgetnumberofcolumns) · [`LeaderboardsReadAnyPending`](#leaderboardsreadanypending) · [`LeaderboardsReadClear`](#leaderboardsreadclear) · [`LeaderboardsReadClearAll`](#leaderboardsreadclearall) · [`LeaderboardsReadPending`](#leaderboardsreadpending) · [`LeaderboardsReadSuccessful`](#leaderboardsreadsuccessful) · [`LeaderboardsWriteAddColumn`](#leaderboardswriteaddcolumn) · [`LeaderboardsWriteAddColumnLong`](#leaderboardswriteaddcolumnlong) · [`N_0x0077f15613d36993`](#n_0x0077f15613d36993) · [`N_0x015b03ee1c43e6ec`](#n_0x015b03ee1c43e6ec) · [`N_0x03c2eebb04b3fb72`](#n_0x03c2eebb04b3fb72) · [`N_0x06eaf70ae066441e`](#n_0x06eaf70ae066441e) · [`N_0x0a9c7f36e5d7b683`](#n_0x0a9c7f36e5d7b683) · [`N_0x0b565b0aae56a0e8`](#n_0x0b565b0aae56a0e8) · [`N_0x0b8b7f74bf061c6d`](#n_0x0b8b7f74bf061c6d) · [`N_0x0d01d20616fc73fb`](#n_0x0d01d20616fc73fb) · [`N_0x14e0b2d1ad1044e0`](#n_0x14e0b2d1ad1044e0) · [`N_0x14eda9ee27bd1626`](#n_0x14eda9ee27bd1626) · [`N_0x164c5ff663790845`](#n_0x164c5ff663790845) · [`N_0x1a7ce7cd3e653485`](#n_0x1a7ce7cd3e653485) · [`N_0x1a8ea222f9c67dbb`](#n_0x1a8ea222f9c67dbb) · [`N_0x26d7399b9587fe89`](#n_0x26d7399b9587fe89) · [`N_0x27aa1c973cacfe63`](#n_0x27aa1c973cacfe63) · [`N_0x2818ff6638cb09de`](#n_0x2818ff6638cb09de) · [`N_0x282b6739644f4347`](#n_0x282b6739644f4347) · [`N_0x28ecb8ac2f607db2`](#n_0x28ecb8ac2f607db2) · [`N_0x2cd90358f67d0aa8`](#n_0x2cd90358f67d0aa8) · [`N_0x2d7a9b577e72385e`](#n_0x2d7a9b577e72385e) · [`N_0x2e0259babc27a327`](#n_0x2e0259babc27a327) · [`N_0x2fa3173480008493`](#n_0x2fa3173480008493) · [`N_0x316db59cd14c1774`](#n_0x316db59cd14c1774) · [`N_0x32cac93c9de73d32`](#n_0x32cac93c9de73d32) · [`N_0x33d72899e24c3365`](#n_0x33d72899e24c3365) · [`N_0x34770b9ce0e03b91`](#n_0x34770b9ce0e03b91) · [`N_0x38491439b6ba7f7d`](#n_0x38491439b6ba7f7d) · [`N_0x38baaa5dd4c9d19f`](#n_0x38baaa5dd4c9d19f) · [`N_0x3de3aa516fb126a4`](#n_0x3de3aa516fb126a4) · [`N_0x3ebeac6c3f81f6bd`](#n_0x3ebeac6c3f81f6bd) · [`N_0x419615486bbf1956`](#n_0x419615486bbf1956) · [`N_0x44919cc079bb60bf`](#n_0x44919cc079bb60bf) · [`N_0x4aff7e02e485e92b`](#n_0x4aff7e02e485e92b) · [`N_0x4c89fe2bdeb3f169`](#n_0x4c89fe2bdeb3f169) · [`N_0x4dc416f246a41fc8`](#n_0x4dc416f246a41fc8) · [`N_0x4fcdbd3f0a813c25`](#n_0x4fcdbd3f0a813c25) · [`N_0x53c31853ec9531ff`](#n_0x53c31853ec9531ff) · [`N_0x53cae13e9b426993`](#n_0x53cae13e9b426993) · [`N_0x55384438fc55ad8e`](#n_0x55384438fc55ad8e) · [`N_0x55a8becaf28a4eb7`](#n_0x55a8becaf28a4eb7) · [`N_0x5688585e6d563cd8`](#n_0x5688585e6d563cd8) · [`N_0x5a556b229a169402`](#n_0x5a556b229a169402) · [`N_0x5bd5f255321c4aaf`](#n_0x5bd5f255321c4aaf) · [`N_0x5bf29846c6527c54`](#n_0x5bf29846c6527c54) · [`N_0x5cdaed54b34b0ed0`](#n_0x5cdaed54b34b0ed0) · [`N_0x5ead2bf6484852e4`](#n_0x5ead2bf6484852e4) · [`N_0x5ff2c33b13a02a11`](#n_0x5ff2c33b13a02a11) · [`N_0x60eedc12af66e846`](#n_0x60eedc12af66e846) · [`N_0x629526aba383bcaa`](#n_0x629526aba383bcaa) · [`N_0x6483c25849031c4f`](#n_0x6483c25849031c4f) · [`N_0x6551b1f7f6cd46ea`](#n_0x6551b1f7f6cd46ea) · [`N_0x678f86d8fc040bdb`](#n_0x678f86d8fc040bdb) · [`N_0x6a60e43998228229`](#n_0x6a60e43998228229) · [`N_0x6a7f19756f1a9016`](#n_0x6a7f19756f1a9016) · [`N_0x6bc0acd0673acebe`](#n_0x6bc0acd0673acebe) · [`N_0x6bccf9948492fd85`](#n_0x6bccf9948492fd85) · [`N_0x6dee77aff8c21bd1`](#n_0x6dee77aff8c21bd1) · [`N_0x6e0a5253375c4584`](#n_0x6e0a5253375c4584) · [`N_0x6f361b8889a792a3`](#n_0x6f361b8889a792a3) · [`N_0x7033eefd9b28088e`](#n_0x7033eefd9b28088e) · [`N_0x71b008056e5692d6`](#n_0x71b008056e5692d6) · [`N_0x723c1ce13fbfdb67`](#n_0x723c1ce13fbfdb67) · [`N_0x73001e34f85137f8`](#n_0x73001e34f85137f8) · [`N_0x79d310a861697cc9`](#n_0x79d310a861697cc9) · [`N_0x7b18da61f6bae9d5`](#n_0x7b18da61f6bae9d5) · [`N_0x7d36291161859389`](#n_0x7d36291161859389) · [`N_0x7d8ba05688ad64c7`](#n_0x7d8ba05688ad64c7) · [`N_0x7e6946f68a38b74f`](#n_0x7e6946f68a38b74f) · [`N_0x7eec2a316c250073`](#n_0x7eec2a316c250073) · [`N_0x7f2c4cdf2e82df4c`](#n_0x7f2c4cdf2e82df4c) · [`N_0x810b5fcc52ec7ff0`](#n_0x810b5fcc52ec7ff0) · [`N_0x830c3a44eb3f2cf9`](#n_0x830c3a44eb3f2cf9) · [`N_0x84a810b375e69c0e`](#n_0x84a810b375e69c0e) · [`N_0x84dfc579c2fc214c`](#n_0x84dfc579c2fc214c) · [`N_0x88087ee1f28024ae`](#n_0x88087ee1f28024ae) · [`N_0x88578f6ec36b4a3a`](#n_0x88578f6ec36b4a3a) · [`N_0x8989cbd7b4e82534`](#n_0x8989cbd7b4e82534) · [`N_0x8b9cdbd6c566c38c`](#n_0x8b9cdbd6c566c38c) · [`N_0x8c9d11605e59d955`](#n_0x8c9d11605e59d955) · [`N_0x8d8adb562f09a245`](#n_0x8d8adb562f09a245) · [`N_0x8ec74ceb042e7cff`](#n_0x8ec74ceb042e7cff) · [`N_0x92fc0eedfac04a14`](#n_0x92fc0eedfac04a14) · [`N_0x930f504203f561c9`](#n_0x930f504203f561c9) · [`N_0x96e6d5150dbf1c09`](#n_0x96e6d5150dbf1c09) · [`N_0x98e2bc1ca26287c3`](#n_0x98e2bc1ca26287c3) · [`N_0x9a62ec95ae10e011`](#n_0x9a62ec95ae10e011) · [`N_0x9b4bd21d69b1e609`](#n_0x9b4bd21d69b1e609) · [`N_0x9ec8858184cd253a`](#n_0x9ec8858184cd253a) · [`N_0xa0f93d5465b3094d`](#n_0xa0f93d5465b3094d) · [`N_0xa3c53804bdb68ed2`](#n_0xa3c53804bdb68ed2) · [`N_0xa6f54bb2ffca35ea`](#n_0xa6f54bb2ffca35ea) · [`N_0xa736cf7fb7c5bff4`](#n_0xa736cf7fb7c5bff4) · [`N_0xa761d4ac6115623d`](#n_0xa761d4ac6115623d) · [`N_0xa78b8fa58200da56`](#n_0xa78b8fa58200da56) · [`N_0xa8733668d1047b51`](#n_0xa8733668d1047b51) · [`N_0xa943fd1722e11efd`](#n_0xa943fd1722e11efd) · [`N_0xaa525dff66bb82f5`](#n_0xaa525dff66bb82f5) · [`N_0xaff47709f1d5dcce`](#n_0xaff47709f1d5dcce) · [`N_0xb1d2bb1e1631f5b1`](#n_0xb1d2bb1e1631f5b1) · [`N_0xb26f670685631727`](#n_0xb26f670685631727) · [`N_0xb3da2606774a8e2d`](#n_0xb3da2606774a8e2d) · [`N_0xba9749cc94c1fd85`](#n_0xba9749cc94c1fd85) · [`N_0xbaa2f0490e146be8`](#n_0xbaa2f0490e146be8) · [`N_0xbe3db208333d9844`](#n_0xbe3db208333d9844) · [`N_0xbed9f5693f34ed17`](#n_0xbed9f5693f34ed17) · [`N_0xbf371cd2b64212fd`](#n_0xbf371cd2b64212fd) · [`N_0xbfafdb5faaa5c5ab`](#n_0xbfafdb5faaa5c5ab) · [`N_0xc01d2470f22cde5a`](#n_0xc01d2470f22cde5a) · [`N_0xc03fab2c2f92289b`](#n_0xc03fab2c2f92289b) · [`N_0xc0e0d686ddfc6eae`](#n_0xc0e0d686ddfc6eae) · [`N_0xc141b8917e0017ec`](#n_0xc141b8917e0017ec) · [`N_0xc14bd9f5337219b2`](#n_0xc14bd9f5337219b2) · [`N_0xc1e963c58664b556`](#n_0xc1e963c58664b556) · [`N_0xc67e2da1cbe759e2`](#n_0xc67e2da1cbe759e2) · [`N_0xc6e0e2616a7576bb`](#n_0xc6e0e2616a7576bb) · [`N_0xc847b43f369ac0b5`](#n_0xc847b43f369ac0b5) · [`N_0xcc25a4553dfbf9ea`](#n_0xcc25a4553dfbf9ea) · [`N_0xd1a1ee3b4fa8e760`](#n_0xd1a1ee3b4fa8e760) · [`N_0xd1c9b92bdd3f151d`](#n_0xd1c9b92bdd3f151d) · [`N_0xd4367d310f079db0`](#n_0xd4367d310f079db0) · [`N_0xd558bec0bba7e8d2`](#n_0xd558bec0bba7e8d2) · [`N_0xd6ca58b3b53a0f22`](#n_0xd6ca58b3b53a0f22) · [`N_0xdaf80797fc534bec`](#n_0xdaf80797fc534bec) · [`N_0xdeaaf77eb3687e97`](#n_0xdeaaf77eb3687e97) · [`N_0xdfbd93bf2943e29b`](#n_0xdfbd93bf2943e29b) · [`N_0xdfcdb14317a9b361`](#n_0xdfcdb14317a9b361) · [`N_0xe3261d791eb44acb`](#n_0xe3261d791eb44acb) · [`N_0xe496a53ba5f50a56`](#n_0xe496a53ba5f50a56) · [`N_0xe8853fbce7d8d0d6`](#n_0xe8853fbce7d8d0d6) · [`N_0xecb41ac6ab754401`](#n_0xecb41ac6ab754401) · [`N_0xedbf6c9b0d2c65c8`](#n_0xedbf6c9b0d2c65c8) · [`N_0xf06a6f41cb445443`](#n_0xf06a6f41cb445443) · [`N_0xf11f01d98113536a`](#n_0xf11f01d98113536a) · [`N_0xf1a1803d3476f215`](#n_0xf1a1803d3476f215) · [`N_0xf534d94dfa2ead26`](#n_0xf534d94dfa2ead26) · [`N_0xf8c54a461c3e11dc`](#n_0xf8c54a461c3e11dc) · [`N_0xf9096193df1f99d4`](#n_0xf9096193df1f99d4) · [`N_0xf9f2922717b819ec`](#n_0xf9f2922717b819ec) · [`N_0xfcc228e07217fcac`](#n_0xfcc228e07217fcac) · [`OrderedBossVehicle`](#orderedbossvehicle) · [`PlaystatsAcquiredHiddenPackage`](#playstatsacquiredhiddenpackage) · [`PlaystatsActivityDone`](#playstatsactivitydone) · [`PlaystatsArcadegame`](#playstatsarcadegame) · [`PlaystatsArenaWarSpectator`](#playstatsarenawarspectator) · [`PlaystatsArenaWarsEnded`](#playstatsarenawarsended) · [`PlaystatsAwardBadsport`](#playstatsawardbadsport) · [`PlaystatsAwardXp`](#playstatsawardxp) · [`PlaystatsBackgroundScriptAction`](#playstatsbackgroundscriptaction) · [`PlaystatsBanAlert`](#playstatsbanalert) · [`PlaystatsBuyContraband`](#playstatsbuycontraband) · [`PlaystatsCarclubChallenge`](#playstatscarclubchallenge) · [`PlaystatsCarclubPoints`](#playstatscarclubpoints) · [`PlaystatsCarclubPrize`](#playstatscarclubprize) · [`PlaystatsCasinoBlackjack`](#playstatscasinoblackjack) · [`PlaystatsCasinoBlackjackLight`](#playstatscasinoblackjacklight) · [`PlaystatsCasinoChip`](#playstatscasinochip) · [`PlaystatsCasinoInsidetrack`](#playstatscasinoinsidetrack) · [`PlaystatsCasinoInsidetrackLight`](#playstatscasinoinsidetracklight) · [`PlaystatsCasinoLuckyseven`](#playstatscasinoluckyseven) · [`PlaystatsCasinoMissionEnded`](#playstatscasinomissionended) · [`PlaystatsCasinoRoulette`](#playstatscasinoroulette) · [`PlaystatsCasinoRouletteLight`](#playstatscasinoroulettelight) · [`PlaystatsCasinoSlotmachine`](#playstatscasinoslotmachine) · [`PlaystatsCasinoSlotmachineLight`](#playstatscasinoslotmachinelight) · [`PlaystatsCasinoStoryMissionEnded`](#playstatscasinostorymissionended) · [`PlaystatsCasinoThreecardpoker`](#playstatscasinothreecardpoker) · [`PlaystatsCasinoThreecardpokerLight`](#playstatscasinothreecardpokerlight) · [`PlaystatsChangeMcEmblem`](#playstatschangemcemblem) · [`PlaystatsCheatApplied`](#playstatscheatapplied) · [`PlaystatsClothChange`](#playstatsclothchange) · [`PlaystatsCollectible`](#playstatscollectible) · [`PlaystatsCopyRankIntoNewSlot`](#playstatscopyrankintonewslot) · [`PlaystatsCrateCreated`](#playstatscratecreated) · [`PlaystatsCrateDropMissionDone`](#playstatscratedropmissiondone) · [`PlaystatsDarMissionEnd`](#playstatsdarmissionend) · [`PlaystatsDefendContraband`](#playstatsdefendcontraband) · [`PlaystatsDirectorMode`](#playstatsdirectormode) · [`PlaystatsDroneUsage`](#playstatsdroneusage) · [`PlaystatsDupeDetection`](#playstatsdupedetection) · [`PlaystatsEarnedMcPoints`](#playstatsearnedmcpoints) · [`PlaystatsEnterSessionPack`](#playstatsentersessionpack) · [`PlaystatsExtraEvent`](#playstatsextraevent) · [`PlaystatsFriendActivity`](#playstatsfriendactivity) · [`PlaystatsGunrunMissionEnded`](#playstatsgunrunmissionended) · [`PlaystatsH2FmprepEnd`](#playstatsh2fmprepend) · [`PlaystatsH2InstanceEnd`](#playstatsh2instanceend) · [`PlaystatsHeistSaveCheat`](#playstatsheistsavecheat) · [`PlaystatsHoldUpMissionDone`](#playstatsholdupmissiondone) · [`PlaystatsIdleKick`](#playstatsidlekick) · [`PlaystatsImportExportMissionDone`](#playstatsimportexportmissiondone) · [`PlaystatsInventory`](#playstatsinventory) · [`PlaystatsJobBend`](#playstatsjobbend) · [`PlaystatsLeaveJobChain`](#playstatsleavejobchain) · [`PlaystatsMatchStarted`](#playstatsmatchstarted) · [`PlaystatsMissionCheckpoint`](#playstatsmissioncheckpoint) · [`PlaystatsMissionOver`](#playstatsmissionover) · [`PlaystatsMissionStarted`](#playstatsmissionstarted) · [`PlaystatsNpcInvite`](#playstatsnpcinvite) · [`PlaystatsOddjobDone`](#playstatsoddjobdone) · [`PlaystatsPassiveMode`](#playstatspassivemode) · [`PlaystatsPegasaircraft`](#playstatspegasaircraft) · [`PlaystatsPiMenuHideSettings`](#playstatspimenuhidesettings) · [`PlaystatsPropChange`](#playstatspropchange) · [`PlaystatsQuickfixTool`](#playstatsquickfixtool) · [`PlaystatsRaceCheckpoint`](#playstatsracecheckpoint) · [`PlaystatsRaceToPointMissionDone`](#playstatsracetopointmissiondone) · [`PlaystatsRandomMissionDone`](#playstatsrandommissiondone) · [`PlaystatsRankUp`](#playstatsrankup) · [`PlaystatsRecoverContraband`](#playstatsrecovercontraband) · [`PlaystatsRobberyFinale`](#playstatsrobberyfinale) · [`PlaystatsRobberyPrep`](#playstatsrobberyprep) · [`PlaystatsRosBet`](#playstatsrosbet) · [`PlaystatsSellContraband`](#playstatssellcontraband) · [`PlaystatsSetJoinType`](#playstatssetjointype) · [`PlaystatsShopItem`](#playstatsshopitem) · [`PlaystatsSmugMissionEnded`](#playstatssmugmissionended) · [`PlaystatsSpectatorWheelSpin`](#playstatsspectatorwheelspin) · [`PlaystatsSpentPiCustomLoadout`](#playstatsspentpicustomloadout) · [`PlaystatsStartOfflineMode`](#playstatsstartofflinemode) · [`PlaystatsStartTrackingStunts`](#playstatsstarttrackingstunts) · [`PlaystatsStoneHatchetEnd`](#playstatsstonehatchetend) · [`PlaystatsStopTrackingStunts`](#playstatsstoptrackingstunts) · [`PlaystatsWeaponModeChange`](#playstatsweaponmodechange) · [`PlaystatsWebsiteVisited`](#playstatswebsitevisited) · [`PresenceEventUpdatestatFloat`](#presenceeventupdatestatfloat) · [`PresenceEventUpdatestatInt`](#presenceeventupdatestatint) · [`SetHasContentUnlocksFlags`](#sethascontentunlocksflags) · [`SetProfileSettingPrologueComplete`](#setprofilesettingprologuecomplete) · [`SetSaveMigrationTransactionId`](#setsavemigrationtransactionid) · [`StatClearSlotForReload`](#statclearslotforreload) · [`StatDeleteSlot`](#statdeleteslot) · [`StatGetBool`](#statgetbool) · [`StatGetBoolMasked`](#statgetboolmasked) · [`StatGetCancelSaveMigrationStatus`](#statgetcancelsavemigrationstatus) · [`StatGetDate`](#statgetdate) · [`StatGetFloat`](#statgetfloat) · [`StatGetInt`](#statgetint) · [`StatGetLicensePlate`](#statgetlicenseplate) · [`StatGetMaskedInt`](#statgetmaskedint) · [`StatGetNumberOfDays`](#statgetnumberofdays) · [`StatGetNumberOfHours`](#statgetnumberofhours) · [`StatGetNumberOfMinutes`](#statgetnumberofminutes) · [`StatGetNumberOfSeconds`](#statgetnumberofseconds) · [`StatGetPackedBoolMask`](#statgetpackedboolmask) · [`StatGetPackedIntMask`](#statgetpackedintmask) · [`StatGetPos`](#statgetpos) · [`StatGetSaveMigrationConsumeContentUnlockStatus`](#statgetsavemigrationconsumecontentunlockstatus) · [`StatGetSaveMigrationStatus`](#statgetsavemigrationstatus) · [`StatGetString`](#statgetstring) · [`StatGetUserId`](#statgetuserid) · [`StatIncrement`](#statincrement) · [`StatLoad`](#statload) · [`StatLoadPending`](#statloadpending) · [`StatMigrateSave`](#statmigratesave) · [`StatSave`](#statsave) · [`StatSaveMigrationCancel`](#statsavemigrationcancel) · [`StatSaveMigrationConsumeContentUnlock`](#statsavemigrationconsumecontentunlock) · [`StatSaveMigrationStatusStart`](#statsavemigrationstatusstart) · [`StatSavePending`](#statsavepending) · [`StatSavePendingOrRequested`](#statsavependingorrequested) · [`StatSetBlockSaves`](#statsetblocksaves) · [`StatSetBool`](#statsetbool) · [`StatSetBoolMasked`](#statsetboolmasked) · [`StatSetCheatIsActive`](#statsetcheatisactive) · [`StatSetCurrentPosixTime`](#statsetcurrentposixtime) · [`StatSetDate`](#statsetdate) · [`StatSetFloat`](#statsetfloat) · [`StatSetGxtLabel`](#statsetgxtlabel) · [`StatSetInt`](#statsetint) · [`StatSetLicensePlate`](#statsetlicenseplate) · [`StatSetMaskedInt`](#statsetmaskedint) · [`StatSetPos`](#statsetpos) · [`StatSetProfileSettingValue`](#statsetprofilesettingvalue) · [`StatSetString`](#statsetstring) · [`StatSetUserId`](#statsetuserid) · [`StatSlotIsLoaded`](#statslotisloaded)

---
### GetNgstatBoolHash

`_GET_NGSTAT_BOOL_HASH` · hash `0xBA52FF538ED2BC71` · **Cliente**

```lua
local retval = GetNgstatBoolHash(index, spStat, charStat, character, section)
```
```c
Hash _GET_NGSTAT_BOOL_HASH(int index, BOOL spStat, BOOL charStat, int character, char* section);
```

**Parámetros**

- `index` (`int`)
- `spStat` (`BOOL`)
- `charStat` (`BOOL`)
- `character` (`int`)
- `section` (`char*`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Needs more research. Gets the stat name of a masked bool?
section - values used in the decompiled scripts:
"_NGPSTAT_BOOL"
"_NGTATPSTAT_BOOL"
"_NGDLCPSTAT_BOOL"
"_DLCBIKEPSTAT_BOOL"
"_DLCGUNPSTAT_BOOL"
"_GUNTATPSTAT_BOOL"
"_DLCSMUGCHARPSTAT_BOOL"
"_GANGOPSPSTAT_BOOL"
"_BUSINESSBATPSTAT_BOOL"
"_ARENAWARSPSTAT_BOOL"
"_CASINOPSTAT_BOOL"
"_CASINOHSTPSTAT_BOOL"
"_HEIST3TATTOOSTAT_BOOL"
```

**Nombres antiguos (alias):** `0xBA52FF538ED2BC71` (`N_0xba52ff538ed2bc71`)

---
### GetNgstatIntHash

`_GET_NGSTAT_INT_HASH` · hash `0x2B4CDCA6F07FF3DA` · **Cliente**

```lua
local retval = GetNgstatIntHash(index, spStat, charStat, character, section)
```
```c
Hash _GET_NGSTAT_INT_HASH(int index, BOOL spStat, BOOL charStat, int character, char* section);
```

**Parámetros**

- `index` (`int`)
- `spStat` (`BOOL`)
- `charStat` (`BOOL`)
- `character` (`int`)
- `section` (`char*`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Needs more research. Gets the stat name of a masked int?
section - values used in the decompiled scripts:
"_NGPSTAT_INT"
"_MP_NGPSTAT_INT"
"_MP_LRPSTAT_INT"
"_MP_APAPSTAT_INT"
"_MP_LR2PSTAT_INT"
"_MP_BIKEPSTAT_INT"
"_MP_IMPEXPPSTAT_INT"
"_MP_GUNRPSTAT_INT"
"_NGDLCPSTAT_INT"
"_MP_NGDLCPSTAT_INT"
"_DLCSMUGCHARPSTAT_INT"
"_GANGOPSPSTAT_INT"
"_BUSINESSBATPSTAT_INT"
"_ARENAWARSPSTAT_INT"
"_CASINOPSTAT_INT"
"_CASINOHSTPSTAT_INT"
```

**Nombres antiguos (alias):** `0x2B4CDCA6F07FF3DA` (`N_0x2b4cdca6f07ff3da`)

---
### GetPackedBoolStatKey

`GET_PACKED_BOOL_STAT_KEY` · hash `0x80C75307B1C42837` · jhash `0xB5BF87B2` · **Cliente**

```lua
local retval = GetPackedBoolStatKey(index, spStat, charStat, character)
```
```c
Hash GET_PACKED_BOOL_STAT_KEY(int index, BOOL spStat, BOOL charStat, int character);
```

**Parámetros**

- `index` (`int`)
- `spStat` (`BOOL`)
- `charStat` (`BOOL`)
- `character` (`int`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0x80C75307B1C42837` (`N_0x80c75307b1c42837`), `_GET_PSTAT_BOOL_HASH` (`GetPstatBoolHash`)

---
### GetPackedIntStatKey

`GET_PACKED_INT_STAT_KEY` · hash `0x61E111E323419E07` · jhash `0x1F938864` · **Cliente**

```lua
local retval = GetPackedIntStatKey(index, spStat, charStat, character)
```
```c
Hash GET_PACKED_INT_STAT_KEY(int index, BOOL spStat, BOOL charStat, int character);
```

**Parámetros**

- `index` (`int`)
- `spStat` (`BOOL`)
- `charStat` (`BOOL`)
- `character` (`int`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0x61E111E323419E07` (`N_0x61e111e323419e07`), `_GET_PSTAT_INT_HASH` (`GetPstatIntHash`)

---
### GetPackedTuBoolStatKey

`GET_PACKED_TU_BOOL_STAT_KEY` · hash `0xC4BB08EE7907471E` · jhash `0x3F8E893B` · **Cliente**

```lua
local retval = GetPackedTuBoolStatKey(index, spStat, charStat, character)
```
```c
Hash GET_PACKED_TU_BOOL_STAT_KEY(int index, BOOL spStat, BOOL charStat, int character);
```

**Parámetros**

- `index` (`int`)
- `spStat` (`BOOL`)
- `charStat` (`BOOL`)
- `character` (`int`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0xC4BB08EE7907471E` (`N_0xc4bb08ee7907471e`), `_GET_TUPSTAT_BOOL_HASH` (`GetTupstatBoolHash`), `_GET_PACKED_TITLE_UPDATE_BOOL_STAT_KEY` (`GetPackedTitleUpdateBoolStatKey`)

---
### GetPackedTuIntStatKey

`GET_PACKED_TU_INT_STAT_KEY` · hash `0xD16C2AD6B8E32854` · jhash `0xFB93C5A2` · **Cliente**

```lua
local retval = GetPackedTuIntStatKey(index, spStat, charStat, character)
```
```c
Hash GET_PACKED_TU_INT_STAT_KEY(int index, BOOL spStat, BOOL charStat, int character);
```

**Parámetros**

- `index` (`int`)
- `spStat` (`BOOL`)
- `charStat` (`BOOL`)
- `character` (`int`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0xD16C2AD6B8E32854` (`N_0xd16c2ad6b8e32854`), `_GET_TUPSTAT_INT_HASH` (`GetTupstatIntHash`), `_GET_PACKED_TITLE_UPDATE_INT_STAT_KEY` (`GetPackedTitleUpdateIntStatKey`)

---
### HiredLimo

`_HIRED_LIMO` · hash `0x792271AB35C356A4` · **Cliente**

```lua
HiredLimo(p0, p1)
```
```c
void _HIRED_LIMO(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x792271AB35C356A4` (`N_0x792271ab35c356a4`)

---
### Leaderboards2ReadByHandle

`LEADERBOARDS2_READ_BY_HANDLE` · hash `0xC30713A383BFBF0E` · jhash `0x6B553408` · **Cliente**

```lua
local retval, p0, p1 = Leaderboards2ReadByHandle()
```
```c
BOOL LEADERBOARDS2_READ_BY_HANDLE(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### Leaderboards2ReadByPlatform

`_LEADERBOARDS2_READ_BY_PLATFORM` · hash `0xF1AE5DCDBFCA2721` · **Cliente**

```lua
local retval, p0 = Leaderboards2ReadByPlatform(gamerHandleCsv, platformName)
```
```c
BOOL _LEADERBOARDS2_READ_BY_PLATFORM(Any* p0, char* gamerHandleCsv, char* platformName);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `gamerHandleCsv` (`char*`)
- `platformName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF1AE5DCDBFCA2721` (`N_0xf1ae5dcdbfca2721`)

---
### Leaderboards2ReadByRadius

`LEADERBOARDS2_READ_BY_RADIUS` · hash `0x5CE587FB5A42C8C4` · jhash `0xC5B7E685` · **Cliente**

```lua
local retval, p0, p2 = Leaderboards2ReadByRadius(p1)
```
```c
BOOL LEADERBOARDS2_READ_BY_RADIUS(Any* p0, Any p1, Any* p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### Leaderboards2ReadByRank

`LEADERBOARDS2_READ_BY_RANK` · hash `0xBA2C7DB0C129449A` · jhash `0x1B03F59F` · **Cliente**

```lua
local retval, p0 = Leaderboards2ReadByRank(p1, p2)
```
```c
BOOL LEADERBOARDS2_READ_BY_RANK(Any* p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### Leaderboards2ReadByRow

`LEADERBOARDS2_READ_BY_ROW` · hash `0xA9CDB1E3F0A49883` · jhash `0xCA931F34` · **Cliente**

```lua
local retval, p0, p1, p3, p5 = Leaderboards2ReadByRow(p2, p4, p6)
```
```c
BOOL LEADERBOARDS2_READ_BY_ROW(Any* p0, Any* p1, Any p2, Any* p3, Any p4, Any* p5, Any p6);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any`)
- `p5` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p6` (`Any`)

**Devuelve:** `BOOL`

---
### Leaderboards2ReadByScoreFloat

`LEADERBOARDS2_READ_BY_SCORE_FLOAT` · hash `0xE662C8B759D08F3C` · jhash `0xC678B29F` · **Cliente**

```lua
local retval, p0 = Leaderboards2ReadByScoreFloat(p1, p2)
```
```c
BOOL LEADERBOARDS2_READ_BY_SCORE_FLOAT(Any* p0, float p1, Any p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`float`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### Leaderboards2ReadByScoreInt

`LEADERBOARDS2_READ_BY_SCORE_INT` · hash `0x7EEC7E4F6984A16A` · jhash `0xAC020C18` · **Cliente**

```lua
local retval, p0 = Leaderboards2ReadByScoreInt(p1, p2)
```
```c
BOOL LEADERBOARDS2_READ_BY_SCORE_INT(Any* p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### Leaderboards2ReadFriendsByRow

`LEADERBOARDS2_READ_FRIENDS_BY_ROW` · hash `0x918B101666F9CB83` · jhash `0xBD91B136` · **Cliente**

```lua
local retval, p0, p1 = Leaderboards2ReadFriendsByRow(p2, p3, p4, p5)
```
```c
BOOL LEADERBOARDS2_READ_FRIENDS_BY_ROW(Any* p0, Any* p1, Any p2, BOOL p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`BOOL`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `BOOL`

---
### Leaderboards2ReadRankPrediction

`LEADERBOARDS2_READ_RANK_PREDICTION` · hash `0xC38DC1E90D22547C` · jhash `0x9BEC3401` · **Cliente**

```lua
local retval, p0, p1, p2 = Leaderboards2ReadRankPrediction()
```
```c
BOOL LEADERBOARDS2_READ_RANK_PREDICTION(Any* p0, Any* p1, Any* p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC38DC1E90D22547C` (`N_0xc38dc1e90d22547c`)

---
### Leaderboards2WriteData

`LEADERBOARDS2_WRITE_DATA` · hash `0xAE2206545888AE49` · jhash `0x5F9DF634` · **Cliente**

```lua
local retval, p0 = Leaderboards2WriteData(p0)
```
```c
BOOL LEADERBOARDS2_WRITE_DATA(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### Leaderboards2WriteDataForEventType

`LEADERBOARDS2_WRITE_DATA_FOR_EVENT_TYPE` · hash `0xC980E62E33DF1D5C` · jhash `0x62C19A3D` · **Cliente**

```lua
local retval, p0, p1 = Leaderboards2WriteDataForEventType()
```
```c
BOOL LEADERBOARDS2_WRITE_DATA_FOR_EVENT_TYPE(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC980E62E33DF1D5C` (`N_0xc980e62e33df1d5c`)

---
### LeaderboardsCacheDataRow

`LEADERBOARDS_CACHE_DATA_ROW` · hash `0xB9BB18E2C40142ED` · jhash `0x44F7D82B` · **Cliente**

```lua
local retval, p0 = LeaderboardsCacheDataRow(p0)
```
```c
BOOL LEADERBOARDS_CACHE_DATA_ROW(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### LeaderboardsClearCacheData

`LEADERBOARDS_CLEAR_CACHE_DATA` · hash `0xD4B02A6B476E1FDC` · jhash `0x87F498C1` · **Cliente**

```lua
LeaderboardsClearCacheData()
```
```c
void LEADERBOARDS_CLEAR_CACHE_DATA();
```

**Devuelve:** `void`

---
### LeaderboardsDeaths

`_LEADERBOARDS_DEATHS` · hash `0x428EAF89E24F6C36` · jhash `0xEE292B91` · **Cliente**

```lua
LeaderboardsDeaths(statName, value)
```
```c
void _LEADERBOARDS_DEATHS(Hash statName, float value);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x428EAF89E24F6C36` (`N_0x428eaf89e24f6c36`)

---
### LeaderboardsGetCacheDataRow

`LEADERBOARDS_GET_CACHE_DATA_ROW` · hash `0x9120E8DBA3D69273` · jhash `0xA11289EC` · **Cliente**

```lua
local retval, p2 = LeaderboardsGetCacheDataRow(p0, p1, p2)
```
```c
BOOL LEADERBOARDS_GET_CACHE_DATA_ROW(Any p0, Any p1, Any* p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### LeaderboardsGetCacheExists

`LEADERBOARDS_GET_CACHE_EXISTS` · hash `0x9C51349BE6CDFE2C` · jhash `0xFC8A71F3` · **Cliente**

```lua
local retval = LeaderboardsGetCacheExists(p0)
```
```c
BOOL LEADERBOARDS_GET_CACHE_EXISTS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### LeaderboardsGetCacheNumberOfRows

`LEADERBOARDS_GET_CACHE_NUMBER_OF_ROWS` · hash `0x58A651CD201D89AD` · jhash `0xCE7CB520` · **Cliente**

```lua
local retval = LeaderboardsGetCacheNumberOfRows(p0)
```
```c
int LEADERBOARDS_GET_CACHE_NUMBER_OF_ROWS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x58A651CD201D89AD` (`N_0x58a651cd201d89ad`)

---
### LeaderboardsGetCacheTime

`LEADERBOARDS_GET_CACHE_TIME` · hash `0xF04C1C27DA35F6C8` · jhash `0xEDF02302` · **Cliente**

```lua
local retval = LeaderboardsGetCacheTime(p0)
```
```c
Any LEADERBOARDS_GET_CACHE_TIME(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### LeaderboardsGetColumnId

`LEADERBOARDS_GET_COLUMN_ID` · hash `0xC4B5467A1886EA7E` · jhash `0x3821A334` · **Cliente**

```lua
local retval = LeaderboardsGetColumnId(p0, p1, p2)
```
```c
Any LEADERBOARDS_GET_COLUMN_ID(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### LeaderboardsGetColumnType

`LEADERBOARDS_GET_COLUMN_TYPE` · hash `0xBF4FEF46DB7894D3` · jhash `0x6F2820F4` · **Cliente**

```lua
local retval = LeaderboardsGetColumnType(p0, p1, p2)
```
```c
Any LEADERBOARDS_GET_COLUMN_TYPE(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### LeaderboardsGetNumberOfColumns

`LEADERBOARDS_GET_NUMBER_OF_COLUMNS` · hash `0x117B45156D7EFF2E` · jhash `0x0A56EE34` · **Cliente**

```lua
local retval = LeaderboardsGetNumberOfColumns(p0, p1)
```
```c
Any LEADERBOARDS_GET_NUMBER_OF_COLUMNS(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### LeaderboardsReadAnyPending

`LEADERBOARDS_READ_ANY_PENDING` · hash `0xA31FD15197B192BD` · jhash `0x1789437B` · **Cliente**

```lua
local retval = LeaderboardsReadAnyPending()
```
```c
BOOL LEADERBOARDS_READ_ANY_PENDING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA31FD15197B192BD` (`N_0xa31fd15197b192bd`)

---
### LeaderboardsReadClear

`LEADERBOARDS_READ_CLEAR` · hash `0x7CCE5C737A665701` · jhash `0x7090012F` · **Cliente**

```lua
local retval = LeaderboardsReadClear(p0, p1, p2)
```
```c
Any LEADERBOARDS_READ_CLEAR(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### LeaderboardsReadClearAll

`LEADERBOARDS_READ_CLEAR_ALL` · hash `0xA34CB6E6F0DF4A0B` · jhash `0x233E058A` · **Cliente**

```lua
local retval = LeaderboardsReadClearAll()
```
```c
Any LEADERBOARDS_READ_CLEAR_ALL();
```

**Devuelve:** `Any`

---
### LeaderboardsReadPending

`LEADERBOARDS_READ_PENDING` · hash `0xAC392C8483342AC2` · jhash `0xEEB8BF5C` · **Cliente**

```lua
local retval = LeaderboardsReadPending(p0, p1, p2)
```
```c
BOOL LEADERBOARDS_READ_PENDING(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### LeaderboardsReadSuccessful

`LEADERBOARDS_READ_SUCCESSFUL` · hash `0x2FB19228983E832C` · jhash `0x3AC5B2F1` · **Cliente**

```lua
local retval = LeaderboardsReadSuccessful(p0, p1, p2)
```
```c
BOOL LEADERBOARDS_READ_SUCCESSFUL(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### LeaderboardsWriteAddColumn

`LEADERBOARDS_WRITE_ADD_COLUMN` · hash `0x0BCA1D2C47B0D269` · jhash `0x7524E27B` · **Cliente**

```lua
LeaderboardsWriteAddColumn(p0, p1, p2)
```
```c
void LEADERBOARDS_WRITE_ADD_COLUMN(Any p0, Any p1, float p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0BCA1D2C47B0D269` (`N_0x0bca1d2c47b0d269`)

---
### LeaderboardsWriteAddColumnLong

`LEADERBOARDS_WRITE_ADD_COLUMN_LONG` · hash `0x2E65248609523599` · jhash `0x1C5CCC3A` · **Cliente**

```lua
LeaderboardsWriteAddColumnLong(p0, p1, p2)
```
```c
void LEADERBOARDS_WRITE_ADD_COLUMN_LONG(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2E65248609523599` (`N_0x2e65248609523599`)

---
### N_0x0077f15613d36993

`0x0077F15613D36993` · hash `0x0077F15613D36993` · **Cliente**

```lua
N_0x0077f15613d36993(p0, p1, p2, p3)
```
```c
void 0x0077F15613D36993(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x015b03ee1c43e6ec

`0x015B03EE1C43E6EC` · hash `0x015B03EE1C43E6EC` · **Cliente**

```lua
N_0x015b03ee1c43e6ec(p0)
```
```c
void 0x015B03EE1C43E6EC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x03c2eebb04b3fb72

`0x03C2EEBB04B3FB72` · hash `0x03C2EEBB04B3FB72` · **Cliente**

```lua
N_0x03c2eebb04b3fb72(p0, p1, p2, p3, p4, p5, p6)
```
```c
void 0x03C2EEBB04B3FB72(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### N_0x06eaf70ae066441e

`0x06EAF70AE066441E` · hash `0x06EAF70AE066441E` · **Cliente**

```lua
N_0x06eaf70ae066441e(p0)
```
```c
void 0x06EAF70AE066441E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x0a9c7f36e5d7b683

`0x0A9C7F36E5D7B683` · hash `0x0A9C7F36E5D7B683` · **Cliente**

```lua
N_0x0a9c7f36e5d7b683(p0)
```
```c
void 0x0A9C7F36E5D7B683(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x0b565b0aae56a0e8

`0x0B565B0AAE56A0E8` · hash `0x0B565B0AAE56A0E8` · **Cliente**

```lua
N_0x0b565b0aae56a0e8(p0, p1, p2, p3, p4, p5, p6)
```
```c
void 0x0B565B0AAE56A0E8(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### N_0x0b8b7f74bf061c6d

`0x0B8B7F74BF061C6D` · hash `0x0B8B7F74BF061C6D` · **Cliente**

```lua
local retval = N_0x0b8b7f74bf061c6d()
```
```c
Any 0x0B8B7F74BF061C6D();
```

**Devuelve:** `Any`

---
### N_0x0d01d20616fc73fb

`0x0D01D20616FC73FB` · hash `0x0D01D20616FC73FB` · jhash `0x2180AE13` · **Cliente**

```lua
N_0x0d01d20616fc73fb(p0, p1)
```
```c
void 0x0D01D20616FC73FB(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x14e0b2d1ad1044e0

`0x14E0B2D1AD1044E0` · hash `0x14E0B2D1AD1044E0` · jhash `0xDDD1F1F3` · **Cliente**

```lua
local p0, p1, p2, p3 = N_0x14e0b2d1ad1044e0()
```
```c
void 0x14E0B2D1AD1044E0(Any* p0, Any* p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### N_0x14eda9ee27bd1626

`0x14EDA9EE27BD1626` · hash `0x14EDA9EE27BD1626` · **Cliente**

```lua
N_0x14eda9ee27bd1626(p0)
```
```c
void 0x14EDA9EE27BD1626(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x164c5ff663790845

`0x164C5FF663790845` · hash `0x164C5FF663790845` · **Cliente**

```lua
N_0x164c5ff663790845(p0)
```
```c
void 0x164C5FF663790845(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x1a7ce7cd3e653485

`0x1A7CE7CD3E653485` · hash `0x1A7CE7CD3E653485` · **Cliente**

```lua
N_0x1a7ce7cd3e653485(p0)
```
```c
void 0x1A7CE7CD3E653485(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x1a8ea222f9c67dbb

`0x1A8EA222F9C67DBB` · hash `0x1A8EA222F9C67DBB` · **Cliente**

```lua
local retval, p0 = N_0x1a8ea222f9c67dbb(p0)
```
```c
Any 0x1A8EA222F9C67DBB(float* p0);
```

**Parámetros**

- `p0` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0x26d7399b9587fe89

`0x26D7399B9587FE89` · hash `0x26D7399B9587FE89` · jhash `0x343B27E2` · **Cliente**

```lua
N_0x26d7399b9587fe89(p0)
```
```c
void 0x26D7399B9587FE89(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
STATS::0x343B27E2(0);  
STATS::0x343B27E2(1);  
STATS::0x343B27E2(2);  
STATS::0x343B27E2(3);  
STATS::0x343B27E2(4);  
STATS::0x343B27E2(5);  
STATS::0x343B27E2(6);  
STATS::0x343B27E2(7);  
Identical in ingamehud & maintransition.  
```

---
### N_0x27aa1c973cacfe63

`0x27AA1C973CACFE63` · hash `0x27AA1C973CACFE63` · **Cliente**

```lua
N_0x27aa1c973cacfe63(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void 0x27AA1C973CACFE63(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`Any`)

**Devuelve:** `void`

---
### N_0x2818ff6638cb09de

`0x2818FF6638CB09DE` · hash `0x2818FF6638CB09DE` · **Cliente**

```lua
N_0x2818ff6638cb09de(p0)
```
```c
void 0x2818FF6638CB09DE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x282b6739644f4347

`0x282B6739644F4347` · hash `0x282B6739644F4347` · **Cliente**

```lua
N_0x282b6739644f4347(p0)
```
```c
void 0x282B6739644F4347(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x28ecb8ac2f607db2

`0x28ECB8AC2F607DB2` · hash `0x28ECB8AC2F607DB2` · **Cliente**

```lua
N_0x28ecb8ac2f607db2(p0, p1, p2, p3, p4)
```
```c
void 0x28ECB8AC2F607DB2(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### N_0x2cd90358f67d0aa8

`0x2CD90358F67D0AA8` · hash `0x2CD90358F67D0AA8` · **Cliente**

```lua
N_0x2cd90358f67d0aa8(p0)
```
```c
void 0x2CD90358F67D0AA8(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x2d7a9b577e72385e

`0x2D7A9B577E72385E` · hash `0x2D7A9B577E72385E` · **Cliente**

```lua
N_0x2d7a9b577e72385e(p0)
```
```c
void 0x2D7A9B577E72385E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x2e0259babc27a327

`0x2E0259BABC27A327` · hash `0x2E0259BABC27A327` · **Cliente**

```lua
N_0x2e0259babc27a327(p0)
```
```c
void 0x2E0259BABC27A327(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x2fa3173480008493

`0x2FA3173480008493` · hash `0x2FA3173480008493` · **Cliente**

```lua
N_0x2fa3173480008493(p0, p1, p2, p3, p4)
```
```c
void 0x2FA3173480008493(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x316db59cd14c1774

`0x316DB59CD14C1774` · hash `0x316DB59CD14C1774` · **Cliente**

```lua
N_0x316db59cd14c1774(p0)
```
```c
void 0x316DB59CD14C1774(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x32cac93c9de73d32

`0x32CAC93C9DE73D32` · hash `0x32CAC93C9DE73D32` · **Cliente**

```lua
local retval = N_0x32cac93c9de73d32()
```
```c
Any 0x32CAC93C9DE73D32();
```

**Devuelve:** `Any`

---
### N_0x33d72899e24c3365

`0x33D72899E24C3365` · hash `0x33D72899E24C3365` · **Cliente**

```lua
local retval = N_0x33d72899e24c3365(p0, p1)
```
```c
Any 0x33D72899E24C3365(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0x34770b9ce0e03b91

`0x34770B9CE0E03B91` · hash `0x34770B9CE0E03B91` · jhash `0x766A74FE` · **Cliente**

```lua
local retval, p1 = N_0x34770b9ce0e03b91(p0, p1)
```
```c
BOOL 0x34770B9CE0E03B91(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x38491439b6ba7f7d

`0x38491439B6BA7F7D` · hash `0x38491439B6BA7F7D` · jhash `0x509A286F` · **Cliente**

```lua
local retval = N_0x38491439b6ba7f7d(p0, p1)
```
```c
float 0x38491439B6BA7F7D(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `float`

---
### N_0x38baaa5dd4c9d19f

`0x38BAAA5DD4C9D19F` · hash `0x38BAAA5DD4C9D19F` · jhash `0x726FAE66` · **Cliente**

```lua
N_0x38baaa5dd4c9d19f(value)
```
```c
void 0x38BAAA5DD4C9D19F(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets profile setting 934  
```

---
### N_0x3de3aa516fb126a4

`0x3DE3AA516FB126A4` · hash `0x3DE3AA516FB126A4` · **Cliente**

```lua
N_0x3de3aa516fb126a4(p0)
```
```c
void 0x3DE3AA516FB126A4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x3ebeac6c3f81f6bd

`0x3EBEAC6C3F81F6BD` · hash `0x3EBEAC6C3F81F6BD` · **Cliente**

```lua
N_0x3ebeac6c3f81f6bd(p0)
```
```c
void 0x3EBEAC6C3F81F6BD(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x419615486bbf1956

`0x419615486BBF1956` · hash `0x419615486BBF1956` · **Cliente**

```lua
N_0x419615486bbf1956(p0)
```
```c
void 0x419615486BBF1956(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x44919cc079bb60bf

`0x44919CC079BB60BF` · hash `0x44919CC079BB60BF` · **Cliente**

```lua
N_0x44919cc079bb60bf(p0)
```
```c
void 0x44919CC079BB60BF(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x4aff7e02e485e92b

`0x4AFF7E02E485E92B` · hash `0x4AFF7E02E485E92B` · **Cliente**

```lua
N_0x4aff7e02e485e92b()
```
```c
void 0x4AFF7E02E485E92B();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x4c89fe2bdeb3f169

`0x4C89FE2BDEB3F169` · hash `0x4C89FE2BDEB3F169` · **Cliente**

```lua
local retval = N_0x4c89fe2bdeb3f169()
```
```c
Any 0x4C89FE2BDEB3F169();
```

**Devuelve:** `Any`

---
### N_0x4dc416f246a41fc8

`0x4DC416F246A41FC8` · hash `0x4DC416F246A41FC8` · **Cliente**

```lua
N_0x4dc416f246a41fc8(p0, p1, p2, p3, p4)
```
```c
void 0x4DC416F246A41FC8(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x4fcdbd3f0a813c25

`0x4FCDBD3F0A813C25` · hash `0x4FCDBD3F0A813C25` · **Cliente**

```lua
N_0x4fcdbd3f0a813c25(p0, p1)
```
```c
void 0x4FCDBD3F0A813C25(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x53c31853ec9531ff

`0x53C31853EC9531FF` · hash `0x53C31853EC9531FF` · **Cliente**

```lua
N_0x53c31853ec9531ff(p0)
```
```c
void 0x53C31853EC9531FF(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x53cae13e9b426993

`0x53CAE13E9B426993` · hash `0x53CAE13E9B426993` · **Cliente**

```lua
N_0x53cae13e9b426993(p0)
```
```c
void 0x53CAE13E9B426993(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x55384438fc55ad8e

`0x55384438FC55AD8E` · hash `0x55384438FC55AD8E` · jhash `0xF03895A4` · **Cliente**

```lua
N_0x55384438fc55ad8e(value)
```
```c
void 0x55384438FC55AD8E(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets profile setting 935  
```

---
### N_0x55a8becaf28a4eb7

`0x55A8BECAF28A4EB7` · hash `0x55A8BECAF28A4EB7` · **Cliente**

```lua
local retval = N_0x55a8becaf28a4eb7()
```
```c
Any 0x55A8BECAF28A4EB7();
```

**Devuelve:** `Any`

---
### N_0x5688585e6d563cd8

`0x5688585E6D563CD8` · hash `0x5688585E6D563CD8` · jhash `0xC62406A6` · **Cliente**

```lua
N_0x5688585e6d563cd8(p0)
```
```c
void 0x5688585E6D563CD8(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
STAT_SET_*
```

---
### N_0x5a556b229a169402

`0x5A556B229A169402` · hash `0x5A556B229A169402` · jhash `0x46F21343` · **Cliente**

```lua
local retval = N_0x5a556b229a169402()
```
```c
BOOL 0x5A556B229A169402();
```

**Devuelve:** `BOOL`

---
### N_0x5bd5f255321c4aaf

`0x5BD5F255321C4AAF` · hash `0x5BD5F255321C4AAF` · **Cliente**

```lua
local retval = N_0x5bd5f255321c4aaf(p0)
```
```c
Any 0x5BD5F255321C4AAF(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x5bf29846c6527c54

`0x5BF29846C6527C54` · hash `0x5BF29846C6527C54` · **Cliente**

```lua
N_0x5bf29846c6527c54(p0, p1, p2, p3, p4)
```
```c
void 0x5BF29846C6527C54(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x5cdaed54b34b0ed0

`0x5CDAED54B34B0ED0` · hash `0x5CDAED54B34B0ED0` · **Cliente**

```lua
N_0x5cdaed54b34b0ed0(p0)
```
```c
void 0x5CDAED54B34B0ED0(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x5ead2bf6484852e4

`0x5EAD2BF6484852E4` · hash `0x5EAD2BF6484852E4` · jhash `0x23D70C39` · **Cliente**

```lua
local retval = N_0x5ead2bf6484852e4()
```
```c
BOOL 0x5EAD2BF6484852E4();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
example from completionpercentage_controller.ysc.c4
if (STATS::_5EAD2BF6484852E4()) {
            MISC::SET_BIT(g_17b95._f20df._ff10, 15);
            STATS::_11FF1C80276097ED(0xe9ec4dd1, 200, 0);
        }
```

---
### N_0x5ff2c33b13a02a11

`0x5FF2C33B13A02A11` · hash `0x5FF2C33B13A02A11` · **Cliente**

```lua
N_0x5ff2c33b13a02a11(p0)
```
```c
void 0x5FF2C33B13A02A11(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x60eedc12af66e846

`0x60EEDC12AF66E846` · hash `0x60EEDC12AF66E846` · **Cliente**

```lua
N_0x60eedc12af66e846(p0)
```
```c
void 0x60EEDC12AF66E846(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x629526aba383bcaa

`0x629526ABA383BCAA` · hash `0x629526ABA383BCAA` · **Cliente**

```lua
N_0x629526aba383bcaa()
```
```c
void 0x629526ABA383BCAA();
```

**Devuelve:** `void`

---
### N_0x6483c25849031c4f

`0x6483C25849031C4F` · hash `0x6483C25849031C4F` · jhash `0x2FFD2FA5` · **Cliente**

```lua
local p3 = N_0x6483c25849031c4f(p0, p1, p2, p3)
```
```c
void 0x6483C25849031C4F(Any p0, Any p1, Any p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### N_0x6551b1f7f6cd46ea

`0x6551B1F7F6CD46EA` · hash `0x6551B1F7F6CD46EA` · **Cliente**

```lua
N_0x6551b1f7f6cd46ea(p0)
```
```c
void 0x6551B1F7F6CD46EA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x678f86d8fc040bdb

`0x678F86D8FC040BDB` · hash `0x678F86D8FC040BDB` · **Cliente**

```lua
N_0x678f86d8fc040bdb(p0)
```
```c
void 0x678F86D8FC040BDB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x6a60e43998228229

`0x6A60E43998228229` · hash `0x6A60E43998228229` · **Cliente**

```lua
N_0x6a60e43998228229(p0)
```
```c
void 0x6A60E43998228229(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x6a7f19756f1a9016

`0x6A7F19756F1A9016` · hash `0x6A7F19756F1A9016` · **Cliente**

```lua
local retval = N_0x6a7f19756f1a9016()
```
```c
BOOL 0x6A7F19756F1A9016();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0x6bc0acd0673acebe

`0x6BC0ACD0673ACEBE` · hash `0x6BC0ACD0673ACEBE` · **Cliente**

```lua
local valueA, valueB = N_0x6bc0acd0673acebe(p0)
```
```c
void 0x6BC0ACD0673ACEBE(Any p0, int* valueA, int* valueB);
```

**Parámetros**

- `p0` (`Any`)
- `valueA` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `valueB` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### N_0x6bccf9948492fd85

`0x6BCCF9948492FD85` · hash `0x6BCCF9948492FD85` · **Cliente**

```lua
N_0x6bccf9948492fd85(p0, p1, p2, p3, p4)
```
```c
void 0x6BCCF9948492FD85(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### N_0x6dee77aff8c21bd1

`0x6DEE77AFF8C21BD1` · hash `0x6DEE77AFF8C21BD1` · jhash `0x489E27E7` · **Cliente**

```lua
local retval, playerAccountId, posixTime = N_0x6dee77aff8c21bd1()
```
```c
BOOL 0x6DEE77AFF8C21BD1(int* playerAccountId, int* posixTime);
```

**Parámetros**

- `playerAccountId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posixTime` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0x6e0a5253375c4584

`0x6E0A5253375C4584` · hash `0x6E0A5253375C4584` · **Cliente**

```lua
local retval = N_0x6e0a5253375c4584()
```
```c
Any 0x6E0A5253375C4584();
```

**Devuelve:** `Any`

---
### N_0x6f361b8889a792a3

`0x6F361B8889A792A3` · hash `0x6F361B8889A792A3` · jhash `0x3B4EF322` · **Cliente**

```lua
N_0x6f361b8889a792a3()
```
```c
void 0x6F361B8889A792A3();
```

**Devuelve:** `void`

---
### N_0x7033eefd9b28088e

`0x7033EEFD9B28088E` · hash `0x7033EEFD9B28088E` · **Cliente**

```lua
N_0x7033eefd9b28088e(p0)
```
```c
void 0x7033EEFD9B28088E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x71b008056e5692d6

`0x71B008056E5692D6` · hash `0x71B008056E5692D6` · jhash `0xF2DB6A82` · **Cliente**

```lua
N_0x71b008056e5692d6()
```
```c
void 0x71B008056E5692D6();
```

**Devuelve:** `void`

---
### N_0x723c1ce13fbfdb67

`0x723C1CE13FBFDB67` · hash `0x723C1CE13FBFDB67` · jhash `0x4C39CF10` · **Cliente**

```lua
N_0x723c1ce13fbfdb67(p0, p1)
```
```c
void 0x723C1CE13FBFDB67(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x73001e34f85137f8

`0x73001E34F85137F8` · hash `0x73001E34F85137F8` · **Cliente**

```lua
N_0x73001e34f85137f8(p0)
```
```c
void 0x73001E34F85137F8(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x79d310a861697cc9

`0x79D310A861697CC9` · hash `0x79D310A861697CC9` · **Cliente**

```lua
N_0x79d310a861697cc9(profileSetting, settingValue)
```
```c
void 0x79D310A861697CC9(int profileSetting, int settingValue);
```

**Parámetros**

- `profileSetting` (`int`)
- `settingValue` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets profile setting 940 and 941

_SET_F* - _SET_G*
```

```
NativeDB Introduced: v2699
```

---
### N_0x7b18da61f6bae9d5

`0x7B18DA61F6BAE9D5` · hash `0x7B18DA61F6BAE9D5` · **Cliente**

```lua
N_0x7b18da61f6bae9d5(p0)
```
```c
void 0x7B18DA61F6BAE9D5(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x7d36291161859389

`0x7D36291161859389` · hash `0x7D36291161859389` · **Cliente**

```lua
N_0x7d36291161859389(p0)
```
```c
void 0x7D36291161859389(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x7d8ba05688ad64c7

`0x7D8BA05688AD64C7` · hash `0x7D8BA05688AD64C7` · **Cliente**

```lua
N_0x7d8ba05688ad64c7(p0)
```
```c
void 0x7D8BA05688AD64C7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x7e6946f68a38b74f

`0x7E6946F68A38B74F` · hash `0x7E6946F68A38B74F` · jhash `0x22804C20` · **Cliente**

```lua
local retval = N_0x7e6946f68a38b74f(p0)
```
```c
BOOL 0x7E6946F68A38B74F(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x7eec2a316c250073

`0x7EEC2A316C250073` · hash `0x7EEC2A316C250073` · jhash `0x30558CFD` · **Cliente**

```lua
N_0x7eec2a316c250073(p0, p1, p2)
```
```c
void 0x7EEC2A316C250073(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
_PLAYSTATS_ROB_ARMOURD_TRUCK  
```

---
### N_0x7f2c4cdf2e82df4c

`0x7F2C4CDF2E82DF4C` · hash `0x7F2C4CDF2E82DF4C` · jhash `0x0BF0F4B2` · **Cliente**

```lua
local retval = N_0x7f2c4cdf2e82df4c(p0)
```
```c
BOOL 0x7F2C4CDF2E82DF4C(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x810b5fcc52ec7ff0

`0x810B5FCC52EC7FF0` · hash `0x810B5FCC52EC7FF0` · **Cliente**

```lua
N_0x810b5fcc52ec7ff0(p0, p1, p2, p3)
```
```c
void 0x810B5FCC52EC7FF0(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x830c3a44eb3f2cf9

`0x830C3A44EB3F2CF9` · hash `0x830C3A44EB3F2CF9` · **Cliente**

```lua
N_0x830c3a44eb3f2cf9(p0)
```
```c
void 0x830C3A44EB3F2CF9(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x84a810b375e69c0e

`0x84A810B375E69C0E` · hash `0x84A810B375E69C0E` · **Cliente**

```lua
local retval = N_0x84a810b375e69c0e()
```
```c
Any 0x84A810B375E69C0E();
```

**Devuelve:** `Any`

---
### N_0x84dfc579c2fc214c

`0x84DFC579C2FC214C` · hash `0x84DFC579C2FC214C` · **Cliente**

```lua
N_0x84dfc579c2fc214c(p0)
```
```c
void 0x84DFC579C2FC214C(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x88087ee1f28024ae

`0x88087EE1F28024AE` · hash `0x88087EE1F28024AE` · **Cliente**

```lua
N_0x88087ee1f28024ae(p0)
```
```c
void 0x88087EE1F28024AE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x88578f6ec36b4a3a

`0x88578F6EC36B4A3A` · hash `0x88578F6EC36B4A3A` · jhash `0x6B90E730` · **Cliente**

```lua
local retval = N_0x88578f6ec36b4a3a(p0, p1)
```
```c
Any 0x88578F6EC36B4A3A(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0x8989cbd7b4e82534

`0x8989CBD7B4E82534` · hash `0x8989CBD7B4E82534` · **Cliente**

```lua
N_0x8989cbd7b4e82534(p0, p1, p2, p3, p4, p5, p6)
```
```c
void 0x8989CBD7B4E82534(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### N_0x8b9cdbd6c566c38c

`0x8B9CDBD6C566C38C` · hash `0x8B9CDBD6C566C38C` · **Cliente**

```lua
local retval = N_0x8b9cdbd6c566c38c()
```
```c
Any 0x8B9CDBD6C566C38C();
```

**Devuelve:** `Any`

---
### N_0x8c9d11605e59d955

`0x8C9D11605E59D955` · hash `0x8C9D11605E59D955` · **Cliente**

```lua
N_0x8c9d11605e59d955(p0)
```
```c
void 0x8C9D11605E59D955(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x8d8adb562f09a245

`0x8D8ADB562F09A245` · hash `0x8D8ADB562F09A245` · **Cliente**

```lua
N_0x8d8adb562f09a245(p0)
```
```c
void 0x8D8ADB562F09A245(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x8ec74ceb042e7cff

`0x8EC74CEB042E7CFF` · hash `0x8EC74CEB042E7CFF` · jhash `0x88AE9667` · **Cliente**

```lua
N_0x8ec74ceb042e7cff(p0)
```
```c
void 0x8EC74CEB042E7CFF(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x92fc0eedfac04a14

`0x92FC0EEDFAC04A14` · hash `0x92FC0EEDFAC04A14` · **Cliente**

```lua
N_0x92fc0eedfac04a14(p0, p1, p2, p3, p4, p5)
```
```c
void 0x92FC0EEDFAC04A14(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x930f504203f561c9

`0x930F504203F561C9` · hash `0x930F504203F561C9` · **Cliente**

```lua
N_0x930f504203f561c9(p0)
```
```c
void 0x930F504203F561C9(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x96e6d5150dbf1c09

`0x96E6D5150DBF1C09` · hash `0x96E6D5150DBF1C09` · **Cliente**

```lua
N_0x96e6d5150dbf1c09(p0, p1, p2)
```
```c
void 0x96E6D5150DBF1C09(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0x98e2bc1ca26287c3

`0x98E2BC1CA26287C3` · hash `0x98E2BC1CA26287C3` · **Cliente**

```lua
N_0x98e2bc1ca26287c3()
```
```c
void 0x98E2BC1CA26287C3();
```

**Devuelve:** `void`

---
### N_0x9a62ec95ae10e011

`0x9A62EC95AE10E011` · hash `0x9A62EC95AE10E011` · **Cliente**

```lua
local retval = N_0x9a62ec95ae10e011()
```
```c
int 0x9A62EC95AE10E011();
```

**Devuelve:** `int`

---
### N_0x9b4bd21d69b1e609

`0x9B4BD21D69B1E609` · hash `0x9B4BD21D69B1E609` · **Cliente**

```lua
N_0x9b4bd21d69b1e609()
```
```c
void 0x9B4BD21D69B1E609();
```

**Devuelve:** `void`

---
### N_0x9ec8858184cd253a

`0x9EC8858184CD253A` · hash `0x9EC8858184CD253A` · **Cliente**

```lua
local retval = N_0x9ec8858184cd253a()
```
```c
Any 0x9EC8858184CD253A();
```

**Devuelve:** `Any`

---
### N_0xa0f93d5465b3094d

`0xA0F93D5465B3094D` · hash `0xA0F93D5465B3094D` · jhash `0xC977D6E2` · **Cliente**

```lua
local retval, p0 = N_0xa0f93d5465b3094d(p0)
```
```c
BOOL 0xA0F93D5465B3094D(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0xa3c53804bdb68ed2

`0xA3C53804BDB68ED2` · hash `0xA3C53804BDB68ED2` · **Cliente**

```lua
N_0xa3c53804bdb68ed2(p0, p1)
```
```c
void 0xA3C53804BDB68ED2(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xa6f54bb2ffca35ea

`0xA6F54BB2FFCA35EA` · hash `0xA6F54BB2FFCA35EA` · **Cliente**

```lua
N_0xa6f54bb2ffca35ea(p0)
```
```c
void 0xA6F54BB2FFCA35EA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xa736cf7fb7c5bff4

`0xA736CF7FB7C5BFF4` · hash `0xA736CF7FB7C5BFF4` · jhash `0x31002201` · **Cliente**

```lua
local p0, p1, p2, p3 = N_0xa736cf7fb7c5bff4()
```
```c
void 0xA736CF7FB7C5BFF4(Any* p0, Any* p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### N_0xa761d4ac6115623d

`0xA761D4AC6115623D` · hash `0xA761D4AC6115623D` · **Cliente**

```lua
local retval = N_0xa761d4ac6115623d()
```
```c
Any 0xA761D4AC6115623D();
```

**Devuelve:** `Any`

---
### N_0xa78b8fa58200da56

`0xA78B8FA58200DA56` · hash `0xA78B8FA58200DA56` · jhash `0xE3247582` · **Cliente**

```lua
N_0xa78b8fa58200da56(p0)
```
```c
void 0xA78B8FA58200DA56(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
STATS::0xE3247582(0);  
STATS::0xE3247582(1);  
STATS::0xE3247582(2);  
STATS::0xE3247582(3);  
STATS::0xE3247582(4);  
STATS::0xE3247582(5);  
STATS::0xE3247582(6);  
```

---
### N_0xa8733668d1047b51

`0xA8733668D1047B51` · hash `0xA8733668D1047B51` · jhash `0x395D18B1` · **Cliente**

```lua
N_0xa8733668d1047b51(p0)
```
```c
void 0xA8733668D1047B51(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xa943fd1722e11efd

`0xA943FD1722E11EFD` · hash `0xA943FD1722E11EFD` · **Cliente**

```lua
local retval = N_0xa943fd1722e11efd()
```
```c
Any 0xA943FD1722E11EFD();
```

**Devuelve:** `Any`

---
### N_0xaa525dff66bb82f5

`0xAA525DFF66BB82F5` · hash `0xAA525DFF66BB82F5` · **Cliente**

```lua
N_0xaa525dff66bb82f5(p0, p1, p2)
```
```c
void 0xAA525DFF66BB82F5(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0xaff47709f1d5dcce

`0xAFF47709F1D5DCCE` · hash `0xAFF47709F1D5DCCE` · **Cliente**

```lua
local retval = N_0xaff47709f1d5dcce()
```
```c
Any 0xAFF47709F1D5DCCE();
```

**Devuelve:** `Any`

---
### N_0xb1d2bb1e1631f5b1

`0xB1D2BB1E1631F5B1` · hash `0xB1D2BB1E1631F5B1` · jhash `0x02F283CE` · **Cliente**

```lua
local retval = N_0xb1d2bb1e1631f5b1()
```
```c
BOOL 0xB1D2BB1E1631F5B1();
```

**Devuelve:** `BOOL`

---
### N_0xb26f670685631727

`0xB26F670685631727` · hash `0xB26F670685631727` · **Cliente**

```lua
N_0xb26f670685631727(p0)
```
```c
void 0xB26F670685631727(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
NativeDB Introduced: v1493
```

---
### N_0xb3da2606774a8e2d

`0xB3DA2606774A8E2D` · hash `0xB3DA2606774A8E2D` · **Cliente**

```lua
local retval = N_0xb3da2606774a8e2d()
```
```c
BOOL 0xB3DA2606774A8E2D();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 1.
NETWORK_IS_*
```

---
### N_0xba9749cc94c1fd85

`0xBA9749CC94C1FD85` · hash `0xBA9749CC94C1FD85` · **Cliente**

```lua
local retval = N_0xba9749cc94c1fd85()
```
```c
Any 0xBA9749CC94C1FD85();
```

**Devuelve:** `Any`

---
### N_0xbaa2f0490e146be8

`0xBAA2F0490E146BE8` · hash `0xBAA2F0490E146BE8` · **Cliente**

```lua
N_0xbaa2f0490e146be8(p0)
```
```c
void 0xBAA2F0490E146BE8(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xbe3db208333d9844

`0xBE3DB208333D9844` · hash `0xBE3DB208333D9844` · **Cliente**

```lua
local retval = N_0xbe3db208333d9844()
```
```c
Any 0xBE3DB208333D9844();
```

**Devuelve:** `Any`

---
### N_0xbed9f5693f34ed17

`0xBED9F5693F34ED17` · hash `0xBED9F5693F34ED17` · jhash `0xC4110917` · **Cliente**

```lua
local retval, outValue = N_0xbed9f5693f34ed17(statName, p1, outValue)
```
```c
BOOL 0xBED9F5693F34ED17(Hash statName, int p1, float* outValue);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)
- `outValue` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0xbf371cd2b64212fd

`0xBF371CD2B64212FD` · hash `0xBF371CD2B64212FD` · **Cliente**

```lua
N_0xbf371cd2b64212fd(p0)
```
```c
void 0xBF371CD2B64212FD(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xbfafdb5faaa5c5ab

`0xBFAFDB5FAAA5C5AB` · hash `0xBFAFDB5FAAA5C5AB` · **Cliente**

```lua
N_0xbfafdb5faaa5c5ab(p0)
```
```c
void 0xBFAFDB5FAAA5C5AB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xc01d2470f22cde5a

`0xC01D2470F22CDE5A` · hash `0xC01D2470F22CDE5A` · **Cliente**

```lua
N_0xc01d2470f22cde5a()
```
```c
void 0xC01D2470F22CDE5A();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

```
NativeDB Introduced: v2372
```

---
### N_0xc03fab2c2f92289b

`0xC03FAB2C2F92289B` · hash `0xC03FAB2C2F92289B` · **Cliente**

```lua
N_0xc03fab2c2f92289b(p0)
```
```c
void 0xC03FAB2C2F92289B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0xc0e0d686ddfc6eae

`0xC0E0D686DDFC6EAE` · hash `0xC0E0D686DDFC6EAE` · jhash `0x099FCC86` · **Cliente**

```lua
local retval = N_0xc0e0d686ddfc6eae()
```
```c
Any 0xC0E0D686DDFC6EAE();
```

**Devuelve:** `Any`

---
### N_0xc141b8917e0017ec

`0xC141B8917E0017EC` · hash `0xC141B8917E0017EC` · jhash `0x0AD43306` · **Cliente**

```lua
N_0xc141b8917e0017ec()
```
```c
void 0xC141B8917E0017EC();
```

**Devuelve:** `void`

---
### N_0xc14bd9f5337219b2

`0xC14BD9F5337219B2` · hash `0xC14BD9F5337219B2` · **Cliente**

```lua
N_0xc14bd9f5337219b2(p0)
```
```c
void 0xC14BD9F5337219B2(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
NativeDB Introduced: v1493
```

---
### N_0xc1e963c58664b556

`0xC1E963C58664B556` · hash `0xC1E963C58664B556` · **Cliente**

```lua
N_0xc1e963c58664b556(p0)
```
```c
void 0xC1E963C58664B556(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xc67e2da1cbe759e2

`0xC67E2DA1CBE759E2` · hash `0xC67E2DA1CBE759E2` · **Cliente**

```lua
N_0xc67e2da1cbe759e2()
```
```c
void 0xC67E2DA1CBE759E2();
```

**Devuelve:** `void`

**Descripción oficial:**

Sets profile setting 939

```
NativeDB Introduced: v1734
```

---
### N_0xc6e0e2616a7576bb

`0xC6E0E2616A7576BB` · hash `0xC6E0E2616A7576BB` · **Cliente**

```lua
local retval = N_0xc6e0e2616a7576bb()
```
```c
Any 0xC6E0E2616A7576BB();
```

**Devuelve:** `Any`

---
### N_0xc847b43f369ac0b5

`0xC847B43F369AC0B5` · hash `0xC847B43F369AC0B5` · **Cliente**

```lua
N_0xc847b43f369ac0b5()
```
```c
void 0xC847B43F369AC0B5();
```

**Devuelve:** `void`

---
### N_0xcc25a4553dfbf9ea

`0xCC25A4553DFBF9EA` · hash `0xCC25A4553DFBF9EA` · **Cliente**

```lua
N_0xcc25a4553dfbf9ea(p0, p1, p2, p3, p4)
```
```c
void 0xCC25A4553DFBF9EA(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### N_0xd1a1ee3b4fa8e760

`0xD1A1EE3B4FA8E760` · hash `0xD1A1EE3B4FA8E760` · **Cliente**

```lua
N_0xd1a1ee3b4fa8e760(p0)
```
```c
void 0xD1A1EE3B4FA8E760(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xd1c9b92bdd3f151d

`0xD1C9B92BDD3F151D` · hash `0xD1C9B92BDD3F151D` · **Cliente**

```lua
N_0xd1c9b92bdd3f151d(p0, p1, p2)
```
```c
void 0xD1C9B92BDD3F151D(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0xd4367d310f079db0

`0xD4367D310F079DB0` · hash `0xD4367D310F079DB0` · **Cliente**

```lua
N_0xd4367d310f079db0(p0, p1, p2, p3)
```
```c
void 0xD4367D310F079DB0(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xd558bec0bba7e8d2

`0xD558BEC0BBA7E8D2` · hash `0xD558BEC0BBA7E8D2` · **Cliente**

```lua
N_0xd558bec0bba7e8d2(p0, p1, p2, p3, p4)
```
```c
void 0xD558BEC0BBA7E8D2(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### N_0xd6ca58b3b53a0f22

`0xD6CA58B3B53A0F22` · hash `0xD6CA58B3B53A0F22` · **Cliente**

```lua
N_0xd6ca58b3b53a0f22(p0)
```
```c
void 0xD6CA58B3B53A0F22(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xdaf80797fc534bec

`0xDAF80797FC534BEC` · hash `0xDAF80797FC534BEC` · **Cliente**

```lua
N_0xdaf80797fc534bec(p0)
```
```c
void 0xDAF80797FC534BEC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xdeaaf77eb3687e97

`0xDEAAF77EB3687E97` · hash `0xDEAAF77EB3687E97` · **Cliente**

```lua
local retval, p1 = N_0xdeaaf77eb3687e97(p0, p1)
```
```c
Any 0xDEAAF77EB3687E97(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0xdfbd93bf2943e29b

`0xDFBD93BF2943E29B` · hash `0xDFBD93BF2943E29B` · **Cliente**

```lua
N_0xdfbd93bf2943e29b(p0)
```
```c
void 0xDFBD93BF2943E29B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0xdfcdb14317a9b361

`0xDFCDB14317A9B361` · hash `0xDFCDB14317A9B361` · **Cliente**

```lua
N_0xdfcdb14317a9b361(p0)
```
```c
void 0xDFCDB14317A9B361(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xe3261d791eb44acb

`0xE3261D791EB44ACB` · hash `0xE3261D791EB44ACB` · **Cliente**

```lua
N_0xe3261d791eb44acb(p0)
```
```c
void 0xE3261D791EB44ACB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xe496a53ba5f50a56

`0xE496A53BA5F50A56` · hash `0xE496A53BA5F50A56` · jhash `0xCE6B62B5` · **Cliente**

```lua
local retval = N_0xe496a53ba5f50a56(p0)
```
```c
Any 0xE496A53BA5F50A56(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0xe8853fbce7d8d0d6

`0xE8853FBCE7D8D0D6` · hash `0xE8853FBCE7D8D0D6` · **Cliente**

```lua
local retval = N_0xe8853fbce7d8d0d6()
```
```c
Any 0xE8853FBCE7D8D0D6();
```

**Devuelve:** `Any`

---
### N_0xecb41ac6ab754401

`0xECB41AC6AB754401` · hash `0xECB41AC6AB754401` · jhash `0xED7000C8` · **Cliente**

```lua
local retval = N_0xecb41ac6ab754401()
```
```c
BOOL 0xECB41AC6AB754401();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
STAT_LOAD_*
```

---
### N_0xedbf6c9b0d2c65c8

`0xEDBF6C9B0D2C65C8` · hash `0xEDBF6C9B0D2C65C8` · **Cliente**

```lua
N_0xedbf6c9b0d2c65c8(p0)
```
```c
void 0xEDBF6C9B0D2C65C8(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xf06a6f41cb445443

`0xF06A6F41CB445443` · hash `0xF06A6F41CB445443` · **Cliente**

```lua
N_0xf06a6f41cb445443(p0)
```
```c
void 0xF06A6F41CB445443(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xf11f01d98113536a

`0xF11F01D98113536A` · hash `0xF11F01D98113536A` · **Cliente**

```lua
local retval, p0 = N_0xf11f01d98113536a(p0)
```
```c
Any 0xF11F01D98113536A(float* p0);
```

**Parámetros**

- `p0` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0xf1a1803d3476f215

`0xF1A1803D3476F215` · hash `0xF1A1803D3476F215` · jhash `0xA3DAC790` · **Cliente**

```lua
N_0xf1a1803d3476f215(value)
```
```c
void 0xF1A1803D3476F215(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets profile setting 933  
```

---
### N_0xf534d94dfa2ead26

`0xF534D94DFA2EAD26` · hash `0xF534D94DFA2EAD26` · **Cliente**

```lua
N_0xf534d94dfa2ead26(p0, p1, p2, p3, p4)
```
```c
void 0xF534D94DFA2EAD26(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### N_0xf8c54a461c3e11dc

`0xF8C54A461C3E11DC` · hash `0xF8C54A461C3E11DC` · jhash `0x04181752` · **Cliente**

```lua
local p0, p1, p2, p3 = N_0xf8c54a461c3e11dc()
```
```c
void 0xF8C54A461C3E11DC(Any* p0, Any* p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### N_0xf9096193df1f99d4

`0xF9096193DF1F99D4` · hash `0xF9096193DF1F99D4` · **Cliente**

```lua
N_0xf9096193df1f99d4(p0)
```
```c
void 0xF9096193DF1F99D4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0xf9f2922717b819ec

`0xF9F2922717B819EC` · hash `0xF9F2922717B819EC` · **Cliente**

```lua
local retval = N_0xf9f2922717b819ec()
```
```c
Any 0xF9F2922717B819EC();
```

**Devuelve:** `Any`

---
### N_0xfcc228e07217fcac

`0xFCC228E07217FCAC` · hash `0xFCC228E07217FCAC` · **Cliente**

```lua
N_0xfcc228e07217fcac(p0)
```
```c
void 0xFCC228E07217FCAC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### OrderedBossVehicle

`_ORDERED_BOSS_VEHICLE` · hash `0xCEA553E35C2246E1` · **Cliente**

```lua
OrderedBossVehicle(p0, p1, vehicleHash)
```
```c
void _ORDERED_BOSS_VEHICLE(Any p0, Any p1, Hash vehicleHash);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `vehicleHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCEA553E35C2246E1` (`N_0xcea553e35c2246e1`)

---
### PlaystatsAcquiredHiddenPackage

`PLAYSTATS_ACQUIRED_HIDDEN_PACKAGE` · hash `0x79AB33F0FBFAC40C` · jhash `0x8D5C7B37` · **Cliente**

```lua
PlaystatsAcquiredHiddenPackage(p0)
```
```c
void PLAYSTATS_ACQUIRED_HIDDEN_PACKAGE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x79AB33F0FBFAC40C` (`N_0x79ab33f0fbfac40c`)

---
### PlaystatsActivityDone

`PLAYSTATS_ACTIVITY_DONE` · hash `0xA071E0ED98F91286` · jhash `0x1A66945F` · **Cliente**

```lua
PlaystatsActivityDone(p0, p1)
```
```c
void PLAYSTATS_ACTIVITY_DONE(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA071E0ED98F91286` (`N_0xa071e0ed98f91286`)

---
### PlaystatsArcadegame

`_PLAYSTATS_ARCADEGAME` · hash `0x533A7D1EA58DF958` · **Cliente**

```lua
PlaystatsArcadegame(p0, p1, p2, p3, p4, p5)
```
```c
void _PLAYSTATS_ARCADEGAME(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsArenaWarSpectator

`_PLAYSTATS_ARENA_WAR_SPECTATOR` · hash `0x6F4F599753F8200A` · **Cliente**

```lua
PlaystatsArenaWarSpectator(p0, p1, p2, p3, p4)
```
```c
void _PLAYSTATS_ARENA_WAR_SPECTATOR(int p0, int p1, int p2, int p3, int p4);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`int`)
- `p4` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### PlaystatsArenaWarsEnded

`_PLAYSTATS_ARENA_WARS_ENDED` · hash `0xB479D9F0D48A1BC5` · **Cliente**

```lua
local data = PlaystatsArenaWarsEnded(data)
```
```c
void _PLAYSTATS_ARENA_WARS_ENDED(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### PlaystatsAwardBadsport

`_PLAYSTATS_AWARD_BADSPORT` · hash `0x47B32F5611E6E483` · **Cliente**

```lua
PlaystatsAwardBadsport(id)
```
```c
void _PLAYSTATS_AWARD_BADSPORT(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x47B32F5611E6E483` (`N_0x47b32f5611e6e483`)

---
### PlaystatsAwardXp

`PLAYSTATS_AWARD_XP` · hash `0x46F917F6B4128FE4` · jhash `0x8770017B` · **Cliente**

```lua
PlaystatsAwardXp(amount, type, category)
```
```c
void PLAYSTATS_AWARD_XP(int amount, Hash type, Hash category);
```

**Parámetros**

- `amount` (`int`)
- `type` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `category` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### PlaystatsBackgroundScriptAction

`PLAYSTATS_BACKGROUND_SCRIPT_ACTION` · hash `0x5009DFD741329729` · jhash `0x61ECC465` · **Cliente**

```lua
PlaystatsBackgroundScriptAction(action, value)
```
```c
void PLAYSTATS_BACKGROUND_SCRIPT_ACTION(char* action, int value);
```

**Parámetros**

- `action` (`char*`)
- `value` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5009DFD741329729` (`N_0x5009dfd741329729`)

---
### PlaystatsBanAlert

`_PLAYSTATS_BAN_ALERT` · hash `0x516FC96EB88EEFE5` · **Cliente**

```lua
PlaystatsBanAlert(p0)
```
```c
void _PLAYSTATS_BAN_ALERT(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x516FC96EB88EEFE5` (`N_0x516fc96eb88eefe5`)

---
### PlaystatsBuyContraband

`_PLAYSTATS_BUY_CONTRABAND` · hash `0xD6781E42755531F7` · **Cliente**

```lua
local data = PlaystatsBuyContraband(data)
```
```c
void _PLAYSTATS_BUY_CONTRABAND(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD6781E42755531F7` (`N_0xd6781e42755531f7`)

---
### PlaystatsCarclubChallenge

`_PLAYSTATS_CARCLUB_CHALLENGE` · hash `0x1187CB58D7F3BED7` · **Cliente**

```lua
PlaystatsCarclubChallenge(p0, p1, p2, p3)
```
```c
void _PLAYSTATS_CARCLUB_CHALLENGE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x1187CB58D7F3BED7` (`N_0x1187cb58d7f3bed7`)

---
### PlaystatsCarclubPoints

`_PLAYSTATS_CARCLUB_POINTS` · hash `0xFF14D6FEEC507BBE` · **Cliente**

```lua
PlaystatsCarclubPoints(p0)
```
```c
void _PLAYSTATS_CARCLUB_POINTS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xFF14D6FEEC507BBE` (`N_0xff14d6feec507bbe`)

---
### PlaystatsCarclubPrize

`_PLAYSTATS_CARCLUB_PRIZE` · hash `0x69C922B677621428` · **Cliente**

```lua
PlaystatsCarclubPrize(p0, p1)
```
```c
void _PLAYSTATS_CARCLUB_PRIZE(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x69C922B677621428` (`N_0x69c922b677621428`)

---
### PlaystatsCasinoBlackjack

`_PLAYSTATS_CASINO_BLACKJACK` · hash `0x3EAE97309727E7AD` · **Cliente**

```lua
PlaystatsCasinoBlackjack(p0)
```
```c
void _PLAYSTATS_CASINO_BLACKJACK(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoBlackjackLight

`_PLAYSTATS_CASINO_BLACKJACK_LIGHT` · hash `0xD5451C7BF151EB6F` · **Cliente**

```lua
PlaystatsCasinoBlackjackLight(p0)
```
```c
void _PLAYSTATS_CASINO_BLACKJACK_LIGHT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoChip

`_PLAYSTATS_CASINO_CHIP` · hash `0x0999F3F090EC5012` · **Cliente**

```lua
PlaystatsCasinoChip(p0)
```
```c
void _PLAYSTATS_CASINO_CHIP(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoInsidetrack

`_PLAYSTATS_CASINO_INSIDETRACK` · hash `0x049F059625058A86` · **Cliente**

```lua
PlaystatsCasinoInsidetrack(p0)
```
```c
void _PLAYSTATS_CASINO_INSIDETRACK(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoInsidetrackLight

`_PLAYSTATS_CASINO_INSIDETRACK_LIGHT` · hash `0x23A3CBCD50D54E47` · **Cliente**

```lua
PlaystatsCasinoInsidetrackLight(p0)
```
```c
void _PLAYSTATS_CASINO_INSIDETRACK_LIGHT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoLuckyseven

`_PLAYSTATS_CASINO_LUCKYSEVEN` · hash `0x0C432C1435F5E4FA` · **Cliente**

```lua
PlaystatsCasinoLuckyseven(p0)
```
```c
void _PLAYSTATS_CASINO_LUCKYSEVEN(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoMissionEnded

`_PLAYSTATS_CASINO_MISSION_ENDED` · hash `0x1A0D4A6C336B7BC5` · **Cliente**

```lua
local data = PlaystatsCasinoMissionEnded(data)
```
```c
void _PLAYSTATS_CASINO_MISSION_ENDED(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoRoulette

`_PLAYSTATS_CASINO_ROULETTE` · hash `0x95101C443A84E7F1` · **Cliente**

```lua
PlaystatsCasinoRoulette(p0)
```
```c
void _PLAYSTATS_CASINO_ROULETTE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoRouletteLight

`_PLAYSTATS_CASINO_ROULETTE_LIGHT` · hash `0x6572ABA3DE1197FC` · **Cliente**

```lua
PlaystatsCasinoRouletteLight(p0)
```
```c
void _PLAYSTATS_CASINO_ROULETTE_LIGHT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoSlotmachine

`_PLAYSTATS_CASINO_SLOTMACHINE` · hash `0xEF5EC67D392B830A` · **Cliente**

```lua
PlaystatsCasinoSlotmachine(p0)
```
```c
void _PLAYSTATS_CASINO_SLOTMACHINE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoSlotmachineLight

`_PLAYSTATS_CASINO_SLOTMACHINE_LIGHT` · hash `0xE60054A0FAE8227F` · **Cliente**

```lua
PlaystatsCasinoSlotmachineLight(p0)
```
```c
void _PLAYSTATS_CASINO_SLOTMACHINE_LIGHT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoStoryMissionEnded

`_PLAYSTATS_CASINO_STORY_MISSION_ENDED` · hash `0xFCCCAC2BD3C1F180` · **Cliente**

```lua
PlaystatsCasinoStoryMissionEnded(p0, p1)
```
```c
void _PLAYSTATS_CASINO_STORY_MISSION_ENDED(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoThreecardpoker

`_PLAYSTATS_CASINO_THREECARDPOKER` · hash `0xF740FB339D471C35` · **Cliente**

```lua
PlaystatsCasinoThreecardpoker(p0)
```
```c
void _PLAYSTATS_CASINO_THREECARDPOKER(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCasinoThreecardpokerLight

`_PLAYSTATS_CASINO_THREECARDPOKER_LIGHT` · hash `0xC9001364B4388F22` · **Cliente**

```lua
PlaystatsCasinoThreecardpokerLight(p0)
```
```c
void _PLAYSTATS_CASINO_THREECARDPOKER_LIGHT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsChangeMcEmblem

`_PLAYSTATS_CHANGE_MC_EMBLEM` · hash `0x0A50D2604E05CB94` · **Cliente**

```lua
PlaystatsChangeMcEmblem(p0, p1, p2, p3, p4)
```
```c
void _PLAYSTATS_CHANGE_MC_EMBLEM(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0A50D2604E05CB94` (`N_0x0a50d2604e05cb94`)

---
### PlaystatsCheatApplied

`PLAYSTATS_CHEAT_APPLIED` · hash `0x6058665D72302D3F` · jhash `0x345166F3` · **Cliente**

```lua
PlaystatsCheatApplied(cheat)
```
```c
void PLAYSTATS_CHEAT_APPLIED(char* cheat);
```

**Parámetros**

- `cheat` (`char*`)

**Devuelve:** `void`

---
### PlaystatsClothChange

`PLAYSTATS_CLOTH_CHANGE` · hash `0x34B973047A2268B9` · jhash `0x3AFF9E58` · **Cliente**

```lua
PlaystatsClothChange(p0, p1, p2, p3, p4)
```
```c
void PLAYSTATS_CLOTH_CHANGE(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### PlaystatsCollectible

`_PLAYSTATS_COLLECTIBLE` · hash `0xCD0A8A9338681CF2` · **Cliente**

```lua
PlaystatsCollectible(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void _PLAYSTATS_COLLECTIBLE(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsCopyRankIntoNewSlot

`_PLAYSTATS_COPY_RANK_INTO_NEW_SLOT` · hash `0xB7257BA2550EA10A` · **Cliente**

```lua
PlaystatsCopyRankIntoNewSlot(p0, p1, p2, p3, p4, p5, p6)
```
```c
void _PLAYSTATS_COPY_RANK_INTO_NEW_SLOT(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB7257BA2550EA10A` (`N_0xb7257ba2550ea10a`)

---
### PlaystatsCrateCreated

`PLAYSTATS_CRATE_CREATED` · hash `0xAFC7E5E075A96F46` · jhash `0xD003E648` · **Cliente**

```lua
PlaystatsCrateCreated(p0, p1, p2)
```
```c
void PLAYSTATS_CRATE_CREATED(float p0, float p1, float p2);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAFC7E5E075A96F46` (`N_0xafc7e5e075a96f46`), `_PLAYSTATS_AMBIENT_MISSION_CRATE_CREATED` (`PlaystatsAmbientMissionCrateCreated`), `_PLAYSTATS_CRATE_CREATED` (`PlaystatsCrateCreated`), `_PLAYSTATS_CRATE_CREATED_MISSION_DONE` (`PlaystatsCrateCreatedMissionDone`)

---
### PlaystatsCrateDropMissionDone

`PLAYSTATS_CRATE_DROP_MISSION_DONE` · hash `0x1CAE5D2E3F9A07F0` · jhash `0x6602CED6` · **Cliente**

```lua
PlaystatsCrateDropMissionDone(p0, p1, p2, p3, p4, p5)
```
```c
void PLAYSTATS_CRATE_DROP_MISSION_DONE(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 7: Any p6
NativeDB Added Parameter 8: Any p7
```

**Nombres antiguos (alias):** `0x1CAE5D2E3F9A07F0` (`N_0x1cae5d2e3f9a07f0`), `_PLAYSTATS_CRATE_DROP` (`PlaystatsCrateDrop`)

---
### PlaystatsDarMissionEnd

`_PLAYSTATS_DAR_MISSION_END` · hash `0x0BC254FF3A911501` · **Cliente**

```lua
local data = PlaystatsDarMissionEnd(data)
```
```c
void _PLAYSTATS_DAR_MISSION_END(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### PlaystatsDefendContraband

`_PLAYSTATS_DEFEND_CONTRABAND` · hash `0x2605663BD4F23B5D` · **Cliente**

```lua
local data = PlaystatsDefendContraband(data)
```
```c
void _PLAYSTATS_DEFEND_CONTRABAND(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2605663BD4F23B5D` (`N_0x2605663bd4f23b5d`)

---
### PlaystatsDirectorMode

`_PLAYSTATS_DIRECTOR_MODE` · hash `0x46326E13DA4E0546` · **Cliente**

```lua
local p0 = PlaystatsDirectorMode(p0)
```
```c
void _PLAYSTATS_DIRECTOR_MODE(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x46326E13DA4E0546` (`N_0x46326e13da4e0546`)

---
### PlaystatsDroneUsage

`_PLAYSTATS_DRONE_USAGE` · hash `0x66C7BB2416ED3FCE` · **Cliente**

```lua
PlaystatsDroneUsage(p0, p1, p2)
```
```c
void _PLAYSTATS_DRONE_USAGE(int p0, int p1, int p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### PlaystatsDupeDetection

`_PLAYSTATS_DUPE_DETECTION` · hash `0x848B66100EE33B05` · **Cliente**

```lua
local data = PlaystatsDupeDetection(data)
```
```c
void _PLAYSTATS_DUPE_DETECTION(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x848B66100EE33B05` (`N_0x848b66100ee33b05`)

---
### PlaystatsEarnedMcPoints

`_PLAYSTATS_EARNED_MC_POINTS` · hash `0x501478855A6074CE` · **Cliente**

```lua
PlaystatsEarnedMcPoints(p0, p1, p2, p3, p4, p5)
```
```c
void _PLAYSTATS_EARNED_MC_POINTS(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x501478855A6074CE` (`N_0x501478855a6074ce`)

---
### PlaystatsEnterSessionPack

`_PLAYSTATS_ENTER_SESSION_PACK` · hash `0x878FF156D36E9956` · **Cliente**

```lua
local data = PlaystatsEnterSessionPack(data)
```
```c
void _PLAYSTATS_ENTER_SESSION_PACK(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### PlaystatsExtraEvent

`_PLAYSTATS_EXTRA_EVENT` · hash `0xFA5B74BAB8A7EF99` · **Cliente**

```lua
PlaystatsExtraEvent(p0)
```
```c
void _PLAYSTATS_EXTRA_EVENT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xFA5B74BAB8A7EF99` (`N_0xfa5b74bab8a7ef99`)

---
### PlaystatsFriendActivity

`PLAYSTATS_FRIEND_ACTIVITY` · hash `0x0F71DE29AB2258F1` · jhash `0xD1FA1BDB` · **Cliente**

```lua
PlaystatsFriendActivity(p0, p1)
```
```c
void PLAYSTATS_FRIEND_ACTIVITY(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### PlaystatsGunrunMissionEnded

`_PLAYSTATS_GUNRUN_MISSION_ENDED` · hash `0x0EACDF8487D5155A` · **Cliente**

```lua
local data = PlaystatsGunrunMissionEnded(data)
```
```c
void _PLAYSTATS_GUNRUN_MISSION_ENDED(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0EACDF8487D5155A` (`N_0x0eacdf8487d5155a`)

---
### PlaystatsH2FmprepEnd

`_PLAYSTATS_H2_FMPREP_END` · hash `0xD8AFB345A9C5CCBB` · **Cliente**

```lua
local data = PlaystatsH2FmprepEnd(data)
```
```c
void _PLAYSTATS_H2_FMPREP_END(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### PlaystatsH2InstanceEnd

`_PLAYSTATS_H2_INSTANCE_END` · hash `0x1E1497D0D2108115` · **Cliente**

```lua
local data = PlaystatsH2InstanceEnd(p1, p2, p3)
```
```c
void _PLAYSTATS_H2_INSTANCE_END(Any* data, Any p1, Any p2, Any p3);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### PlaystatsHeistSaveCheat

`PLAYSTATS_HEIST_SAVE_CHEAT` · hash `0xF4FF020A08BC8863` · jhash `0xB731DF54` · **Cliente**

```lua
PlaystatsHeistSaveCheat(hash, p1)
```
```c
void PLAYSTATS_HEIST_SAVE_CHEAT(Hash hash, int p1);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF4FF020A08BC8863` (`N_0xf4ff020a08bc8863`), `_PLAYSTATS_HEIST_SAVE_CHEAT` (`PlaystatsHeistSaveCheat`)

---
### PlaystatsHoldUpMissionDone

`PLAYSTATS_HOLD_UP_MISSION_DONE` · hash `0xCB00196B31C39EB1` · jhash `0x759E0EC9` · **Cliente**

```lua
PlaystatsHoldUpMissionDone(p0, p1, p2, p3)
```
```c
void PLAYSTATS_HOLD_UP_MISSION_DONE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCB00196B31C39EB1` (`N_0xcb00196b31c39eb1`), `_PLAYSTATS_HOLD_UP` (`PlaystatsHoldUp`)

---
### PlaystatsIdleKick

`PLAYSTATS_IDLE_KICK` · hash `0x5DA3A8DE8CB6226F` · jhash `0x9E2B9522` · **Cliente**

```lua
PlaystatsIdleKick(time)
```
```c
void PLAYSTATS_IDLE_KICK(int time);
```

**Parámetros**

- `time` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
longest time being ilde?  
```

**Nombres antiguos (alias):** `0x5DA3A8DE8CB6226F` (`N_0x5da3a8de8cb6226f`)

---
### PlaystatsImportExportMissionDone

`PLAYSTATS_IMPORT_EXPORT_MISSION_DONE` · hash `0x2B69F5074C894811` · jhash `0x62073DF7` · **Cliente**

```lua
PlaystatsImportExportMissionDone(p0, p1, p2, p3)
```
```c
void PLAYSTATS_IMPORT_EXPORT_MISSION_DONE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2B69F5074C894811` (`N_0x2b69f5074c894811`), `_PLAYSTATS_IMP_EXP` (`PlaystatsImpExp`)

---
### PlaystatsInventory

`_PLAYSTATS_INVENTORY` · hash `0x887DAD63CF5B7908` · **Cliente**

```lua
PlaystatsInventory(p0)
```
```c
void _PLAYSTATS_INVENTORY(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### PlaystatsJobBend

`PLAYSTATS_JOB_BEND` · hash `0xF5BB8DAC426A52C0` · jhash `0x40520E70` · **Cliente**

```lua
local p0, p1, p2, p3 = PlaystatsJobBend()
```
```c
void PLAYSTATS_JOB_BEND(Any* p0, Any* p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF5BB8DAC426A52C0` (`N_0xf5bb8dac426a52c0`)

---
### PlaystatsLeaveJobChain

`PLAYSTATS_LEAVE_JOB_CHAIN` · hash `0xC5BE134EC7BA96A0` · jhash `0xC960E161` · **Cliente**

```lua
PlaystatsLeaveJobChain(p0, p1, p2, p3, p4)
```
```c
void PLAYSTATS_LEAVE_JOB_CHAIN(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC5BE134EC7BA96A0` (`N_0xc5be134ec7ba96a0`)

---
### PlaystatsMatchStarted

`PLAYSTATS_MATCH_STARTED` · hash `0xBC80E22DED931E3D` · jhash `0x2BDE85C1` · **Cliente**

```lua
PlaystatsMatchStarted(p0, p1, p2, p3, p4, p5, p6)
```
```c
void PLAYSTATS_MATCH_STARTED(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Removed Parameter 4: Any p3
NativeDB Removed Parameter 5: Any p4
NativeDB Removed Parameter 6: Any p5
NativeDB Removed Parameter 7: Any p6
```

---
### PlaystatsMissionCheckpoint

`PLAYSTATS_MISSION_CHECKPOINT` · hash `0xC900596A63978C1D` · jhash `0xCDC52280` · **Cliente**

```lua
local p0 = PlaystatsMissionCheckpoint(p1, p2, p3)
```
```c
void PLAYSTATS_MISSION_CHECKPOINT(Any* p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### PlaystatsMissionOver

`PLAYSTATS_MISSION_OVER` · hash `0x7C4BB33A8CED7324` · jhash `0x5B90B5FF` · **Cliente**

```lua
local p0 = PlaystatsMissionOver(p1, p2, p3, p4, p5)
```
```c
void PLAYSTATS_MISSION_OVER(Any* p0, Any p1, Any p2, BOOL p3, BOOL p4, BOOL p5);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `void`

---
### PlaystatsMissionStarted

`PLAYSTATS_MISSION_STARTED` · hash `0xC19A2925C34D2231` · jhash `0x3AAB699C` · **Cliente**

```lua
local p0 = PlaystatsMissionStarted(p1, p2, p3)
```
```c
void PLAYSTATS_MISSION_STARTED(Any* p0, Any p1, Any p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### PlaystatsNpcInvite

`PLAYSTATS_NPC_INVITE` · hash `0x93054C88E6AA7C44` · jhash `0x598C06F3` · **Cliente**

```lua
local p0 = PlaystatsNpcInvite(p0)
```
```c
void PLAYSTATS_NPC_INVITE(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### PlaystatsOddjobDone

`PLAYSTATS_ODDJOB_DONE` · hash `0x69DEA3E9DB727B4C` · jhash `0xFE14A8EA` · **Cliente**

```lua
PlaystatsOddjobDone(p0, p1, p2)
```
```c
void PLAYSTATS_ODDJOB_DONE(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### PlaystatsPassiveMode

`_PLAYSTATS_PASSIVE_MODE` · hash `0x35EEC6C2BC821A71` · **Cliente**

```lua
PlaystatsPassiveMode(p0, p1, p2, p3)
```
```c
void _PLAYSTATS_PASSIVE_MODE(BOOL p0, int p1, int p2, int p3);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### PlaystatsPegasaircraft

`_PLAYSTATS_PEGASAIRCRAFT` · hash `0x9572BD4DD6B72122` · **Cliente**

```lua
PlaystatsPegasaircraft(modelHash)
```
```c
void _PLAYSTATS_PEGASAIRCRAFT(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### PlaystatsPiMenuHideSettings

`_PLAYSTATS_PI_MENU_HIDE_SETTINGS` · hash `0x203B381133817079` · **Cliente**

```lua
local data = PlaystatsPiMenuHideSettings(data)
```
```c
void _PLAYSTATS_PI_MENU_HIDE_SETTINGS(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x203B381133817079` (`N_0x203b381133817079`)

---
### PlaystatsPropChange

`PLAYSTATS_PROP_CHANGE` · hash `0xBA739D6D5A05D6E7` · jhash `0x25740A1D` · **Cliente**

```lua
PlaystatsPropChange(p0, p1, p2, p3)
```
```c
void PLAYSTATS_PROP_CHANGE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### PlaystatsQuickfixTool

`PLAYSTATS_QUICKFIX_TOOL` · hash `0x90D0622866E80445` · jhash `0x66FEB701` · **Cliente**

```lua
PlaystatsQuickfixTool(element, item)
```
```c
void PLAYSTATS_QUICKFIX_TOOL(int element, char* item);
```

**Parámetros**

- `element` (`int`)
- `item` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x90D0622866E80445` (`N_0x90d0622866e80445`)

---
### PlaystatsRaceCheckpoint

`PLAYSTATS_RACE_CHECKPOINT` · hash `0x9C375C315099DDE4` · jhash `0x580D5508` · **Cliente**

```lua
PlaystatsRaceCheckpoint(p0, p1, p2, p3, p4)
```
```c
void PLAYSTATS_RACE_CHECKPOINT(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### PlaystatsRaceToPointMissionDone

`PLAYSTATS_RACE_TO_POINT_MISSION_DONE` · hash `0xADDD1C754E2E2914` · jhash `0x06CE3692` · **Cliente**

```lua
PlaystatsRaceToPointMissionDone(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void PLAYSTATS_RACE_TO_POINT_MISSION_DONE(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Removed Parameter 5: Any p4
NativeDB Removed Parameter 6: Any p5
NativeDB Removed Parameter 7: Any p6
NativeDB Removed Parameter 8: Any p7
NativeDB Removed Parameter 9: Any p8
NativeDB Removed Parameter 10: Any p9
```

**Nombres antiguos (alias):** `0xADDD1C754E2E2914` (`N_0xaddd1c754e2e2914`), `_PLAYSTATS_RACE_TO_POINT` (`PlaystatsRaceToPoint`)

---
### PlaystatsRandomMissionDone

`PLAYSTATS_RANDOM_MISSION_DONE` · hash `0x71862B1D855F32E1` · jhash `0xAC2C7C63` · **Cliente**

```lua
PlaystatsRandomMissionDone(name, p1, p2, p3)
```
```c
void PLAYSTATS_RANDOM_MISSION_DONE(char* name, Any p1, Any p2, Any p3);
```

**Parámetros**

- `name` (`char*`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x71862B1D855F32E1` (`N_0x71862b1d855f32e1`)

---
### PlaystatsRankUp

`PLAYSTATS_RANK_UP` · hash `0xC7F2DE41D102BFB4` · jhash `0x56AFB9F5` · **Cliente**

```lua
PlaystatsRankUp(rank)
```
```c
void PLAYSTATS_RANK_UP(int rank);
```

**Parámetros**

- `rank` (`int`)

**Devuelve:** `void`

---
### PlaystatsRecoverContraband

`_PLAYSTATS_RECOVER_CONTRABAND` · hash `0x04D90BA8207ADA2D` · **Cliente**

```lua
local data = PlaystatsRecoverContraband(data)
```
```c
void _PLAYSTATS_RECOVER_CONTRABAND(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x04D90BA8207ADA2D` (`N_0x04d90ba8207ada2d`)

---
### PlaystatsRobberyFinale

`_PLAYSTATS_ROBBERY_FINALE` · hash `0xBBA55BE9AAAABF44` · **Cliente**

```lua
PlaystatsRobberyFinale(p0)
```
```c
void _PLAYSTATS_ROBBERY_FINALE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xBBA55BE9AAAABF44` (`N_0xbba55be9aaaabf44`)

---
### PlaystatsRobberyPrep

`_PLAYSTATS_ROBBERY_PREP` · hash `0x1A67DFBF1F5C3835` · **Cliente**

```lua
PlaystatsRobberyPrep(p0)
```
```c
void _PLAYSTATS_ROBBERY_PREP(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x1A67DFBF1F5C3835` (`N_0x1a67dfbf1f5c3835`)

---
### PlaystatsRosBet

`PLAYSTATS_ROS_BET` · hash `0x121FB4DDDC2D5291` · jhash `0x413539BC` · **Cliente**

```lua
PlaystatsRosBet(amount, act, player, cm)
```
```c
void PLAYSTATS_ROS_BET(int amount, int act, Player player, float cm);
```

**Parámetros**

- `amount` (`int`)
- `act` (`int`)
- `player` (`Player`)
- `cm` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x121FB4DDDC2D5291` (`N_0x121fb4dddc2d5291`)

---
### PlaystatsSellContraband

`_PLAYSTATS_SELL_CONTRABAND` · hash `0xC729991A9065376E` · **Cliente**

```lua
local data = PlaystatsSellContraband(data)
```
```c
void _PLAYSTATS_SELL_CONTRABAND(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC729991A9065376E` (`N_0xc729991a9065376e`)

---
### PlaystatsSetJoinType

`PLAYSTATS_SET_JOIN_TYPE` · hash `0xD1032E482629049E` · jhash `0x1AC97138` · **Cliente**

```lua
PlaystatsSetJoinType(joinType)
```
```c
void PLAYSTATS_SET_JOIN_TYPE(int joinType);
```

**Parámetros**

- `joinType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Sets a byte that is then used in session_host and session_join metrics when hosting or joining a session

**Nombres antiguos (alias):** `0xD1032E482629049E` (`N_0xd1032e482629049e`)

---
### PlaystatsShopItem

`PLAYSTATS_SHOP_ITEM` · hash `0x176852ACAAC173D1` · jhash `0xA4746384` · **Cliente**

```lua
PlaystatsShopItem(p0, p1, p2, p3, p4)
```
```c
void PLAYSTATS_SHOP_ITEM(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### PlaystatsSmugMissionEnded

`_PLAYSTATS_SMUG_MISSION_ENDED` · hash `0x320C35147D5B5DDD` · **Cliente**

```lua
local data = PlaystatsSmugMissionEnded(data)
```
```c
void _PLAYSTATS_SMUG_MISSION_ENDED(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### PlaystatsSpectatorWheelSpin

`_PLAYSTATS_SPECTATOR_WHEEL_SPIN` · hash `0x6731DE84A38BFAD0` · **Cliente**

```lua
PlaystatsSpectatorWheelSpin(p0, p1, p2, p3)
```
```c
void _PLAYSTATS_SPECTATOR_WHEEL_SPIN(int p0, int p1, int p2, int p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### PlaystatsSpentPiCustomLoadout

`_PLAYSTATS_SPENT_PI_CUSTOM_LOADOUT` · hash `0xBE509B0A3693DE8B` · **Cliente**

```lua
PlaystatsSpentPiCustomLoadout(amount)
```
```c
void _PLAYSTATS_SPENT_PI_CUSTOM_LOADOUT(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBE509B0A3693DE8B` (`N_0xbe509b0a3693de8b`)

---
### PlaystatsStartOfflineMode

`_PLAYSTATS_START_OFFLINE_MODE` · hash `0x098760C7461724CD` · jhash `0x896CDF8D` · **Cliente**

```lua
PlaystatsStartOfflineMode()
```
```c
void _PLAYSTATS_START_OFFLINE_MODE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
PLAYSTATS_START_INVITE_DESPAWNING?
```

**Nombres antiguos (alias):** `0x098760C7461724CD` (`N_0x098760c7461724cd`)

---
### PlaystatsStartTrackingStunts

`PLAYSTATS_START_TRACKING_STUNTS` · hash `0x928DBFB892638EF3` · **Cliente**

```lua
PlaystatsStartTrackingStunts()
```
```c
void PLAYSTATS_START_TRACKING_STUNTS();
```

**Devuelve:** `void`

**Descripción oficial:**

Allows stunts to be triggered and sent as a `CEventNetworkStuntPerformed` event.

Event types are shown below:

```cpp
enum eTrackedStuntType
{
    ST_FRONTFLIP = 0,
    ST_BACKFLIP = 1,
    ST_SPIN = 2,
    ST_WHEELIE = 3,
    ST_STOPPIE = 4,
    ST_BOWLING_PIN = 5,
    ST_FOOTBALL = 6,
    ST_ROLL = 7
};
```

**Nombres antiguos (alias):** `0x928DBFB892638EF3` (`N_0x928dbfb892638ef3`), `_PLAYSTATS_STUNT_PERFORMED_EVENT_ALLOW_TRIGGER` (`PlaystatsStuntPerformedEventAllowTrigger`)

---
### PlaystatsStoneHatchetEnd

`_PLAYSTATS_STONE_HATCHET_END` · hash `0x35E39E5570358630` · **Cliente**

```lua
local data = PlaystatsStoneHatchetEnd(data)
```
```c
void _PLAYSTATS_STONE_HATCHET_END(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### PlaystatsStopTrackingStunts

`PLAYSTATS_STOP_TRACKING_STUNTS` · hash `0x8A800DACCC0DA55D` · **Cliente**

```lua
PlaystatsStopTrackingStunts()
```
```c
void PLAYSTATS_STOP_TRACKING_STUNTS();
```

**Devuelve:** `void`

**Descripción oficial:**

Disallows CEventNetworkStuntPerformed to be triggered (Resets [`PLAYSTATS_START_TRACKING_STUNTS`](#playstatsstarttrackingstunts)).

**Nombres antiguos (alias):** `0x8A800DACCC0DA55D` (`N_0x8a800daccc0da55d`), `_PLAYSTATS_STUNT_PERFORMED_EVENT_DISALLOW_TRIGGER` (`PlaystatsStuntPerformedEventDisallowTrigger`)

---
### PlaystatsWeaponModeChange

`PLAYSTATS_WEAPON_MODE_CHANGE` · hash `0xE95C8A1875A02CA4` · jhash `0x79716890` · **Cliente**

```lua
PlaystatsWeaponModeChange(weaponHash, componentHashTo, componentHashFrom)
```
```c
void PLAYSTATS_WEAPON_MODE_CHANGE(Hash weaponHash, Hash componentHashTo, Hash componentHashFrom);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHashTo` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHashFrom` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE95C8A1875A02CA4` (`N_0xe95c8a1875a02ca4`)

---
### PlaystatsWebsiteVisited

`PLAYSTATS_WEBSITE_VISITED` · hash `0xDDF24D535060F811` · jhash `0x37D152BB` · **Cliente**

```lua
PlaystatsWebsiteVisited(scaleformHash, p1)
```
```c
void PLAYSTATS_WEBSITE_VISITED(Hash scaleformHash, int p1);
```

**Parámetros**

- `scaleformHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDDF24D535060F811` (`N_0xddf24d535060f811`)

---
### PresenceEventUpdatestatFloat

`PRESENCE_EVENT_UPDATESTAT_FLOAT` · hash `0x30A6614C1F7799B8` · jhash `0x3E69E7C3` · **Cliente**

```lua
PresenceEventUpdatestatFloat(statHash, value, p2)
```
```c
void PRESENCE_EVENT_UPDATESTAT_FLOAT(Hash statHash, float value, int p2);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`float`)
- `p2` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x30A6614C1F7799B8` (`N_0x30a6614c1f7799b8`), `_UPDATE_STAT_FLOAT` (`UpdateStatFloat`)

---
### PresenceEventUpdatestatInt

`PRESENCE_EVENT_UPDATESTAT_INT` · hash `0x11FF1C80276097ED` · jhash `0x4AC39C6C` · **Cliente**

```lua
PresenceEventUpdatestatInt(statHash, value, p2)
```
```c
void PRESENCE_EVENT_UPDATESTAT_INT(Hash statHash, int value, int p2);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`int`)
- `p2` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x11FF1C80276097ED` (`N_0x11ff1c80276097ed`), `_UPDATE_STAT_INT` (`UpdateStatInt`)

---
### SetHasContentUnlocksFlags

`_SET_HAS_CONTENT_UNLOCKS_FLAGS` · hash `0xDAC073C7901F9E15` · **Cliente**

```lua
SetHasContentUnlocksFlags(value)
```
```c
void _SET_HAS_CONTENT_UNLOCKS_FLAGS(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets profile setting 866
SET_*
```

**Nombres antiguos (alias):** `0xDAC073C7901F9E15` (`N_0xdac073c7901f9e15`)

---
### SetProfileSettingPrologueComplete

`SET_PROFILE_SETTING_PROLOGUE_COMPLETE` · hash `0xB475F27C6A994D65` · jhash `0xC7DE5C30` · **Cliente**

```lua
SetProfileSettingPrologueComplete()
```
```c
void SET_PROFILE_SETTING_PROLOGUE_COMPLETE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB475F27C6A994D65` (`N_0xb475f27c6a994d65`)

---
### SetSaveMigrationTransactionId

`_SET_SAVE_MIGRATION_TRANSACTION_ID` · hash `0xF6792800AC95350D` · **Cliente**

```lua
SetSaveMigrationTransactionId(transactionId)
```
```c
void _SET_SAVE_MIGRATION_TRANSACTION_ID(int transactionId);
```

**Parámetros**

- `transactionId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets profile setting 501
```

**Nombres antiguos (alias):** `0xF6792800AC95350D` (`N_0xf6792800ac95350d`)

---
### StatClearSlotForReload

`STAT_CLEAR_SLOT_FOR_RELOAD` · hash `0xEB0A72181D4AA4AD` · jhash `0x84BDD475` · **Cliente**

```lua
local retval = StatClearSlotForReload(statSlot)
```
```c
Any STAT_CLEAR_SLOT_FOR_RELOAD(int statSlot);
```

**Parámetros**

- `statSlot` (`int`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Example:
for (v_2 = 0; v_2 <= 4; v_2 += 1) {
    STATS::STAT_CLEAR_SLOT_FOR_RELOAD(v_2);
}
```

---
### StatDeleteSlot

`STAT_DELETE_SLOT` · hash `0x49A49BED12794D70` · jhash `0x2F171B94` · **Cliente**

```lua
local retval = StatDeleteSlot(p0)
```
```c
Any STAT_DELETE_SLOT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### StatGetBool

`STAT_GET_BOOL` · hash `0x11B5E6D2AE73F48E` · jhash `0x28A3DD2B` · **Cliente**

```lua
local retval, outValue = StatGetBool(statHash, p2)
```
```c
BOOL STAT_GET_BOOL(Hash statHash, BOOL* outValue, Any p2);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outValue` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### StatGetBoolMasked

`STAT_GET_BOOL_MASKED` · hash `0x10FE3F1B79F9B071` · jhash `0x6ACE1B7D` · **Cliente**

```lua
local retval = StatGetBoolMasked(statName, mask, p2)
```
```c
BOOL STAT_GET_BOOL_MASKED(Hash statName, int mask, int p2);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `mask` (`int`)
- `p2` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p2 - Default value? Seems to be -1 most of the time.  
```

---
### StatGetCancelSaveMigrationStatus

`_STAT_GET_CANCEL_SAVE_MIGRATION_STATUS` · hash `0x567384DFA67029E6` · **Cliente**

```lua
local retval = StatGetCancelSaveMigrationStatus()
```
```c
int _STAT_GET_CANCEL_SAVE_MIGRATION_STATUS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x567384DFA67029E6` (`N_0x567384dfa67029e6`)

---
### StatGetDate

`STAT_GET_DATE` · hash `0x8B0FACEFC36C824B` · jhash `0xD762D16C` · **Cliente**

```lua
local retval, p1 = StatGetDate(statHash, p2, p3)
```
```c
BOOL STAT_GET_DATE(Hash statHash, Any* p1, Any p2, Any p3);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

---
### StatGetFloat

`STAT_GET_FLOAT` · hash `0xD7AE6C9C9C6AC54C` · jhash `0xFCBDA612` · **Cliente**

```lua
local retval, outValue = StatGetFloat(statHash, p2)
```
```c
BOOL STAT_GET_FLOAT(Hash statHash, float* outValue, Any p2);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outValue` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### StatGetInt

`STAT_GET_INT` · hash `0x767FBC2AC802EF3D` · jhash `0x1C6FE43E` · **Cliente**

```lua
local retval, outValue = StatGetInt(statHash, p2)
```
```c
BOOL STAT_GET_INT(Hash statHash, int* outValue, int p2);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outValue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p2 appears to always be -1  
```

---
### StatGetLicensePlate

`STAT_GET_LICENSE_PLATE` · hash `0x5473D4195058B2E4` · jhash `0x1544B29F` · **Cliente**

```lua
local retval = StatGetLicensePlate(statName)
```
```c
char* STAT_GET_LICENSE_PLATE(Hash statName);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `char*`

---
### StatGetMaskedInt

`STAT_GET_MASKED_INT` · hash `0x655185A06D9EEAAB` · jhash `0xE9D9B70F` · **Cliente**

```lua
local retval, p1 = StatGetMaskedInt(p0, p2, p3, p4)
```
```c
BOOL STAT_GET_MASKED_INT(Any p0, Any* p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `BOOL`

---
### StatGetNumberOfDays

`STAT_GET_NUMBER_OF_DAYS` · hash `0xE0E854F5280FB769` · jhash `0xFD66A429` · **Cliente**

```lua
local retval = StatGetNumberOfDays(statName)
```
```c
int STAT_GET_NUMBER_OF_DAYS(Hash statName);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xE0E854F5280FB769` (`N_0xe0e854f5280fb769`)

---
### StatGetNumberOfHours

`STAT_GET_NUMBER_OF_HOURS` · hash `0xF2D4B2FE415AAFC3` · jhash `0x9B431236` · **Cliente**

```lua
local retval = StatGetNumberOfHours(statName)
```
```c
int STAT_GET_NUMBER_OF_HOURS(Hash statName);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xF2D4B2FE415AAFC3` (`N_0xf2d4b2fe415aafc3`)

---
### StatGetNumberOfMinutes

`STAT_GET_NUMBER_OF_MINUTES` · hash `0x7583B4BE4C5A41B5` · jhash `0x347B4436` · **Cliente**

```lua
local retval = StatGetNumberOfMinutes(statName)
```
```c
int STAT_GET_NUMBER_OF_MINUTES(Hash statName);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x7583B4BE4C5A41B5` (`N_0x7583b4be4c5a41b5`)

---
### StatGetNumberOfSeconds

`STAT_GET_NUMBER_OF_SECONDS` · hash `0x2CE056FF3723F00B` · jhash `0x2C1D6C31` · **Cliente**

```lua
local retval = StatGetNumberOfSeconds(statName)
```
```c
int STAT_GET_NUMBER_OF_SECONDS(Hash statName);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x2CE056FF3723F00B` (`N_0x2ce056ff3723f00b`)

---
### StatGetPackedBoolMask

`_STAT_GET_PACKED_BOOL_MASK` · hash `0xF4D8E7AC2A27758C` · jhash `0xDFC25D66` · **Cliente**

```lua
local retval = StatGetPackedBoolMask(p0)
```
```c
int _STAT_GET_PACKED_BOOL_MASK(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Needs more research. Possibly used to calculate the "mask" when calling "STAT_SET_BOOL_MASKED"?  
```

**Nombres antiguos (alias):** `0xF4D8E7AC2A27758C` (`N_0xf4d8e7ac2a27758c`)

---
### StatGetPackedIntMask

`_STAT_GET_PACKED_INT_MASK` · hash `0x94F12ABF9C79E339` · jhash `0xCA160BCC` · **Cliente**

```lua
local retval = StatGetPackedIntMask(p0)
```
```c
int _STAT_GET_PACKED_INT_MASK(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Needs more research. Possibly used to calculate the "mask" when calling "STAT_SET_MASKED_INT"?  
```

**Nombres antiguos (alias):** `0x94F12ABF9C79E339` (`N_0x94f12abf9c79e339`)

---
### StatGetPos

`STAT_GET_POS` · hash `0x350F82CCB186AA1B` · jhash `0xC846ECCE` · **Cliente**

```lua
local retval, p1, p2, p3 = StatGetPos(p0, p4)
```
```c
BOOL STAT_GET_POS(Any p0, Any* p1, Any* p2, Any* p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any`)

**Devuelve:** `BOOL`

---
### StatGetSaveMigrationConsumeContentUnlockStatus

`_STAT_GET_SAVE_MIGRATION_CONSUME_CONTENT_UNLOCK_STATUS` · hash `0xCE5AA445ABA8DEE0` · **Cliente**

```lua
local retval, p0 = StatGetSaveMigrationConsumeContentUnlockStatus(p0)
```
```c
int _STAT_GET_SAVE_MIGRATION_CONSUME_CONTENT_UNLOCK_STATUS(int* p0);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xCE5AA445ABA8DEE0` (`N_0xce5aa445aba8dee0`)

---
### StatGetSaveMigrationStatus

`STAT_GET_SAVE_MIGRATION_STATUS` · hash `0x886913BBEACA68C1` · jhash `0xE3F0D62D` · **Cliente**

```lua
local retval, data = StatGetSaveMigrationStatus(data)
```
```c
int STAT_GET_SAVE_MIGRATION_STATUS(Any* data);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x886913BBEACA68C1` (`N_0x886913bbeaca68c1`)

---
### StatGetString

`STAT_GET_STRING` · hash `0xE50384ACC2C3DB74` · jhash `0x10CE4BDE` · **Cliente**

```lua
local retval = StatGetString(statHash, p1)
```
```c
char* STAT_GET_STRING(Hash statHash, int p1);
```

**Parámetros**

- `statHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
p1 is always -1 in the script files  
```

---
### StatGetUserId

`STAT_GET_USER_ID` · hash `0x2365C388E393BBE2` · jhash `0xE2E8B6BA` · **Cliente**

```lua
local retval = StatGetUserId(p0)
```
```c
char* STAT_GET_USER_ID(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Needs more research. Seems to return "STAT_UNKNOWN" if no such user id exists.  
```

---
### StatIncrement

`STAT_INCREMENT` · hash `0x9B5A68C6489E9909` · jhash `0xDFC5F71E` · **Cliente**

```lua
StatIncrement(statName, value)
```
```c
void STAT_INCREMENT(Hash statName, float value);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`float`)

**Devuelve:** `void`

---
### StatLoad

`STAT_LOAD` · hash `0xA651443F437B1CE6` · jhash `0x9E5629F4` · **Cliente**

```lua
local retval = StatLoad(p0)
```
```c
BOOL STAT_LOAD(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

---
### StatLoadPending

`STAT_LOAD_PENDING` · hash `0xA1750FFAFA181661` · jhash `0x4E9AC983` · **Cliente**

```lua
local retval = StatLoadPending(p0)
```
```c
BOOL STAT_LOAD_PENDING(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### StatMigrateSave

`_STAT_MIGRATE_SAVE` · hash `0xA5C80D8E768A9E66` · **Cliente**

```lua
local retval = StatMigrateSave(platformName)
```
```c
BOOL _STAT_MIGRATE_SAVE(char* platformName);
```

**Parámetros**

- `platformName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
platformName must be one of the following: ps3, xbox360, ps4, xboxone
```

**Nombres antiguos (alias):** `0xA5C80D8E768A9E66` (`N_0xa5c80d8e768a9e66`)

---
### StatSave

`STAT_SAVE` · hash `0xE07BCA305B82D2FD` · jhash `0xE10A7CA4` · **Cliente**

```lua
local retval = StatSave(p0, p1, p2)
```
```c
BOOL STAT_SAVE(int p0, BOOL p1, int p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`BOOL`)
- `p2` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 4: Any p3
```

---
### StatSaveMigrationCancel

`_STAT_SAVE_MIGRATION_CANCEL` · hash `0x4FEF53183C3C6414` · **Cliente**

```lua
local retval = StatSaveMigrationCancel()
```
```c
BOOL _STAT_SAVE_MIGRATION_CANCEL();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4FEF53183C3C6414` (`N_0x4fef53183c3c6414`)

---
### StatSaveMigrationConsumeContentUnlock

`_STAT_SAVE_MIGRATION_CONSUME_CONTENT_UNLOCK` · hash `0x3270F67EED31FBC1` · **Cliente**

```lua
local retval = StatSaveMigrationConsumeContentUnlock(contentId, srcPlatform, srcGamerHandle)
```
```c
BOOL _STAT_SAVE_MIGRATION_CONSUME_CONTENT_UNLOCK(Hash contentId, char* srcPlatform, char* srcGamerHandle);
```

**Parámetros**

- `contentId` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `srcPlatform` (`char*`)
- `srcGamerHandle` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3270F67EED31FBC1` (`N_0x3270f67eed31fbc1`)

---
### StatSaveMigrationStatusStart

`STAT_SAVE_MIGRATION_STATUS_START` · hash `0xC70DDCE56D0D3A99` · jhash `0x54E775E0` · **Cliente**

```lua
local retval = StatSaveMigrationStatusStart()
```
```c
BOOL STAT_SAVE_MIGRATION_STATUS_START();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC70DDCE56D0D3A99` (`N_0xc70ddce56d0d3a99`)

---
### StatSavePending

`STAT_SAVE_PENDING` · hash `0x7D3A583856F2C5AC` · jhash `0xC3FD3822` · **Cliente**

```lua
local retval = StatSavePending()
```
```c
BOOL STAT_SAVE_PENDING();
```

**Devuelve:** `BOOL`

---
### StatSavePendingOrRequested

`STAT_SAVE_PENDING_OR_REQUESTED` · hash `0xBBB6AD006F1BBEA3` · jhash `0xA3407CA3` · **Cliente**

```lua
local retval = StatSavePendingOrRequested()
```
```c
BOOL STAT_SAVE_PENDING_OR_REQUESTED();
```

**Devuelve:** `BOOL`

---
### StatSetBlockSaves

`STAT_SET_BLOCK_SAVES` · hash `0xF434A10BA01C37D0` · jhash `0xCE7A2411` · **Cliente**

```lua
StatSetBlockSaves(toggle)
```
```c
void STAT_SET_BLOCK_SAVES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF434A10BA01C37D0` (`N_0xf434a10ba01c37d0`)

---
### StatSetBool

`STAT_SET_BOOL` · hash `0x4B33C4243DE0C432` · jhash `0x55D79DFB` · **Cliente**

```lua
local retval = StatSetBool(statName, value, save)
```
```c
BOOL STAT_SET_BOOL(Hash statName, BOOL value, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`BOOL`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Example:
 STATS::STAT_SET_BOOL(MISC::GET_HASH_KEY("MPPLY_MELEECHLENGECOMPLETED"), trur, true);
```

---
### StatSetBoolMasked

`STAT_SET_BOOL_MASKED` · hash `0x5BC62EC1937B9E5B` · jhash `0x7842C4D6` · **Cliente**

```lua
local retval = StatSetBoolMasked(statName, value, mask, save)
```
```c
BOOL STAT_SET_BOOL_MASKED(Hash statName, BOOL value, int mask, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`BOOL`)
- `mask` (`int`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

---
### StatSetCheatIsActive

`STAT_SET_CHEAT_IS_ACTIVE` · hash `0x047CBED6F6F8B63C` · jhash `0xA063CABD` · **Cliente**

```lua
StatSetCheatIsActive()
```
```c
void STAT_SET_CHEAT_IS_ACTIVE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x047CBED6F6F8B63C` (`N_0x047cbed6f6f8b63c`)

---
### StatSetCurrentPosixTime

`STAT_SET_CURRENT_POSIX_TIME` · hash `0xC2F84B7F9C4D0C61` · jhash `0xA286F015` · **Cliente**

```lua
local retval = StatSetCurrentPosixTime(statName, p1)
```
```c
BOOL STAT_SET_CURRENT_POSIX_TIME(Hash statName, BOOL p1);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 always true.  
```

---
### StatSetDate

`STAT_SET_DATE` · hash `0x2C29BFB64F4FCBE4` · jhash `0x36BE807B` · **Cliente**

```lua
local retval, value = StatSetDate(statName, numFields, save)
```
```c
BOOL STAT_SET_DATE(Hash statName, Any* value, int numFields, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `numFields` (`int`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
'value' is a structure to a structure, 'numFields' is how many fields there are in said structure (usually 7).  
The structure looks like this:  
int year  
int month  
int day  
int hour  
int minute  
int second  
int millisecond  
The decompiled scripts use TIME::GET_POSIX_TIME to fill this structure.  
```

---
### StatSetFloat

`STAT_SET_FLOAT` · hash `0x4851997F37FE9B3C` · jhash `0x6CEA96F2` · **Cliente**

```lua
local retval = StatSetFloat(statName, value, save)
```
```c
BOOL STAT_SET_FLOAT(Hash statName, float value, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`float`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Example:
 STATS::STAT_SET_FLOAT(MISC::GET_HASH_KEY("MP0_WEAPON_ACCURACY"), 66.6f, true);
```

---
### StatSetGxtLabel

`STAT_SET_GXT_LABEL` · hash `0x17695002FD8B2AE0` · jhash `0xC1224AA7` · **Cliente**

```lua
local retval = StatSetGxtLabel(statName, value, save)
```
```c
BOOL STAT_SET_GXT_LABEL(Hash statName, char* value, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`char*`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
The following values have been found in the decompiled scripts:  
"RC_ABI1"  
"RC_ABI2"  
"RC_BA1"  
"RC_BA2"  
"RC_BA3"  
"RC_BA3A"  
"RC_BA3C"  
"RC_BA4"  
"RC_DRE1"  
"RC_EPS1"  
"RC_EPS2"  
"RC_EPS3"  
"RC_EPS4"  
"RC_EPS5"  
"RC_EPS6"  
"RC_EPS7"  
"RC_EPS8"  
"RC_EXT1"  
"RC_EXT2"  
"RC_EXT3"  
"RC_EXT4"  
"RC_FAN1"  
"RC_FAN2"  
"RC_FAN3"  
"RC_HAO1"  
"RC_HUN1"  
"RC_HUN2"  
"RC_JOS1"  
"RC_JOS2"  
"RC_JOS3"  
"RC_JOS4"  
"RC_MAU1"  
"RC_MIN1"  
"RC_MIN2"  
"RC_MIN3"  
"RC_MRS1"  
"RC_MRS2"  
"RC_NI1"  
"RC_NI1A"  
"RC_NI1B"  
"RC_NI1C"  
"RC_NI1D"  
"RC_NI2"  
"RC_NI3"  
"RC_OME1"  
"RC_OME2"  
"RC_PA1"  
"RC_PA2"  
"RC_PA3"  
"RC_PA3A"  
"RC_PA3B"  
"RC_PA4"  
"RC_RAM1"  
"RC_RAM2"  
"RC_RAM3"  
"RC_RAM4"  
"RC_RAM5"  
"RC_SAS1"  
"RC_TON1"  
"RC_TON2"  
"RC_TON3"  
"RC_TON4"  
"RC_TON5"  
```

---
### StatSetInt

`STAT_SET_INT` · hash `0xB3271D7AB655B441` · jhash `0xC9CC1C5C` · **Cliente**

```lua
local retval = StatSetInt(statName, value, save)
```
```c
BOOL STAT_SET_INT(Hash statName, int value, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`int`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

**Ejemplo (lua):**

```lua
StatSetInt(`MPPLY_KILLS_PLAYERS`, 1337, true)
StatSetInt(`MP0_SHOOTING_ABILITY`, 100, true)
StatSetInt(`MP0_SHOOTING_ABILITY`, 100, true)
StatSetInt(`MP0_STEALTH_ABILITY`, 10, true)
StatSetInt(`MP0_FLYING_ABILITY`, 5, true)
StatSetInt(`MP0_WHEELIE_ABILITY`, 25, true)
StatSetInt(`MP0_LUNG_CAPACITY`, 35, true)
StatSetInt(`MP0_STRENGTH`, 15, true)
StatSetInt(`MP0_STAMINA`, 25, true)
```

---
### StatSetLicensePlate

`STAT_SET_LICENSE_PLATE` · hash `0x69FF13266D7296DA` · jhash `0x3507D253` · **Cliente**

```lua
local retval = StatSetLicensePlate(statName, str)
```
```c
BOOL STAT_SET_LICENSE_PLATE(Hash statName, char* str);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `str` (`char*`)

**Devuelve:** `BOOL`

---
### StatSetMaskedInt

`STAT_SET_MASKED_INT` · hash `0x7BBB1B54583ED410` · jhash `0x2CBAA739` · **Cliente**

```lua
local retval = StatSetMaskedInt(statName, p1, p2, p3, save)
```
```c
BOOL STAT_SET_MASKED_INT(Hash statName, Any p1, Any p2, int p3, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`int`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

---
### StatSetPos

`STAT_SET_POS` · hash `0xDB283FDE680FE72E` · jhash `0x1192C9A3` · **Cliente**

```lua
local retval = StatSetPos(statName, x, y, z, save)
```
```c
BOOL STAT_SET_POS(Hash statName, float x, float y, float z, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

---
### StatSetProfileSettingValue

`STAT_SET_PROFILE_SETTING_VALUE` · hash `0x68F01422BE1D838F` · jhash `0x24DD4929` · **Cliente**

```lua
StatSetProfileSettingValue(profileSetting, value)
```
```c
void STAT_SET_PROFILE_SETTING_VALUE(int profileSetting, int value);
```

**Parámetros**

- `profileSetting` (`int`)
- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does not take effect immediately, unfortunately.
profileSetting seems to only be 936, 937 and 938 in scripts
```

**Nombres antiguos (alias):** `0x68F01422BE1D838F` (`N_0x68f01422be1d838f`), `_STAT_SET_PROFILE_SETTING` (`StatSetProfileSetting`)

---
### StatSetString

`STAT_SET_STRING` · hash `0xA87B2335D12531D7` · jhash `0xB1EF2E21` · **Cliente**

```lua
local retval = StatSetString(statName, value, save)
```
```c
BOOL STAT_SET_STRING(Hash statName, char* value, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`char*`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

---
### StatSetUserId

`STAT_SET_USER_ID` · hash `0x8CDDF1E452BABE11` · jhash `0xDBE78ED7` · **Cliente**

```lua
local retval = StatSetUserId(statName, value, save)
```
```c
BOOL STAT_SET_USER_ID(Hash statName, char* value, BOOL save);
```

**Parámetros**

- `statName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`char*`)
- `save` (`BOOL`)

**Devuelve:** `BOOL`

---
### StatSlotIsLoaded

`STAT_SLOT_IS_LOADED` · hash `0x0D0A9F0E7BD91E3C` · jhash `0x7A299C13` · **Cliente**

```lua
local retval = StatSlotIsLoaded(p0)
```
```c
BOOL STAT_SLOT_IS_LOADED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
