# Natives de GTA V — NETWORK (parte 1 de 2: ActivateDamageTrackerOnNetworkId … SetNetworkVehicleAsGhost)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `NETWORK`: **823** natives.

Partes: **[1]** · [2](NETWORK-2.md)

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateDamageTrackerOnNetworkId`](#activatedamagetrackeronnetworkid) · [`ActivateDamageTrackerOnPlayer`](#activatedamagetrackeronplayer) · [`BadSportPlayerLeftDetected`](#badsportplayerleftdetected) · [`CanRegisterMissionEntities`](#canregistermissionentities) · [`CanRegisterMissionObjects`](#canregistermissionobjects) · [`CanRegisterMissionPeds`](#canregistermissionpeds) · [`CanRegisterMissionPickups`](#canregistermissionpickups) · [`CanRegisterMissionVehicles`](#canregistermissionvehicles) · [`ClearLaunchParams`](#clearlaunchparams) · [`CloudCheckAvailability`](#cloudcheckavailability) · [`CloudDeleteMemberFile`](#clouddeletememberfile) · [`CloudDidRequestSucceed`](#clouddidrequestsucceed) · [`CloudGetAvailabilityCheckResult`](#cloudgetavailabilitycheckresult) · [`CloudHasRequestCompleted`](#cloudhasrequestcompleted) · [`CloudIsCheckingAvailability`](#cloudischeckingavailability) · [`ConvertPosixTime`](#convertposixtime) · [`FacebookDoUnkCheck`](#facebookdounkcheck) · [`FacebookIsAvailable`](#facebookisavailable) · [`FacebookIsSendingData`](#facebookissendingdata) · [`FacebookSetCreateCharacterComplete`](#facebooksetcreatecharactercomplete) · [`FacebookSetHeistComplete`](#facebooksetheistcomplete) · [`FacebookSetMilestoneComplete`](#facebooksetmilestonecomplete) · [`FadeOutLocalPlayer`](#fadeoutlocalplayer) · [`FilloutPmPlayerList`](#filloutpmplayerlist) · [`FilloutPmPlayerListWithNames`](#filloutpmplayerlistwithnames) · [`GetCloudTimeAsInt`](#getcloudtimeasint) · [`GetCloudTimeAsString`](#getcloudtimeasstring) · [`GetCommerceItemCat`](#getcommerceitemcat) · [`GetCommerceItemId`](#getcommerceitemid) · [`GetCommerceItemName`](#getcommerceitemname) · [`GetCommerceItemNumCats`](#getcommerceitemnumcats) · [`GetCommerceItemTexturename`](#getcommerceitemtexturename) · [`GetCommerceProductPrice`](#getcommerceproductprice) · [`GetMaxNumNetworkObjects`](#getmaxnumnetworkobjects) · [`GetMaxNumNetworkPeds`](#getmaxnumnetworkpeds) · [`GetMaxNumNetworkPickups`](#getmaxnumnetworkpickups) · [`GetMaxNumNetworkVehicles`](#getmaxnumnetworkvehicles) · [`GetNetworkTime`](#getnetworktime) · [`GetNetworkTimeAccurate`](#getnetworktimeaccurate) · [`GetNumCommerceItems`](#getnumcommerceitems) · [`GetNumCreatedMissionObjects`](#getnumcreatedmissionobjects) · [`GetNumCreatedMissionPeds`](#getnumcreatedmissionpeds) · [`GetNumCreatedMissionVehicles`](#getnumcreatedmissionvehicles) · [`GetNumReservedMissionObjects`](#getnumreservedmissionobjects) · [`GetNumReservedMissionPeds`](#getnumreservedmissionpeds) · [`GetNumReservedMissionVehicles`](#getnumreservedmissionvehicles) · [`GetOnlineVersion`](#getonlineversion) · [`GetStatusOfTextureDownload`](#getstatusoftexturedownload) · [`GetTimeAsString`](#gettimeasstring) · [`GetTimeDifference`](#gettimedifference) · [`GetTimeOffset`](#gettimeoffset) · [`HasNetworkTimeStarted`](#hasnetworktimestarted) · [`IsCommerceDataValid`](#iscommercedatavalid) · [`IsCommerceStoreOpen`](#iscommercestoreopen) · [`IsDamageTrackerActiveOnNetworkId`](#isdamagetrackeractiveonnetworkid) · [`IsDamageTrackerActiveOnPlayer`](#isdamagetrackeractiveonplayer) · [`IsEntityGhostedToLocalPlayer`](#isentityghostedtolocalplayer) · [`IsNetworkIdOwnedByParticipant`](#isnetworkidownedbyparticipant) · [`IsPlayerInCutscene`](#isplayerincutscene) · [`IsSphereVisibleToAnotherMachine`](#isspherevisibletoanothermachine) · [`IsSphereVisibleToPlayer`](#isspherevisibletoplayer) · [`IsStoreAvailableToUser`](#isstoreavailabletouser) · [`IsTimeEqualTo`](#istimeequalto) · [`IsTimeLessThan`](#istimelessthan) · [`IsTimeMoreThan`](#istimemorethan) · [`N_0x023acab2dc9dc4a4`](#n_0x023acab2dc9dc4a4) · [`N_0x041c7f2a6c9894e6`](#n_0x041c7f2a6c9894e6) · [`N_0x04918a41bc9b8157`](#n_0x04918a41bc9b8157) · [`N_0x07eab372c8841d99`](#n_0x07eab372c8841d99) · [`N_0x0cf6cc51aa18f0f8`](#n_0x0cf6cc51aa18f0f8) · [`N_0x0d77a82dc2d0da59`](#n_0x0d77a82dc2d0da59) · [`N_0x0ede326d47cd0f3e`](#n_0x0ede326d47cd0f3e) · [`N_0x0f1a4b45b7693b95`](#n_0x0f1a4b45b7693b95) · [`N_0x1153fa02a659051c`](#n_0x1153fa02a659051c) · [`N_0x1171a97a3d3981b6`](#n_0x1171a97a3d3981b6) · [`N_0x1398582b7f72b3ed`](#n_0x1398582b7f72b3ed) · [`N_0x13f1fcb111b820b0`](#n_0x13f1fcb111b820b0) · [`N_0x140e6a44870a11ce`](#n_0x140e6a44870a11ce) · [`N_0x144da052257ae7d8`](#n_0x144da052257ae7d8) · [`N_0x14922ed3e38761f0`](#n_0x14922ed3e38761f0) · [`N_0x155467aca0f55705`](#n_0x155467aca0f55705) · [`N_0x162c23ca83ed0a62`](#n_0x162c23ca83ed0a62) · [`N_0x17c9e241111a674d`](#n_0x17c9e241111a674d) · [`N_0x1d4dc17c38feaff0`](#n_0x1d4dc17c38feaff0) · [`N_0x1d610eb0fea716d9`](#n_0x1d610eb0fea716d9) · [`N_0x1f7bc3539f9e0224`](#n_0x1f7bc3539f9e0224) · [`N_0x1f8e00fb18239600`](#n_0x1f8e00fb18239600) · [`N_0x2302c0264ea58d31`](#n_0x2302c0264ea58d31) · [`N_0x24e4e51fc16305f9`](#n_0x24e4e51fc16305f9) · [`N_0x2555cf7da5473794`](#n_0x2555cf7da5473794) · [`N_0x25d990f8e0e3f13c`](#n_0x25d990f8e0e3f13c) · [`N_0x261e97ad7bcf3d40`](#n_0x261e97ad7bcf3d40) · [`N_0x265559da40b3f327`](#n_0x265559da40b3f327) · [`N_0x265635150fb0d82e`](#n_0x265635150fb0d82e) · [`N_0x26f07dd83a5f7f98`](#n_0x26f07dd83a5f7f98) · [`N_0x283b6062a2c01e9b`](#n_0x283b6062a2c01e9b) · [`N_0x2b1c623823db0d9d`](#n_0x2b1c623823db0d9d) · [`N_0x2b51edbefc301339`](#n_0x2b51edbefc301339) · [`N_0x2bf66d2e7414f686`](#n_0x2bf66d2e7414f686) · [`N_0x2ce9d95e4051aecd`](#n_0x2ce9d95e4051aecd) · [`N_0x2d5dc831176d0114`](#n_0x2d5dc831176d0114) · [`N_0x2da41ed6e1fcd7a5`](#n_0x2da41ed6e1fcd7a5) · [`N_0x2e0bf682cc778d49`](#n_0x2e0bf682cc778d49) · [`N_0x2e4c123d1c8a710e`](#n_0x2e4c123d1c8a710e) · [`N_0x32ebd154cb6b8b99`](#n_0x32ebd154cb6b8b99) · [`N_0x36391f397731595d`](#n_0x36391f397731595d) · [`N_0x367ef5e2f439b4c6`](#n_0x367ef5e2f439b4c6) · [`N_0x37d5f739fd494675`](#n_0x37d5f739fd494675) · [`N_0x3855fb5eb2c5e8b2`](#n_0x3855fb5eb2c5e8b2) · [`N_0x38b7c51ab1edc7d8`](#n_0x38b7c51ab1edc7d8) · [`N_0x39917e1b4cb0f911`](#n_0x39917e1b4cb0f911) · [`N_0x3c5c1e2c2ff814b1`](#n_0x3c5c1e2c2ff814b1) · [`N_0x3fa36981311fa4ff`](#n_0x3fa36981311fa4ff) · [`N_0x3fc795691834481d`](#n_0x3fc795691834481d) · [`N_0x4237e822315d8ba9`](#n_0x4237e822315d8ba9) · [`N_0x4348bfda56023a2f`](#n_0x4348bfda56023a2f) · [`N_0x444c4525ece0a4b9`](#n_0x444c4525ece0a4b9) · [`N_0x45e816772e93a9db`](#n_0x45e816772e93a9db) · [`N_0x4811bbac21c5fcd5`](#n_0x4811bbac21c5fcd5) · [`N_0x4a9fde3a5a6d0437`](#n_0x4a9fde3a5a6d0437) · [`N_0x4ad490ae1536933b`](#n_0x4ad490ae1536933b) · [`N_0x4c2a9fdc22377075`](#n_0x4c2a9fdc22377075) · [`N_0x4c9034162368e206`](#n_0x4c9034162368e206) · [`N_0x4d02279c83be69fe`](#n_0x4d02279c83be69fe) · [`N_0x4df7cfff471a7fb1`](#n_0x4df7cfff471a7fb1) · [`N_0x5324a0e3e4ce3570`](#n_0x5324a0e3e4ce3570) · [`N_0x53c10c8bd774f2c9`](#n_0x53c10c8bd774f2c9) · [`N_0x5539c3ebf104a53a`](#n_0x5539c3ebf104a53a) · [`N_0x559ebf901a8c68e0`](#n_0x559ebf901a8c68e0) · [`N_0x560b423d73015e77`](#n_0x560b423d73015e77) · [`N_0x584770794d758c18`](#n_0x584770794d758c18) · [`N_0x59328eb08c5ceb2b`](#n_0x59328eb08c5ceb2b) · [`N_0x59d421683d31835a`](#n_0x59d421683d31835a) · [`N_0x5a34cd9c3c5bec44`](#n_0x5a34cd9c3c5bec44) · [`N_0x5c497525f803486b`](#n_0x5c497525f803486b) · [`N_0x5e3aa4ca2b6fb0ee`](#n_0x5e3aa4ca2b6fb0ee) · [`N_0x5ecd378ee64450ab`](#n_0x5ecd378ee64450ab) · [`N_0x600f8cb31c7aab6e`](#n_0x600f8cb31c7aab6e) · [`N_0x60edd13eb3ac1ff3`](#n_0x60edd13eb3ac1ff3) · [`N_0x617f49c2668e6155`](#n_0x617f49c2668e6155) · [`N_0x63b406d7884bfa95`](#n_0x63b406d7884bfa95) · [`N_0x64d779659bc37b19`](#n_0x64d779659bc37b19) · [`N_0x64e5c4cc82847b73`](#n_0x64e5c4cc82847b73) · [`N_0x67fc09bc554a75e5`](#n_0x67fc09bc554a75e5) · [`N_0x68103e2247887242`](#n_0x68103e2247887242) · [`N_0x692d58df40657e8c`](#n_0x692d58df40657e8c) · [`N_0x6a5d89d7769a40d8`](#n_0x6a5d89d7769a40d8) · [`N_0x6bff5f84102df80a`](#n_0x6bff5f84102df80a) · [`N_0x6ce50e47f5543d0c`](#n_0x6ce50e47f5543d0c) · [`N_0x6fb7bb3607d27fa2`](#n_0x6fb7bb3607d27fa2) · [`N_0x6fd992c4a1c1b986`](#n_0x6fd992c4a1c1b986) · [`N_0x702bc4d605522539`](#n_0x702bc4d605522539) · [`N_0x741a3d8380319a81`](#n_0x741a3d8380319a81) · [`N_0x742b58f723233ed9`](#n_0x742b58f723233ed9) · [`N_0x74fb3e29e6d10fa9`](#n_0x74fb3e29e6d10fa9) · [`N_0x754615490a029508`](#n_0x754615490a029508) · [`N_0x76b3f29d3f967692`](#n_0x76b3f29d3f967692) · [`N_0x77faddcbe3499df7`](#n_0x77faddcbe3499df7) · [`N_0x7808619f31ff22db`](#n_0x7808619f31ff22db) · [`N_0x78321bea235fd8cd`](#n_0x78321bea235fd8cd) · [`N_0x793ff272d5b365f4`](#n_0x793ff272d5b365f4) · [`N_0x7d395ea61622e116`](#n_0x7d395ea61622e116) · [`N_0x7db53b37a2f211a0`](#n_0x7db53b37a2f211a0) · [`N_0x7ef7649b64d7ff10`](#n_0x7ef7649b64d7ff10) · [`N_0x7fcc39c46c3c03bd`](#n_0x7fcc39c46c3c03bd) · [`N_0x83660b734994124d`](#n_0x83660b734994124d) · [`N_0x83fe8d7229593017`](#n_0x83fe8d7229593017) · [`N_0x88b588b41ff7868e`](#n_0x88b588b41ff7868e) · [`N_0x8b0c2964ba471961`](#n_0x8b0c2964ba471961) · [`N_0x8b4ffc790ca131ef`](#n_0x8b4ffc790ca131ef) · [`N_0x8c8d2739ba44af0f`](#n_0x8c8d2739ba44af0f) · [`N_0x8ef52acaecc51d9c`](#n_0x8ef52acaecc51d9c) · [`N_0x906ca41a4b74eca4`](#n_0x906ca41a4b74eca4) · [`N_0x94538037ee44f5cf`](#n_0x94538037ee44f5cf) · [`N_0x9465e683b12d3f6b`](#n_0x9465e683b12d3f6b) · [`N_0x95baf97c82464629`](#n_0x95baf97c82464629) · [`N_0x973d76aa760a6cb6`](#n_0x973d76aa760a6cb6) · [`N_0x9d724b400a7e8ffc`](#n_0x9d724b400a7e8ffc) · [`N_0x9d7afcbf21c51712`](#n_0x9d7afcbf21c51712) · [`N_0x9fedf86898f100e9`](#n_0x9fedf86898f100e9) · [`N_0xa0fa4ec6a05da44e`](#n_0xa0fa4ec6a05da44e) · [`N_0xa12d3a5a3753cc23`](#n_0xa12d3a5a3753cc23) · [`N_0xa2e9c1ab8a92e8cd`](#n_0xa2e9c1ab8a92e8cd) · [`N_0xa306f470d1660581`](#n_0xa306f470d1660581) · [`N_0xa6fceccf4721d679`](#n_0xa6fceccf4721d679) · [`N_0xa7862bc5ed1dfd7e`](#n_0xa7862bc5ed1dfd7e) · [`N_0xa8acb6459542a8c8`](#n_0xa8acb6459542a8c8) · [`N_0xaa5fafcd2c5f5e47`](#n_0xaa5fafcd2c5f5e47) · [`N_0xadb57e5b663cca8b`](#n_0xadb57e5b663cca8b) · [`N_0xaeab987727c5a8a4`](#n_0xaeab987727c5a8a4) · [`N_0xaedf1bc1c133d6e3`](#n_0xaedf1bc1c133d6e3) · [`N_0xb13e88e655e5a3bc`](#n_0xb13e88e655e5a3bc) · [`N_0xb309ebea797e001f`](#n_0xb309ebea797e001f) · [`N_0xb37e4e6a2388ca7b`](#n_0xb37e4e6a2388ca7b) · [`N_0xb5d3453c98456528`](#n_0xb5d3453c98456528) · [`N_0xb606e6cc59664972`](#n_0xb606e6cc59664972) · [`N_0xb746d20b17f2a229`](#n_0xb746d20b17f2a229) · [`N_0xb9351a07a0d458b1`](#n_0xb9351a07a0d458b1) · [`N_0xba7f0b77d80a4eb7`](#n_0xba7f0b77d80a4eb7) · [`N_0xbd545d44cce70597`](#n_0xbd545d44cce70597) · [`N_0xbdb6f89c729cf388`](#n_0xbdb6f89c729cf388) · [`N_0xbf22e0f32968e967`](#n_0xbf22e0f32968e967) · [`N_0xc32ea7a2f6ca7557`](#n_0xc32ea7a2f6ca7557) · [`N_0xc42dd763159f3461`](#n_0xc42dd763159f3461) · [`N_0xc434133d9ba52777`](#n_0xc434133d9ba52777) · [`N_0xc571d0e77d8bbc29`](#n_0xc571d0e77d8bbc29) · [`N_0xc87e740d9f3872cc`](#n_0xc87e740d9f3872cc) · [`N_0xca575c391fea25cc`](#n_0xca575c391fea25cc) · [`N_0xca59ccae5d01e4ce`](#n_0xca59ccae5d01e4ce) · [`N_0xcfeb46dcd7d8d5eb`](#n_0xcfeb46dcd7d8d5eb) · [`N_0xd313de83394af134`](#n_0xd313de83394af134) · [`N_0xd6d7478ca62b8d41`](#n_0xd6d7478ca62b8d41) · [`N_0xd7b6c73cad419bcf`](#n_0xd7b6c73cad419bcf) · [`N_0xdb663cc9ff3407a9`](#n_0xdb663cc9ff3407a9) · [`N_0xe16aa70ce9beedc3`](#n_0xe16aa70ce9beedc3) · [`N_0xe42d626eec94e5d9`](#n_0xe42d626eec94e5d9) · [`N_0xe6717e652b8c8d8a`](#n_0xe6717e652b8c8d8a) · [`N_0xea8c0ddb10e2822a`](#n_0xea8c0ddb10e2822a) · [`N_0xebcab9e5048434f4`](#n_0xebcab9e5048434f4) · [`N_0xebf8284d8cadeb53`](#n_0xebf8284d8cadeb53) · [`N_0xebfa8d50addc54c4`](#n_0xebfa8d50addc54c4) · [`N_0xf083835b70ba9bfe`](#n_0xf083835b70ba9bfe) · [`N_0xf287f506767cc8a9`](#n_0xf287f506767cc8a9) · [`N_0xf49abc20d8552257`](#n_0xf49abc20d8552257) · [`N_0xf6f4383b7c92f11a`](#n_0xf6f4383b7c92f11a) · [`N_0xf814fec6a19fd6e0`](#n_0xf814fec6a19fd6e0) · [`N_0xfa2888e3833c8e96`](#n_0xfa2888e3833c8e96) · [`N_0xfac18e7356bd3210`](#n_0xfac18e7356bd3210) · [`N_0xfae628f1e9adb239`](#n_0xfae628f1e9adb239) · [`N_0xfb1f9381e80fa13f`](#n_0xfb1f9381e80fa13f) · [`N_0xfb680d403909dc70`](#n_0xfb680d403909dc70) · [`N_0xfd75dabc0957bf33`](#n_0xfd75dabc0957bf33) · [`NetToEnt`](#nettoent) · [`NetToObj`](#nettoobj) · [`NetToPed`](#nettoped) · [`NetToVeh`](#nettoveh) · [`NetworkAcceptInvite`](#networkacceptinvite) · [`NetworkAcceptPresenceInvite`](#networkacceptpresenceinvite) · [`NetworkAccessTunableBool`](#networkaccesstunablebool) · [`NetworkAccessTunableBoolHash`](#networkaccesstunableboolhash) · [`NetworkAccessTunableFloat`](#networkaccesstunablefloat) · [`NetworkAccessTunableFloatHash`](#networkaccesstunablefloathash) · [`NetworkAccessTunableInt`](#networkaccesstunableint) · [`NetworkAccessTunableIntHash`](#networkaccesstunableinthash) · [`NetworkActionFollowInvite`](#networkactionfollowinvite) · [`NetworkAddEntityAngledArea`](#networkaddentityangledarea) · [`NetworkAddEntityArea`](#networkaddentityarea) · [`NetworkAddEntityDisplayedBoundaries`](#networkaddentitydisplayedboundaries) · [`NetworkAddEntityToSynchronisedScene`](#networkaddentitytosynchronisedscene) · [`NetworkAddFollowers`](#networkaddfollowers) · [`NetworkAddFriend`](#networkaddfriend) · [`NetworkAddMapEntityToSynchronisedScene`](#networkaddmapentitytosynchronisedscene) · [`NetworkAddPedToSynchronisedScene`](#networkaddpedtosynchronisedscene) · [`NetworkAddPedToSynchronisedSceneWithIk`](#networkaddpedtosynchronisedscenewithik) · [`NetworkAddSynchronisedSceneCamera`](#networkaddsynchronisedscenecamera) · [`NetworkAllocateTunablesRegistrationDataMap`](#networkallocatetunablesregistrationdatamap) · [`NetworkAllowRemoteAttachmentModification`](#networkallowremoteattachmentmodification) · [`NetworkAmIBlockedByGamer`](#networkamiblockedbygamer) · [`NetworkAmIBlockedByPlayer`](#networkamiblockedbyplayer) · [`NetworkAmIMutedByGamer`](#networkamimutedbygamer) · [`NetworkAmIMutedByPlayer`](#networkamimutedbyplayer) · [`NetworkApplyCachedPlayerHeadBlendData`](#networkapplycachedplayerheadblenddata) · [`NetworkApplyPedScarData`](#networkapplypedscardata) · [`NetworkApplyTransitionParameter`](#networkapplytransitionparameter) · [`NetworkApplyTransitionParameterString`](#networkapplytransitionparameterstring) · [`NetworkApplyVoiceProximityOverride`](#networkapplyvoiceproximityoverride) · [`NetworkAreCutsceneEntities`](#networkarecutsceneentities) · [`NetworkAreHandlesTheSame`](#networkarehandlesthesame) · [`NetworkAreSocialClubPoliciesCurrent`](#networkaresocialclubpoliciescurrent) · [`NetworkAreTransitionDetailsValid`](#networkaretransitiondetailsvalid) · [`NetworkAttachSynchronisedSceneToEntity`](#networkattachsynchronisedscenetoentity) · [`NetworkBail`](#networkbail) · [`NetworkBailTransition`](#networkbailtransition) · [`NetworkBailTransitionQuickmatch`](#networkbailtransitionquickmatch) · [`NetworkBlockInvites`](#networkblockinvites) · [`NetworkBlockJoinQueueInvites`](#networkblockjoinqueueinvites) · [`NetworkBlockKickedPlayers`](#networkblockkickedplayers) · [`NetworkCacheLocalPlayerHeadBlendData`](#networkcachelocalplayerheadblenddata) · [`NetworkCanAccessMultiplayer`](#networkcanaccessmultiplayer) · [`NetworkCanBail`](#networkcanbail) · [`NetworkCanCommunicateWithGamer`](#networkcancommunicatewithgamer) · [`NetworkCanCommunicateWithGamer_2`](#networkcancommunicatewithgamer_2) · [`NetworkCanEnterMultiplayer`](#networkcanentermultiplayer) · [`NetworkCanGamerPlayMultiplayerWithMe`](#networkcangamerplaymultiplayerwithme) · [`NetworkCanPlayMultiplayerWithGamer`](#networkcanplaymultiplayerwithgamer) · [`NetworkCanSessionEnd`](#networkcansessionend) · [`NetworkCanSetWaypoint`](#networkcansetwaypoint) · [`NetworkCanViewGamerUserContent`](#networkcanviewgamerusercontent) · [`NetworkCancelRespawnSearch`](#networkcancelrespawnsearch) · [`NetworkChangeTransitionSlots`](#networkchangetransitionslots) · [`NetworkCheckCommunicationPrivileges`](#networkcheckcommunicationprivileges) · [`NetworkCheckDataManagerSucceededForHandle`](#networkcheckdatamanagersucceededforhandle) · [`NetworkCheckUserContentPrivileges`](#networkcheckusercontentprivileges) · [`NetworkClanAnimation`](#networkclananimation) · [`NetworkClanAnyDownloadMembershipPending`](#networkclananydownloadmembershippending) · [`NetworkClanDownloadMembership`](#networkclandownloadmembership) · [`NetworkClanDownloadMembershipPending`](#networkclandownloadmembershippending) · [`NetworkClanGetEmblemTxdName`](#networkclangetemblemtxdname) · [`NetworkClanGetLocalMembershipsCount`](#networkclangetlocalmembershipscount) · [`NetworkClanGetMembership`](#networkclangetmembership) · [`NetworkClanGetMembershipCount`](#networkclangetmembershipcount) · [`NetworkClanGetMembershipDesc`](#networkclangetmembershipdesc) · [`NetworkClanGetMembershipValid`](#networkclangetmembershipvalid) · [`NetworkClanGetUiFormattedTag`](#networkclangetuiformattedtag) · [`NetworkClanIsEmblemReady`](#networkclanisemblemready) · [`NetworkClanIsRockstarClan`](#networkclanisrockstarclan) · [`NetworkClanJoin`](#networkclanjoin) · [`NetworkClanPlayerGetDesc`](#networkclanplayergetdesc) · [`NetworkClanPlayerIsActive`](#networkclanplayerisactive) · [`NetworkClanReleaseEmblem`](#networkclanreleaseemblem) · [`NetworkClanRemoteMembershipsAreInCache`](#networkclanremotemembershipsareincache) · [`NetworkClanRequestEmblem`](#networkclanrequestemblem) · [`NetworkClanServiceIsValid`](#networkclanserviceisvalid) · [`NetworkClearClockTimeOverride`](#networkclearclocktimeoverride) · [`NetworkClearFollowInvite`](#networkclearfollowinvite) · [`NetworkClearFollowers`](#networkclearfollowers) · [`NetworkClearFoundGamers`](#networkclearfoundgamers) · [`NetworkClearGetGamerStatus`](#networkcleargetgamerstatus) · [`NetworkClearGroupActivity`](#networkcleargroupactivity) · [`NetworkClearPropertyId`](#networkclearpropertyid) · [`NetworkClearTransitionCreatorHandle`](#networkcleartransitioncreatorhandle) · [`NetworkClearVoiceChannel`](#networkclearvoicechannel) · [`NetworkClearVoiceProximityOverride`](#networkclearvoiceproximityoverride) · [`NetworkCloseTransitionMatchmaking`](#networkclosetransitionmatchmaking) · [`NetworkConcealEntity`](#networkconcealentity) · [`NetworkConcealPlayer`](#networkconcealplayer) · [`NetworkCreateSynchronisedScene`](#networkcreatesynchronisedscene) · [`NetworkDidFindGamersSucceed`](#networkdidfindgamerssucceed) · [`NetworkDidGetGamerStatusSucceed`](#networkdidgetgamerstatussucceed) · [`NetworkDisableInvincibleFlashing`](#networkdisableinvincibleflashing) · [`NetworkDisableLeaveRemotePedBehind`](#networkdisableleaveremotepedbehind) · [`NetworkDisableProximityMigration`](#networkdisableproximitymigration) · [`NetworkDisplaynamesFromHandlesStart`](#networkdisplaynamesfromhandlesstart) · [`NetworkDoTransitionQuickmatch`](#networkdotransitionquickmatch) · [`NetworkDoTransitionQuickmatchAsync`](#networkdotransitionquickmatchasync) · [`NetworkDoTransitionQuickmatchWithGroup`](#networkdotransitionquickmatchwithgroup) · [`NetworkDoTransitionToFreemode`](#networkdotransitiontofreemode) · [`NetworkDoTransitionToGame`](#networkdotransitiontogame) · [`NetworkDoTransitionToNewFreemode`](#networkdotransitiontonewfreemode) · [`NetworkDoTransitionToNewGame`](#networkdotransitiontonewgame) · [`NetworkDoesEntityExistWithNetworkId`](#networkdoesentityexistwithnetworkid) · [`NetworkDoesNetworkIdExist`](#networkdoesnetworkidexist) · [`NetworkDoesTunableExist`](#networkdoestunableexist) · [`NetworkDoesTunableExistHash`](#networkdoestunableexisthash) · [`NetworkEndTutorialSession`](#networkendtutorialsession) · [`NetworkEntityAreaDoesExist`](#networkentityareadoesexist) · [`NetworkEntityAreaIsOccupied`](#networkentityareaisoccupied) · [`NetworkExplodeHeli`](#networkexplodeheli) · [`NetworkExplodeVehicle`](#networkexplodevehicle) · [`NetworkFadeInEntity`](#networkfadeinentity) · [`NetworkFadeOutEntity`](#networkfadeoutentity) · [`NetworkFindGamersInCrew`](#networkfindgamersincrew) · [`NetworkFindMatchedGamers`](#networkfindmatchedgamers) · [`NetworkFinishBroadcastingData`](#networkfinishbroadcastingdata) · [`NetworkForceLocalUseOfSyncedSceneCamera`](#networkforcelocaluseofsyncedscenecamera) · [`NetworkGamerHasHeadset`](#networkgamerhasheadset) · [`NetworkGamertagFromHandlePending`](#networkgamertagfromhandlepending) · [`NetworkGamertagFromHandleStart`](#networkgamertagfromhandlestart) · [`NetworkGamertagFromHandleSucceeded`](#networkgamertagfromhandlesucceeded) · [`NetworkGetActivityPlayerNum`](#networkgetactivityplayernum) · [`NetworkGetAgeGroup`](#networkgetagegroup) · [`NetworkGetAverageLatencyForPlayer`](#networkgetaveragelatencyforplayer) · [`NetworkGetAverageLatencyForPlayer_2`](#networkgetaveragelatencyforplayer_2) · [`NetworkGetAveragePacketLossForPlayer`](#networkgetaveragepacketlossforplayer) · [`NetworkGetBackgroundLoadingRecipients`](#networkgetbackgroundloadingrecipients) · [`NetworkGetContentModifierListId`](#networkgetcontentmodifierlistid) · [`NetworkGetCurrentlySelectedGamerHandleFromInviteMenu`](#networkgetcurrentlyselectedgamerhandlefrominvitemenu) · [`NetworkGetDestroyerOfEntity`](#networkgetdestroyerofentity) · [`NetworkGetDestroyerOfNetworkId`](#networkgetdestroyerofnetworkid) · [`NetworkGetDisplaynamesFromHandles`](#networkgetdisplaynamesfromhandles) · [`NetworkGetEntityFromNetworkId`](#networkgetentityfromnetworkid) · [`NetworkGetEntityIsLocal`](#networkgetentityislocal) · [`NetworkGetEntityIsNetworked`](#networkgetentityisnetworked) · [`NetworkGetEntityKillerOfPlayer`](#networkgetentitykillerofplayer) · [`NetworkGetEntityNetScriptId`](#networkgetentitynetscriptid) · [`NetworkGetFoundGamer`](#networkgetfoundgamer) · [`NetworkGetFriendCount`](#networkgetfriendcount) · [`NetworkGetFriendName`](#networkgetfriendname) · [`NetworkGetFriendNameFromIndex`](#networkgetfriendnamefromindex) · [`NetworkGetGamerStatusFromQueue`](#networkgetgamerstatusfromqueue) · [`NetworkGetGamerStatusResult`](#networkgetgamerstatusresult) · [`NetworkGetGamertagFromHandle`](#networkgetgamertagfromhandle) · [`NetworkGetGlobalMultiplayerClock`](#networkgetglobalmultiplayerclock) · [`NetworkGetHostOfScript`](#networkgethostofscript) · [`NetworkGetHostOfThisScript`](#networkgethostofthisscript) · [`NetworkGetInstanceIdOfThisScript`](#networkgetinstanceidofthisscript) · [`NetworkGetLastVelocityReceived`](#networkgetlastvelocityreceived) · [`NetworkGetLocalHandle`](#networkgetlocalhandle) · [`NetworkGetLocalSceneFromNetworkId`](#networkgetlocalscenefromnetworkid) · [`NetworkGetMaxFriends`](#networkgetmaxfriends) · [`NetworkGetMaxNumParticipants`](#networkgetmaxnumparticipants) · [`NetworkGetNetworkIdFromEntity`](#networkgetnetworkidfromentity) · [`NetworkGetNumBodyTrackers`](#networkgetnumbodytrackers) · [`NetworkGetNumConnectedPlayers`](#networkgetnumconnectedplayers) · [`NetworkGetNumFoundGamers`](#networkgetnumfoundgamers) · [`NetworkGetNumParticipants`](#networkgetnumparticipants) · [`NetworkGetNumPresenceInvites`](#networkgetnumpresenceinvites) · [`NetworkGetNumScriptParticipants`](#networkgetnumscriptparticipants) · [`NetworkGetNumUnackedForPlayer`](#networkgetnumunackedforplayer) · [`NetworkGetOldestResendCountForPlayer`](#networkgetoldestresendcountforplayer) · [`NetworkGetParticipantIndex`](#networkgetparticipantindex) · [`NetworkGetPlatformPartyMembers`](#networkgetplatformpartymembers) · [`NetworkGetPlatformPartyUnk`](#networkgetplatformpartyunk) · [`NetworkGetPlayerCoords`](#networkgetplayercoords) · [`NetworkGetPlayerFromGamerHandle`](#networkgetplayerfromgamerhandle) · [`NetworkGetPlayerIndex`](#networkgetplayerindex) · [`NetworkGetPlayerIndexFromPed`](#networkgetplayerindexfromped) · [`NetworkGetPlayerLoudness`](#networkgetplayerloudness) · [`NetworkGetPlayerOwnsWaypoint`](#networkgetplayerownswaypoint) · [`NetworkGetPlayerTutorialSessionInstance`](#networkgetplayertutorialsessioninstance) · [`NetworkGetPositionHashOfThisScript`](#networkgetpositionhashofthisscript) · [`NetworkGetPresenceInviteContentId`](#networkgetpresenceinvitecontentid) · [`NetworkGetPresenceInviteFromAdmin`](#networkgetpresenceinvitefromadmin) · [`NetworkGetPresenceInviteHandle`](#networkgetpresenceinvitehandle) · [`NetworkGetPresenceInviteId`](#networkgetpresenceinviteid) · [`NetworkGetPresenceInviteInviter`](#networkgetpresenceinviteinviter) · [`NetworkGetPresenceInviteIsTournament`](#networkgetpresenceinviteistournament) · [`NetworkGetPresenceInvitePlaylistCurrent`](#networkgetpresenceinviteplaylistcurrent) · [`NetworkGetPresenceInvitePlaylistLength`](#networkgetpresenceinviteplaylistlength) · [`NetworkGetPresenceInviteSessionId`](#networkgetpresenceinvitesessionid) · [`NetworkGetPrimaryClanDataCancel`](#networkgetprimaryclandatacancel) · [`NetworkGetPrimaryClanDataClear`](#networkgetprimaryclandataclear) · [`NetworkGetPrimaryClanDataNew`](#networkgetprimaryclandatanew) · [`NetworkGetPrimaryClanDataPending`](#networkgetprimaryclandatapending) · [`NetworkGetPrimaryClanDataStart`](#networkgetprimaryclandatastart) · [`NetworkGetPrimaryClanDataSuccess`](#networkgetprimaryclandatasuccess) · [`NetworkGetRandomInt`](#networkgetrandomint) · [`NetworkGetRandomIntRanged`](#networkgetrandomintranged) · [`NetworkGetRespawnResult`](#networkgetrespawnresult) · [`NetworkGetRespawnResultFlags`](#networkgetrespawnresultflags) · [`NetworkGetRosPrivilege_24`](#networkgetrosprivilege_24) · [`NetworkGetRosPrivilege_25`](#networkgetrosprivilege_25) · [`NetworkGetRosPrivilege_9`](#networkgetrosprivilege_9) · [`NetworkGetScriptStatus`](#networkgetscriptstatus) · [`NetworkGetTalkerProximity`](#networkgettalkerproximity) · [`NetworkGetTargetingMode`](#networkgettargetingmode) · [`NetworkGetThisScriptIsNetworkScript`](#networkgetthisscriptisnetworkscript) · [`NetworkGetTimeoutTime`](#networkgettimeouttime) · [`NetworkGetTotalNumPlayers`](#networkgettotalnumplayers) · [`NetworkGetTransitionHost`](#networkgettransitionhost) · [`NetworkGetTransitionMembers`](#networkgettransitionmembers) · [`NetworkGetTunableCloudCrc`](#networkgettunablecloudcrc) · [`NetworkGetUnreliableResendCountForPlayer`](#networkgetunreliableresendcountforplayer) · [`NetworkHandleFromFriend`](#networkhandlefromfriend) · [`NetworkHandleFromMemberId`](#networkhandlefrommemberid) · [`NetworkHandleFromPlayer`](#networkhandlefromplayer) · [`NetworkHandleFromUserId`](#networkhandlefromuserid) · [`NetworkHasAgeRestrictedProfile`](#networkhasagerestrictedprofile) · [`NetworkHasCachedPlayerHeadBlendData`](#networkhascachedplayerheadblenddata) · [`NetworkHasControlOfDoor`](#networkhascontrolofdoor) · [`NetworkHasControlOfEntity`](#networkhascontrolofentity) · [`NetworkHasControlOfNetworkId`](#networkhascontrolofnetworkid) · [`NetworkHasControlOfPickup`](#networkhascontrolofpickup) · [`NetworkHasEntityBeenRegisteredWithThisThread`](#networkhasentitybeenregisteredwiththisthread) · [`NetworkHasFollowInvite`](#networkhasfollowinvite) · [`NetworkHasGameBeenAltered`](#networkhasgamebeenaltered) · [`NetworkHasHeadset`](#networkhasheadset) · [`NetworkHasInviteBeenAcked`](#networkhasinvitebeenacked) · [`NetworkHasInvitedGamer`](#networkhasinvitedgamer) · [`NetworkHasInvitedGamerToTransition`](#networkhasinvitedgamertotransition) · [`NetworkHasPendingInvite`](#networkhaspendinginvite) · [`NetworkHasPlayerStartedTransition`](#networkhasplayerstartedtransition) · [`NetworkHasReceivedHostBroadcastData`](#networkhasreceivedhostbroadcastdata) · [`NetworkHasRosPrivilege`](#networkhasrosprivilege) · [`NetworkHasRosPrivilegeEndDate`](#networkhasrosprivilegeenddate) · [`NetworkHasSocialClubAccount`](#networkhassocialclubaccount) · [`NetworkHasSocialNetworkingSharingPriv`](#networkhassocialnetworkingsharingpriv) · [`NetworkHasTransitionInviteBeenAcked`](#networkhastransitioninvitebeenacked) · [`NetworkHasValidRosCredentials`](#networkhasvalidroscredentials) · [`NetworkHasViewGamerUserContentResult`](#networkhasviewgamerusercontentresult) · [`NetworkHashFromGamerHandle`](#networkhashfromgamerhandle) · [`NetworkHashFromPlayerHandle`](#networkhashfromplayerhandle) · [`NetworkHaveCommunicationPrivileges`](#networkhavecommunicationprivileges) · [`NetworkHaveOnlinePrivilege_2`](#networkhaveonlineprivilege_2) · [`NetworkHaveOnlinePrivileges`](#networkhaveonlineprivileges) · [`NetworkHaveRosBannedPriv`](#networkhaverosbannedpriv) · [`NetworkHaveRosCreateTicketPriv`](#networkhaveroscreateticketpriv) · [`NetworkHaveRosLeaderboardWritePriv`](#networkhaverosleaderboardwritepriv) · [`NetworkHaveRosMultiplayerPriv`](#networkhaverosmultiplayerpriv) · [`NetworkHaveRosSocialClubPriv`](#networkhaverossocialclubpriv) · [`NetworkHaveUserContentPrivileges`](#networkhaveusercontentprivileges) · [`NetworkHostTransition`](#networkhosttransition) · [`NetworkInviteGamers`](#networkinvitegamers) · [`NetworkInviteGamersToTransition`](#networkinvitegamerstotransition) · [`NetworkIsActivitySession`](#networkisactivitysession) · [`NetworkIsActivitySpectator`](#networkisactivityspectator) · [`NetworkIsActivitySpectatorFromHandle`](#networkisactivityspectatorfromhandle) · [`NetworkIsAddingFriend`](#networkisaddingfriend) · [`NetworkIsCableConnected`](#networkiscableconnected) · [`NetworkIsChattingInPlatformParty`](#networkischattinginplatformparty) · [`NetworkIsClockTimeOverridden`](#networkisclocktimeoverridden) · [`NetworkIsCloudAvailable`](#networkiscloudavailable) · [`NetworkIsCloudBackgroundScriptRequestPending`](#networkiscloudbackgroundscriptrequestpending) · [`NetworkIsConnectionEndpointRelayServer`](#networkisconnectionendpointrelayserver) · [`NetworkIsDoorNetworked`](#networkisdoornetworked) · [`NetworkIsEntityConcealed`](#networkisentityconcealed) · [`NetworkIsEntityFading`](#networkisentityfading) · [`NetworkIsFindingGamers`](#networkisfindinggamers) · [`NetworkIsFriend`](#networkisfriend) · [`NetworkIsFriendHandleOnline`](#networkisfriendhandleonline) · [`NetworkIsFriendInMultiplayer`](#networkisfriendinmultiplayer) · [`NetworkIsFriendInSameTitle`](#networkisfriendinsametitle) · [`NetworkIsFriendIndexOnline`](#networkisfriendindexonline) · [`NetworkIsFriendOnline`](#networkisfriendonline) · [`NetworkIsGameInProgress`](#networkisgameinprogress) · [`NetworkIsGamerBlockedByMe`](#networkisgamerblockedbyme) · [`NetworkIsGamerInMySession`](#networkisgamerinmysession) · [`NetworkIsGamerMutedByMe`](#networkisgamermutedbyme) · [`NetworkIsGamerTalking`](#networkisgamertalking) · [`NetworkIsGettingGamerStatus`](#networkisgettinggamerstatus) · [`NetworkIsHandleValid`](#networkishandlevalid) · [`NetworkIsHost`](#networkishost) · [`NetworkIsHostOfThisScript`](#networkishostofthisscript) · [`NetworkIsInMpCutscene`](#networkisinmpcutscene) · [`NetworkIsInParty`](#networkisinparty) · [`NetworkIsInPlatformParty`](#networkisinplatformparty) · [`NetworkIsInPlatformPartyChat`](#networkisinplatformpartychat) · [`NetworkIsInSession`](#networkisinsession) · [`NetworkIsInSpectatorMode`](#networkisinspectatormode) · [`NetworkIsInTransition`](#networkisintransition) · [`NetworkIsInTutorialSession`](#networkisintutorialsession) · [`NetworkIsInactiveProfile`](#networkisinactiveprofile) · [`NetworkIsLocalPlayerInvincible`](#networkislocalplayerinvincible) · [`NetworkIsLocalTalking`](#networkislocaltalking) · [`NetworkIsMultiplayerDisabled`](#networkismultiplayerdisabled) · [`NetworkIsNetworkIdAClone`](#networkisnetworkidaclone) · [`NetworkIsOfflineInvitePending`](#networkisofflineinvitepending) · [`NetworkIsParticipantActive`](#networkisparticipantactive) · [`NetworkIsPartyMember`](#networkispartymember) · [`NetworkIsPendingFriend`](#networkispendingfriend) · [`NetworkIsPlayerAParticipant`](#networkisplayeraparticipant) · [`NetworkIsPlayerAParticipantOnScript`](#networkisplayeraparticipantonscript) · [`NetworkIsPlayerActive`](#networkisplayeractive) · [`NetworkIsPlayerBlockedByMe`](#networkisplayerblockedbyme) · [`NetworkIsPlayerConcealed`](#networkisplayerconcealed) · [`NetworkIsPlayerConnected`](#networkisplayerconnected) · [`NetworkIsPlayerEqualToIndex`](#networkisplayerequaltoindex) · [`NetworkIsPlayerFading`](#networkisplayerfading) · [`NetworkIsPlayerInMpCutscene`](#networkisplayerinmpcutscene) · [`NetworkIsPlayerMutedByMe`](#networkisplayermutedbyme) · [`NetworkIsPlayerTalking`](#networkisplayertalking) · [`NetworkIsPsnAvailable`](#networkispsnavailable) · [`NetworkIsScriptActive`](#networkisscriptactive) · [`NetworkIsScriptActiveByHash`](#networkisscriptactivebyhash) · [`NetworkIsSessionActive`](#networkissessionactive) · [`NetworkIsSessionBusy`](#networkissessionbusy) · [`NetworkIsSessionStarted`](#networkissessionstarted) · [`NetworkIsSignedIn`](#networkissignedin) · [`NetworkIsSignedOnline`](#networkissignedonline) · [`NetworkIsTextChatActive`](#networkistextchatactive) · [`NetworkIsThisScriptMarked`](#networkisthisscriptmarked) · [`NetworkIsTransitionBusy`](#networkistransitionbusy) · [`NetworkIsTransitionClosedCrew`](#networkistransitionclosedcrew) · [`NetworkIsTransitionClosedFriends`](#networkistransitionclosedfriends) · [`NetworkIsTransitionHost`](#networkistransitionhost) · [`NetworkIsTransitionHostFromHandle`](#networkistransitionhostfromhandle) · [`NetworkIsTransitionMatchmaking`](#networkistransitionmatchmaking) · [`NetworkIsTransitionOpenToMatchmaking`](#networkistransitionopentomatchmaking) · [`NetworkIsTransitionPrivate`](#networkistransitionprivate) · [`NetworkIsTransitionSolo`](#networkistransitionsolo) · [`NetworkIsTransitionStarted`](#networkistransitionstarted) · [`NetworkIsTransitionToGame`](#networkistransitiontogame) · [`NetworkIsTransitionVisibilityLocked`](#networkistransitionvisibilitylocked) · [`NetworkIsTunableCloudRequestPending`](#networkistunablecloudrequestpending) · [`NetworkIsTutorialSessionChangePending`](#networkistutorialsessionchangepending) · [`NetworkJoinGroupActivity`](#networkjoingroupactivity) · [`NetworkJoinPreviouslyFailedSession`](#networkjoinpreviouslyfailedsession) · [`NetworkJoinPreviouslyFailedTransition`](#networkjoinpreviouslyfailedtransition) · [`NetworkJoinTransition`](#networkjointransition) · [`NetworkLaunchTransition`](#networklaunchtransition) · [`NetworkLeaveTransition`](#networkleavetransition) · [`NetworkMarkTransitionGamerAsFullyJoined`](#networkmarktransitiongamerasfullyjoined) · [`NetworkMemberIdFromGamerHandle`](#networkmemberidfromgamerhandle) · [`NetworkOpenTransitionMatchmaking`](#networkopentransitionmatchmaking) · [`NetworkOverrideChatRestrictions`](#networkoverridechatrestrictions) · [`NetworkOverrideClockMillisecondsPerGameMinute`](#networkoverrideclockmillisecondspergameminute) · [`NetworkOverrideClockTime`](#networkoverrideclocktime) · [`NetworkOverrideCoordsAndHeading`](#networkoverridecoordsandheading) · [`NetworkOverrideReceiveRestrictions`](#networkoverridereceiverestrictions) · [`NetworkOverrideReceiveRestrictionsAll`](#networkoverridereceiverestrictionsall) · [`NetworkOverrideSendRestrictions`](#networkoverridesendrestrictions) · [`NetworkOverrideSendRestrictionsAll`](#networkoverridesendrestrictionsall) · [`NetworkOverrideTeamRestrictions`](#networkoverrideteamrestrictions) · [`NetworkOverrideTransitionChat`](#networkoverridetransitionchat) · [`NetworkPedForceGameStateUpdate`](#networkpedforcegamestateupdate) · [`NetworkPlayerGetCheaterReason`](#networkplayergetcheaterreason) · [`NetworkPlayerGetName`](#networkplayergetname) · [`NetworkPlayerGetUserid`](#networkplayergetuserid) · [`NetworkPlayerHasHeadset`](#networkplayerhasheadset) · [`NetworkPlayerIndexIsCheater`](#networkplayerindexischeater) · [`NetworkPlayerIsBadsport`](#networkplayerisbadsport) · [`NetworkPlayerIsCheater`](#networkplayerischeater) · [`NetworkPlayerIsRockstarDev`](#networkplayerisrockstardev) · [`NetworkQueryRespawnResults`](#networkqueryrespawnresults) · [`NetworkQueueGamerForStatus`](#networkqueuegamerforstatus) · [`NetworkQuitMpToDesktop`](#networkquitmptodesktop) · [`NetworkRegisterEntityAsNetworked`](#networkregisterentityasnetworked) · [`NetworkRegisterHostBroadcastVariables`](#networkregisterhostbroadcastvariables) · [`NetworkRegisterPlayerBroadcastVariables`](#networkregisterplayerbroadcastvariables) · [`NetworkRegisterTunableBoolHash`](#networkregistertunableboolhash) · [`NetworkRegisterTunableFloatHash`](#networkregistertunablefloathash) · [`NetworkRegisterTunableIntHash`](#networkregistertunableinthash) · [`NetworkRemoveAllTransitionInvite`](#networkremovealltransitioninvite) · [`NetworkRemoveEntityArea`](#networkremoveentityarea) · [`NetworkRemovePresenceInvite`](#networkremovepresenceinvite) · [`NetworkRemoveTransitionInvite`](#networkremovetransitioninvite) · [`NetworkReportMyself`](#networkreportmyself) · [`NetworkRequestCloudBackgroundScripts`](#networkrequestcloudbackgroundscripts) · [`NetworkRequestCloudTunables`](#networkrequestcloudtunables) · [`NetworkRequestControlOfDoor`](#networkrequestcontrolofdoor) · [`NetworkRequestControlOfEntity`](#networkrequestcontrolofentity) · [`NetworkRequestControlOfNetworkId`](#networkrequestcontrolofnetworkid) · [`NetworkResetBodyTracker`](#networkresetbodytracker) · [`NetworkRespawnCoords`](#networkrespawncoords) · [`NetworkResurrectLocalPlayer`](#networkresurrectlocalplayer) · [`NetworkSeedRandomNumberGenerator`](#networkseedrandomnumbergenerator) · [`NetworkSendInviteViaPresence`](#networksendinviteviapresence) · [`NetworkSendPresenceTransitionInvite`](#networksendpresencetransitioninvite) · [`NetworkSendTextMessage`](#networksendtextmessage) · [`NetworkSendTransitionGamerInstruction`](#networksendtransitiongamerinstruction) · [`NetworkSessionActivityQuickmatch`](#networksessionactivityquickmatch) · [`NetworkSessionAddActiveMatchmakingGroup`](#networksessionaddactivematchmakinggroup) · [`NetworkSessionBlockJoinRequests`](#networksessionblockjoinrequests) · [`NetworkSessionCancelInvite`](#networksessioncancelinvite) · [`NetworkSessionChangeSlots`](#networksessionchangeslots) · [`NetworkSessionCrewMatchmaking`](#networksessioncrewmatchmaking) · [`NetworkSessionEnd`](#networksessionend) · [`NetworkSessionEnter`](#networksessionenter) · [`NetworkSessionForceCancelInvite`](#networksessionforcecancelinvite) · [`NetworkSessionFriendMatchmaking`](#networksessionfriendmatchmaking) · [`NetworkSessionGetInviter`](#networksessiongetinviter) · [`NetworkSessionGetKickVote`](#networksessiongetkickvote) · [`NetworkSessionGetMatchmakingGroupFree`](#networksessiongetmatchmakinggroupfree) · [`NetworkSessionGetPrivateSlots`](#networksessiongetprivateslots) · [`NetworkSessionHost`](#networksessionhost) · [`NetworkSessionHostClosed`](#networksessionhostclosed) · [`NetworkSessionHostFriendsOnly`](#networksessionhostfriendsonly) · [`NetworkSessionHostSinglePlayer`](#networksessionhostsingleplayer) · [`NetworkSessionIsClosedCrew`](#networksessionisclosedcrew) · [`NetworkSessionIsClosedFriends`](#networksessionisclosedfriends) · [`NetworkSessionIsInVoiceSession`](#networksessionisinvoicesession) · [`NetworkSessionIsPrivate`](#networksessionisprivate) · [`NetworkSessionIsSolo`](#networksessionissolo) · [`NetworkSessionIsVisible`](#networksessionisvisible) · [`NetworkSessionIsVoiceSessionBusy`](#networksessionisvoicesessionbusy) · [`NetworkSessionJoinInvite`](#networksessionjoininvite) · [`NetworkSessionKickPlayer`](#networksessionkickplayer) · [`NetworkSessionLeaveSinglePlayer`](#networksessionleavesingleplayer) · [`NetworkSessionMarkVisible`](#networksessionmarkvisible) · [`NetworkSessionSetMatchmakingGroup`](#networksessionsetmatchmakinggroup) · [`NetworkSessionSetMatchmakingGroupMax`](#networksessionsetmatchmakinggroupmax) · [`NetworkSessionSetMatchmakingMentalState`](#networksessionsetmatchmakingmentalstate) · [`NetworkSessionSetMatchmakingPropertyId`](#networksessionsetmatchmakingpropertyid) · [`NetworkSessionValidateJoin`](#networksessionvalidatejoin) · [`NetworkSessionVoiceConnectToPlayer`](#networksessionvoiceconnecttoplayer) · [`NetworkSessionVoiceHost`](#networksessionvoicehost) · [`NetworkSessionVoiceLeave`](#networksessionvoiceleave) · [`NetworkSessionVoiceRespondToRequest`](#networksessionvoicerespondtorequest) · [`NetworkSessionVoiceSetTimeout`](#networksessionvoicesettimeout) · [`NetworkSessionWasInvited`](#networksessionwasinvited) · [`NetworkSetActivityPlayerMax`](#networksetactivityplayermax) · [`NetworkSetActivitySpectator`](#networksetactivityspectator) · [`NetworkSetActivitySpectatorMax`](#networksetactivityspectatormax) · [`NetworkSetChoiceMigrateOptions`](#networksetchoicemigrateoptions) · [`NetworkSetCurrentDataManagerHandle`](#networksetcurrentdatamanagerhandle) · [`NetworkSetCurrentMissionId`](#networksetcurrentmissionid) · [`NetworkSetCurrentSpawnSetting`](#networksetcurrentspawnsetting) · [`NetworkSetCurrentlySelectedGamerHandleFromInviteMenu`](#networksetcurrentlyselectedgamerhandlefrominvitemenu) · [`NetworkSetEntityCanBlend`](#networksetentitycanblend) · [`NetworkSetEntityGhostedWithOwner`](#networksetentityghostedwithowner) · [`NetworkSetEntityInvisibleToNetwork`](#networksetentityinvisibletonetwork) · [`NetworkSetFriendlyFireOption`](#networksetfriendlyfireoption) · [`NetworkSetGamerInvitedToTransition`](#networksetgamerinvitedtotransition) · [`NetworkSetInFreeCamMode`](#networksetinfreecammode) · [`NetworkSetInMpCutscene`](#networksetinmpcutscene) · [`NetworkSetInSpectatorMode`](#networksetinspectatormode) · [`NetworkSetInSpectatorModeExtended`](#networksetinspectatormodeextended) · [`NetworkSetInviteOnCallForInviteMenu`](#networksetinviteoncallforinvitemenu) · [`NetworkSetLocalPlayerInvincibleTime`](#networksetlocalplayerinvincibletime) · [`NetworkSetLocalPlayerSyncLookAt`](#networksetlocalplayersynclookat) · [`NetworkSetMissionFinished`](#networksetmissionfinished) · [`NetworkSetNoSpectatorChat`](#networksetnospectatorchat) · [`NetworkSetObjectForceStaticBlend`](#networksetobjectforcestaticblend) · [`NetworkSetOverrideSpectatorMode`](#networksetoverridespectatormode) · [`NetworkSetPlayerIsPassive`](#networksetplayerispassive) · [`NetworkSetPropertyId`](#networksetpropertyid) · [`NetworkSetRichPresence`](#networksetrichpresence) · [`NetworkSetRichPresenceString`](#networksetrichpresencestring) · [`NetworkSetScriptReadyForEvents`](#networksetscriptreadyforevents) · [`NetworkSetTalkerProximity`](#networksettalkerproximity) · [`NetworkSetTeamOnlyChat`](#networksetteamonlychat) · [`NetworkSetThisScriptIsNetworkScript`](#networksetthisscriptisnetworkscript) · [`NetworkSetTransitionActivityId`](#networksettransitionactivityid) · [`NetworkSetTransitionCreatorHandle`](#networksettransitioncreatorhandle) · [`NetworkSetTransitionVisibilityLock`](#networksettransitionvisibilitylock) · [`NetworkSetVehicleTestDrive`](#networksetvehicletestdrive) · [`NetworkSetVehicleWheelsDestructible`](#networksetvehiclewheelsdestructible) · [`NetworkSetVoiceActive`](#networksetvoiceactive) · [`NetworkSetVoiceChannel`](#networksetvoicechannel) · [`NetworkShouldShowConnectivityTroubleshooting`](#networkshouldshowconnectivitytroubleshooting) · [`NetworkShowProfileUi`](#networkshowprofileui) · [`NetworkStartRespawnSearchForPlayer`](#networkstartrespawnsearchforplayer) · [`NetworkStartRespawnSearchInAngledAreaForPlayer`](#networkstartrespawnsearchinangledareaforplayer) · [`NetworkStartSoloTutorialSession`](#networkstartsolotutorialsession) · [`NetworkStartSynchronisedScene`](#networkstartsynchronisedscene) · [`NetworkStartUserContentPermissionsCheck`](#networkstartusercontentpermissionscheck) · [`NetworkStopSynchronisedScene`](#networkstopsynchronisedscene) · [`NetworkSuppressInvite`](#networksuppressinvite) · [`NetworkTransitionTrack`](#networktransitiontrack) · [`NetworkTryAccessTunableBoolHash`](#networktryaccesstunableboolhash) · [`NetworkUgcNav`](#networkugcnav) · [`NetworkUnregisterNetworkedEntity`](#networkunregisternetworkedentity) · [`NetworkUpdatePlayerScars`](#networkupdateplayerscars) · [`NetworkUseHighPrecisionBlending`](#networkusehighprecisionblending) · [`NetworkUseLogarithmicBlendingThisFrame`](#networkuselogarithmicblendingthisframe) · [`ObjToNet`](#objtonet) · [`OpenCommerceStore`](#opencommercestore) · [`ParticipantId`](#participantid) · [`ParticipantIdToInt`](#participantidtoint) · [`PedToNet`](#pedtonet) · [`RefreshPlayerListStats`](#refreshplayerliststats) · [`ReleaseAllCommerceItemImages`](#releaseallcommerceitemimages) · [`RemoteCheatDetected`](#remotecheatdetected) · [`RemoveAllStickyBombsFromEntity`](#removeallstickybombsfromentity) · [`RequestCommerceItemImage`](#requestcommerceitemimage) · [`ReserveNetworkLocalObjects`](#reservenetworklocalobjects) · [`ReserveNetworkLocalPeds`](#reservenetworklocalpeds) · [`ReserveNetworkLocalVehicles`](#reservenetworklocalvehicles) · [`ReserveNetworkMissionObjects`](#reservenetworkmissionobjects) · [`ReserveNetworkMissionPeds`](#reservenetworkmissionpeds) · [`ReserveNetworkMissionVehicles`](#reservenetworkmissionvehicles) · [`ResetGhostedEntityAlpha`](#resetghostedentityalpha) · [`SetBalanceAddMachine`](#setbalanceaddmachine) · [`SetBalanceAddMachines`](#setbalanceaddmachines) · [`SetEntityLocallyInvisible`](#setentitylocallyinvisible) · [`SetEntityLocallyVisible`](#setentitylocallyvisible) · [`SetEntityVisibleInCutscene`](#setentityvisibleincutscene) · [`SetGhostedEntityAlpha`](#setghostedentityalpha) · [`SetLocalPlayerAsGhost`](#setlocalplayerasghost) · [`SetLocalPlayerInvisibleLocally`](#setlocalplayerinvisiblelocally) · [`SetLocalPlayerVisibleInCutscene`](#setlocalplayervisibleincutscene) · [`SetLocalPlayerVisibleLocally`](#setlocalplayervisiblelocally) · [`SetNetworkCutsceneEntities`](#setnetworkcutsceneentities) · [`SetNetworkEnableVehiclePositionCorrection`](#setnetworkenablevehiclepositioncorrection) · [`SetNetworkIdAlwaysExistsForPlayer`](#setnetworkidalwaysexistsforplayer) · [`SetNetworkIdCanMigrate`](#setnetworkidcanmigrate) · [`SetNetworkIdExistsOnAllMachines`](#setnetworkidexistsonallmachines) · [`SetNetworkIdVisibleInCutscene`](#setnetworkidvisibleincutscene) · [`SetNetworkVehicleAsGhost`](#setnetworkvehicleasghost)

---
### ActivateDamageTrackerOnNetworkId

`ACTIVATE_DAMAGE_TRACKER_ON_NETWORK_ID` · hash `0xD45B1FFCCD52FF19` · jhash `0x95D07BA5` · **Cliente**

```lua
ActivateDamageTrackerOnNetworkId(netID, toggle)
```
```c
void ACTIVATE_DAMAGE_TRACKER_ON_NETWORK_ID(int netID, BOOL toggle);
```

**Parámetros**

- `netID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### ActivateDamageTrackerOnPlayer

`_ACTIVATE_DAMAGE_TRACKER_ON_PLAYER` · hash `0xBEC0816FF5ACBCDA` · **Cliente**

```lua
ActivateDamageTrackerOnPlayer(player, toggle)
```
```c
void _ACTIVATE_DAMAGE_TRACKER_ON_PLAYER(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBEC0816FF5ACBCDA` (`N_0xbec0816ff5acbcda`)

---
### BadSportPlayerLeftDetected

`BAD_SPORT_PLAYER_LEFT_DETECTED` · hash `0xEC5E3AF5289DCA81` · jhash `0x4C2C6B6A` · **Cliente**

```lua
local retval, networkHandle = BadSportPlayerLeftDetected(event, amountReceived)
```
```c
BOOL BAD_SPORT_PLAYER_LEFT_DETECTED(int* networkHandle, int event, int amountReceived);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `event` (`int`)
- `amountReceived` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEC5E3AF5289DCA81` (`N_0xec5e3af5289dca81`)

---
### CanRegisterMissionEntities

`CAN_REGISTER_MISSION_ENTITIES` · hash `0x69778E7564BADE6D` · jhash `0x83794008` · **Cliente**

```lua
local retval = CanRegisterMissionEntities(ped_amt, vehicle_amt, object_amt, pickup_amt)
```
```c
BOOL CAN_REGISTER_MISSION_ENTITIES(int ped_amt, int vehicle_amt, int object_amt, int pickup_amt);
```

**Parámetros**

- `ped_amt` (`int`)
- `vehicle_amt` (`int`)
- `object_amt` (`int`)
- `pickup_amt` (`int`)

**Devuelve:** `BOOL`

---
### CanRegisterMissionObjects

`CAN_REGISTER_MISSION_OBJECTS` · hash `0x800DD4721A8B008B` · jhash `0x7F85DFDE` · **Cliente**

```lua
local retval = CanRegisterMissionObjects(amount)
```
```c
BOOL CAN_REGISTER_MISSION_OBJECTS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

---
### CanRegisterMissionPeds

`CAN_REGISTER_MISSION_PEDS` · hash `0xBCBF4FEF9FA5D781` · jhash `0xCCAA5CE9` · **Cliente**

```lua
local retval = CanRegisterMissionPeds(amount)
```
```c
BOOL CAN_REGISTER_MISSION_PEDS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

---
### CanRegisterMissionPickups

`_CAN_REGISTER_MISSION_PICKUPS` · hash `0x0A49D1CB6E34AF72` · **Cliente**

```lua
local retval = CanRegisterMissionPickups(amount)
```
```c
BOOL _CAN_REGISTER_MISSION_PICKUPS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

---
### CanRegisterMissionVehicles

`CAN_REGISTER_MISSION_VEHICLES` · hash `0x7277F1F2E085EE74` · jhash `0x818B6830` · **Cliente**

```lua
local retval = CanRegisterMissionVehicles(amount)
```
```c
BOOL CAN_REGISTER_MISSION_VEHICLES(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

---
### ClearLaunchParams

`_CLEAR_LAUNCH_PARAMS` · hash `0x966DD84FB6A46017` · **Cliente**

```lua
ClearLaunchParams()
```
```c
void _CLEAR_LAUNCH_PARAMS();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

**Nombres antiguos (alias):** `0x966DD84FB6A46017` (`N_0x966dd84fb6a46017`)

---
### CloudCheckAvailability

`CLOUD_CHECK_AVAILABILITY` · hash `0x4F18196C8D38768D` · jhash `0xC38E9DB0` · **Cliente**

```lua
CloudCheckAvailability()
```
```c
void CLOUD_CHECK_AVAILABILITY();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Downloads prod.cloud.rockstargames.com/titles/gta5/[platform]/check.json
```

**Nombres antiguos (alias):** `0x4F18196C8D38768D` (`N_0x4f18196c8d38768d`), `_DOWNLOAD_CHECK` (`DownloadCheck`)

---
### CloudDeleteMemberFile

`CLOUD_DELETE_MEMBER_FILE` · hash `0xC64DED7EF0D2FE37` · jhash `0x2B7B57B3` · **Cliente**

```lua
local retval = CloudDeleteMemberFile(p0)
```
```c
int CLOUD_DELETE_MEMBER_FILE(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xC64DED7EF0D2FE37` (`N_0xc64ded7ef0d2fe37`)

---
### CloudDidRequestSucceed

`CLOUD_DID_REQUEST_SUCCEED` · hash `0x3A3D5568AF297CD5` · jhash `0x9B9AFFF1` · **Cliente**

```lua
local retval = CloudDidRequestSucceed(handle)
```
```c
BOOL CLOUD_DID_REQUEST_SUCCEED(int handle);
```

**Parámetros**

- `handle` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3A3D5568AF297CD5` (`N_0x3a3d5568af297cd5`)

---
### CloudGetAvailabilityCheckResult

`CLOUD_GET_AVAILABILITY_CHECK_RESULT` · hash `0x0B0CC10720653F3B` · jhash `0x9262744C` · **Cliente**

```lua
local retval = CloudGetAvailabilityCheckResult()
```
```c
BOOL CLOUD_GET_AVAILABILITY_CHECK_RESULT();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `NETWORK_ENABLE_MOTION_DRUGGED` (`NetworkEnableMotionDrugged`), `0x0B0CC10720653F3B` (`N_0x0b0cc10720653f3b`)

---
### CloudHasRequestCompleted

`CLOUD_HAS_REQUEST_COMPLETED` · hash `0x4C61B39930D045DA` · jhash `0xBAF52DD8` · **Cliente**

```lua
local retval = CloudHasRequestCompleted(handle)
```
```c
BOOL CLOUD_HAS_REQUEST_COMPLETED(int handle);
```

**Parámetros**

- `handle` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4C61B39930D045DA` (`N_0x4c61b39930d045da`)

---
### CloudIsCheckingAvailability

`CLOUD_IS_CHECKING_AVAILABILITY` · hash `0xC7ABAC5DE675EE3B` · jhash `0x32A4EB22` · **Cliente**

```lua
local retval = CloudIsCheckingAvailability()
```
```c
BOOL CLOUD_IS_CHECKING_AVAILABILITY();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC7ABAC5DE675EE3B` (`N_0xc7abac5de675ee3b`)

---
### ConvertPosixTime

`CONVERT_POSIX_TIME` · hash `0xAC97AF97FA68E5D5` · jhash `0xBB7CCE49` · **Cliente**

```lua
local timeStructure = ConvertPosixTime(posixTime, timeStructure)
```
```c
void CONVERT_POSIX_TIME(int posixTime, Any* timeStructure);
```

**Parámetros**

- `posixTime` (`int`)
- `timeStructure` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Takes the specified time and writes it to the structure specified in the second argument.  
struct date_time  
{ 
    alignas(8) int year;  
    alignas(8) int month;  
    alignas(8) int day;  
    alignas(8) int hour;  
    alignas(8) int minute;  
    alignas(8) int second;  
};
```

**Nombres antiguos (alias):** `_GET_DATE_AND_TIME_FROM_UNIX_EPOCH` (`GetDateAndTimeFromUnixEpoch`)

---
### FacebookDoUnkCheck

`_FACEBOOK_DO_UNK_CHECK` · hash `0xA75E2B6733DA5142` · jhash `0x11E8B5CD` · **Cliente**

```lua
local retval = FacebookDoUnkCheck()
```
```c
BOOL _FACEBOOK_DO_UNK_CHECK();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA75E2B6733DA5142` (`N_0xa75e2b6733da5142`)

---
### FacebookIsAvailable

`_FACEBOOK_IS_AVAILABLE` · hash `0x43865688AE10F0D7` · jhash `0x429AEAB3` · **Cliente**

```lua
local retval = FacebookIsAvailable()
```
```c
BOOL _FACEBOOK_IS_AVAILABLE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x43865688AE10F0D7` (`N_0x43865688ae10f0d7`)

---
### FacebookIsSendingData

`_FACEBOOK_IS_SENDING_DATA` · hash `0x62B9FEC9A11F10EF` · jhash `0x37A28C26` · **Cliente**

```lua
local retval = FacebookIsSendingData()
```
```c
BOOL _FACEBOOK_IS_SENDING_DATA();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x62B9FEC9A11F10EF` (`N_0x62b9fec9a11f10ef`)

---
### FacebookSetCreateCharacterComplete

`_FACEBOOK_SET_CREATE_CHARACTER_COMPLETE` · hash `0xDC48473142545431` · jhash `0x02DAD93F` · **Cliente**

```lua
local retval = FacebookSetCreateCharacterComplete()
```
```c
BOOL _FACEBOOK_SET_CREATE_CHARACTER_COMPLETE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDC48473142545431` (`N_0xdc48473142545431`)

---
### FacebookSetHeistComplete

`_FACEBOOK_SET_HEIST_COMPLETE` · hash `0x098AB65B9ED9A9EC` · jhash `0x30B51753` · **Cliente**

```lua
local retval = FacebookSetHeistComplete(heistName, cashEarned, xpEarned)
```
```c
BOOL _FACEBOOK_SET_HEIST_COMPLETE(char* heistName, int cashEarned, int xpEarned);
```

**Parámetros**

- `heistName` (`char*`)
- `cashEarned` (`int`)
- `xpEarned` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x098AB65B9ED9A9EC` (`N_0x098ab65b9ed9a9ec`)

---
### FacebookSetMilestoneComplete

`_FACEBOOK_SET_MILESTONE_COMPLETE` · hash `0x0AE1F1653B554AB9` · jhash `0x2D947814` · **Cliente**

```lua
local retval = FacebookSetMilestoneComplete(milestoneId)
```
```c
BOOL _FACEBOOK_SET_MILESTONE_COMPLETE(int milestoneId);
```

**Parámetros**

- `milestoneId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
milestoneId:  
0 = "percentcomplete"  
1 = "storycomplete"  
2 = "vehicles"  
3 = "properties"  
4 = "psych"  
5 = "mapreveal"  
6 = "prologue"  
```

**Nombres antiguos (alias):** `0x0AE1F1653B554AB9` (`N_0x0ae1f1653b554ab9`)

---
### FadeOutLocalPlayer

`FADE_OUT_LOCAL_PLAYER` · hash `0x416DBD4CD6ED8DD2` · jhash `0x8FA7CEBD` · **Cliente**

```lua
FadeOutLocalPlayer(p0)
```
```c
void FADE_OUT_LOCAL_PLAYER(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Hardcoded to not work in SP.  
```

---
### FilloutPmPlayerList

`FILLOUT_PM_PLAYER_LIST` · hash `0xCBBD7C4991B64809` · jhash `0xCE40F423` · **Cliente**

```lua
local retval, networkHandle = FilloutPmPlayerList(p1, p2)
```
```c
BOOL FILLOUT_PM_PLAYER_LIST(int* networkHandle, Any p1, Any p2);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### FilloutPmPlayerListWithNames

`FILLOUT_PM_PLAYER_LIST_WITH_NAMES` · hash `0x716B6DB9D1886106` · jhash `0xB8DF604E` · **Cliente**

```lua
local retval, p0, p1 = FilloutPmPlayerListWithNames(p2, p3)
```
```c
BOOL FILLOUT_PM_PLAYER_LIST_WITH_NAMES(Any* p0, Any* p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

---
### GetCloudTimeAsInt

`GET_CLOUD_TIME_AS_INT` · hash `0x9A73240B49945C76` · jhash `0xF2FDF2E0` · **Cliente**

```lua
local retval = GetCloudTimeAsInt()
```
```c
int GET_CLOUD_TIME_AS_INT();
```

**Devuelve:** `int` — An int representing the cloud time.

**Descripción oficial:**

Returns POSIX timestamp.

Renamed from `_GET_POSIX_TIME` to `GET_CLOUD_TIME_AS_INT` because of conflicting native names ([`0xDA488F299A5B164E`](CLOCK.md#getposixtime))

**Nombres antiguos (alias):** `0x9A73240B49945C76` (`N_0x9a73240b49945c76`)

---
### GetCloudTimeAsString

`_GET_CLOUD_TIME_AS_STRING` · hash `0xF12E6CD06C73D69E` · **Cliente**

```lua
local retval = GetCloudTimeAsString()
```
```c
char* _GET_CLOUD_TIME_AS_STRING();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
Same as GET_CLOUD_TIME_AS_INT but returns the value as a hex string (%I64X).
```

**Nombres antiguos (alias):** `0xF12E6CD06C73D69E` (`N_0xf12e6cd06c73d69e`)

---
### GetCommerceItemCat

`GET_COMMERCE_ITEM_CAT` · hash `0x6F44CBF56D79FAC0` · jhash `0x16E53875` · **Cliente**

```lua
local retval = GetCommerceItemCat(index, index2)
```
```c
char* GET_COMMERCE_ITEM_CAT(int index, int index2);
```

**Parámetros**

- `index` (`int`)
- `index2` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
index2 is unused
```

**Nombres antiguos (alias):** `0x6F44CBF56D79FAC0` (`N_0x6f44cbf56d79fac0`)

---
### GetCommerceItemId

`GET_COMMERCE_ITEM_ID` · hash `0x662635855957C411` · jhash `0x4ACF110C` · **Cliente**

```lua
local retval = GetCommerceItemId(index)
```
```c
char* GET_COMMERCE_ITEM_ID(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x662635855957C411` (`N_0x662635855957c411`)

---
### GetCommerceItemName

`GET_COMMERCE_ITEM_NAME` · hash `0xB4271092CA7EDF48` · jhash `0x1AA3A0D5` · **Cliente**

```lua
local retval = GetCommerceItemName(index)
```
```c
char* GET_COMMERCE_ITEM_NAME(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xB4271092CA7EDF48` (`N_0xb4271092ca7edf48`)

---
### GetCommerceItemNumCats

`GET_COMMERCE_ITEM_NUM_CATS` · hash `0x2A7776C709904AB0` · jhash `0x1CF89DA5` · **Cliente**

```lua
local retval = GetCommerceItemNumCats(index)
```
```c
int GET_COMMERCE_ITEM_NUM_CATS(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x2A7776C709904AB0` (`N_0x2a7776c709904ab0`)

---
### GetCommerceItemTexturename

`GET_COMMERCE_ITEM_TEXTURENAME` · hash `0x722F5D28B61C5EA8` · jhash `0x44A58B0A` · **Cliente**

```lua
local retval = GetCommerceItemTexturename(index)
```
```c
char* GET_COMMERCE_ITEM_TEXTURENAME(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
NativeDB Added Parameter 3: int p2
```

**Nombres antiguos (alias):** `0x722F5D28B61C5EA8` (`N_0x722f5d28b61c5ea8`)

---
### GetCommerceProductPrice

`GET_COMMERCE_PRODUCT_PRICE` · hash `0xCA94551B50B4932C` · jhash `0x37877757` · **Cliente**

```lua
local retval = GetCommerceProductPrice(index)
```
```c
char* GET_COMMERCE_PRODUCT_PRICE(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xCA94551B50B4932C` (`N_0xca94551b50b4932c`)

---
### GetMaxNumNetworkObjects

`GET_MAX_NUM_NETWORK_OBJECTS` · hash `0xC7BE335216B5EC7C` · jhash `0x8687E285` · **Cliente**

```lua
local retval = GetMaxNumNetworkObjects()
```
```c
int GET_MAX_NUM_NETWORK_OBJECTS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xC7BE335216B5EC7C` (`N_0xc7be335216b5ec7c`)

---
### GetMaxNumNetworkPeds

`GET_MAX_NUM_NETWORK_PEDS` · hash `0x0C1F7D49C39D2289` · jhash `0x744AC008` · **Cliente**

```lua
local retval = GetMaxNumNetworkPeds()
```
```c
int GET_MAX_NUM_NETWORK_PEDS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0C1F7D49C39D2289` (`N_0x0c1f7d49c39d2289`)

---
### GetMaxNumNetworkPickups

`GET_MAX_NUM_NETWORK_PICKUPS` · hash `0xA72835064DD63E4C` · jhash `0x6A036061` · **Cliente**

```lua
local retval = GetMaxNumNetworkPickups()
```
```c
int GET_MAX_NUM_NETWORK_PICKUPS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xA72835064DD63E4C` (`N_0xa72835064dd63e4c`)

---
### GetMaxNumNetworkVehicles

`GET_MAX_NUM_NETWORK_VEHICLES` · hash `0x0AFCE529F69B21FF` · jhash `0xC3A12135` · **Cliente**

```lua
local retval = GetMaxNumNetworkVehicles()
```
```c
int GET_MAX_NUM_NETWORK_VEHICLES();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0AFCE529F69B21FF` (`N_0x0afce529f69b21ff`)

---
### GetNetworkTime

`GET_NETWORK_TIME` · hash `0x7A5487FE9FAA6B48` · jhash `0x998103C2` · **Cliente**

```lua
local retval = GetNetworkTime()
```
```c
int GET_NETWORK_TIME();
```

**Devuelve:** `int` — Returns the network time this tick, if you want a tick-agnostic version use [`GetNetworkTimeAccurate`](#getnetworktimeaccurate).

**Ejemplo (lua):**

```lua
print(GetNetworkTime())
```

**Ejemplo (js):**

```js
console.log(GetNetworkTime())
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int networkTime = GetNetworkTime();
Debug.WriteLine($"{networkTime}");
```

---
### GetNetworkTimeAccurate

`GET_NETWORK_TIME_ACCURATE` · hash `0x89023FBBF9200E9F` · jhash `0x98AA48E5` · **Cliente**

```lua
local retval = GetNetworkTimeAccurate()
```
```c
int GET_NETWORK_TIME_ACCURATE();
```

**Devuelve:** `int` — Returns the network time as an integer

**Descripción oficial:**

Returns the same value as [`GetNetworkTime`](#getnetworktime) in freemode, but as opposed to `GetNetworkTime` it always gets the most recent time, instead of once per tick.

Could be used for benchmarking since it can return times in ticks.

**Nombres antiguos (alias):** `0x89023FBBF9200E9F` (`N_0x89023fbbf9200e9f`)

---
### GetNumCommerceItems

`GET_NUM_COMMERCE_ITEMS` · hash `0xF2EAC213D5EA0623` · jhash `0x965EA007` · **Cliente**

```lua
local retval = GetNumCommerceItems()
```
```c
int GET_NUM_COMMERCE_ITEMS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xF2EAC213D5EA0623` (`N_0xf2eac213d5ea0623`)

---
### GetNumCreatedMissionObjects

`GET_NUM_CREATED_MISSION_OBJECTS` · hash `0x12B6281B6C6706C0` · jhash `0x603FA104` · **Cliente**

```lua
local retval = GetNumCreatedMissionObjects(p0)
```
```c
int GET_NUM_CREATED_MISSION_OBJECTS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x12B6281B6C6706C0` (`N_0x12b6281b6c6706c0`)

---
### GetNumCreatedMissionPeds

`GET_NUM_CREATED_MISSION_PEDS` · hash `0xCB215C4B56A7FAE7` · jhash `0xD8FEC4F8` · **Cliente**

```lua
local retval = GetNumCreatedMissionPeds(p0)
```
```c
int GET_NUM_CREATED_MISSION_PEDS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xCB215C4B56A7FAE7` (`N_0xcb215c4b56a7fae7`)

---
### GetNumCreatedMissionVehicles

`GET_NUM_CREATED_MISSION_VEHICLES` · hash `0x0CD9AB83489430EA` · jhash `0x20527695` · **Cliente**

```lua
local retval = GetNumCreatedMissionVehicles(p0)
```
```c
int GET_NUM_CREATED_MISSION_VEHICLES(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0CD9AB83489430EA` (`N_0x0cd9ab83489430ea`)

---
### GetNumReservedMissionObjects

`GET_NUM_RESERVED_MISSION_OBJECTS` · hash `0xAA81B5F10BC43AC2` · jhash `0x16A80CD6` · **Cliente**

```lua
local retval = GetNumReservedMissionObjects(p0)
```
```c
int GET_NUM_RESERVED_MISSION_OBJECTS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
p0 appears to be for MP  
```

```
NativeDB Added Parameter 2: Any p1
```

---
### GetNumReservedMissionPeds

`GET_NUM_RESERVED_MISSION_PEDS` · hash `0x1F13D5AE5CB17E17` · jhash `0x6C25975C` · **Cliente**

```lua
local retval = GetNumReservedMissionPeds(p0)
```
```c
int GET_NUM_RESERVED_MISSION_PEDS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
p0 appears to be for MP  
```

```
NativeDB Added Parameter 2: Any p1
```

---
### GetNumReservedMissionVehicles

`GET_NUM_RESERVED_MISSION_VEHICLES` · hash `0xCF3A965906452031` · jhash `0xA9A308F3` · **Cliente**

```lua
local retval = GetNumReservedMissionVehicles(p0)
```
```c
int GET_NUM_RESERVED_MISSION_VEHICLES(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
p0 appears to be for MP  
```

```
NativeDB Added Parameter 2: Any p1
```

---
### GetOnlineVersion

`_GET_ONLINE_VERSION` · hash `0xFCA9373EF340AC0A` · **Cliente**

```lua
local retval = GetOnlineVersion()
```
```c
char* _GET_ONLINE_VERSION();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
Online version is defined here: update\update.rpf\common\data\version.txt
Example:
[ONLINE_VERSION_NUMBER]
1.33
_GET_ONLINE_VERSION() will return "1.33"
```

**Nombres antiguos (alias):** `_GET_GAME_VERSION` (`GetGameVersion`)

---
### GetStatusOfTextureDownload

`GET_STATUS_OF_TEXTURE_DOWNLOAD` · hash `0x8BD6C6DEA20E82C6` · jhash `0x03225BA3` · **Cliente**

```lua
local retval = GetStatusOfTextureDownload(p0)
```
```c
int GET_STATUS_OF_TEXTURE_DOWNLOAD(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
0 = succeeded
1 = pending
2 = failed
```

**Nombres antiguos (alias):** `0x8BD6C6DEA20E82C6` (`N_0x8bd6c6dea20e82c6`), `_GET_STATUS_OF_TEXTURE_DOWNLOAD` (`GetStatusOfTextureDownload`)

---
### GetTimeAsString

`GET_TIME_AS_STRING` · hash `0x9E23B1777A927DAD` · jhash `0x8218944E` · **Cliente**

```lua
local retval = GetTimeAsString(time)
```
```c
char* GET_TIME_AS_STRING(int time);
```

**Parámetros**

- `time` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `_FORMAT_TIME` (`FormatTime`)

---
### GetTimeDifference

`GET_TIME_DIFFERENCE` · hash `0xA2C6FC031D46FFF0` · jhash `0x5666A837` · **Cliente**

```lua
local retval = GetTimeDifference(timeA, timeB)
```
```c
int GET_TIME_DIFFERENCE(int timeA, int timeB);
```

**Parámetros**

- `timeA` (`int`)
- `timeB` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Subtracts the second argument from the first.  
```

---
### GetTimeOffset

`GET_TIME_OFFSET` · hash `0x017008CCDAD48503` · jhash `0x2E079AE6` · **Cliente**

```lua
local retval = GetTimeOffset(timeA, timeB)
```
```c
int GET_TIME_OFFSET(int timeA, int timeB);
```

**Parámetros**

- `timeA` (`int`)
- `timeB` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Adds the first argument to the second.  
```

---
### HasNetworkTimeStarted

`HAS_NETWORK_TIME_STARTED` · hash `0x46718ACEEDEAFC84` · jhash `0x4538C4A2` · **Cliente**

```lua
local retval = HasNetworkTimeStarted()
```
```c
BOOL HAS_NETWORK_TIME_STARTED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x46718ACEEDEAFC84` (`N_0x46718aceedeafc84`)

---
### IsCommerceDataValid

`IS_COMMERCE_DATA_VALID` · hash `0xEA14EEF5B7CD2C30` · jhash `0xEEFC8A55` · **Cliente**

```lua
local retval = IsCommerceDataValid()
```
```c
BOOL IS_COMMERCE_DATA_VALID();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEA14EEF5B7CD2C30` (`N_0xea14eef5b7cd2c30`)

---
### IsCommerceStoreOpen

`IS_COMMERCE_STORE_OPEN` · hash `0x2EAC52B4019E2782` · jhash `0x25E2DBA9` · **Cliente**

```lua
local retval = IsCommerceStoreOpen()
```
```c
BOOL IS_COMMERCE_STORE_OPEN();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2EAC52B4019E2782` (`N_0x2eac52b4019e2782`)

---
### IsDamageTrackerActiveOnNetworkId

`IS_DAMAGE_TRACKER_ACTIVE_ON_NETWORK_ID` · hash `0x6E192E33AD436366` · jhash `0x597063BA` · **Cliente**

```lua
local retval = IsDamageTrackerActiveOnNetworkId(netID)
```
```c
BOOL IS_DAMAGE_TRACKER_ACTIVE_ON_NETWORK_ID(int netID);
```

**Parámetros**

- `netID` (`int`)

**Devuelve:** `BOOL`

---
### IsDamageTrackerActiveOnPlayer

`_IS_DAMAGE_TRACKER_ACTIVE_ON_PLAYER` · hash `0xB2092A1EAA7FD45F` · **Cliente**

```lua
local retval = IsDamageTrackerActiveOnPlayer(player)
```
```c
BOOL _IS_DAMAGE_TRACKER_ACTIVE_ON_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB2092A1EAA7FD45F` (`N_0xb2092a1eaa7fd45f`)

---
### IsEntityGhostedToLocalPlayer

`_IS_ENTITY_GHOSTED_TO_LOCAL_PLAYER` · hash `0x21D04D7BC538C146` · **Cliente**

```lua
local retval = IsEntityGhostedToLocalPlayer(entity)
```
```c
BOOL _IS_ENTITY_GHOSTED_TO_LOCAL_PLAYER(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x21D04D7BC538C146` (`N_0x21d04d7bc538c146`), `_IS_ENTITY_A_GHOST` (`IsEntityAGhost`)

---
### IsNetworkIdOwnedByParticipant

`IS_NETWORK_ID_OWNED_BY_PARTICIPANT` · hash `0xA1607996431332DF` · jhash `0xEA5176C0` · **Cliente**

```lua
local retval = IsNetworkIdOwnedByParticipant(netId)
```
```c
BOOL IS_NETWORK_ID_OWNED_BY_PARTICIPANT(int netId);
```

**Parámetros**

- `netId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA1607996431332DF` (`N_0xa1607996431332df`), `_NETWORK_CAN_NETWORK_ID_BE_SEEN` (`NetworkCanNetworkIdBeSeen`)

---
### IsPlayerInCutscene

`IS_PLAYER_IN_CUTSCENE` · hash `0xE73092F4157CD126` · jhash `0xE0A619BD` · **Cliente**

```lua
local retval = IsPlayerInCutscene(player)
```
```c
BOOL IS_PLAYER_IN_CUTSCENE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsSphereVisibleToAnotherMachine

`IS_SPHERE_VISIBLE_TO_ANOTHER_MACHINE` · hash `0xD82CF8E64C8729D8` · jhash `0x23C5274E` · **Cliente**

```lua
local retval = IsSphereVisibleToAnotherMachine(p0, p1, p2, p3)
```
```c
BOOL IS_SPHERE_VISIBLE_TO_ANOTHER_MACHINE(float p0, float p1, float p2, float p3);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `BOOL`

---
### IsSphereVisibleToPlayer

`IS_SPHERE_VISIBLE_TO_PLAYER` · hash `0xDC3A310219E5DA62` · jhash `0xE9FCFB32` · **Cliente**

```lua
local retval = IsSphereVisibleToPlayer(p0, p1, p2, p3, p4)
```
```c
BOOL IS_SPHERE_VISIBLE_TO_PLAYER(Any p0, float p1, float p2, float p3, float p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `BOOL`

---
### IsStoreAvailableToUser

`IS_STORE_AVAILABLE_TO_USER` · hash `0x883D79C4071E18B3` · jhash `0xD32FA11F` · **Cliente**

```lua
local retval = IsStoreAvailableToUser()
```
```c
BOOL IS_STORE_AVAILABLE_TO_USER();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x883D79C4071E18B3` (`N_0x883d79c4071e18b3`)

---
### IsTimeEqualTo

`IS_TIME_EQUAL_TO` · hash `0xF5BC95857BD6D512` · jhash `0x8B4D1C06` · **Cliente**

```lua
local retval = IsTimeEqualTo(timeA, timeB)
```
```c
BOOL IS_TIME_EQUAL_TO(int timeA, int timeB);
```

**Parámetros**

- `timeA` (`int`)
- `timeB` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the two times are equal; otherwise returns false.  
```

**Nombres antiguos (alias):** `_ARE_INTEGERS_EQUAL` (`AreIntegersEqual`)

---
### IsTimeLessThan

`IS_TIME_LESS_THAN` · hash `0xCB2CF5148012C8D0` · jhash `0x50EF8FC6` · **Cliente**

```lua
local retval = IsTimeLessThan(timeA, timeB)
```
```c
BOOL IS_TIME_LESS_THAN(int timeA, int timeB);
```

**Parámetros**

- `timeA` (`int`)
- `timeB` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Subtracts the second argument from the first, then returns whether the result is negative.  
```

**Nombres antiguos (alias):** `_SUBTRACT_B_FROM_A_AND_CHECK_IF_NEGATIVE` (`SubtractBFromAAndCheckIfNegative`)

---
### IsTimeMoreThan

`IS_TIME_MORE_THAN` · hash `0xDE350F8651E4346C` · jhash `0xBBB6DF61` · **Cliente**

```lua
local retval = IsTimeMoreThan(timeA, timeB)
```
```c
BOOL IS_TIME_MORE_THAN(int timeA, int timeB);
```

**Parámetros**

- `timeA` (`int`)
- `timeB` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Subtracts the first argument from the second, then returns whether the result is negative.  
```

**Nombres antiguos (alias):** `_SUBTRACT_A_FROM_B_AND_CHECK_IF_NEGATIVE` (`SubtractAFromBAndCheckIfNegative`)

---
### N_0x023acab2dc9dc4a4

`0x023ACAB2DC9DC4A4` · hash `0x023ACAB2DC9DC4A4` · **Cliente**

```lua
local retval = N_0x023acab2dc9dc4a4()
```
```c
Any 0x023ACAB2DC9DC4A4();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x041c7f2a6c9894e6

`0x041C7F2A6C9894E6` · hash `0x041C7F2A6C9894E6` · **Cliente**

```lua
local retval = N_0x041c7f2a6c9894e6(p0, p1, p2)
```
```c
Any 0x041C7F2A6C9894E6(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### N_0x04918a41bc9b8157

`0x04918A41BC9B8157` · hash `0x04918A41BC9B8157` · **Cliente**

```lua
local retval = N_0x04918a41bc9b8157(p0, p1, p2)
```
```c
Any 0x04918A41BC9B8157(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### N_0x07eab372c8841d99

`0x07EAB372C8841D99` · hash `0x07EAB372C8841D99` · **Cliente**

```lua
local retval = N_0x07eab372c8841d99(p0, p1, p2)
```
```c
Any 0x07EAB372C8841D99(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### N_0x0cf6cc51aa18f0f8

`0x0CF6CC51AA18F0F8` · hash `0x0CF6CC51AA18F0F8` · **Cliente**

```lua
local retval = N_0x0cf6cc51aa18f0f8(p0, p1, p2)
```
```c
Any 0x0CF6CC51AA18F0F8(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x0d77a82dc2d0da59

`0x0D77A82DC2D0DA59` · hash `0x0D77A82DC2D0DA59` · jhash `0x0808D4CC` · **Cliente**

```lua
local p0, p1 = N_0x0d77a82dc2d0da59()
```
```c
void 0x0D77A82DC2D0DA59(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
NETWORK_SET_*
```

---
### N_0x0ede326d47cd0f3e

`0x0EDE326D47CD0F3E` · hash `0x0EDE326D47CD0F3E` · jhash `0xBEB7281A` · **Cliente**

```lua
local retval = N_0x0ede326d47cd0f3e(ped, player)
```
```c
BOOL 0x0EDE326D47CD0F3E(Ped ped, Player player);
```

**Parámetros**

- `ped` (`Ped`)
- `player` (`Player`)

**Devuelve:** `BOOL`

---
### N_0x0f1a4b45b7693b95

`0x0F1A4B45B7693B95` · hash `0x0F1A4B45B7693B95` · **Cliente**

```lua
N_0x0f1a4b45b7693b95(p0, p1)
```
```c
void 0x0F1A4B45B7693B95(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x1153fa02a659051c

`0x1153FA02A659051C` · hash `0x1153FA02A659051C` · jhash `0x57F9BC83` · **Cliente**

```lua
N_0x1153fa02a659051c()
```
```c
void 0x1153FA02A659051C();
```

**Devuelve:** `void`

---
### N_0x1171a97a3d3981b6

`0x1171A97A3D3981B6` · hash `0x1171A97A3D3981B6` · **Cliente**

```lua
local retval, p0, p1 = N_0x1171a97a3d3981b6(p2, p3)
```
```c
BOOL 0x1171A97A3D3981B6(Any* p0, Any* p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x1398582b7f72b3ed

`0x1398582B7F72B3ED` · hash `0x1398582B7F72B3ED` · **Cliente**

```lua
N_0x1398582b7f72b3ed(p0)
```
```c
void 0x1398582B7F72B3ED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x13f1fcb111b820b0

`0x13F1FCB111B820B0` · hash `0x13F1FCB111B820B0` · **Cliente**

```lua
N_0x13f1fcb111b820b0(p0)
```
```c
void 0x13F1FCB111B820B0(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_NETWORK_*
```

---
### N_0x140e6a44870a11ce

`0x140E6A44870A11CE` · hash `0x140E6A44870A11CE` · jhash `0x50507BED` · **Cliente**

```lua
N_0x140e6a44870a11ce()
```
```c
void 0x140E6A44870A11CE();
```

**Devuelve:** `void`

---
### N_0x144da052257ae7d8

`0x144DA052257AE7D8` · hash `0x144DA052257AE7D8` · **Cliente**

```lua
N_0x144da052257ae7d8(p0)
```
```c
void 0x144DA052257AE7D8(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x14922ed3e38761f0

`0x14922ED3E38761F0` · hash `0x14922ED3E38761F0` · jhash `0x8FA6EE0E` · **Cliente**

```lua
local retval = N_0x14922ed3e38761f0()
```
```c
BOOL 0x14922ED3E38761F0();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_IS_*
```

---
### N_0x155467aca0f55705

`0x155467ACA0F55705` · hash `0x155467ACA0F55705` · **Cliente**

```lua
local retval = N_0x155467aca0f55705()
```
```c
int 0x155467ACA0F55705();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Checks some commerce stuff

NativeDB Introduced: v1290
```

---
### N_0x162c23ca83ed0a62

`0x162C23CA83ED0A62` · hash `0x162C23CA83ED0A62` · jhash `0xB3BBD241` · **Cliente**

```lua
local retval = N_0x162c23ca83ed0a62(p0)
```
```c
BOOL 0x162C23CA83ED0A62(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x17c9e241111a674d

`0x17C9E241111A674D` · hash `0x17C9E241111A674D` · **Cliente**

```lua
N_0x17c9e241111a674d(p0, p1)
```
```c
void 0x17C9E241111A674D(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0x1d4dc17c38feaff0

`0x1D4DC17C38FEAFF0` · hash `0x1D4DC17C38FEAFF0` · jhash `0xED4A272F` · **Cliente**

```lua
local retval = N_0x1d4dc17c38feaff0()
```
```c
BOOL 0x1D4DC17C38FEAFF0();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_COMMERCE_*
```

---
### N_0x1d610eb0fea716d9

`0x1D610EB0FEA716D9` · hash `0x1D610EB0FEA716D9` · **Cliente**

```lua
local retval = N_0x1d610eb0fea716d9(p0)
```
```c
BOOL 0x1D610EB0FEA716D9(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

---
### N_0x1f7bc3539f9e0224

`0x1F7BC3539F9E0224` · hash `0x1F7BC3539F9E0224` · **Cliente**

```lua
N_0x1f7bc3539f9e0224()
```
```c
void 0x1F7BC3539F9E0224();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x1f8e00fb18239600

`0x1F8E00FB18239600` · hash `0x1F8E00FB18239600` · **Cliente**

```lua
N_0x1f8e00fb18239600(p0)
```
```c
void 0x1F8E00FB18239600(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x2302c0264ea58d31

`0x2302C0264EA58D31` · hash `0x2302C0264EA58D31` · jhash `0x8DCFE77D` · **Cliente**

```lua
N_0x2302c0264ea58d31()
```
```c
void 0x2302C0264EA58D31();
```

**Devuelve:** `void`

---
### N_0x24e4e51fc16305f9

`0x24E4E51FC16305F9` · hash `0x24E4E51FC16305F9` · jhash `0x742075FE` · **Cliente**

```lua
local retval = N_0x24e4e51fc16305f9()
```
```c
Any 0x24E4E51FC16305F9();
```

**Devuelve:** `Any`

---
### N_0x2555cf7da5473794

`0x2555CF7DA5473794` · hash `0x2555CF7DA5473794` · **Cliente**

```lua
N_0x2555cf7da5473794()
```
```c
void 0x2555CF7DA5473794();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing (it's a nullsub).

NativeDB Introduced: v323
```

---
### N_0x25d990f8e0e3f13c

`0x25D990F8E0E3F13C` · hash `0x25D990F8E0E3F13C` · **Cliente**

```lua
N_0x25d990f8e0e3f13c()
```
```c
void 0x25D990F8E0E3F13C();
```

**Devuelve:** `void`

---
### N_0x261e97ad7bcf3d40

`0x261E97AD7BCF3D40` · hash `0x261E97AD7BCF3D40` · jhash `0x7EF353E1` · **Cliente**

```lua
N_0x261e97ad7bcf3d40(p0)
```
```c
void 0x261E97AD7BCF3D40(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x265559da40b3f327

`0x265559DA40B3F327` · hash `0x265559DA40B3F327` · **Cliente**

```lua
N_0x265559da40b3f327(p0)
```
```c
void 0x265559DA40B3F327(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x265635150fb0d82e

`0x265635150FB0D82E` · hash `0x265635150FB0D82E` · jhash `0xA7FA70AE` · **Cliente**

```lua
N_0x265635150fb0d82e()
```
```c
void 0x265635150FB0D82E();
```

**Devuelve:** `void`

---
### N_0x26f07dd83a5f7f98

`0x26F07DD83A5F7F98` · hash `0x26F07DD83A5F7F98` · jhash `0x9A176B6E` · **Cliente**

```lua
local retval = N_0x26f07dd83a5f7f98()
```
```c
Any 0x26F07DD83A5F7F98();
```

**Devuelve:** `Any`

---
### N_0x283b6062a2c01e9b

`0x283B6062A2C01E9B` · hash `0x283B6062A2C01E9B` · jhash `0x96E28FE2` · **Cliente**

```lua
N_0x283b6062a2c01e9b()
```
```c
void 0x283B6062A2C01E9B();
```

**Devuelve:** `void`

---
### N_0x2b1c623823db0d9d

`0x2B1C623823DB0D9D` · hash `0x2B1C623823DB0D9D` · **Cliente**

```lua
local retval = N_0x2b1c623823db0d9d(p0, p1, p2, p3, p4, p5, p6)
```
```c
Any 0x2B1C623823DB0D9D(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `Any`

---
### N_0x2b51edbefc301339

`0x2B51EDBEFC301339` · hash `0x2B51EDBEFC301339` · jhash `0x8E952B12` · **Cliente**

```lua
local retval = N_0x2b51edbefc301339(p0, p1)
```
```c
BOOL 0x2B51EDBEFC301339(int p0, char* p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`char*`)

**Devuelve:** `BOOL`

---
### N_0x2bf66d2e7414f686

`0x2BF66D2E7414F686` · hash `0x2BF66D2E7414F686` · jhash `0x9156EFC0` · **Cliente**

```lua
local retval = N_0x2bf66d2e7414f686()
```
```c
Any 0x2BF66D2E7414F686();
```

**Devuelve:** `Any`

---
### N_0x2ce9d95e4051aecd

`0x2CE9D95E4051AECD` · hash `0x2CE9D95E4051AECD` · **Cliente**

```lua
N_0x2ce9d95e4051aecd(p0)
```
```c
void 0x2CE9D95E4051AECD(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x2d5dc831176d0114

`0x2D5DC831176D0114` · hash `0x2D5DC831176D0114` · jhash `0xA69AE16C` · **Cliente**

```lua
local retval = N_0x2d5dc831176d0114(p0)
```
```c
BOOL 0x2D5DC831176D0114(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x2da41ed6e1fcd7a5

`0x2DA41ED6E1FCD7A5` · hash `0x2DA41ED6E1FCD7A5` · **Cliente**

```lua
local retval, TypeOfWeapon = N_0x2da41ed6e1fcd7a5(p0, TypeOfWeapon)
```
```c
Any 0x2DA41ED6E1FCD7A5(Any p0, int* TypeOfWeapon);
```

**Parámetros**

- `p0` (`Any`)
- `TypeOfWeapon` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0x2e0bf682cc778d49

`0x2E0BF682CC778D49` · hash `0x2E0BF682CC778D49` · jhash `0xBFAA349B` · **Cliente**

```lua
local retval = N_0x2e0bf682cc778d49(p0)
```
```c
BOOL 0x2E0BF682CC778D49(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x2e4c123d1c8a710e

`0x2E4C123D1C8A710E` · hash `0x2E4C123D1C8A710E` · **Cliente**

```lua
local retval, retPlayerIds, retNumber = N_0x2e4c123d1c8a710e(p2, p3, p4, p5, p6)
```
```c
Any 0x2E4C123D1C8A710E(int* retPlayerIds, int* retNumber, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `retPlayerIds` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `retNumber` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `Any`

---
### N_0x32ebd154cb6b8b99

`0x32EBD154CB6B8B99` · hash `0x32EBD154CB6B8B99` · **Cliente**

```lua
N_0x32ebd154cb6b8b99(p0, p1, p2)
```
```c
void 0x32EBD154CB6B8B99(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0x36391f397731595d

`0x36391F397731595D` · hash `0x36391F397731595D` · **Cliente**

```lua
local retval = N_0x36391f397731595d(p0)
```
```c
Any 0x36391F397731595D(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x367ef5e2f439b4c6

`0x367EF5E2F439B4C6` · hash `0x367EF5E2F439B4C6` · jhash `0x53C9563C` · **Cliente**

```lua
N_0x367ef5e2f439b4c6(p0)
```
```c
void 0x367EF5E2F439B4C6(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### N_0x37d5f739fd494675

`0x37D5F739FD494675` · hash `0x37D5F739FD494675` · **Cliente**

```lua
local retval = N_0x37d5f739fd494675(p0)
```
```c
int 0x37D5F739FD494675(Any p0);
```

**Parámetros**

- `p0` (`Any`): unknown.

**Devuelve:** `int` — Returns an entity handle or -1, value changes based on p0's value.

**Descripción oficial:**

I've had this return the player's ped handle sometimes, but also other random entities.

Whatever p0 is, it's at least not synced to other players.
At least not all the time, some p0 values actually output the same entity, (different handle of course, but same entity).
But another p0 value may return an entity for player x, but not for player y (it'll just return -1 even if the entity exists on both clients).

---
### N_0x3855fb5eb2c5e8b2

`0x3855FB5EB2C5E8B2` · hash `0x3855FB5EB2C5E8B2` · **Cliente**

```lua
local retval = N_0x3855fb5eb2c5e8b2(p0)
```
```c
Any 0x3855FB5EB2C5E8B2(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x38b7c51ab1edc7d8

`0x38B7C51AB1EDC7D8` · hash `0x38B7C51AB1EDC7D8` · **Cliente**

```lua
N_0x38b7c51ab1edc7d8(entity, toggle)
```
```c
void 0x38B7C51AB1EDC7D8(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### N_0x39917e1b4cb0f911

`0x39917E1B4CB0F911` · hash `0x39917E1B4CB0F911` · jhash `0xF60986FC` · **Cliente**

```lua
N_0x39917e1b4cb0f911(p0)
```
```c
void 0x39917E1B4CB0F911(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x3c5c1e2c2ff814b1

`0x3C5C1E2C2FF814B1` · hash `0x3C5C1E2C2FF814B1` · jhash `0xC9DDA85B` · **Cliente**

```lua
N_0x3c5c1e2c2ff814b1(toggle)
```
```c
void 0x3C5C1E2C2FF814B1(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets some voice chat related value.

NETWORK_SET_*
```

---
### N_0x3fa36981311fa4ff

`0x3FA36981311FA4FF` · hash `0x3FA36981311FA4FF` · jhash `0x00AE4E17` · **Cliente**

```lua
N_0x3fa36981311fa4ff(netId, state)
```
```c
void 0x3FA36981311FA4FF(int netId, BOOL state);
```

**Parámetros**

- `netId` (`int`)
- `state` (`BOOL`)

**Devuelve:** `void`

---
### N_0x3fc795691834481d

`0x3FC795691834481D` · hash `0x3FC795691834481D` · **Cliente**

```lua
N_0x3fc795691834481d(p0, p1)
```
```c
void 0x3FC795691834481D(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

nullsub, doesn't do anything

```
NativeDB Introduced: v1868
```

---
### N_0x4237e822315d8ba9

`0x4237E822315D8BA9` · hash `0x4237E822315D8BA9` · **Cliente**

```lua
local retval = N_0x4237e822315d8ba9()
```
```c
BOOL 0x4237E822315D8BA9();
```

**Devuelve:** `BOOL`

---
### N_0x4348bfda56023a2f

`0x4348BFDA56023A2F` · hash `0x4348BFDA56023A2F` · **Cliente**

```lua
local retval = N_0x4348bfda56023a2f(p0, p1)
```
```c
Any 0x4348BFDA56023A2F(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0x444c4525ece0a4b9

`0x444C4525ECE0A4B9` · hash `0x444C4525ECE0A4B9` · jhash `0xCC7DCE24` · **Cliente**

```lua
N_0x444c4525ece0a4b9()
```
```c
void 0x444C4525ECE0A4B9();
```

**Devuelve:** `void`

**Descripción oficial:**

```
related to: 
NETWORK_BAIL  
NETWORK_BAIL_TRANSITION  
NETWORK_JOIN_GROUP_ACTIVITY  
NETWORK_JOIN_TRANSITION  
NETWORK_LAUNCH_TRANSITION  
NETWORK_SESSION_HOST  
NETWORK_SESSION_HOST_CLOSED  
NETWORK_SESSION_HOST_FRIENDS_ONLY  
NETWORK_SESSION_HOST_SINGLE_PLAYER  
NETWORK_SESSION_VOICE_LEAVE  
```

---
### N_0x45e816772e93a9db

`0x45E816772E93A9DB` · hash `0x45E816772E93A9DB` · jhash `0x8E664EFD` · **Cliente**

```lua
local retval = N_0x45e816772e93a9db()
```
```c
Any 0x45E816772E93A9DB();
```

**Devuelve:** `Any`

---
### N_0x4811bbac21c5fcd5

`0x4811BBAC21C5FCD5` · hash `0x4811BBAC21C5FCD5` · jhash `0xE5961511` · **Cliente**

```lua
N_0x4811bbac21c5fcd5(p0)
```
```c
void 0x4811BBAC21C5FCD5(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x4a9fde3a5a6d0437

`0x4A9FDE3A5A6D0437` · hash `0x4A9FDE3A5A6D0437` · jhash `0x18F03AFD` · **Cliente**

```lua
N_0x4a9fde3a5a6d0437(toggle)
```
```c
void 0x4A9FDE3A5A6D0437(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x4ad490ae1536933b

`0x4AD490AE1536933B` · hash `0x4AD490AE1536933B` · **Cliente**

```lua
local retval = N_0x4ad490ae1536933b(p0, p1)
```
```c
Any 0x4AD490AE1536933B(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0x4c2a9fdc22377075

`0x4C2A9FDC22377075` · hash `0x4C2A9FDC22377075` · **Cliente**

```lua
N_0x4c2a9fdc22377075()
```
```c
void 0x4C2A9FDC22377075();
```

**Devuelve:** `void`

---
### N_0x4c9034162368e206

`0x4C9034162368E206` · hash `0x4C9034162368E206` · **Cliente**

```lua
local retval = N_0x4c9034162368e206()
```
```c
Any 0x4C9034162368E206();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0x4d02279c83be69fe

`0x4D02279C83BE69FE` · hash `0x4D02279C83BE69FE` · jhash `0xA7F3F82B` · **Cliente**

```lua
local retval = N_0x4d02279c83be69fe()
```
```c
Any 0x4D02279C83BE69FE();
```

**Devuelve:** `Any`

---
### N_0x4df7cfff471a7fb1

`0x4DF7CFFF471A7FB1` · hash `0x4DF7CFFF471A7FB1` · jhash `0xCB1CD6D3` · **Cliente**

```lua
local retval = N_0x4df7cfff471a7fb1(p0)
```
```c
BOOL 0x4DF7CFFF471A7FB1(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x5324a0e3e4ce3570

`0x5324A0E3E4CE3570` · hash `0x5324A0E3E4CE3570` · jhash `0x87D1E6BD` · **Cliente**

```lua
local retval, p2, p3 = N_0x5324a0e3e4ce3570(p0, p1)
```
```c
BOOL 0x5324A0E3E4CE3570(Any p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0x53c10c8bd774f2c9

`0x53C10C8BD774F2C9` · hash `0x53C10C8BD774F2C9` · **Cliente**

```lua
local retval = N_0x53c10c8bd774f2c9()
```
```c
Any 0x53C10C8BD774F2C9();
```

**Devuelve:** `Any`

---
### N_0x5539c3ebf104a53a

`0x5539C3EBF104A53A` · hash `0x5539C3EBF104A53A` · jhash `0xAE396263` · **Cliente**

```lua
N_0x5539c3ebf104a53a(p0)
```
```c
void 0x5539C3EBF104A53A(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x559ebf901a8c68e0

`0x559EBF901A8C68E0` · hash `0x559EBF901A8C68E0` · **Cliente**

```lua
local retval, gamerHandle = N_0x559ebf901a8c68e0(gamerHandle)
```
```c
BOOL 0x559EBF901A8C68E0(Any* gamerHandle);
```

**Parámetros**

- `gamerHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
_NETWORK_CAN_VIEW_* - _NETWORK_CAN_SESSION*

NETWORK_CAN_PLAY_GAMER_USER_CONTENT?
```

```
NativeDB Introduced: v2699
```

---
### N_0x560b423d73015e77

`0x560B423D73015E77` · hash `0x560B423D73015E77` · **Cliente**

```lua
local retval = N_0x560b423d73015e77(p0)
```
```c
Any 0x560B423D73015E77(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x584770794d758c18

`0x584770794D758C18` · hash `0x584770794D758C18` · **Cliente**

```lua
local retval, p1 = N_0x584770794d758c18(p0, p1)
```
```c
BOOL 0x584770794D758C18(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x59328eb08c5ceb2b

`0x59328EB08C5CEB2B` · hash `0x59328EB08C5CEB2B` · jhash `0x70F6D3AD` · **Cliente**

```lua
local retval = N_0x59328eb08c5ceb2b()
```
```c
BOOL 0x59328EB08C5CEB2B();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

---
### N_0x59d421683d31835a

`0x59D421683D31835A` · hash `0x59D421683D31835A` · **Cliente**

```lua
N_0x59d421683d31835a(p0)
```
```c
void 0x59D421683D31835A(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x5a34cd9c3c5bec44

`0x5A34CD9C3C5BEC44` · hash `0x5A34CD9C3C5BEC44` · jhash `0x346B506C` · **Cliente**

```lua
local retval = N_0x5a34cd9c3c5bec44(p0)
```
```c
BOOL 0x5A34CD9C3C5BEC44(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x5c497525f803486b

`0x5C497525F803486B` · hash `0x5C497525F803486B` · **Cliente**

```lua
N_0x5c497525f803486b()
```
```c
void 0x5C497525F803486B();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x5e3aa4ca2b6fb0ee

`0x5E3AA4CA2B6FB0EE` · hash `0x5E3AA4CA2B6FB0EE` · jhash `0x7BBEA8CF` · **Cliente**

```lua
N_0x5e3aa4ca2b6fb0ee(p0)
```
```c
void 0x5E3AA4CA2B6FB0EE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x5ecd378ee64450ab

`0x5ECD378EE64450AB` · hash `0x5ECD378EE64450AB` · **Cliente**

```lua
N_0x5ecd378ee64450ab(p0)
```
```c
void 0x5ECD378EE64450AB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x600f8cb31c7aab6e

`0x600F8CB31C7AAB6E` · hash `0x600F8CB31C7AAB6E` · jhash `0x959E43A3` · **Cliente**

```lua
N_0x600f8cb31c7aab6e(p0)
```
```c
void 0x600F8CB31C7AAB6E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x60edd13eb3ac1ff3

`0x60EDD13EB3AC1FF3` · hash `0x60EDD13EB3AC1FF3` · jhash `0x4DEBC227` · **Cliente**

```lua
local retval = N_0x60edd13eb3ac1ff3()
```
```c
BOOL 0x60EDD13EB3AC1FF3();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if profile setting 901 is set to true and sets it to false.

NETWORK_C*
```

---
### N_0x617f49c2668e6155

`0x617F49C2668E6155` · hash `0x617F49C2668E6155` · **Cliente**

```lua
local retval = N_0x617f49c2668e6155()
```
```c
int 0x617F49C2668E6155();
```

**Devuelve:** `int`

**Descripción oficial:**

```
NETWORK_GET_NUM_*
```

---
### N_0x63b406d7884bfa95

`0x63B406D7884BFA95` · hash `0x63B406D7884BFA95` · jhash `0xF79FFF3C` · **Cliente**

```lua
local retval = N_0x63b406d7884bfa95()
```
```c
Any 0x63B406D7884BFA95();
```

**Devuelve:** `Any`

---
### N_0x64d779659bc37b19

`0x64D779659BC37B19` · hash `0x64D779659BC37B19` · **Cliente**

```lua
local retval = N_0x64d779659bc37b19(entity)
```
```c
Vector3 0x64D779659BC37B19(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
NETWORK_GET_*
```

---
### N_0x64e5c4cc82847b73

`0x64E5C4CC82847B73` · hash `0x64E5C4CC82847B73` · **Cliente**

```lua
local retval = N_0x64e5c4cc82847b73()
```
```c
BOOL 0x64E5C4CC82847B73();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

Hardcoded to return false.

```
NativeDB Introduced: v1734
```

---
### N_0x67fc09bc554a75e5

`0x67FC09BC554A75E5` · hash `0x67FC09BC554A75E5` · **Cliente**

```lua
local retval = N_0x67fc09bc554a75e5()
```
```c
Any 0x67FC09BC554A75E5();
```

**Devuelve:** `Any` — Hard-coded to always return 0.

---
### N_0x68103e2247887242

`0x68103E2247887242` · hash `0x68103E2247887242` · jhash `0x0095DB71` · **Cliente**

```lua
N_0x68103e2247887242()
```
```c
void 0x68103E2247887242();
```

**Devuelve:** `void`

---
### N_0x692d58df40657e8c

`0x692D58DF40657E8C` · hash `0x692D58DF40657E8C` · **Cliente**

```lua
local retval, p3 = N_0x692d58df40657e8c(p0, p1, p2, p4, p5)
```
```c
BOOL 0x692D58DF40657E8C(Any p0, Any p1, Any p2, Any* p3, Any p4, BOOL p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any`)
- `p5` (`BOOL`)

**Devuelve:** `BOOL`

---
### N_0x6a5d89d7769a40d8

`0x6A5D89D7769A40D8` · hash `0x6A5D89D7769A40D8` · jhash `0x4FFEFE43` · **Cliente**

```lua
N_0x6a5d89d7769a40d8(toggle)
```
```c
void 0x6A5D89D7769A40D8(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets some voice chat related value.
NETWORK_SET_*
```

---
### N_0x6bff5f84102df80a

`0x6BFF5F84102DF80A` · hash `0x6BFF5F84102DF80A` · **Cliente**

```lua
N_0x6bff5f84102df80a(player)
```
```c
void 0x6BFF5F84102DF80A(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x6ce50e47f5543d0c

`0x6CE50E47F5543D0C` · hash `0x6CE50E47F5543D0C` · **Cliente**

```lua
N_0x6ce50e47f5543d0c()
```
```c
void 0x6CE50E47F5543D0C();
```

**Devuelve:** `void`

---
### N_0x6fb7bb3607d27fa2

`0x6FB7BB3607D27FA2` · hash `0x6FB7BB3607D27FA2` · **Cliente**

```lua
local retval = N_0x6fb7bb3607d27fa2()
```
```c
Any 0x6FB7BB3607D27FA2();
```

**Devuelve:** `Any` — Hard-coded to always return 0.

---
### N_0x6fd992c4a1c1b986

`0x6FD992C4A1C1B986` · hash `0x6FD992C4A1C1B986` · **Cliente**

```lua
N_0x6fd992c4a1c1b986()
```
```c
void 0x6FD992C4A1C1B986();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing (it's a nullsub).

NativeDB Introduced: v323
```

---
### N_0x702bc4d605522539

`0x702BC4D605522539` · hash `0x702BC4D605522539` · jhash `0x913FD7D6` · **Cliente**

```lua
N_0x702bc4d605522539(p0)
```
```c
void 0x702BC4D605522539(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x741a3d8380319a81

`0x741A3D8380319A81` · hash `0x741A3D8380319A81` · jhash `0x331D9A27` · **Cliente**

```lua
N_0x741a3d8380319a81()
```
```c
void 0x741A3D8380319A81();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Has something to do with a host request.

NETWORK_RE*
```

---
### N_0x742b58f723233ed9

`0x742B58F723233ED9` · hash `0x742B58F723233ED9` · jhash `0x5E832444` · **Cliente**

```lua
local retval = N_0x742b58f723233ed9(p0)
```
```c
Any 0x742B58F723233ED9(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x74fb3e29e6d10fa9

`0x74FB3E29E6D10FA9` · hash `0x74FB3E29E6D10FA9` · **Cliente**

```lua
local retval = N_0x74fb3e29e6d10fa9()
```
```c
int 0x74FB3E29E6D10FA9();
```

**Devuelve:** `int` — Hard-coded to always return 0.

**Descripción oficial:**

```
Hardcoded to return zero.
==== PS4 specific info ====
Returns some sort of unavailable reason:
-1 = REASON_INVALID
 0 = REASON_OTHER
 1 = REASON_SYSTEM_UPDATE
 2 = REASON_GAME_UPDATE
 3 = REASON_SIGNED_OUT
 4 = REASON_AGE
 5 = REASON_CONNECTION
=================================
```

---
### N_0x754615490a029508

`0x754615490A029508` · hash `0x754615490A029508` · **Cliente**

```lua
local retval = N_0x754615490a029508()
```
```c
int 0x754615490A029508();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Checks some commerce stuff

NativeDB Introduced: v1290
```

---
### N_0x76b3f29d3f967692

`0x76B3F29D3F967692` · hash `0x76B3F29D3F967692` · **Cliente**

```lua
N_0x76b3f29d3f967692(p0, p1)
```
```c
void 0x76B3F29D3F967692(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x77faddcbe3499df7

`0x77FADDCBE3499DF7` · hash `0x77FADDCBE3499DF7` · jhash `0x8179C48A` · **Cliente**

```lua
N_0x77faddcbe3499df7(p0)
```
```c
void 0x77FADDCBE3499DF7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x7808619f31ff22db

`0x7808619F31FF22DB` · hash `0x7808619F31FF22DB` · **Cliente**

```lua
local retval = N_0x7808619f31ff22db()
```
```c
Any 0x7808619F31FF22DB();
```

**Devuelve:** `Any` — Hard-coded to always return 1.

---
### N_0x78321bea235fd8cd

`0x78321BEA235FD8CD` · hash `0x78321BEA235FD8CD` · **Cliente**

```lua
local retval = N_0x78321bea235fd8cd(p0, p1)
```
```c
BOOL 0x78321BEA235FD8CD(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

---
### N_0x793ff272d5b365f4

`0x793FF272D5B365F4` · hash `0x793FF272D5B365F4` · jhash `0xF0211AC1` · **Cliente**

```lua
local retval = N_0x793ff272d5b365f4()
```
```c
Any 0x793FF272D5B365F4();
```

**Devuelve:** `Any`

---
### N_0x7d395ea61622e116

`0x7D395EA61622E116` · hash `0x7D395EA61622E116` · jhash `0x5C05B7E1` · **Cliente**

```lua
N_0x7d395ea61622e116(p0)
```
```c
void 0x7D395EA61622E116(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x7db53b37a2f211a0

`0x7DB53B37A2F211A0` · hash `0x7DB53B37A2F211A0` · jhash `0x053BB329` · **Cliente**

```lua
local retval = N_0x7db53b37a2f211a0()
```
```c
int 0x7DB53B37A2F211A0();
```

**Devuelve:** `int`

---
### N_0x7ef7649b64d7ff10

`0x7EF7649B64D7FF10` · hash `0x7EF7649B64D7FF10` · **Cliente**

```lua
local retval = N_0x7ef7649b64d7ff10(entity)
```
```c
BOOL 0x7EF7649B64D7FF10(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

---
### N_0x7fcc39c46c3c03bd

`0x7FCC39C46C3C03BD` · hash `0x7FCC39C46C3C03BD` · **Cliente**

```lua
local retval = N_0x7fcc39c46c3c03bd(p0)
```
```c
BOOL 0x7FCC39C46C3C03BD(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

---
### N_0x83660b734994124d

`0x83660B734994124D` · hash `0x83660B734994124D` · **Cliente**

```lua
local retval, damageDealt = N_0x83660b734994124d(p0, p1, damageDealt)
```
```c
Any 0x83660B734994124D(Any p0, Any p1, int* damageDealt);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `damageDealt` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0x83fe8d7229593017

`0x83FE8D7229593017` · hash `0x83FE8D7229593017` · **Cliente**

```lua
N_0x83fe8d7229593017()
```
```c
void 0x83FE8D7229593017();
```

**Devuelve:** `void`

---
### N_0x88b588b41ff7868e

`0x88B588B41FF7868E` · hash `0x88B588B41FF7868E` · **Cliente**

```lua
local retval = N_0x88b588b41ff7868e()
```
```c
Any 0x88B588B41FF7868E();
```

**Devuelve:** `Any` — Hard-coded to always return 0.

---
### N_0x8b0c2964ba471961

`0x8B0C2964BA471961` · hash `0x8B0C2964BA471961` · **Cliente**

```lua
local retval = N_0x8b0c2964ba471961()
```
```c
Any 0x8B0C2964BA471961();
```

**Devuelve:** `Any` — Hard-coded to always return 0.

---
### N_0x8b4ffc790ca131ef

`0x8B4FFC790CA131EF` · hash `0x8B4FFC790CA131EF` · **Cliente**

```lua
local retval = N_0x8b4ffc790ca131ef(p0, p1, p2, p3)
```
```c
Any 0x8B4FFC790CA131EF(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `Any`

---
### N_0x8c8d2739ba44af0f

`0x8C8D2739BA44AF0F` · hash `0x8C8D2739BA44AF0F` · **Cliente**

```lua
local retval = N_0x8c8d2739ba44af0f(p0)
```
```c
BOOL 0x8C8D2739BA44AF0F(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x8ef52acaecc51d9c

`0x8EF52ACAECC51D9C` · hash `0x8EF52ACAECC51D9C` · **Cliente**

```lua
N_0x8ef52acaecc51d9c(toggle)
```
```c
void 0x8EF52ACAECC51D9C(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

NETWORK_SET_\*

```
NativeDB Introduced: v1734
```

---
### N_0x906ca41a4b74eca4

`0x906CA41A4B74ECA4` · hash `0x906CA41A4B74ECA4` · **Cliente**

```lua
local retval = N_0x906ca41a4b74eca4()
```
```c
Any 0x906CA41A4B74ECA4();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x94538037ee44f5cf

`0x94538037EE44F5CF` · hash `0x94538037EE44F5CF` · jhash `0x6B97075B` · **Cliente**

```lua
N_0x94538037ee44f5cf(p0)
```
```c
void 0x94538037EE44F5CF(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9465e683b12d3f6b

`0x9465E683B12D3F6B` · hash `0x9465E683B12D3F6B` · jhash `0x273C6180` · **Cliente**

```lua
N_0x9465e683b12d3f6b()
```
```c
void 0x9465E683B12D3F6B();
```

**Devuelve:** `void`

---
### N_0x95baf97c82464629

`0x95BAF97C82464629` · hash `0x95BAF97C82464629` · **Cliente**

```lua
N_0x95baf97c82464629(p0, p1)
```
```c
void 0x95BAF97C82464629(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x973d76aa760a6cb6

`0x973D76AA760A6CB6` · hash `0x973D76AA760A6CB6` · jhash `0x0532DDD2` · **Cliente**

```lua
N_0x973d76aa760a6cb6(p0)
```
```c
void 0x973D76AA760A6CB6(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9d724b400a7e8ffc

`0x9D724B400A7E8FFC` · hash `0x9D724B400A7E8FFC` · **Cliente**

```lua
N_0x9d724b400a7e8ffc(p0, p1)
```
```c
void 0x9D724B400A7E8FFC(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x9d7afcbf21c51712

`0x9D7AFCBF21C51712` · hash `0x9D7AFCBF21C51712` · jhash `0xE5219410` · **Cliente**

```lua
N_0x9d7afcbf21c51712(toggle)
```
```c
void 0x9D7AFCBF21C51712(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets some voice chat related value.

NETWORK_SET_*
```

---
### N_0x9fedf86898f100e9

`0x9FEDF86898F100E9` · hash `0x9FEDF86898F100E9` · jhash `0x798D6C27` · **Cliente**

```lua
local retval = N_0x9fedf86898f100e9()
```
```c
Any 0x9FEDF86898F100E9();
```

**Devuelve:** `Any`

---
### N_0xa0fa4ec6a05da44e

`0xA0FA4EC6A05DA44E` · hash `0xA0FA4EC6A05DA44E` · **Cliente**

```lua
local retval = N_0xa0fa4ec6a05da44e()
```
```c
Any 0xA0FA4EC6A05DA44E();
```

**Devuelve:** `Any` — Hard-coded to always return 0.

---
### N_0xa12d3a5a3753cc23

`0xA12D3A5A3753CC23` · hash `0xA12D3A5A3753CC23` · **Cliente**

```lua
local retval = N_0xa12d3a5a3753cc23()
```
```c
Any 0xA12D3A5A3753CC23();
```

**Devuelve:** `Any`

---
### N_0xa2e9c1ab8a92e8cd

`0xA2E9C1AB8A92E8CD` · hash `0xA2E9C1AB8A92E8CD` · jhash `0x8D014B23` · **Cliente**

```lua
N_0xa2e9c1ab8a92e8cd(toggle)
```
```c
void 0xA2E9C1AB8A92E8CD(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Appears to set whether a transition should be started when the session is migrating.

NETWORK_SET_*
```

---
### N_0xa306f470d1660581

`0xA306F470D1660581` · hash `0xA306F470D1660581` · **Cliente**

```lua
local retval = N_0xa306f470d1660581()
```
```c
Any 0xA306F470D1660581();
```

**Devuelve:** `Any`

---
### N_0xa6fceccf4721d679

`0xA6FCECCF4721D679` · hash `0xA6FCECCF4721D679` · **Cliente**

```lua
N_0xa6fceccf4721d679(p0)
```
```c
void 0xA6FCECCF4721D679(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0xa7862bc5ed1dfd7e

`0xA7862BC5ED1DFD7E` · hash `0xA7862BC5ED1DFD7E` · jhash `0x37F5BD93` · **Cliente**

```lua
local retval, p2, p3 = N_0xa7862bc5ed1dfd7e(p0, p1)
```
```c
BOOL 0xA7862BC5ED1DFD7E(Any p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0xa8acb6459542a8c8

`0xA8ACB6459542A8C8` · hash `0xA8ACB6459542A8C8` · **Cliente**

```lua
local retval = N_0xa8acb6459542a8c8()
```
```c
Any 0xA8ACB6459542A8C8();
```

**Devuelve:** `Any`

---
### N_0xaa5fafcd2c5f5e47

`0xAA5FAFCD2C5F5E47` · hash `0xAA5FAFCD2C5F5E47` · **Cliente**

```lua
local retval = N_0xaa5fafcd2c5f5e47()
```
```c
Vector3 0xAA5FAFCD2C5F5E47();
```

**Devuelve:** `Vector3`

**Descripción oficial:**

```
NativeDB Added Parameter 1: Entity entity
```

---
### N_0xadb57e5b663cca8b

`0xADB57E5B663CCA8B` · hash `0xADB57E5B663CCA8B` · jhash `0x92268BB5` · **Cliente**

```lua
local p1, p2 = N_0xadb57e5b663cca8b(p0)
```
```c
void 0xADB57E5B663CCA8B(Player p0, float* p1, float* p2);
```

**Parámetros**

- `p0` (`Player`)
- `p1` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
gets 2 floats from the CNetGamePlayer of p0 and stores them in p1 and p2.  
Possibly waypoint?  
```

---
### N_0xaeab987727c5a8a4

`0xAEAB987727C5A8A4` · hash `0xAEAB987727C5A8A4` · jhash `0x9FEEAA9C` · **Cliente**

```lua
local retval = N_0xaeab987727c5a8a4(p0)
```
```c
BOOL 0xAEAB987727C5A8A4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0xaedf1bc1c133d6e3

`0xAEDF1BC1C133D6E3` · hash `0xAEDF1BC1C133D6E3` · **Cliente**

```lua
N_0xaedf1bc1c133d6e3()
```
```c
void 0xAEDF1BC1C133D6E3();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing (it's a nullsub).

NativeDB Introduced: v323
```

---
### N_0xb13e88e655e5a3bc

`0xB13E88E655E5A3BC` · hash `0xB13E88E655E5A3BC` · jhash `0x36A5F2DA` · **Cliente**

```lua
N_0xb13e88e655e5a3bc()
```
```c
void 0xB13E88E655E5A3BC();
```

**Devuelve:** `void`

---
### N_0xb309ebea797e001f

`0xB309EBEA797E001F` · hash `0xB309EBEA797E001F` · jhash `0x5C0AB2A9` · **Cliente**

```lua
local retval = N_0xb309ebea797e001f(p0)
```
```c
Any 0xB309EBEA797E001F(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0xb37e4e6a2388ca7b

`0xB37E4E6A2388CA7B` · hash `0xB37E4E6A2388CA7B` · jhash `0x755A2B3E` · **Cliente**

```lua
local retval = N_0xb37e4e6a2388ca7b()
```
```c
BOOL 0xB37E4E6A2388CA7B();
```

**Devuelve:** `BOOL`

---
### N_0xb5d3453c98456528

`0xB5D3453C98456528` · hash `0xB5D3453C98456528` · **Cliente**

```lua
local retval = N_0xb5d3453c98456528()
```
```c
Any 0xB5D3453C98456528();
```

**Devuelve:** `Any`

---
### N_0xb606e6cc59664972

`0xB606E6CC59664972` · hash `0xB606E6CC59664972` · jhash `0x866D1B67` · **Cliente**

```lua
N_0xb606e6cc59664972(p0)
```
```c
void 0xB606E6CC59664972(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xb746d20b17f2a229

`0xB746D20B17F2A229` · hash `0xB746D20B17F2A229` · jhash `0x9567392B` · **Cliente**

```lua
local retval, p0, p1 = N_0xb746d20b17f2a229()
```
```c
BOOL 0xB746D20B17F2A229(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0xb9351a07a0d458b1

`0xB9351A07A0D458B1` · hash `0xB9351A07A0D458B1` · **Cliente**

```lua
local retval = N_0xb9351a07a0d458b1(p0)
```
```c
Any 0xB9351A07A0D458B1(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0xba7f0b77d80a4eb7

`0xBA7F0B77D80A4EB7` · hash `0xBA7F0B77D80A4EB7` · **Cliente**

```lua
N_0xba7f0b77d80a4eb7(p0, p1)
```
```c
void 0xBA7F0B77D80A4EB7(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xbd545d44cce70597

`0xBD545D44CCE70597` · hash `0xBD545D44CCE70597` · **Cliente**

```lua
local retval = N_0xbd545d44cce70597()
```
```c
BOOL 0xBD545D44CCE70597();
```

**Devuelve:** `BOOL` — Hard-coded to always return 1.

---
### N_0xbdb6f89c729cf388

`0xBDB6F89C729CF388` · hash `0xBDB6F89C729CF388` · jhash `0x9374523F` · **Cliente**

```lua
local retval = N_0xbdb6f89c729cf388()
```
```c
BOOL 0xBDB6F89C729CF388();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_SESSION_IS_*
```

---
### N_0xbf22e0f32968e967

`0xBF22E0F32968E967` · hash `0xBF22E0F32968E967` · jhash `0x22E03AD0` · **Cliente**

```lua
N_0xbf22e0f32968e967(player, p1)
```
```c
void 0xBF22E0F32968E967(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xc32ea7a2f6ca7557

`0xC32EA7A2F6CA7557` · hash `0xC32EA7A2F6CA7557` · jhash `0x966C90FD` · **Cliente**

```lua
local retval = N_0xc32ea7a2f6ca7557()
```
```c
Any 0xC32EA7A2F6CA7557();
```

**Devuelve:** `Any`

---
### N_0xc42dd763159f3461

`0xC42DD763159F3461` · hash `0xC42DD763159F3461` · jhash `0xFBBAC350` · **Cliente**

```lua
local retval = N_0xc42dd763159f3461()
```
```c
BOOL 0xC42DD763159F3461();
```

**Devuelve:** `BOOL`

---
### N_0xc434133d9ba52777

`0xC434133D9BA52777` · hash `0xC434133D9BA52777` · **Cliente**

```lua
local retval, TypeOfWeapon = N_0xc434133d9ba52777(p0, TypeOfWeapon)
```
```c
Any 0xC434133D9BA52777(Any p0, int* TypeOfWeapon);
```

**Parámetros**

- `p0` (`Any`)
- `TypeOfWeapon` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0xc571d0e77d8bbc29

`0xC571D0E77D8BBC29` · hash `0xC571D0E77D8BBC29` · jhash `0x4F4BB300` · **Cliente**

```lua
local retval = N_0xc571d0e77d8bbc29()
```
```c
BOOL 0xC571D0E77D8BBC29();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_IS_TRANSITION_*
```

---
### N_0xc87e740d9f3872cc

`0xC87E740D9F3872CC` · hash `0xC87E740D9F3872CC` · jhash `0xC1487110` · **Cliente**

```lua
local retval = N_0xc87e740d9f3872cc()
```
```c
Any 0xC87E740D9F3872CC();
```

**Devuelve:** `Any`

---
### N_0xca575c391fea25cc

`0xCA575C391FEA25CC` · hash `0xCA575C391FEA25CC` · jhash `0xE797A4B6` · **Cliente**

```lua
N_0xca575c391fea25cc(p0)
```
```c
void 0xCA575C391FEA25CC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xca59ccae5d01e4ce

`0xCA59CCAE5D01E4CE` · hash `0xCA59CCAE5D01E4CE` · **Cliente**

```lua
N_0xca59ccae5d01e4ce()
```
```c
void 0xCA59CCAE5D01E4CE();
```

**Devuelve:** `void`

**Descripción oficial:**

NETWORK_S\*

```
NativeDB Introduced: v1734
```

---
### N_0xcfeb46dcd7d8d5eb

`0xCFEB46DCD7D8D5EB` · hash `0xCFEB46DCD7D8D5EB` · jhash `0x1A3EA6CD` · **Cliente**

```lua
N_0xcfeb46dcd7d8d5eb(p0)
```
```c
void 0xCFEB46DCD7D8D5EB(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xd313de83394af134

`0xD313DE83394AF134` · hash `0xD313DE83394AF134` · jhash `0x3EA9D44C` · **Cliente**

```lua
local retval = N_0xd313de83394af134()
```
```c
BOOL 0xD313DE83394AF134();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_SESSION_IS_*
```

---
### N_0xd6d7478ca62b8d41

`0xD6D7478CA62B8D41` · hash `0xD6D7478CA62B8D41` · **Cliente**

```lua
N_0xd6d7478ca62b8d41(p0, p1)
```
```c
void 0xD6D7478CA62B8D41(Any p0, Any p1);
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
### N_0xd7b6c73cad419bcf

`0xD7B6C73CAD419BCF` · hash `0xD7B6C73CAD419BCF` · **Cliente**

```lua
N_0xd7b6c73cad419bcf(p0)
```
```c
void 0xD7B6C73CAD419BCF(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xdb663cc9ff3407a9

`0xDB663CC9FF3407A9` · hash `0xDB663CC9FF3407A9` · **Cliente**

```lua
local retval = N_0xdb663cc9ff3407a9(player)
```
```c
int 0xDB663CC9FF3407A9(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### N_0xe16aa70ce9beedc3

`0xE16AA70CE9BEEDC3` · hash `0xE16AA70CE9BEEDC3` · **Cliente**

```lua
local retval = N_0xe16aa70ce9beedc3(p0)
```
```c
Any 0xE16AA70CE9BEEDC3(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0xe42d626eec94e5d9

`0xE42D626EEC94E5D9` · hash `0xE42D626EEC94E5D9` · **Cliente**

```lua
local numReservedPeds, numReservedVehicles, numReservedObjects = N_0xe42d626eec94e5d9(p0, p1, p2, p3)
```
```c
void 0xE42D626EEC94E5D9(Any p0, Any p1, Any p2, Any p3, int* numReservedPeds, int* numReservedVehicles, int* numReservedObjects);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `numReservedPeds` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `numReservedVehicles` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `numReservedObjects` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xe6717e652b8c8d8a

`0xE6717E652B8C8D8A` · hash `0xE6717E652B8C8D8A` · **Cliente**

```lua
N_0xe6717e652b8c8d8a(p0, p1)
```
```c
void 0xE6717E652B8C8D8A(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xea8c0ddb10e2822a

`0xEA8C0DDB10E2822A` · hash `0xEA8C0DDB10E2822A` · **Cliente**

```lua
N_0xea8c0ddb10e2822a(p0, p1)
```
```c
void 0xEA8C0DDB10E2822A(Any p0, Any p1);
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
### N_0xebcab9e5048434f4

`0xEBCAB9E5048434F4` · hash `0xEBCAB9E5048434F4` · **Cliente**

```lua
local retval = N_0xebcab9e5048434f4()
```
```c
Any 0xEBCAB9E5048434F4();
```

**Devuelve:** `Any` — Hard-coded to always return 1.

---
### N_0xebf8284d8cadeb53

`0xEBF8284D8CADEB53` · hash `0xEBF8284D8CADEB53` · jhash `0x9773F36A` · **Cliente**

```lua
N_0xebf8284d8cadeb53()
```
```c
void 0xEBF8284D8CADEB53();
```

**Devuelve:** `void`

---
### N_0xebfa8d50addc54c4

`0xEBFA8D50ADDC54C4` · hash `0xEBFA8D50ADDC54C4` · jhash `0xF50BC67A` · **Cliente**

```lua
local retval = N_0xebfa8d50addc54c4(p0)
```
```c
BOOL 0xEBFA8D50ADDC54C4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0xf083835b70ba9bfe

`0xF083835B70BA9BFE` · hash `0xF083835B70BA9BFE` · jhash `0xC47352E7` · **Cliente**

```lua
N_0xf083835b70ba9bfe()
```
```c
void 0xF083835B70BA9BFE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NETWORK_RE*
```

---
### N_0xf287f506767cc8a9

`0xF287F506767CC8A9` · hash `0xF287F506767CC8A9` · **Cliente**

```lua
local retval = N_0xf287f506767cc8a9()
```
```c
Any 0xF287F506767CC8A9();
```

**Devuelve:** `Any`

---
### N_0xf49abc20d8552257

`0xF49ABC20D8552257` · hash `0xF49ABC20D8552257` · jhash `0x454C7B67` · **Cliente**

```lua
N_0xf49abc20d8552257(p0)
```
```c
void 0xF49ABC20D8552257(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xf6f4383b7c92f11a

`0xF6F4383B7C92F11A` · hash `0xF6F4383B7C92F11A` · **Cliente**

```lua
N_0xf6f4383b7c92f11a(p0)
```
```c
void 0xF6F4383B7C92F11A(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xf814fec6a19fd6e0

`0xF814FEC6A19FD6E0` · hash `0xF814FEC6A19FD6E0` · jhash `0x32B7A076` · **Cliente**

```lua
N_0xf814fec6a19fd6e0()
```
```c
void 0xF814FEC6A19FD6E0();
```

**Devuelve:** `void`

---
### N_0xfa2888e3833c8e96

`0xFA2888E3833C8E96` · hash `0xFA2888E3833C8E96` · jhash `0x7F70C15A` · **Cliente**

```lua
N_0xfa2888e3833c8e96()
```
```c
void 0xFA2888E3833C8E96();
```

**Devuelve:** `void`

---
### N_0xfac18e7356bd3210

`0xFAC18E7356BD3210` · hash `0xFAC18E7356BD3210` · **Cliente**

```lua
N_0xfac18e7356bd3210()
```
```c
void 0xFAC18E7356BD3210();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xfae628f1e9adb239

`0xFAE628F1E9ADB239` · hash `0xFAE628F1E9ADB239` · jhash `0xD59A822B` · **Cliente**

```lua
N_0xfae628f1e9adb239(p0, p1, p2)
```
```c
void 0xFAE628F1E9ADB239(Hash p0, int p1, Hash p2);
```

**Parámetros**

- `p0` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)
- `p2` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### N_0xfb1f9381e80fa13f

`0xFB1F9381E80FA13F` · hash `0xFB1F9381E80FA13F` · jhash `0x0679CE71` · **Cliente**

```lua
local retval, p1 = N_0xfb1f9381e80fa13f(p0, p1)
```
```c
Any 0xFB1F9381E80FA13F(int p0, Any* p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

**Descripción oficial:**

```
p0 is always 0. p1 is pointing to a global.  
```

---
### N_0xfb680d403909dc70

`0xFB680D403909DC70` · hash `0xFB680D403909DC70` · jhash `0xFFB2ADA1` · **Cliente**

```lua
N_0xfb680d403909dc70(p0, p1)
```
```c
void 0xFB680D403909DC70(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xfd75dabc0957bf33

`0xFD75DABC0957BF33` · hash `0xFD75DABC0957BF33` · jhash `0x511E6F50` · **Cliente**

```lua
N_0xfd75dabc0957bf33(p0)
```
```c
void 0xFD75DABC0957BF33(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### NetToEnt

`NET_TO_ENT` · hash `0xBFFEAB45A9A9094A` · jhash `0x5E149683` · **Cliente**

```lua
local retval = NetToEnt(netHandle)
```
```c
Entity NET_TO_ENT(int netHandle);
```

**Parámetros**

- `netHandle` (`int`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
gets the entity id of a network id  
```

---
### NetToObj

`NET_TO_OBJ` · hash `0xD8515F5FEA14CB3F` · jhash `0x27AA14D8` · **Cliente**

```lua
local retval = NetToObj(netHandle)
```
```c
Object NET_TO_OBJ(int netHandle);
```

**Parámetros**

- `netHandle` (`int`)

**Devuelve:** `Object`

**Descripción oficial:**

```
gets the object id of a network id  
```

---
### NetToPed

`NET_TO_PED` · hash `0xBDCD95FC216A8B3E` · jhash `0x87717DD4` · **Cliente**

```lua
local retval = NetToPed(netHandle)
```
```c
Ped NET_TO_PED(int netHandle);
```

**Parámetros**

- `netHandle` (`int`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
gets the ped id of a network id  
```

---
### NetToVeh

`NET_TO_VEH` · hash `0x367B936610BA360C` · jhash `0x7E02FAEA` · **Cliente**

```lua
local retval = NetToVeh(netHandle)
```
```c
Vehicle NET_TO_VEH(int netHandle);
```

**Parámetros**

- `netHandle` (`int`)

**Devuelve:** `Vehicle`

---
### NetworkAcceptInvite

`_NETWORK_ACCEPT_INVITE` · hash `0x62A0296C1BB1CEB3` · jhash `0x0907A6BF` · **Cliente**

```lua
local retval = NetworkAcceptInvite()
```
```c
BOOL _NETWORK_ACCEPT_INVITE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_RE*

Triggers a CEventNetworkInviteConfirmed event
```

**Nombres antiguos (alias):** `0x62A0296C1BB1CEB3` (`N_0x62a0296c1bb1ceb3`)

---
### NetworkAcceptPresenceInvite

`NETWORK_ACCEPT_PRESENCE_INVITE` · hash `0xFA91550DF9318B22` · jhash `0xE5DA4CED` · **Cliente**

```lua
local retval = NetworkAcceptPresenceInvite(p0)
```
```c
BOOL NETWORK_ACCEPT_PRESENCE_INVITE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkAccessTunableBool

`NETWORK_ACCESS_TUNABLE_BOOL` · hash `0xAA6A47A573ABB75A` · jhash `0x8A04E1FE` · **Cliente**

```lua
local retval = NetworkAccessTunableBool(tunableContext, tunableName)
```
```c
BOOL NETWORK_ACCESS_TUNABLE_BOOL(char* tunableContext, char* tunableName);
```

**Parámetros**

- `tunableContext` (`char*`)
- `tunableName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xAA6A47A573ABB75A` (`N_0xaa6a47a573abb75a`)

---
### NetworkAccessTunableBoolHash

`NETWORK_ACCESS_TUNABLE_BOOL_HASH` · hash `0xEA16B69D93D71A45` · jhash `0x18867C61` · **Cliente**

```lua
local retval = NetworkAccessTunableBoolHash(tunableContext, tunableName)
```
```c
BOOL NETWORK_ACCESS_TUNABLE_BOOL_HASH(Hash tunableContext, Hash tunableName);
```

**Parámetros**

- `tunableContext` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `tunableName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEA16B69D93D71A45` (`N_0xea16b69d93d71a45`), `_NETWORK_ACCESS_TUNABLE_BOOL_HASH` (`NetworkAccessTunableBoolHash`)

---
### NetworkAccessTunableFloat

`NETWORK_ACCESS_TUNABLE_FLOAT` · hash `0xE5608CA7BC163A5F` · jhash `0x41E8912A` · **Cliente**

```lua
local retval, value = NetworkAccessTunableFloat(tunableContext, tunableName, value)
```
```c
BOOL NETWORK_ACCESS_TUNABLE_FLOAT(char* tunableContext, char* tunableName, float* value);
```

**Parámetros**

- `tunableContext` (`char*`)
- `tunableName` (`char*`)
- `value` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE5608CA7BC163A5F` (`N_0xe5608ca7bc163a5f`)

---
### NetworkAccessTunableFloatHash

`NETWORK_ACCESS_TUNABLE_FLOAT_HASH` · hash `0x972BC203BBC4C4D5` · jhash `0x3972551F` · **Cliente**

```lua
local retval, value = NetworkAccessTunableFloatHash(tunableContext, tunableName, value)
```
```c
BOOL NETWORK_ACCESS_TUNABLE_FLOAT_HASH(Hash tunableContext, Hash tunableName, float* value);
```

**Parámetros**

- `tunableContext` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `tunableName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x972BC203BBC4C4D5` (`N_0x972bc203bbc4c4d5`), `_NETWORK_ACCESS_TUNABLE_FLOAT_HASH` (`NetworkAccessTunableFloatHash`)

---
### NetworkAccessTunableInt

`NETWORK_ACCESS_TUNABLE_INT` · hash `0x8BE1146DFD5D4468` · jhash `0xE4B3726A` · **Cliente**

```lua
local retval, value = NetworkAccessTunableInt(tunableContext, tunableName, value)
```
```c
BOOL NETWORK_ACCESS_TUNABLE_INT(char* tunableContext, char* tunableName, int* value);
```

**Parámetros**

- `tunableContext` (`char*`)
- `tunableName` (`char*`)
- `value` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8BE1146DFD5D4468` (`N_0x8be1146dfd5d4468`)

---
### NetworkAccessTunableIntHash

`NETWORK_ACCESS_TUNABLE_INT_HASH` · hash `0x40FCE03E50E8DBE8` · jhash `0xB2E83B75` · **Cliente**

```lua
local retval, value = NetworkAccessTunableIntHash(tunableContext, tunableName, value)
```
```c
BOOL NETWORK_ACCESS_TUNABLE_INT_HASH(Hash tunableContext, Hash tunableName, int* value);
```

**Parámetros**

- `tunableContext` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `tunableName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x40FCE03E50E8DBE8` (`N_0x40fce03e50e8dbe8`), `_NETWORK_ACCESS_TUNABLE_INT_HASH` (`NetworkAccessTunableIntHash`)

---
### NetworkActionFollowInvite

`NETWORK_ACTION_FOLLOW_INVITE` · hash `0xC88156EBB786F8D5` · jhash `0xAB969F00` · **Cliente**

```lua
local retval = NetworkActionFollowInvite()
```
```c
Any NETWORK_ACTION_FOLLOW_INVITE();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xC88156EBB786F8D5` (`N_0xc88156ebb786f8d5`)

---
### NetworkAddEntityAngledArea

`NETWORK_ADD_ENTITY_ANGLED_AREA` · hash `0x376C6375BA60293A` · jhash `0xCD69BEA1` · **Cliente**

```lua
local retval = NetworkAddEntityAngledArea(x1, y1, z1, x2, y2, z2, width)
```
```c
Any NETWORK_ADD_ENTITY_ANGLED_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float width);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area

**Devuelve:** `Any`

**Descripción oficial:**

To remove, see: [`NETWORK_REMOVE_ENTITY_AREA`](#networkremoveentityarea).

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

**Nombres antiguos (alias):** `0x376C6375BA60293A` (`N_0x376c6375ba60293a`), `_NETWORK_ADD_ENTITY_ANGLED_AREA` (`NetworkAddEntityAngledArea`)

---
### NetworkAddEntityArea

`NETWORK_ADD_ENTITY_AREA` · hash `0x494C8FB299290269` · jhash `0x51030E5B` · **Cliente**

```lua
local retval = NetworkAddEntityArea(p0, p1, p2, p3, p4, p5)
```
```c
Any NETWORK_ADD_ENTITY_AREA(float p0, float p1, float p2, float p3, float p4, float p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `Any`

---
### NetworkAddEntityDisplayedBoundaries

`NETWORK_ADD_ENTITY_DISPLAYED_BOUNDARIES` · hash `0x25B99872D588A101` · jhash `0x4C2C2B12` · **Cliente**

```lua
local retval = NetworkAddEntityDisplayedBoundaries(p0, p1, p2, p3, p4, p5)
```
```c
Any NETWORK_ADD_ENTITY_DISPLAYED_BOUNDARIES(float p0, float p1, float p2, float p3, float p4, float p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x25B99872D588A101` (`N_0x25b99872d588a101`)

---
### NetworkAddEntityToSynchronisedScene

`NETWORK_ADD_ENTITY_TO_SYNCHRONISED_SCENE` · hash `0xF2404D68CBC855FA` · jhash `0x10DD636C` · **Cliente**

```lua
NetworkAddEntityToSynchronisedScene(entity, netScene, animDict, animName, blendIn, blendOut, flag)
```
```c
void NETWORK_ADD_ENTITY_TO_SYNCHRONISED_SCENE(Entity entity, int netScene, char* animDict, char* animName, float blendIn, float blendOut, int flag);
```

**Parámetros**

- `entity` (`Entity`): Entity handle to add to the scene.
- `netScene` (`int`): Which network scene to add this entity to (Returned by [`NETWORK_CREATE_SYNCHRONISED_SCENE`](#networkcreatesynchronisedscene))
- `animDict` (`char*`): Animation dictionary to play on this entity.
- `animName` (`char*`): Animation clip from the dictionary to play on this entity.
- `blendIn` (`float`): Blend in speed of the animation. Default is `8.0`.
- `blendOut` (`float`): Blend out speed of the animation. Default is `-8.0`.
- `flag` (`int`): Synchronized scene flags. See [`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE`](#networkaddpedtosynchronisedscene) for more info.

**Devuelve:** `void`

**Descripción oficial:**

Adds an entity to a network synchronised scene.

---
### NetworkAddFollowers

`NETWORK_ADD_FOLLOWERS` · hash `0x236406F60CF216D6` · jhash `0x0EC62629` · **Cliente**

```lua
local p0 = NetworkAddFollowers(p1)
```
```c
void NETWORK_ADD_FOLLOWERS(int* p0, int p1);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
..  
```

**Nombres antiguos (alias):** `0x236406F60CF216D6` (`N_0x236406f60cf216d6`)

---
### NetworkAddFriend

`NETWORK_ADD_FRIEND` · hash `0x8E02D73914064223` · jhash `0x20E5B3EE` · **Cliente**

```lua
local retval, networkHandle = NetworkAddFriend(message)
```
```c
BOOL NETWORK_ADD_FRIEND(int* networkHandle, char* message);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `message` (`char*`)

**Devuelve:** `BOOL`

---
### NetworkAddMapEntityToSynchronisedScene

`NETWORK_ADD_MAP_ENTITY_TO_SYNCHRONISED_SCENE` · hash `0x45F35C0EDC33B03B` · **Cliente**

```lua
NetworkAddMapEntityToSynchronisedScene(netScene, modelHash, x, y, z, animDict, animName, blendInSpeed, blendOutSpeed, flags)
```
```c
void NETWORK_ADD_MAP_ENTITY_TO_SYNCHRONISED_SCENE(int netScene, Hash modelHash, float x, float y, float z, char* animDict, char* animName, float blendInSpeed, float blendOutSpeed, int flags);
```

**Parámetros**

- `netScene` (`int`): Net scene ID returned by [`NETWORK_CREATE_SYNCHRONISED_SCENE`](#networkcreatesynchronisedscene)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Model hash of the object the script should look for.
- `x` (`float`): Object X coord.
- `y` (`float`): Object Y coord.
- `z` (`float`): Object Z coord.
- `animDict` (`char*`): Anim dictionary to play on this object.
- `animName` (`char*`): Anim name to play on this object.
- `blendInSpeed` (`float`): Float representing how quickly the animation should be blended into. Default is `8.0`.
- `blendOutSpeed` (`float`): Float representing how quickly the animation should be blended out of. Default is `-8.0`
- `flags` (`int`): See [`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE`](#networkaddpedtosynchronisedscene).

**Devuelve:** `void`

**Descripción oficial:**

Adds a map entity to a network synchronized scene. This native function is utilized only once as of game build 2944 within the casino_slots script.
Please note that it's only possible to add a single map entity to synchronised scenes.

It's advisable to initially locate the object and retrieve its actual coordinates using [`GET_CLOSEST_OBJECT_OF_TYPE`](OBJECT.md#getclosestobjectoftype).

```
NativeDB Introduced: v1734
```

**Nombres antiguos (alias):** `0x45F35C0EDC33B03B` (`N_0x45f35c0edc33b03b`)

---
### NetworkAddPedToSynchronisedScene

`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE` · hash `0x742A637471BCECD9` · jhash `0xB386713E` · **Cliente**

```lua
NetworkAddPedToSynchronisedScene(ped, netScene, animDict, animClip, blendInSpeed, blendOutSpeed, syncedSceneFlags, ragdollFlags, moverBlendInDelta, ikFlags)
```
```c
void NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE(Ped ped, int netScene, char* animDict, char* animClip, float blendInSpeed, float blendOutSpeed, int syncedSceneFlags, int ragdollFlags, float moverBlendInDelta, int ikFlags);
```

**Parámetros**

- `ped` (`Ped`): Ped handle to add.
- `netScene` (`int`): Network scene handle (Returned by [`NETWORK_CREATE_SYNCHRONISED_SCENE`](#networkcreatesynchronisedscene))
- `animDict` (`char*`): Dictionary of the animation that the ped will play. Network synchronised scenes don't require the animation dictionary to be loaded, unlike [`TASK_SYNCHRONIZED_SCENE`](TASK.md#tasksynchronizedscene).
- `animClip` (`char*`): Clip name from the anim dictionary that the ped will play.
- `blendInSpeed` (`float`): Blend in speed. The lower the value, the slower the blend in speed is. Default is `8.0`.
- `blendOutSpeed` (`float`): Blend out speed. This should be the negative value of `blendInSpeed`. Default is `-8.0`.
- `syncedSceneFlags` (`int`): Synchronized scene flags bit field from the above table.
- `ragdollFlags` (`int`): Ragdoll blocking flags. Default is `0`.
- `moverBlendInDelta` (`float`): Determines the rate at which the mover blends in to the scene. Useful for ensuring a seamless entry onto a synchronized scene. Default is `1000.0`.
- `ikFlags` (`int`): Inverse kinematics flags. Default is `0`.

**Devuelve:** `void`

**Descripción oficial:**

Adds a ped to a networked synchronised scene.

Synchronized scene playback flags (Also works in other `NETWORK_ADD_*_TO_SYNCHRONISED_SCENE` natives):

| Value     |                  Name                     |                                                             Notes                                                                |
| :-------: | :---------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: |
| `0`       |  None                                     | No flag set.                                                                                                                     |
| `1`       | USE_PHYSICS                               | Allows the ped to have physics during the scene.                                                                                 |
| `2`       | TAG_SYNC_OUT                              | The task will do a tag synchronized blend out with the movement behaviour of the ped.                                            |
| `4`       | DONT_INTERRUPT                            | The scene will not be interrupted by external events.                                                                            |
| `8`       | ON_ABORT_STOP_SCENE                       | The scene will be stopped if the scripted task is aborted.                                                                       |
| `16`      | ABORT_ON_WEAPON_DAMAGE                    | The scene will be stopped if the ped is damaged by a weapon.                                                                     |
| `32`      | BLOCK_MOVER_UPDATE                        | The task will not update the mover.                                                                                              |
| `64`      | LOOP_WITHIN_SCENE                         | Animations within this scene will be looped until the scene is finished.                                                         |
| `128`     | PRESERVE_VELOCITY                         | The task will keep it's velocity when the scene is cleaned up/stopped. Do note that the `USE_PHYSICS` flag must also be present. |
| `256`     | EXPAND_PED_CAPSULE_FROM_SKELETON          | The task will apply the `ExpandPedCapsuleFromSkeleton` reset flag to the ped (See [`SET_PED_RESET_FLAG`](../cfx/servidor.md#setpedresetflag)). |
| `512`     | ACTIVATE_RAGDOLL_ON_COLLISION             | The ped will be ragdoll if it comes in contact with an object.                                                                   |
| `1024`    | HIDE_WEAPON                               | The ped's current weapon will be hidden during the scene.                                                                        |
| `2048`    | ABORT_ON_DEATH                            | The synchronised scene will be aborted if the ped dies.                                                                          |
| `4096`    | VEHICLE_ABORT_ON_LARGE_IMPACT             | If the scene is running on a vehicle, then it will be aborted if the vehicle takes a heavy collision with another vehicle.       |
| `8192`    | VEHICLE_ALLOW_PLAYER_ENTRY                | If the scene is on a vehicle, it allows players to enter it.                                                                     |
| `16384`   | PROCESS_ATTACHMENTS_ON_START              | Attachments will be processed at the start of the scene.                                                                         |
| `32768`   | NET_ON_EARLY_NON_PED_STOP_RETURN_TO_START | A non-ped entity will be returned to their starting position if the scene finishes early.                                        |
| `65536`   | SET_PED_OUT_OF_VEHICLE_AT_START           | If the ped is in a vehicle when the scene starts, it will be set out of the vehicle.                                             |
| `131072`  | NET_DISREGARD_ATTACHMENT_CHECKS           | Attachment checks will be disregarded when the scene is running.                                                                 |

These flags can be combined with the `|` operator.

---
### NetworkAddPedToSynchronisedSceneWithIk

`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE_WITH_IK` · hash `0xA5EAFE473E45C442` · **Cliente**

```lua
NetworkAddPedToSynchronisedSceneWithIk(ped, netSceneID, animDict, animClip, blendIn, blendOut, sceneFlags, ragdollFlags, moverBlendInDelta, ikFlags)
```
```c
void NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE_WITH_IK(Ped ped, int netSceneID, char* animDict, char* animClip, float blendIn, float blendOut, int sceneFlags, int ragdollFlags, float moverBlendInDelta, int ikFlags);
```

**Parámetros**

- `ped` (`Ped`): Index of the ped to add to the scene.
- `netSceneID` (`int`): Network scene ID returned by [`NETWORK_CREATE_SYNCHRONISED_SCENE`](#networkcreatesynchronisedscene).
- `animDict` (`char*`): Which anim dictionary to use on this ped.
- `animClip` (`char*`): Which clip from the anim dictionary to use on this ped.
- `blendIn` (`float`): Blend in speed of the animation. Default is `8.0`.
- `blendOut` (`float`): Blend out speed of the animation. Default is `-8.0`.
- `sceneFlags` (`int`): Synchronized scene flags. See [`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE`](#networkaddpedtosynchronisedscene).
- `ragdollFlags` (`int`): Ragdoll blocking flags. Default is 0.
- `moverBlendInDelta` (`float`): Determines the rate at which the mover blends in to the scene. Useful for ensuring a seamless entry onto a synchronized scene. Default is `1000.0`.
- `ikFlags` (`int`): Inverse kinematics flags. Default is `0`.

**Devuelve:** `void`

**Descripción oficial:**

Adds a ped to a networked synchronized scene but extends [`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE`](#networkaddpedtosynchronisedscene) to support IK flags.
There is barely any difference between this and [`NETWORK_ADD_PED_TO_SYNCHRONISED_SCENE`](#networkaddpedtosynchronisedscene).

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xA5EAFE473E45C442` (`N_0xa5eafe473e45c442`)

---
### NetworkAddSynchronisedSceneCamera

`NETWORK_ADD_SYNCHRONISED_SCENE_CAMERA` · hash `0xCF8BD3B0BD6D42D7` · jhash `0xBFFE8B5C` · **Cliente**

```lua
NetworkAddSynchronisedSceneCamera(netScene, animDict, animName)
```
```c
void NETWORK_ADD_SYNCHRONISED_SCENE_CAMERA(int netScene, char* animDict, char* animName);
```

**Parámetros**

- `netScene` (`int`)
- `animDict` (`char*`)
- `animName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCF8BD3B0BD6D42D7` (`N_0xcf8bd3b0bd6d42d7`)

---
### NetworkAllocateTunablesRegistrationDataMap

`_NETWORK_ALLOCATE_TUNABLES_REGISTRATION_DATA_MAP` · hash `0xFAFC23AEE23868DB` · **Cliente**

```lua
local retval = NetworkAllocateTunablesRegistrationDataMap()
```
```c
BOOL _NETWORK_ALLOCATE_TUNABLES_REGISTRATION_DATA_MAP();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFAFC23AEE23868DB` (`N_0xfafc23aee23868db`)

---
### NetworkAllowRemoteAttachmentModification

`NETWORK_ALLOW_REMOTE_ATTACHMENT_MODIFICATION` · hash `0x267C78C60E806B9A` · jhash `0xBB2D33D3` · **Cliente**

```lua
NetworkAllowRemoteAttachmentModification(entity, toggle)
```
```c
void NETWORK_ALLOW_REMOTE_ATTACHMENT_MODIFICATION(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`): Entity handle to allow remote attachment for.
- `toggle` (`BOOL`): true/false.

**Devuelve:** `void`

**Descripción oficial:**

Allows scripts to use attachment commands on entities (eg. [`ATTACH_ENTITY_TO_ENTITY`](ENTITY.md#attachentitytoentity)) that are not controlled by the client.

**Note:** This is only local and does not affect entities on other machines. This is used by the ferris wheel script to sync players on carts.

**Nombres antiguos (alias):** `0x267C78C60E806B9A` (`N_0x267c78c60e806b9a`), `_NETWORK_ALLOW_LOCAL_ENTITY_ATTACHMENT` (`NetworkAllowLocalEntityAttachment`)

---
### NetworkAmIBlockedByGamer

`NETWORK_AM_I_BLOCKED_BY_GAMER` · hash `0x15337C7C268A27B2` · jhash `0xD19B312C` · **Cliente**

```lua
local retval, networkHandle = NetworkAmIBlockedByGamer(networkHandle)
```
```c
BOOL NETWORK_AM_I_BLOCKED_BY_GAMER(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkAmIBlockedByPlayer

`NETWORK_AM_I_BLOCKED_BY_PLAYER` · hash `0x87F395D957D4353D` · jhash `0x953EF45E` · **Cliente**

```lua
local retval = NetworkAmIBlockedByPlayer(player)
```
```c
BOOL NETWORK_AM_I_BLOCKED_BY_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkAmIMutedByGamer

`NETWORK_AM_I_MUTED_BY_GAMER` · hash `0xDF02A2C93F1F26DA` · jhash `0x7685B333` · **Cliente**

```lua
local retval, networkHandle = NetworkAmIMutedByGamer(networkHandle)
```
```c
BOOL NETWORK_AM_I_MUTED_BY_GAMER(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkAmIMutedByPlayer

`NETWORK_AM_I_MUTED_BY_PLAYER` · hash `0x9D6981DFC91A8604` · jhash `0xE128F2B0` · **Cliente**

```lua
local retval = NetworkAmIMutedByPlayer(player)
```
```c
BOOL NETWORK_AM_I_MUTED_BY_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkApplyCachedPlayerHeadBlendData

`NETWORK_APPLY_CACHED_PLAYER_HEAD_BLEND_DATA` · hash `0x99B72C7ABDE5C910` · jhash `0x99F58A07` · **Cliente**

```lua
local retval = NetworkApplyCachedPlayerHeadBlendData(ped, player)
```
```c
BOOL NETWORK_APPLY_CACHED_PLAYER_HEAD_BLEND_DATA(Ped ped, Player player);
```

**Parámetros**

- `ped` (`Ped`)
- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x99B72C7ABDE5C910` (`N_0x99b72c7abde5c910`), `_NETWORK_COPY_PED_BLEND_DATA` (`NetworkCopyPedBlendData`)

---
### NetworkApplyPedScarData

`NETWORK_APPLY_PED_SCAR_DATA` · hash `0xE66C690248F11150` · jhash `0x4818ACD0` · **Cliente**

```lua
NetworkApplyPedScarData(ped, p1)
```
```c
void NETWORK_APPLY_PED_SCAR_DATA(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE66C690248F11150` (`N_0xe66c690248f11150`)

---
### NetworkApplyTransitionParameter

`NETWORK_APPLY_TRANSITION_PARAMETER` · hash `0x521638ADA1BA0D18` · jhash `0xCEE79711` · **Cliente**

```lua
NetworkApplyTransitionParameter(p0, p1)
```
```c
void NETWORK_APPLY_TRANSITION_PARAMETER(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x521638ADA1BA0D18` (`N_0x521638ada1ba0d18`)

---
### NetworkApplyTransitionParameterString

`NETWORK_APPLY_TRANSITION_PARAMETER_STRING` · hash `0xEBEFC2E77084F599` · jhash `0xE0C28DB5` · **Cliente**

```lua
NetworkApplyTransitionParameterString(p0, string, p2)
```
```c
void NETWORK_APPLY_TRANSITION_PARAMETER_STRING(int p0, char* string, BOOL p2);
```

**Parámetros**

- `p0` (`int`)
- `string` (`char*`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEBEFC2E77084F599` (`N_0xebefc2e77084f599`)

---
### NetworkApplyVoiceProximityOverride

`NETWORK_APPLY_VOICE_PROXIMITY_OVERRIDE` · hash `0xDBD2056652689917` · jhash `0xF1E84832` · **Cliente**

```lua
NetworkApplyVoiceProximityOverride(x, y, z)
```
```c
void NETWORK_APPLY_VOICE_PROXIMITY_OVERRIDE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `IS_NETWORK_VEHICLE_BEEN_DAMAGED_BY_ANY_OBJECT` (`IsNetworkVehicleBeenDamagedByAnyObject`)

---
### NetworkAreCutsceneEntities

`_NETWORK_ARE_CUTSCENE_ENTITIES` · hash `0x66D6A5E9C511214A` · **Cliente**

```lua
local retval = NetworkAreCutsceneEntities()
```
```c
BOOL _NETWORK_ARE_CUTSCENE_ENTITIES();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Getter for SET_NETWORK_CUTSCENE_ENTITIES.
```

```
NativeDB Introduced: v2699
```

---
### NetworkAreHandlesTheSame

`NETWORK_ARE_HANDLES_THE_SAME` · hash `0x57DBA049E110F217` · jhash `0x45975AE3` · **Cliente**

```lua
local retval, netHandle1, netHandle2 = NetworkAreHandlesTheSame()
```
```c
BOOL NETWORK_ARE_HANDLES_THE_SAME(int* netHandle1, int* netHandle2);
```

**Parámetros**

- `netHandle1` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `netHandle2` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### NetworkAreSocialClubPoliciesCurrent

`NETWORK_ARE_SOCIAL_CLUB_POLICIES_CURRENT` · hash `0xBA9775570DB788CF` · jhash `0x358D1D77` · **Cliente**

```lua
local retval = NetworkAreSocialClubPoliciesCurrent()
```
```c
BOOL NETWORK_ARE_SOCIAL_CLUB_POLICIES_CURRENT();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBA9775570DB788CF` (`N_0xba9775570db788cf`)

---
### NetworkAreTransitionDetailsValid

`NETWORK_ARE_TRANSITION_DETAILS_VALID` · hash `0x2615AA2A695930C1` · jhash `0xCDEBCCE7` · **Cliente**

```lua
local retval = NetworkAreTransitionDetailsValid(p0)
```
```c
BOOL NETWORK_ARE_TRANSITION_DETAILS_VALID(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2615AA2A695930C1` (`N_0x2615aa2a695930c1`)

---
### NetworkAttachSynchronisedSceneToEntity

`NETWORK_ATTACH_SYNCHRONISED_SCENE_TO_ENTITY` · hash `0x478DCBD2A98B705A` · jhash `0x3FE5B222` · **Cliente**

```lua
NetworkAttachSynchronisedSceneToEntity(netScene, entity, bone)
```
```c
void NETWORK_ATTACH_SYNCHRONISED_SCENE_TO_ENTITY(int netScene, Entity entity, int bone);
```

**Parámetros**

- `netScene` (`int`)
- `entity` (`Entity`)
- `bone` (`int`)

**Devuelve:** `void`

---
### NetworkBail

`NETWORK_BAIL` · hash `0x95914459A87EBA28` · jhash `0x87D79A04` · **Cliente**

```lua
NetworkBail()
```
```c
void NETWORK_BAIL();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
NativeDB Added Parameter 2: int p1
NativeDB Added Parameter 3: int p2
```

---
### NetworkBailTransition

`NETWORK_BAIL_TRANSITION` · hash `0xEAA572036990CD1B` · jhash `0xB59D74CA` · **Cliente**

```lua
NetworkBailTransition()
```
```c
void NETWORK_BAIL_TRANSITION();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
NativeDB Added Parameter 2: int p1
NativeDB Added Parameter 3: int p2
```

---
### NetworkBailTransitionQuickmatch

`_NETWORK_BAIL_TRANSITION_QUICKMATCH` · hash `0x023782EFC70585EE` · **Cliente**

```lua
NetworkBailTransitionQuickmatch()
```
```c
void _NETWORK_BAIL_TRANSITION_QUICKMATCH();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkBlockInvites

`NETWORK_BLOCK_INVITES` · hash `0x34F9E9049454A7A0` · jhash `0xD156FD1A` · **Cliente**

```lua
NetworkBlockInvites(toggle)
```
```c
void NETWORK_BLOCK_INVITES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkBlockJoinQueueInvites

`NETWORK_BLOCK_JOIN_QUEUE_INVITES` · hash `0xCFEB8AF24FC1D0BB` · jhash `0x8AB4890B` · **Cliente**

```lua
NetworkBlockJoinQueueInvites(toggle)
```
```c
void NETWORK_BLOCK_JOIN_QUEUE_INVITES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCFEB8AF24FC1D0BB` (`N_0xcfeb8af24fc1d0bb`), `_NETWORK_BLOCK_INVITES_2` (`NetworkBlockInvites_2`)

---
### NetworkBlockKickedPlayers

`_NETWORK_BLOCK_KICKED_PLAYERS` · hash `0x6B07B9CE4D390375` · jhash `0x0FCE995D` · **Cliente**

```lua
NetworkBlockKickedPlayers(p0)
```
```c
void _NETWORK_BLOCK_KICKED_PLAYERS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6B07B9CE4D390375` (`N_0x6b07b9ce4d390375`)

---
### NetworkCacheLocalPlayerHeadBlendData

`NETWORK_CACHE_LOCAL_PLAYER_HEAD_BLEND_DATA` · hash `0xBD0BE0BFC927EAC1` · jhash `0x94AB35A9` · **Cliente**

```lua
NetworkCacheLocalPlayerHeadBlendData()
```
```c
void NETWORK_CACHE_LOCAL_PLAYER_HEAD_BLEND_DATA();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBD0BE0BFC927EAC1` (`N_0xbd0be0bfc927eac1`)

---
### NetworkCanAccessMultiplayer

`NETWORK_CAN_ACCESS_MULTIPLAYER` · hash `0xAF50DA1A3F8B1BA4` · jhash `0xA520B982` · **Cliente**

```lua
local retval, loadingState = NetworkCanAccessMultiplayer(loadingState)
```
```c
BOOL NETWORK_CAN_ACCESS_MULTIPLAYER(int* loadingState);
```

**Parámetros**

- `loadingState` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
11 - Need to download tunables.  
12 - Need to download background script.  
Returns 1 if the multiplayer is loaded, otherwhise 0.  
```

**Nombres antiguos (alias):** `0xAF50DA1A3F8B1BA4` (`N_0xaf50da1a3f8b1ba4`)

---
### NetworkCanBail

`NETWORK_CAN_BAIL` · hash `0x580CE4438479CC61` · jhash `0x60E1FEDF` · **Cliente**

```lua
local retval = NetworkCanBail()
```
```c
BOOL NETWORK_CAN_BAIL();
```

**Devuelve:** `BOOL`

---
### NetworkCanCommunicateWithGamer

`NETWORK_CAN_COMMUNICATE_WITH_GAMER` · hash `0xA150A4F065806B1F` · jhash `0xD05EB7F6` · **Cliente**

```lua
local retval, networkHandle = NetworkCanCommunicateWithGamer(networkHandle)
```
```c
BOOL NETWORK_CAN_COMMUNICATE_WITH_GAMER(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkCanCommunicateWithGamer_2

`_NETWORK_CAN_COMMUNICATE_WITH_GAMER_2` · hash `0x8F5D1AD832AEB06C` · **Cliente**

```lua
local retval, networkHandle = NetworkCanCommunicateWithGamer_2(networkHandle)
```
```c
BOOL _NETWORK_CAN_COMMUNICATE_WITH_GAMER_2(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Same as NETWORK_CAN_COMMUNICATE_WITH_GAMER

NETWORK_CAN_*
```

**Nombres antiguos (alias):** `0x8F5D1AD832AEB06C` (`N_0x8f5d1ad832aeb06c`)

---
### NetworkCanEnterMultiplayer

`NETWORK_CAN_ENTER_MULTIPLAYER` · hash `0x7E782A910C362C25` · jhash `0x4A23B9C9` · **Cliente**

```lua
local retval = NetworkCanEnterMultiplayer()
```
```c
BOOL NETWORK_CAN_ENTER_MULTIPLAYER();
```

**Devuelve:** `BOOL`

---
### NetworkCanGamerPlayMultiplayerWithMe

`_NETWORK_CAN_GAMER_PLAY_MULTIPLAYER_WITH_ME` · hash `0x135F9B7B7ADD2185` · **Cliente**

```lua
local retval, networkHandle = NetworkCanGamerPlayMultiplayerWithMe(networkHandle)
```
```c
BOOL _NETWORK_CAN_GAMER_PLAY_MULTIPLAYER_WITH_ME(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x135F9B7B7ADD2185` (`N_0x135f9b7b7add2185`)

---
### NetworkCanPlayMultiplayerWithGamer

`_NETWORK_CAN_PLAY_MULTIPLAYER_WITH_GAMER` · hash `0x07DD29D5E22763F1` · **Cliente**

```lua
local retval, networkHandle = NetworkCanPlayMultiplayerWithGamer(networkHandle)
```
```c
BOOL _NETWORK_CAN_PLAY_MULTIPLAYER_WITH_GAMER(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x07DD29D5E22763F1` (`N_0x07dd29d5e22763f1`)

---
### NetworkCanSessionEnd

`NETWORK_CAN_SESSION_END` · hash `0x4EEBC3694E49C572` · jhash `0xE1FCCDBA` · **Cliente**

```lua
local retval = NetworkCanSessionEnd()
```
```c
BOOL NETWORK_CAN_SESSION_END();
```

**Devuelve:** `BOOL`

---
### NetworkCanSetWaypoint

`NETWORK_CAN_SET_WAYPOINT` · hash `0xC927EC229934AF60` · jhash `0x009E68F3` · **Cliente**

```lua
local retval = NetworkCanSetWaypoint()
```
```c
BOOL NETWORK_CAN_SET_WAYPOINT();
```

**Devuelve:** `BOOL`

---
### NetworkCanViewGamerUserContent

`_NETWORK_CAN_VIEW_GAMER_USER_CONTENT` · hash `0xB57A49545BA53CE7` · **Cliente**

```lua
local retval, networkHandle = NetworkCanViewGamerUserContent(networkHandle)
```
```c
BOOL _NETWORK_CAN_VIEW_GAMER_USER_CONTENT(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB57A49545BA53CE7` (`N_0xb57a49545ba53ce7`)

---
### NetworkCancelRespawnSearch

`NETWORK_CANCEL_RESPAWN_SEARCH` · hash `0xFB8F2A6F3DF08CBE` · jhash `0x44BFB619` · **Cliente**

```lua
NetworkCancelRespawnSearch()
```
```c
void NETWORK_CANCEL_RESPAWN_SEARCH();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFB8F2A6F3DF08CBE` (`N_0xfb8f2a6f3df08cbe`)

---
### NetworkChangeTransitionSlots

`NETWORK_CHANGE_TRANSITION_SLOTS` · hash `0xEEEDA5E6D7080987` · jhash `0x1E5F6AEF` · **Cliente**

```lua
NetworkChangeTransitionSlots(p0, p1)
```
```c
void NETWORK_CHANGE_TRANSITION_SLOTS(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEEEDA5E6D7080987` (`N_0xeeeda5e6d7080987`)

---
### NetworkCheckCommunicationPrivileges

`NETWORK_CHECK_COMMUNICATION_PRIVILEGES` · hash `0x83F28CE49FBBFFBA` · jhash `0xA79E5B05` · **Cliente**

```lua
local retval = NetworkCheckCommunicationPrivileges(p0, p1, p2)
```
```c
BOOL NETWORK_CHECK_COMMUNICATION_PRIVILEGES(int p0, int p1, BOOL p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x83F28CE49FBBFFBA` (`N_0x83f28ce49fbbffba`)

---
### NetworkCheckDataManagerSucceededForHandle

`NETWORK_CHECK_DATA_MANAGER_SUCCEEDED_FOR_HANDLE` · hash `0x44B37CDCAE765AAE` · jhash `0x13301529` · **Cliente**

```lua
local retval, networkHandle = NetworkCheckDataManagerSucceededForHandle(friendDataIndex, networkHandle)
```
```c
BOOL NETWORK_CHECK_DATA_MANAGER_SUCCEEDED_FOR_HANDLE(int friendDataIndex, int* networkHandle);
```

**Parámetros**

- `friendDataIndex` (`int`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Checks if the friendDataIndex in the friend data manager contains the data for the specified networkHandle

**Nombres antiguos (alias):** `0x44B37CDCAE765AAE` (`N_0x44b37cdcae765aae`)

---
### NetworkCheckUserContentPrivileges

`NETWORK_CHECK_USER_CONTENT_PRIVILEGES` · hash `0x595F028698072DD9` · jhash `0xBB54AA3D` · **Cliente**

```lua
local retval = NetworkCheckUserContentPrivileges(p0, p1, p2)
```
```c
BOOL NETWORK_CHECK_USER_CONTENT_PRIVILEGES(int p0, int p1, BOOL p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x595F028698072DD9` (`N_0x595f028698072dd9`)

---
### NetworkClanAnimation

`_NETWORK_CLAN_ANIMATION` · hash `0x729E3401F0430686` · jhash `0xBDA90BAC` · **Cliente**

```lua
local retval = NetworkClanAnimation(animDict, animName)
```
```c
BOOL _NETWORK_CLAN_ANIMATION(char* animDict, char* animName);
```

**Parámetros**

- `animDict` (`char*`)
- `animName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Only documented...  
```

**Nombres antiguos (alias):** `0x729E3401F0430686` (`N_0x729e3401f0430686`)

---
### NetworkClanAnyDownloadMembershipPending

`NETWORK_CLAN_ANY_DOWNLOAD_MEMBERSHIP_PENDING` · hash `0xB3F64A6A91432477` · jhash `0x83ED8E08` · **Cliente**

```lua
local retval = NetworkClanAnyDownloadMembershipPending()
```
```c
BOOL NETWORK_CLAN_ANY_DOWNLOAD_MEMBERSHIP_PENDING();
```

**Devuelve:** `BOOL` — True if there are any pending downloads, false otherwise.

**Nombres antiguos (alias):** `0xB3F64A6A91432477` (`N_0xb3f64a6a91432477`), `_NETWORK_IS_CLAN_MEMBERSHIP_FINISHED_DOWNLOADING` (`NetworkIsClanMembershipFinishedDownloading`)

---
### NetworkClanDownloadMembership

`NETWORK_CLAN_DOWNLOAD_MEMBERSHIP` · hash `0xA989044E70010ABE` · jhash `0x8E8CB520` · **Cliente**

```lua
local retval, networkHandle = NetworkClanDownloadMembership(networkHandle)
```
```c
BOOL NETWORK_CLAN_DOWNLOAD_MEMBERSHIP(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkClanDownloadMembershipPending

`NETWORK_CLAN_DOWNLOAD_MEMBERSHIP_PENDING` · hash `0x5B9E023DC6EBEDC0` · jhash `0x1FDB590F` · **Cliente**

```lua
local retval, p0 = NetworkClanDownloadMembershipPending(p0)
```
```c
BOOL NETWORK_CLAN_DOWNLOAD_MEMBERSHIP_PENDING(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkClanGetEmblemTxdName

`NETWORK_CLAN_GET_EMBLEM_TXD_NAME` · hash `0x5835D9CD92E83184` · jhash `0xBA672146` · **Cliente**

```lua
local retval, netHandle = NetworkClanGetEmblemTxdName(txdName)
```
```c
BOOL NETWORK_CLAN_GET_EMBLEM_TXD_NAME(Any* netHandle, char* txdName);
```

**Parámetros**

- `netHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `txdName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5835D9CD92E83184` (`N_0x5835d9cd92e83184`), `_NETWORK_GET_PLAYER_CREW_EMBLEM_TXD_NAME` (`NetworkGetPlayerCrewEmblemTxdName`)

---
### NetworkClanGetLocalMembershipsCount

`NETWORK_CLAN_GET_LOCAL_MEMBERSHIPS_COUNT` · hash `0x1F471B79ACC90BEF` · jhash `0x807B3450` · **Cliente**

```lua
local retval = NetworkClanGetLocalMembershipsCount()
```
```c
int NETWORK_CLAN_GET_LOCAL_MEMBERSHIPS_COUNT();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x1F471B79ACC90BEF` (`N_0x1f471b79acc90bef`), `_GET_NUM_MEMBERSHIP_DESC` (`GetNumMembershipDesc`), `_NETWORK_CLAN_GET_NUM_MEMBERSHIP_DESC` (`NetworkClanGetNumMembershipDesc`)

---
### NetworkClanGetMembership

`NETWORK_CLAN_GET_MEMBERSHIP` · hash `0xC8BC2011F67B3411` · jhash `0xCDC4A590` · **Cliente**

```lua
local retval, networkHandle, clanMembership = NetworkClanGetMembership(membershipIndex)
```
```c
BOOL NETWORK_CLAN_GET_MEMBERSHIP(int* networkHandle, int* clanMembership, int membershipIndex);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A player network handle.
- `clanMembership` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output buffer for the membership data. Also known as "desc".
- `membershipIndex` (`int`): If the player has multiple crews/memberships, use \[0-9], or -1 to get the active crew/membership.

**Devuelve:** `BOOL` — Returns true on success, false otherwise.

**Descripción oficial:**

Retrieves a membership for a player, from the cache (i.e. downloaded via NETWORK_CLAN_DOWNLOAD_MEMBERSHIP).

Test C++ code:
https://pastebin.com/CD8wni4C

---
### NetworkClanGetMembershipCount

`NETWORK_CLAN_GET_MEMBERSHIP_COUNT` · hash `0xAAB11F6C4ADBC2C1` · jhash `0x25924010` · **Cliente**

```lua
local retval, p0 = NetworkClanGetMembershipCount(p0)
```
```c
int NETWORK_CLAN_GET_MEMBERSHIP_COUNT(int* p0);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

---
### NetworkClanGetMembershipDesc

`NETWORK_CLAN_GET_MEMBERSHIP_DESC` · hash `0x48DE78AF2C8885B8` · jhash `0x3369DD1F` · **Cliente**

```lua
local retval, memberDesc = NetworkClanGetMembershipDesc(p1)
```
```c
BOOL NETWORK_CLAN_GET_MEMBERSHIP_DESC(int* memberDesc, int p1);
```

**Parámetros**

- `memberDesc` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`int`)

**Devuelve:** `BOOL`

---
### NetworkClanGetMembershipValid

`NETWORK_CLAN_GET_MEMBERSHIP_VALID` · hash `0x48A59CF88D43DF0E` · jhash `0x48914F6A` · **Cliente**

```lua
local retval, networkHandle = NetworkClanGetMembershipValid(membershipIndex)
```
```c
BOOL NETWORK_CLAN_GET_MEMBERSHIP_VALID(int* networkHandle, int membershipIndex);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A player network handle.
- `membershipIndex` (`int`): If the player has multiple crews/memberships, use \[0-9], or -1 to get the active crew/membership.

**Devuelve:** `BOOL` — Returns true if valid, false otherwise.

**Descripción oficial:**

Checks if a crew/membership for a player, from the cache (i.e. downloaded via NETWORK_CLAN_DOWNLOAD_MEMBERSHIP) is valid.

---
### NetworkClanGetUiFormattedTag

`NETWORK_CLAN_GET_UI_FORMATTED_TAG` · hash `0xF45352426FF3A4F0` · jhash `0xF633805A` · **Cliente**

```lua
local clanDesc = NetworkClanGetUiFormattedTag(bufferSize, formattedTag)
```
```c
void NETWORK_CLAN_GET_UI_FORMATTED_TAG(int* clanDesc, int bufferSize, char* formattedTag);
```

**Parámetros**

- `clanDesc` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)
- `formattedTag` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
bufferSize is 35 in the scripts.
```

**Nombres antiguos (alias):** `0xF45352426FF3A4F0` (`N_0xf45352426ff3a4f0`)

---
### NetworkClanIsEmblemReady

`NETWORK_CLAN_IS_EMBLEM_READY` · hash `0xA134777FF7F33331` · jhash `0x88B13CDC` · **Cliente**

```lua
local retval, p1 = NetworkClanIsEmblemReady(p0, p1)
```
```c
BOOL NETWORK_CLAN_IS_EMBLEM_READY(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA134777FF7F33331` (`N_0xa134777ff7f33331`)

---
### NetworkClanIsRockstarClan

`NETWORK_CLAN_IS_ROCKSTAR_CLAN` · hash `0x7543BB439F63792B` · jhash `0x54E79E9C` · **Cliente**

```lua
local retval, clanDesc = NetworkClanIsRockstarClan(bufferSize)
```
```c
BOOL NETWORK_CLAN_IS_ROCKSTAR_CLAN(int* clanDesc, int bufferSize);
```

**Parámetros**

- `clanDesc` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
bufferSize is 35 in the scripts.  
```

**Nombres antiguos (alias):** `0x7543BB439F63792B` (`N_0x7543bb439f63792b`)

---
### NetworkClanJoin

`NETWORK_CLAN_JOIN` · hash `0x9FAAA4F4FC71F87F` · jhash `0x79C916C5` · **Cliente**

```lua
local retval = NetworkClanJoin(clanDesc)
```
```c
BOOL NETWORK_CLAN_JOIN(int clanDesc);
```

**Parámetros**

- `clanDesc` (`int`)

**Devuelve:** `BOOL`

---
### NetworkClanPlayerGetDesc

`NETWORK_CLAN_PLAYER_GET_DESC` · hash `0xEEE6EACBE8874FBA` · jhash `0x6EE4A282` · **Cliente**

```lua
local retval, clanDesc, networkHandle = NetworkClanPlayerGetDesc(bufferSize)
```
```c
BOOL NETWORK_CLAN_PLAYER_GET_DESC(int* clanDesc, int bufferSize, int* networkHandle);
```

**Parámetros**

- `clanDesc` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
bufferSize is 35 in the scripts.  
bufferSize is the elementCount of p0(desc), sizeof(p0) == 280 == p1*8 == 35 * 8, p2(netHandle) is obtained from NETWORK::NETWORK_HANDLE_FROM_PLAYER.  And no, I can't explain why 35 * sizeof(int) == 280 and not 140, but I'll get back to you on that.  
the answer is: because p0 an int64_t* / int64_t[35].  and FYI p2 is an int64_t[13]  
pastebin.com/cSZniHak  
```

---
### NetworkClanPlayerIsActive

`NETWORK_CLAN_PLAYER_IS_ACTIVE` · hash `0xB124B57F571D8F18` · jhash `0xAB8319A3` · **Cliente**

```lua
local retval, networkHandle = NetworkClanPlayerIsActive(networkHandle)
```
```c
BOOL NETWORK_CLAN_PLAYER_IS_ACTIVE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkClanReleaseEmblem

`NETWORK_CLAN_RELEASE_EMBLEM` · hash `0x113E6E3E50E286B0` · jhash `0xD6E3D5EA` · **Cliente**

```lua
NetworkClanReleaseEmblem(p0)
```
```c
void NETWORK_CLAN_RELEASE_EMBLEM(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x113E6E3E50E286B0` (`N_0x113e6e3e50e286b0`)

---
### NetworkClanRemoteMembershipsAreInCache

`NETWORK_CLAN_REMOTE_MEMBERSHIPS_ARE_IN_CACHE` · hash `0xBB6E6FEE99D866B2` · jhash `0x40202867` · **Cliente**

```lua
local retval, p0 = NetworkClanRemoteMembershipsAreInCache(p0)
```
```c
BOOL NETWORK_CLAN_REMOTE_MEMBERSHIPS_ARE_IN_CACHE(int* p0);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkClanRequestEmblem

`NETWORK_CLAN_REQUEST_EMBLEM` · hash `0x13518FF1C6B28938` · jhash `0x7963FA4D` · **Cliente**

```lua
local retval = NetworkClanRequestEmblem(p0)
```
```c
BOOL NETWORK_CLAN_REQUEST_EMBLEM(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x13518FF1C6B28938` (`N_0x13518ff1c6b28938`)

---
### NetworkClanServiceIsValid

`NETWORK_CLAN_SERVICE_IS_VALID` · hash `0x579CCED0265D4896` · jhash `0xF5F4BD95` · **Cliente**

```lua
local retval = NetworkClanServiceIsValid()
```
```c
BOOL NETWORK_CLAN_SERVICE_IS_VALID();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_NETWORK_PLAYER_IS_IN_CLAN` (`NetworkPlayerIsInClan`)

---
### NetworkClearClockTimeOverride

`NETWORK_CLEAR_CLOCK_TIME_OVERRIDE` · hash `0xD972DF67326F966E` · jhash `0xC4AEAF49` · **Cliente**

```lua
NetworkClearClockTimeOverride()
```
```c
void NETWORK_CLEAR_CLOCK_TIME_OVERRIDE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD972DF67326F966E` (`N_0xd972df67326f966e`)

---
### NetworkClearFollowInvite

`NETWORK_CLEAR_FOLLOW_INVITE` · hash `0x439BFDE3CD0610F6` · jhash `0x3242F952` · **Cliente**

```lua
local retval = NetworkClearFollowInvite()
```
```c
Any NETWORK_CLEAR_FOLLOW_INVITE();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x439BFDE3CD0610F6` (`N_0x439bfde3cd0610f6`)

---
### NetworkClearFollowers

`NETWORK_CLEAR_FOLLOWERS` · hash `0x058F43EC59A8631A` · jhash `0x5E557307` · **Cliente**

```lua
NetworkClearFollowers()
```
```c
void NETWORK_CLEAR_FOLLOWERS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x058F43EC59A8631A` (`N_0x058f43ec59a8631a`)

---
### NetworkClearFoundGamers

`NETWORK_CLEAR_FOUND_GAMERS` · hash `0x6D14CCEE1B40381A` · jhash `0x6AA9A154` · **Cliente**

```lua
NetworkClearFoundGamers()
```
```c
void NETWORK_CLEAR_FOUND_GAMERS();
```

**Devuelve:** `void`

---
### NetworkClearGetGamerStatus

`NETWORK_CLEAR_GET_GAMER_STATUS` · hash `0x86E0660E4F5C956D` · jhash `0x3F7EDBBD` · **Cliente**

```lua
NetworkClearGetGamerStatus()
```
```c
void NETWORK_CLEAR_GET_GAMER_STATUS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x86E0660E4F5C956D` (`N_0x86e0660e4f5c956d`)

---
### NetworkClearGroupActivity

`NETWORK_CLEAR_GROUP_ACTIVITY` · hash `0x1888694923EF4591` · jhash `0x157D44D3` · **Cliente**

```lua
NetworkClearGroupActivity()
```
```c
void NETWORK_CLEAR_GROUP_ACTIVITY();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1888694923EF4591` (`N_0x1888694923ef4591`)

---
### NetworkClearPropertyId

`NETWORK_CLEAR_PROPERTY_ID` · hash `0xC2B82527CA77053E` · jhash `0x38BC35C8` · **Cliente**

```lua
NetworkClearPropertyId()
```
```c
void NETWORK_CLEAR_PROPERTY_ID();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC2B82527CA77053E` (`N_0xc2b82527ca77053e`)

---
### NetworkClearTransitionCreatorHandle

`NETWORK_CLEAR_TRANSITION_CREATOR_HANDLE` · hash `0xFB3272229A82C759` · jhash `0x8BB336F7` · **Cliente**

```lua
NetworkClearTransitionCreatorHandle()
```
```c
void NETWORK_CLEAR_TRANSITION_CREATOR_HANDLE();
```

**Devuelve:** `void`

---
### NetworkClearVoiceChannel

`NETWORK_CLEAR_VOICE_CHANNEL` · hash `0xE036A705F989E049` · jhash `0x9ECF722A` · **Cliente**

```lua
NetworkClearVoiceChannel()
```
```c
void NETWORK_CLEAR_VOICE_CHANNEL();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE036A705F989E049` (`N_0xe036a705f989e049`)

---
### NetworkClearVoiceProximityOverride

`NETWORK_CLEAR_VOICE_PROXIMITY_OVERRIDE` · hash `0xF03755696450470C` · jhash `0x7F9B9052` · **Cliente**

```lua
NetworkClearVoiceProximityOverride()
```
```c
void NETWORK_CLEAR_VOICE_PROXIMITY_OVERRIDE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF03755696450470C` (`N_0xf03755696450470c`)

---
### NetworkCloseTransitionMatchmaking

`NETWORK_CLOSE_TRANSITION_MATCHMAKING` · hash `0x43F4DBA69710E01E` · jhash `0x82D32D07` · **Cliente**

```lua
NetworkCloseTransitionMatchmaking()
```
```c
void NETWORK_CLOSE_TRANSITION_MATCHMAKING();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x43F4DBA69710E01E` (`N_0x43f4dba69710e01e`)

---
### NetworkConcealEntity

`_NETWORK_CONCEAL_ENTITY` · hash `0x1632BE0AC1E62876` · **Cliente**

```lua
NetworkConcealEntity(entity, toggle)
```
```c
void _NETWORK_CONCEAL_ENTITY(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkConcealPlayer

`NETWORK_CONCEAL_PLAYER` · hash `0xBBDF066252829606` · jhash `0x72052DB3` · **Cliente**

```lua
NetworkConcealPlayer(player, toggle, bAllowDamagingWhileConcealed)
```
```c
void NETWORK_CONCEAL_PLAYER(Player player, BOOL toggle, BOOL bAllowDamagingWhileConcealed);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)
- `bAllowDamagingWhileConcealed` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This is what R\* uses to hide players in MP interiors.

To manage player visibility with NetworkConcealPlayer, here’s a solid approach:

**General Population (players not in any instance):**

*   Use NetworkConcealPlayer to hide players who are in any instance. This way, general population players won’t see or interact with instance players.

**Instance Players (players in a specific instance):**

*   Use NetworkConcealPlayer to hide players who aren’t in the same instance. Instance players can still see and interact with the general population but not with players in other instances.

This setup keeps instance players separate from each other while allowing interaction with the general population.

**Ejemplo (lua):**

```lua
function GetPlayerInstance(player)
	-- you can replace this with your own data
    local playerServerId = GetPlayerServerId(player)
    return Player(playerServerId).state.instance_id or 0
end

local playerId = PlayerId()
-- Function to manage player visibility
function concealPlayers()
    local allPlayers = GetActivePlayers()
	local localPlayerInstance = GetPlayerInstance(playerId)

    for _, player in ipairs(allPlayers) do
        if player == playerId then goto continue end

        local playerInstance = GetPlayerInstance(player)

		if playerInstance == localPlayerInstance then
			-- if we're in the same instance then we want to be able to see them
			NetworkConcealPlayer(player, false, false)
		else
			-- they're in a different instance, so hide them
			NetworkConcealPlayer(player, true, false)
		end

		::continue::
    end
end

CreateThread(function()
	while true do
		concealPlayers()
		Wait(250)
	end
end)
```

---
### NetworkCreateSynchronisedScene

`NETWORK_CREATE_SYNCHRONISED_SCENE` · hash `0x7CD6BC4C2BBDD526` · jhash `0xB06FE3FE` · **Cliente**

```lua
local retval = NetworkCreateSynchronisedScene(x, y, z, xRot, yRot, zRot, rotationOrder, holdLastFrame, looped, phaseToStopScene, phaseToStartScene, animSpeed)
```
```c
int NETWORK_CREATE_SYNCHRONISED_SCENE(float x, float y, float z, float xRot, float yRot, float zRot, int rotationOrder, BOOL holdLastFrame, BOOL looped, float phaseToStopScene, float phaseToStartScene, float animSpeed);
```

**Parámetros**

- `x` (`float`): X coord of the scene position (If the scene is for an object, the position should be of the object's coordinates most of the time)
- `y` (`float`): Y coord of the scene position.
- `z` (`float`): Z coord of the scene position.
- `xRot` (`float`): Value x of the scene rotation.
- `yRot` (`float`): Value y of the scene rotation.
- `zRot` (`float`): Value z of the scene rotation (It's heading).
- `rotationOrder` (`int`): Rotation order. Default is 2.
- `holdLastFrame` (`BOOL`): If true, the scene stays on the last frame once it finishes, making `GetSynchronizedScenePhase` keep returning `1.0`. Script is expected to clean up it's memory and stop the animation if this is passed as true and the phase reaches `1.0`.
- `looped` (`BOOL`): If true, the scene will be looped and `holdLastFrame` will be disregarded.
- `phaseToStopScene` (`float`): Which phase (from `0.0` to `1.0` to stop the scene. Default is `1.0`)
- `phaseToStartScene` (`float`): Which phase (from `0.0` to `1.0` to start the scene. Default is `0.0`)
- `animSpeed` (`float`): Speed of the animation. Default is `1.0`

**Devuelve:** `int` — Returns the network synchronized scene's handle. You can get information regarding the phase, rate etc of this synchronised scene by using local synchronized scene natives (e.g [`GET_SYNCHRONIZED_SCENE_PHASE`](PED-1.md#getsynchronizedscenephase)). Do note that you need to get the local scene handle from the network scene handle (using [`NETWORK_GET_LOCAL_SCENE_FROM_NETWORK_ID`](#networkgetlocalscenefromnetworkid)) and then pass the returned value to the local synchronized scene info natives.

**Descripción oficial:**

Creates a networked synchronized scene.
Be sure to actually start the scene with [`NETWORK_START_SYNCHRONISED_SCENE`](#networkstartsynchronisedscene) after you're done adding peds or entities to the scene.

---
### NetworkDidFindGamersSucceed

`NETWORK_DID_FIND_GAMERS_SUCCEED` · hash `0xF9B83B77929D8863` · jhash `0xBEDC4503` · **Cliente**

```lua
local retval = NetworkDidFindGamersSucceed()
```
```c
BOOL NETWORK_DID_FIND_GAMERS_SUCCEED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF9B83B77929D8863` (`N_0xf9b83b77929d8863`)

---
### NetworkDidGetGamerStatusSucceed

`NETWORK_DID_GET_GAMER_STATUS_SUCCEED` · hash `0x5AE17C6B0134B7F1` · jhash `0xC871E745` · **Cliente**

```lua
local retval = NetworkDidGetGamerStatusSucceed()
```
```c
BOOL NETWORK_DID_GET_GAMER_STATUS_SUCCEED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5AE17C6B0134B7F1` (`N_0x5ae17c6b0134b7f1`)

---
### NetworkDisableInvincibleFlashing

`NETWORK_DISABLE_INVINCIBLE_FLASHING` · hash `0x9DD368BF06983221` · jhash `0x8D27280E` · **Cliente**

```lua
NetworkDisableInvincibleFlashing(player, toggle)
```
```c
void NETWORK_DISABLE_INVINCIBLE_FLASHING(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9DD368BF06983221` (`N_0x9dd368bf06983221`)

---
### NetworkDisableLeaveRemotePedBehind

`NETWORK_DISABLE_LEAVE_REMOTE_PED_BEHIND` · hash `0xC505036A35AFD01B` · jhash `0xA100CC97` · **Cliente**

```lua
NetworkDisableLeaveRemotePedBehind(toggle)
```
```c
void NETWORK_DISABLE_LEAVE_REMOTE_PED_BEHIND(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC505036A35AFD01B` (`N_0xc505036a35afd01b`)

---
### NetworkDisableProximityMigration

`NETWORK_DISABLE_PROXIMITY_MIGRATION` · hash `0x407091CF6037118E` · jhash `0x9F82917F` · **Cliente**

```lua
NetworkDisableProximityMigration(netID)
```
```c
void NETWORK_DISABLE_PROXIMITY_MIGRATION(int netID);
```

**Parámetros**

- `netID` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x407091CF6037118E` (`N_0x407091cf6037118e`)

---
### NetworkDisplaynamesFromHandlesStart

`_NETWORK_DISPLAYNAMES_FROM_HANDLES_START` · hash `0xD66C9E72B3CC4982` · **Cliente**

```lua
local retval, p0 = NetworkDisplaynamesFromHandlesStart(p1)
```
```c
int _NETWORK_DISPLAYNAMES_FROM_HANDLES_START(Any* p0, Any p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)

**Devuelve:** `int`

**Descripción oficial:**

```
Hardcoded to return -1.
```

**Nombres antiguos (alias):** `0xD66C9E72B3CC4982` (`N_0xd66c9e72b3cc4982`)

---
### NetworkDoTransitionQuickmatch

`NETWORK_DO_TRANSITION_QUICKMATCH` · hash `0x71FB0EBCD4915D56` · jhash `0x2FF65C0B` · **Cliente**

```lua
local retval = NetworkDoTransitionQuickmatch(p0, p1, p2, p3)
```
```c
BOOL NETWORK_DO_TRANSITION_QUICKMATCH(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 5: Any p4
NativeDB Added Parameter 6: Any p5
```

**Nombres antiguos (alias):** `0x71FB0EBCD4915D56` (`N_0x71fb0ebcd4915d56`)

---
### NetworkDoTransitionQuickmatchAsync

`NETWORK_DO_TRANSITION_QUICKMATCH_ASYNC` · hash `0xA091A5E44F0072E5` · jhash `0x47D61C99` · **Cliente**

```lua
local retval = NetworkDoTransitionQuickmatchAsync(p0, p1, p2, p3)
```
```c
BOOL NETWORK_DO_TRANSITION_QUICKMATCH_ASYNC(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 5: Any p4
NativeDB Added Parameter 6: Any p5
```

**Nombres antiguos (alias):** `0xA091A5E44F0072E5` (`N_0xa091a5e44f0072e5`)

---
### NetworkDoTransitionQuickmatchWithGroup

`NETWORK_DO_TRANSITION_QUICKMATCH_WITH_GROUP` · hash `0x9C4AB58491FDC98A` · jhash `0x5CE60A11` · **Cliente**

```lua
local retval, p4 = NetworkDoTransitionQuickmatchWithGroup(p0, p1, p2, p3, p5)
```
```c
BOOL NETWORK_DO_TRANSITION_QUICKMATCH_WITH_GROUP(Any p0, Any p1, Any p2, Any p3, Any* p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p5` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 7: Any p6
NativeDB Added Parameter 8: Any p7
```

---
### NetworkDoTransitionToFreemode

`NETWORK_DO_TRANSITION_TO_FREEMODE` · hash `0x3AAD8B2FCA1E289F` · jhash `0xC7CB8ADF` · **Cliente**

```lua
local retval, p0 = NetworkDoTransitionToFreemode(p1, p2, players, p4)
```
```c
BOOL NETWORK_DO_TRANSITION_TO_FREEMODE(Any* p0, Any p1, BOOL p2, int players, BOOL p4);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`BOOL`)
- `players` (`int`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p2 is true 3/4 of the occurrences I found.  
'players' is the number of players for a session. On PS3/360 it's always 18. On PC it's 32.  
```

---
### NetworkDoTransitionToGame

`NETWORK_DO_TRANSITION_TO_GAME` · hash `0x3E9BB38102A589B0` · jhash `0x1B2114D2` · **Cliente**

```lua
local retval = NetworkDoTransitionToGame(p0, maxPlayers)
```
```c
BOOL NETWORK_DO_TRANSITION_TO_GAME(BOOL p0, int maxPlayers);
```

**Parámetros**

- `p0` (`BOOL`)
- `maxPlayers` (`int`)

**Devuelve:** `BOOL`

---
### NetworkDoTransitionToNewFreemode

`NETWORK_DO_TRANSITION_TO_NEW_FREEMODE` · hash `0x9E80A5BA8109F974` · jhash `0xAD13375E` · **Cliente**

```lua
local retval, p0, p1 = NetworkDoTransitionToNewFreemode(players, p3, p4, p5)
```
```c
BOOL NETWORK_DO_TRANSITION_TO_NEW_FREEMODE(Any* p0, Any* p1, int players, BOOL p3, BOOL p4, BOOL p5);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `players` (`int`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `BOOL`

---
### NetworkDoTransitionToNewGame

`NETWORK_DO_TRANSITION_TO_NEW_GAME` · hash `0x4665F51EFED00034` · jhash `0x58AFBE63` · **Cliente**

```lua
local retval = NetworkDoTransitionToNewGame(p0, maxPlayers, p2)
```
```c
BOOL NETWORK_DO_TRANSITION_TO_NEW_GAME(BOOL p0, int maxPlayers, BOOL p2);
```

**Parámetros**

- `p0` (`BOOL`)
- `maxPlayers` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

---
### NetworkDoesEntityExistWithNetworkId

`NETWORK_DOES_ENTITY_EXIST_WITH_NETWORK_ID` · hash `0x18A47D074708FD68` · jhash `0x1E2E3177` · **Cliente**

```lua
local retval = NetworkDoesEntityExistWithNetworkId(netId)
```
```c
BOOL NETWORK_DOES_ENTITY_EXIST_WITH_NETWORK_ID(int netId);
```

**Parámetros**

- `netId` (`int`)

**Devuelve:** `BOOL`

---
### NetworkDoesNetworkIdExist

`NETWORK_DOES_NETWORK_ID_EXIST` · hash `0x38CE16C96BD11344` · jhash `0xB8D2C99E` · **Cliente**

```lua
local retval = NetworkDoesNetworkIdExist(netId)
```
```c
BOOL NETWORK_DOES_NETWORK_ID_EXIST(int netId);
```

**Parámetros**

- `netId` (`int`)

**Devuelve:** `BOOL`

---
### NetworkDoesTunableExist

`NETWORK_DOES_TUNABLE_EXIST` · hash `0x85E5F8B9B898B20A` · jhash `0x9FCE9C9A` · **Cliente**

```lua
local retval = NetworkDoesTunableExist(tunableContext, tunableName)
```
```c
BOOL NETWORK_DOES_TUNABLE_EXIST(char* tunableContext, char* tunableName);
```

**Parámetros**

- `tunableContext` (`char*`)
- `tunableName` (`char*`)

**Devuelve:** `BOOL`

---
### NetworkDoesTunableExistHash

`NETWORK_DOES_TUNABLE_EXIST_HASH` · hash `0xE4E53E1419D81127` · jhash `0x25915CB9` · **Cliente**

```lua
local retval = NetworkDoesTunableExistHash(tunableContext, tunableName)
```
```c
BOOL NETWORK_DOES_TUNABLE_EXIST_HASH(Hash tunableContext, Hash tunableName);
```

**Parámetros**

- `tunableContext` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `tunableName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE4E53E1419D81127` (`N_0xe4e53e1419d81127`), `_NETWORK_DOES_TUNABLE_EXIST_HASH` (`NetworkDoesTunableExistHash`)

---
### NetworkEndTutorialSession

`NETWORK_END_TUTORIAL_SESSION` · hash `0xD0AFAFF5A51D72F7` · jhash `0xBA57E53E` · **Cliente**

```lua
NetworkEndTutorialSession()
```
```c
void NETWORK_END_TUTORIAL_SESSION();
```

**Devuelve:** `void`

---
### NetworkEntityAreaDoesExist

`NETWORK_ENTITY_AREA_DOES_EXIST` · hash `0xE64A3CA08DFA37A9` · jhash `0x69956127` · **Cliente**

```lua
local retval = NetworkEntityAreaDoesExist(areaHandle)
```
```c
BOOL NETWORK_ENTITY_AREA_DOES_EXIST(int areaHandle);
```

**Parámetros**

- `areaHandle` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE64A3CA08DFA37A9` (`N_0xe64a3ca08dfa37a9`)

---
### NetworkEntityAreaIsOccupied

`NETWORK_ENTITY_AREA_IS_OCCUPIED` · hash `0x4A2D4E8BF4265B0F` · jhash `0xC6D53AA0` · **Cliente**

```lua
local retval = NetworkEntityAreaIsOccupied(areaHandle)
```
```c
BOOL NETWORK_ENTITY_AREA_IS_OCCUPIED(int areaHandle);
```

**Parámetros**

- `areaHandle` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4A2D4E8BF4265B0F` (`N_0x4a2d4e8bf4265b0f`)

---
### NetworkExplodeHeli

`NETWORK_EXPLODE_HELI` · hash `0x2A5E0621DD815A9A` · jhash `0x955B31BF` · **Cliente**

```lua
NetworkExplodeHeli(heli, isAudible, isInvisible, netScriptEntityId)
```
```c
void NETWORK_EXPLODE_HELI(Vehicle heli, BOOL isAudible, BOOL isInvisible, int netScriptEntityId);
```

**Parámetros**

- `heli` (`Vehicle`): Heli to explode
- `isAudible` (`BOOL`)
- `isInvisible` (`BOOL`)
- `netScriptEntityId` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2A5E0621DD815A9A` (`N_0x2a5e0621dd815a9a`)

---
### NetworkExplodeVehicle

`NETWORK_EXPLODE_VEHICLE` · hash `0x301A42153C9AD707` · jhash `0x0E1B38AE` · **Cliente**

```lua
NetworkExplodeVehicle(vehicle, isAudible, isInvisible, p3)
```
```c
void NETWORK_EXPLODE_VEHICLE(Vehicle vehicle, BOOL isAudible, BOOL isInvisible, BOOL p3);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `isAudible` (`BOOL`)
- `isInvisible` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
In the console script dumps, this is only referenced once.   
NETWORK::NETWORK_EXPLODE_VEHICLE(vehicle, 1, 0, 0);  
^^^^^ That must be PC script dumps? In X360 Script Dumps it is reference a few times with 2 differences in the parameters.  
Which as you see below is 1, 0, 0 + 1, 1, 0 + 1, 0, and a *param?  
am_plane_takedown.c   
network_explode_vehicle(net_to_veh(Local_40.imm_2), 1, 1, 0);  
armenian2.c   
network_explode_vehicle(Local_80[6 <2>], 1, 0, 0);  
fm_horde_controler.c  
network_explode_vehicle(net_to_veh(*uParam0), 1, 0, *uParam0);  
fm_mission_controller.c, has 6 hits so not going to list them.  
Side note, setting the first parameter to 0 seems to mute sound or so?  
Seems it's like ADD_EXPLOSION, etc. the first 2 params. The 3rd atm no need to worry since it always seems to be 0.  
```

---
### NetworkFadeInEntity

`NETWORK_FADE_IN_ENTITY` · hash `0x1F4ED342ACEFE62D` · jhash `0x9B9FCD02` · **Cliente**

```lua
NetworkFadeInEntity(entity, bNetwork)
```
```c
void NETWORK_FADE_IN_ENTITY(Entity entity, BOOL bNetwork);
```

**Parámetros**

- `entity` (`Entity`): The entity to fade in
- `bNetwork` (`BOOL`): When set to true the fade in will be networked.

**Devuelve:** `void`

**Descripción oficial:**

Fade the given entity back in, usually used after the entity has been faded out with [NETWORK_FADE_OUT_ENTITY](#networkfadeoutentity)

When used on a entity which isn't invisible or faded out then the native will still work, it will just instanly make the ped invisible before fading in.

**Additional Parameters**:

*   **flash**: If set to true the entity will flash while fading in.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()

-- fade out the player while flashing them
NetworkFadeOutEntity(playerPed, true, false)
while NetworkIsEntityFading(playerPed) do
  Wait(0)
end

--- Do something like a teleport, or warp into a vehicle

-- while generally frowned upon when you can use natives, this declaration has
-- a missing parameter, which doesn't work without manually invoking.
Citizen.InvokeNative(0x1F4ED342ACEFE62D, playerPed, false, true)
while NetworkIsEntityFading(playerPed) do
  Wait(0)
end
```

---
### NetworkFadeOutEntity

`NETWORK_FADE_OUT_ENTITY` · hash `0xDE564951F95E09ED` · jhash `0x47EDEE56` · **Cliente**

```lua
NetworkFadeOutEntity(entity, normal, slow)
```
```c
void NETWORK_FADE_OUT_ENTITY(Entity entity, BOOL normal, BOOL slow);
```

**Parámetros**

- `entity` (`Entity`)
- `normal` (`BOOL`)
- `slow` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
normal - transition like when your coming out of LSC  
slow - transition like when you walk into a mission  
```

---
### NetworkFindGamersInCrew

`NETWORK_FIND_GAMERS_IN_CREW` · hash `0xE532D6811B3A4D2A` · jhash `0x7771AB83` · **Cliente**

```lua
local retval = NetworkFindGamersInCrew(p0)
```
```c
BOOL NETWORK_FIND_GAMERS_IN_CREW(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE532D6811B3A4D2A` (`N_0xe532d6811b3a4d2a`), `NETWORK_X_AFFECTS_GAMERS` (`NetworkXAffectsGamers`)

---
### NetworkFindMatchedGamers

`NETWORK_FIND_MATCHED_GAMERS` · hash `0xF7B2CFDE5C9F700D` · jhash `0xA13045D4` · **Cliente**

```lua
local retval = NetworkFindMatchedGamers(p0, p1, p2, p3)
```
```c
BOOL NETWORK_FIND_MATCHED_GAMERS(Any p0, float p1, float p2, float p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF7B2CFDE5C9F700D` (`N_0xf7b2cfde5c9f700d`)

---
### NetworkFinishBroadcastingData

`NETWORK_FINISH_BROADCASTING_DATA` · hash `0x64F62AFB081E260D` · jhash `0xA71A1D2A` · **Cliente**

```lua
NetworkFinishBroadcastingData()
```
```c
void NETWORK_FINISH_BROADCASTING_DATA();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x64F62AFB081E260D` (`N_0x64f62afb081e260d`)

---
### NetworkForceLocalUseOfSyncedSceneCamera

`NETWORK_FORCE_LOCAL_USE_OF_SYNCED_SCENE_CAMERA` · hash `0xC9B43A33D09CADA7` · jhash `0xC3AA2EC7` · **Cliente**

```lua
NetworkForceLocalUseOfSyncedSceneCamera(sceneId)
```
```c
void NETWORK_FORCE_LOCAL_USE_OF_SYNCED_SCENE_CAMERA(int sceneId);
```

**Parámetros**

- `sceneId` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC9B43A33D09CADA7` (`N_0xc9b43a33d09cada7`)

---
### NetworkGamerHasHeadset

`NETWORK_GAMER_HAS_HEADSET` · hash `0xF2FD55CB574BCC55` · jhash `0xD036DA4A` · **Cliente**

```lua
local retval, networkHandle = NetworkGamerHasHeadset(networkHandle)
```
```c
BOOL NETWORK_GAMER_HAS_HEADSET(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkGamertagFromHandlePending

`NETWORK_GAMERTAG_FROM_HANDLE_PENDING` · hash `0xB071E27958EF4CF0` · jhash `0xF000828E` · **Cliente**

```lua
local retval = NetworkGamertagFromHandlePending()
```
```c
BOOL NETWORK_GAMERTAG_FROM_HANDLE_PENDING();
```

**Devuelve:** `BOOL`

---
### NetworkGamertagFromHandleStart

`NETWORK_GAMERTAG_FROM_HANDLE_START` · hash `0x9F0C0A981D73FA56` · jhash `0xEBA00C2A` · **Cliente**

```lua
local retval, networkHandle = NetworkGamertagFromHandleStart(networkHandle)
```
```c
BOOL NETWORK_GAMERTAG_FROM_HANDLE_START(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkGamertagFromHandleSucceeded

`NETWORK_GAMERTAG_FROM_HANDLE_SUCCEEDED` · hash `0xFD00798DBA7523DD` · jhash `0x89C2B5EA` · **Cliente**

```lua
local retval = NetworkGamertagFromHandleSucceeded()
```
```c
BOOL NETWORK_GAMERTAG_FROM_HANDLE_SUCCEEDED();
```

**Devuelve:** `BOOL`

---
### NetworkGetActivityPlayerNum

`NETWORK_GET_ACTIVITY_PLAYER_NUM` · hash `0x73E2B500410DA5A2` · jhash `0x31F951FD` · **Cliente**

```lua
local retval = NetworkGetActivityPlayerNum(p0)
```
```c
int NETWORK_GET_ACTIVITY_PLAYER_NUM(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

---
### NetworkGetAgeGroup

`NETWORK_GET_AGE_GROUP` · hash `0x9614B71F8ADB982B` · jhash `0xAB07CBBE` · **Cliente**

```lua
local retval = NetworkGetAgeGroup()
```
```c
int NETWORK_GET_AGE_GROUP();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x9614B71F8ADB982B` (`N_0x9614b71f8adb982b`)

---
### NetworkGetAverageLatencyForPlayer

`_NETWORK_GET_AVERAGE_LATENCY_FOR_PLAYER` · hash `0xD414BE129BB81B32` · **Cliente**

```lua
local retval = NetworkGetAverageLatencyForPlayer(player)
```
```c
float _NETWORK_GET_AVERAGE_LATENCY_FOR_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xD414BE129BB81B32` (`N_0xd414be129bb81b32`)

---
### NetworkGetAverageLatencyForPlayer_2

`_NETWORK_GET_AVERAGE_LATENCY_FOR_PLAYER_2` · hash `0x0E3A041ED6AC2B45` · **Cliente**

```lua
local retval = NetworkGetAverageLatencyForPlayer_2(player)
```
```c
float _NETWORK_GET_AVERAGE_LATENCY_FOR_PLAYER_2(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

**Descripción oficial:**

```
Same as _NETWORK_GET_AVERAGE_LATENCY_FOR_PLAYER (0xD414BE129BB81B32)
```

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x0E3A041ED6AC2B45` (`N_0x0e3a041ed6ac2b45`)

---
### NetworkGetAveragePacketLossForPlayer

`_NETWORK_GET_AVERAGE_PACKET_LOSS_FOR_PLAYER` · hash `0x350C23949E43686C` · **Cliente**

```lua
local retval = NetworkGetAveragePacketLossForPlayer(player)
```
```c
float _NETWORK_GET_AVERAGE_PACKET_LOSS_FOR_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

**Descripción oficial:**

```
NETWORK_GET_*

NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x350C23949E43686C` (`N_0x350c23949e43686c`)

---
### NetworkGetBackgroundLoadingRecipients

`NETWORK_GET_BACKGROUND_LOADING_RECIPIENTS` · hash `0x97A770BEEF227E2B` · jhash `0x1CFB3F51` · **Cliente**

```lua
local retval, p2, p3 = NetworkGetBackgroundLoadingRecipients(p0, p1)
```
```c
BOOL NETWORK_GET_BACKGROUND_LOADING_RECIPIENTS(Any p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x97A770BEEF227E2B` (`N_0x97a770beef227e2b`)

---
### NetworkGetContentModifierListId

`NETWORK_GET_CONTENT_MODIFIER_LIST_ID` · hash `0x187382F8A3E0A6C3` · jhash `0xA78571CA` · **Cliente**

```lua
local retval = NetworkGetContentModifierListId(contentHash)
```
```c
int NETWORK_GET_CONTENT_MODIFIER_LIST_ID(Hash contentHash);
```

**Parámetros**

- `contentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Return the content modifier id (the tunables context if you want) of a specific content.  
It takes the content hash (which is the mission id hash), and return the content modifier id, used as the tunables context.  
The mission id can be found on the Social club, for example, 'socialclub.rockstargames.com/games/gtav/jobs/job/A8M6Bz8MLEC5xngvDCzGwA'  
'A8M6Bz8MLEC5xngvDCzGwA' is the mission id, so the game hash this and use it as the parameter for this native.  
```

**Nombres antiguos (alias):** `0x187382F8A3E0A6C3` (`N_0x187382f8a3e0a6c3`), `_GET_TUNABLES_CONTENT_MODIFIER_ID` (`GetTunablesContentModifierId`)

---
### NetworkGetCurrentlySelectedGamerHandleFromInviteMenu

`NETWORK_GET_CURRENTLY_SELECTED_GAMER_HANDLE_FROM_INVITE_MENU` · hash `0x74881E6BCAE2327C` · jhash `0x72BA00CE` · **Cliente**

```lua
local retval, p0 = NetworkGetCurrentlySelectedGamerHandleFromInviteMenu(p0)
```
```c
BOOL NETWORK_GET_CURRENTLY_SELECTED_GAMER_HANDLE_FROM_INVITE_MENU(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkGetDestroyerOfEntity

`_NETWORK_GET_DESTROYER_OF_ENTITY` · hash `0x4CACA84440FA26F6` · jhash `0x28A45454` · **Cliente**

```lua
local retval, weaponHash = NetworkGetDestroyerOfEntity(p0, p1, weaponHash)
```
```c
BOOL _NETWORK_GET_DESTROYER_OF_ENTITY(Any p0, Any p1, Hash* weaponHash);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `weaponHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4CACA84440FA26F6` (`N_0x4caca84440fa26f6`), `_NETWORK_GET_DESROYER_OF_ENTITY` (`NetworkGetDesroyerOfEntity`)

---
### NetworkGetDestroyerOfNetworkId

`NETWORK_GET_DESTROYER_OF_NETWORK_ID` · hash `0x7A1ADEEF01740A24` · jhash `0x4FCA6436` · **Cliente**

```lua
local retval, weaponHash = NetworkGetDestroyerOfNetworkId(netId, weaponHash)
```
```c
int NETWORK_GET_DESTROYER_OF_NETWORK_ID(int netId, Hash* weaponHash);
```

**Parámetros**

- `netId` (`int`)
- `weaponHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

---
### NetworkGetDisplaynamesFromHandles

`_NETWORK_GET_DISPLAYNAMES_FROM_HANDLES` · hash `0x58CC181719256197` · **Cliente**

```lua
local retval = NetworkGetDisplaynamesFromHandles(p0, p1, p2)
```
```c
int _NETWORK_GET_DISPLAYNAMES_FROM_HANDLES(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `int` — Hard-coded to always return 0.

**Nombres antiguos (alias):** `0x58CC181719256197` (`N_0x58cc181719256197`)

---
### NetworkGetEntityFromNetworkId

`NETWORK_GET_ENTITY_FROM_NETWORK_ID` · hash `0xCE4E5D9B0A4FF560` · jhash `0x5B912C3F` · **Cliente**

```lua
local retval = NetworkGetEntityFromNetworkId(netId)
```
```c
Entity NETWORK_GET_ENTITY_FROM_NETWORK_ID(int netId);
```

**Parámetros**

- `netId` (`int`): the network id of the entity

**Devuelve:** `Entity` — The local entity handle of the network id

**Descripción oficial:**

Get the local entity handle of the given network id

Through this native you can get back the entity that you previously converted to netid with [NetworkGetNetworkIdFromEntity](../cfx/servidor.md#networkgetnetworkidfromentity) or with the `ToNet` natives

**Ejemplo (lua):**

```lua
local entity = NetworkGetEntityFromNetworkId(netId)
```

**Ejemplo (js):**

```js
const entity = NetworkGetEntityFromNetworkId(netId);
```

**Ejemplo (cs):**

```cs
int entity = NetworkGetEntityFromNetworkId(netId);
```

---
### NetworkGetEntityIsLocal

`NETWORK_GET_ENTITY_IS_LOCAL` · hash `0x0991549DE4D64762` · jhash `0x813353ED` · **Cliente**

```lua
local retval = NetworkGetEntityIsLocal(entity)
```
```c
BOOL NETWORK_GET_ENTITY_IS_LOCAL(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### NetworkGetEntityIsNetworked

`NETWORK_GET_ENTITY_IS_NETWORKED` · hash `0xC7827959479DCC78` · jhash `0xD7F934F4` · **Cliente**

```lua
local retval = NetworkGetEntityIsNetworked(entity)
```
```c
BOOL NETWORK_GET_ENTITY_IS_NETWORKED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC7827959479DCC78` (`N_0xc7827959479dcc78`)

---
### NetworkGetEntityKillerOfPlayer

`NETWORK_GET_ENTITY_KILLER_OF_PLAYER` · hash `0x42B2DAA6B596F5F8` · jhash `0xA7E7E04F` · **Cliente**

```lua
local retval, weaponHash = NetworkGetEntityKillerOfPlayer(player, weaponHash)
```
```c
Entity NETWORK_GET_ENTITY_KILLER_OF_PLAYER(Player player, Hash* weaponHash);
```

**Parámetros**

- `player` (`Player`)
- `weaponHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Entity`

---
### NetworkGetEntityNetScriptId

`_NETWORK_GET_ENTITY_NET_SCRIPT_ID` · hash `0x815F18AD865F057F` · **Cliente**

```lua
local retval = NetworkGetEntityNetScriptId(entity)
```
```c
int _NETWORK_GET_ENTITY_NET_SCRIPT_ID(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x815F18AD865F057F` (`N_0x815f18ad865f057f`)

---
### NetworkGetFoundGamer

`NETWORK_GET_FOUND_GAMER` · hash `0x9DCFF2AFB68B3476` · jhash `0xA08C9141` · **Cliente**

```lua
local retval, p0 = NetworkGetFoundGamer(p1)
```
```c
BOOL NETWORK_GET_FOUND_GAMER(Any* p0, Any p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkGetFriendCount

`NETWORK_GET_FRIEND_COUNT` · hash `0x203F1CFD823B27A4` · jhash `0xA396ACDE` · **Cliente**

```lua
local retval = NetworkGetFriendCount()
```
```c
int NETWORK_GET_FRIEND_COUNT();
```

**Devuelve:** `int`

---
### NetworkGetFriendName

`NETWORK_GET_FRIEND_NAME` · hash `0xE11EBBB2A783FE8B` · jhash `0x97420B6D` · **Cliente**

```lua
local retval = NetworkGetFriendName(friendIndex)
```
```c
char* NETWORK_GET_FRIEND_NAME(int friendIndex);
```

**Parámetros**

- `friendIndex` (`int`)

**Devuelve:** `char*`

---
### NetworkGetFriendNameFromIndex

`_NETWORK_GET_FRIEND_NAME_FROM_INDEX` · hash `0x4164F227D052E293` · **Cliente**

```lua
local retval = NetworkGetFriendNameFromIndex(friendIndex)
```
```c
char* _NETWORK_GET_FRIEND_NAME_FROM_INDEX(int friendIndex);
```

**Parámetros**

- `friendIndex` (`int`)

**Devuelve:** `char*`

---
### NetworkGetGamerStatusFromQueue

`NETWORK_GET_GAMER_STATUS_FROM_QUEUE` · hash `0x2CC848A861D01493` · jhash `0xBEB98840` · **Cliente**

```lua
local retval = NetworkGetGamerStatusFromQueue()
```
```c
BOOL NETWORK_GET_GAMER_STATUS_FROM_QUEUE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2CC848A861D01493` (`N_0x2cc848a861d01493`)

---
### NetworkGetGamerStatusResult

`NETWORK_GET_GAMER_STATUS_RESULT` · hash `0x02A8BEC6FD9AF660` · jhash `0xB5ABC4B4` · **Cliente**

```lua
local retval, p0 = NetworkGetGamerStatusResult(p1)
```
```c
BOOL NETWORK_GET_GAMER_STATUS_RESULT(Any* p0, Any p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x02A8BEC6FD9AF660` (`N_0x02a8bec6fd9af660`)

---
### NetworkGetGamertagFromHandle

`NETWORK_GET_GAMERTAG_FROM_HANDLE` · hash `0x426141162EBE5CDB` · jhash `0xA18A1B26` · **Cliente**

```lua
local retval, networkHandle = NetworkGetGamertagFromHandle(networkHandle)
```
```c
char* NETWORK_GET_GAMERTAG_FROM_HANDLE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `char*`

---
### NetworkGetGlobalMultiplayerClock

`NETWORK_GET_GLOBAL_MULTIPLAYER_CLOCK` · hash `0x6D03BFBD643B2A02` · jhash `0x74E8C53E` · **Cliente**

```lua
local hours, minutes, seconds = NetworkGetGlobalMultiplayerClock()
```
```c
void NETWORK_GET_GLOBAL_MULTIPLAYER_CLOCK(int* hours, int* minutes, int* seconds);
```

**Parámetros**

- `hours` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `minutes` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `seconds` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6D03BFBD643B2A02` (`N_0x6d03bfbd643b2a02`), `_NETWORK_GET_SERVER_TIME` (`NetworkGetServerTime`)

---
### NetworkGetHostOfScript

`NETWORK_GET_HOST_OF_SCRIPT` · hash `0x1D6A14F1F9A736FC` · jhash `0x9C95D0BB` · **Cliente**

```lua
local retval = NetworkGetHostOfScript(scriptName, p1, p2)
```
```c
Player NETWORK_GET_HOST_OF_SCRIPT(char* scriptName, int p1, int p2);
```

**Parámetros**

- `scriptName` (`char*`)
- `p1` (`int`)
- `p2` (`int`)

**Devuelve:** `Player`

**Descripción oficial:**

```
scriptName examples:  
"freemode", "AM_CR_SecurityVan", ...  
Most of the time, these values are used:  
p1 = -1  
p2 = 0  
```

---
### NetworkGetHostOfThisScript

`NETWORK_GET_HOST_OF_THIS_SCRIPT` · hash `0xC7B4D79B01FA7A5C` · jhash `0x89EA7B54` · **Cliente**

```lua
local retval = NetworkGetHostOfThisScript()
```
```c
Player NETWORK_GET_HOST_OF_THIS_SCRIPT();
```

**Devuelve:** `Player`

---
### NetworkGetInstanceIdOfThisScript

`NETWORK_GET_INSTANCE_ID_OF_THIS_SCRIPT` · hash `0x638A3A81733086DB` · jhash `0xDB8B5D71` · **Cliente**

```lua
local retval = NetworkGetInstanceIdOfThisScript()
```
```c
int NETWORK_GET_INSTANCE_ID_OF_THIS_SCRIPT();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x638A3A81733086DB` (`N_0x638a3a81733086db`)

---
### NetworkGetLastVelocityReceived

`_NETWORK_GET_LAST_VELOCITY_RECEIVED` · hash `0x33DE49EDF4DDE77A` · **Cliente**

```lua
local retval = NetworkGetLastVelocityReceived(entity)
```
```c
Vector3 _NETWORK_GET_LAST_VELOCITY_RECEIVED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Used by NetBlender
```

**Nombres antiguos (alias):** `0x33DE49EDF4DDE77A` (`N_0x33de49edf4dde77a`)

---
### NetworkGetLocalHandle

`NETWORK_GET_LOCAL_HANDLE` · hash `0xE86051786B66CD8E` · jhash `0x08023B16` · **Cliente**

```lua
local networkHandle = NetworkGetLocalHandle(bufferSize)
```
```c
void NETWORK_GET_LOCAL_HANDLE(int* networkHandle, int bufferSize);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Retrieves the local player's NetworkHandle* and stores it in the given buffer.  
* Currently unknown struct  
```

---
### NetworkGetLocalSceneFromNetworkId

`NETWORK_GET_LOCAL_SCENE_FROM_NETWORK_ID` · hash `0x02C40BF885C567B6` · jhash `0x16AED87B` · **Cliente**

```lua
local retval = NetworkGetLocalSceneFromNetworkId(netSceneId)
```
```c
int NETWORK_GET_LOCAL_SCENE_FROM_NETWORK_ID(int netSceneId);
```

**Parámetros**

- `netSceneId` (`int`): Network synchronised scene ID (returned by [`NETWORK_CREATE_SYNCHRONISED_SCENE`](#networkcreatesynchronisedscene)).

**Devuelve:** `int` — Local synchronized scene ID. This value can be used with natives such as: [`GET_SYNCHRONIZED_SCENE_PHASE`](PED-1.md#getsynchronizedscenephase), [`GET_SYNCHRONIZED_SCENE_RATE`](PED-1.md#getsynchronizedscenerate), [`IS_SYNCHRONIZED_SCENE_RUNNING`](PED-1.md#issynchronizedscenerunning) and more.

**Descripción oficial:**

Returns a local synchronized scene handle of a networked synchronised scene.

**Nombres antiguos (alias):** `0x02C40BF885C567B6` (`N_0x02c40bf885c567b6`), `_NETWORK_UNLINK_NETWORKED_SYNCHRONISED_SCENE` (`NetworkUnlinkNetworkedSynchronisedScene`), `_NETWORK_CONVERT_SYNCHRONISED_SCENE_TO_SYNCHRONIZED_SCENE` (`NetworkConvertSynchronisedSceneToSynchronizedScene`)

---
### NetworkGetMaxFriends

`NETWORK_GET_MAX_FRIENDS` · hash `0xAFEBB0D5D8F687D2` · jhash `0x048171BC` · **Cliente**

```lua
local retval = NetworkGetMaxFriends()
```
```c
int NETWORK_GET_MAX_FRIENDS();
```

**Devuelve:** `int`

---
### NetworkGetMaxNumParticipants

`NETWORK_GET_MAX_NUM_PARTICIPANTS` · hash `0xA6C90FBC38E395EE` · jhash `0xCCD8C02D` · **Cliente**

```lua
local retval = NetworkGetMaxNumParticipants()
```
```c
int NETWORK_GET_MAX_NUM_PARTICIPANTS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Seems to always return 0, but it's used in quite a few loops.
for (num3 = 0; num3 < NETWORK::0xCCD8C02D(); num3++)
    {
        if (NETWORK::NETWORK_IS_PARTICIPANT_ACTIVE(PLAYER::0x98F3B274(num3)) != 0)
        {
            var num5 = NETWORK::NETWORK_GET_PLAYER_INDEX(PLAYER::0x98F3B274(num3));
```

**Nombres antiguos (alias):** `_NETWORK_GET_NUM_PARTICIPANTS_HOST` (`NetworkGetNumParticipantsHost`)

---
### NetworkGetNetworkIdFromEntity

`NETWORK_GET_NETWORK_ID_FROM_ENTITY` · hash `0xA11700682F3AD45C` · jhash `0x9E35DAB6` · **Cliente**

```lua
local retval = NetworkGetNetworkIdFromEntity(entity)
```
```c
int NETWORK_GET_NETWORK_ID_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): the handle of the entity from which the network id should be taken

**Devuelve:** `int` — The network id of the given entity

**Descripción oficial:**

Get the network id of the given entity

An entity network id represents a given entity for other clients, it's a handle shared between clients, can be reconverted to a client entity handle.\
These (entity network IDs) can and will be reused, the network id will not change.
If you need to refer to an entity across machines (clients, or the server), you should use its network id.

Read more at [Network and local IDs](https://docs.fivem.net/docs/scripting-manual/networking/ids/)

**Ejemplo (lua):**

```lua
local obj = CreateObject(`prop_weed_01`, vector3(0.0, 0.0, 0.0), true)
local netId = NetworkGetNetworkIdFromEntity(obj)
```

**Ejemplo (js):**

```js
let [x, y, z] = GetEntityCoords(PlayerPedId());
let obj = CreateObject(GetHashKey('prop_weed_01'), x, y, z, true);
let netId = NetworkGetNetworkIdFromEntity(obj);
```

**Ejemplo (cs):**

```cs
var obj = CreateObject(GetHashKey('prop_weed_01'), new Vector3(0.0f, 0.0f, 0.0f), true);
var netId = NetworkGetNetworkIdFromEntity(obj);
```

---
### NetworkGetNumBodyTrackers

`_NETWORK_GET_NUM_BODY_TRACKERS` · hash `0xD38C4A6D047C019D` · jhash `0x17CBC608` · **Cliente**

```lua
local retval = NetworkGetNumBodyTrackers()
```
```c
int _NETWORK_GET_NUM_BODY_TRACKERS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xD38C4A6D047C019D` (`N_0xd38c4a6d047c019d`)

---
### NetworkGetNumConnectedPlayers

`NETWORK_GET_NUM_CONNECTED_PLAYERS` · hash `0xA4A79DD2D9600654` · jhash `0xF7952E62` · **Cliente**

```lua
local retval = NetworkGetNumConnectedPlayers()
```
```c
int NETWORK_GET_NUM_CONNECTED_PLAYERS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the amount of players connected in the current session. Only works when connected to a session/server.  
```

---
### NetworkGetNumFoundGamers

`NETWORK_GET_NUM_FOUND_GAMERS` · hash `0xA1B043EE79A916FB` · jhash `0xF4B80C7E` · **Cliente**

```lua
local retval = NetworkGetNumFoundGamers()
```
```c
int NETWORK_GET_NUM_FOUND_GAMERS();
```

**Devuelve:** `int`

---
### NetworkGetNumParticipants

`NETWORK_GET_NUM_PARTICIPANTS` · hash `0x18D0456E86604654` · jhash `0x3E25A3C5` · **Cliente**

```lua
local retval = NetworkGetNumParticipants()
```
```c
int NETWORK_GET_NUM_PARTICIPANTS();
```

**Devuelve:** `int`

---
### NetworkGetNumPresenceInvites

`NETWORK_GET_NUM_PRESENCE_INVITES` · hash `0xCEFA968912D0F78D` · jhash `0x3FDA00F3` · **Cliente**

```lua
local retval = NetworkGetNumPresenceInvites()
```
```c
int NETWORK_GET_NUM_PRESENCE_INVITES();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xCEFA968912D0F78D` (`N_0xcefa968912d0f78d`)

---
### NetworkGetNumScriptParticipants

`NETWORK_GET_NUM_SCRIPT_PARTICIPANTS` · hash `0x3658E8CD94FC121A` · jhash `0x8F7D9F46` · **Cliente**

```lua
local retval, p0 = NetworkGetNumScriptParticipants(p1, p2)
```
```c
int NETWORK_GET_NUM_SCRIPT_PARTICIPANTS(Any* p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x3658E8CD94FC121A` (`N_0x3658e8cd94fc121a`)

---
### NetworkGetNumUnackedForPlayer

`_NETWORK_GET_NUM_UNACKED_FOR_PLAYER` · hash `0xFF8FCF9FFC458A1C` · **Cliente**

```lua
local retval = NetworkGetNumUnackedForPlayer(player)
```
```c
int _NETWORK_GET_NUM_UNACKED_FOR_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkGetOldestResendCountForPlayer

`_NETWORK_GET_OLDEST_RESEND_COUNT_FOR_PLAYER` · hash `0x52C1EADAF7B10302` · **Cliente**

```lua
local retval = NetworkGetOldestResendCountForPlayer(player)
```
```c
int _NETWORK_GET_OLDEST_RESEND_COUNT_FOR_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Descripción oficial:**

```
NETWORK_GET_*

NativeDB Introduced: v323
```

---
### NetworkGetParticipantIndex

`NETWORK_GET_PARTICIPANT_INDEX` · hash `0x1B84DF6AF2A46938` · jhash `0xC4D91094` · **Cliente**

```lua
local retval = NetworkGetParticipantIndex(index)
```
```c
int NETWORK_GET_PARTICIPANT_INDEX(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `int`

---
### NetworkGetPlatformPartyMembers

`NETWORK_GET_PLATFORM_PARTY_MEMBERS` · hash `0x120364DE2845DAF8` · jhash `0xF30E5814` · **Cliente**

```lua
local retval, data = NetworkGetPlatformPartyMembers(dataSize)
```
```c
int NETWORK_GET_PLATFORM_PARTY_MEMBERS(Any* data, int dataSize);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `dataSize` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x120364DE2845DAF8` (`N_0x120364de2845daf8`)

---
### NetworkGetPlatformPartyUnk

`_NETWORK_GET_PLATFORM_PARTY_UNK` · hash `0x01ABCE5E7CBDA196` · **Cliente**

```lua
local retval = NetworkGetPlatformPartyUnk()
```
```c
int _NETWORK_GET_PLATFORM_PARTY_UNK();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x01ABCE5E7CBDA196` (`N_0x01abce5e7cbda196`)

---
### NetworkGetPlayerCoords

`_NETWORK_GET_PLAYER_COORDS` · hash `0x125E6D638B8605D4` · **Cliente**

```lua
local retval = NetworkGetPlayerCoords(player)
```
```c
Vector3 _NETWORK_GET_PLAYER_COORDS(Player player);
```

**Parámetros**

- `player` (`Player`): The player id, MUST be another player.

**Devuelve:** `Vector3` — A Vector3 containing the coordinates of another player.

**Descripción oficial:**

Returns the coordinates of another player.

Does not work if you enter your own player id as p0 (will return `(0.0, 0.0, 0.0)` in that case).

**Nombres antiguos (alias):** `0x125E6D638B8605D4` (`N_0x125e6d638b8605d4`)

---
### NetworkGetPlayerFromGamerHandle

`NETWORK_GET_PLAYER_FROM_GAMER_HANDLE` · hash `0xCE5F689CF5A0A49D` · jhash `0x2E96EF1E` · **Cliente**

```lua
local retval, networkHandle = NetworkGetPlayerFromGamerHandle(networkHandle)
```
```c
Player NETWORK_GET_PLAYER_FROM_GAMER_HANDLE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Player`

---
### NetworkGetPlayerIndex

`NETWORK_GET_PLAYER_INDEX` · hash `0x24FB80D107371267` · jhash `0xBE1C1506` · **Cliente**

```lua
local retval = NetworkGetPlayerIndex(player)
```
```c
int NETWORK_GET_PLAYER_INDEX(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### NetworkGetPlayerIndexFromPed

`NETWORK_GET_PLAYER_INDEX_FROM_PED` · hash `0x6C0E2E0125610278` · jhash `0x40DBF464` · **Cliente**

```lua
local retval = NetworkGetPlayerIndexFromPed(ped)
```
```c
Player NETWORK_GET_PLAYER_INDEX_FROM_PED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Player`

**Descripción oficial:**

```
Returns the Player associated to a given Ped when in an online session.  
```

**Nombres antiguos (alias):** `0x6C0E2E0125610278` (`N_0x6c0e2e0125610278`)

---
### NetworkGetPlayerLoudness

`NETWORK_GET_PLAYER_LOUDNESS` · hash `0x21A1684A25C2867F` · jhash `0xF2F67014` · **Cliente**

```lua
local retval = NetworkGetPlayerLoudness(player)
```
```c
float NETWORK_GET_PLAYER_LOUDNESS(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

---
### NetworkGetPlayerOwnsWaypoint

`NETWORK_GET_PLAYER_OWNS_WAYPOINT` · hash `0x82377B65E943F72D` · jhash `0xB802B671` · **Cliente**

```lua
local retval = NetworkGetPlayerOwnsWaypoint(player)
```
```c
BOOL NETWORK_GET_PLAYER_OWNS_WAYPOINT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x82377B65E943F72D` (`N_0x82377b65e943f72d`)

---
### NetworkGetPlayerTutorialSessionInstance

`NETWORK_GET_PLAYER_TUTORIAL_SESSION_INSTANCE` · hash `0x3B39236746714134` · jhash `0x5E1020CC` · **Cliente**

```lua
local retval = NetworkGetPlayerTutorialSessionInstance(player)
```
```c
int NETWORK_GET_PLAYER_TUTORIAL_SESSION_INSTANCE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x3B39236746714134` (`N_0x3b39236746714134`)

---
### NetworkGetPositionHashOfThisScript

`_NETWORK_GET_POSITION_HASH_OF_THIS_SCRIPT` · hash `0x257ED0FADF750BCF` · **Cliente**

```lua
local retval = NetworkGetPositionHashOfThisScript()
```
```c
Any _NETWORK_GET_POSITION_HASH_OF_THIS_SCRIPT();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x257ED0FADF750BCF` (`N_0x257ed0fadf750bcf`)

---
### NetworkGetPresenceInviteContentId

`NETWORK_GET_PRESENCE_INVITE_CONTENT_ID` · hash `0x24409FC4C55CB22D` · jhash `0xA4302183` · **Cliente**

```lua
local retval = NetworkGetPresenceInviteContentId(p0)
```
```c
char* NETWORK_GET_PRESENCE_INVITE_CONTENT_ID(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x24409FC4C55CB22D` (`N_0x24409fc4c55cb22d`)

---
### NetworkGetPresenceInviteFromAdmin

`NETWORK_GET_PRESENCE_INVITE_FROM_ADMIN` · hash `0x3DBF2DF0AEB7D289` · jhash `0xF5E3401C` · **Cliente**

```lua
local retval = NetworkGetPresenceInviteFromAdmin(p0)
```
```c
BOOL NETWORK_GET_PRESENCE_INVITE_FROM_ADMIN(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3DBF2DF0AEB7D289` (`N_0x3dbf2df0aeb7d289`)

---
### NetworkGetPresenceInviteHandle

`NETWORK_GET_PRESENCE_INVITE_HANDLE` · hash `0x38D5B0FEBB086F75` · jhash `0xB2451429` · **Cliente**

```lua
local retval, p1 = NetworkGetPresenceInviteHandle(p0, p1)
```
```c
BOOL NETWORK_GET_PRESENCE_INVITE_HANDLE(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkGetPresenceInviteId

`NETWORK_GET_PRESENCE_INVITE_ID` · hash `0xDFF09646E12EC386` · jhash `0xD50DF46C` · **Cliente**

```lua
local retval = NetworkGetPresenceInviteId(p0)
```
```c
Any NETWORK_GET_PRESENCE_INVITE_ID(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xDFF09646E12EC386` (`N_0xdff09646e12ec386`)

---
### NetworkGetPresenceInviteInviter

`NETWORK_GET_PRESENCE_INVITE_INVITER` · hash `0x4962CC4AA2F345B7` · jhash `0x19EC65D9` · **Cliente**

```lua
local retval = NetworkGetPresenceInviteInviter(inviteIndex)
```
```c
char* NETWORK_GET_PRESENCE_INVITE_INVITER(int inviteIndex);
```

**Parámetros**

- `inviteIndex` (`int`)

**Devuelve:** `char*` — The Name of the inviter.

**Descripción oficial:**

Returns the Name of the inviter of the specific selected Invite.

**Nombres antiguos (alias):** `0x4962CC4AA2F345B7` (`N_0x4962cc4aa2f345b7`)

---
### NetworkGetPresenceInviteIsTournament

`NETWORK_GET_PRESENCE_INVITE_IS_TOURNAMENT` · hash `0x8806CEBFABD3CE05` · jhash `0x7D593B4C` · **Cliente**

```lua
local retval = NetworkGetPresenceInviteIsTournament(p0)
```
```c
BOOL NETWORK_GET_PRESENCE_INVITE_IS_TOURNAMENT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8806CEBFABD3CE05` (`N_0x8806cebfabd3ce05`)

---
### NetworkGetPresenceInvitePlaylistCurrent

`NETWORK_GET_PRESENCE_INVITE_PLAYLIST_CURRENT` · hash `0x728C4CC7920CD102` · jhash `0x4677C656` · **Cliente**

```lua
local retval = NetworkGetPresenceInvitePlaylistCurrent(p0)
```
```c
Any NETWORK_GET_PRESENCE_INVITE_PLAYLIST_CURRENT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x728C4CC7920CD102` (`N_0x728c4cc7920cd102`)

---
### NetworkGetPresenceInvitePlaylistLength

`NETWORK_GET_PRESENCE_INVITE_PLAYLIST_LENGTH` · hash `0xD39B3FFF8FFDD5BF` · jhash `0x51B2D848` · **Cliente**

```lua
local retval = NetworkGetPresenceInvitePlaylistLength(p0)
```
```c
Any NETWORK_GET_PRESENCE_INVITE_PLAYLIST_LENGTH(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xD39B3FFF8FFDD5BF` (`N_0xd39b3fff8ffdd5bf`)

---
### NetworkGetPresenceInviteSessionId

`NETWORK_GET_PRESENCE_INVITE_SESSION_ID` · hash `0x26E1CD96B0903D60` · jhash `0xC5E0C989` · **Cliente**

```lua
local retval = NetworkGetPresenceInviteSessionId(inviteIndex)
```
```c
Hash NETWORK_GET_PRESENCE_INVITE_SESSION_ID(int inviteIndex);
```

**Parámetros**

- `inviteIndex` (`int`)

**Devuelve:** `Hash` — A hash of the session id.

**Descripción oficial:**

The Native returns a hash of the session id as string from the specific invite index!

**Nombres antiguos (alias):** `0x26E1CD96B0903D60` (`N_0x26e1cd96b0903d60`)

---
### NetworkGetPrimaryClanDataCancel

`NETWORK_GET_PRIMARY_CLAN_DATA_CANCEL` · hash `0x042E4B70B93E6054` · jhash `0x455DDF5C` · **Cliente**

```lua
NetworkGetPrimaryClanDataCancel()
```
```c
void NETWORK_GET_PRIMARY_CLAN_DATA_CANCEL();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x042E4B70B93E6054` (`N_0x042e4b70b93e6054`)

---
### NetworkGetPrimaryClanDataClear

`NETWORK_GET_PRIMARY_CLAN_DATA_CLEAR` · hash `0x9AA46BADAD0E27ED` · jhash `0xE22445DA` · **Cliente**

```lua
local retval = NetworkGetPrimaryClanDataClear()
```
```c
Any NETWORK_GET_PRIMARY_CLAN_DATA_CLEAR();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x9AA46BADAD0E27ED` (`N_0x9aa46badad0e27ed`)

---
### NetworkGetPrimaryClanDataNew

`NETWORK_GET_PRIMARY_CLAN_DATA_NEW` · hash `0xC080FF658B2E41DA` · jhash `0x9B8631EB` · **Cliente**

```lua
local retval, p0, p1 = NetworkGetPrimaryClanDataNew()
```
```c
BOOL NETWORK_GET_PRIMARY_CLAN_DATA_NEW(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### NetworkGetPrimaryClanDataPending

`NETWORK_GET_PRIMARY_CLAN_DATA_PENDING` · hash `0xB5074DB804E28CE7` · jhash `0xA4EF02F3` · **Cliente**

```lua
local retval = NetworkGetPrimaryClanDataPending()
```
```c
Any NETWORK_GET_PRIMARY_CLAN_DATA_PENDING();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xB5074DB804E28CE7` (`N_0xb5074db804e28ce7`)

---
### NetworkGetPrimaryClanDataStart

`NETWORK_GET_PRIMARY_CLAN_DATA_START` · hash `0xCE86D8191B762107` · jhash `0x89DB0EC7` · **Cliente**

```lua
local retval, p0 = NetworkGetPrimaryClanDataStart(p1)
```
```c
BOOL NETWORK_GET_PRIMARY_CLAN_DATA_START(Any* p0, Any p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkGetPrimaryClanDataSuccess

`NETWORK_GET_PRIMARY_CLAN_DATA_SUCCESS` · hash `0x5B4F04F19376A0BA` · jhash `0x068A054E` · **Cliente**

```lua
local retval = NetworkGetPrimaryClanDataSuccess()
```
```c
Any NETWORK_GET_PRIMARY_CLAN_DATA_SUCCESS();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x5B4F04F19376A0BA` (`N_0x5b4f04f19376a0ba`)

---
### NetworkGetRandomInt

`NETWORK_GET_RANDOM_INT` · hash `0x599E4FA1F87EB5FF` · jhash `0x208DD848` · **Cliente**

```lua
local retval = NetworkGetRandomInt()
```
```c
int NETWORK_GET_RANDOM_INT();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x599E4FA1F87EB5FF` (`N_0x599e4fa1f87eb5ff`)

---
### NetworkGetRandomIntRanged

`NETWORK_GET_RANDOM_INT_RANGED` · hash `0xE30CF56F1EFA5F43` · jhash `0xF9B6426D` · **Cliente**

```lua
local retval = NetworkGetRandomIntRanged(rangeStart, rangeEnd)
```
```c
int NETWORK_GET_RANDOM_INT_RANGED(int rangeStart, int rangeEnd);
```

**Parámetros**

- `rangeStart` (`int`)
- `rangeEnd` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Same as GET_RANDOM_INT_IN_RANGE
```

**Nombres antiguos (alias):** `0xE30CF56F1EFA5F43` (`N_0xe30cf56f1efa5f43`), `_NETWORK_GET_RANDOM_INT_IN_RANGE` (`NetworkGetRandomIntInRange`)

---
### NetworkGetRespawnResult

`NETWORK_GET_RESPAWN_RESULT` · hash `0x371EA43692861CF1` · jhash `0xDDFE9FBC` · **Cliente**

```lua
local coordinates, heading = NetworkGetRespawnResult(randomInt)
```
```c
void NETWORK_GET_RESPAWN_RESULT(int randomInt, Vector3* coordinates, float* heading);
```

**Parámetros**

- `randomInt` (`int`)
- `coordinates` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `heading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Based on scripts such as in freemode.c how they call their vars vVar and fVar the 2nd and 3rd param it a Vector3 and Float, but the first is based on get_random_int_in_range..  
```

---
### NetworkGetRespawnResultFlags

`NETWORK_GET_RESPAWN_RESULT_FLAGS` · hash `0x6C34F1208B8923FD` · jhash `0x03287FD2` · **Cliente**

```lua
local retval = NetworkGetRespawnResultFlags(p0)
```
```c
Any NETWORK_GET_RESPAWN_RESULT_FLAGS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x6C34F1208B8923FD` (`N_0x6c34f1208b8923fd`)

---
### NetworkGetRosPrivilege_24

`_NETWORK_GET_ROS_PRIVILEGE_24` · hash `0x593570C289A77688` · **Cliente**

```lua
local retval = NetworkGetRosPrivilege_24()
```
```c
BOOL _NETWORK_GET_ROS_PRIVILEGE_24();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x593570C289A77688` (`N_0x593570c289a77688`)

---
### NetworkGetRosPrivilege_25

`_NETWORK_GET_ROS_PRIVILEGE_25` · hash `0x91B87C55093DE351` · **Cliente**

```lua
local retval = NetworkGetRosPrivilege_25()
```
```c
BOOL _NETWORK_GET_ROS_PRIVILEGE_25();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x91B87C55093DE351` (`N_0x91b87c55093de351`)

---
### NetworkGetRosPrivilege_9

`_NETWORK_GET_ROS_PRIVILEGE_9` · hash `0x66B59CFFD78467AF` · jhash `0x0CA1167F` · **Cliente**

```lua
local retval = NetworkGetRosPrivilege_9()
```
```c
BOOL _NETWORK_GET_ROS_PRIVILEGE_9();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x66B59CFFD78467AF` (`N_0x66b59cffd78467af`)

---
### NetworkGetScriptStatus

`NETWORK_GET_SCRIPT_STATUS` · hash `0x57D158647A6BFABF` · jhash `0x2BE9235A` · **Cliente**

```lua
local retval = NetworkGetScriptStatus()
```
```c
int NETWORK_GET_SCRIPT_STATUS();
```

**Devuelve:** `int`

---
### NetworkGetTalkerProximity

`NETWORK_GET_TALKER_PROXIMITY` · hash `0x84F0F13120B4E098` · jhash `0x19991ADD` · **Cliente**

```lua
local retval = NetworkGetTalkerProximity()
```
```c
float NETWORK_GET_TALKER_PROXIMITY();
```

**Devuelve:** `float`

---
### NetworkGetTargetingMode

`_NETWORK_GET_TARGETING_MODE` · hash `0xDFFA5BE8381C3314` · **Cliente**

```lua
local retval = NetworkGetTargetingMode()
```
```c
int _NETWORK_GET_TARGETING_MODE();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xDFFA5BE8381C3314` (`N_0xdffa5be8381c3314`)

---
### NetworkGetThisScriptIsNetworkScript

`NETWORK_GET_THIS_SCRIPT_IS_NETWORK_SCRIPT` · hash `0x2910669969E9535E` · jhash `0xD9BF6549` · **Cliente**

```lua
local retval = NetworkGetThisScriptIsNetworkScript()
```
```c
BOOL NETWORK_GET_THIS_SCRIPT_IS_NETWORK_SCRIPT();
```

**Devuelve:** `BOOL`

---
### NetworkGetTimeoutTime

`NETWORK_GET_TIMEOUT_TIME` · hash `0x5ED0356A0CE3A34F` · jhash `0xE1F86C6A` · **Cliente**

```lua
local retval = NetworkGetTimeoutTime()
```
```c
int NETWORK_GET_TIMEOUT_TIME();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x5ED0356A0CE3A34F` (`N_0x5ed0356a0ce3a34f`)

---
### NetworkGetTotalNumPlayers

`NETWORK_GET_TOTAL_NUM_PLAYERS` · hash `0xCF61D4B4702EE9EB` · jhash `0xF4F13B06` · **Cliente**

```lua
local retval = NetworkGetTotalNumPlayers()
```
```c
int NETWORK_GET_TOTAL_NUM_PLAYERS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xCF61D4B4702EE9EB` (`N_0xcf61d4b4702ee9eb`)

---
### NetworkGetTransitionHost

`NETWORK_GET_TRANSITION_HOST` · hash `0x65042B9774C4435E` · jhash `0x73098D40` · **Cliente**

```lua
local retval, networkHandle = NetworkGetTransitionHost(networkHandle)
```
```c
BOOL NETWORK_GET_TRANSITION_HOST(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkGetTransitionMembers

`NETWORK_GET_TRANSITION_MEMBERS` · hash `0x73B000F7FBC55829` · jhash `0x31F19263` · **Cliente**

```lua
local retval, data = NetworkGetTransitionMembers(dataCount)
```
```c
int NETWORK_GET_TRANSITION_MEMBERS(Any* data, int dataCount);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `dataCount` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns count.
```

---
### NetworkGetTunableCloudCrc

`NETWORK_GET_TUNABLE_CLOUD_CRC` · hash `0x10BD227A753B0D84` · jhash `0x231CFD12` · **Cliente**

```lua
local retval = NetworkGetTunableCloudCrc()
```
```c
int NETWORK_GET_TUNABLE_CLOUD_CRC();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Actually returns the version (TUNABLE_VERSION)
```

**Nombres antiguos (alias):** `0x10BD227A753B0D84` (`N_0x10bd227a753b0d84`), `_NETWORK_GET_TUNABLES_VERSION` (`NetworkGetTunablesVersion`)

---
### NetworkGetUnreliableResendCountForPlayer

`_NETWORK_GET_UNRELIABLE_RESEND_COUNT_FOR_PLAYER` · hash `0x3765C3A3E8192E10` · **Cliente**

```lua
local retval = NetworkGetUnreliableResendCountForPlayer(player)
```
```c
int _NETWORK_GET_UNRELIABLE_RESEND_COUNT_FOR_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Descripción oficial:**

```
NETWORK_*

NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x3765C3A3E8192E10` (`N_0x3765c3a3e8192e10`)

---
### NetworkHandleFromFriend

`NETWORK_HANDLE_FROM_FRIEND` · hash `0xD45CB817D7E177D2` · jhash `0x3B0BB3A3` · **Cliente**

```lua
local networkHandle = NetworkHandleFromFriend(friendIndex, bufferSize)
```
```c
void NETWORK_HANDLE_FROM_FRIEND(int friendIndex, int* networkHandle, int bufferSize);
```

**Parámetros**

- `friendIndex` (`int`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `void`

---
### NetworkHandleFromMemberId

`NETWORK_HANDLE_FROM_MEMBER_ID` · hash `0xA0FD21BED61E5C4C` · jhash `0x9BFC9FE2` · **Cliente**

```lua
local networkHandle = NetworkHandleFromMemberId(memberId, bufferSize)
```
```c
void NETWORK_HANDLE_FROM_MEMBER_ID(char* memberId, int* networkHandle, int bufferSize);
```

**Parámetros**

- `memberId` (`char*`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Returns a NetworkHandle* from the specified member ID and stores it in a given buffer.  
* Currently unknown struct  
```

---
### NetworkHandleFromPlayer

`NETWORK_HANDLE_FROM_PLAYER` · hash `0x388EB2B86C73B6B3` · jhash `0xD3498917` · **Cliente**

```lua
local networkHandle = NetworkHandleFromPlayer(player, bufferSize)
```
```c
void NETWORK_HANDLE_FROM_PLAYER(Player player, int* networkHandle, int bufferSize);
```

**Parámetros**

- `player` (`Player`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Returns a handle to networkHandle* from the specified player handle and stores it in a given buffer.  
* Currently unknown struct  
Example:  
std::vector<UINT64> GetPlayerNetworkHandle(Player player) {  
    const int size = 13;  
    uint64_t *buffer = std::make_unique<uint64_t[]>(size).get();  
    NETWORK::NETWORK_HANDLE_FROM_PLAYER(player, reinterpret_cast<int *>(buffer), 13);  
    for (int i = 0; i < size; i++) {  
        Log::Msg("networkhandle[%i]: %llx", i, buffer[i]);  
    }  
    std::vector<UINT64> result(buffer, buffer + sizeof(buffer));  
    return result;  
}  
```

---
### NetworkHandleFromUserId

`NETWORK_HANDLE_FROM_USER_ID` · hash `0xDCD51DD8F87AEC5C` · jhash `0x74C2C1B7` · **Cliente**

```lua
local networkHandle = NetworkHandleFromUserId(userId, bufferSize)
```
```c
void NETWORK_HANDLE_FROM_USER_ID(char* userId, int* networkHandle, int bufferSize);
```

**Parámetros**

- `userId` (`char*`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Returns a NetworkHandle* from the specified user ID and stores it in a given buffer.  
* Currently unknown struct  
```

---
### NetworkHasAgeRestrictedProfile

`_NETWORK_HAS_AGE_RESTRICTED_PROFILE` · hash `0x1353F87E89946207` · **Cliente**

```lua
local retval = NetworkHasAgeRestrictedProfile()
```
```c
BOOL _NETWORK_HAS_AGE_RESTRICTED_PROFILE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1353F87E89946207` (`N_0x1353f87e89946207`)

---
### NetworkHasCachedPlayerHeadBlendData

`NETWORK_HAS_CACHED_PLAYER_HEAD_BLEND_DATA` · hash `0x237D5336A9A54108` · jhash `0x7B2A0337` · **Cliente**

```lua
local retval = NetworkHasCachedPlayerHeadBlendData(player)
```
```c
BOOL NETWORK_HAS_CACHED_PLAYER_HEAD_BLEND_DATA(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x237D5336A9A54108` (`N_0x237d5336a9a54108`)

---
### NetworkHasControlOfDoor

`NETWORK_HAS_CONTROL_OF_DOOR` · hash `0xCB3C68ADB06195DF` · jhash `0x136326EC` · **Cliente**

```lua
local retval = NetworkHasControlOfDoor(doorHash)
```
```c
BOOL NETWORK_HAS_CONTROL_OF_DOOR(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### NetworkHasControlOfEntity

`NETWORK_HAS_CONTROL_OF_ENTITY` · hash `0x01BF60A500E28887` · jhash `0x005FD797` · **Cliente**

```lua
local retval = NetworkHasControlOfEntity(entity)
```
```c
BOOL NETWORK_HAS_CONTROL_OF_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### NetworkHasControlOfNetworkId

`NETWORK_HAS_CONTROL_OF_NETWORK_ID` · hash `0x4D36070FE0215186` · jhash `0x92E77D21` · **Cliente**

```lua
local retval = NetworkHasControlOfNetworkId(netId)
```
```c
BOOL NETWORK_HAS_CONTROL_OF_NETWORK_ID(int netId);
```

**Parámetros**

- `netId` (`int`)

**Devuelve:** `BOOL`

---
### NetworkHasControlOfPickup

`NETWORK_HAS_CONTROL_OF_PICKUP` · hash `0x5BC9495F0B3B6FA6` · jhash `0xF7784FC8` · **Cliente**

```lua
local retval = NetworkHasControlOfPickup(pickup)
```
```c
BOOL NETWORK_HAS_CONTROL_OF_PICKUP(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `BOOL`

---
### NetworkHasEntityBeenRegisteredWithThisThread

`NETWORK_HAS_ENTITY_BEEN_REGISTERED_WITH_THIS_THREAD` · hash `0xB07D3185E11657A5` · jhash `0xEDA68956` · **Cliente**

```lua
local retval = NetworkHasEntityBeenRegisteredWithThisThread(entity)
```
```c
BOOL NETWORK_HAS_ENTITY_BEEN_REGISTERED_WITH_THIS_THREAD(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB07D3185E11657A5` (`N_0xb07d3185e11657a5`)

---
### NetworkHasFollowInvite

`NETWORK_HAS_FOLLOW_INVITE` · hash `0x76D9B976C4C09FDE` · jhash `0xE96CFE7D` · **Cliente**

```lua
local retval = NetworkHasFollowInvite()
```
```c
BOOL NETWORK_HAS_FOLLOW_INVITE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x76D9B976C4C09FDE` (`N_0x76d9b976c4c09fde`)

---
### NetworkHasGameBeenAltered

`_NETWORK_HAS_GAME_BEEN_ALTERED` · hash `0x659CF2EF7F550C4F` · **Cliente**

```lua
local retval = NetworkHasGameBeenAltered()
```
```c
BOOL _NETWORK_HAS_GAME_BEEN_ALTERED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if dinput8.dll is present in the game directory.
You will get following error message if that is true: "You are attempting to access GTA Online servers with an altered version of the game."
```

**Nombres antiguos (alias):** `0x659CF2EF7F550C4F` (`N_0x659cf2ef7f550c4f`)

---
### NetworkHasHeadset

`NETWORK_HAS_HEADSET` · hash `0xE870F9F1F7B4F1FA` · jhash `0xA7DC5657` · **Cliente**

```lua
local retval = NetworkHasHeadset()
```
```c
BOOL NETWORK_HAS_HEADSET();
```

**Devuelve:** `BOOL`

---
### NetworkHasInviteBeenAcked

`NETWORK_HAS_INVITE_BEEN_ACKED` · hash `0x71DC455F5CD1C2B1` · jhash `0xF6F9D1B9` · **Cliente**

```lua
local retval, networkHandle = NetworkHasInviteBeenAcked(networkHandle)
```
```c
BOOL NETWORK_HAS_INVITE_BEEN_ACKED(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x71DC455F5CD1C2B1` (`N_0x71dc455f5cd1c2b1`)

---
### NetworkHasInvitedGamer

`NETWORK_HAS_INVITED_GAMER` · hash `0x4D86CD31E8976ECE` · jhash `0xEC651BC0` · **Cliente**

```lua
local retval, p0 = NetworkHasInvitedGamer(p0)
```
```c
BOOL NETWORK_HAS_INVITED_GAMER(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkHasInvitedGamerToTransition

`NETWORK_HAS_INVITED_GAMER_TO_TRANSITION` · hash `0x7284A47B3540E6CF` · jhash `0x4F41DF6B` · **Cliente**

```lua
local retval, p0 = NetworkHasInvitedGamerToTransition(p0)
```
```c
BOOL NETWORK_HAS_INVITED_GAMER_TO_TRANSITION(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkHasPendingInvite

`NETWORK_HAS_PENDING_INVITE` · hash `0xAC8C7B9B88C4A668` · jhash `0x0C207D6E` · **Cliente**

```lua
local retval = NetworkHasPendingInvite()
```
```c
BOOL NETWORK_HAS_PENDING_INVITE();
```

**Devuelve:** `BOOL`

---
### NetworkHasPlayerStartedTransition

`NETWORK_HAS_PLAYER_STARTED_TRANSITION` · hash `0x9AC9CCBFA8C29795` · jhash `0x4ABD1E59` · **Cliente**

```lua
local retval = NetworkHasPlayerStartedTransition(player)
```
```c
BOOL NETWORK_HAS_PLAYER_STARTED_TRANSITION(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkHasReceivedHostBroadcastData

`NETWORK_HAS_RECEIVED_HOST_BROADCAST_DATA` · hash `0x5D10B3795F3FC886` · jhash `0x0B739F53` · **Cliente**

```lua
local retval = NetworkHasReceivedHostBroadcastData()
```
```c
BOOL NETWORK_HAS_RECEIVED_HOST_BROADCAST_DATA();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5D10B3795F3FC886` (`N_0x5d10b3795f3fc886`)

---
### NetworkHasRosPrivilege

`NETWORK_HAS_ROS_PRIVILEGE` · hash `0xA699957E60D80214` · jhash `0xFD261E30` · **Cliente**

```lua
local retval = NetworkHasRosPrivilege(index)
```
```c
BOOL NETWORK_HAS_ROS_PRIVILEGE(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
index is always 18 in scripts
```

**Nombres antiguos (alias):** `0xA699957E60D80214` (`N_0xa699957e60d80214`)

---
### NetworkHasRosPrivilegeEndDate

`NETWORK_HAS_ROS_PRIVILEGE_END_DATE` · hash `0xC22912B1D85F26B1` · jhash `0x8570DD34` · **Cliente**

```lua
local retval, banType, timeData = NetworkHasRosPrivilegeEndDate(privilege)
```
```c
BOOL NETWORK_HAS_ROS_PRIVILEGE_END_DATE(int privilege, int* banType, Vector3* timeData);
```

**Parámetros**

- `privilege` (`int`)
- `banType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `timeData` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC22912B1D85F26B1` (`N_0xc22912b1d85f26b1`), `_NETWORK_GET_BAN_DATA` (`NetworkGetBanData`)

---
### NetworkHasSocialClubAccount

`NETWORK_HAS_SOCIAL_CLUB_ACCOUNT` · hash `0x67A5589628E0CFF6` · jhash `0x66EC713F` · **Cliente**

```lua
local retval = NetworkHasSocialClubAccount()
```
```c
BOOL NETWORK_HAS_SOCIAL_CLUB_ACCOUNT();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x67A5589628E0CFF6` (`N_0x67a5589628e0cff6`)

---
### NetworkHasSocialNetworkingSharingPriv

`NETWORK_HAS_SOCIAL_NETWORKING_SHARING_PRIV` · hash `0x76BF03FADBF154F5` · jhash `0xEB864288` · **Cliente**

```lua
local retval = NetworkHasSocialNetworkingSharingPriv()
```
```c
BOOL NETWORK_HAS_SOCIAL_NETWORKING_SHARING_PRIV();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x76BF03FADBF154F5` (`N_0x76bf03fadbf154f5`)

---
### NetworkHasTransitionInviteBeenAcked

`NETWORK_HAS_TRANSITION_INVITE_BEEN_ACKED` · hash `0x3F9990BF5F22759C` · jhash `0x00F26CDC` · **Cliente**

```lua
local retval, networkHandle = NetworkHasTransitionInviteBeenAcked(networkHandle)
```
```c
BOOL NETWORK_HAS_TRANSITION_INVITE_BEEN_ACKED(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3F9990BF5F22759C` (`N_0x3f9990bf5f22759c`)

---
### NetworkHasValidRosCredentials

`NETWORK_HAS_VALID_ROS_CREDENTIALS` · hash `0x85443FF4C328F53B` · jhash `0x3FB40673` · **Cliente**

```lua
local retval = NetworkHasValidRosCredentials()
```
```c
BOOL NETWORK_HAS_VALID_ROS_CREDENTIALS();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the signed-in user has valid Rockstar Online Services (ROS) credentials.
```

**Nombres antiguos (alias):** `0x85443FF4C328F53B` (`N_0x85443ff4c328f53b`), `_NETWORK_ARE_ROS_AVAILABLE` (`NetworkAreRosAvailable`), `NETWORK_HAVE_JUST_UPLOAD_LATER` (`NetworkHaveJustUploadLater`)

---
### NetworkHasViewGamerUserContentResult

`_NETWORK_HAS_VIEW_GAMER_USER_CONTENT_RESULT` · hash `0xCCA4318E1AB03F1F` · **Cliente**

```lua
local retval, networkHandle = NetworkHasViewGamerUserContentResult(networkHandle)
```
```c
BOOL _NETWORK_HAS_VIEW_GAMER_USER_CONTENT_RESULT(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCCA4318E1AB03F1F` (`N_0xcca4318e1ab03f1f`)

---
### NetworkHashFromGamerHandle

`NETWORK_HASH_FROM_GAMER_HANDLE` · hash `0x58575AC3CF2CA8EC` · jhash `0x5AC9F04D` · **Cliente**

```lua
local retval, networkHandle = NetworkHashFromGamerHandle(networkHandle)
```
```c
Hash NETWORK_HASH_FROM_GAMER_HANDLE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0x58575AC3CF2CA8EC` (`N_0x58575ac3cf2ca8ec`), `_NETWORK_HASH_FROM_GAMER_HANDLE` (`NetworkHashFromGamerHandle`)

---
### NetworkHashFromPlayerHandle

`NETWORK_HASH_FROM_PLAYER_HANDLE` · hash `0xBC1D768F2F5D6C05` · jhash `0xF8D7AF3B` · **Cliente**

```lua
local retval = NetworkHashFromPlayerHandle(player)
```
```c
Hash NETWORK_HASH_FROM_PLAYER_HANDLE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0xBC1D768F2F5D6C05` (`N_0xbc1d768f2f5d6c05`), `_NETWORK_HASH_FROM_PLAYER_HANDLE` (`NetworkHashFromPlayerHandle`)

---
### NetworkHaveCommunicationPrivileges

`NETWORK_HAVE_COMMUNICATION_PRIVILEGES` · hash `0xAEEF48CDF5B6CE7C` · jhash `0x2D817A5E` · **Cliente**

```lua
local retval = NetworkHaveCommunicationPrivileges(p0, player)
```
```c
BOOL NETWORK_HAVE_COMMUNICATION_PRIVILEGES(int p0, Player player);
```

**Parámetros**

- `p0` (`int`)
- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xAEEF48CDF5B6CE7C` (`N_0xaeef48cdf5b6ce7c`)

---
### NetworkHaveOnlinePrivilege_2

`_NETWORK_HAVE_ONLINE_PRIVILEGE_2` · hash `0x5EA784D197556507` · **Cliente**

```lua
local retval = NetworkHaveOnlinePrivilege_2()
```
```c
BOOL _NETWORK_HAVE_ONLINE_PRIVILEGE_2();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5EA784D197556507` (`N_0x5ea784d197556507`)

---
### NetworkHaveOnlinePrivileges

`NETWORK_HAVE_ONLINE_PRIVILEGES` · hash `0x25CB5A9F37BFD063` · jhash `0xEF63BFDF` · **Cliente**

```lua
local retval = NetworkHaveOnlinePrivileges()
```
```c
BOOL NETWORK_HAVE_ONLINE_PRIVILEGES();
```

**Devuelve:** `BOOL`

---
### NetworkHaveRosBannedPriv

`NETWORK_HAVE_ROS_BANNED_PRIV` · hash `0x8020A73847E0CA7D` · jhash `0xD3BBE42F` · **Cliente**

```lua
local retval = NetworkHaveRosBannedPriv()
```
```c
BOOL NETWORK_HAVE_ROS_BANNED_PRIV();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_IS_ROCKSTAR_BANNED` (`IsRockstarBanned`), `_NETWORK_HAS_PLAYER_BEEN_BANNED` (`NetworkHasPlayerBeenBanned`)

---
### NetworkHaveRosCreateTicketPriv

`NETWORK_HAVE_ROS_CREATE_TICKET_PRIV` · hash `0xA0AD7E2AF5349F61` · jhash `0xBDBB5948` · **Cliente**

```lua
local retval = NetworkHaveRosCreateTicketPriv()
```
```c
BOOL NETWORK_HAVE_ROS_CREATE_TICKET_PRIV();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_IS_SOCIALCLUB_BANNED` (`IsSocialclubBanned`), `_NETWORK_HAVE_SOCIAL_CLUB_PRIVILEGE` (`NetworkHaveSocialClubPrivilege`)

---
### NetworkHaveRosLeaderboardWritePriv

`NETWORK_HAVE_ROS_LEADERBOARD_WRITE_PRIV` · hash `0x422D396F80A96547` · jhash `0xC6EA802E` · **Cliente**

```lua
local retval = NetworkHaveRosLeaderboardWritePriv()
```
```c
BOOL NETWORK_HAVE_ROS_LEADERBOARD_WRITE_PRIV();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x422D396F80A96547` (`N_0x422d396f80a96547`), `_NETWORK_GET_ROS_PRIVILEGE_4` (`NetworkGetRosPrivilege_4`)

---
### NetworkHaveRosMultiplayerPriv

`NETWORK_HAVE_ROS_MULTIPLAYER_PRIV` · hash `0x5F91D5D0B36AA310` · jhash `0x97287D68` · **Cliente**

```lua
local retval = NetworkHaveRosMultiplayerPriv()
```
```c
BOOL NETWORK_HAVE_ROS_MULTIPLAYER_PRIV();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_IS_PLAYER_BANNED` (`IsPlayerBanned`), `_CAN_PLAY_ONLINE` (`CanPlayOnline`), `_NETWORK_GET_ROS_PRIVILEGE_3` (`NetworkGetRosPrivilege_3`)

---
### NetworkHaveRosSocialClubPriv

`NETWORK_HAVE_ROS_SOCIAL_CLUB_PRIV` · hash `0x606E4D3E3CCCF3EB` · jhash `0x424C6E27` · **Cliente**

```lua
local retval = NetworkHaveRosSocialClubPriv()
```
```c
BOOL NETWORK_HAVE_ROS_SOCIAL_CLUB_PRIV();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x606E4D3E3CCCF3EB` (`N_0x606e4d3e3cccf3eb`), `_NETWORK_GET_ROS_PRIVILEGE_10` (`NetworkGetRosPrivilege_10`)

---
### NetworkHaveUserContentPrivileges

`NETWORK_HAVE_USER_CONTENT_PRIVILEGES` · hash `0x72D918C99BCACC54` · jhash `0x1F88819D` · **Cliente**

```lua
local retval = NetworkHaveUserContentPrivileges(p0)
```
```c
BOOL NETWORK_HAVE_USER_CONTENT_PRIVILEGES(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x72D918C99BCACC54` (`N_0x72d918c99bcacc54`)

---
### NetworkHostTransition

`NETWORK_HOST_TRANSITION` · hash `0xA60BB5CE242BB254` · jhash `0x146764FB` · **Cliente**

```lua
local retval = NetworkHostTransition(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
BOOL NETWORK_HOST_TRANSITION(int p0, int p1, int p2, int p3, Any p4, BOOL p5, BOOL p6, int p7, Any p8, int p9);
```

**Parámetros**

- `p0` (`int`): Unknown int
- `p1` (`int`): Unknown int
- `p2` (`int`): Unknown int
- `p3` (`int`): Unknown int
- `p4` (`Any`): Unknown always 0 in decompiled scripts
- `p5` (`BOOL`): BOOL purpose unknown, both 0 and 1 are used in decompiled scripts.
- `p6` (`BOOL`): BOOL purpose unknown, both 0 and 1 are used in decompiled scripts.
- `p7` (`int`): Unknown int, it's an int according to decompiled scripts, however the value is always 0 or 1.
- `p8` (`Any`): Unknown int, it's an int according to decompiled scripts, however the value is always 0 or 1.
- `p9` (`int`): Unknown int, sometimes 0, but also 32768 or 16384 appear in decompiled scripst, maybe a flag of some sort?

**Devuelve:** `BOOL` — Probably a bool indicating if the transition was created.

**Descripción oficial:**

From what I can tell it looks like it does the following:

Creates/hosts a new transition to another online session, using this in FiveM will result in other players being disconencted from the server/preventing them from joining. This is most likely because I entered the wrong session parameters since they're pretty much all unknown right now.

You also need to use `NetworkJoinTransition(Player player)` and `NetworkLaunchTransition()`.

---
### NetworkInviteGamers

`NETWORK_INVITE_GAMERS` · hash `0x9D80CD1D0E6327DE` · jhash `0x52FB8074` · **Cliente**

```lua
local retval, p0, p2, p3 = NetworkInviteGamers(p1)
```
```c
BOOL NETWORK_INVITE_GAMERS(Any* p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### NetworkInviteGamersToTransition

`NETWORK_INVITE_GAMERS_TO_TRANSITION` · hash `0x4A595C32F77DFF76` · jhash `0x5332E645` · **Cliente**

```lua
local retval, p0 = NetworkInviteGamersToTransition(p1)
```
```c
BOOL NETWORK_INVITE_GAMERS_TO_TRANSITION(Any* p0, Any p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkIsActivitySession

`NETWORK_IS_ACTIVITY_SESSION` · hash `0x05095437424397FA` · jhash `0x577DAA8A` · **Cliente**

```lua
local retval = NetworkIsActivitySession()
```
```c
BOOL NETWORK_IS_ACTIVITY_SESSION();
```

**Devuelve:** `BOOL`

---
### NetworkIsActivitySpectator

`NETWORK_IS_ACTIVITY_SPECTATOR` · hash `0x12103B9E0C9F92FB` · jhash `0xAF329720` · **Cliente**

```lua
local retval = NetworkIsActivitySpectator()
```
```c
BOOL NETWORK_IS_ACTIVITY_SPECTATOR();
```

**Devuelve:** `BOOL`

---
### NetworkIsActivitySpectatorFromHandle

`NETWORK_IS_ACTIVITY_SPECTATOR_FROM_HANDLE` · hash `0x2763BBAA72A7BCB9` · jhash `0x58F1DF7D` · **Cliente**

```lua
local retval, networkHandle = NetworkIsActivitySpectatorFromHandle(networkHandle)
```
```c
BOOL NETWORK_IS_ACTIVITY_SPECTATOR_FROM_HANDLE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsAddingFriend

`NETWORK_IS_ADDING_FRIEND` · hash `0x6EA101606F6E4D81` · jhash `0xBB7EC8C4` · **Cliente**

```lua
local retval = NetworkIsAddingFriend()
```
```c
Any NETWORK_IS_ADDING_FRIEND();
```

**Devuelve:** `Any`

---
### NetworkIsCableConnected

`NETWORK_IS_CABLE_CONNECTED` · hash `0xEFFB25453D8600F9` · jhash `0x5C065D55` · **Cliente**

```lua
local retval = NetworkIsCableConnected()
```
```c
BOOL NETWORK_IS_CABLE_CONNECTED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEFFB25453D8600F9` (`N_0xeffb25453d8600f9`)

---
### NetworkIsChattingInPlatformParty

`NETWORK_IS_CHATTING_IN_PLATFORM_PARTY` · hash `0x8DE9945BCC9AEC52` · jhash `0x51367B34` · **Cliente**

```lua
local retval, networkHandle = NetworkIsChattingInPlatformParty(networkHandle)
```
```c
BOOL NETWORK_IS_CHATTING_IN_PLATFORM_PARTY(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This would be nice to see if someone is in party chat, but 2 sad notes.  
1) It only becomes true if said person is speaking in that party at the time.  
2) It will never, become true unless you are in that party with said person.  
```

---
### NetworkIsClockTimeOverridden

`NETWORK_IS_CLOCK_TIME_OVERRIDDEN` · hash `0xD7C95D322FF57522` · jhash `0x2465296D` · **Cliente**

```lua
local retval = NetworkIsClockTimeOverridden()
```
```c
BOOL NETWORK_IS_CLOCK_TIME_OVERRIDDEN();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD7C95D322FF57522` (`N_0xd7c95d322ff57522`)

---
### NetworkIsCloudAvailable

`NETWORK_IS_CLOUD_AVAILABLE` · hash `0x9A4CF4F48AD77302` · jhash `0xC7FF5AFC` · **Cliente**

```lua
local retval = NetworkIsCloudAvailable()
```
```c
BOOL NETWORK_IS_CLOUD_AVAILABLE();
```

**Devuelve:** `BOOL`

---
### NetworkIsCloudBackgroundScriptRequestPending

`NETWORK_IS_CLOUD_BACKGROUND_SCRIPT_REQUEST_PENDING` · hash `0x8132C0EB8B2B3293` · jhash `0x20AB933A` · **Cliente**

```lua
local retval = NetworkIsCloudBackgroundScriptRequestPending()
```
```c
BOOL NETWORK_IS_CLOUD_BACKGROUND_SCRIPT_REQUEST_PENDING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8132C0EB8B2B3293` (`N_0x8132c0eb8b2b3293`), `_HAS_BG_SCRIPT_BEEN_DOWNLOADED` (`HasBgScriptBeenDownloaded`), `_NETWORK_IS_CLOUD_BACKGROUND_SCRIPTS_REQUEST_PENDING` (`NetworkIsCloudBackgroundScriptsRequestPending`)

---
### NetworkIsConnectionEndpointRelayServer

`_NETWORK_IS_CONNECTION_ENDPOINT_RELAY_SERVER` · hash `0x16D3D49902F697BB` · **Cliente**

```lua
local retval = NetworkIsConnectionEndpointRelayServer(player)
```
```c
BOOL _NETWORK_IS_CONNECTION_ENDPOINT_RELAY_SERVER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_IS_*

NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x16D3D49902F697BB` (`N_0x16d3d49902f697bb`)

---
### NetworkIsDoorNetworked

`NETWORK_IS_DOOR_NETWORKED` · hash `0xC01E93FAC20C3346` · jhash `0xD14D9C07` · **Cliente**

```lua
local retval = NetworkIsDoorNetworked(doorHash)
```
```c
BOOL NETWORK_IS_DOOR_NETWORKED(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC01E93FAC20C3346` (`N_0xc01e93fac20c3346`), `_NETWORK_HAS_CONTROL_OF_PAVEMENT_STATS` (`NetworkHasControlOfPavementStats`)

---
### NetworkIsEntityConcealed

`_NETWORK_IS_ENTITY_CONCEALED` · hash `0x71302EC70689052A` · **Cliente**

```lua
local retval = NetworkIsEntityConcealed(entity)
```
```c
BOOL _NETWORK_IS_ENTITY_CONCEALED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Note: This only works for vehicles, which appears to be a bug (since the setter *does* work for every entity type and the name is 99% correct).

---
### NetworkIsEntityFading

`NETWORK_IS_ENTITY_FADING` · hash `0x422F32CC7E56ABAD` · jhash `0xB5087ACF` · **Cliente**

```lua
local retval = NetworkIsEntityFading(entity)
```
```c
BOOL NETWORK_IS_ENTITY_FADING(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x422F32CC7E56ABAD` (`N_0x422f32cc7e56abad`)

---
### NetworkIsFindingGamers

`NETWORK_IS_FINDING_GAMERS` · hash `0xDDDF64C91BFCF0AA` · jhash `0xA6DAA79F` · **Cliente**

```lua
local retval = NetworkIsFindingGamers()
```
```c
BOOL NETWORK_IS_FINDING_GAMERS();
```

**Devuelve:** `BOOL`

---
### NetworkIsFriend

`NETWORK_IS_FRIEND` · hash `0x1A24A179F9B31654` · jhash `0x2DA4C282` · **Cliente**

```lua
local retval, networkHandle = NetworkIsFriend(networkHandle)
```
```c
BOOL NETWORK_IS_FRIEND(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsFriendHandleOnline

`_NETWORK_IS_FRIEND_HANDLE_ONLINE` · hash `0x87EB7A3FFCB314DB` · **Cliente**

```lua
local retval, networkHandle = NetworkIsFriendHandleOnline(networkHandle)
```
```c
BOOL _NETWORK_IS_FRIEND_HANDLE_ONLINE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x87EB7A3FFCB314DB` (`N_0x87eb7a3ffcb314db`), `_NETWORK_IS_FRIEND_ONLINE_2` (`NetworkIsFriendOnline_2`)

---
### NetworkIsFriendInMultiplayer

`NETWORK_IS_FRIEND_IN_MULTIPLAYER` · hash `0x57005C18827F3A28` · jhash `0x400BDDD9` · **Cliente**

```lua
local retval = NetworkIsFriendInMultiplayer(friendName)
```
```c
BOOL NETWORK_IS_FRIEND_IN_MULTIPLAYER(char* friendName);
```

**Parámetros**

- `friendName` (`char*`)

**Devuelve:** `BOOL`

---
### NetworkIsFriendInSameTitle

`NETWORK_IS_FRIEND_IN_SAME_TITLE` · hash `0x2EA9A3BEDF3F17B8` · jhash `0xC54365C2` · **Cliente**

```lua
local retval = NetworkIsFriendInSameTitle(friendName)
```
```c
BOOL NETWORK_IS_FRIEND_IN_SAME_TITLE(char* friendName);
```

**Parámetros**

- `friendName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
In scripts R* calls 'NETWORK_GET_FRIEND_NAME' in this param.  
```

---
### NetworkIsFriendIndexOnline

`NETWORK_IS_FRIEND_INDEX_ONLINE` · hash `0xBAD8F2A42B844821` · jhash `0x94AE7172` · **Cliente**

```lua
local retval = NetworkIsFriendIndexOnline(friendIndex)
```
```c
BOOL NETWORK_IS_FRIEND_INDEX_ONLINE(int friendIndex);
```

**Parámetros**

- `friendIndex` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBAD8F2A42B844821` (`N_0xbad8f2a42b844821`)

---
### NetworkIsFriendOnline

`NETWORK_IS_FRIEND_ONLINE` · hash `0x425A44533437B64D` · jhash `0xE0A42430` · **Cliente**

```lua
local retval = NetworkIsFriendOnline(name)
```
```c
BOOL NETWORK_IS_FRIEND_ONLINE(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

---
### NetworkIsGameInProgress

`NETWORK_IS_GAME_IN_PROGRESS` · hash `0x10FAB35428CCC9D7` · jhash `0x09B88E3E` · **Cliente**

```lua
local retval = NetworkIsGameInProgress()
```
```c
BOOL NETWORK_IS_GAME_IN_PROGRESS();
```

**Devuelve:** `BOOL`

---
### NetworkIsGamerBlockedByMe

`NETWORK_IS_GAMER_BLOCKED_BY_ME` · hash `0xE944C4F5AF1B5883` · jhash `0x3FDCC8D7` · **Cliente**

```lua
local retval, networkHandle = NetworkIsGamerBlockedByMe(networkHandle)
```
```c
BOOL NETWORK_IS_GAMER_BLOCKED_BY_ME(Any* networkHandle);
```

**Parámetros**

- `networkHandle` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsGamerInMySession

`NETWORK_IS_GAMER_IN_MY_SESSION` · hash `0x0F10B05DDF8D16E9` · jhash `0x59127716` · **Cliente**

```lua
local retval, networkHandle = NetworkIsGamerInMySession(networkHandle)
```
```c
BOOL NETWORK_IS_GAMER_IN_MY_SESSION(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsGamerMutedByMe

`NETWORK_IS_GAMER_MUTED_BY_ME` · hash `0xCE60DE011B6C7978` · jhash `0x001B4046` · **Cliente**

```lua
local retval, networkHandle = NetworkIsGamerMutedByMe(networkHandle)
```
```c
BOOL NETWORK_IS_GAMER_MUTED_BY_ME(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsGamerTalking

`NETWORK_IS_GAMER_TALKING` · hash `0x71C33B22606CD88A` · jhash `0x99B58DBC` · **Cliente**

```lua
local retval, networkHandle = NetworkIsGamerTalking(networkHandle)
```
```c
BOOL NETWORK_IS_GAMER_TALKING(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsGettingGamerStatus

`NETWORK_IS_GETTING_GAMER_STATUS` · hash `0x94A8394D150B013A` · jhash `0x08029970` · **Cliente**

```lua
local retval = NetworkIsGettingGamerStatus()
```
```c
BOOL NETWORK_IS_GETTING_GAMER_STATUS();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x94A8394D150B013A` (`N_0x94a8394d150b013a`)

---
### NetworkIsHandleValid

`NETWORK_IS_HANDLE_VALID` · hash `0x6F79B93B0A8E4133` · jhash `0xF0996C6E` · **Cliente**

```lua
local retval, networkHandle = NetworkIsHandleValid(bufferSize)
```
```c
BOOL NETWORK_IS_HANDLE_VALID(int* networkHandle, int bufferSize);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bufferSize` (`int`)

**Devuelve:** `BOOL`

---
### NetworkIsHost

`NETWORK_IS_HOST` · hash `0x8DB296B814EDDA07` · jhash `0xE46AC10F` · **Cliente**

```lua
local retval = NetworkIsHost()
```
```c
BOOL NETWORK_IS_HOST();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
If you are host, returns true else returns false.
```

---
### NetworkIsHostOfThisScript

`NETWORK_IS_HOST_OF_THIS_SCRIPT` · hash `0x83CD99A1E6061AB5` · jhash `0x6970BA94` · **Cliente**

```lua
local retval = NetworkIsHostOfThisScript()
```
```c
BOOL NETWORK_IS_HOST_OF_THIS_SCRIPT();
```

**Devuelve:** `BOOL`

---
### NetworkIsInMpCutscene

`NETWORK_IS_IN_MP_CUTSCENE` · hash `0x6CC27C9FA2040220` · jhash `0x4BB33316` · **Cliente**

```lua
local retval = NetworkIsInMpCutscene()
```
```c
BOOL NETWORK_IS_IN_MP_CUTSCENE();
```

**Devuelve:** `BOOL`

---
### NetworkIsInParty

`NETWORK_IS_IN_PARTY` · hash `0x966C2BC2A7FE3F30` · jhash `0xF9D7D67D` · **Cliente**

```lua
local retval = NetworkIsInParty()
```
```c
BOOL NETWORK_IS_IN_PARTY();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Note according to IDA TU27 X360(Console),  
This native & 'NETWORK_IS_PARTY_MEMBER' both jump to the same location.  
Side note: This location just stops where it's at once jumped to.  
Screenshot for side note,   
https://i.imgur.com/0yMiTs9.png
https://i.imgur.com/td7SjGH.png
```

---
### NetworkIsInPlatformParty

`NETWORK_IS_IN_PLATFORM_PARTY` · hash `0x2FC5650B0271CB57` · jhash `0xA812B6CB` · **Cliente**

```lua
local retval = NetworkIsInPlatformParty()
```
```c
BOOL NETWORK_IS_IN_PLATFORM_PARTY();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Hardcoded to return false.
```

**Nombres antiguos (alias):** `0x2FC5650B0271CB57` (`N_0x2fc5650b0271cb57`)

---
### NetworkIsInPlatformPartyChat

`NETWORK_IS_IN_PLATFORM_PARTY_CHAT` · hash `0xFD8B834A8BA05048` · jhash `0xC6609191` · **Cliente**

```lua
local retval = NetworkIsInPlatformPartyChat()
```
```c
BOOL NETWORK_IS_IN_PLATFORM_PARTY_CHAT();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Hardcoded to return false.
```

**Nombres antiguos (alias):** `0xFD8B834A8BA05048` (`N_0xfd8b834a8ba05048`)

---
### NetworkIsInSession

`NETWORK_IS_IN_SESSION` · hash `0xCA97246103B63917` · jhash `0x4BC4105E` · **Cliente**

```lua
local retval = NetworkIsInSession()
```
```c
BOOL NETWORK_IS_IN_SESSION();
```

**Devuelve:** `BOOL`

---
### NetworkIsInSpectatorMode

`NETWORK_IS_IN_SPECTATOR_MODE` · hash `0x048746E388762E11` · jhash `0x3EAD9DB8` · **Cliente**

```lua
local retval = NetworkIsInSpectatorMode()
```
```c
BOOL NETWORK_IS_IN_SPECTATOR_MODE();
```

**Devuelve:** `BOOL`

---
### NetworkIsInTransition

`NETWORK_IS_IN_TRANSITION` · hash `0x68049AEFF83D8F0A` · jhash `0xC3CDB626` · **Cliente**

```lua
local retval = NetworkIsInTransition()
```
```c
BOOL NETWORK_IS_IN_TRANSITION();
```

**Devuelve:** `BOOL`

---
### NetworkIsInTutorialSession

`NETWORK_IS_IN_TUTORIAL_SESSION` · hash `0xADA24309FE08DACF` · jhash `0x34DD7B28` · **Cliente**

```lua
local retval = NetworkIsInTutorialSession()
```
```c
BOOL NETWORK_IS_IN_TUTORIAL_SESSION();
```

**Devuelve:** `BOOL`

---
### NetworkIsInactiveProfile

`NETWORK_IS_INACTIVE_PROFILE` · hash `0x7E58745504313A2E` · jhash `0x95481343` · **Cliente**

```lua
local retval, networkHandle = NetworkIsInactiveProfile(networkHandle)
```
```c
BOOL NETWORK_IS_INACTIVE_PROFILE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns true if the networkHandle is signed in on the same machine, but is not the main player.

**Descripción oficial:**

Checks if the networkHandle is the same as any other user that is signed in on the local machine.
For example, if your console has two or more users signed in (on different controllers), the profile that is not controlling the game would be "inactive".

---
### NetworkIsLocalPlayerInvincible

`NETWORK_IS_LOCAL_PLAYER_INVINCIBLE` · hash `0x8A8694B48715B000` · jhash `0x8DE13B36` · **Cliente**

```lua
local retval = NetworkIsLocalPlayerInvincible()
```
```c
BOOL NETWORK_IS_LOCAL_PLAYER_INVINCIBLE();
```

**Devuelve:** `BOOL`

---
### NetworkIsLocalTalking

`NETWORK_IS_LOCAL_TALKING` · hash `0xC0D2AF00BCC234CA` · jhash `0xAC00A5BE` · **Cliente**

```lua
local retval = NetworkIsLocalTalking()
```
```c
BOOL NETWORK_IS_LOCAL_TALKING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC0D2AF00BCC234CA` (`N_0xc0d2af00bcc234ca`)

---
### NetworkIsMultiplayerDisabled

`NETWORK_IS_MULTIPLAYER_DISABLED` · hash `0x9747292807126EDA` · jhash `0x05518C0F` · **Cliente**

```lua
local retval = NetworkIsMultiplayerDisabled()
```
```c
BOOL NETWORK_IS_MULTIPLAYER_DISABLED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9747292807126EDA` (`N_0x9747292807126eda`)

---
### NetworkIsNetworkIdAClone

`_NETWORK_IS_NETWORK_ID_A_CLONE` · hash `0x7242F8B741CE1086` · **Cliente**

```lua
local retval = NetworkIsNetworkIdAClone(netId)
```
```c
BOOL _NETWORK_IS_NETWORK_ID_A_CLONE(int netId);
```

**Parámetros**

- `netId` (`int`): The network id for an object or entity.

**Devuelve:** `BOOL` — Probably a bool, returns 1 if you don't have control over the netId entity.

**Descripción oficial:**

Returns true if the specified network id is controlled by someone else.

**Nombres antiguos (alias):** `0x7242F8B741CE1086` (`N_0x7242f8b741ce1086`)

---
### NetworkIsOfflineInvitePending

`NETWORK_IS_OFFLINE_INVITE_PENDING` · hash `0x74698374C45701D2` · jhash `0x70ED476A` · **Cliente**

```lua
local retval = NetworkIsOfflineInvitePending()
```
```c
BOOL NETWORK_IS_OFFLINE_INVITE_PENDING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x74698374C45701D2` (`N_0x74698374c45701d2`)

---
### NetworkIsParticipantActive

`NETWORK_IS_PARTICIPANT_ACTIVE` · hash `0x6FF8FF40B6357D45` · jhash `0x4E2C348B` · **Cliente**

```lua
local retval = NetworkIsParticipantActive(p0)
```
```c
BOOL NETWORK_IS_PARTICIPANT_ACTIVE(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

---
### NetworkIsPartyMember

`NETWORK_IS_PARTY_MEMBER` · hash `0x676ED266AADD31E0` · jhash `0x1D0C929D` · **Cliente**

```lua
local retval, networkHandle = NetworkIsPartyMember(networkHandle)
```
```c
BOOL NETWORK_IS_PARTY_MEMBER(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Note according to IDA TU27 X360(Console),  
This native & 'NETWORK_IS_PARTY_MEMBER' both jump to the same location.  
Side note: This location just stops where it's at once jumped to.  
Screenshot for side note,   
https://i.imgur.com/1CIH2VT.png
https://i.imgur.com/6QTCRj2.png
```

---
### NetworkIsPendingFriend

`NETWORK_IS_PENDING_FRIEND` · hash `0x0BE73DA6984A6E33` · jhash `0x5C85FF81` · **Cliente**

```lua
local retval = NetworkIsPendingFriend(p0)
```
```c
Any NETWORK_IS_PENDING_FRIEND(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
This function is hard-coded to always return 0.
```

---
### NetworkIsPlayerAParticipant

`NETWORK_IS_PLAYER_A_PARTICIPANT` · hash `0x3CA58F6CB7CBD784` · jhash `0xB08B6992` · **Cliente**

```lua
local retval = NetworkIsPlayerAParticipant(player)
```
```c
BOOL NETWORK_IS_PLAYER_A_PARTICIPANT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerAParticipantOnScript

`NETWORK_IS_PLAYER_A_PARTICIPANT_ON_SCRIPT` · hash `0x1AD5B71586B94820` · jhash `0xCEA55F4C` · **Cliente**

```lua
local retval = NetworkIsPlayerAParticipantOnScript(player1, script, player2)
```
```c
BOOL NETWORK_IS_PLAYER_A_PARTICIPANT_ON_SCRIPT(Player player1, char* script, Player player2);
```

**Parámetros**

- `player1` (`Player`)
- `script` (`char*`)
- `player2` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1AD5B71586B94820` (`N_0x1ad5b71586b94820`)

---
### NetworkIsPlayerActive

`NETWORK_IS_PLAYER_ACTIVE` · hash `0xB8DFD30D6973E135` · jhash `0x43657B17` · **Cliente**

```lua
local retval = NetworkIsPlayerActive(player)
```
```c
BOOL NETWORK_IS_PLAYER_ACTIVE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerBlockedByMe

`NETWORK_IS_PLAYER_BLOCKED_BY_ME` · hash `0x57AF1F8E27483721` · jhash `0xAE4F4560` · **Cliente**

```lua
local retval = NetworkIsPlayerBlockedByMe(player)
```
```c
BOOL NETWORK_IS_PLAYER_BLOCKED_BY_ME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerConcealed

`NETWORK_IS_PLAYER_CONCEALED` · hash `0x919B3C98ED8292F9` · jhash `0xB0313590` · **Cliente**

```lua
local retval = NetworkIsPlayerConcealed(player)
```
```c
BOOL NETWORK_IS_PLAYER_CONCEALED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerConnected

`NETWORK_IS_PLAYER_CONNECTED` · hash `0x93DC1BE4E1ABE9D1` · jhash `0x168EE2C2` · **Cliente**

```lua
local retval = NetworkIsPlayerConnected(player)
```
```c
BOOL NETWORK_IS_PLAYER_CONNECTED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerEqualToIndex

`_NETWORK_IS_PLAYER_EQUAL_TO_INDEX` · hash `0x9DE986FC9A87C474` · jhash `0xE66A0B40` · **Cliente**

```lua
local retval = NetworkIsPlayerEqualToIndex(player, index)
```
```c
BOOL _NETWORK_IS_PLAYER_EQUAL_TO_INDEX(Player player, int index);
```

**Parámetros**

- `player` (`Player`)
- `index` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_ARE_*  
```

**Nombres antiguos (alias):** `0x9DE986FC9A87C474` (`N_0x9de986fc9a87c474`)

---
### NetworkIsPlayerFading

`NETWORK_IS_PLAYER_FADING` · hash `0x631DC5DFF4B110E3` · jhash `0x065C597B` · **Cliente**

```lua
local retval = NetworkIsPlayerFading(player)
```
```c
BOOL NETWORK_IS_PLAYER_FADING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x631DC5DFF4B110E3` (`N_0x631dc5dff4b110e3`)

---
### NetworkIsPlayerInMpCutscene

`NETWORK_IS_PLAYER_IN_MP_CUTSCENE` · hash `0x63F9EE203C3619F2` · jhash `0x56F961E4` · **Cliente**

```lua
local retval = NetworkIsPlayerInMpCutscene(player)
```
```c
BOOL NETWORK_IS_PLAYER_IN_MP_CUTSCENE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerMutedByMe

`NETWORK_IS_PLAYER_MUTED_BY_ME` · hash `0x8C71288AE68EDE39` · jhash `0x7A21050E` · **Cliente**

```lua
local retval = NetworkIsPlayerMutedByMe(player)
```
```c
BOOL NETWORK_IS_PLAYER_MUTED_BY_ME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkIsPlayerTalking

`NETWORK_IS_PLAYER_TALKING` · hash `0x031E11F3D447647E` · jhash `0xDA9FD9DB` · **Cliente**

```lua
local retval = NetworkIsPlayerTalking(player)
```
```c
BOOL NETWORK_IS_PLAYER_TALKING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
returns true if someone is screaming or talking in a microphone  
```

---
### NetworkIsPsnAvailable

`_NETWORK_IS_PSN_AVAILABLE` · hash `0x8D11E61A4ABF49CC` · **Cliente**

```lua
local retval = NetworkIsPsnAvailable()
```
```c
BOOL _NETWORK_IS_PSN_AVAILABLE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8D11E61A4ABF49CC` (`N_0x8d11e61a4abf49cc`)

---
### NetworkIsScriptActive

`NETWORK_IS_SCRIPT_ACTIVE` · hash `0x9D40DF90FAD26098` · jhash `0x4A65250C` · **Cliente**

```lua
local retval = NetworkIsScriptActive(scriptName, player, p2, p3)
```
```c
BOOL NETWORK_IS_SCRIPT_ACTIVE(char* scriptName, Player player, BOOL p2, Any p3);
```

**Parámetros**

- `scriptName` (`char*`)
- `player` (`Player`)
- `p2` (`BOOL`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkIsScriptActiveByHash

`_NETWORK_IS_SCRIPT_ACTIVE_BY_HASH` · hash `0xDA7DE67F5FE5EE13` · **Cliente**

```lua
local retval = NetworkIsScriptActiveByHash(scriptHash, p1, p2, p3)
```
```c
BOOL _NETWORK_IS_SCRIPT_ACTIVE_BY_HASH(Hash scriptHash, int p1, BOOL p2, int p3);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)
- `p2` (`BOOL`)
- `p3` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2245
```

---
### NetworkIsSessionActive

`NETWORK_IS_SESSION_ACTIVE` · hash `0xD83C2B94E7508980` · jhash `0x715CB8C4` · **Cliente**

```lua
local retval = NetworkIsSessionActive()
```
```c
BOOL NETWORK_IS_SESSION_ACTIVE();
```

**Devuelve:** `BOOL`

---
### NetworkIsSessionBusy

`NETWORK_IS_SESSION_BUSY` · hash `0xF4435D66A8E2905E` · jhash `0x8592152D` · **Cliente**

```lua
local retval = NetworkIsSessionBusy()
```
```c
BOOL NETWORK_IS_SESSION_BUSY();
```

**Devuelve:** `BOOL`

---
### NetworkIsSessionStarted

`NETWORK_IS_SESSION_STARTED` · hash `0x9DE624D2FC4B603F` · jhash `0x9D854A37` · **Cliente**

```lua
local retval = NetworkIsSessionStarted()
```
```c
BOOL NETWORK_IS_SESSION_STARTED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This checks if player is playing on gta online or not.  
Please add an if and block your mod if this is "true".  
```

---
### NetworkIsSignedIn

`NETWORK_IS_SIGNED_IN` · hash `0x054354A99211EB96` · jhash `0xADD0B40F` · **Cliente**

```lua
local retval = NetworkIsSignedIn()
```
```c
BOOL NETWORK_IS_SIGNED_IN();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the player is signed into Social Club.  
```

---
### NetworkIsSignedOnline

`NETWORK_IS_SIGNED_ONLINE` · hash `0x1077788E268557C2` · jhash `0x6E5BDCE2` · **Cliente**

```lua
local retval = NetworkIsSignedOnline()
```
```c
BOOL NETWORK_IS_SIGNED_ONLINE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the game is not in offline mode.  
seemed not to work for some ppl  
```

---
### NetworkIsTextChatActive

`_NETWORK_IS_TEXT_CHAT_ACTIVE` · hash `0x5FCF4D7069B09026` · **Cliente**

```lua
local retval = NetworkIsTextChatActive()
```
```c
BOOL _NETWORK_IS_TEXT_CHAT_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Same as _IS_TEXT_CHAT_ACTIVE, except it does not check if the text chat HUD component is initialized, and therefore may crash.  
```

---
### NetworkIsThisScriptMarked

`_NETWORK_IS_THIS_SCRIPT_MARKED` · hash `0xD1110739EEADB592` · **Cliente**

```lua
local retval = NetworkIsThisScriptMarked(p0, p1, p2)
```
```c
BOOL _NETWORK_IS_THIS_SCRIPT_MARKED(Any p0, BOOL p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD1110739EEADB592` (`N_0xd1110739eeadb592`), `_NETWORK_SET_THIS_SCRIPT_MARKED` (`NetworkSetThisScriptMarked`)

---
### NetworkIsTransitionBusy

`NETWORK_IS_TRANSITION_BUSY` · hash `0x520F3282A53D26B7` · jhash `0xA357A2C6` · **Cliente**

```lua
local retval = NetworkIsTransitionBusy()
```
```c
BOOL NETWORK_IS_TRANSITION_BUSY();
```

**Devuelve:** `BOOL`

---
### NetworkIsTransitionClosedCrew

`NETWORK_IS_TRANSITION_CLOSED_CREW` · hash `0x0DBD5D7E3C5BEC3B` · jhash `0xB97A966B` · **Cliente**

```lua
local retval = NetworkIsTransitionClosedCrew()
```
```c
BOOL NETWORK_IS_TRANSITION_CLOSED_CREW();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0DBD5D7E3C5BEC3B` (`N_0x0dbd5d7e3c5bec3b`)

---
### NetworkIsTransitionClosedFriends

`NETWORK_IS_TRANSITION_CLOSED_FRIENDS` · hash `0x6512765E3BE78C50` · jhash `0x95FFACF8` · **Cliente**

```lua
local retval = NetworkIsTransitionClosedFriends()
```
```c
BOOL NETWORK_IS_TRANSITION_CLOSED_FRIENDS();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6512765E3BE78C50` (`N_0x6512765e3be78c50`)

---
### NetworkIsTransitionHost

`NETWORK_IS_TRANSITION_HOST` · hash `0x0B824797C9BF2159` · jhash `0x0C0900BC` · **Cliente**

```lua
local retval = NetworkIsTransitionHost()
```
```c
BOOL NETWORK_IS_TRANSITION_HOST();
```

**Devuelve:** `BOOL`

---
### NetworkIsTransitionHostFromHandle

`NETWORK_IS_TRANSITION_HOST_FROM_HANDLE` · hash `0x6B5C83BA3EFE6A10` · jhash `0x0E2854C4` · **Cliente**

```lua
local retval, networkHandle = NetworkIsTransitionHostFromHandle(networkHandle)
```
```c
BOOL NETWORK_IS_TRANSITION_HOST_FROM_HANDLE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkIsTransitionMatchmaking

`NETWORK_IS_TRANSITION_MATCHMAKING` · hash `0x292564C735375EDF` · jhash `0x8262C70E` · **Cliente**

```lua
local retval = NetworkIsTransitionMatchmaking()
```
```c
BOOL NETWORK_IS_TRANSITION_MATCHMAKING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x292564C735375EDF` (`N_0x292564c735375edf`)

---
### NetworkIsTransitionOpenToMatchmaking

`NETWORK_IS_TRANSITION_OPEN_TO_MATCHMAKING` · hash `0x37A4494483B9F5C9` · jhash `0xC901AA9F` · **Cliente**

```lua
local retval = NetworkIsTransitionOpenToMatchmaking()
```
```c
BOOL NETWORK_IS_TRANSITION_OPEN_TO_MATCHMAKING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x37A4494483B9F5C9` (`N_0x37a4494483b9f5c9`)

---
### NetworkIsTransitionPrivate

`NETWORK_IS_TRANSITION_PRIVATE` · hash `0x5A6AA44FF8E931E6` · jhash `0x104DDE8D` · **Cliente**

```lua
local retval = NetworkIsTransitionPrivate()
```
```c
BOOL NETWORK_IS_TRANSITION_PRIVATE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5A6AA44FF8E931E6` (`N_0x5a6aa44ff8e931e6`)

---
### NetworkIsTransitionSolo

`NETWORK_IS_TRANSITION_SOLO` · hash `0x5DC577201723960A` · jhash `0x063DC4A5` · **Cliente**

```lua
local retval = NetworkIsTransitionSolo()
```
```c
BOOL NETWORK_IS_TRANSITION_SOLO();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5DC577201723960A` (`N_0x5dc577201723960a`)

---
### NetworkIsTransitionStarted

`NETWORK_IS_TRANSITION_STARTED` · hash `0x53FA83401D9C07FE` · jhash `0x7917E111` · **Cliente**

```lua
local retval = NetworkIsTransitionStarted()
```
```c
BOOL NETWORK_IS_TRANSITION_STARTED();
```

**Devuelve:** `BOOL`

---
### NetworkIsTransitionToGame

`NETWORK_IS_TRANSITION_TO_GAME` · hash `0x9D7696D8F4FA6CB7` · jhash `0x17146B2B` · **Cliente**

```lua
local retval = NetworkIsTransitionToGame()
```
```c
BOOL NETWORK_IS_TRANSITION_TO_GAME();
```

**Devuelve:** `BOOL`

---
### NetworkIsTransitionVisibilityLocked

`NETWORK_IS_TRANSITION_VISIBILITY_LOCKED` · hash `0xD0A484CB2F829FBE` · jhash `0xF637166E` · **Cliente**

```lua
local retval = NetworkIsTransitionVisibilityLocked()
```
```c
BOOL NETWORK_IS_TRANSITION_VISIBILITY_LOCKED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD0A484CB2F829FBE` (`N_0xd0a484cb2f829fbe`)

---
### NetworkIsTunableCloudRequestPending

`NETWORK_IS_TUNABLE_CLOUD_REQUEST_PENDING` · hash `0x0467C11ED88B7D28` · jhash `0x47978D7F` · **Cliente**

```lua
local retval = NetworkIsTunableCloudRequestPending()
```
```c
BOOL NETWORK_IS_TUNABLE_CLOUD_REQUEST_PENDING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0467C11ED88B7D28` (`N_0x0467c11ed88b7d28`), `_HAS_TUNABLES_BEEN_DOWNLOADED` (`HasTunablesBeenDownloaded`)

---
### NetworkIsTutorialSessionChangePending

`NETWORK_IS_TUTORIAL_SESSION_CHANGE_PENDING` · hash `0x35F0B98A8387274D` · jhash `0xA003C40B` · **Cliente**

```lua
local retval = NetworkIsTutorialSessionChangePending()
```
```c
BOOL NETWORK_IS_TUTORIAL_SESSION_CHANGE_PENDING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x35F0B98A8387274D` (`N_0x35f0b98a8387274d`)

---
### NetworkJoinGroupActivity

`NETWORK_JOIN_GROUP_ACTIVITY` · hash `0xA06509A691D12BE4` · jhash `0x0D7E5CF9` · **Cliente**

```lua
local retval = NetworkJoinGroupActivity()
```
```c
Any NETWORK_JOIN_GROUP_ACTIVITY();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xA06509A691D12BE4` (`N_0xa06509a691d12be4`)

---
### NetworkJoinPreviouslyFailedSession

`NETWORK_JOIN_PREVIOUSLY_FAILED_SESSION` · hash `0x59DF79317F85A7E0` · jhash `0x6CDAA7D2` · **Cliente**

```lua
local retval = NetworkJoinPreviouslyFailedSession()
```
```c
BOOL NETWORK_JOIN_PREVIOUSLY_FAILED_SESSION();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x59DF79317F85A7E0` (`N_0x59df79317f85a7e0`)

---
### NetworkJoinPreviouslyFailedTransition

`NETWORK_JOIN_PREVIOUSLY_FAILED_TRANSITION` · hash `0xFFE1E5B792D92B34` · jhash `0xBF21818E` · **Cliente**

```lua
local retval = NetworkJoinPreviouslyFailedTransition()
```
```c
BOOL NETWORK_JOIN_PREVIOUSLY_FAILED_TRANSITION();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFFE1E5B792D92B34` (`N_0xffe1e5b792d92b34`)

---
### NetworkJoinTransition

`NETWORK_JOIN_TRANSITION` · hash `0x9D060B08CD63321A` · jhash `0xB054EC4B` · **Cliente**

```lua
local retval = NetworkJoinTransition(player)
```
```c
BOOL NETWORK_JOIN_TRANSITION(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
int handle[76];  
NETWORK_HANDLE_FROM_FRIEND(iSelectedPlayer, &handle[0], 13);  
Player uVar2 = NETWORK_GET_PLAYER_FROM_GAMER_HANDLE(&handle[0]);  
NETWORK_JOIN_TRANSITION(uVar2);  
		nothing doin.  
```

---
### NetworkLaunchTransition

`NETWORK_LAUNCH_TRANSITION` · hash `0x2DCF46CB1A4F0884` · jhash `0xE3570BA2` · **Cliente**

```lua
local retval = NetworkLaunchTransition()
```
```c
BOOL NETWORK_LAUNCH_TRANSITION();
```

**Devuelve:** `BOOL`

---
### NetworkLeaveTransition

`NETWORK_LEAVE_TRANSITION` · hash `0xD23A1A815D21DB19` · jhash `0x3A3599B7` · **Cliente**

```lua
local retval = NetworkLeaveTransition()
```
```c
BOOL NETWORK_LEAVE_TRANSITION();
```

**Devuelve:** `BOOL`

---
### NetworkMarkTransitionGamerAsFullyJoined

`NETWORK_MARK_TRANSITION_GAMER_AS_FULLY_JOINED` · hash `0x5728BB6D63E3FF1D` · jhash `0x03383F57` · **Cliente**

```lua
local retval, p0 = NetworkMarkTransitionGamerAsFullyJoined(p0)
```
```c
BOOL NETWORK_MARK_TRANSITION_GAMER_AS_FULLY_JOINED(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkMemberIdFromGamerHandle

`NETWORK_MEMBER_ID_FROM_GAMER_HANDLE` · hash `0xC82630132081BB6F` · jhash `0x62EF0A63` · **Cliente**

```lua
local retval, networkHandle = NetworkMemberIdFromGamerHandle(networkHandle)
```
```c
char* NETWORK_MEMBER_ID_FROM_GAMER_HANDLE(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `char*`

---
### NetworkOpenTransitionMatchmaking

`NETWORK_OPEN_TRANSITION_MATCHMAKING` · hash `0x2B3A8F7CA3A38FDE` · jhash `0xC71E607B` · **Cliente**

```lua
NetworkOpenTransitionMatchmaking()
```
```c
void NETWORK_OPEN_TRANSITION_MATCHMAKING();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2B3A8F7CA3A38FDE` (`N_0x2b3a8f7ca3a38fde`)

---
### NetworkOverrideChatRestrictions

`NETWORK_OVERRIDE_CHAT_RESTRICTIONS` · hash `0x3039AE5AD2C9C0C4` · jhash `0x74EE2D8B` · **Cliente**

```lua
NetworkOverrideChatRestrictions(player, toggle)
```
```c
void NETWORK_OVERRIDE_CHAT_RESTRICTIONS(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Could possibly bypass being muted or automatically muted  
```

**Nombres antiguos (alias):** `0x3039AE5AD2C9C0C4` (`N_0x3039ae5ad2c9c0c4`)

---
### NetworkOverrideClockMillisecondsPerGameMinute

`_NETWORK_OVERRIDE_CLOCK_MILLISECONDS_PER_GAME_MINUTE` · hash `0x42BF1D2E723B6D7E` · **Cliente**

```lua
NetworkOverrideClockMillisecondsPerGameMinute(ms)
```
```c
void _NETWORK_OVERRIDE_CLOCK_MILLISECONDS_PER_GAME_MINUTE(int ms);
```

**Parámetros**

- `ms` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### NetworkOverrideClockTime

`NETWORK_OVERRIDE_CLOCK_TIME` · hash `0xE679E3E06E363892` · jhash `0xC077BCD6` · **Cliente**

```lua
NetworkOverrideClockTime(hours, minutes, seconds)
```
```c
void NETWORK_OVERRIDE_CLOCK_TIME(int hours, int minutes, int seconds);
```

**Parámetros**

- `hours` (`int`): The hour to set (0-23).
- `minutes` (`int`): The minute to set (0-59).
- `seconds` (`int`): The second to set (0-59).

**Devuelve:** `void`

**Descripción oficial:**

Overrides the game clock time for the local player, allowing for manipulation of the in-game time. This native is effective in both multiplayer and singleplayer modes.

**Note:** Passing wrong data (e.g. hours above 23) will cause the game to crash.

---
### NetworkOverrideCoordsAndHeading

`NETWORK_OVERRIDE_COORDS_AND_HEADING` · hash `0xA7E30DE9272B6D49` · jhash `0x644141C5` · **Cliente**

```lua
NetworkOverrideCoordsAndHeading(entity, x, y, z, heading)
```
```c
void NETWORK_OVERRIDE_COORDS_AND_HEADING(Entity entity, float x, float y, float z, float heading);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA7E30DE9272B6D49` (`N_0xa7e30de9272b6d49`)

---
### NetworkOverrideReceiveRestrictions

`NETWORK_OVERRIDE_RECEIVE_RESTRICTIONS` · hash `0xDDF73E2B1FEC5AB4` · jhash `0x95F1C60D` · **Cliente**

```lua
NetworkOverrideReceiveRestrictions(player, toggle)
```
```c
void NETWORK_OVERRIDE_RECEIVE_RESTRICTIONS(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
R* uses this to hear all player when spectating.   
It allows you to hear other online players when their chat is on none, crew and or friends  
```

**Nombres antiguos (alias):** `0xDDF73E2B1FEC5AB4` (`N_0xddf73e2b1fec5ab4`)

---
### NetworkOverrideReceiveRestrictionsAll

`NETWORK_OVERRIDE_RECEIVE_RESTRICTIONS_ALL` · hash `0x0FF2862B61A58AF9` · jhash `0x1BCD3DDF` · **Cliente**

```lua
NetworkOverrideReceiveRestrictionsAll(toggle)
```
```c
void NETWORK_OVERRIDE_RECEIVE_RESTRICTIONS_ALL(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p0 is always false in scripts.
```

**Nombres antiguos (alias):** `0x0FF2862B61A58AF9` (`N_0x0ff2862b61a58af9`)

---
### NetworkOverrideSendRestrictions

`NETWORK_OVERRIDE_SEND_RESTRICTIONS` · hash `0x97DD4C5944CC2E6A` · jhash `0x6C344AE3` · **Cliente**

```lua
NetworkOverrideSendRestrictions(player, toggle)
```
```c
void NETWORK_OVERRIDE_SEND_RESTRICTIONS(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This is used alongside the native,
'NETWORK_OVERRIDE_RECEIVE_RESTRICTIONS'. Read its description for more info.
```

**Nombres antiguos (alias):** `0x97DD4C5944CC2E6A` (`N_0x97dd4c5944cc2e6a`), `_NETWORK_OVERRIDE_SEND_RESTRICTIONS` (`NetworkOverrideSendRestrictions`)

---
### NetworkOverrideSendRestrictionsAll

`NETWORK_OVERRIDE_SEND_RESTRICTIONS_ALL` · hash `0x57B192B4D4AD23D5` · jhash `0x2F98B405` · **Cliente**

```lua
NetworkOverrideSendRestrictionsAll(toggle)
```
```c
void NETWORK_OVERRIDE_SEND_RESTRICTIONS_ALL(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x57B192B4D4AD23D5` (`N_0x57b192b4d4ad23d5`), `_NETWORK_CHAT_MUTE` (`NetworkChatMute`)

---
### NetworkOverrideTeamRestrictions

`NETWORK_OVERRIDE_TEAM_RESTRICTIONS` · hash `0x6F697A66CE78674E` · jhash `0xC8CC9E75` · **Cliente**

```lua
NetworkOverrideTeamRestrictions(team, toggle)
```
```c
void NETWORK_OVERRIDE_TEAM_RESTRICTIONS(int team, BOOL toggle);
```

**Parámetros**

- `team` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6F697A66CE78674E` (`N_0x6f697a66ce78674e`)

---
### NetworkOverrideTransitionChat

`NETWORK_OVERRIDE_TRANSITION_CHAT` · hash `0xAF66059A131AA269` · jhash `0xCAB21090` · **Cliente**

```lua
NetworkOverrideTransitionChat(p0)
```
```c
void NETWORK_OVERRIDE_TRANSITION_CHAT(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAF66059A131AA269` (`N_0xaf66059a131aa269`)

---
### NetworkPedForceGameStateUpdate

`_NETWORK_PED_FORCE_GAME_STATE_UPDATE` · hash `0xF0BC9BCD24A511D5` · **Cliente**

```lua
NetworkPedForceGameStateUpdate(ped)
```
```c
void _NETWORK_PED_FORCE_GAME_STATE_UPDATE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xF0BC9BCD24A511D5` (`N_0xf0bc9bcd24a511d5`)

---
### NetworkPlayerGetCheaterReason

`NETWORK_PLAYER_GET_CHEATER_REASON` · hash `0x172F75B6EE2233BA` · jhash `0x1720ABA6` · **Cliente**

```lua
local retval = NetworkPlayerGetCheaterReason()
```
```c
int NETWORK_PLAYER_GET_CHEATER_REASON();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x172F75B6EE2233BA` (`N_0x172f75b6ee2233ba`), `_NETWORK_PLAYER_IS_UNK` (`NetworkPlayerIsUnk`)

---
### NetworkPlayerGetName

`NETWORK_PLAYER_GET_NAME` · hash `0x7718D2E2060837D2` · jhash `0xCE48F260` · **Cliente**

```lua
local retval = NetworkPlayerGetName(player)
```
```c
char* NETWORK_PLAYER_GET_NAME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns the name of a given player. Returns "**Invalid**" if CPlayerInfo of the given player cannot be retrieved or the player doesn't exist.
```

---
### NetworkPlayerGetUserid

`NETWORK_PLAYER_GET_USERID` · hash `0x4927FC39CD0869A0` · jhash `0x4EC0D983` · **Cliente**

```lua
local retval, userID = NetworkPlayerGetUserid(player, userID)
```
```c
char* NETWORK_PLAYER_GET_USERID(Player player, int* userID);
```

**Parámetros**

- `player` (`Player`)
- `userID` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `char*`

**Descripción oficial:**

```
Takes a 24 char buffer. Returns the buffer or "**Invalid**" if CPlayerInfo of the given player cannot be retrieved or the player doesn't exist.
```

**Nombres antiguos (alias):** `_NETWORK_PLAYER_GET_USER_ID` (`NetworkPlayerGetUserId`)

---
### NetworkPlayerHasHeadset

`NETWORK_PLAYER_HAS_HEADSET` · hash `0x3FB99A8B08D18FD6` · jhash `0x451FB6B6` · **Cliente**

```lua
local retval = NetworkPlayerHasHeadset(player)
```
```c
BOOL NETWORK_PLAYER_HAS_HEADSET(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### NetworkPlayerIndexIsCheater

`NETWORK_PLAYER_INDEX_IS_CHEATER` · hash `0x565E430DB3B05BEC` · jhash `0xD265B049` · **Cliente**

```lua
local retval = NetworkPlayerIndexIsCheater(player)
```
```c
BOOL NETWORK_PLAYER_INDEX_IS_CHEATER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x565E430DB3B05BEC` (`N_0x565e430db3b05bec`), `_NETWORK_PLAYER_SOMETHING` (`NetworkPlayerSomething`)

---
### NetworkPlayerIsBadsport

`NETWORK_PLAYER_IS_BADSPORT` · hash `0x19D8DA0E5A68045A` · jhash `0xA19708E3` · **Cliente**

```lua
local retval = NetworkPlayerIsBadsport()
```
```c
BOOL NETWORK_PLAYER_IS_BADSPORT();
```

**Devuelve:** `BOOL`

---
### NetworkPlayerIsCheater

`NETWORK_PLAYER_IS_CHEATER` · hash `0x655B91F1495A9090` · jhash `0xA51DC214` · **Cliente**

```lua
local retval = NetworkPlayerIsCheater()
```
```c
BOOL NETWORK_PLAYER_IS_CHEATER();
```

**Devuelve:** `BOOL`

---
### NetworkPlayerIsRockstarDev

`NETWORK_PLAYER_IS_ROCKSTAR_DEV` · hash `0x544ABDDA3B409B6D` · jhash `0xF6659045` · **Cliente**

```lua
local retval = NetworkPlayerIsRockstarDev(player)
```
```c
BOOL NETWORK_PLAYER_IS_ROCKSTAR_DEV(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if a specific value (BYTE) in CPlayerInfo is nonzero.  
Returns always false in Singleplayer.  
No longer used for dev checks since first mods were released on PS3 & 360.  
R* now checks with the is_dlc_present native for the dlc hash 2532323046,  
if that is present it will unlock dev stuff.  
```

---
### NetworkQueryRespawnResults

`NETWORK_QUERY_RESPAWN_RESULTS` · hash `0x3C891A251567DFCE` · jhash `0x90700C7D` · **Cliente**

```lua
local retval, p0 = NetworkQueryRespawnResults(p0)
```
```c
Any NETWORK_QUERY_RESPAWN_RESULTS(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x3C891A251567DFCE` (`N_0x3c891a251567dfce`)

---
### NetworkQueueGamerForStatus

`NETWORK_QUEUE_GAMER_FOR_STATUS` · hash `0x85A0EF54A500882C` · jhash `0x42BD0780` · **Cliente**

```lua
local retval, p0 = NetworkQueueGamerForStatus(p0)
```
```c
BOOL NETWORK_QUEUE_GAMER_FOR_STATUS(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x85A0EF54A500882C` (`N_0x85a0ef54a500882c`), `_NETWORK_GET_GAMER_STATUS` (`NetworkGetGamerStatus`)

---
### NetworkQuitMpToDesktop

`NETWORK_QUIT_MP_TO_DESKTOP` · hash `0x45A83257ED02D9BC` · **Cliente**

```lua
NetworkQuitMpToDesktop()
```
```c
void NETWORK_QUIT_MP_TO_DESKTOP();
```

**Devuelve:** `void`

**Descripción oficial:**

Forces the "Are you sure you want to quit Grand Theft Auto V?" warning message (Same as when you Alt+F4) to show.
Doesn't work in singleplayer.

**Nombres antiguos (alias):** `0x45A83257ED02D9BC` (`N_0x45a83257ed02d9bc`)

---
### NetworkRegisterEntityAsNetworked

`NETWORK_REGISTER_ENTITY_AS_NETWORKED` · hash `0x06FAACD625D80CAA` · jhash `0x31A630A4` · **Cliente**

```lua
NetworkRegisterEntityAsNetworked(entity)
```
```c
void NETWORK_REGISTER_ENTITY_AS_NETWORKED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x06FAACD625D80CAA` (`N_0x06faacd625d80caa`)

---
### NetworkRegisterHostBroadcastVariables

`NETWORK_REGISTER_HOST_BROADCAST_VARIABLES` · hash `0x3E9B2F01C50DF595` · jhash `0xDAF3B0AE` · **Cliente**

```lua
local vars = NetworkRegisterHostBroadcastVariables(numVars)
```
```c
void NETWORK_REGISTER_HOST_BROADCAST_VARIABLES(int* vars, int numVars);
```

**Parámetros**

- `vars` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `numVars` (`int`)

**Devuelve:** `void`

---
### NetworkRegisterPlayerBroadcastVariables

`NETWORK_REGISTER_PLAYER_BROADCAST_VARIABLES` · hash `0x3364AA97340CA215` · jhash `0xBE3D32B4` · **Cliente**

```lua
local vars = NetworkRegisterPlayerBroadcastVariables(numVars)
```
```c
void NETWORK_REGISTER_PLAYER_BROADCAST_VARIABLES(int* vars, int numVars);
```

**Parámetros**

- `vars` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `numVars` (`int`)

**Devuelve:** `void`

---
### NetworkRegisterTunableBoolHash

`_NETWORK_REGISTER_TUNABLE_BOOL_HASH` · hash `0x697F508861875B42` · **Cliente**

```lua
local retval, value = NetworkRegisterTunableBoolHash(contextHash, nameHash, value)
```
```c
BOOL _NETWORK_REGISTER_TUNABLE_BOOL_HASH(Hash contextHash, Hash nameHash, BOOL* value);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `nameHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`BOOL*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x697F508861875B42` (`N_0x697f508861875b42`)

---
### NetworkRegisterTunableFloatHash

`_NETWORK_REGISTER_TUNABLE_FLOAT_HASH` · hash `0x1950DAE9848A4739` · **Cliente**

```lua
local retval, value = NetworkRegisterTunableFloatHash(contextHash, nameHash, value)
```
```c
BOOL _NETWORK_REGISTER_TUNABLE_FLOAT_HASH(Hash contextHash, Hash nameHash, float* value);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `nameHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1950DAE9848A4739` (`N_0x1950dae9848a4739`)

---
### NetworkRegisterTunableIntHash

`_NETWORK_REGISTER_TUNABLE_INT_HASH` · hash `0x3A8B55FDA4C8DDEF` · **Cliente**

```lua
local retval, value = NetworkRegisterTunableIntHash(contextHash, nameHash, value)
```
```c
BOOL _NETWORK_REGISTER_TUNABLE_INT_HASH(Hash contextHash, Hash nameHash, int* value);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `nameHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3A8B55FDA4C8DDEF` (`N_0x3a8b55fda4c8ddef`)

---
### NetworkRemoveAllTransitionInvite

`NETWORK_REMOVE_ALL_TRANSITION_INVITE` · hash `0x726E0375C7A26368` · jhash `0xF7134E73` · **Cliente**

```lua
NetworkRemoveAllTransitionInvite()
```
```c
void NETWORK_REMOVE_ALL_TRANSITION_INVITE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x726E0375C7A26368` (`N_0x726e0375c7a26368`)

---
### NetworkRemoveEntityArea

`NETWORK_REMOVE_ENTITY_AREA` · hash `0x93CF869BAA0C4874` · jhash `0xEAB97F25` · **Cliente**

```lua
local retval = NetworkRemoveEntityArea(p0)
```
```c
BOOL NETWORK_REMOVE_ENTITY_AREA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkRemovePresenceInvite

`NETWORK_REMOVE_PRESENCE_INVITE` · hash `0xF0210268DB0974B1` · jhash `0x93C665FA` · **Cliente**

```lua
local retval = NetworkRemovePresenceInvite(p0)
```
```c
BOOL NETWORK_REMOVE_PRESENCE_INVITE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF0210268DB0974B1` (`N_0xf0210268db0974b1`)

---
### NetworkRemoveTransitionInvite

`NETWORK_REMOVE_TRANSITION_INVITE` · hash `0x7524B431B2E6F7EE` · jhash `0xFDE84CB7` · **Cliente**

```lua
local p0 = NetworkRemoveTransitionInvite(p0)
```
```c
void NETWORK_REMOVE_TRANSITION_INVITE(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### NetworkReportMyself

`_NETWORK_REPORT_MYSELF` · hash `0x5626D9D6810730D5` · **Cliente**

```lua
NetworkReportMyself()
```
```c
void _NETWORK_REPORT_MYSELF();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5626D9D6810730D5` (`N_0x5626d9d6810730d5`)

---
### NetworkRequestCloudBackgroundScripts

`NETWORK_REQUEST_CLOUD_BACKGROUND_SCRIPTS` · hash `0x924426BFFD82E915` · jhash `0x98EFB921` · **Cliente**

```lua
local retval = NetworkRequestCloudBackgroundScripts()
```
```c
BOOL NETWORK_REQUEST_CLOUD_BACKGROUND_SCRIPTS();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x924426BFFD82E915` (`N_0x924426bffd82e915`), `_NETWORK_REQUEST_CLOUD_BACKGROUND_SCRIPTS` (`NetworkRequestCloudBackgroundScripts`)

---
### NetworkRequestCloudTunables

`NETWORK_REQUEST_CLOUD_TUNABLES` · hash `0x42FB3B532D526E6C` · jhash `0xD760CAD5` · **Cliente**

```lua
NetworkRequestCloudTunables()
```
```c
void NETWORK_REQUEST_CLOUD_TUNABLES();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x42FB3B532D526E6C` (`N_0x42fb3b532d526e6c`)

---
### NetworkRequestControlOfDoor

`NETWORK_REQUEST_CONTROL_OF_DOOR` · hash `0x870DDFD5A4A796E4` · jhash `0xF60DAAF6` · **Cliente**

```lua
local retval = NetworkRequestControlOfDoor(doorID)
```
```c
BOOL NETWORK_REQUEST_CONTROL_OF_DOOR(int doorID);
```

**Parámetros**

- `doorID` (`int`)

**Devuelve:** `BOOL`

---
### NetworkRequestControlOfEntity

`NETWORK_REQUEST_CONTROL_OF_ENTITY` · hash `0xB69317BF5E782347` · jhash `0xA05FEBD7` · **Cliente**

```lua
local retval = NetworkRequestControlOfEntity(entity)
```
```c
BOOL NETWORK_REQUEST_CONTROL_OF_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### NetworkRequestControlOfNetworkId

`NETWORK_REQUEST_CONTROL_OF_NETWORK_ID` · hash `0xA670B3662FAFFBD0` · jhash `0x9262A60A` · **Cliente**

```lua
local retval = NetworkRequestControlOfNetworkId(netId)
```
```c
BOOL NETWORK_REQUEST_CONTROL_OF_NETWORK_ID(int netId);
```

**Parámetros**

- `netId` (`int`)

**Devuelve:** `BOOL`

---
### NetworkResetBodyTracker

`NETWORK_RESET_BODY_TRACKER` · hash `0x72433699B4E6DD64` · jhash `0x3914463F` · **Cliente**

```lua
NetworkResetBodyTracker()
```
```c
void NETWORK_RESET_BODY_TRACKER();
```

**Devuelve:** `void`

---
### NetworkRespawnCoords

`_NETWORK_RESPAWN_COORDS` · hash `0x9769F811D1785B03` · jhash `0xBE6A30C3` · **Cliente**

```lua
NetworkRespawnCoords(player, x, y, z, p4, p5)
```
```c
void _NETWORK_RESPAWN_COORDS(Player player, float x, float y, float z, BOOL p4, BOOL p5);
```

**Parámetros**

- `player` (`Player`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p4 and p5 are always 0 in scripts  
```

**Nombres antiguos (alias):** `0x9769F811D1785B03` (`N_0x9769f811d1785b03`)

---
### NetworkResurrectLocalPlayer

`NETWORK_RESURRECT_LOCAL_PLAYER` · hash `0xEA23C49EAA83ACFB` · jhash `0xF1F9D4B4` · **Cliente**

```lua
NetworkResurrectLocalPlayer(x, y, z, heading, nInvincibilityTime, bLeaveDeadPed)
```
```c
void NETWORK_RESURRECT_LOCAL_PLAYER(float x, float y, float z, float heading, int nInvincibilityTime, BOOL bLeaveDeadPed);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `nInvincibilityTime` (`int`): This is the length of time in milliseconds that the player will be invincible for after resurrection.
- `bLeaveDeadPed` (`BOOL`): Leaves the dead ped behind when resurrecting.

**Devuelve:** `void`

**Descripción oficial:**

Revives our local player who was previously dead.

**Note:** Call this once you resurrect the player (this does not need to be called every frame).

```cpp
enum ePlayerSpawnLocation {
  // system will decide
  SPAWN_LOCATION_AUTOMATIC = 0,
  SPAWN_LOCATION_NEAR_DEATH = 1,
  SPAWN_LOCATION_NEAR_TEAM_MATES = 2,
  // script defined area
  SPAWN_LOCATION_MISSION_AREA = 3,
  SPAWN_LOCATION_NEAR_OTHER_PLAYERS = 4,
  SPAWN_LOCATION_NEAR_CURRENT_POSITION = 5,
  SPAWN_LOCATION_AT_CURRENT_POSITION = 6,
  SPAWN_LOCATION_NET_TEST_BED = 7,
  SPAWN_LOCATION_CUSTOM_SPAWN_POINTS = 8,
  SPAWN_LOCATION_OUTSIDE_SIMEON_GARAGE = 9,
  SPAWN_LOCATION_NEAR_SPECIFIC_COORDS = 10,
  SPAWN_LOCATION_AT_SPECIFIC_COORDS = 11,
  SPAWN_LOCATION_AT_AIRPORT_ARRIVALS = 12,
  SPAWN_LOCATION_AT_SPECIFIC_COORDS_IF_POSSIBLE = 13,
  SPAWN_LOCATION_IN_SPECIFIC_ANGLED_AREA = 14,
  SPAWN_LOCATION_NEAREST_RESPAWN_POINT = 15,
  SPAWN_LOCATION_AT_SPECIFIC_COORDS_RACE_CORONA = 16,
  SPAWN_LOCATION_INSIDE_GARAGE = 17,
  SPAWN_LOCATION_INSIDE_PROPERTY = 18,
  SPAWN_LOCATION_INSIDE_PROPERTY_OR_GARAGE = 19,
  SPAWN_LOCATION_NEAR_DEATH_IMPROMPTU = 20,
  SPAWN_LOCATION_NEAR_CURRENT_POSITION_SPREAD_OUT = 21,
  SPAWN_LOCATION_NEAREST_RESPAWN_POINT_TO_SPECIFIC_COORDS = 22,
  SPAWN_LOCATION_NEAREST_HOSPITAL = 23,
  SPAWN_LOCATION_NEAREST_POLICE_STATION = 24,
  SPAWN_LOCATION_NEAREST_HOTEL_TO_SPECIFIC_COORDS = 25,
  SPAWN_LOCATION_MISSION_AREA_NEAR_CURRENT_POSITION = 26,
  SPAWN_LOCATION_PRIVATE_YACHT = 27,
  SPAWN_LOCATION_PRIVATE_YACHT_APARTMENT = 28,
  SPAWN_LOCATION_PRIVATE_FRIEND_YACHT = 29,
  SPAWN_LOCATION_PRIVATE_YACHT_NEAR_SHORE = 30,
  SPAWN_LOCATION_NEAR_GANG_BOSS = 31,
  SPAWN_LOCATION_NEAR_SPECIFIC_COORDS_WITH_GANG = 32,
  SPAWN_LOCATION_GANG_DM = 33,
  SPAWN_LOCATION_GANG_BOSS_PRIVATE_YACHT = 34,
  SPAWN_LOCATION_OFFICE = 35,
  SPAWN_LOCATION_CLUBHOUSE = 36,
  SPAWN_LOCATION_NEAR_CURRENT_POSITION_AS_POSSIBLE = 37,
  SPAWN_LOCATION_NEAR_CURRENT_PERCEIVED_POSITION = 38,
  SPAWN_LOCATION_IE_WAREHOUSE = 39,
  SPAWN_LOCATION_BUNKER = 40,
  SPAWN_LOCATION_HANGAR = 41,
  SPAWN_LOCATION_DEFUNCT_BASE = 42,
  SPAWN_LOCATION_NIGHTCLUB = 43,
  SPAWN_LOCATION_ARENA_GARAGE = 44,
  SPAWN_LOCATION_CASINO = 45,
  SPAWN_LOCATION_CASINO_APARTMENT = 46,
  SPAWN_LOCATION_CASINO_OUTSIDE = 47,
  SPAWN_LOCATION_ARCADE = 48,
  SPAWN_LOCATION_CASINO_NIGHTCLUB = 49,
  SPAWN_LOCATION_SUBMARINE = 50,
  SPAWN_LOCATION_HEIST_ISLAND_NEAR_DEATH = 51,
  SPAWN_LOCATION_HEIST_ISLAND_BEACH_PARTY = 52,
  SPAWN_LOCATION_LAND_NEAR_SUBMARINE = 53,
  SPAWN_LOCATION_CAR_MEET = 54,
  SPAWN_LOCATION_AUTO_SHOP = 55,
  SPAWN_LOCATION_FIXER_HQ = 56,
  SPAWN_LOCATION_SITTING_SMOKING = 57,
  SPAWN_LOCATION_DRUNK_WAKE_UP_MUSIC_STUDIO = 58,
  SPAWN_LOCATION_MUSIC_STUDIO = 59,
  TOTAL_SPAWN_LOCATIONS = 60
};
```

```cpp
enum eSpawnReason {
  SPAWN_REASON_DEATH = 0,
  SPAWN_REASON_TRANSITION,
  SPAWN_REASON_MANUAL,
  SPAWN_REASON_RESTORE_CHARACTER,
  SPAWN_REASON_IN_VEHICLE
};
```

**Added parameters**

*   **bUnpauseRenderPhases**: This boolean parameter will unpause the render phases when set to `true`.
*   **iSpawnLocation**: This integer parameter sets the player's spawn location metric for telemetry. See `ePlayerSpawnLocation` enum.
*   **iSpawnReason**: This integer parameter sets the player's spawn reason metric for telemetry. See `eSpawnReason` enum.

---
### NetworkSeedRandomNumberGenerator

`NETWORK_SEED_RANDOM_NUMBER_GENERATOR` · hash `0xF1B84178F8674195` · jhash `0x41702C8A` · **Cliente**

```lua
NetworkSeedRandomNumberGenerator(seed)
```
```c
void NETWORK_SEED_RANDOM_NUMBER_GENERATOR(int seed);
```

**Parámetros**

- `seed` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF1B84178F8674195` (`N_0xf1b84178f8674195`)

---
### NetworkSendInviteViaPresence

`NETWORK_SEND_INVITE_VIA_PRESENCE` · hash `0xC3C7A6AFDB244624` · jhash `0x8B99B72B` · **Cliente**

```lua
local retval, networkHandle, p1 = NetworkSendInviteViaPresence(p2, p3)
```
```c
BOOL NETWORK_SEND_INVITE_VIA_PRESENCE(int* networkHandle, Any* p1, Any p2, Any p3);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC3C7A6AFDB244624` (`N_0xc3c7a6afdb244624`), `_NETWORK_SEND_PRESENCE_INVITE` (`NetworkSendPresenceInvite`)

---
### NetworkSendPresenceTransitionInvite

`_NETWORK_SEND_PRESENCE_TRANSITION_INVITE` · hash `0xC116FF9B4D488291` · jhash `0x877C0E1C` · **Cliente**

```lua
local retval, p0, p1 = NetworkSendPresenceTransitionInvite(p2, p3)
```
```c
BOOL _NETWORK_SEND_PRESENCE_TRANSITION_INVITE(Any* p0, Any* p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
String "NETWORK_SEND_PRESENCE_TRANSITION_INVITE" is contained in the function in ida so this one is correct.  
```

**Nombres antiguos (alias):** `0xC116FF9B4D488291` (`N_0xc116ff9b4d488291`)

---
### NetworkSendTextMessage

`NETWORK_SEND_TEXT_MESSAGE` · hash `0x3A214F2EC889B100` · jhash `0xAFFEA720` · **Cliente**

```lua
local retval, networkHandle = NetworkSendTextMessage(message, networkHandle)
```
```c
BOOL NETWORK_SEND_TEXT_MESSAGE(char* message, int* networkHandle);
```

**Parámetros**

- `message` (`char*`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Message is limited to 64 characters.
```

---
### NetworkSendTransitionGamerInstruction

`NETWORK_SEND_TRANSITION_GAMER_INSTRUCTION` · hash `0x31D1D2B858D25E6B` · jhash `0x468B0884` · **Cliente**

```lua
local retval, networkHandle = NetworkSendTransitionGamerInstruction(p1, p2, p3, p4)
```
```c
BOOL NETWORK_SEND_TRANSITION_GAMER_INSTRUCTION(int* networkHandle, char* p1, int p2, int p3, BOOL p4);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`char*`)
- `p2` (`int`)
- `p3` (`int`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
the first arg seems to be the network player handle (&handle) and the second var is pretty much always "" and the third seems to be a number between 0 and ~10 and the 4th is is something like 0 to 5 and I guess the 5th is a bool cuz it is always 0 or 1  
does this send an invite to a player?  
```

---
### NetworkSessionActivityQuickmatch

`NETWORK_SESSION_ACTIVITY_QUICKMATCH` · hash `0xBE3E347A87ACEB82` · jhash `0x3F75CC38` · **Cliente**

```lua
local retval = NetworkSessionActivityQuickmatch(p0, p1, p2, p3)
```
```c
BOOL NETWORK_SESSION_ACTIVITY_QUICKMATCH(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBE3E347A87ACEB82` (`N_0xbe3e347a87aceb82`)

---
### NetworkSessionAddActiveMatchmakingGroup

`NETWORK_SESSION_ADD_ACTIVE_MATCHMAKING_GROUP` · hash `0xCAE55F48D3D7875C` · jhash `0x5BE529F7` · **Cliente**

```lua
NetworkSessionAddActiveMatchmakingGroup(groupId)
```
```c
void NETWORK_SESSION_ADD_ACTIVE_MATCHMAKING_GROUP(int groupId);
```

**Parámetros**

- `groupId` (`int`): An identifier value between zero and four

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCAE55F48D3D7875C` (`N_0xcae55f48d3d7875c`)

---
### NetworkSessionBlockJoinRequests

`NETWORK_SESSION_BLOCK_JOIN_REQUESTS` · hash `0xA73667484D7037C3` · jhash `0xE6EEF8AF` · **Cliente**

```lua
NetworkSessionBlockJoinRequests(toggle)
```
```c
void NETWORK_SESSION_BLOCK_JOIN_REQUESTS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA73667484D7037C3` (`N_0xa73667484d7037c3`)

---
### NetworkSessionCancelInvite

`NETWORK_SESSION_CANCEL_INVITE` · hash `0x2FBF47B1B36D36F9` · jhash `0x20317535` · **Cliente**

```lua
NetworkSessionCancelInvite()
```
```c
void NETWORK_SESSION_CANCEL_INVITE();
```

**Devuelve:** `void`

---
### NetworkSessionChangeSlots

`NETWORK_SESSION_CHANGE_SLOTS` · hash `0xB4AB419E0D86ACAE` · jhash `0x6BB93227` · **Cliente**

```lua
NetworkSessionChangeSlots(p0, p1)
```
```c
void NETWORK_SESSION_CHANGE_SLOTS(int p0, BOOL p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB4AB419E0D86ACAE` (`N_0xb4ab419e0d86acae`)

---
### NetworkSessionCrewMatchmaking

`NETWORK_SESSION_CREW_MATCHMAKING` · hash `0x94BC51E9449D917F` · jhash `0xD7624E6B` · **Cliente**

```lua
local retval = NetworkSessionCrewMatchmaking(p0, p1, p2, maxPlayers, p4)
```
```c
BOOL NETWORK_SESSION_CREW_MATCHMAKING(int p0, int p1, int p2, int maxPlayers, BOOL p4);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`int`)
- `maxPlayers` (`int`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x94BC51E9449D917F` (`N_0x94bc51e9449d917f`)

---
### NetworkSessionEnd

`NETWORK_SESSION_END` · hash `0xA02E59562D711006` · jhash `0xBCACBEA2` · **Cliente**

```lua
local retval = NetworkSessionEnd(p0, p1)
```
```c
BOOL NETWORK_SESSION_END(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p0 is always false and p1 varies.  
NETWORK_SESSION_END(0, 1)  
NETWORK_SESSION_END(0, 0)  
Results in: "Connection to session lost due to an unknown network error. Please return to Grand Theft Auto V and try again later."  
```

---
### NetworkSessionEnter

`NETWORK_SESSION_ENTER` · hash `0x330ED4D05491934F` · jhash `0x543CD2BE` · **Cliente**

```lua
local retval = NetworkSessionEnter(p0, p1, p2, maxPlayers, p4, p5)
```
```c
Any NETWORK_SESSION_ENTER(Any p0, Any p1, Any p2, int maxPlayers, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `maxPlayers` (`int`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
unknown params  
p0 = 0, 2, or 999 (The global is 999 by default.)  
p1 = 0 (Always in every script it's found in atleast.)  
p2 = 0, 3, or 4 (Based on a var that is determined by a function.)  
p3 = maxPlayers (It's obvious in x360 scripts it's always 18)  
p4 = 0 (Always in every script it's found in atleast.)  
p5 = 0 or 1. (1 if network_can_enter_multiplayer, but set to 0 if other checks after that are passed.)  
p5 is reset to 0 if,  
Global_1315318 = 0 or Global_1315323 = 9 or 12 or (Global_1312629 = 0 && Global_1312631 = true/1) those are passed.  
```

---
### NetworkSessionForceCancelInvite

`NETWORK_SESSION_FORCE_CANCEL_INVITE` · hash `0xA29177F7703B5644` · jhash `0x3FD49D3B` · **Cliente**

```lua
NetworkSessionForceCancelInvite()
```
```c
void NETWORK_SESSION_FORCE_CANCEL_INVITE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA29177F7703B5644` (`N_0xa29177f7703b5644`)

---
### NetworkSessionFriendMatchmaking

`NETWORK_SESSION_FRIEND_MATCHMAKING` · hash `0x2CFC76E0D087C994` · jhash `0x4E53202A` · **Cliente**

```lua
local retval = NetworkSessionFriendMatchmaking(p0, p1, maxPlayers, p3)
```
```c
BOOL NETWORK_SESSION_FRIEND_MATCHMAKING(int p0, int p1, int maxPlayers, BOOL p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `maxPlayers` (`int`)
- `p3` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2CFC76E0D087C994` (`N_0x2cfc76e0d087c994`)

---
### NetworkSessionGetInviter

`NETWORK_SESSION_GET_INVITER` · hash `0xE57397B4A3429DD0` · jhash `0xE9C6B3FD` · **Cliente**

```lua
local networkHandle = NetworkSessionGetInviter(networkHandle)
```
```c
void NETWORK_SESSION_GET_INVITER(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### NetworkSessionGetKickVote

`NETWORK_SESSION_GET_KICK_VOTE` · hash `0xD6D09A6F32F49EF1` · jhash `0x8A559D26` · **Cliente**

```lua
local retval = NetworkSessionGetKickVote(player)
```
```c
BOOL NETWORK_SESSION_GET_KICK_VOTE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_NETWORK_SESSION_ARE_PLAYERS_VOTING_TO_KICK` (`NetworkSessionArePlayersVotingToKick`), `_NETWORK_SESSION_IS_PLAYER_VOTED_TO_KICK` (`NetworkSessionIsPlayerVotedToKick`)

---
### NetworkSessionGetMatchmakingGroupFree

`NETWORK_SESSION_GET_MATCHMAKING_GROUP_FREE` · hash `0x56CE820830EF040B` · jhash `0x36EAD960` · **Cliente**

```lua
local retval = NetworkSessionGetMatchmakingGroupFree(p0)
```
```c
int NETWORK_SESSION_GET_MATCHMAKING_GROUP_FREE(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x56CE820830EF040B` (`N_0x56ce820830ef040b`), `_NETWORK_SESSION_GET_UNK` (`NetworkSessionGetUnk`)

---
### NetworkSessionGetPrivateSlots

`NETWORK_SESSION_GET_PRIVATE_SLOTS` · hash `0x53AFD64C6758F2F9` · jhash `0xE642F2FD` · **Cliente**

```lua
local retval = NetworkSessionGetPrivateSlots()
```
```c
int NETWORK_SESSION_GET_PRIVATE_SLOTS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x53AFD64C6758F2F9` (`N_0x53afd64c6758f2f9`)

---
### NetworkSessionHost

`NETWORK_SESSION_HOST` · hash `0x6F3D4ED9BEE4E61D` · jhash `0x6716460F` · **Cliente**

```lua
local retval = NetworkSessionHost(p0, maxPlayers, p2)
```
```c
BOOL NETWORK_SESSION_HOST(int p0, int maxPlayers, BOOL p2);
```

**Parámetros**

- `p0` (`int`)
- `maxPlayers` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Does nothing in online but in offline it will cause the screen to fade to black. Nothing happens past then, the screen will sit at black until you restart GTA. Other stuff must be needed to actually host a session.  
```

---
### NetworkSessionHostClosed

`NETWORK_SESSION_HOST_CLOSED` · hash `0xED34C0C02C098BB7` · jhash `0x8AC9EA19` · **Cliente**

```lua
local retval = NetworkSessionHostClosed(p0, maxPlayers)
```
```c
BOOL NETWORK_SESSION_HOST_CLOSED(int p0, int maxPlayers);
```

**Parámetros**

- `p0` (`int`)
- `maxPlayers` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xED34C0C02C098BB7` (`N_0xed34c0c02c098bb7`)

---
### NetworkSessionHostFriendsOnly

`NETWORK_SESSION_HOST_FRIENDS_ONLY` · hash `0xB9CFD27A5D578D83` · jhash `0x26864403` · **Cliente**

```lua
local retval = NetworkSessionHostFriendsOnly(p0, maxPlayers)
```
```c
BOOL NETWORK_SESSION_HOST_FRIENDS_ONLY(int p0, int maxPlayers);
```

**Parámetros**

- `p0` (`int`)
- `maxPlayers` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Does nothing in online but in offline it will cause the screen to fade to black. Nothing happens past then, the screen will sit at black until you restart GTA. Other stuff must be needed to actually host a session.  
```

---
### NetworkSessionHostSinglePlayer

`NETWORK_SESSION_HOST_SINGLE_PLAYER` · hash `0xC74C33FCA52856D5` · jhash `0xF3B1CA85` · **Cliente**

```lua
NetworkSessionHostSinglePlayer(p0)
```
```c
void NETWORK_SESSION_HOST_SINGLE_PLAYER(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Loads up the map that is loaded when beeing in mission creator  
Player gets placed in a mix between online/offline mode  
p0 is always 2 in R* scripts.  
Appears to be patched in gtav b757 (game gets terminated) alonside with most other network natives to prevent online modding ~ghost30812  
```

---
### NetworkSessionIsClosedCrew

`NETWORK_SESSION_IS_CLOSED_CREW` · hash `0x74732C6CA90DA2B4` · jhash `0xA95299B9` · **Cliente**

```lua
local retval = NetworkSessionIsClosedCrew()
```
```c
BOOL NETWORK_SESSION_IS_CLOSED_CREW();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x74732C6CA90DA2B4` (`N_0x74732c6ca90da2b4`)

---
### NetworkSessionIsClosedFriends

`NETWORK_SESSION_IS_CLOSED_FRIENDS` · hash `0xFBCFA2EA2E206890` · jhash `0x56E75FE4` · **Cliente**

```lua
local retval = NetworkSessionIsClosedFriends()
```
```c
BOOL NETWORK_SESSION_IS_CLOSED_FRIENDS();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFBCFA2EA2E206890` (`N_0xfbcfa2ea2e206890`)

---
### NetworkSessionIsInVoiceSession

`NETWORK_SESSION_IS_IN_VOICE_SESSION` · hash `0x855BC38818F6F684` · jhash `0x60AA4AA1` · **Cliente**

```lua
local retval = NetworkSessionIsInVoiceSession()
```
```c
BOOL NETWORK_SESSION_IS_IN_VOICE_SESSION();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x855BC38818F6F684` (`N_0x855bc38818f6f684`)

---
### NetworkSessionIsPrivate

`NETWORK_SESSION_IS_PRIVATE` · hash `0xCEF70AA5B3F89BA1` · jhash `0xDB67785D` · **Cliente**

```lua
local retval = NetworkSessionIsPrivate()
```
```c
BOOL NETWORK_SESSION_IS_PRIVATE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCEF70AA5B3F89BA1` (`N_0xcef70aa5b3f89ba1`)

---
### NetworkSessionIsSolo

`NETWORK_SESSION_IS_SOLO` · hash `0xF3929C2379B60CCE` · jhash `0x3D2C1916` · **Cliente**

```lua
local retval = NetworkSessionIsSolo()
```
```c
BOOL NETWORK_SESSION_IS_SOLO();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF3929C2379B60CCE` (`N_0xf3929c2379b60cce`)

---
### NetworkSessionIsVisible

`NETWORK_SESSION_IS_VISIBLE` · hash `0xBA416D68C631496A` · jhash `0x4977AC28` · **Cliente**

```lua
local retval = NetworkSessionIsVisible()
```
```c
BOOL NETWORK_SESSION_IS_VISIBLE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBA416D68C631496A` (`N_0xba416d68c631496a`)

---
### NetworkSessionIsVoiceSessionBusy

`NETWORK_SESSION_IS_VOICE_SESSION_BUSY` · hash `0xEF0912DDF7C4CB4B` · jhash `0x132CA01E` · **Cliente**

```lua
local retval = NetworkSessionIsVoiceSessionBusy()
```
```c
BOOL NETWORK_SESSION_IS_VOICE_SESSION_BUSY();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEF0912DDF7C4CB4B` (`N_0xef0912ddf7c4cb4b`)

---
### NetworkSessionJoinInvite

`NETWORK_SESSION_JOIN_INVITE` · hash `0xC6F8AB8A4189CF3A` · jhash `0x3D6360B5` · **Cliente**

```lua
NetworkSessionJoinInvite()
```
```c
void NETWORK_SESSION_JOIN_INVITE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `NETWORK_IS_PLAYER_ANIMATION_DRAWING_SYNCHRONIZED` (`NetworkIsPlayerAnimationDrawingSynchronized`)

---
### NetworkSessionKickPlayer

`NETWORK_SESSION_KICK_PLAYER` · hash `0xFA8904DC5F304220` · jhash `0x1E20138A` · **Cliente**

```lua
NetworkSessionKickPlayer(player)
```
```c
void NETWORK_SESSION_KICK_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only works as host.
```

---
### NetworkSessionLeaveSinglePlayer

`NETWORK_SESSION_LEAVE_SINGLE_PLAYER` · hash `0x3442775428FD2DAA` · jhash `0xC692F86A` · **Cliente**

```lua
NetworkSessionLeaveSinglePlayer()
```
```c
void NETWORK_SESSION_LEAVE_SINGLE_PLAYER();
```

**Devuelve:** `void`

---
### NetworkSessionMarkVisible

`NETWORK_SESSION_MARK_VISIBLE` · hash `0x271CC6AB59EBF9A5` · jhash `0x7017257D` · **Cliente**

```lua
NetworkSessionMarkVisible(toggle)
```
```c
void NETWORK_SESSION_MARK_VISIBLE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x271CC6AB59EBF9A5` (`N_0x271cc6ab59ebf9a5`)

---
### NetworkSessionSetMatchmakingGroup

`NETWORK_SESSION_SET_MATCHMAKING_GROUP` · hash `0x49EC8030F5015F8B` · jhash `0x3C3E2AB6` · **Cliente**

```lua
NetworkSessionSetMatchmakingGroup(matchmakingGroup)
```
```c
void NETWORK_SESSION_SET_MATCHMAKING_GROUP(int matchmakingGroup);
```

**Parámetros**

- `matchmakingGroup` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x49EC8030F5015F8B` (`N_0x49ec8030f5015f8b`), `_NETWORK_SCTV_SLOTS` (`NetworkSctvSlots`)

---
### NetworkSessionSetMatchmakingGroupMax

`NETWORK_SESSION_SET_MATCHMAKING_GROUP_MAX` · hash `0x8B6A4DD0AF9CE215` · jhash `0x5F29A7E0` · **Cliente**

```lua
NetworkSessionSetMatchmakingGroupMax(playerType, playerCount)
```
```c
void NETWORK_SESSION_SET_MATCHMAKING_GROUP_MAX(int playerType, int playerCount);
```

**Parámetros**

- `playerType` (`int`)
- `playerCount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
playerTypes:
0 = regular joiner
4 = spectator
8 = unknown
```

**Nombres antiguos (alias):** `0x8B6A4DD0AF9CE215` (`N_0x8b6a4dd0af9ce215`), `_NETWORK_SESSION_SET_MAX_PLAYERS` (`NetworkSessionSetMaxPlayers`)

---
### NetworkSessionSetMatchmakingMentalState

`NETWORK_SESSION_SET_MATCHMAKING_MENTAL_STATE` · hash `0xF1EEA2DDA9FFA69D` · jhash `0x6CC062FC` · **Cliente**

```lua
NetworkSessionSetMatchmakingMentalState(p0)
```
```c
void NETWORK_SESSION_SET_MATCHMAKING_MENTAL_STATE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF1EEA2DDA9FFA69D` (`N_0xf1eea2dda9ffa69d`)

---
### NetworkSessionSetMatchmakingPropertyId

`NETWORK_SESSION_SET_MATCHMAKING_PROPERTY_ID` · hash `0x3F52E880AAF6C8CA` · jhash `0xB3D9A67F` · **Cliente**

```lua
NetworkSessionSetMatchmakingPropertyId(p0)
```
```c
void NETWORK_SESSION_SET_MATCHMAKING_PROPERTY_ID(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3F52E880AAF6C8CA` (`N_0x3f52e880aaf6c8ca`)

---
### NetworkSessionValidateJoin

`NETWORK_SESSION_VALIDATE_JOIN` · hash `0xC19F6C8E7865A6FF` · jhash `0xF3768F90` · **Cliente**

```lua
NetworkSessionValidateJoin(p0)
```
```c
void NETWORK_SESSION_VALIDATE_JOIN(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC19F6C8E7865A6FF` (`N_0xc19f6c8e7865a6ff`), `_NETWORK_SESSION_HOSTED` (`NetworkSessionHosted`)

---
### NetworkSessionVoiceConnectToPlayer

`NETWORK_SESSION_VOICE_CONNECT_TO_PLAYER` · hash `0xABD5E88B8A2D3DB2` · jhash `0x9DFD89E6` · **Cliente**

```lua
local globalPtr = NetworkSessionVoiceConnectToPlayer(globalPtr)
```
```c
void NETWORK_SESSION_VOICE_CONNECT_TO_PLAYER(Any* globalPtr);
```

**Parámetros**

- `globalPtr` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Only one occurence in the scripts:
auto sub_cb43(auto a_0, auto a_1) {
    if (g_2594CB._f1) {
        if (NETWORK::_855BC38818F6F684()) {
            NETWORK::_ABD5E88B8A2D3DB2(&a_0._fB93);
            g_2594CB._f14/*{13}*/ = a_0._fB93;
            g_2594CB._f4/*"64"*/ = a_1;
            return 1;
        }
    }
    return 0;
}
other:
looks like it passes a player in the paramater
Contains string "NETWORK_VOICE_CONNECT_TO_PLAYER" in ida
```

**Nombres antiguos (alias):** `0xABD5E88B8A2D3DB2` (`N_0xabd5e88b8a2d3db2`), `_NETWORK_VOICE_CONNECT_TO_PLAYER` (`NetworkVoiceConnectToPlayer`)

---
### NetworkSessionVoiceHost

`NETWORK_SESSION_VOICE_HOST` · hash `0x9C1556705F864230` · jhash `0x345C2980` · **Cliente**

```lua
NetworkSessionVoiceHost()
```
```c
void NETWORK_SESSION_VOICE_HOST();
```

**Devuelve:** `void`

---
### NetworkSessionVoiceLeave

`NETWORK_SESSION_VOICE_LEAVE` · hash `0x6793E42BE02B575D` · jhash `0xE566C7DA` · **Cliente**

```lua
NetworkSessionVoiceLeave()
```
```c
void NETWORK_SESSION_VOICE_LEAVE();
```

**Devuelve:** `void`

---
### NetworkSessionVoiceRespondToRequest

`NETWORK_SESSION_VOICE_RESPOND_TO_REQUEST` · hash `0x7F8413B7FC2AA6B9` · jhash `0x075321B5` · **Cliente**

```lua
NetworkSessionVoiceRespondToRequest(p0, p1)
```
```c
void NETWORK_SESSION_VOICE_RESPOND_TO_REQUEST(BOOL p0, int p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `NETWORK_SET_KEEP_FOCUSPOINT` (`NetworkSetKeepFocuspoint`)

---
### NetworkSessionVoiceSetTimeout

`NETWORK_SESSION_VOICE_SET_TIMEOUT` · hash `0x5B8ED3DB018927B1` · jhash `0x6EFC2FD0` · **Cliente**

```lua
NetworkSessionVoiceSetTimeout(timeout)
```
```c
void NETWORK_SESSION_VOICE_SET_TIMEOUT(int timeout);
```

**Parámetros**

- `timeout` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_0x5B8ED3DB018927B1` (`N_0x5b8ed3db018927b1`)

---
### NetworkSessionWasInvited

`NETWORK_SESSION_WAS_INVITED` · hash `0x23DFB504655D0CE4` · jhash `0x6A0BEA60` · **Cliente**

```lua
local retval = NetworkSessionWasInvited()
```
```c
BOOL NETWORK_SESSION_WAS_INVITED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x23DFB504655D0CE4` (`N_0x23dfb504655d0ce4`)

---
### NetworkSetActivityPlayerMax

`NETWORK_SET_ACTIVITY_PLAYER_MAX` · hash `0x0E4F77F7B9D74D84` · jhash `0x04CB2AB4` · **Cliente**

```lua
NetworkSetActivityPlayerMax(playerCount)
```
```c
void NETWORK_SET_ACTIVITY_PLAYER_MAX(int playerCount);
```

**Parámetros**

- `playerCount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0E4F77F7B9D74D84` (`N_0x0e4f77f7b9d74d84`)

---
### NetworkSetActivitySpectator

`NETWORK_SET_ACTIVITY_SPECTATOR` · hash `0x75138790B4359A74` · jhash `0xFC9AD060` · **Cliente**

```lua
NetworkSetActivitySpectator(toggle)
```
```c
void NETWORK_SET_ACTIVITY_SPECTATOR(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetActivitySpectatorMax

`NETWORK_SET_ACTIVITY_SPECTATOR_MAX` · hash `0x9D277B76D1D12222` · jhash `0x74E0BC0A` · **Cliente**

```lua
NetworkSetActivitySpectatorMax(maxSpectators)
```
```c
void NETWORK_SET_ACTIVITY_SPECTATOR_MAX(int maxSpectators);
```

**Parámetros**

- `maxSpectators` (`int`)

**Devuelve:** `void`

---
### NetworkSetChoiceMigrateOptions

`NETWORK_SET_CHOICE_MIGRATE_OPTIONS` · hash `0x5C707A667DF8B9FA` · jhash `0x64235620` · **Cliente**

```lua
NetworkSetChoiceMigrateOptions(toggle, player)
```
```c
void NETWORK_SET_CHOICE_MIGRATE_OPTIONS(BOOL toggle, Player player);
```

**Parámetros**

- `toggle` (`BOOL`)
- `player` (`Player`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5C707A667DF8B9FA` (`N_0x5c707a667df8b9fa`)

---
### NetworkSetCurrentDataManagerHandle

`_NETWORK_SET_CURRENT_DATA_MANAGER_HANDLE` · hash `0x796A87B3B68D1F3D` · **Cliente**

```lua
local retval, p0 = NetworkSetCurrentDataManagerHandle(p0)
```
```c
BOOL _NETWORK_SET_CURRENT_DATA_MANAGER_HANDLE(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x796A87B3B68D1F3D` (`N_0x796a87b3b68d1f3d`), `_NETWORK_CHECK_DATA_MANAGER_FOR_HANDLE` (`NetworkCheckDataManagerForHandle`)

---
### NetworkSetCurrentMissionId

`_NETWORK_SET_CURRENT_MISSION_ID` · hash `0x2C863ACDCD12B3DB` · **Cliente**

```lua
NetworkSetCurrentMissionId(missionId)
```
```c
void _NETWORK_SET_CURRENT_MISSION_ID(char* missionId);
```

**Parámetros**

- `missionId` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkSetCurrentSpawnSetting

`_NETWORK_SET_CURRENT_SPAWN_SETTING` · hash `0xAA6D5451DC3448B6` · **Cliente**

```lua
NetworkSetCurrentSpawnSetting(mpSettingSpawn)
```
```c
void _NETWORK_SET_CURRENT_SPAWN_SETTING(Hash mpSettingSpawn);
```

**Parámetros**

- `mpSettingSpawn` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eMpSettingSpawn
{
	MP_SETTING_SPAWN_NULL = 0,
	MP_SETTING_SPAWN_PROPERTY = 1,
	MP_SETTING_SPAWN_LAST_POSITION = 2,
	MP_SETTING_SPAWN_GARAGE = 3,
	MP_SETTING_SPAWN_RANDOM = 4,
	MP_SETTING_SPAWN_PRIVATE_YACHT = 5,
	MP_SETTING_SPAWN_OFFICE = 6,
	MP_SETTING_SPAWN_CLUBHOUSE = 7,
	MP_SETTING_SPAWN_IE_WAREHOUSE = 8,
	MP_SETTING_SPAWN_BUNKER = 9,
	MP_SETTING_SPAWN_HANGAR = 10,
	MP_SETTING_SPAWN_DEFUNCT_BASE = 11,
	MP_SETTING_SPAWN_NIGHTCLUB = 12,
	MP_SETTING_SPAWN_ARENA_GARAGE = 13,
	MP_SETTING_SPAWN_CASINO_APARTMENT = 14,
	MP_SETTING_SPAWN_ARCADE = 15,
	MP_SETTING_SPAWN_SUBMARINE = 16,
	MP_SETTING_SPAWN_CAR_MEET = 17,
	MP_SETTING_SPAWN_AUTO_SHOP = 18,
	MP_SETTING_SPAWN_FIXER_HQ = 19,
	MP_SETTING_SPAWN_MAX = 20,
};
```

```
NativeDB Introduced: v2699
```

---
### NetworkSetCurrentlySelectedGamerHandleFromInviteMenu

`NETWORK_SET_CURRENTLY_SELECTED_GAMER_HANDLE_FROM_INVITE_MENU` · hash `0x7206F674F2A3B1BB` · jhash `0xFD95899E` · **Cliente**

```lua
local retval, p0 = NetworkSetCurrentlySelectedGamerHandleFromInviteMenu(p0)
```
```c
BOOL NETWORK_SET_CURRENTLY_SELECTED_GAMER_HANDLE_FROM_INVITE_MENU(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### NetworkSetEntityCanBlend

`NETWORK_SET_ENTITY_CAN_BLEND` · hash `0xD830567D88A1E873` · jhash `0xDE8C0DB8` · **Cliente**

```lua
NetworkSetEntityCanBlend(entity, toggle)
```
```c
void NETWORK_SET_ENTITY_CAN_BLEND(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetEntityGhostedWithOwner

`_NETWORK_SET_ENTITY_GHOSTED_WITH_OWNER` · hash `0x4BA166079D658ED4` · **Cliente**

```lua
NetworkSetEntityGhostedWithOwner(entity, p1)
```
```c
void _NETWORK_SET_ENTITY_GHOSTED_WITH_OWNER(Entity entity, BOOL p1);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4BA166079D658ED4` (`N_0x4ba166079d658ed4`)

---
### NetworkSetEntityInvisibleToNetwork

`_NETWORK_SET_ENTITY_INVISIBLE_TO_NETWORK` · hash `0xF1CA12B18AEF5298` · jhash `0x09CBC4B0` · **Cliente**

```lua
NetworkSetEntityInvisibleToNetwork(entity, toggle)
```
```c
void _NETWORK_SET_ENTITY_INVISIBLE_TO_NETWORK(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
if set to true other network players can't see it  
if set to false other network player can see it  
=========================================  
^^ I attempted this by grabbing an object with GET_ENTITY_PLAYER_IS_FREE_AIMING_AT and setting this naive no matter the toggle he could still see it.  
pc or last gen?  
^^ last-gen  
```

**Nombres antiguos (alias):** `0xF1CA12B18AEF5298` (`N_0xf1ca12b18aef5298`), `_NETWORK_SET_ENTITY_VISIBLE_TO_NETWORK` (`NetworkSetEntityVisibleToNetwork`)

---
### NetworkSetFriendlyFireOption

`NETWORK_SET_FRIENDLY_FIRE_OPTION` · hash `0xF808475FA571D823` · jhash `0x6BAF95FA` · **Cliente**

```lua
NetworkSetFriendlyFireOption(toggle)
```
```c
void NETWORK_SET_FRIENDLY_FIRE_OPTION(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetGamerInvitedToTransition

`NETWORK_SET_GAMER_INVITED_TO_TRANSITION` · hash `0xCA2C8073411ECDB6` · jhash `0x17F1C69D` · **Cliente**

```lua
local networkHandle = NetworkSetGamerInvitedToTransition(networkHandle)
```
```c
void NETWORK_SET_GAMER_INVITED_TO_TRANSITION(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### NetworkSetInFreeCamMode

`NETWORK_SET_IN_FREE_CAM_MODE` · hash `0xFC18DB55AE19E046` · jhash `0xA7E36020` · **Cliente**

```lua
NetworkSetInFreeCamMode(toggle)
```
```c
void NETWORK_SET_IN_FREE_CAM_MODE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFC18DB55AE19E046` (`N_0xfc18db55ae19e046`)

---
### NetworkSetInMpCutscene

`NETWORK_SET_IN_MP_CUTSCENE` · hash `0x9CA5DE655269FEC4` · jhash `0x8434CB43` · **Cliente**

```lua
NetworkSetInMpCutscene(p0, p1)
```
```c
void NETWORK_SET_IN_MP_CUTSCENE(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetInSpectatorMode

`NETWORK_SET_IN_SPECTATOR_MODE` · hash `0x423DE3854BB50894` · jhash `0x5C4C8458` · **Cliente**

```lua
NetworkSetInSpectatorMode(toggle, playerPed)
```
```c
void NETWORK_SET_IN_SPECTATOR_MODE(BOOL toggle, Ped playerPed);
```

**Parámetros**

- `toggle` (`BOOL`)
- `playerPed` (`Ped`)

**Devuelve:** `void`

---
### NetworkSetInSpectatorModeExtended

`NETWORK_SET_IN_SPECTATOR_MODE_EXTENDED` · hash `0x419594E137637120` · jhash `0x54058F5F` · **Cliente**

```lua
NetworkSetInSpectatorModeExtended(toggle, playerPed, p2)
```
```c
void NETWORK_SET_IN_SPECTATOR_MODE_EXTENDED(BOOL toggle, Ped playerPed, BOOL p2);
```

**Parámetros**

- `toggle` (`BOOL`)
- `playerPed` (`Ped`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x419594E137637120` (`N_0x419594e137637120`)

---
### NetworkSetInviteOnCallForInviteMenu

`NETWORK_SET_INVITE_ON_CALL_FOR_INVITE_MENU` · hash `0x66F010A4B031A331` · jhash `0x11378777` · **Cliente**

```lua
local networkHandle = NetworkSetInviteOnCallForInviteMenu(networkHandle)
```
```c
void NETWORK_SET_INVITE_ON_CALL_FOR_INVITE_MENU(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x66F010A4B031A331` (`N_0x66f010a4b031a331`)

---
### NetworkSetLocalPlayerInvincibleTime

`NETWORK_SET_LOCAL_PLAYER_INVINCIBLE_TIME` · hash `0x2D95C7E2D7E07307` · jhash `0xFEA9B85C` · **Cliente**

```lua
NetworkSetLocalPlayerInvincibleTime(time)
```
```c
void NETWORK_SET_LOCAL_PLAYER_INVINCIBLE_TIME(int time);
```

**Parámetros**

- `time` (`int`)

**Devuelve:** `void`

---
### NetworkSetLocalPlayerSyncLookAt

`NETWORK_SET_LOCAL_PLAYER_SYNC_LOOK_AT` · hash `0x524FF0AEFF9C3973` · jhash `0xB72F086D` · **Cliente**

```lua
NetworkSetLocalPlayerSyncLookAt(toggle)
```
```c
void NETWORK_SET_LOCAL_PLAYER_SYNC_LOOK_AT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x524FF0AEFF9C3973` (`N_0x524ff0aeff9c3973`)

---
### NetworkSetMissionFinished

`NETWORK_SET_MISSION_FINISHED` · hash `0x3B3D11CD9FFCDFC9` · jhash `0x3083FAD7` · **Cliente**

```lua
NetworkSetMissionFinished()
```
```c
void NETWORK_SET_MISSION_FINISHED();
```

**Devuelve:** `void`

---
### NetworkSetNoSpectatorChat

`NETWORK_SET_NO_SPECTATOR_CHAT` · hash `0xF46A1E03E8755980` · jhash `0xD33AFF79` · **Cliente**

```lua
NetworkSetNoSpectatorChat(toggle)
```
```c
void NETWORK_SET_NO_SPECTATOR_CHAT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF46A1E03E8755980` (`N_0xf46a1e03e8755980`)

---
### NetworkSetObjectForceStaticBlend

`_NETWORK_SET_OBJECT_FORCE_STATIC_BLEND` · hash `0x0379DAF89BA09AA5` · **Cliente**

```lua
NetworkSetObjectForceStaticBlend(object, enabled)
```
```c
void _NETWORK_SET_OBJECT_FORCE_STATIC_BLEND(Object object, BOOL enabled);
```

**Parámetros**

- `object` (`Object`): The object to set forced blending state for.
- `enabled` (`BOOL`): `true` to enable forced blending.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether or not an object (created using `CREATE_OBJECT`, or similar) should have its position/rotation synchronized,
even if it is a 'static' object (for example, having flag 32 - Static - set in its archetype definition).

This has to be called during the same frame the object is created/registered for network, as otherwise it may already
have a remote clone created.

Once a remote clone is created, changing this value will not have any effect on said clone.

**Nombres antiguos (alias):** `0x0379DAF89BA09AA5` (`N_0x0379daf89ba09aa5`)

---
### NetworkSetOverrideSpectatorMode

`NETWORK_SET_OVERRIDE_SPECTATOR_MODE` · hash `0x70DA3BF8DACD3210` · jhash `0xA0FD42D3` · **Cliente**

```lua
NetworkSetOverrideSpectatorMode(toggle)
```
```c
void NETWORK_SET_OVERRIDE_SPECTATOR_MODE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetPlayerIsPassive

`NETWORK_SET_PLAYER_IS_PASSIVE` · hash `0x1B857666604B1A74` · jhash `0x76A9FEB6` · **Cliente**

```lua
NetworkSetPlayerIsPassive(toggle)
```
```c
void NETWORK_SET_PLAYER_IS_PASSIVE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1B857666604B1A74` (`N_0x1b857666604b1a74`)

---
### NetworkSetPropertyId

`NETWORK_SET_PROPERTY_ID` · hash `0x1775961C2FBBCB5C` · jhash `0x5A74E873` · **Cliente**

```lua
NetworkSetPropertyId(id)
```
```c
void NETWORK_SET_PROPERTY_ID(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
value must be < 255
```

---
### NetworkSetRichPresence

`NETWORK_SET_RICH_PRESENCE` · hash `0x1DCCACDCFC569362` · jhash `0x932A6CED` · **Cliente**

```lua
NetworkSetRichPresence(p0, p1, p2, p3)
```
```c
void NETWORK_SET_RICH_PRESENCE(int p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
On PC it's a nullsub which means it does absolutely nothing.  
Now that Discord supports Rich Presence, R* might finally implement this for PC. Or maybe in future games like RDR2, GTA VI...  
```

---
### NetworkSetRichPresenceString

`NETWORK_SET_RICH_PRESENCE_STRING` · hash `0x3E200C2BCF4164EB` · jhash `0x017E6777` · **Cliente**

```lua
NetworkSetRichPresenceString(p0, textLabel)
```
```c
void NETWORK_SET_RICH_PRESENCE_STRING(int p0, char* textLabel);
```

**Parámetros**

- `p0` (`int`)
- `textLabel` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

This native does absolutely nothing, just a nullsub

**Nombres antiguos (alias):** `0x3E200C2BCF4164EB` (`N_0x3e200c2bcf4164eb`), `_NETWORK_SET_RICH_PRESENCE_2` (`NetworkSetRichPresence_2`)

---
### NetworkSetScriptReadyForEvents

`NETWORK_SET_SCRIPT_READY_FOR_EVENTS` · hash `0x7AC752103856FB20` · jhash `0xA639DCA2` · **Cliente**

```lua
NetworkSetScriptReadyForEvents(toggle)
```
```c
void NETWORK_SET_SCRIPT_READY_FOR_EVENTS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7AC752103856FB20` (`N_0x7ac752103856fb20`)

---
### NetworkSetTalkerProximity

`NETWORK_SET_TALKER_PROXIMITY` · hash `0xCBF12D65F95AD686` · jhash `0x67555C66` · **Cliente**

```lua
NetworkSetTalkerProximity(value)
```
```c
void NETWORK_SET_TALKER_PROXIMITY(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

---
### NetworkSetTeamOnlyChat

`NETWORK_SET_TEAM_ONLY_CHAT` · hash `0xD5B4883AC32F24C3` · jhash `0x3813019A` · **Cliente**

```lua
NetworkSetTeamOnlyChat(toggle)
```
```c
void NETWORK_SET_TEAM_ONLY_CHAT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetThisScriptIsNetworkScript

`NETWORK_SET_THIS_SCRIPT_IS_NETWORK_SCRIPT` · hash `0x1CA59E306ECB80A5` · jhash `0x470810ED` · **Cliente**

```lua
NetworkSetThisScriptIsNetworkScript(maxNumMissionParticipants, p1, instanceId)
```
```c
void NETWORK_SET_THIS_SCRIPT_IS_NETWORK_SCRIPT(int maxNumMissionParticipants, BOOL p1, int instanceId);
```

**Parámetros**

- `maxNumMissionParticipants` (`int`)
- `p1` (`BOOL`)
- `instanceId` (`int`)

**Devuelve:** `void`

---
### NetworkSetTransitionActivityId

`NETWORK_SET_TRANSITION_ACTIVITY_ID` · hash `0x30DE938B516F0AD2` · jhash `0xCCA9C022` · **Cliente**

```lua
NetworkSetTransitionActivityId(p0)
```
```c
void NETWORK_SET_TRANSITION_ACTIVITY_ID(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x30DE938B516F0AD2` (`N_0x30de938b516f0ad2`)

---
### NetworkSetTransitionCreatorHandle

`NETWORK_SET_TRANSITION_CREATOR_HANDLE` · hash `0xEF26739BCD9907D5` · jhash `0x1DD01FE7` · **Cliente**

```lua
local p0 = NetworkSetTransitionCreatorHandle(p0)
```
```c
void NETWORK_SET_TRANSITION_CREATOR_HANDLE(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### NetworkSetTransitionVisibilityLock

`NETWORK_SET_TRANSITION_VISIBILITY_LOCK` · hash `0x0C978FDA19692C2C` · jhash `0x4AF0ADF5` · **Cliente**

```lua
NetworkSetTransitionVisibilityLock(p0, p1)
```
```c
void NETWORK_SET_TRANSITION_VISIBILITY_LOCK(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0C978FDA19692C2C` (`N_0x0c978fda19692c2c`)

---
### NetworkSetVehicleTestDrive

`_NETWORK_SET_VEHICLE_TEST_DRIVE` · hash `0x8C70252FC40F320B` · **Cliente**

```lua
NetworkSetVehicleTestDrive(toggle)
```
```c
void _NETWORK_SET_VEHICLE_TEST_DRIVE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used by Metric VEHICLE_DIST_DRIVEN
```

```
NativeDB Introduced: v2699
```

---
### NetworkSetVehicleWheelsDestructible

`_NETWORK_SET_VEHICLE_WHEELS_DESTRUCTIBLE` · hash `0x890E2C5ABED7236D` · **Cliente**

```lua
NetworkSetVehicleWheelsDestructible(vehicle, toggle)
```
```c
void _NETWORK_SET_VEHICLE_WHEELS_DESTRUCTIBLE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Allow vehicle wheels to be destructible even when the Vehicle entity is invincible.
```

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0x890E2C5ABED7236D` (`N_0x890e2c5abed7236d`)

---
### NetworkSetVoiceActive

`NETWORK_SET_VOICE_ACTIVE` · hash `0xBABEC9E69A91C57B` · jhash `0x8011247F` · **Cliente**

```lua
NetworkSetVoiceActive(toggle)
```
```c
void NETWORK_SET_VOICE_ACTIVE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSetVoiceChannel

`NETWORK_SET_VOICE_CHANNEL` · hash `0xEF6212C2EFEF1A23` · jhash `0x3974879F` · **Cliente**

```lua
NetworkSetVoiceChannel(channel)
```
```c
void NETWORK_SET_VOICE_CHANNEL(int channel);
```

**Parámetros**

- `channel` (`int`)

**Devuelve:** `void`

---
### NetworkShouldShowConnectivityTroubleshooting

`_NETWORK_SHOULD_SHOW_CONNECTIVITY_TROUBLESHOOTING` · hash `0x82A2B386716608F1` · **Cliente**

```lua
local retval = NetworkShouldShowConnectivityTroubleshooting()
```
```c
BOOL _NETWORK_SHOULD_SHOW_CONNECTIVITY_TROUBLESHOOTING();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the NAT type is Strict (3) and a certain number of connections have failed.
```

**Nombres antiguos (alias):** `0x82A2B386716608F1` (`N_0x82a2b386716608f1`)

---
### NetworkShowProfileUi

`NETWORK_SHOW_PROFILE_UI` · hash `0x859ED1CEA343FCA8` · jhash `0xF00A20B0` · **Cliente**

```lua
local networkHandle = NetworkShowProfileUi(networkHandle)
```
```c
void NETWORK_SHOW_PROFILE_UI(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Example:  
int playerHandle;	  
NETWORK_HANDLE_FROM_PLAYER(selectedPlayer, &playerHandle, 13);  
NETWORK_SHOW_PROFILE_UI(&playerHandle);  
```

---
### NetworkStartRespawnSearchForPlayer

`NETWORK_START_RESPAWN_SEARCH_FOR_PLAYER` · hash `0x5A6FFA2433E2F14C` · jhash `0xC62E77B3` · **Cliente**

```lua
local retval = NetworkStartRespawnSearchForPlayer(player, x, y, z, radius, p5, p6, p7, flags)
```
```c
BOOL NETWORK_START_RESPAWN_SEARCH_FOR_PLAYER(Player player, float x, float y, float z, float radius, float p5, float p6, float p7, int flags);
```

**Parámetros**

- `player` (`Player`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `flags` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
One of the first things it does is get the players ped.  
Then it calls a function that is used in some tasks and ped based functions.  
```

p5, p6, p7 is another coordinate (or zero), often related to `GET_BLIP_COORDS`, in the decompiled scripts.

**Nombres antiguos (alias):** `0x5A6FFA2433E2F14C` (`N_0x5a6ffa2433e2f14c`)

---
### NetworkStartRespawnSearchInAngledAreaForPlayer

`NETWORK_START_RESPAWN_SEARCH_IN_ANGLED_AREA_FOR_PLAYER` · hash `0x4BA92A18502BCA61` · jhash `0x74D6B13C` · **Cliente**

```lua
local retval = NetworkStartRespawnSearchInAngledAreaForPlayer(player, x1, y1, z1, x2, y2, z2, width, p8, p9, p10, flags)
```
```c
BOOL NETWORK_START_RESPAWN_SEARCH_IN_ANGLED_AREA_FOR_PLAYER(Player player, float x1, float y1, float z1, float x2, float y2, float z2, float width, float p8, float p9, float p10, int flags);
```

**Parámetros**

- `player` (`Player`)
- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `p8` (`float`)
- `p9` (`float`)
- `p10` (`float`)
- `flags` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

p8, p9, p10 is another coordinate, or zero, often related to `GET_BLIP_COORDS` in the decompiled scripts.

**Nombres antiguos (alias):** `0x4BA92A18502BCA61` (`N_0x4ba92a18502bca61`)

---
### NetworkStartSoloTutorialSession

`NETWORK_START_SOLO_TUTORIAL_SESSION` · hash `0x17E0198B3882C2CB` · jhash `0x408A9436` · **Cliente**

```lua
NetworkStartSoloTutorialSession()
```
```c
void NETWORK_START_SOLO_TUTORIAL_SESSION();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x17E0198B3882C2CB` (`N_0x17e0198b3882c2cb`)

---
### NetworkStartSynchronisedScene

`NETWORK_START_SYNCHRONISED_SCENE` · hash `0x9A1B3FCDB36C8697` · jhash `0xA9DFDC40` · **Cliente**

```lua
NetworkStartSynchronisedScene(netScene)
```
```c
void NETWORK_START_SYNCHRONISED_SCENE(int netScene);
```

**Parámetros**

- `netScene` (`int`)

**Devuelve:** `void`

---
### NetworkStartUserContentPermissionsCheck

`_NETWORK_START_USER_CONTENT_PERMISSIONS_CHECK` · hash `0xDEB2B99A1AF1A2A6` · **Cliente**

```lua
local retval = NetworkStartUserContentPermissionsCheck(netHandle)
```
```c
int _NETWORK_START_USER_CONTENT_PERMISSIONS_CHECK(Any netHandle);
```

**Parámetros**

- `netHandle` (`Any`)

**Devuelve:** `int`

**Descripción oficial:**

```
Always returns -1. Seems to be XB1 specific.
```

**Nombres antiguos (alias):** `0xDEB2B99A1AF1A2A6` (`N_0xdeb2b99a1af1a2a6`)

---
### NetworkStopSynchronisedScene

`NETWORK_STOP_SYNCHRONISED_SCENE` · hash `0xC254481A4574CB2F` · jhash `0x97B1CDF6` · **Cliente**

```lua
NetworkStopSynchronisedScene(netScene)
```
```c
void NETWORK_STOP_SYNCHRONISED_SCENE(int netScene);
```

**Parámetros**

- `netScene` (`int`)

**Devuelve:** `void`

---
### NetworkSuppressInvite

`NETWORK_SUPPRESS_INVITE` · hash `0xA0682D67EF1FBA3D` · jhash `0x323DC78C` · **Cliente**

```lua
NetworkSuppressInvite(toggle)
```
```c
void NETWORK_SUPPRESS_INVITE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### NetworkTransitionTrack

`_NETWORK_TRANSITION_TRACK` · hash `0xC3BFED92026A2AAD` · **Cliente**

```lua
NetworkTransitionTrack(hash, p1, p2, state, p4)
```
```c
void _NETWORK_TRANSITION_TRACK(Hash hash, int p1, int p2, int state, int p4);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)
- `p2` (`int`)
- `state` (`int`)
- `p4` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC3BFED92026A2AAD` (`N_0xc3bfed92026a2aad`)

---
### NetworkTryAccessTunableBoolHash

`NETWORK_TRY_ACCESS_TUNABLE_BOOL_HASH` · hash `0xC7420099936CE286` · jhash `0x8AFE3D90` · **Cliente**

```lua
local retval = NetworkTryAccessTunableBoolHash(tunableContext, tunableName, defaultValue)
```
```c
BOOL NETWORK_TRY_ACCESS_TUNABLE_BOOL_HASH(Hash tunableContext, Hash tunableName, BOOL defaultValue);
```

**Parámetros**

- `tunableContext` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `tunableName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `defaultValue` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns defaultValue if the tunable doesn't exist.
```

**Nombres antiguos (alias):** `0xC7420099936CE286` (`N_0xc7420099936ce286`), `_NETWORK_ACCESS_TUNABLE_BOOL_HASH_FAIL_VAL` (`NetworkAccessTunableBoolHashFailVal`)

---
### NetworkUgcNav

`_NETWORK_UGC_NAV` · hash `0xC1447451DDB512F0` · **Cliente**

```lua
NetworkUgcNav(p0, p1)
```
```c
void _NETWORK_UGC_NAV(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xC1447451DDB512F0` (`N_0xc1447451ddb512f0`)

---
### NetworkUnregisterNetworkedEntity

`NETWORK_UNREGISTER_NETWORKED_ENTITY` · hash `0x7368E683BB9038D6` · jhash `0x5C645F64` · **Cliente**

```lua
NetworkUnregisterNetworkedEntity(entity)
```
```c
void NETWORK_UNREGISTER_NETWORKED_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7368E683BB9038D6` (`N_0x7368e683bb9038d6`)

---
### NetworkUpdatePlayerScars

`_NETWORK_UPDATE_PLAYER_SCARS` · hash `0xB7C7F6AD6424304B` · jhash `0x371BBA08` · **Cliente**

```lua
NetworkUpdatePlayerScars()
```
```c
void _NETWORK_UPDATE_PLAYER_SCARS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB7C7F6AD6424304B` (`N_0xb7c7f6ad6424304b`)

---
### NetworkUseHighPrecisionBlending

`NETWORK_USE_HIGH_PRECISION_BLENDING` · hash `0x2B1813ABA29016C5` · jhash `0x155465EE` · **Cliente**

```lua
NetworkUseHighPrecisionBlending(netID, toggle)
```
```c
void NETWORK_USE_HIGH_PRECISION_BLENDING(int netID, BOOL toggle);
```

**Parámetros**

- `netID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Old name: _NETWORK_SET_NETWORK_ID_DYNAMIC
```

**Nombres antiguos (alias):** `0x2B1813ABA29016C5` (`N_0x2b1813aba29016c5`), `_NETWORK_SET_NETWORK_ID_DYNAMIC` (`NetworkSetNetworkIdDynamic`)

---
### NetworkUseLogarithmicBlendingThisFrame

`NETWORK_USE_LOGARITHMIC_BLENDING_THIS_FRAME` · hash `0xCD71A4ECAB22709E` · jhash `0xBC54371B` · **Cliente**

```lua
NetworkUseLogarithmicBlendingThisFrame(entity)
```
```c
void NETWORK_USE_LOGARITHMIC_BLENDING_THIS_FRAME(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCD71A4ECAB22709E` (`N_0xcd71a4ecab22709e`)

---
### ObjToNet

`OBJ_TO_NET` · hash `0x99BFDC94A603E541` · jhash `0x1E05F29F` · **Cliente**

```lua
local retval = ObjToNet(object)
```
```c
int OBJ_TO_NET(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `int`

**Descripción oficial:**

```
Lets objects spawn online simply do it like this:  
int createdObject = OBJ_TO_NET(CREATE_OBJECT_NO_OFFSET(oball, pCoords.x, pCoords.y, pCoords.z, 1, 0, 0));  
```

---
### OpenCommerceStore

`OPEN_COMMERCE_STORE` · hash `0x58C21165F6545892` · jhash `0x365C50EE` · **Cliente**

```lua
OpenCommerceStore(p0, p1)
```
```c
void OPEN_COMMERCE_STORE(char* p0, char* p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Has a 3rd param (int) since patch [???].  
```

```
NativeDB Added Parameter 3: int p2
```

**Nombres antiguos (alias):** `0x58C21165F6545892` (`N_0x58c21165f6545892`)

---
### ParticipantId

`PARTICIPANT_ID` · hash `0x90986E8876CE0A83` · jhash `0x9C35A221` · **Cliente**

```lua
local retval = ParticipantId()
```
```c
Player PARTICIPANT_ID();
```

**Devuelve:** `Player`

**Descripción oficial:**

```
Return the local Participant ID  
```

---
### ParticipantIdToInt

`PARTICIPANT_ID_TO_INT` · hash `0x57A3BDDAD8E5AA0A` · jhash `0x907498B0` · **Cliente**

```lua
local retval = ParticipantIdToInt()
```
```c
int PARTICIPANT_ID_TO_INT();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Return the local Participant ID.  
This native is exactly the same as 'PARTICIPANT_ID' native.  
```

---
### PedToNet

`PED_TO_NET` · hash `0x0EDEC3C276198689` · jhash `0x86A0B759` · **Cliente**

```lua
local retval = PedToNet(ped)
```
```c
int PED_TO_NET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
gets the network id of a ped  
```

---
### RefreshPlayerListStats

`REFRESH_PLAYER_LIST_STATS` · hash `0xE26CCFF8094D8C74` · jhash `0xF49C1533` · **Cliente**

```lua
local retval = RefreshPlayerListStats(p0)
```
```c
BOOL REFRESH_PLAYER_LIST_STATS(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `USING_NETWORK_WEAPONTYPE` (`UsingNetworkWeapontype`), `0xE26CCFF8094D8C74` (`N_0xe26ccff8094d8c74`)

---
### ReleaseAllCommerceItemImages

`RELEASE_ALL_COMMERCE_ITEM_IMAGES` · hash `0x72D0706CD6CCDB58` · jhash `0xCA7A0A49` · **Cliente**

```lua
ReleaseAllCommerceItemImages()
```
```c
void RELEASE_ALL_COMMERCE_ITEM_IMAGES();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x72D0706CD6CCDB58` (`N_0x72d0706cd6ccdb58`)

---
### RemoteCheatDetected

`_REMOTE_CHEAT_DETECTED` · hash `0x472841A026D26D8B` · **Cliente**

```lua
local retval = RemoteCheatDetected()
```
```c
BOOL _REMOTE_CHEAT_DETECTED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: Player player
NativeDB Added Parameter 2: int a
NativeDB Added Parameter 3: int b
```

**Nombres antiguos (alias):** `0x472841A026D26D8B` (`N_0x472841a026d26d8b`)

---
### RemoveAllStickyBombsFromEntity

`REMOVE_ALL_STICKY_BOMBS_FROM_ENTITY` · hash `0x715135F4B82AC90D` · jhash `0xCEAE5AFC` · **Cliente**

```lua
RemoveAllStickyBombsFromEntity(entity)
```
```c
void REMOVE_ALL_STICKY_BOMBS_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used in am_mp_property_ext and am_mp_property_int  
```

```
NativeDB Added Parameter 2: Ped ped
```

**Nombres antiguos (alias):** `0x715135F4B82AC90D` (`N_0x715135f4b82ac90d`)

---
### RequestCommerceItemImage

`REQUEST_COMMERCE_ITEM_IMAGE` · hash `0xA2F952104FC6DD4B` · jhash `0x1FDC75DC` · **Cliente**

```lua
local retval = RequestCommerceItemImage(index)
```
```c
BOOL REQUEST_COMMERCE_ITEM_IMAGE(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA2F952104FC6DD4B` (`N_0xa2f952104fc6dd4b`)

---
### ReserveNetworkLocalObjects

`_RESERVE_NETWORK_LOCAL_OBJECTS` · hash `0x797F9C5E661D920E` · **Cliente**

```lua
ReserveNetworkLocalObjects(amount)
```
```c
void _RESERVE_NETWORK_LOCAL_OBJECTS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Internal logging string: SCRIPT_RESERVING_LOCAL_OBJECTS
```

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x797F9C5E661D920E` (`N_0x797f9c5e661d920e`)

---
### ReserveNetworkLocalPeds

`_RESERVE_NETWORK_LOCAL_PEDS` · hash `0x2C8DF5D129595281` · **Cliente**

```lua
ReserveNetworkLocalPeds(amount)
```
```c
void _RESERVE_NETWORK_LOCAL_PEDS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Internal logging string: SCRIPT_RESERVING_LOCAL_PEDS
```

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x2C8DF5D129595281` (`N_0x2c8df5d129595281`)

---
### ReserveNetworkLocalVehicles

`_RESERVE_NETWORK_LOCAL_VEHICLES` · hash `0x42613035157E4208` · **Cliente**

```lua
ReserveNetworkLocalVehicles(amount)
```
```c
void _RESERVE_NETWORK_LOCAL_VEHICLES(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x42613035157E4208` (`N_0x42613035157e4208`)

---
### ReserveNetworkMissionObjects

`RESERVE_NETWORK_MISSION_OBJECTS` · hash `0x4E5C93BD0C32FBF8` · jhash `0x391DF4F3` · **Cliente**

```lua
ReserveNetworkMissionObjects(amount)
```
```c
void RESERVE_NETWORK_MISSION_OBJECTS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

---
### ReserveNetworkMissionPeds

`RESERVE_NETWORK_MISSION_PEDS` · hash `0xB60FEBA45333D36F` · jhash `0x54998C37` · **Cliente**

```lua
ReserveNetworkMissionPeds(amount)
```
```c
void RESERVE_NETWORK_MISSION_PEDS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

---
### ReserveNetworkMissionVehicles

`RESERVE_NETWORK_MISSION_VEHICLES` · hash `0x76B02E21ED27A469` · jhash `0x5062875E` · **Cliente**

```lua
ReserveNetworkMissionVehicles(amount)
```
```c
void RESERVE_NETWORK_MISSION_VEHICLES(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

---
### ResetGhostedEntityAlpha

`_RESET_GHOSTED_ENTITY_ALPHA` · hash `0x17330EBF2F2124A8` · **Cliente**

```lua
ResetGhostedEntityAlpha()
```
```c
void _RESET_GHOSTED_ENTITY_ALPHA();
```

**Devuelve:** `void`

**Descripción oficial:**

Sets the alpha value used by [`_SET_LOCAL_PLAYER_AS_GHOST`](#setlocalplayerasghost), [`SET_NETWORK_VEHICLE_AS_GHOST`](#setnetworkvehicleasghost), and [`_NETWORK_SET_ENTITY_GHOSTED_WITH_OWNER`](#networksetentityghostedwithowner).

**Nombres antiguos (alias):** `0x17330EBF2F2124A8` (`N_0x17330ebf2f2124a8`)

---
### SetBalanceAddMachine

`SET_BALANCE_ADD_MACHINE` · hash `0x815E5E3073DA1D67` · jhash `0xE123C7AC` · **Cliente**

```lua
local retval = SetBalanceAddMachine(contentId, contentTypeName)
```
```c
BOOL SET_BALANCE_ADD_MACHINE(char* contentId, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

---
### SetBalanceAddMachines

`SET_BALANCE_ADD_MACHINES` · hash `0xB8322EEB38BE7C26` · jhash `0x22C33603` · **Cliente**

```lua
local retval, data = SetBalanceAddMachines(dataCount, contentTypeName)
```
```c
BOOL SET_BALANCE_ADD_MACHINES(Any* data, int dataCount, char* contentTypeName);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `dataCount` (`int`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

---
### SetEntityLocallyInvisible

`SET_ENTITY_LOCALLY_INVISIBLE` · hash `0xE135A9FF3F5D05D8` · jhash `0x51ADCC5F` · **Cliente**

```lua
SetEntityLocallyInvisible(entity)
```
```c
void SET_ENTITY_LOCALLY_INVISIBLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the provided entity not visible for yourself for the current frame.

**Ejemplo (lua):**

```lua
CreateThread(function()
  -- Any random entity should work
  local entity = PlayerPedId()
  -- Make the entity visible for all players
  SetEntityVisible(entity, true)
  while true do
    Wait(0)
    -- Make the entity invisible for the current player only.
    SetEntityLocallyInvisible(entity)
  end
end)
```

---
### SetEntityLocallyVisible

`SET_ENTITY_LOCALLY_VISIBLE` · hash `0x241E289B5C059EDC` · jhash `0x235A57B3` · **Cliente**

```lua
SetEntityLocallyVisible(entity)
```
```c
void SET_ENTITY_LOCALLY_VISIBLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to set locally visible.

**Devuelve:** `void`

**Descripción oficial:**

Sets the provided entity visible for yourself for the current frame.

**Ejemplo (lua):**

```lua
CreateThread(function()
  -- Any random entity should work
  local entity = GetVehiclePedIsIn(PlayerPedId(), false)
  -- Sets the entity not visible to other players
  SetEntityVisible(entity, false)
  while true do
    Wait(0)
    -- Sets the entity as visible for yourself
    SetEntityLocallyVisible(entity)
  end
end)
```

---
### SetEntityVisibleInCutscene

`SET_ENTITY_VISIBLE_IN_CUTSCENE` · hash `0xE0031D3C8F36AB82` · jhash `0xDBFB067B` · **Cliente**

```lua
SetEntityVisibleInCutscene(p0, p1, p2)
```
```c
void SET_ENTITY_VISIBLE_IN_CUTSCENE(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### SetGhostedEntityAlpha

`_SET_GHOSTED_ENTITY_ALPHA` · hash `0x658500AE6D723A7E` · **Cliente**

```lua
SetGhostedEntityAlpha(alpha)
```
```c
void _SET_GHOSTED_ENTITY_ALPHA(int alpha);
```

**Parámetros**

- `alpha` (`int`): A value between 1 and 254. Default: 128

**Devuelve:** `void`

**Descripción oficial:**

Sets the alpha value used by [`_SET_LOCAL_PLAYER_AS_GHOST`](#setlocalplayerasghost), [`SET_NETWORK_VEHICLE_AS_GHOST`](#setnetworkvehicleasghost), and [`_NETWORK_SET_ENTITY_GHOSTED_WITH_OWNER`](#networksetentityghostedwithowner).

'Solidness' cannot be achieved using 255 - this will have the opposite effect of it defaulting to 128 it seems (or just having no effect at all).

**Nombres antiguos (alias):** `0x658500AE6D723A7E` (`N_0x658500ae6d723a7e`)

---
### SetLocalPlayerAsGhost

`_SET_LOCAL_PLAYER_AS_GHOST` · hash `0x5FFE9B4144F9712F` · **Cliente**

```lua
SetLocalPlayerAsGhost(toggle)
```
```c
void _SET_LOCAL_PLAYER_AS_GHOST(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Formerly incorrectly named `USE_PLAYER_COLOUR_INSTEAD_OF_TEAM_COLOUR` due to incorrect treatment of console vs. PC native registration.

Native name guessed through ordering.

```
NativeDB Added Parameter 2: BOOL p1
```

---
### SetLocalPlayerInvisibleLocally

`SET_LOCAL_PLAYER_INVISIBLE_LOCALLY` · hash `0xE5F773C1A1D9D168` · jhash `0x764F6222` · **Cliente**

```lua
SetLocalPlayerInvisibleLocally(p0)
```
```c
void SET_LOCAL_PLAYER_INVISIBLE_LOCALLY(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### SetLocalPlayerVisibleInCutscene

`SET_LOCAL_PLAYER_VISIBLE_IN_CUTSCENE` · hash `0xD1065D68947E7B6E` · jhash `0x59F3479B` · **Cliente**

```lua
SetLocalPlayerVisibleInCutscene(p0, p1)
```
```c
void SET_LOCAL_PLAYER_VISIBLE_IN_CUTSCENE(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### SetLocalPlayerVisibleLocally

`SET_LOCAL_PLAYER_VISIBLE_LOCALLY` · hash `0x7619364C82D3BF14` · jhash `0x324B56DB` · **Cliente**

```lua
SetLocalPlayerVisibleLocally(p0)
```
```c
void SET_LOCAL_PLAYER_VISIBLE_LOCALLY(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### SetNetworkCutsceneEntities

`SET_NETWORK_CUTSCENE_ENTITIES` · hash `0xAAA553E7DD28A457` · jhash `0xFD0F7EDD` · **Cliente**

```lua
SetNetworkCutsceneEntities(toggle)
```
```c
void SET_NETWORK_CUTSCENE_ENTITIES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAAA553E7DD28A457` (`N_0xaaa553e7dd28a457`)

---
### SetNetworkEnableVehiclePositionCorrection

`_SET_NETWORK_ENABLE_VEHICLE_POSITION_CORRECTION` · hash `0x838DA0936A24ED4D` · **Cliente**

```lua
SetNetworkEnableVehiclePositionCorrection(vehicle, toggle)
```
```c
void _SET_NETWORK_ENABLE_VEHICLE_POSITION_CORRECTION(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enables a periodic ShapeTest within the NetBlender and invokes rage::netBlenderLinInterp::GoStraightToTarget (or some functional wrapper).
```

**Nombres antiguos (alias):** `0x838DA0936A24ED4D` (`N_0x838da0936a24ed4d`)

---
### SetNetworkIdAlwaysExistsForPlayer

`SET_NETWORK_ID_ALWAYS_EXISTS_FOR_PLAYER` · hash `0xA8A024587329F36A` · jhash `0x4D15FDB1` · **Cliente**

```lua
SetNetworkIdAlwaysExistsForPlayer(netId, player, toggle)
```
```c
void SET_NETWORK_ID_ALWAYS_EXISTS_FOR_PLAYER(int netId, Player player, BOOL toggle);
```

**Parámetros**

- `netId` (`int`)
- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA8A024587329F36A` (`N_0xa8a024587329f36a`), `_SET_NETWORK_ID_SYNC_TO_PLAYER` (`SetNetworkIdSyncToPlayer`)

---
### SetNetworkIdCanMigrate

`SET_NETWORK_ID_CAN_MIGRATE` · hash `0x299EEB23175895FC` · jhash `0x47C8E5FF` · **Cliente**

```lua
SetNetworkIdCanMigrate(netId, toggle)
```
```c
void SET_NETWORK_ID_CAN_MIGRATE(int netId, BOOL toggle);
```

**Parámetros**

- `netId` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Whether or not another player is allowed to take control of the entity  
```

---
### SetNetworkIdExistsOnAllMachines

`SET_NETWORK_ID_EXISTS_ON_ALL_MACHINES` · hash `0xE05E81A888FA63C8` · jhash `0x68D486B2` · **Cliente**

```lua
SetNetworkIdExistsOnAllMachines(netId, toggle)
```
```c
void SET_NETWORK_ID_EXISTS_ON_ALL_MACHINES(int netId, BOOL toggle);
```

**Parámetros**

- `netId` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetNetworkIdVisibleInCutscene

`SET_NETWORK_ID_VISIBLE_IN_CUTSCENE` · hash `0xA6928482543022B4` · jhash `0x199E75EF` · **Cliente**

```lua
SetNetworkIdVisibleInCutscene(netId, p1, p2)
```
```c
void SET_NETWORK_ID_VISIBLE_IN_CUTSCENE(int netId, BOOL p1, BOOL p2);
```

**Parámetros**

- `netId` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### SetNetworkVehicleAsGhost

`SET_NETWORK_VEHICLE_AS_GHOST` · hash `0x6274C4712850841E` · jhash `0xEA235081` · **Cliente**

```lua
SetNetworkVehicleAsGhost(vehicle, toggle)
```
```c
void SET_NETWORK_VEHICLE_AS_GHOST(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6274C4712850841E` (`N_0x6274c4712850841e`), `_SET_NETWORK_OBJECT_NON_CONTACT` (`SetNetworkObjectNonContact`)

---
