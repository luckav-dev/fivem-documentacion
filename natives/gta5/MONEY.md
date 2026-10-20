# Natives de GTA V — MONEY

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `MONEY`: **301** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`CanPayGoon`](#canpaygoon) · [`DepositVc`](#depositvc) · [`N_0x08e8eeadfd0dc4a0`](#n_0x08e8eeadfd0dc4a0) · [`N_0x0d30eb83668e63c5`](#n_0x0d30eb83668e63c5) · [`N_0x0dd362f14f18942a`](#n_0x0dd362f14f18942a) · [`N_0x112209ce0290c03a`](#n_0x112209ce0290c03a) · [`N_0x1dc9b749e7ae282b`](#n_0x1dc9b749e7ae282b) · [`N_0x226c284c830d0ca8`](#n_0x226c284c830d0ca8) · [`N_0x2a7cec72c3443bcc`](#n_0x2a7cec72c3443bcc) · [`N_0x2a93c46aab1eacc9`](#n_0x2a93c46aab1eacc9) · [`N_0x2afc2d19b50797f2`](#n_0x2afc2d19b50797f2) · [`N_0x2fab6614ce22e196`](#n_0x2fab6614ce22e196) · [`N_0x31ba138f6304fb9f`](#n_0x31ba138f6304fb9f) · [`N_0x4128464231e3ca0b`](#n_0x4128464231e3ca0b) · [`N_0x4c3b75694f7e0d9c`](#n_0x4c3b75694f7e0d9c) · [`N_0x5574637681911fda`](#n_0x5574637681911fda) · [`N_0x55a1e095db052fa5`](#n_0x55a1e095db052fa5) · [`N_0x5f456788b05faeac`](#n_0x5f456788b05faeac) · [`N_0x65482bfd0923c8a1`](#n_0x65482bfd0923c8a1) · [`N_0x675d19c6067cae08`](#n_0x675d19c6067cae08) · [`N_0x69ef772b192614c1`](#n_0x69ef772b192614c1) · [`N_0x6b7e4fb50d5f3d65`](#n_0x6b7e4fb50d5f3d65) · [`N_0x6fcf8ddea146c45b`](#n_0x6fcf8ddea146c45b) · [`N_0x6fd97159fe3c971a`](#n_0x6fd97159fe3c971a) · [`N_0x7c4fccd2e4deb394`](#n_0x7c4fccd2e4deb394) · [`N_0x870289a558348378`](#n_0x870289a558348378) · [`N_0x8e243837643d9583`](#n_0x8e243837643d9583) · [`N_0x90cd7c6871fbf1b4`](#n_0x90cd7c6871fbf1b4) · [`N_0x998e18ceb44487fc`](#n_0x998e18ceb44487fc) · [`N_0x9b5016a6433a68c5`](#n_0x9b5016a6433a68c5) · [`N_0xa51338e0dccd4065`](#n_0xa51338e0dccd4065) · [`N_0xa51b086b0b2c0f7a`](#n_0xa51b086b0b2c0f7a) · [`N_0xa95cfb4e02390842`](#n_0xa95cfb4e02390842) · [`N_0xa95f667a755725da`](#n_0xa95f667a755725da) · [`N_0xb4c2ec463672474e`](#n_0xb4c2ec463672474e) · [`N_0xb4deae67f35e2acd`](#n_0xb4deae67f35e2acd) · [`N_0xb5b58e24868cb09e`](#n_0xb5b58e24868cb09e) · [`N_0xbd0efb25cca8f97a`](#n_0xbd0efb25cca8f97a) · [`N_0xc6e74cf8c884c880`](#n_0xc6e74cf8c884c880) · [`N_0xcd0f5b5d932ae473`](#n_0xcd0f5b5d932ae473) · [`N_0xcd4d66b43b1dd28d`](#n_0xcd4d66b43b1dd28d) · [`N_0xd29334ed1a256dbf`](#n_0xd29334ed1a256dbf) · [`N_0xde68e30d89f97132`](#n_0xde68e30d89f97132) · [`N_0xe0f82d68c7039158`](#n_0xe0f82d68c7039158) · [`N_0xe154b48b68ef72bc`](#n_0xe154b48b68ef72bc) · [`N_0xe23adc6fcb1f29ae`](#n_0xe23adc6fcb1f29ae) · [`N_0xe2bb399d90942091`](#n_0xe2bb399d90942091) · [`N_0xe2e244ab823b4483`](#n_0xe2e244ab823b4483) · [`N_0xed5fd7af10f5e262`](#n_0xed5fd7af10f5e262) · [`N_0xed76d195e6e3bf7f`](#n_0xed76d195e6e3bf7f) · [`N_0xfa07759e6fddd7cf`](#n_0xfa07759e6fddd7cf) · [`NetworkBuyAirstrike`](#networkbuyairstrike) · [`NetworkBuyBackupGang`](#networkbuybackupgang) · [`NetworkBuyBounty`](#networkbuybounty) · [`NetworkBuyContraband`](#networkbuycontraband) · [`NetworkBuyFairgroundRide`](#networkbuyfairgroundride) · [`NetworkBuyHealthcare`](#networkbuyhealthcare) · [`NetworkBuyHeliStrike`](#networkbuyhelistrike) · [`NetworkBuyItem`](#networkbuyitem) · [`NetworkBuyLotteryTicket`](#networkbuylotteryticket) · [`NetworkBuyProperty`](#networkbuyproperty) · [`NetworkBuySmokes`](#networkbuysmokes) · [`NetworkCanBet`](#networkcanbet) · [`NetworkCanBuyLotteryTicket`](#networkcanbuylotteryticket) · [`NetworkCanReceivePlayerCash`](#networkcanreceiveplayercash) · [`NetworkCanShareJobCash`](#networkcansharejobcash) · [`NetworkCanSpendMoney`](#networkcanspendmoney) · [`NetworkCanSpendMoney_2`](#networkcanspendmoney_2) · [`NetworkCasinoCanGamble`](#networkcasinocangamble) · [`NetworkCasinoCanPurchaseChipsWithPvc`](#networkcasinocanpurchasechipswithpvc) · [`NetworkCasinoCanPurchaseChipsWithPvc_2`](#networkcasinocanpurchasechipswithpvc_2) · [`NetworkCasinoCanUseGamblingType`](#networkcasinocanusegamblingtype) · [`NetworkCasinoPurchaseChips`](#networkcasinopurchasechips) · [`NetworkCasinoSellChips`](#networkcasinosellchips) · [`NetworkClearCharacterWallet`](#networkclearcharacterwallet) · [`NetworkDeductCash`](#networkdeductcash) · [`NetworkDeleteCharacter`](#networkdeletecharacter) · [`NetworkEarnBoss`](#networkearnboss) · [`NetworkEarnBossAgency`](#networkearnbossagency) · [`NetworkEarnBountyHunterReward`](#networkearnbountyhunterreward) · [`NetworkEarnCasinoHeist`](#networkearncasinoheist) · [`NetworkEarnCasinoHeistBonus`](#networkearncasinoheistbonus) · [`NetworkEarnCollectableCompletedCollection`](#networkearncollectablecompletedcollection) · [`NetworkEarnFmbbWageBonus`](#networkearnfmbbwagebonus) · [`NetworkEarnFromAiTargetKill`](#networkearnfromaitargetkill) · [`NetworkEarnFromAmbientJob`](#networkearnfromambientjob) · [`NetworkEarnFromArenaCareerProgression`](#networkearnfromarenacareerprogression) · [`NetworkEarnFromArenaSkillLevelProgression`](#networkearnfromarenaskilllevelprogression) · [`NetworkEarnFromArenaWar`](#networkearnfromarenawar) · [`NetworkEarnFromArmourTruck`](#networkearnfromarmourtruck) · [`NetworkEarnFromAssassinateTargetKilled`](#networkearnfromassassinatetargetkilled) · [`NetworkEarnFromAssassinateTargetKilled_2`](#networkearnfromassassinatetargetkilled_2) · [`NetworkEarnFromAutoshopBusiness`](#networkearnfromautoshopbusiness) · [`NetworkEarnFromAutoshopIncome`](#networkearnfromautoshopincome) · [`NetworkEarnFromBbEventBonus`](#networkearnfrombbeventbonus) · [`NetworkEarnFromBbEventCargo`](#networkearnfrombbeventcargo) · [`NetworkEarnFromBendJob`](#networkearnfrombendjob) · [`NetworkEarnFromBetting`](#networkearnfrombetting) · [`NetworkEarnFromBikeShopBusiness`](#networkearnfrombikeshopbusiness) · [`NetworkEarnFromBikerIncome`](#networkearnfrombikerincome) · [`NetworkEarnFromBounty`](#networkearnfrombounty) · [`NetworkEarnFromBusinessBattle`](#networkearnfrombusinessbattle) · [`NetworkEarnFromBusinessHubSell`](#networkearnfrombusinesshubsell) · [`NetworkEarnFromBusinessHubSource`](#networkearnfrombusinesshubsource) · [`NetworkEarnFromBusinessProduct`](#networkearnfrombusinessproduct) · [`NetworkEarnFromCarclubMembership`](#networkearnfromcarclubmembership) · [`NetworkEarnFromCashingOut`](#networkearnfromcashingout) · [`NetworkEarnFromCasinoAward`](#networkearnfromcasinoaward) · [`NetworkEarnFromCasinoMissionParticipation`](#networkearnfromcasinomissionparticipation) · [`NetworkEarnFromCasinoMissionReward`](#networkearnfromcasinomissionreward) · [`NetworkEarnFromCasinoStoryMissionReward`](#networkearnfromcasinostorymissionreward) · [`NetworkEarnFromChallengeWin`](#networkearnfromchallengewin) · [`NetworkEarnFromClubManagementParticipation`](#networkearnfromclubmanagementparticipation) · [`NetworkEarnFromCollectablesActionFigures`](#networkearnfromcollectablesactionfigures) · [`NetworkEarnFromCollectionItem`](#networkearnfromcollectionitem) · [`NetworkEarnFromCompleteCollection`](#networkearnfromcompletecollection) · [`NetworkEarnFromContraband`](#networkearnfromcontraband) · [`NetworkEarnFromCrateDrop`](#networkearnfromcratedrop) · [`NetworkEarnFromCriminalMastermindBonus`](#networkearnfromcriminalmastermindbonus) · [`NetworkEarnFromDailyObjectiveEvent`](#networkearnfromdailyobjectiveevent) · [`NetworkEarnFromDailyObjectives`](#networkearnfromdailyobjectives) · [`NetworkEarnFromDarChallenge`](#networkearnfromdarchallenge) · [`NetworkEarnFromDestroyingContraband`](#networkearnfromdestroyingcontraband) · [`NetworkEarnFromDoomsdayFinaleBonus`](#networkearnfromdoomsdayfinalebonus) · [`NetworkEarnFromFmbbBossWork`](#networkearnfromfmbbbosswork) · [`NetworkEarnFromFmbbPhonecallMission`](#networkearnfromfmbbphonecallmission) · [`NetworkEarnFromGangPickup`](#networkearnfromgangpickup) · [`NetworkEarnFromGangopsAwards`](#networkearnfromgangopsawards) · [`NetworkEarnFromGangopsElite`](#networkearnfromgangopselite) · [`NetworkEarnFromGangopsJobsFinale`](#networkearnfromgangopsjobsfinale) · [`NetworkEarnFromGangopsJobsPrepParticipation`](#networkearnfromgangopsjobsprepparticipation) · [`NetworkEarnFromGangopsJobsSetup`](#networkearnfromgangopsjobssetup) · [`NetworkEarnFromGangopsWages`](#networkearnfromgangopswages) · [`NetworkEarnFromGangopsWagesBonus`](#networkearnfromgangopswagesbonus) · [`NetworkEarnFromHackerTruckMission`](#networkearnfromhackertruckmission) · [`NetworkEarnFromHoldups`](#networkearnfromholdups) · [`NetworkEarnFromImportExport`](#networkearnfromimportexport) · [`NetworkEarnFromJob`](#networkearnfromjob) · [`NetworkEarnFromJobBonus`](#networkearnfromjobbonus) · [`NetworkEarnFromJobX2`](#networkearnfromjobx2) · [`NetworkEarnFromNotBadsport`](#networkearnfromnotbadsport) · [`NetworkEarnFromPersonalVehicle`](#networkearnfrompersonalvehicle) · [`NetworkEarnFromPickup`](#networkearnfrompickup) · [`NetworkEarnFromPremiumJob`](#networkearnfrompremiumjob) · [`NetworkEarnFromProperty`](#networkearnfromproperty) · [`NetworkEarnFromRcTimeTrial`](#networkearnfromrctimetrial) · [`NetworkEarnFromRdrBonus`](#networkearnfromrdrbonus) · [`NetworkEarnFromRockstar`](#networkearnfromrockstar) · [`NetworkEarnFromSellBase`](#networkearnfromsellbase) · [`NetworkEarnFromSellBunker`](#networkearnfromsellbunker) · [`NetworkEarnFromSellingVehicle`](#networkearnfromsellingvehicle) · [`NetworkEarnFromSightseeing`](#networkearnfromsightseeing) · [`NetworkEarnFromSmuggling`](#networkearnfromsmuggling) · [`NetworkEarnFromSpinTheWheelCash`](#networkearnfromspinthewheelcash) · [`NetworkEarnFromTargetRefund`](#networkearnfromtargetrefund) · [`NetworkEarnFromTimeTrialWin`](#networkearnfromtimetrialwin) · [`NetworkEarnFromTunerAward`](#networkearnfromtuneraward) · [`NetworkEarnFromTunerFinale`](#networkearnfromtunerfinale) · [`NetworkEarnFromUpgradeAutoshopLocation`](#networkearnfromupgradeautoshoplocation) · [`NetworkEarnFromVehicle`](#networkearnfromvehicle) · [`NetworkEarnFromVehicleAutoshop`](#networkearnfromvehicleautoshop) · [`NetworkEarnFromVehicleAutoshopBonus`](#networkearnfromvehicleautoshopbonus) · [`NetworkEarnFromVehicleExport`](#networkearnfromvehicleexport) · [`NetworkEarnFromWagePayment`](#networkearnfromwagepayment) · [`NetworkEarnFromWagePaymentBonus`](#networkearnfromwagepaymentbonus) · [`NetworkEarnFromWarehouse`](#networkearnfromwarehouse) · [`NetworkEarnGoon`](#networkearngoon) · [`NetworkEarnIslandHeist`](#networkearnislandheist) · [`NetworkEarnJobBonusFirstTimeBonus`](#networkearnjobbonusfirsttimebonus) · [`NetworkEarnJobBonusHeistAward`](#networkearnjobbonusheistaward) · [`NetworkGetEvcBalance`](#networkgetevcbalance) · [`NetworkGetIsHighEarner`](#networkgetishighearner) · [`NetworkGetPvcBalance`](#networkgetpvcbalance) · [`NetworkGetPvcTransferBalance`](#networkgetpvctransferbalance) · [`NetworkGetRemainingTransferBalance`](#networkgetremainingtransferbalance) · [`NetworkGetStringBankBalance`](#networkgetstringbankbalance) · [`NetworkGetStringBankWalletBalance`](#networkgetstringbankwalletbalance) · [`NetworkGetStringWalletBalance`](#networkgetstringwalletbalance) · [`NetworkGetVcBalance`](#networkgetvcbalance) · [`NetworkGetVcBankBalance`](#networkgetvcbankbalance) · [`NetworkGetVcBankBalanceIsNotLessThan`](#networkgetvcbankbalanceisnotlessthan) · [`NetworkGetVcBankWalletBalanceIsNotLessThan`](#networkgetvcbankwalletbalanceisnotlessthan) · [`NetworkGetVcWalletBalance`](#networkgetvcwalletbalance) · [`NetworkGetVcWalletBalanceIsNotLessThan`](#networkgetvcwalletbalanceisnotlessthan) · [`NetworkGivePlayerJobshareCash`](#networkgiveplayerjobsharecash) · [`NetworkInitializeCash`](#networkinitializecash) · [`NetworkManualDeleteCharacter`](#networkmanualdeletecharacter) · [`NetworkMoneyCanBet`](#networkmoneycanbet) · [`NetworkPayEmployeeWage`](#networkpayemployeewage) · [`NetworkPayMatchEntryFee`](#networkpaymatchentryfee) · [`NetworkPayUtilityBill`](#networkpayutilitybill) · [`NetworkReceivePlayerJobshareCash`](#networkreceiveplayerjobsharecash) · [`NetworkRefundCash`](#networkrefundcash) · [`NetworkRivalDeliveryCompleted`](#networkrivaldeliverycompleted) · [`NetworkSpentAmmoDrop`](#networkspentammodrop) · [`NetworkSpentArcadeGame`](#networkspentarcadegame) · [`NetworkSpentArcadeGeneric`](#networkspentarcadegeneric) · [`NetworkSpentArenaJoinSpectator`](#networkspentarenajoinspectator) · [`NetworkSpentArenaPremium`](#networkspentarenapremium) · [`NetworkSpentArenaSpectatorBox`](#networkspentarenaspectatorbox) · [`NetworkSpentArrestBail`](#networkspentarrestbail) · [`NetworkSpentAutoshopModifications`](#networkspentautoshopmodifications) · [`NetworkSpentAutoshopPropertyUtilityFee`](#networkspentautoshoppropertyutilityfee) · [`NetworkSpentBaService`](#networkspentbaservice) · [`NetworkSpentBallisticEquipment`](#networkspentballisticequipment) · [`NetworkSpentBankInterest`](#networkspentbankinterest) · [`NetworkSpentBeachPartyGeneric`](#networkspentbeachpartygeneric) · [`NetworkSpentBetting`](#networkspentbetting) · [`NetworkSpentBikeShopModify`](#networkspentbikeshopmodify) · [`NetworkSpentBoatPickup`](#networkspentboatpickup) · [`NetworkSpentBoss`](#networkspentboss) · [`NetworkSpentBounty`](#networkspentbounty) · [`NetworkSpentBountyHunterMission`](#networkspentbountyhuntermission) · [`NetworkSpentBullShark`](#networkspentbullshark) · [`NetworkSpentBusiness`](#networkspentbusiness) · [`NetworkSpentBuyArena`](#networkspentbuyarena) · [`NetworkSpentBuyAutoshop`](#networkspentbuyautoshop) · [`NetworkSpentBuyBase`](#networkspentbuybase) · [`NetworkSpentBuyBunker`](#networkspentbuybunker) · [`NetworkSpentBuyCasino`](#networkspentbuycasino) · [`NetworkSpentBuyOfftheradar`](#networkspentbuyofftheradar) · [`NetworkSpentBuyPassiveMode`](#networkspentbuypassivemode) · [`NetworkSpentBuyRevealPlayers`](#networkspentbuyrevealplayers) · [`NetworkSpentBuyTiltrotor`](#networkspentbuytiltrotor) · [`NetworkSpentBuyTruck`](#networkspentbuytruck) · [`NetworkSpentBuyWantedlevel`](#networkspentbuywantedlevel) · [`NetworkSpentCallPlayer`](#networkspentcallplayer) · [`NetworkSpentCarclub`](#networkspentcarclub) · [`NetworkSpentCarclubMembership`](#networkspentcarclubmembership) · [`NetworkSpentCarclubTakeover`](#networkspentcarclubtakeover) · [`NetworkSpentCargoSourcing`](#networkspentcargosourcing) · [`NetworkSpentCarwash`](#networkspentcarwash) · [`NetworkSpentCashDrop`](#networkspentcashdrop) · [`NetworkSpentCasinoClubGeneric`](#networkspentcasinoclubgeneric) · [`NetworkSpentCasinoGeneric`](#networkspentcasinogeneric) · [`NetworkSpentCasinoHeist`](#networkspentcasinoheist) · [`NetworkSpentCasinoHeistSkipMission`](#networkspentcasinoheistskipmission) · [`NetworkSpentCasinoMembership`](#networkspentcasinomembership) · [`NetworkSpentCinema`](#networkspentcinema) · [`NetworkSpentEmployAssassins`](#networkspentemployassassins) · [`NetworkSpentFromBank`](#networkspentfrombank) · [`NetworkSpentFromRockstar`](#networkspentfromrockstar) · [`NetworkSpentGangopsCannon`](#networkspentgangopscannon) · [`NetworkSpentGangopsStartMission`](#networkspentgangopsstartmission) · [`NetworkSpentGangopsStartStrand`](#networkspentgangopsstartstrand) · [`NetworkSpentGangopsTripSkip`](#networkspentgangopstripskip) · [`NetworkSpentGunrunningContactService`](#networkspentgunrunningcontactservice) · [`NetworkSpentHangarStaffCharges`](#networkspenthangarstaffcharges) · [`NetworkSpentHangarUtilityCharges`](#networkspenthangarutilitycharges) · [`NetworkSpentHeliPickup`](#networkspenthelipickup) · [`NetworkSpentHireMercenary`](#networkspenthiremercenary) · [`NetworkSpentHireMugger`](#networkspenthiremugger) · [`NetworkSpentHoldups`](#networkspentholdups) · [`NetworkSpentImAbility`](#networkspentimability) · [`NetworkSpentImportExportRepair`](#networkspentimportexportrepair) · [`NetworkSpentInStripclub`](#networkspentinstripclub) · [`NetworkSpentIslandHeist`](#networkspentislandheist) · [`NetworkSpentJobSkip`](#networkspentjobskip) · [`NetworkSpentJukebox`](#networkspentjukebox) · [`NetworkSpentMakeItRain`](#networkspentmakeitrain) · [`NetworkSpentMoveYacht`](#networkspentmoveyacht) · [`NetworkSpentNightclubBarDrink`](#networkspentnightclubbardrink) · [`NetworkSpentNightclubEntryFee`](#networkspentnightclubentryfee) · [`NetworkSpentNoCops`](#networkspentnocops) · [`NetworkSpentOrderBodyguardVehicle`](#networkspentorderbodyguardvehicle) · [`NetworkSpentOrderWarehouseVehicle`](#networkspentorderwarehousevehicle) · [`NetworkSpentPaServiceDancer`](#networkspentpaservicedancer) · [`NetworkSpentPaServiceHeliPickup`](#networkspentpaservicehelipickup) · [`NetworkSpentPayBoss`](#networkspentpayboss) · [`NetworkSpentPayGoon`](#networkspentpaygoon) · [`NetworkSpentPayVehicleInsurancePremium`](#networkspentpayvehicleinsurancepremium) · [`NetworkSpentPlayerHealthcare`](#networkspentplayerhealthcare) · [`NetworkSpentProstitutes`](#networkspentprostitutes) · [`NetworkSpentPurchaseHangar`](#networkspentpurchasehangar) · [`NetworkSpentPurchaseWarehouse`](#networkspentpurchasewarehouse) · [`NetworkSpentRdrhatchetBonus`](#networkspentrdrhatchetbonus) · [`NetworkSpentRehireDj`](#networkspentrehiredj) · [`NetworkSpentRenameOrganization`](#networkspentrenameorganization) · [`NetworkSpentRequestHeist`](#networkspentrequestheist) · [`NetworkSpentRequestJob`](#networkspentrequestjob) · [`NetworkSpentRobbedByMugger`](#networkspentrobbedbymugger) · [`NetworkSpentSalesDisplay`](#networkspentsalesdisplay) · [`NetworkSpentSpinTheWheelPayment`](#networkspentspinthewheelpayment) · [`NetworkSpentSubmarine`](#networkspentsubmarine) · [`NetworkSpentTaxi`](#networkspenttaxi) · [`NetworkSpentTelescope`](#networkspenttelescope) · [`NetworkSpentUpgradeArena`](#networkspentupgradearena) · [`NetworkSpentUpgradeAutoshop`](#networkspentupgradeautoshop) · [`NetworkSpentUpgradeBase`](#networkspentupgradebase) · [`NetworkSpentUpgradeBunker`](#networkspentupgradebunker) · [`NetworkSpentUpgradeCasino`](#networkspentupgradecasino) · [`NetworkSpentUpgradeHangar`](#networkspentupgradehangar) · [`NetworkSpentUpgradeSub`](#networkspentupgradesub) · [`NetworkSpentUpgradeTiltrotor`](#networkspentupgradetiltrotor) · [`NetworkSpentUpgradeTruck`](#networkspentupgradetruck) · [`NetworkSpentVehicleExportMods`](#networkspentvehicleexportmods) · [`NetworkSpentVehicleRequested`](#networkspentvehiclerequested) · [`NetworkSpentVipUtilityCharges`](#networkspentviputilitycharges) · [`NetworkSpentWager`](#networkspentwager) · [`ProcessCashGift`](#processcashgift) · [`WithdrawVc`](#withdrawvc)

---
### CanPayGoon

`_CAN_PAY_GOON` · hash `0x9777734DAD16992F` · **Cliente**

```lua
local retval = CanPayGoon()
```
```c
BOOL _CAN_PAY_GOON();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
NativeDB Added Parameter 2: int p1
NativeDB Added Parameter 3: int amount
NativeDB Added Parameter 4: int* p3
```

**Nombres antiguos (alias):** `0x9777734DAD16992F` (`N_0x9777734dad16992f`)

---
### DepositVc

`DEPOSIT_VC` · hash `0xE260E0BB9CD995AC` · jhash `0x8F266745` · **Cliente**

```lua
local retval = DepositVc(amount)
```
```c
BOOL DEPOSIT_VC(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Does nothing and always returns false.
```

**Nombres antiguos (alias):** `0xE260E0BB9CD995AC` (`N_0xe260e0bb9cd995ac`)

---
### N_0x08e8eeadfd0dc4a0

`0x08E8EEADFD0DC4A0` · hash `0x08E8EEADFD0DC4A0` · jhash `0x03461981` · **Cliente**

```lua
local retval = N_0x08e8eeadfd0dc4a0(amount)
```
```c
BOOL 0x08E8EEADFD0DC4A0(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns false if amount > wallet balance or daily transfer limit has been hit.

NativeDB Introduced: v323
```

---
### N_0x0d30eb83668e63c5

`0x0D30EB83668E63C5` · hash `0x0D30EB83668E63C5` · **Cliente**

```lua
N_0x0d30eb83668e63c5(p0, p1, p2, p3)
```
```c
void 0x0D30EB83668E63C5(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x0dd362f14f18942a

`0x0DD362F14F18942A` · hash `0x0DD362F14F18942A` · **Cliente**

```lua
N_0x0dd362f14f18942a(amount, p1, p2)
```
```c
void 0x0DD362F14F18942A(int amount, Any p1, Any p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x112209ce0290c03a

`0x112209CE0290C03A` · hash `0x112209CE0290C03A` · **Cliente**

```lua
N_0x112209ce0290c03a(p0, p1, p2, p3)
```
```c
void 0x112209CE0290C03A(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x1dc9b749e7ae282b

`0x1DC9B749E7AE282B` · hash `0x1DC9B749E7AE282B` · **Cliente**

```lua
N_0x1dc9b749e7ae282b(p0, p1, p2, p3)
```
```c
void 0x1DC9B749E7AE282B(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x226c284c830d0ca8

`0x226C284C830D0CA8` · hash `0x226C284C830D0CA8` · **Cliente**

```lua
N_0x226c284c830d0ca8(p0, p1, p2, p3)
```
```c
void 0x226C284C830D0CA8(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x2a7cec72c3443bcc

`0x2A7CEC72C3443BCC` · hash `0x2A7CEC72C3443BCC` · **Cliente**

```lua
N_0x2a7cec72c3443bcc(p0, p1, p2)
```
```c
void 0x2A7CEC72C3443BCC(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x2a93c46aab1eacc9

`0x2A93C46AAB1EACC9` · hash `0x2A93C46AAB1EACC9` · **Cliente**

```lua
N_0x2a93c46aab1eacc9(p0, p1, p2, p3)
```
```c
void 0x2A93C46AAB1EACC9(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x2afc2d19b50797f2

`0x2AFC2D19B50797F2` · hash `0x2AFC2D19B50797F2` · **Cliente**

```lua
N_0x2afc2d19b50797f2(p0, p1, p2, p3)
```
```c
void 0x2AFC2D19B50797F2(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x2fab6614ce22e196

`0x2FAB6614CE22E196` · hash `0x2FAB6614CE22E196` · **Cliente**

```lua
N_0x2fab6614ce22e196(p0, p1, p2, p3)
```
```c
void 0x2FAB6614CE22E196(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x31ba138f6304fb9f

`0x31BA138F6304FB9F` · hash `0x31BA138F6304FB9F` · **Cliente**

```lua
N_0x31ba138f6304fb9f(p0, p1)
```
```c
void 0x31BA138F6304FB9F(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x4128464231e3ca0b

`0x4128464231E3CA0B` · hash `0x4128464231E3CA0B` · **Cliente**

```lua
N_0x4128464231e3ca0b(p0, p1, p2, p3)
```
```c
void 0x4128464231E3CA0B(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x4c3b75694f7e0d9c

`0x4C3B75694F7E0D9C` · hash `0x4C3B75694F7E0D9C` · **Cliente**

```lua
N_0x4c3b75694f7e0d9c(p0, p1, p2)
```
```c
void 0x4C3B75694F7E0D9C(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x5574637681911fda

`0x5574637681911FDA` · hash `0x5574637681911FDA` · **Cliente**

```lua
N_0x5574637681911fda(p0, p1, p2, p3)
```
```c
void 0x5574637681911FDA(Any p0, Any p1, Any p2, Any p3);
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
### N_0x55a1e095db052fa5

`0x55A1E095DB052FA5` · hash `0x55A1E095DB052FA5` · **Cliente**

```lua
N_0x55a1e095db052fa5(p0, p1)
```
```c
void 0x55A1E095DB052FA5(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x5f456788b05faeac

`0x5F456788B05FAEAC` · hash `0x5F456788B05FAEAC` · **Cliente**

```lua
N_0x5f456788b05faeac(p0, p1, p2)
```
```c
void 0x5F456788B05FAEAC(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0x65482bfd0923c8a1

`0x65482BFD0923C8A1` · hash `0x65482BFD0923C8A1` · **Cliente**

```lua
N_0x65482bfd0923c8a1(p0, p1, p2, p3, p4, p5)
```
```c
void 0x65482BFD0923C8A1(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
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
NativeDB Introduced: v1493
```

---
### N_0x675d19c6067cae08

`0x675D19C6067CAE08` · hash `0x675D19C6067CAE08` · **Cliente**

```lua
N_0x675d19c6067cae08(p0, p1, p2, p3)
```
```c
void 0x675D19C6067CAE08(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x69ef772b192614c1

`0x69EF772B192614C1` · hash `0x69EF772B192614C1` · **Cliente**

```lua
N_0x69ef772b192614c1(p0, p1, p2, p3)
```
```c
void 0x69EF772B192614C1(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x6b7e4fb50d5f3d65

`0x6B7E4FB50D5F3D65` · hash `0x6B7E4FB50D5F3D65` · **Cliente**

```lua
N_0x6b7e4fb50d5f3d65(p0, p1, p2, p3, p4)
```
```c
void 0x6B7E4FB50D5F3D65(Any p0, Any p1, Any p2, Any p3, Any p4);
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
NativeDB Introduced: v1180
```

---
### N_0x6fcf8ddea146c45b

`0x6FCF8DDEA146C45B` · hash `0x6FCF8DDEA146C45B` · jhash `0xB96C7ABE` · **Cliente**

```lua
local retval = N_0x6fcf8ddea146c45b(p0)
```
```c
BOOL 0x6FCF8DDEA146C45B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 1.
```

---
### N_0x6fd97159fe3c971a

`0x6FD97159FE3C971A` · hash `0x6FD97159FE3C971A` · **Cliente**

```lua
N_0x6fd97159fe3c971a(p0, p1, p2, p3)
```
```c
void 0x6FD97159FE3C971A(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x7c4fccd2e4deb394

`0x7C4FCCD2E4DEB394` · hash `0x7C4FCCD2E4DEB394` · jhash `0x468CC978` · **Cliente**

```lua
local retval = N_0x7c4fccd2e4deb394()
```
```c
BOOL 0x7C4FCCD2E4DEB394();
```

**Devuelve:** `BOOL`

---
### N_0x870289a558348378

`0x870289A558348378` · hash `0x870289A558348378` · **Cliente**

```lua
N_0x870289a558348378(p0, p1, p2, p3)
```
```c
void 0x870289A558348378(Any p0, Any p1, Any p2, Any p3);
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
### N_0x8e243837643d9583

`0x8E243837643D9583` · hash `0x8E243837643D9583` · **Cliente**

```lua
N_0x8e243837643d9583(p0, p1, p2, p3)
```
```c
void 0x8E243837643D9583(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x90cd7c6871fbf1b4

`0x90CD7C6871FBF1B4` · hash `0x90CD7C6871FBF1B4` · **Cliente**

```lua
N_0x90cd7c6871fbf1b4(p0, p1, p2, p3)
```
```c
void 0x90CD7C6871FBF1B4(Any p0, Any p1, Any p2, Any p3);
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
### N_0x998e18ceb44487fc

`0x998E18CEB44487FC` · hash `0x998E18CEB44487FC` · **Cliente**

```lua
N_0x998e18ceb44487fc(p0, p1, p2, p3)
```
```c
void 0x998E18CEB44487FC(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0x9b5016a6433a68c5

`0x9B5016A6433A68C5` · hash `0x9B5016A6433A68C5` · jhash `0xBD64F1B7` · **Cliente**

```lua
local retval = N_0x9b5016a6433a68c5()
```
```c
Any 0x9B5016A6433A68C5();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
Hardcoded to return 0.

NativeDB Introduced: v323
```

---
### N_0xa51338e0dccd4065

`0xA51338E0DCCD4065` · hash `0xA51338E0DCCD4065` · **Cliente**

```lua
N_0xa51338e0dccd4065(p0, p1, p2)
```
```c
void 0xA51338E0DCCD4065(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xa51b086b0b2c0f7a

`0xA51B086B0B2C0F7A` · hash `0xA51B086B0B2C0F7A` · **Cliente**

```lua
N_0xa51b086b0b2c0f7a(p0, p1, p2, p3)
```
```c
void 0xA51B086B0B2C0F7A(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0xa95cfb4e02390842

`0xA95CFB4E02390842` · hash `0xA95CFB4E02390842` · **Cliente**

```lua
N_0xa95cfb4e02390842(p0, p1, p2)
```
```c
void 0xA95CFB4E02390842(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0xa95f667a755725da

`0xA95F667A755725DA` · hash `0xA95F667A755725DA` · **Cliente**

```lua
N_0xa95f667a755725da(p0, p1, p2, p3)
```
```c
void 0xA95F667A755725DA(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0xb4c2ec463672474e

`0xB4C2EC463672474E` · hash `0xB4C2EC463672474E` · **Cliente**

```lua
N_0xb4c2ec463672474e(p0, p1, p2, p3)
```
```c
void 0xB4C2EC463672474E(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0xb4deae67f35e2acd

`0xB4DEAE67F35E2ACD` · hash `0xB4DEAE67F35E2ACD` · **Cliente**

```lua
N_0xb4deae67f35e2acd(p0)
```
```c
void 0xB4DEAE67F35E2ACD(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0xb5b58e24868cb09e

`0xB5B58E24868CB09E` · hash `0xB5B58E24868CB09E` · **Cliente**

```lua
N_0xb5b58e24868cb09e(p0, p1, p2, p3, p4)
```
```c
void 0xB5B58E24868CB09E(Any p0, Any p1, Any p2, Any p3, Any p4);
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
### N_0xbd0efb25cca8f97a

`0xBD0EFB25CCA8F97A` · hash `0xBD0EFB25CCA8F97A` · **Cliente**

```lua
N_0xbd0efb25cca8f97a(p0, p1, p2, p3)
```
```c
void 0xBD0EFB25CCA8F97A(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0xc6e74cf8c884c880

`0xC6E74CF8C884C880` · hash `0xC6E74CF8C884C880` · **Cliente**

```lua
N_0xc6e74cf8c884c880(p0, p1, p2, p3, p4, p5, p6)
```
```c
void 0xC6E74CF8C884C880(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
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
NativeDB Introduced: v1493
```

---
### N_0xcd0f5b5d932ae473

`0xCD0F5B5D932AE473` · hash `0xCD0F5B5D932AE473` · jhash `0xC4CD928D` · **Cliente**

```lua
N_0xcd0f5b5d932ae473()
```
```c
void 0xCD0F5B5D932AE473();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing (it's a nullsub).

NativeDB Introduced: v323
```

---
### N_0xcd4d66b43b1dd28d

`0xCD4D66B43B1DD28D` · hash `0xCD4D66B43B1DD28D` · **Cliente**

```lua
N_0xcd4d66b43b1dd28d(p0, p1, p2)
```
```c
void 0xCD4D66B43B1DD28D(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xd29334ed1a256dbf

`0xD29334ED1A256DBF` · hash `0xD29334ED1A256DBF` · **Cliente**

```lua
N_0xd29334ed1a256dbf(p0, p1, p2, p3, p4)
```
```c
void 0xD29334ED1A256DBF(Any p0, Any p1, Any p2, Any p3, Any p4);
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
### N_0xde68e30d89f97132

`0xDE68E30D89F97132` · hash `0xDE68E30D89F97132` · **Cliente**

```lua
N_0xde68e30d89f97132(amount, p1)
```
```c
void 0xDE68E30D89F97132(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0xe0f82d68c7039158

`0xE0F82D68C7039158` · hash `0xE0F82D68C7039158` · **Cliente**

```lua
N_0xe0f82d68c7039158(p0)
```
```c
void 0xE0F82D68C7039158(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0xe154b48b68ef72bc

`0xE154B48B68EF72BC` · hash `0xE154B48B68EF72BC` · jhash `0x531E4892` · **Cliente**

```lua
local retval = N_0xe154b48b68ef72bc(p0)
```
```c
BOOL 0xE154B48B68EF72BC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 1.  
```

---
### N_0xe23adc6fcb1f29ae

`0xE23ADC6FCB1F29AE` · hash `0xE23ADC6FCB1F29AE` · **Cliente**

```lua
N_0xe23adc6fcb1f29ae(p0, p1, p2)
```
```c
void 0xE23ADC6FCB1F29AE(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0xe2bb399d90942091

`0xE2BB399D90942091` · hash `0xE2BB399D90942091` · **Cliente**

```lua
N_0xe2bb399d90942091(p0, p1)
```
```c
void 0xE2BB399D90942091(Any p0, Any p1);
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
### N_0xe2e244ab823b4483

`0xE2E244AB823B4483` · hash `0xE2E244AB823B4483` · **Cliente**

```lua
N_0xe2e244ab823b4483(amount, p1)
```
```c
void 0xE2E244AB823B4483(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0xed5fd7af10f5e262

`0xED5FD7AF10F5E262` · hash `0xED5FD7AF10F5E262` · **Cliente**

```lua
N_0xed5fd7af10f5e262(p0, p1, p2, p3)
```
```c
void 0xED5FD7AF10F5E262(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0xed76d195e6e3bf7f

`0xED76D195E6E3BF7F` · hash `0xED76D195E6E3BF7F` · **Cliente**

```lua
N_0xed76d195e6e3bf7f(p0, p1, p2, p3)
```
```c
void 0xED76D195E6E3BF7F(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0xfa07759e6fddd7cf

`0xFA07759E6FDDD7CF` · hash `0xFA07759E6FDDD7CF` · **Cliente**

```lua
N_0xfa07759e6fddd7cf(p0, p1, p2, p3)
```
```c
void 0xFA07759E6FDDD7CF(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### NetworkBuyAirstrike

`NETWORK_BUY_AIRSTRIKE` · hash `0x763B4BD305338F19` · jhash `0x40470683` · **Cliente**

```lua
NetworkBuyAirstrike(cost, p1, p2)
```
```c
void NETWORK_BUY_AIRSTRIKE(int cost, BOOL p1, BOOL p2);
```

**Parámetros**

- `cost` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 = 0 (always)  
p2 = 1 (always)  
```

---
### NetworkBuyBackupGang

`NETWORK_BUY_BACKUP_GANG` · hash `0xA3EDDAA42411D3B9` · jhash `0x2AD2EC51` · **Cliente**

```lua
NetworkBuyBackupGang(p0, p1, p2, p3)
```
```c
void NETWORK_BUY_BACKUP_GANG(int p0, int p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkBuyBounty

`NETWORK_BUY_BOUNTY` · hash `0x7B718E197453F2D9` · jhash `0xCB89CBE0` · **Cliente**

```lua
NetworkBuyBounty(amount, victim, p2, p3)
```
```c
void NETWORK_BUY_BOUNTY(int amount, Player victim, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `victim` (`Player`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is just an assumption. p2 was false and p3 was true.  
```

---
### NetworkBuyContraband

`_NETWORK_BUY_CONTRABAND` · hash `0x30FD873ECE50E9F6` · **Cliente**

```lua
NetworkBuyContraband(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_BUY_CONTRABAND(int p0, int p1, Hash p2, BOOL p3, BOOL p4);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p3` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x30FD873ECE50E9F6` (`N_0x30fd873ece50e9f6`)

---
### NetworkBuyFairgroundRide

`NETWORK_BUY_FAIRGROUND_RIDE` · hash `0x8A7B3952DD64D2B5` · jhash `0xD9622D64` · **Cliente**

```lua
NetworkBuyFairgroundRide(amountSpent, p1, p2, p3)
```
```c
void NETWORK_BUY_FAIRGROUND_RIDE(int amountSpent, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `amountSpent` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
The first parameter is the amount spent which is store in a global when this native is called. The global returns 10. Which is the price for both rides.  
The last 3 parameters are,   
2,0,1 in the am_ferriswheel.c  
1,0,1 in the am_rollercoaster.c  
```

**Nombres antiguos (alias):** `0x8A7B3952DD64D2B5` (`N_0x8a7b3952dd64d2b5`)

---
### NetworkBuyHealthcare

`NETWORK_BUY_HEALTHCARE` · hash `0xD9B067E55253E3DD` · jhash `0x832150E5` · **Cliente**

```lua
NetworkBuyHealthcare(cost, p1, p2)
```
```c
void NETWORK_BUY_HEALTHCARE(int cost, BOOL p1, BOOL p2);
```

**Parámetros**

- `cost` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkBuyHeliStrike

`NETWORK_BUY_HELI_STRIKE` · hash `0x81AA4610E3FD3A69` · jhash `0x047547D4` · **Cliente**

```lua
NetworkBuyHeliStrike(cost, p1, p2)
```
```c
void NETWORK_BUY_HELI_STRIKE(int cost, BOOL p1, BOOL p2);
```

**Parámetros**

- `cost` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 = 0 (always)  
p2 = 1 (always)  
```

---
### NetworkBuyItem

`NETWORK_BUY_ITEM` · hash `0xF0077C797F66A355` · jhash `0xA07B6368` · **Cliente**

```lua
NetworkBuyItem(amount, item, p2, p3, p4, item_name, p6, p7, p8, p9)
```
```c
void NETWORK_BUY_ITEM(int amount, Hash item, Any p2, Any p3, BOOL p4, char* item_name, Any p6, Any p7, Any p8, BOOL p9);
```

**Parámetros**

- `amount` (`int`)
- `item` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`BOOL`)
- `item_name` (`char*`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`BOOL`)

**Devuelve:** `void`

---
### NetworkBuyLotteryTicket

`NETWORK_BUY_LOTTERY_TICKET` · hash `0xD987F2489969668C` · jhash `0xF64DF4CF` · **Cliente**

```lua
NetworkBuyLotteryTicket(p0, p1, p2, p3)
```
```c
void NETWORK_BUY_LOTTERY_TICKET(int p0, int p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkBuyProperty

`NETWORK_BUY_PROPERTY` · hash `0x650A08A280870AF6` · jhash `0x7D479AAB` · **Cliente**

```lua
NetworkBuyProperty(propertyCost, propertyName, p2, p3)
```
```c
void NETWORK_BUY_PROPERTY(int propertyCost, Hash propertyName, BOOL p2, BOOL p3);
```

**Parámetros**

- `propertyCost` (`int`)
- `propertyName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### NetworkBuySmokes

`NETWORK_BUY_SMOKES` · hash `0x75AF80E61248EEBD` · jhash `0xC0AB03EB` · **Cliente**

```lua
NetworkBuySmokes(p0, p1, p2)
```
```c
void NETWORK_BUY_SMOKES(int p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkCanBet

`NETWORK_CAN_BET` · hash `0x3A54E33660DED67F` · jhash `0xE3802533` · **Cliente**

```lua
local retval = NetworkCanBet(amount)
```
```c
BOOL NETWORK_CAN_BET(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3A54E33660DED67F` (`N_0x3a54e33660ded67f`)

---
### NetworkCanBuyLotteryTicket

`NETWORK_CAN_BUY_LOTTERY_TICKET` · hash `0xC62DD18375C99130` · jhash `0x334B9364` · **Cliente**

```lua
local retval = NetworkCanBuyLotteryTicket(cost)
```
```c
BOOL NETWORK_CAN_BUY_LOTTERY_TICKET(int cost);
```

**Parámetros**

- `cost` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkCanReceivePlayerCash

`NETWORK_CAN_RECEIVE_PLAYER_CASH` · hash `0x5D17BE59D2123284` · jhash `0x41F5F10E` · **Cliente**

```lua
local retval = NetworkCanReceivePlayerCash(p0, p1, p2, p3)
```
```c
BOOL NETWORK_CAN_RECEIVE_PLAYER_CASH(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

---
### NetworkCanShareJobCash

`NETWORK_CAN_SHARE_JOB_CASH` · hash `0x1C2473301B1C66BA` · jhash `0xA27B9FE8` · **Cliente**

```lua
local retval = NetworkCanShareJobCash()
```
```c
BOOL NETWORK_CAN_SHARE_JOB_CASH();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1C2473301B1C66BA` (`N_0x1c2473301b1c66ba`)

---
### NetworkCanSpendMoney

`NETWORK_CAN_SPEND_MONEY` · hash `0xAB3CAA6B422164DA` · jhash `0x5AA379D9` · **Cliente**

```lua
local retval = NetworkCanSpendMoney(p0, p1, p2, p3, p4)
```
```c
BOOL NETWORK_CAN_SPEND_MONEY(Any p0, BOOL p1, BOOL p2, BOOL p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 6: Any p5
```

**Nombres antiguos (alias):** `0xAB3CAA6B422164DA` (`N_0xab3caa6b422164da`)

---
### NetworkCanSpendMoney_2

`_NETWORK_CAN_SPEND_MONEY_2` · hash `0x7303E27CC6532080` · **Cliente**

```lua
local retval, p4 = NetworkCanSpendMoney_2(p0, p1, p2, p3, p5)
```
```c
BOOL _NETWORK_CAN_SPEND_MONEY_2(Any p0, BOOL p1, BOOL p2, BOOL p3, Any* p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p5` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NETWORK_CAN_R??? or NETWORK_CAN_S???  
```

```
NativeDB Added Parameter 7: Any p6
```

**Nombres antiguos (alias):** `0x7303E27CC6532080` (`N_0x7303e27cc6532080`)

---
### NetworkCasinoCanGamble

`_NETWORK_CASINO_CAN_GAMBLE` · hash `0xF62F6D9528358FE4` · **Cliente**

```lua
local retval = NetworkCasinoCanGamble(p0)
```
```c
BOOL _NETWORK_CASINO_CAN_GAMBLE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

NETWORK_C\*

```
NativeDB Introduced: v1734
```

---
### NetworkCasinoCanPurchaseChipsWithPvc

`_NETWORK_CASINO_CAN_PURCHASE_CHIPS_WITH_PVC` · hash `0x394DCDB9E836B7A9` · **Cliente**

```lua
local retval = NetworkCasinoCanPurchaseChipsWithPvc()
```
```c
BOOL _NETWORK_CASINO_CAN_PURCHASE_CHIPS_WITH_PVC();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

Same as 0x8968D4D8C6C40C11.
NETWORK_C\*

```
NativeDB Introduced: v1734
```

---
### NetworkCasinoCanPurchaseChipsWithPvc_2

`_NETWORK_CASINO_CAN_PURCHASE_CHIPS_WITH_PVC_2` · hash `0x8968D4D8C6C40C11` · **Cliente**

```lua
local retval = NetworkCasinoCanPurchaseChipsWithPvc_2()
```
```c
BOOL _NETWORK_CASINO_CAN_PURCHASE_CHIPS_WITH_PVC_2();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

Same as 0x394DCDB9E836B7A9.
NETWORK_C\*

```
NativeDB Introduced: v1734
```

---
### NetworkCasinoCanUseGamblingType

`_NETWORK_CASINO_CAN_USE_GAMBLING_TYPE` · hash `0x158C16F5E4CF41F8` · **Cliente**

```lua
local retval = NetworkCasinoCanUseGamblingType(hash)
```
```c
BOOL _NETWORK_CASINO_CAN_USE_GAMBLING_TYPE(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

GTAO_CASINO_HOUSE
GTAO_CASINO_INSIDETRACK
GTAO_CASINO_LUCKYWHEEL
GTAO_CASINO_BLACKJACK
GTAO_CASINO_ROULETTE
GTAO_CASINO_SLOTS
GTAO_CASINO_PURCHASE_CHIPS
NETWORK_C\*

```
NativeDB Introduced: v1734
```

---
### NetworkCasinoPurchaseChips

`_NETWORK_CASINO_PURCHASE_CHIPS` · hash `0x3BD101471C7F9EEC` · **Cliente**

```lua
local retval = NetworkCasinoPurchaseChips(p0, p1)
```
```c
BOOL _NETWORK_CASINO_PURCHASE_CHIPS(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

NETWORK_C\*

```
NativeDB Introduced: v1734
```

---
### NetworkCasinoSellChips

`_NETWORK_CASINO_SELL_CHIPS` · hash `0xED44897CB336F480` · **Cliente**

```lua
local retval = NetworkCasinoSellChips(p0, p1)
```
```c
BOOL _NETWORK_CASINO_SELL_CHIPS(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

NETWORK_C\*

```
NativeDB Introduced: v1734
```

---
### NetworkClearCharacterWallet

`NETWORK_CLEAR_CHARACTER_WALLET` · hash `0xA921DED15FDF28F5` · jhash `0x19F0C471` · **Cliente**

```lua
NetworkClearCharacterWallet(characterSlot)
```
```c
void NETWORK_CLEAR_CHARACTER_WALLET(int characterSlot);
```

**Parámetros**

- `characterSlot` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA921DED15FDF28F5` (`N_0xa921ded15fdf28f5`)

---
### NetworkDeductCash

`_NETWORK_DEDUCT_CASH` · hash `0x18B7AE224B087E26` · **Cliente**

```lua
NetworkDeductCash(amount, p1, p2, p3, p4, p5)
```
```c
void _NETWORK_DEDUCT_CASH(int amount, char* p1, char* p2, BOOL p3, BOOL p4, BOOL p5);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`char*`)
- `p2` (`char*`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkDeleteCharacter

`NETWORK_DELETE_CHARACTER` · hash `0x05A50AF38947EB8D` · jhash `0xA9F7E9C3` · **Cliente**

```lua
NetworkDeleteCharacter(characterSlot, p1, p2)
```
```c
void NETWORK_DELETE_CHARACTER(int characterSlot, BOOL p1, BOOL p2);
```

**Parámetros**

- `characterSlot` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Note the 2nd parameters are always 1, 0. I have a feeling it deals with your money, wallet, bank. So when you delete the character it of course wipes the wallet cash at that time. So if that was the case, it would be eg, NETWORK_DELETE_CHARACTER(characterIndex, deleteWalletCash, deleteBankCash);  
```

---
### NetworkEarnBoss

`_NETWORK_EARN_BOSS` · hash `0x08B0CA7A6AB3AC32` · **Cliente**

```lua
NetworkEarnBoss(p0, p1, p2)
```
```c
void _NETWORK_EARN_BOSS(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x08B0CA7A6AB3AC32` (`N_0x08b0ca7a6ab3ac32`)

---
### NetworkEarnBossAgency

`_NETWORK_EARN_BOSS_AGENCY` · hash `0x0CB1BE0633C024A8` · **Cliente**

```lua
NetworkEarnBossAgency(p0, p1, p2, p3)
```
```c
void _NETWORK_EARN_BOSS_AGENCY(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0CB1BE0633C024A8` (`N_0x0cb1be0633c024a8`)

---
### NetworkEarnBountyHunterReward

`_NETWORK_EARN_BOUNTY_HUNTER_REWARD` · hash `0xF6B170F9A02E9E87` · **Cliente**

```lua
NetworkEarnBountyHunterReward(p0)
```
```c
void _NETWORK_EARN_BOUNTY_HUNTER_REWARD(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0xF6B170F9A02E9E87` (`N_0xf6b170f9a02e9e87`)

---
### NetworkEarnCasinoHeist

`_NETWORK_EARN_CASINO_HEIST` · hash `0x72E7C7B9615FA3C3` · **Cliente**

```lua
NetworkEarnCasinoHeist(p0, p1, p2, p3, p4, p5, p6)
```
```c
void _NETWORK_EARN_CASINO_HEIST(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
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
NativeDB Introduced: v1868
```

---
### NetworkEarnCasinoHeistBonus

`_NETWORK_EARN_CASINO_HEIST_BONUS` · hash `0x3EC7471E6909798A` · **Cliente**

```lua
NetworkEarnCasinoHeistBonus(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_EARN_CASINO_HEIST_BONUS(Any p0, Any p1, Any p2, Any p3, Any p4);
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
### NetworkEarnCollectableCompletedCollection

`_NETWORK_EARN_COLLECTABLE_COMPLETED_COLLECTION` · hash `0x5C9B198AF5A54FA6` · **Cliente**

```lua
NetworkEarnCollectableCompletedCollection(amount, p1)
```
```c
void _NETWORK_EARN_COLLECTABLE_COMPLETED_COLLECTION(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### NetworkEarnFmbbWageBonus

`_NETWORK_EARN_FMBB_WAGE_BONUS` · hash `0xFFFBA1B1F7C0B6F4` · **Cliente**

```lua
NetworkEarnFmbbWageBonus(p0)
```
```c
void _NETWORK_EARN_FMBB_WAGE_BONUS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0xFFFBA1B1F7C0B6F4` (`N_0xfffba1b1f7c0b6f4`)

---
### NetworkEarnFromAiTargetKill

`NETWORK_EARN_FROM_AI_TARGET_KILL` · hash `0x515B4A22E4D3C6D7` · jhash `0x866004A8` · **Cliente**

```lua
NetworkEarnFromAiTargetKill(p0, p1)
```
```c
void NETWORK_EARN_FROM_AI_TARGET_KILL(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
DSPORT  
```

**Nombres antiguos (alias):** `0x515B4A22E4D3C6D7` (`N_0x515b4a22e4d3c6d7`)

---
### NetworkEarnFromAmbientJob

`NETWORK_EARN_FROM_AMBIENT_JOB` · hash `0xFB6DB092FBAE29E6` · jhash `0xA14CC95D` · **Cliente**

```lua
local p2 = NetworkEarnFromAmbientJob(p0, p1, p2)
```
```c
void NETWORK_EARN_FROM_AMBIENT_JOB(int p0, char* p1, Any* p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`char*`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Example for p1: "AM_DISTRACT_COPS"  
```

**Nombres antiguos (alias):** `0xFB6DB092FBAE29E6` (`N_0xfb6db092fbae29e6`), `_NETWORK_EARN_FROM_AMBIENT_JOB` (`NetworkEarnFromAmbientJob`)

---
### NetworkEarnFromArenaCareerProgression

`_NETWORK_EARN_FROM_ARENA_CAREER_PROGRESSION` · hash `0x0F99F70C61F14619` · **Cliente**

```lua
NetworkEarnFromArenaCareerProgression(amount, p1)
```
```c
void _NETWORK_EARN_FROM_ARENA_CAREER_PROGRESSION(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromArenaSkillLevelProgression

`_NETWORK_EARN_FROM_ARENA_SKILL_LEVEL_PROGRESSION` · hash `0xE08256F972C7BB2C` · **Cliente**

```lua
NetworkEarnFromArenaSkillLevelProgression(amount, p1)
```
```c
void _NETWORK_EARN_FROM_ARENA_SKILL_LEVEL_PROGRESSION(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromArenaWar

`_NETWORK_EARN_FROM_ARENA_WAR` · hash `0x631F1CB8FB4130AA` · **Cliente**

```lua
NetworkEarnFromArenaWar(amount, p1, p2, p3)
```
```c
void _NETWORK_EARN_FROM_ARENA_WAR(int amount, Any p1, Any p2, Any p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromArmourTruck

`_NETWORK_EARN_FROM_ARMOUR_TRUCK` · hash `0xF514621E8EA463D0` · jhash `0x30B3EC0A` · **Cliente**

```lua
NetworkEarnFromArmourTruck(amount)
```
```c
void _NETWORK_EARN_FROM_ARMOUR_TRUCK(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
For the money bags that drop a max of $40,000. Often called 40k bags.
Most likely NETWORK_EARN_FROM_ROB***
```

**Nombres antiguos (alias):** `0xF514621E8EA463D0` (`N_0xf514621e8ea463d0`)

---
### NetworkEarnFromAssassinateTargetKilled

`_NETWORK_EARN_FROM_ASSASSINATE_TARGET_KILLED` · hash `0xFA700D8A9905F78A` · **Cliente**

```lua
NetworkEarnFromAssassinateTargetKilled(amount)
```
```c
void _NETWORK_EARN_FROM_ASSASSINATE_TARGET_KILLED(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromAssassinateTargetKilled_2

`_NETWORK_EARN_FROM_ASSASSINATE_TARGET_KILLED_2` · hash `0x5E7AE8AABE8B7C0D` · **Cliente**

```lua
NetworkEarnFromAssassinateTargetKilled_2(amount)
```
```c
void _NETWORK_EARN_FROM_ASSASSINATE_TARGET_KILLED_2(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromAutoshopBusiness

`_NETWORK_EARN_FROM_AUTOSHOP_BUSINESS` · hash `0x36A7FD5A7194B03E` · **Cliente**

```lua
NetworkEarnFromAutoshopBusiness(p0, p1)
```
```c
void _NETWORK_EARN_FROM_AUTOSHOP_BUSINESS(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x36A7FD5A7194B03E` (`N_0x36a7fd5a7194b03e`)

---
### NetworkEarnFromAutoshopIncome

`_NETWORK_EARN_FROM_AUTOSHOP_INCOME` · hash `0xC66D1CF99ED7FE25` · **Cliente**

```lua
NetworkEarnFromAutoshopIncome(p0)
```
```c
void _NETWORK_EARN_FROM_AUTOSHOP_INCOME(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xC66D1CF99ED7FE25` (`N_0xc66d1cf99ed7fe25`)

---
### NetworkEarnFromBbEventBonus

`_NETWORK_EARN_FROM_BB_EVENT_BONUS` · hash `0xFDD8D2440DAF1590` · **Cliente**

```lua
NetworkEarnFromBbEventBonus(amount)
```
```c
void _NETWORK_EARN_FROM_BB_EVENT_BONUS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromBbEventCargo

`_NETWORK_EARN_FROM_BB_EVENT_CARGO` · hash `0xA82959062361B259` · **Cliente**

```lua
NetworkEarnFromBbEventCargo(amount)
```
```c
void _NETWORK_EARN_FROM_BB_EVENT_CARGO(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromBendJob

`NETWORK_EARN_FROM_BEND_JOB` · hash `0x61326EE6DF15B0CA` · jhash `0xBB293400` · **Cliente**

```lua
NetworkEarnFromBendJob(amount, heistHash)
```
```c
void NETWORK_EARN_FROM_BEND_JOB(int amount, char* heistHash);
```

**Parámetros**

- `amount` (`int`)
- `heistHash` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x61326EE6DF15B0CA` (`N_0x61326ee6df15b0ca`), `NETWORK_EARN_FROM_MISSION_H` (`NetworkEarnFromMissionH`)

---
### NetworkEarnFromBetting

`NETWORK_EARN_FROM_BETTING` · hash `0x827A5BA1A44ACA6D` · jhash `0xA0F7F07C` · **Cliente**

```lua
NetworkEarnFromBetting(amount, p1)
```
```c
void NETWORK_EARN_FROM_BETTING(int amount, char* p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`char*`)

**Devuelve:** `void`

---
### NetworkEarnFromBikeShopBusiness

`_NETWORK_EARN_FROM_BIKE_SHOP_BUSINESS` · hash `0x2C5809EB9DF57257` · **Cliente**

```lua
NetworkEarnFromBikeShopBusiness(p0, p1)
```
```c
void _NETWORK_EARN_FROM_BIKE_SHOP_BUSINESS(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkEarnFromBikerIncome

`_NETWORK_EARN_FROM_BIKER_INCOME` · hash `0x71BEC32FA466E105` · **Cliente**

```lua
NetworkEarnFromBikerIncome(p0)
```
```c
void _NETWORK_EARN_FROM_BIKER_INCOME(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkEarnFromBounty

`NETWORK_EARN_FROM_BOUNTY` · hash `0x131BB5DA15453ACF` · jhash `0x127F2DAE` · **Cliente**

```lua
local networkHandle, p2 = NetworkEarnFromBounty(amount, p3)
```
```c
void NETWORK_EARN_FROM_BOUNTY(int amount, int* networkHandle, Any* p2, Any p3);
```

**Parámetros**

- `amount` (`int`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any`)

**Devuelve:** `void`

---
### NetworkEarnFromBusinessBattle

`_NETWORK_EARN_FROM_BUSINESS_BATTLE` · hash `0x42FCE14F50F27291` · **Cliente**

```lua
NetworkEarnFromBusinessBattle(p0)
```
```c
void _NETWORK_EARN_FROM_BUSINESS_BATTLE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x42FCE14F50F27291` (`N_0x42fce14f50f27291`)

---
### NetworkEarnFromBusinessHubSell

`_NETWORK_EARN_FROM_BUSINESS_HUB_SELL` · hash `0x0B39CF0D53F1C883` · **Cliente**

```lua
NetworkEarnFromBusinessHubSell(p0, p1, p2)
```
```c
void _NETWORK_EARN_FROM_BUSINESS_HUB_SELL(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x0B39CF0D53F1C883` (`N_0x0b39cf0d53f1c883`)

---
### NetworkEarnFromBusinessHubSource

`_NETWORK_EARN_FROM_BUSINESS_HUB_SOURCE` · hash `0x59498BC8B1C8B15C` · **Cliente**

```lua
NetworkEarnFromBusinessHubSource(p0, p1, p2, p3)
```
```c
void _NETWORK_EARN_FROM_BUSINESS_HUB_SOURCE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkEarnFromBusinessProduct

`_NETWORK_EARN_FROM_BUSINESS_PRODUCT` · hash `0x8586789730B10CAF` · **Cliente**

```lua
NetworkEarnFromBusinessProduct(amount, p1, p2, p3)
```
```c
void _NETWORK_EARN_FROM_BUSINESS_PRODUCT(int amount, Any p1, Any p2, Any p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8586789730B10CAF` (`N_0x8586789730b10caf`)

---
### NetworkEarnFromCarclubMembership

`_NETWORK_EARN_FROM_CARCLUB_MEMBERSHIP` · hash `0xBC6227792A188E2E` · **Cliente**

```lua
NetworkEarnFromCarclubMembership(p0)
```
```c
void _NETWORK_EARN_FROM_CARCLUB_MEMBERSHIP(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xBC6227792A188E2E` (`N_0xbc6227792a188e2e`)

---
### NetworkEarnFromCashingOut

`_NETWORK_EARN_FROM_CASHING_OUT` · hash `0xEFE9C9A1651B81E6` · **Cliente**

```lua
NetworkEarnFromCashingOut(amount)
```
```c
void _NETWORK_EARN_FROM_CASHING_OUT(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromCasinoAward

`_NETWORK_EARN_FROM_CASINO_AWARD` · hash `0x973A9781A34F8DEB` · **Cliente**

```lua
NetworkEarnFromCasinoAward(amount, hash)
```
```c
void _NETWORK_EARN_FROM_CASINO_AWARD(int amount, Hash hash);
```

**Parámetros**

- `amount` (`int`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromCasinoMissionParticipation

`_NETWORK_EARN_FROM_CASINO_MISSION_PARTICIPATION` · hash `0x09E8F18641BE2575` · **Cliente**

```lua
NetworkEarnFromCasinoMissionParticipation(amount)
```
```c
void _NETWORK_EARN_FROM_CASINO_MISSION_PARTICIPATION(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromCasinoMissionReward

`_NETWORK_EARN_FROM_CASINO_MISSION_REWARD` · hash `0x566FD402B25787DE` · **Cliente**

```lua
NetworkEarnFromCasinoMissionReward(amount)
```
```c
void _NETWORK_EARN_FROM_CASINO_MISSION_REWARD(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromCasinoStoryMissionReward

`_NETWORK_EARN_FROM_CASINO_STORY_MISSION_REWARD` · hash `0xAC95ED552157E092` · **Cliente**

```lua
NetworkEarnFromCasinoStoryMissionReward(amount)
```
```c
void _NETWORK_EARN_FROM_CASINO_STORY_MISSION_REWARD(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromChallengeWin

`NETWORK_EARN_FROM_CHALLENGE_WIN` · hash `0x2B171E6B2F64D8DF` · jhash `0x2BEFB6C4` · **Cliente**

```lua
local p1 = NetworkEarnFromChallengeWin(p0, p2)
```
```c
void NETWORK_EARN_FROM_CHALLENGE_WIN(Any p0, Any* p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2B171E6B2F64D8DF` (`N_0x2b171e6b2f64d8df`)

---
### NetworkEarnFromClubManagementParticipation

`_NETWORK_EARN_FROM_CLUB_MANAGEMENT_PARTICIPATION` · hash `0xA75EAC69F59E96E7` · **Cliente**

```lua
NetworkEarnFromClubManagementParticipation(p0)
```
```c
void _NETWORK_EARN_FROM_CLUB_MANAGEMENT_PARTICIPATION(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0xA75EAC69F59E96E7` (`N_0xa75eac69f59e96e7`)

---
### NetworkEarnFromCollectablesActionFigures

`_NETWORK_EARN_FROM_COLLECTABLES_ACTION_FIGURES` · hash `0x5517F90043466049` · **Cliente**

```lua
NetworkEarnFromCollectablesActionFigures(amount)
```
```c
void _NETWORK_EARN_FROM_COLLECTABLES_ACTION_FIGURES(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromCollectionItem

`_NETWORK_EARN_FROM_COLLECTION_ITEM` · hash `0x84FF63BD4966F33D` · **Cliente**

```lua
NetworkEarnFromCollectionItem(amount, p1)
```
```c
void _NETWORK_EARN_FROM_COLLECTION_ITEM(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromCompleteCollection

`_NETWORK_EARN_FROM_COMPLETE_COLLECTION` · hash `0x83AD64F53F4E9483` · **Cliente**

```lua
NetworkEarnFromCompleteCollection(amount)
```
```c
void _NETWORK_EARN_FROM_COMPLETE_COLLECTION(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromContraband

`_NETWORK_EARN_FROM_CONTRABAND` · hash `0xECA658CE2A4E5A72` · **Cliente**

```lua
NetworkEarnFromContraband(amount, p1)
```
```c
void _NETWORK_EARN_FROM_CONTRABAND(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xECA658CE2A4E5A72` (`N_0xeca658ce2a4e5a72`)

---
### NetworkEarnFromCrateDrop

`NETWORK_EARN_FROM_CRATE_DROP` · hash `0xB1CC1B9EC3007A2A` · jhash `0xEAF04923` · **Cliente**

```lua
NetworkEarnFromCrateDrop(amount)
```
```c
void NETWORK_EARN_FROM_CRATE_DROP(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB1CC1B9EC3007A2A` (`N_0xb1cc1b9ec3007a2a`)

---
### NetworkEarnFromCriminalMastermindBonus

`_NETWORK_EARN_FROM_CRIMINAL_MASTERMIND_BONUS` · hash `0xFA009A62990671D4` · **Cliente**

```lua
NetworkEarnFromCriminalMastermindBonus(p0, p1, p2)
```
```c
void _NETWORK_EARN_FROM_CRIMINAL_MASTERMIND_BONUS(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xD20D79671A598594` (`N_0xd20d79671a598594`)

---
### NetworkEarnFromDailyObjectiveEvent

`_NETWORK_EARN_FROM_DAILY_OBJECTIVE_EVENT` · hash `0x5128DF14A5BB86FC` · **Cliente**

```lua
NetworkEarnFromDailyObjectiveEvent(amount)
```
```c
void _NETWORK_EARN_FROM_DAILY_OBJECTIVE_EVENT(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromDailyObjectives

`NETWORK_EARN_FROM_DAILY_OBJECTIVES` · hash `0x6EA318C91C1A8786` · jhash `0xAB6BD72F` · **Cliente**

```lua
NetworkEarnFromDailyObjectives(p0, p1, p2)
```
```c
void NETWORK_EARN_FROM_DAILY_OBJECTIVES(int p0, char* p1, int p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`char*`)
- `p2` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6EA318C91C1A8786` (`N_0x6ea318c91c1a8786`), `_NETWORK_EARN_FROM_DAILY_OBJECTIVE` (`NetworkEarnFromDailyObjective`)

---
### NetworkEarnFromDarChallenge

`_NETWORK_EARN_FROM_DAR_CHALLENGE` · hash `0xCAC672087B4A24AB` · **Cliente**

```lua
NetworkEarnFromDarChallenge(amount, p1)
```
```c
void _NETWORK_EARN_FROM_DAR_CHALLENGE(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromDestroyingContraband

`_NETWORK_EARN_FROM_DESTROYING_CONTRABAND` · hash `0x84C0116D012E8FC2` · **Cliente**

```lua
NetworkEarnFromDestroyingContraband(p0)
```
```c
void _NETWORK_EARN_FROM_DESTROYING_CONTRABAND(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x84C0116D012E8FC2` (`N_0x84c0116d012e8fc2`)

---
### NetworkEarnFromDoomsdayFinaleBonus

`_NETWORK_EARN_FROM_DOOMSDAY_FINALE_BONUS` · hash `0x128A747F4A230952` · **Cliente**

```lua
NetworkEarnFromDoomsdayFinaleBonus(amount, vehicleHash)
```
```c
void _NETWORK_EARN_FROM_DOOMSDAY_FINALE_BONUS(int amount, Hash vehicleHash);
```

**Parámetros**

- `amount` (`int`)
- `vehicleHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromFmbbBossWork

`_NETWORK_EARN_FROM_FMBB_BOSS_WORK` · hash `0x1FDA0AA679C9919B` · **Cliente**

```lua
NetworkEarnFromFmbbBossWork(p0)
```
```c
void _NETWORK_EARN_FROM_FMBB_BOSS_WORK(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x1FDA0AA679C9919B` (`N_0x1fda0aa679c9919b`)

---
### NetworkEarnFromFmbbPhonecallMission

`_NETWORK_EARN_FROM_FMBB_PHONECALL_MISSION` · hash `0xC5156361F26E2212` · **Cliente**

```lua
NetworkEarnFromFmbbPhonecallMission(p0)
```
```c
void _NETWORK_EARN_FROM_FMBB_PHONECALL_MISSION(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0xC5156361F26E2212` (`N_0xc5156361f26e2212`)

---
### NetworkEarnFromGangPickup

`_NETWORK_EARN_FROM_GANG_PICKUP` · hash `0xA03D4ACE0A3284CE` · jhash `0x33C20BC4` · **Cliente**

```lua
NetworkEarnFromGangPickup(amount)
```
```c
void _NETWORK_EARN_FROM_GANG_PICKUP(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA03D4ACE0A3284CE` (`N_0xa03d4ace0a3284ce`)

---
### NetworkEarnFromGangopsAwards

`_NETWORK_EARN_FROM_GANGOPS_AWARDS` · hash `0xA9A31475F530DFDA` · **Cliente**

```lua
NetworkEarnFromGangopsAwards(amount, unk, p2)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_AWARDS(int amount, char* unk, Any p2);
```

**Parámetros**

- `amount` (`int`)
- `unk` (`char*`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromGangopsElite

`_NETWORK_EARN_FROM_GANGOPS_ELITE` · hash `0x2597A0D4A4FC2C77` · **Cliente**

```lua
NetworkEarnFromGangopsElite(amount, unk, actIndex)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_ELITE(int amount, char* unk, int actIndex);
```

**Parámetros**

- `amount` (`int`)
- `unk` (`char*`)
- `actIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromGangopsJobsFinale

`_NETWORK_EARN_FROM_GANGOPS_JOBS_FINALE` · hash `0x1C121FC9545E0D52` · **Cliente**

```lua
NetworkEarnFromGangopsJobsFinale(amount, unk)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_JOBS_FINALE(int amount, char* unk);
```

**Parámetros**

- `amount` (`int`)
- `unk` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromGangopsJobsPrepParticipation

`_NETWORK_EARN_FROM_GANGOPS_JOBS_PREP_PARTICIPATION` · hash `0xED26584F6BDCBBFD` · **Cliente**

```lua
NetworkEarnFromGangopsJobsPrepParticipation(amount)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_JOBS_PREP_PARTICIPATION(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromGangopsJobsSetup

`_NETWORK_EARN_FROM_GANGOPS_JOBS_SETUP` · hash `0xA9160796D47A2CF8` · **Cliente**

```lua
NetworkEarnFromGangopsJobsSetup(amount, unk)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_JOBS_SETUP(int amount, char* unk);
```

**Parámetros**

- `amount` (`int`)
- `unk` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromGangopsWages

`_NETWORK_EARN_FROM_GANGOPS_WAGES` · hash `0x2DCB19ABAB0380A8` · **Cliente**

```lua
NetworkEarnFromGangopsWages(amount, p1)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_WAGES(int amount, int p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromGangopsWagesBonus

`_NETWORK_EARN_FROM_GANGOPS_WAGES_BONUS` · hash `0x15BB2A5C757EB91F` · **Cliente**

```lua
NetworkEarnFromGangopsWagesBonus(amount, p1)
```
```c
void _NETWORK_EARN_FROM_GANGOPS_WAGES_BONUS(int amount, int p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromHackerTruckMission

`_NETWORK_EARN_FROM_HACKER_TRUCK_MISSION` · hash `0xE8815FE993896AD3` · **Cliente**

```lua
NetworkEarnFromHackerTruckMission(p0, amount, p2, p3)
```
```c
void _NETWORK_EARN_FROM_HACKER_TRUCK_MISSION(Any p0, int amount, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `amount` (`int`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### NetworkEarnFromHoldups

`NETWORK_EARN_FROM_HOLDUPS` · hash `0x45B8154E077D9E4D` · jhash `0xE6B90E9C` · **Cliente**

```lua
NetworkEarnFromHoldups(amount)
```
```c
void NETWORK_EARN_FROM_HOLDUPS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

---
### NetworkEarnFromImportExport

`NETWORK_EARN_FROM_IMPORT_EXPORT` · hash `0xF92A014A634442D6` · jhash `0xF11FC458` · **Cliente**

```lua
NetworkEarnFromImportExport(amount, modelHash)
```
```c
void NETWORK_EARN_FROM_IMPORT_EXPORT(int amount, Hash modelHash);
```

**Parámetros**

- `amount` (`int`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### NetworkEarnFromJob

`NETWORK_EARN_FROM_JOB` · hash `0xB2CC4836834E8A98` · jhash `0x0B6997FC` · **Cliente**

```lua
NetworkEarnFromJob(amount, p1)
```
```c
void NETWORK_EARN_FROM_JOB(int amount, char* p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`char*`)

**Devuelve:** `void`

---
### NetworkEarnFromJobBonus

`NETWORK_EARN_FROM_JOB_BONUS` · hash `0x6816FB4416760775` · jhash `0xBEE23713` · **Cliente**

```lua
local p1, p2 = NetworkEarnFromJobBonus(p0)
```
```c
void NETWORK_EARN_FROM_JOB_BONUS(Any p0, Any* p1, Any* p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x6816FB4416760775` (`N_0x6816fb4416760775`), `_NETWORK_EARN_FROM_JOB_BONUS` (`NetworkEarnFromJobBonus`)

---
### NetworkEarnFromJobX2

`_NETWORK_EARN_FROM_JOB_X2` · hash `0xDEBBF584665411D0` · **Cliente**

```lua
NetworkEarnFromJobX2(amount, p1)
```
```c
void _NETWORK_EARN_FROM_JOB_X2(int amount, char* p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromNotBadsport

`NETWORK_EARN_FROM_NOT_BADSPORT` · hash `0x4337511FA8221D36` · jhash `0xCC068380` · **Cliente**

```lua
NetworkEarnFromNotBadsport(amount)
```
```c
void NETWORK_EARN_FROM_NOT_BADSPORT(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4337511FA8221D36` (`N_0x4337511fa8221d36`)

---
### NetworkEarnFromPersonalVehicle

`NETWORK_EARN_FROM_PERSONAL_VEHICLE` · hash `0x3F4D00167E41E0AD` · jhash `0x96B8BEE8` · **Cliente**

```lua
NetworkEarnFromPersonalVehicle(p0, p1, p2, p3, p4, p5, p6, p7, p8)
```
```c
void NETWORK_EARN_FROM_PERSONAL_VEHICLE(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8);
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

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3F4D00167E41E0AD` (`N_0x3f4d00167e41e0ad`)

---
### NetworkEarnFromPickup

`NETWORK_EARN_FROM_PICKUP` · hash `0xED1517D3AF17C698` · jhash `0x70A0ED62` · **Cliente**

```lua
NetworkEarnFromPickup(amount)
```
```c
void NETWORK_EARN_FROM_PICKUP(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

---
### NetworkEarnFromPremiumJob

`_NETWORK_EARN_FROM_PREMIUM_JOB` · hash `0xC8407624CEF2354B` · **Cliente**

```lua
NetworkEarnFromPremiumJob(amount, p1)
```
```c
void _NETWORK_EARN_FROM_PREMIUM_JOB(int amount, char* p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC8407624CEF2354B` (`N_0xc8407624cef2354b`)

---
### NetworkEarnFromProperty

`NETWORK_EARN_FROM_PROPERTY` · hash `0x849648349D77F5C5` · jhash `0x9BE4F7E1` · **Cliente**

```lua
NetworkEarnFromProperty(amount, propertyName)
```
```c
void NETWORK_EARN_FROM_PROPERTY(int amount, Hash propertyName);
```

**Parámetros**

- `amount` (`int`)
- `propertyName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### NetworkEarnFromRcTimeTrial

`_NETWORK_EARN_FROM_RC_TIME_TRIAL` · hash `0xDFF49EE984E7AAE8` · **Cliente**

```lua
NetworkEarnFromRcTimeTrial(amount)
```
```c
void _NETWORK_EARN_FROM_RC_TIME_TRIAL(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromRdrBonus

`_NETWORK_EARN_FROM_RDR_BONUS` · hash `0x7A5349B773584675` · **Cliente**

```lua
NetworkEarnFromRdrBonus(amount, p1)
```
```c
void _NETWORK_EARN_FROM_RDR_BONUS(int amount, Any p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromRockstar

`NETWORK_EARN_FROM_ROCKSTAR` · hash `0x02CE1D6AC0FC73EA` · jhash `0x5A3733CC` · **Cliente**

```lua
NetworkEarnFromRockstar(amount)
```
```c
void NETWORK_EARN_FROM_ROCKSTAR(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

---
### NetworkEarnFromSellBase

`_NETWORK_EARN_FROM_SELL_BASE` · hash `0x0E1E2FF3F4EC11AA` · **Cliente**

```lua
NetworkEarnFromSellBase(amount, baseNameHash)
```
```c
void _NETWORK_EARN_FROM_SELL_BASE(int amount, Hash baseNameHash);
```

**Parámetros**

- `amount` (`int`)
- `baseNameHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromSellBunker

`_NETWORK_EARN_FROM_SELL_BUNKER` · hash `0x9251B6ABF2D0A5B4` · **Cliente**

```lua
NetworkEarnFromSellBunker(amount, bunkerHash)
```
```c
void _NETWORK_EARN_FROM_SELL_BUNKER(int amount, Hash bunkerHash);
```

**Parámetros**

- `amount` (`int`)
- `bunkerHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9251B6ABF2D0A5B4` (`N_0x9251b6abf2d0a5b4`)

---
### NetworkEarnFromSellingVehicle

`_NETWORK_EARN_FROM_SELLING_VEHICLE` · hash `0x8BCB27A057DF7B7F` · **Cliente**

```lua
NetworkEarnFromSellingVehicle(amount)
```
```c
void _NETWORK_EARN_FROM_SELLING_VEHICLE(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
NativeDB Added Parameter 3: Any p2
NativeDB Introduced: v1734
```

---
### NetworkEarnFromSightseeing

`_NETWORK_EARN_FROM_SIGHTSEEING` · hash `0x45087AE480B233AC` · **Cliente**

```lua
NetworkEarnFromSightseeing(p0, p1, p2, p3)
```
```c
void _NETWORK_EARN_FROM_SIGHTSEEING(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkEarnFromSmuggling

`_NETWORK_EARN_FROM_SMUGGLING` · hash `0xDEE612F2D71B0308` · **Cliente**

```lua
NetworkEarnFromSmuggling(amount, p1, p2, p3)
```
```c
void _NETWORK_EARN_FROM_SMUGGLING(int amount, Any p1, Any p2, Any p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkEarnFromSpinTheWheelCash

`_NETWORK_EARN_FROM_SPIN_THE_WHEEL_CASH` · hash `0x676C48776CACBB5A` · **Cliente**

```lua
NetworkEarnFromSpinTheWheelCash(amount)
```
```c
void _NETWORK_EARN_FROM_SPIN_THE_WHEEL_CASH(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkEarnFromTargetRefund

`_NETWORK_EARN_FROM_TARGET_REFUND` · hash `0x5B669CF2299A271F` · **Cliente**

```lua
NetworkEarnFromTargetRefund(amount, p1)
```
```c
void _NETWORK_EARN_FROM_TARGET_REFUND(int amount, int p1);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkEarnFromTimeTrialWin

`_NETWORK_EARN_FROM_TIME_TRIAL_WIN` · hash `0x0819DB99FD2FBBD8` · **Cliente**

```lua
NetworkEarnFromTimeTrialWin(amount)
```
```c
void _NETWORK_EARN_FROM_TIME_TRIAL_WIN(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkEarnFromTunerAward

`_NETWORK_EARN_FROM_TUNER_AWARD` · hash `0xB846F547D3792DF6` · **Cliente**

```lua
NetworkEarnFromTunerAward(p0, p1, p2)
```
```c
void _NETWORK_EARN_FROM_TUNER_AWARD(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xB846F547D3792DF6` (`N_0xb846f547d3792df6`)

---
### NetworkEarnFromTunerFinale

`_NETWORK_EARN_FROM_TUNER_FINALE` · hash `0xBCB266247193AC61` · **Cliente**

```lua
NetworkEarnFromTunerFinale(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_EARN_FROM_TUNER_FINALE(Any p0, Any p1, Any p2, Any p3, Any p4);
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
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xBCB266247193AC61` (`N_0xbcb266247193ac61`)

---
### NetworkEarnFromUpgradeAutoshopLocation

`_NETWORK_EARN_FROM_UPGRADE_AUTOSHOP_LOCATION` · hash `0xC10322A8D3E061EE` · **Cliente**

```lua
NetworkEarnFromUpgradeAutoshopLocation(p0, p1)
```
```c
void _NETWORK_EARN_FROM_UPGRADE_AUTOSHOP_LOCATION(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xC10322A8D3E061EE` (`N_0xc10322a8d3e061ee`)

---
### NetworkEarnFromVehicle

`NETWORK_EARN_FROM_VEHICLE` · hash `0xB539BD8A4C1EECF8` · jhash `0xF803589D` · **Cliente**

```lua
NetworkEarnFromVehicle(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
void NETWORK_EARN_FROM_VEHICLE(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7);
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

**Devuelve:** `void`

---
### NetworkEarnFromVehicleAutoshop

`_NETWORK_EARN_FROM_VEHICLE_AUTOSHOP` · hash `0x533073E8A596008C` · **Cliente**

```lua
NetworkEarnFromVehicleAutoshop(p0, p1)
```
```c
void _NETWORK_EARN_FROM_VEHICLE_AUTOSHOP(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x533073E8A596008C` (`N_0x533073e8a596008c`)

---
### NetworkEarnFromVehicleAutoshopBonus

`_NETWORK_EARN_FROM_VEHICLE_AUTOSHOP_BONUS` · hash `0xFE65AFE7308E32B2` · **Cliente**

```lua
NetworkEarnFromVehicleAutoshopBonus(p0)
```
```c
void _NETWORK_EARN_FROM_VEHICLE_AUTOSHOP_BONUS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xFE65AFE7308E32B2` (`N_0xfe65afe7308e32b2`)

---
### NetworkEarnFromVehicleExport

`_NETWORK_EARN_FROM_VEHICLE_EXPORT` · hash `0xEDEAD9A91EC768B3` · **Cliente**

```lua
NetworkEarnFromVehicleExport(amount, p1, p2)
```
```c
void _NETWORK_EARN_FROM_VEHICLE_EXPORT(int amount, Any p1, Any p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEDEAD9A91EC768B3` (`N_0xedead9a91ec768b3`)

---
### NetworkEarnFromWagePayment

`_NETWORK_EARN_FROM_WAGE_PAYMENT` · hash `0x35F8DA0E8A31EF1B` · **Cliente**

```lua
NetworkEarnFromWagePayment(amount)
```
```c
void _NETWORK_EARN_FROM_WAGE_PAYMENT(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkEarnFromWagePaymentBonus

`_NETWORK_EARN_FROM_WAGE_PAYMENT_BONUS` · hash `0x005ACA7100BD101D` · **Cliente**

```lua
NetworkEarnFromWagePaymentBonus(amount)
```
```c
void _NETWORK_EARN_FROM_WAGE_PAYMENT_BONUS(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkEarnFromWarehouse

`_NETWORK_EARN_FROM_WAREHOUSE` · hash `0x3E4ADAFF1830F146` · **Cliente**

```lua
NetworkEarnFromWarehouse()
```
```c
void _NETWORK_EARN_FROM_WAREHOUSE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int amount
NativeDB Added Parameter 2: int id
```

**Nombres antiguos (alias):** `0x3E4ADAFF1830F146` (`N_0x3e4adaff1830f146`)

---
### NetworkEarnGoon

`_NETWORK_EARN_GOON` · hash `0xCDA1C62BE2777802` · **Cliente**

```lua
NetworkEarnGoon(p0, p1, p2)
```
```c
void _NETWORK_EARN_GOON(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCDA1C62BE2777802` (`N_0xcda1c62be2777802`)

---
### NetworkEarnIslandHeist

`_NETWORK_EARN_ISLAND_HEIST` · hash `0xD21D111C46BA9F15` · **Cliente**

```lua
NetworkEarnIslandHeist(p0, p1, p2, p3, p4, p5)
```
```c
void _NETWORK_EARN_ISLAND_HEIST(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
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
NativeDB Introduced: v2189
```

---
### NetworkEarnJobBonusFirstTimeBonus

`_NETWORK_EARN_JOB_BONUS_FIRST_TIME_BONUS` · hash `0x11B0A20C493F7E36` · **Cliente**

```lua
NetworkEarnJobBonusFirstTimeBonus(p0, p1, p2)
```
```c
void _NETWORK_EARN_JOB_BONUS_FIRST_TIME_BONUS(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x11B0A20C493F7E36` (`N_0x11b0a20c493f7e36`)

---
### NetworkEarnJobBonusHeistAward

`_NETWORK_EARN_JOB_BONUS_HEIST_AWARD` · hash `0x9D4FDBB035229669` · **Cliente**

```lua
NetworkEarnJobBonusHeistAward(p0, p1, p2)
```
```c
void _NETWORK_EARN_JOB_BONUS_HEIST_AWARD(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x9D4FDBB035229669` (`N_0x9d4fdbb035229669`)

---
### NetworkGetEvcBalance

`NETWORK_GET_EVC_BALANCE` · hash `0x5D1E75F91C07DEE5` · jhash `0xF1EDB7F4` · **Cliente**

```lua
local retval = NetworkGetEvcBalance()
```
```c
int NETWORK_GET_EVC_BALANCE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkGetIsHighEarner

`_NETWORK_GET_IS_HIGH_EARNER` · hash `0xFB2456B2040A6A67` · jhash `0x63F093A6` · **Cliente**

```lua
local retval = NetworkGetIsHighEarner()
```
```c
BOOL _NETWORK_GET_IS_HIGH_EARNER();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkGetPvcBalance

`NETWORK_GET_PVC_BALANCE` · hash `0x4F54F3B6C202FB4E` · jhash `0x56485B56` · **Cliente**

```lua
local retval = NetworkGetPvcBalance()
```
```c
int NETWORK_GET_PVC_BALANCE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkGetPvcTransferBalance

`NETWORK_GET_PVC_TRANSFER_BALANCE` · hash `0x13A8DE2FD77D04F3` · jhash `0xC670C814` · **Cliente**

```lua
local retval = NetworkGetPvcTransferBalance()
```
```c
int NETWORK_GET_PVC_TRANSFER_BALANCE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Same as 0xEA560AC9EEB1E19B.
```

```
Same as 0xEA560AC9EEB1E19B.

NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_NETWORK_GET_REMAINING_VC_DAILY_TRANSFERS` (`NetworkGetRemainingVcDailyTransfers`)

---
### NetworkGetRemainingTransferBalance

`NETWORK_GET_REMAINING_TRANSFER_BALANCE` · hash `0xEA560AC9EEB1E19B` · jhash `0xA9021211` · **Cliente**

```lua
local retval = NetworkGetRemainingTransferBalance()
```
```c
int NETWORK_GET_REMAINING_TRANSFER_BALANCE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Same as 0x13A8DE2FD77D04F3.

NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_NETWORK_GET_REMAINING_VC_DAILY_TRANSFERS_2` (`NetworkGetRemainingVcDailyTransfers_2`)

---
### NetworkGetStringBankBalance

`NETWORK_GET_STRING_BANK_BALANCE` · hash `0xA6FA3979BED01B81` · jhash `0xAA7EA3BD` · **Cliente**

```lua
local retval = NetworkGetStringBankBalance()
```
```c
char* NETWORK_GET_STRING_BANK_BALANCE();
```

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xA6FA3979BED01B81` (`N_0xa6fa3979bed01b81`), `_NETWORK_GET_BANK_BALANCE_STRING` (`NetworkGetBankBalanceString`)

---
### NetworkGetStringBankWalletBalance

`NETWORK_GET_STRING_BANK_WALLET_BALANCE` · hash `0x700AF71AE615E6DD` · jhash `0x7D4FD28C` · **Cliente**

```lua
local retval = NetworkGetStringBankWalletBalance()
```
```c
char* NETWORK_GET_STRING_BANK_WALLET_BALANCE();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkGetStringWalletBalance

`NETWORK_GET_STRING_WALLET_BALANCE` · hash `0xF9B10B529DCFB33B` · jhash `0xC1A11435` · **Cliente**

```lua
local retval = NetworkGetStringWalletBalance(characterSlot)
```
```c
char* NETWORK_GET_STRING_WALLET_BALANCE(int characterSlot);
```

**Parámetros**

- `characterSlot` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkGetVcBalance

`NETWORK_GET_VC_BALANCE` · hash `0x5CBAD97E059E1B94` · jhash `0xADF8F882` · **Cliente**

```lua
local retval = NetworkGetVcBalance()
```
```c
int NETWORK_GET_VC_BALANCE();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x5CBAD97E059E1B94` (`N_0x5cbad97e059e1b94`)

---
### NetworkGetVcBankBalance

`NETWORK_GET_VC_BANK_BALANCE` · hash `0x76EF28DA05EA395A` · jhash `0x16184FB5` · **Cliente**

```lua
local retval = NetworkGetVcBankBalance()
```
```c
int NETWORK_GET_VC_BANK_BALANCE();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x76EF28DA05EA395A` (`N_0x76ef28da05ea395a`)

---
### NetworkGetVcBankBalanceIsNotLessThan

`_NETWORK_GET_VC_BANK_BALANCE_IS_NOT_LESS_THAN` · hash `0xA31FD6A0865B6D14` · jhash `0xABED6020` · **Cliente**

```lua
local retval = NetworkGetVcBankBalanceIsNotLessThan(amount)
```
```c
BOOL _NETWORK_GET_VC_BANK_BALANCE_IS_NOT_LESS_THAN(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if bank balance >= amount.

NativeDB Introduced: v323
```

---
### NetworkGetVcBankWalletBalanceIsNotLessThan

`_NETWORK_GET_VC_BANK_WALLET_BALANCE_IS_NOT_LESS_THAN` · hash `0xDC18531D7019A535` · jhash `0xCA23FD25` · **Cliente**

```lua
local retval = NetworkGetVcBankWalletBalanceIsNotLessThan(amount, characterSlot)
```
```c
BOOL _NETWORK_GET_VC_BANK_WALLET_BALANCE_IS_NOT_LESS_THAN(int amount, int characterSlot);
```

**Parámetros**

- `amount` (`int`)
- `characterSlot` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if bank balance + wallet balance >= amount.
```

**Nombres antiguos (alias):** `0xDC18531D7019A535` (`N_0xdc18531d7019a535`)

---
### NetworkGetVcWalletBalance

`NETWORK_GET_VC_WALLET_BALANCE` · hash `0xA40F9C2623F6A8B5` · jhash `0x4F5B781C` · **Cliente**

```lua
local retval = NetworkGetVcWalletBalance(characterSlot)
```
```c
int NETWORK_GET_VC_WALLET_BALANCE(int characterSlot);
```

**Parámetros**

- `characterSlot` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xA40F9C2623F6A8B5` (`N_0xa40f9c2623f6a8b5`)

---
### NetworkGetVcWalletBalanceIsNotLessThan

`_NETWORK_GET_VC_WALLET_BALANCE_IS_NOT_LESS_THAN` · hash `0xED5AB8860415BABA` · jhash `0x0EA2188C` · **Cliente**

```lua
local retval = NetworkGetVcWalletBalanceIsNotLessThan(amount, characterSlot)
```
```c
BOOL _NETWORK_GET_VC_WALLET_BALANCE_IS_NOT_LESS_THAN(int amount, int characterSlot);
```

**Parámetros**

- `amount` (`int`)
- `characterSlot` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if wallet balance >= amount.

NativeDB Introduced: v323
```

---
### NetworkGivePlayerJobshareCash

`NETWORK_GIVE_PLAYER_JOBSHARE_CASH` · hash `0xFB18DF9CB95E0105` · jhash `0xC6047FDB` · **Cliente**

```lua
local networkHandle = NetworkGivePlayerJobshareCash(amount, networkHandle)
```
```c
void NETWORK_GIVE_PLAYER_JOBSHARE_CASH(int amount, int* networkHandle);
```

**Parámetros**

- `amount` (`int`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### NetworkInitializeCash

`NETWORK_INITIALIZE_CASH` · hash `0x3DA5ECD1A56CBA6D` · jhash `0x66DA9935` · **Cliente**

```lua
NetworkInitializeCash(wallet, bank)
```
```c
void NETWORK_INITIALIZE_CASH(int wallet, int bank);
```

**Parámetros**

- `wallet` (`int`)
- `bank` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3DA5ECD1A56CBA6D` (`N_0x3da5ecd1a56cba6d`)

---
### NetworkManualDeleteCharacter

`_NETWORK_MANUAL_DELETE_CHARACTER` · hash `0x821418C727FCACD7` · **Cliente**

```lua
NetworkManualDeleteCharacter(characterSlot)
```
```c
void _NETWORK_MANUAL_DELETE_CHARACTER(int characterSlot);
```

**Parámetros**

- `characterSlot` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x821418C727FCACD7` (`N_0x821418c727fcacd7`)

---
### NetworkMoneyCanBet

`NETWORK_MONEY_CAN_BET` · hash `0x81404F3DC124FE5B` · jhash `0x8474E6F0` · **Cliente**

```lua
local retval = NetworkMoneyCanBet(amount, p1, p2)
```
```c
BOOL NETWORK_MONEY_CAN_BET(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x81404F3DC124FE5B` (`N_0x81404f3dc124fe5b`)

---
### NetworkPayEmployeeWage

`NETWORK_PAY_EMPLOYEE_WAGE` · hash `0x5FD5ED82CBBE9989` · jhash `0xBE70849B` · **Cliente**

```lua
NetworkPayEmployeeWage(p0, p1, p2)
```
```c
void NETWORK_PAY_EMPLOYEE_WAGE(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5FD5ED82CBBE9989` (`N_0x5fd5ed82cbbe9989`)

---
### NetworkPayMatchEntryFee

`NETWORK_PAY_MATCH_ENTRY_FEE` · hash `0x9346E14F2AF74D46` · jhash `0x224A3488` · **Cliente**

```lua
NetworkPayMatchEntryFee(amount, matchId, p2, p3)
```
```c
void NETWORK_PAY_MATCH_ENTRY_FEE(int amount, char* matchId, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `matchId` (`char*`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9346E14F2AF74D46` (`N_0x9346e14f2af74d46`)

---
### NetworkPayUtilityBill

`NETWORK_PAY_UTILITY_BILL` · hash `0xAFE08B35EC0C9EAE` · jhash `0x451A2644` · **Cliente**

```lua
NetworkPayUtilityBill(amount, p1, p2)
```
```c
void NETWORK_PAY_UTILITY_BILL(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAFE08B35EC0C9EAE` (`N_0xafe08b35ec0c9eae`)

---
### NetworkReceivePlayerJobshareCash

`NETWORK_RECEIVE_PLAYER_JOBSHARE_CASH` · hash `0x56A3B51944C50598` · jhash `0x4ED71C1A` · **Cliente**

```lua
local networkHandle = NetworkReceivePlayerJobshareCash(value, networkHandle)
```
```c
void NETWORK_RECEIVE_PLAYER_JOBSHARE_CASH(int value, int* networkHandle);
```

**Parámetros**

- `value` (`int`)
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### NetworkRefundCash

`NETWORK_REFUND_CASH` · hash `0xF9C812CD7C46E817` · jhash `0x07C92F21` · **Cliente**

```lua
NetworkRefundCash(index, context, reason, unk)
```
```c
void NETWORK_REFUND_CASH(int index, char* context, char* reason, BOOL unk);
```

**Parámetros**

- `index` (`int`)
- `context` (`char*`)
- `reason` (`char*`)
- `unk` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
index  
-------  
See function sub_1005 in am_boat_taxi.ysc  
context  
----------  
"BACKUP_VAGOS"  
"BACKUP_LOST"  
"BACKUP_FAMILIES"  
"HIRE_MUGGER"  
"HIRE_MERCENARY"  
"BUY_CARDROPOFF"  
"HELI_PICKUP"  
"BOAT_PICKUP"  
"CLEAR_WANTED"  
"HEAD_2_HEAD"  
"CHALLENGE"  
"SHARE_LAST_JOB"  
"DEFAULT"  
reason  
---------  
"NOTREACHTARGET"  
"TARGET_ESCAPE"  
"DELIVERY_FAIL"  
"NOT_USED"  
"TEAM_QUIT"  
"SERVER_ERROR"  
"RECEIVE_LJ_L"  
"CHALLENGE_PLAYER_LEFT"  
"DEFAULT"  
unk  
-----  
Unknown bool value  
```

**Nombres antiguos (alias):** `0xF9C812CD7C46E817` (`N_0xf9c812cd7c46e817`)

---
### NetworkRivalDeliveryCompleted

`_NETWORK_RIVAL_DELIVERY_COMPLETED` · hash `0x1B882107C23A9022` · **Cliente**

```lua
NetworkRivalDeliveryCompleted(earnedMoney)
```
```c
void _NETWORK_RIVAL_DELIVERY_COMPLETED(int earnedMoney);
```

**Parámetros**

- `earnedMoney` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentAmmoDrop

`NETWORK_SPENT_AMMO_DROP` · hash `0xB162DC95C0A3317B` · jhash `0x4B643076` · **Cliente**

```lua
NetworkSpentAmmoDrop(p0, p1, p2)
```
```c
void NETWORK_SPENT_AMMO_DROP(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentArcadeGame

`_NETWORK_SPENT_ARCADE_GAME` · hash `0xEAD3D81F2C3A1458` · **Cliente**

```lua
NetworkSpentArcadeGame(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_ARCADE_GAME(Any p0, Any p1, Any p2, Any p3, Any p4);
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
### NetworkSpentArcadeGeneric

`_NETWORK_SPENT_ARCADE_GENERIC` · hash `0x43AA7FAC4E6D6687` · **Cliente**

```lua
NetworkSpentArcadeGeneric(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_ARCADE_GENERIC(Any p0, Any p1, Any p2, Any p3, Any p4);
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
### NetworkSpentArenaJoinSpectator

`_NETWORK_SPENT_ARENA_JOIN_SPECTATOR` · hash `0x14EAEA58F93B55AF` · **Cliente**

```lua
NetworkSpentArenaJoinSpectator(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_ARENA_JOIN_SPECTATOR(int amount, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkSpentArenaPremium

`_NETWORK_SPENT_ARENA_PREMIUM` · hash `0x619496D837EFD920` · **Cliente**

```lua
NetworkSpentArenaPremium(amount, p1, p2)
```
```c
void _NETWORK_SPENT_ARENA_PREMIUM(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkSpentArenaSpectatorBox

`_NETWORK_SPENT_ARENA_SPECTATOR_BOX` · hash `0x7049BF858601DC0F` · **Cliente**

```lua
NetworkSpentArenaSpectatorBox(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_ARENA_SPECTATOR_BOX(int amount, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkSpentArrestBail

`NETWORK_SPENT_ARREST_BAIL` · hash `0x812F5488B1B2A299` · jhash `0x5AEE2FC1` · **Cliente**

```lua
NetworkSpentArrestBail(p0, p1, p2)
```
```c
void NETWORK_SPENT_ARREST_BAIL(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentAutoshopModifications

`_NETWORK_SPENT_AUTOSHOP_MODIFICATIONS` · hash `0x9BEA350D7C48061B` · **Cliente**

```lua
NetworkSpentAutoshopModifications(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_AUTOSHOP_MODIFICATIONS(Any p0, Any p1, Any p2, Any p3, Any p4);
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
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x9BEA350D7C48061B` (`N_0x9bea350d7c48061b`)

---
### NetworkSpentAutoshopPropertyUtilityFee

`_NETWORK_SPENT_AUTOSHOP_PROPERTY_UTILITY_FEE` · hash `0xB40F96D6D252839B` · **Cliente**

```lua
NetworkSpentAutoshopPropertyUtilityFee(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_AUTOSHOP_PROPERTY_UTILITY_FEE(Any p0, Any p1, Any p2, Any p3);
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

**Nombres antiguos (alias):** `0xB40F96D6D252839B` (`N_0xb40f96d6d252839b`)

---
### NetworkSpentBaService

`_NETWORK_SPENT_BA_SERVICE` · hash `0xD7CCCBA28C4ECAF0` · **Cliente**

```lua
NetworkSpentBaService(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_BA_SERVICE(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD7CCCBA28C4ECAF0` (`N_0xd7cccba28c4ecaf0`)

---
### NetworkSpentBallisticEquipment

`_NETWORK_SPENT_BALLISTIC_EQUIPMENT` · hash `0x5D97630A8A0EF123` · **Cliente**

```lua
NetworkSpentBallisticEquipment(amount, p1, p2)
```
```c
void _NETWORK_SPENT_BALLISTIC_EQUIPMENT(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5D97630A8A0EF123` (`N_0x5d97630a8a0ef123`)

---
### NetworkSpentBankInterest

`NETWORK_SPENT_BANK_INTEREST` · hash `0xCA230C9682556CF1` · jhash `0xF02E92D7` · **Cliente**

```lua
NetworkSpentBankInterest(p0, p1, p2)
```
```c
void NETWORK_SPENT_BANK_INTEREST(int p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkSpentBeachPartyGeneric

`_NETWORK_SPENT_BEACH_PARTY_GENERIC` · hash `0x54ABA22FA6371249` · **Cliente**

```lua
NetworkSpentBeachPartyGeneric(p0)
```
```c
void _NETWORK_SPENT_BEACH_PARTY_GENERIC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### NetworkSpentBetting

`NETWORK_SPENT_BETTING` · hash `0x1C436FD11FFA692F` · jhash `0xF8A07513` · **Cliente**

```lua
NetworkSpentBetting(amount, p1, matchId, p3, p4)
```
```c
void NETWORK_SPENT_BETTING(int amount, int p1, char* matchId, BOOL p3, BOOL p4);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`int`)
- `matchId` (`char*`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBikeShopModify

`_NETWORK_SPENT_BIKE_SHOP_MODIFY` · hash `0x923AEA8E78F8DF0B` · **Cliente**

```lua
NetworkSpentBikeShopModify(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BIKE_SHOP_MODIFY(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkSpentBoatPickup

`NETWORK_SPENT_BOAT_PICKUP` · hash `0x524EE43A37232C00` · jhash `0xB241CABD` · **Cliente**

```lua
NetworkSpentBoatPickup(p0, p1, p2)
```
```c
void NETWORK_SPENT_BOAT_PICKUP(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBoss

`_NETWORK_SPENT_BOSS` · hash `0xFFBE02CD385356BD` · **Cliente**

```lua
local retval = NetworkSpentBoss()
```
```c
BOOL _NETWORK_SPENT_BOSS();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int amount
NativeDB Added Parameter 2: BOOL p1
NativeDB Added Parameter 3: BOOL p2
```

**Nombres antiguos (alias):** `0xFFBE02CD385356BD` (`N_0xffbe02cd385356bd`)

---
### NetworkSpentBounty

`NETWORK_SPENT_BOUNTY` · hash `0x29B260B84947DFCC` · jhash `0x3401FC96` · **Cliente**

```lua
NetworkSpentBounty(p0, p1, p2)
```
```c
void NETWORK_SPENT_BOUNTY(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBountyHunterMission

`_NETWORK_SPENT_BOUNTY_HUNTER_MISSION` · hash `0x1BEA0CD93470BB1F` · **Cliente**

```lua
NetworkSpentBountyHunterMission(amount, p1, p2)
```
```c
void _NETWORK_SPENT_BOUNTY_HUNTER_MISSION(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### NetworkSpentBullShark

`NETWORK_SPENT_BULL_SHARK` · hash `0xA6DD8458CE24012C` · jhash `0xDE7D398C` · **Cliente**

```lua
NetworkSpentBullShark(p0, p1, p2)
```
```c
void NETWORK_SPENT_BULL_SHARK(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBusiness

`_NETWORK_SPENT_BUSINESS` · hash `0x0035BB914316F1E3` · **Cliente**

```lua
NetworkSpentBusiness(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUSINESS(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0035BB914316F1E3` (`N_0x0035bb914316f1e3`)

---
### NetworkSpentBuyArena

`_NETWORK_SPENT_BUY_ARENA` · hash `0x40D5DA9550B7CB46` · **Cliente**

```lua
NetworkSpentBuyArena(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUY_ARENA(int amount, BOOL p1, BOOL p2, char* p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkSpentBuyAutoshop

`_NETWORK_SPENT_BUY_AUTOSHOP` · hash `0xEEB7E5D1FEB20869` · **Cliente**

```lua
NetworkSpentBuyAutoshop(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUY_AUTOSHOP(Any p0, Any p1, Any p2, Any p3);
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

**Nombres antiguos (alias):** `0xEEB7E5D1FEB20869` (`N_0xeeb7e5d1feb20869`)

---
### NetworkSpentBuyBase

`_NETWORK_SPENT_BUY_BASE` · hash `0x4EA3F425C7744D21` · **Cliente**

```lua
NetworkSpentBuyBase(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUY_BASE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentBuyBunker

`_NETWORK_SPENT_BUY_BUNKER` · hash `0x12D148D26538D0F9` · **Cliente**

```lua
NetworkSpentBuyBunker(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUY_BUNKER(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x12D148D26538D0F9` (`N_0x12d148d26538d0f9`)

---
### NetworkSpentBuyCasino

`_NETWORK_SPENT_BUY_CASINO` · hash `0x34A6FC4D06C4DA0F` · **Cliente**

```lua
local data = NetworkSpentBuyCasino(amount, p1, p2, data)
```
```c
void _NETWORK_SPENT_BUY_CASINO(int amount, BOOL p1, BOOL p2, Any* data);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkSpentBuyOfftheradar

`NETWORK_SPENT_BUY_OFFTHERADAR` · hash `0xA628A745E2275C5D` · jhash `0x20DDCF2F` · **Cliente**

```lua
NetworkSpentBuyOfftheradar(p0, p1, p2)
```
```c
void NETWORK_SPENT_BUY_OFFTHERADAR(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBuyPassiveMode

`NETWORK_SPENT_BUY_PASSIVE_MODE` · hash `0x6D3A430D1A809179` · jhash `0x7E97C92C` · **Cliente**

```lua
NetworkSpentBuyPassiveMode(p0, p1, p2)
```
```c
void NETWORK_SPENT_BUY_PASSIVE_MODE(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBuyRevealPlayers

`NETWORK_SPENT_BUY_REVEAL_PLAYERS` · hash `0x6E176F1B18BC0637` · jhash `0x2F7836E2` · **Cliente**

```lua
NetworkSpentBuyRevealPlayers(p0, p1, p2)
```
```c
void NETWORK_SPENT_BUY_REVEAL_PLAYERS(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentBuyTiltrotor

`_NETWORK_SPENT_BUY_TILTROTOR` · hash `0x0CCE73BC7A11E885` · **Cliente**

```lua
NetworkSpentBuyTiltrotor(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUY_TILTROTOR(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentBuyTruck

`_NETWORK_SPENT_BUY_TRUCK` · hash `0xAC272C0AE01B4BD8` · **Cliente**

```lua
NetworkSpentBuyTruck(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_BUY_TRUCK(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAC272C0AE01B4BD8` (`N_0xac272c0ae01b4bd8`)

---
### NetworkSpentBuyWantedlevel

`NETWORK_SPENT_BUY_WANTEDLEVEL` · hash `0xE1B13771A843C4F6` · jhash `0xE7CB4F95` · **Cliente**

```lua
local p1 = NetworkSpentBuyWantedlevel(p0, p2, p3)
```
```c
void NETWORK_SPENT_BUY_WANTEDLEVEL(Any p0, Any* p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentCallPlayer

`NETWORK_SPENT_CALL_PLAYER` · hash `0xACDE7185B374177C` · jhash `0x1A89B5FC` · **Cliente**

```lua
local p1 = NetworkSpentCallPlayer(p0, p2, p3)
```
```c
void NETWORK_SPENT_CALL_PLAYER(Any p0, Any* p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentCarclub

`_NETWORK_SPENT_CARCLUB` · hash `0x925227803A0EAA1B` · **Cliente**

```lua
NetworkSpentCarclub(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_CARCLUB(Any p0, BOOL p1, BOOL p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x925227803A0EAA1B` (`N_0x925227803a0eaa1b`)

---
### NetworkSpentCarclubMembership

`_NETWORK_SPENT_CARCLUB_MEMBERSHIP` · hash `0x1464E17207CD36E2` · **Cliente**

```lua
NetworkSpentCarclubMembership(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_CARCLUB_MEMBERSHIP(Any p0, Any p1, Any p2, Any p3, Any p4);
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
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x1464E17207CD36E2` (`N_0x1464e17207cd36e2`)

---
### NetworkSpentCarclubTakeover

`_NETWORK_SPENT_CARCLUB_TAKEOVER` · hash `0xD1E46824E6FB92B5` · **Cliente**

```lua
NetworkSpentCarclubTakeover(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_CARCLUB_TAKEOVER(Any p0, Any p1, Any p2, Any p3);
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

**Nombres antiguos (alias):** `0xD1E46824E6FB92B5` (`N_0xd1e46824e6fb92b5`)

---
### NetworkSpentCargoSourcing

`_NETWORK_SPENT_CARGO_SOURCING` · hash `0x948705F6F9C50824` · **Cliente**

```lua
NetworkSpentCargoSourcing(p0, p1, p2, p3, p4, p5)
```
```c
void _NETWORK_SPENT_CARGO_SOURCING(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
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
NativeDB Introduced: v2699
```

---
### NetworkSpentCarwash

`NETWORK_SPENT_CARWASH` · hash `0xEC03C719DB2F4306` · jhash `0x8283E028` · **Cliente**

```lua
NetworkSpentCarwash(p0, p1, p2, p3, p4)
```
```c
void NETWORK_SPENT_CARWASH(Any p0, Any p1, Any p2, BOOL p3, BOOL p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentCashDrop

`NETWORK_SPENT_CASH_DROP` · hash `0x289016EC778D60E0` · jhash `0x87BD1D11` · **Cliente**

```lua
NetworkSpentCashDrop(amount, p1, p2)
```
```c
void NETWORK_SPENT_CASH_DROP(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentCasinoClubGeneric

`_NETWORK_SPENT_CASINO_CLUB_GENERIC` · hash `0xC991C255AA6D90B2` · **Cliente**

```lua
NetworkSpentCasinoClubGeneric(p0, p1, p2, p3, p4, p5, p6, p7, p8)
```
```c
void _NETWORK_SPENT_CASINO_CLUB_GENERIC(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8);
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

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### NetworkSpentCasinoGeneric

`_NETWORK_SPENT_CASINO_GENERIC` · hash `0x88BF9B612B84D3C3` · **Cliente**

```lua
NetworkSpentCasinoGeneric(amount, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_CASINO_GENERIC(int amount, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkSpentCasinoHeist

`_NETWORK_SPENT_CASINO_HEIST` · hash `0xD30E8392F407C328` · **Cliente**

```lua
NetworkSpentCasinoHeist(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
```
```c
void _NETWORK_SPENT_CASINO_HEIST(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9, Any p10);
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
- `p10` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### NetworkSpentCasinoHeistSkipMission

`_NETWORK_SPENT_CASINO_HEIST_SKIP_MISSION` · hash `0x487009DD91D93429` · **Cliente**

```lua
NetworkSpentCasinoHeistSkipMission(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_CASINO_HEIST_SKIP_MISSION(Any p0, Any p1, Any p2, Any p3);
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
### NetworkSpentCasinoMembership

`_NETWORK_SPENT_CASINO_MEMBERSHIP` · hash `0xFBBE0570EDF39D46` · **Cliente**

```lua
NetworkSpentCasinoMembership(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_CASINO_MEMBERSHIP(int amount, BOOL p1, BOOL p2, int p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkSpentCinema

`NETWORK_SPENT_CINEMA` · hash `0x6B38ECB05A63A685` · jhash `0x1100CAF5` · **Cliente**

```lua
NetworkSpentCinema(p0, p1, p2, p3)
```
```c
void NETWORK_SPENT_CINEMA(Any p0, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentEmployAssassins

`_NETWORK_SPENT_EMPLOY_ASSASSINS` · hash `0x5BBBD92186E1F1C5` · **Cliente**

```lua
NetworkSpentEmployAssassins(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_EMPLOY_ASSASSINS(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentFromBank

`_NETWORK_SPENT_FROM_BANK` · hash `0xB9F7A469460E7A4A` · **Cliente**

```lua
NetworkSpentFromBank(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_FROM_BANK(Any p0, Any p1, Any p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xB9F7A469460E7A4A` (`N_0xb9f7a469460e7a4a`)

---
### NetworkSpentFromRockstar

`NETWORK_SPENT_FROM_ROCKSTAR` · hash `0x6A445B64ED7ABEB5` · jhash `0x54198922` · **Cliente**

```lua
NetworkSpentFromRockstar(bank, p1, p2)
```
```c
void NETWORK_SPENT_FROM_ROCKSTAR(int bank, BOOL p1, BOOL p2);
```

**Parámetros**

- `bank` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6A445B64ED7ABEB5` (`N_0x6a445b64ed7abeb5`)

---
### NetworkSpentGangopsCannon

`_NETWORK_SPENT_GANGOPS_CANNON` · hash `0x771ADB0E7635B7BF` · **Cliente**

```lua
NetworkSpentGangopsCannon(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_GANGOPS_CANNON(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentGangopsStartMission

`_NETWORK_SPENT_GANGOPS_START_MISSION` · hash `0xDA947AE8880D5C18` · **Cliente**

```lua
NetworkSpentGangopsStartMission(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_GANGOPS_START_MISSION(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentGangopsStartStrand

`_NETWORK_SPENT_GANGOPS_START_STRAND` · hash `0xA19EC0786E326E06` · **Cliente**

```lua
NetworkSpentGangopsStartStrand(type, amount, p2, p3)
```
```c
void _NETWORK_SPENT_GANGOPS_START_STRAND(int type, int amount, BOOL p2, BOOL p3);
```

**Parámetros**

- `type` (`int`)
- `amount` (`int`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentGangopsTripSkip

`_NETWORK_SPENT_GANGOPS_TRIP_SKIP` · hash `0x5ECE6FD7B4EC8D6A` · **Cliente**

```lua
NetworkSpentGangopsTripSkip(amount, p1, p2)
```
```c
void _NETWORK_SPENT_GANGOPS_TRIP_SKIP(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentGunrunningContactService

`_NETWORK_SPENT_GUNRUNNING_CONTACT_SERVICE` · hash `0x2CEB0E0BC2A77C05` · **Cliente**

```lua
NetworkSpentGunrunningContactService(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_GUNRUNNING_CONTACT_SERVICE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkSpentHangarStaffCharges

`_NETWORK_SPENT_HANGAR_STAFF_CHARGES` · hash `0xB1F1346FD57685D7` · **Cliente**

```lua
NetworkSpentHangarStaffCharges(amount, p1, p2)
```
```c
void _NETWORK_SPENT_HANGAR_STAFF_CHARGES(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkSpentHangarUtilityCharges

`_NETWORK_SPENT_HANGAR_UTILITY_CHARGES` · hash `0xB18AC2ECBB15CB6A` · **Cliente**

```lua
NetworkSpentHangarUtilityCharges(amount, p1, p2)
```
```c
void _NETWORK_SPENT_HANGAR_UTILITY_CHARGES(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkSpentHeliPickup

`NETWORK_SPENT_HELI_PICKUP` · hash `0x7BF1D73DB2ECA492` · jhash `0x27EEBCAB` · **Cliente**

```lua
NetworkSpentHeliPickup(p0, p1, p2)
```
```c
void NETWORK_SPENT_HELI_PICKUP(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentHireMercenary

`NETWORK_SPENT_HIRE_MERCENARY` · hash `0xE7B80E2BF9D80BD6` · jhash `0x99CF02C4` · **Cliente**

```lua
NetworkSpentHireMercenary(p0, p1, p2)
```
```c
void NETWORK_SPENT_HIRE_MERCENARY(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentHireMugger

`NETWORK_SPENT_HIRE_MUGGER` · hash `0xE404BFB981665BF0` · jhash `0xE792C4A5` · **Cliente**

```lua
NetworkSpentHireMugger(p0, p1, p2)
```
```c
void NETWORK_SPENT_HIRE_MUGGER(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only used once in a script (am_contact_requests)  
p1 = 0  
p2 = 1  
```

---
### NetworkSpentHoldups

`NETWORK_SPENT_HOLDUPS` · hash `0xD9B86B9872039763` · jhash `0x1B3803B1` · **Cliente**

```lua
NetworkSpentHoldups(p0, p1, p2)
```
```c
void NETWORK_SPENT_HOLDUPS(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentImAbility

`_NETWORK_SPENT_IM_ABILITY` · hash `0x93AA4165CB67E925` · **Cliente**

```lua
NetworkSpentImAbility(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_IM_ABILITY(Any p0, Any p1, Any p2, Any p3);
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

**Nombres antiguos (alias):** `0x93AA4165CB67E925` (`N_0x93aa4165cb67e925`)

---
### NetworkSpentImportExportRepair

`_NETWORK_SPENT_IMPORT_EXPORT_REPAIR` · hash `0xC1952F3773BA18FE` · **Cliente**

```lua
NetworkSpentImportExportRepair(p0, p1, p2)
```
```c
void _NETWORK_SPENT_IMPORT_EXPORT_REPAIR(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC1952F3773BA18FE` (`N_0xc1952f3773ba18fe`)

---
### NetworkSpentInStripclub

`NETWORK_SPENT_IN_STRIPCLUB` · hash `0xEE99784E4467689C` · jhash `0x8957038E` · **Cliente**

```lua
NetworkSpentInStripclub(p0, p1, p2, p3)
```
```c
void NETWORK_SPENT_IN_STRIPCLUB(Any p0, BOOL p1, Any p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`Any`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEE99784E4467689C` (`N_0xee99784e4467689c`)

---
### NetworkSpentIslandHeist

`_NETWORK_SPENT_ISLAND_HEIST` · hash `0xE86689E5F82DE429` · **Cliente**

```lua
NetworkSpentIslandHeist(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_ISLAND_HEIST(Any p0, Any p1, Any p2, Any p3);
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
### NetworkSpentJobSkip

`_NETWORK_SPENT_JOB_SKIP` · hash `0x28F174A67B8D0C2F` · **Cliente**

```lua
NetworkSpentJobSkip(amount, matchId, p2, p3)
```
```c
void _NETWORK_SPENT_JOB_SKIP(int amount, char* matchId, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `matchId` (`char*`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### NetworkSpentJukebox

`_NETWORK_SPENT_JUKEBOX` · hash `0x5BCDE0F640C773D2` · **Cliente**

```lua
NetworkSpentJukebox(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_JUKEBOX(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5BCDE0F640C773D2` (`N_0x5bcde0f640c773d2`)

---
### NetworkSpentMakeItRain

`_NETWORK_SPENT_MAKE_IT_RAIN` · hash `0xE5F5A060439C2F5D` · **Cliente**

```lua
NetworkSpentMakeItRain(amount, p1, p2)
```
```c
void _NETWORK_SPENT_MAKE_IT_RAIN(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkSpentMoveYacht

`_NETWORK_SPENT_MOVE_YACHT` · hash `0xE7DF4E0545DFB56E` · **Cliente**

```lua
NetworkSpentMoveYacht(amount, p1, p2)
```
```c
void _NETWORK_SPENT_MOVE_YACHT(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE7DF4E0545DFB56E` (`N_0xe7df4e0545dfb56e`)

---
### NetworkSpentNightclubBarDrink

`_NETWORK_SPENT_NIGHTCLUB_BAR_DRINK` · hash `0xDD21B016E4289465` · **Cliente**

```lua
NetworkSpentNightclubBarDrink(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_NIGHTCLUB_BAR_DRINK(int amount, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### NetworkSpentNightclubEntryFee

`_NETWORK_SPENT_NIGHTCLUB_ENTRY_FEE` · hash `0x876056684281655D` · **Cliente**

```lua
NetworkSpentNightclubEntryFee(player, amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_NIGHTCLUB_ENTRY_FEE(Player player, int amount, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `player` (`Player`)
- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### NetworkSpentNoCops

`NETWORK_SPENT_NO_COPS` · hash `0xD5BB406F4E04019F` · jhash `0x2E51C61C` · **Cliente**

```lua
NetworkSpentNoCops(p0, p1, p2)
```
```c
void NETWORK_SPENT_NO_COPS(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD5BB406F4E04019F` (`N_0xd5bb406f4e04019f`)

---
### NetworkSpentOrderBodyguardVehicle

`_NETWORK_SPENT_ORDER_BODYGUARD_VEHICLE` · hash `0xE8B0B270B6E7C76E` · **Cliente**

```lua
NetworkSpentOrderBodyguardVehicle(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_ORDER_BODYGUARD_VEHICLE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE8B0B270B6E7C76E` (`N_0xe8b0b270b6e7c76e`)

---
### NetworkSpentOrderWarehouseVehicle

`_NETWORK_SPENT_ORDER_WAREHOUSE_VEHICLE` · hash `0x05F04155A226FBBF` · **Cliente**

```lua
NetworkSpentOrderWarehouseVehicle(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_ORDER_WAREHOUSE_VEHICLE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x05F04155A226FBBF` (`N_0x05f04155a226fbbf`)

---
### NetworkSpentPaServiceDancer

`_NETWORK_SPENT_PA_SERVICE_DANCER` · hash `0xB49ECA122467D05F` · **Cliente**

```lua
NetworkSpentPaServiceDancer(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_PA_SERVICE_DANCER(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB49ECA122467D05F` (`N_0xb49eca122467d05f`)

---
### NetworkSpentPaServiceHeliPickup

`_NETWORK_SPENT_PA_SERVICE_HELI_PICKUP` · hash `0x0FE8E1FCD2B86B33` · **Cliente**

```lua
NetworkSpentPaServiceHeliPickup(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_PA_SERVICE_HELI_PICKUP(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0FE8E1FCD2B86B33` (`N_0x0fe8e1fcd2b86b33`)

---
### NetworkSpentPayBoss

`_NETWORK_SPENT_PAY_BOSS` · hash `0xDBC966A01C02BCA7` · **Cliente**

```lua
NetworkSpentPayBoss(p0, p1, p2)
```
```c
void _NETWORK_SPENT_PAY_BOSS(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDBC966A01C02BCA7` (`N_0xdbc966a01c02bca7`)

---
### NetworkSpentPayGoon

`_NETWORK_SPENT_PAY_GOON` · hash `0x08A1B82B91900682` · **Cliente**

```lua
NetworkSpentPayGoon(p0, p1, amount)
```
```c
void _NETWORK_SPENT_PAY_GOON(int p0, int p1, int amount);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x08A1B82B91900682` (`N_0x08a1b82b91900682`)

---
### NetworkSpentPayVehicleInsurancePremium

`NETWORK_SPENT_PAY_VEHICLE_INSURANCE_PREMIUM` · hash `0x9FF28D88C766E3E8` · jhash `0x4E665BB2` · **Cliente**

```lua
local networkHandle = NetworkSpentPayVehicleInsurancePremium(amount, vehicleModel, notBankrupt, hasTheMoney)
```
```c
void NETWORK_SPENT_PAY_VEHICLE_INSURANCE_PREMIUM(int amount, Hash vehicleModel, int* networkHandle, BOOL notBankrupt, BOOL hasTheMoney);
```

**Parámetros**

- `amount` (`int`)
- `vehicleModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `notBankrupt` (`BOOL`)
- `hasTheMoney` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
According to how I understood this in the freemode script alone,
The first parameter is determined by a function named, func_5749 within the freemode script which has a list of all the vehicles and a set price to return which some vehicles deals with globals as well. So the first parameter is basically the set in stone insurance cost it's gonna charge you for that specific vehicle model.
The second parameter whoever put it was right, they call GET_ENTITY_MODEL with the vehicle as the paremeter.
The third parameter is the network handle as they call their little struct<13> func or atleast how the script decompiled it to look which in lamens terms just returns the network handle of the previous owner based on DECOR_GET_INT(vehicle, "Previous_Owner").
The fourth parameter is a bool that returns true/false depending on if your bank balance is greater then 0.
The fifth and last parameter is a bool that returns true/false depending on if you have the money for the car based on the cost returned by func_5749. In the freemode script eg,
bool hasTheMoney = MONEY::_GET_BANK_BALANCE() < carCost.
```

---
### NetworkSpentPlayerHealthcare

`NETWORK_SPENT_PLAYER_HEALTHCARE` · hash `0x7C99101F7FCE2EE5` · jhash `0x3D96A21C` · **Cliente**

```lua
NetworkSpentPlayerHealthcare(p0, p1, p2, p3)
```
```c
void NETWORK_SPENT_PLAYER_HEALTHCARE(int p0, int p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7C99101F7FCE2EE5` (`N_0x7c99101f7fce2ee5`)

---
### NetworkSpentProstitutes

`NETWORK_SPENT_PROSTITUTES` · hash `0xB21B89501CFAC79E` · jhash `0x78436D07` · **Cliente**

```lua
NetworkSpentProstitutes(p0, p1, p2)
```
```c
void NETWORK_SPENT_PROSTITUTES(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentPurchaseHangar

`_NETWORK_SPENT_PURCHASE_HANGAR` · hash `0xCCB339CC970452DA` · **Cliente**

```lua
NetworkSpentPurchaseHangar(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_PURCHASE_HANGAR(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkSpentPurchaseWarehouse

`_NETWORK_SPENT_PURCHASE_WAREHOUSE` · hash `0x33981D6804E62F49` · **Cliente**

```lua
NetworkSpentPurchaseWarehouse(amount, data, p2, p3)
```
```c
void _NETWORK_SPENT_PURCHASE_WAREHOUSE(int amount, Any data, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `data` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x33981D6804E62F49` (`N_0x33981d6804e62f49`)

---
### NetworkSpentRdrhatchetBonus

`_NETWORK_SPENT_RDRHATCHET_BONUS` · hash `0xE284D46FFDB82E36` · **Cliente**

```lua
NetworkSpentRdrhatchetBonus(amount, p1, p2)
```
```c
void _NETWORK_SPENT_RDRHATCHET_BONUS(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### NetworkSpentRehireDj

`_NETWORK_SPENT_REHIRE_DJ` · hash `0xF6C8A544E4CF14FC` · **Cliente**

```lua
NetworkSpentRehireDj(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_REHIRE_DJ(int amount, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### NetworkSpentRenameOrganization

`_NETWORK_SPENT_RENAME_ORGANIZATION` · hash `0xFC4EE00A7B3BFB76` · **Cliente**

```lua
NetworkSpentRenameOrganization(p0, p1, p2)
```
```c
void _NETWORK_SPENT_RENAME_ORGANIZATION(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFC4EE00A7B3BFB76` (`N_0xfc4ee00a7b3bfb76`)

---
### NetworkSpentRequestHeist

`NETWORK_SPENT_REQUEST_HEIST` · hash `0x9D26502BB97BFE62` · jhash `0xF4287778` · **Cliente**

```lua
NetworkSpentRequestHeist(p0, p1, p2)
```
```c
void NETWORK_SPENT_REQUEST_HEIST(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9D26502BB97BFE62` (`N_0x9d26502bb97bfe62`), `_NETWORK_SPENT_REQUEST_HEIST` (`NetworkSpentRequestHeist`)

---
### NetworkSpentRequestJob

`NETWORK_SPENT_REQUEST_JOB` · hash `0x8204DA7934DF3155` · jhash `0xD57A5125` · **Cliente**

```lua
NetworkSpentRequestJob(p0, p1, p2)
```
```c
void NETWORK_SPENT_REQUEST_JOB(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8204DA7934DF3155` (`N_0x8204da7934df3155`)

---
### NetworkSpentRobbedByMugger

`NETWORK_SPENT_ROBBED_BY_MUGGER` · hash `0x995A65F15F581359` · jhash `0xE6AAA0D5` · **Cliente**

```lua
NetworkSpentRobbedByMugger(amount, p1, p2)
```
```c
void NETWORK_SPENT_ROBBED_BY_MUGGER(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x995A65F15F581359` (`N_0x995a65f15f581359`)

---
### NetworkSpentSalesDisplay

`_NETWORK_SPENT_SALES_DISPLAY` · hash `0x7E2F4E8F44CAF4E0` · **Cliente**

```lua
NetworkSpentSalesDisplay(p0)
```
```c
void _NETWORK_SPENT_SALES_DISPLAY(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### NetworkSpentSpinTheWheelPayment

`_NETWORK_SPENT_SPIN_THE_WHEEL_PAYMENT` · hash `0x9A5BD1D0000B339C` · **Cliente**

```lua
NetworkSpentSpinTheWheelPayment(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_SPIN_THE_WHEEL_PAYMENT(int amount, Any p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604

NativeDB Removed Parameter 4: BOOL p3
```

---
### NetworkSpentSubmarine

`_NETWORK_SPENT_SUBMARINE` · hash `0x6C8BC1488527AAAB` · **Cliente**

```lua
NetworkSpentSubmarine(p0, p1, p2, p3, p4, p5)
```
```c
void _NETWORK_SPENT_SUBMARINE(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
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
NativeDB Introduced: v2189
```

---
### NetworkSpentTaxi

`NETWORK_SPENT_TAXI` · hash `0x17C3A7D31EAE39F9` · jhash `0x1F3DB3E3` · **Cliente**

```lua
NetworkSpentTaxi(amount, p1, p2)
```
```c
void NETWORK_SPENT_TAXI(int amount, BOOL p1, BOOL p2);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentTelescope

`NETWORK_SPENT_TELESCOPE` · hash `0x7FE61782AD94CC09` · jhash `0xAE7FF044` · **Cliente**

```lua
NetworkSpentTelescope(p0, p1, p2)
```
```c
void NETWORK_SPENT_TELESCOPE(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### NetworkSpentUpgradeArena

`_NETWORK_SPENT_UPGRADE_ARENA` · hash `0x037ABB06825D7AB1` · **Cliente**

```lua
NetworkSpentUpgradeArena(amount, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_ARENA(int amount, BOOL p1, BOOL p2, char* p3);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### NetworkSpentUpgradeAutoshop

`_NETWORK_SPENT_UPGRADE_AUTOSHOP` · hash `0xDD829AA198FDC46C` · **Cliente**

```lua
NetworkSpentUpgradeAutoshop(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_AUTOSHOP(Any p0, Any p1, Any p2, Any p3);
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

**Nombres antiguos (alias):** `0xDD829AA198FDC46C` (`N_0xdd829aa198fdc46c`)

---
### NetworkSpentUpgradeBase

`_NETWORK_SPENT_UPGRADE_BASE` · hash `0x3DD3F33A5D55EA6F` · **Cliente**

```lua
NetworkSpentUpgradeBase(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_BASE(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentUpgradeBunker

`_NETWORK_SPENT_UPGRADE_BUNKER` · hash `0x0C82D21A77C22D49` · **Cliente**

```lua
NetworkSpentUpgradeBunker(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_BUNKER(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0C82D21A77C22D49` (`N_0x0c82d21a77c22d49`)

---
### NetworkSpentUpgradeCasino

`_NETWORK_SPENT_UPGRADE_CASINO` · hash `0x4740D62BC1B4EBEA` · **Cliente**

```lua
local data = NetworkSpentUpgradeCasino(amount, p1, p2, data)
```
```c
void _NETWORK_SPENT_UPGRADE_CASINO(int amount, BOOL p1, BOOL p2, Any* data);
```

**Parámetros**

- `amount` (`int`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### NetworkSpentUpgradeHangar

`_NETWORK_SPENT_UPGRADE_HANGAR` · hash `0x615EB504B0788DAF` · **Cliente**

```lua
NetworkSpentUpgradeHangar(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_HANGAR(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### NetworkSpentUpgradeSub

`_NETWORK_SPENT_UPGRADE_SUB` · hash `0x89049A84065CE68E` · **Cliente**

```lua
NetworkSpentUpgradeSub(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_SUB(Any p0, Any p1, Any p2, Any p3);
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

**Nombres antiguos (alias):** `0x89049A84065CE68E` (`N_0x89049a84065ce68e`)

---
### NetworkSpentUpgradeTiltrotor

`_NETWORK_SPENT_UPGRADE_TILTROTOR` · hash `0x165E135D6DFA2907` · **Cliente**

```lua
NetworkSpentUpgradeTiltrotor(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_TILTROTOR(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### NetworkSpentUpgradeTruck

`_NETWORK_SPENT_UPGRADE_TRUCK` · hash `0x365E877C61D6988B` · **Cliente**

```lua
NetworkSpentUpgradeTruck(p0, p1, p2, p3)
```
```c
void _NETWORK_SPENT_UPGRADE_TRUCK(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x365E877C61D6988B` (`N_0x365e877c61d6988b`)

---
### NetworkSpentVehicleExportMods

`_NETWORK_SPENT_VEHICLE_EXPORT_MODS` · hash `0xA75CCF58A60A5FD1` · **Cliente**

```lua
NetworkSpentVehicleExportMods(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void _NETWORK_SPENT_VEHICLE_EXPORT_MODS(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9);
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

**Nombres antiguos (alias):** `0xA75CCF58A60A5FD1` (`N_0xa75ccf58a60a5fd1`)

---
### NetworkSpentVehicleRequested

`_NETWORK_SPENT_VEHICLE_REQUESTED` · hash `0x02D24A35A9CC3503` · **Cliente**

```lua
NetworkSpentVehicleRequested(p0, p1, p2, p3, p4)
```
```c
void _NETWORK_SPENT_VEHICLE_REQUESTED(Any p0, Any p1, Any p2, Any p3, Any p4);
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
NativeDB Introduced: v2699
```

---
### NetworkSpentVipUtilityCharges

`_NETWORK_SPENT_VIP_UTILITY_CHARGES` · hash `0x5182A339A3474510` · **Cliente**

```lua
NetworkSpentVipUtilityCharges(p0, p1, p2)
```
```c
void _NETWORK_SPENT_VIP_UTILITY_CHARGES(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5182A339A3474510` (`N_0x5182a339a3474510`)

---
### NetworkSpentWager

`_NETWORK_SPENT_WAGER` · hash `0xD99DB210089617FE` · **Cliente**

```lua
NetworkSpentWager(p0, p1, amount)
```
```c
void _NETWORK_SPENT_WAGER(Any p0, Any p1, int amount);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `amount` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD99DB210089617FE` (`N_0xd99db210089617fe`)

---
### ProcessCashGift

`PROCESS_CASH_GIFT` · hash `0x20194D48EAEC9A41` · jhash `0xC5D8B1E9` · **Cliente**

```lua
local retval, p0, p1 = ProcessCashGift(p2)
```
```c
char* PROCESS_CASH_GIFT(int* p0, int* p1, char* p2);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`char*`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x20194D48EAEC9A41` (`N_0x20194d48eaec9a41`)

---
### WithdrawVc

`WITHDRAW_VC` · hash `0xF70EFA14FE091429` · jhash `0x8B755993` · **Cliente**

```lua
local retval = WithdrawVc(amount)
```
```c
int WITHDRAW_VC(int amount);
```

**Parámetros**

- `amount` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Does nothing and always returns 0.
```

**Nombres antiguos (alias):** `0xF70EFA14FE091429` (`N_0xf70efa14fe091429`)

---
