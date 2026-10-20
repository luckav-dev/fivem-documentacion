# Natives de GTA V — HUD

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `HUD`: **509** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateFrontendMenu`](#activatefrontendmenu) · [`AddBlipForArea`](#addblipforarea) · [`AddBlipForCoord`](#addblipforcoord) · [`AddBlipForEntity`](#addblipforentity) · [`AddBlipForPickup`](#addblipforpickup) · [`AddBlipForRadius`](#addblipforradius) · [`AddNextMessageToPreviousBriefs`](#addnextmessagetopreviousbriefs) · [`AddPointToGpsCustomRoute`](#addpointtogpscustomroute) · [`AddPointToGpsMultiRoute`](#addpointtogpsmultiroute) · [`AddTextComponentFloat`](#addtextcomponentfloat) · [`AddTextComponentFormattedInteger`](#addtextcomponentformattedinteger) · [`AddTextComponentInteger`](#addtextcomponentinteger) · [`AddTextComponentSubstringBlipName`](#addtextcomponentsubstringblipname) · [`AddTextComponentSubstringKeyboardDisplay`](#addtextcomponentsubstringkeyboarddisplay) · [`AddTextComponentSubstringPhoneNumber`](#addtextcomponentsubstringphonenumber) · [`AddTextComponentSubstringPlayerName`](#addtextcomponentsubstringplayername) · [`AddTextComponentSubstringTextLabel`](#addtextcomponentsubstringtextlabel) · [`AddTextComponentSubstringTextLabelHashKey`](#addtextcomponentsubstringtextlabelhashkey) · [`AddTextComponentSubstringTime`](#addtextcomponentsubstringtime) · [`AddTextComponentSubstringWebsite`](#addtextcomponentsubstringwebsite) · [`AllowDisplayOfMultiplayerCashText`](#allowdisplayofmultiplayercashtext) · [`AllowPauseMenuWhenDeadThisFrame`](#allowpausemenuwhendeadthisframe) · [`AllowSonarBlips`](#allowsonarblips) · [`BeginTextCommandBusyspinnerOn`](#begintextcommandbusyspinneron) · [`BeginTextCommandClearPrint`](#begintextcommandclearprint) · [`BeginTextCommandDisplayHelp`](#begintextcommanddisplayhelp) · [`BeginTextCommandDisplayText`](#begintextcommanddisplaytext) · [`BeginTextCommandGetWidth`](#begintextcommandgetwidth) · [`BeginTextCommandIsMessageDisplayed`](#begintextcommandismessagedisplayed) · [`BeginTextCommandIsThisHelpMessageBeingDisplayed`](#begintextcommandisthishelpmessagebeingdisplayed) · [`BeginTextCommandLineCount`](#begintextcommandlinecount) · [`BeginTextCommandObjective`](#begintextcommandobjective) · [`BeginTextCommandOverrideButtonText`](#begintextcommandoverridebuttontext) · [`BeginTextCommandPrint`](#begintextcommandprint) · [`BeginTextCommandSetBlipName`](#begintextcommandsetblipname) · [`BeginTextCommandThefeedPost`](#begintextcommandthefeedpost) · [`BusyspinnerIsDisplaying`](#busyspinnerisdisplaying) · [`BusyspinnerIsOn`](#busyspinnerison) · [`BusyspinnerOff`](#busyspinneroff) · [`ChangeFakeMpCash`](#changefakempcash) · [`ClearAdditionalText`](#clearadditionaltext) · [`ClearAllBlipRoutes`](#clearallbliproutes) · [`ClearAllHelpMessages`](#clearallhelpmessages) · [`ClearBrief`](#clearbrief) · [`ClearDynamicPauseMenuErrorMessage`](#cleardynamicpausemenuerrormessage) · [`ClearFloatingHelp`](#clearfloatinghelp) · [`ClearGpsCustomRoute`](#cleargpscustomroute) · [`ClearGpsFlags`](#cleargpsflags) · [`ClearGpsMultiRoute`](#cleargpsmultiroute) · [`ClearGpsPlayerWaypoint`](#cleargpsplayerwaypoint) · [`ClearGpsRaceTrack`](#cleargpsracetrack) · [`ClearHelp`](#clearhelp) · [`ClearPedInPauseMenu`](#clearpedinpausemenu) · [`ClearPrints`](#clearprints) · [`ClearRaceGalleryBlips`](#clearracegalleryblips) · [`ClearReminderMessage`](#clearremindermessage) · [`ClearSmallPrints`](#clearsmallprints) · [`ClearThisPrint`](#clearthisprint) · [`CloseMultiplayerChat`](#closemultiplayerchat) · [`CloseSocialClubMenu`](#closesocialclubmenu) · [`CreateFakeMpGamerTag`](#createfakempgamertag) · [`CreateMpGamerTagWithCrewColor`](#creatempgamertagwithcrewcolor) · [`DeleteWaypointsFromThisPlayer`](#deletewaypointsfromthisplayer) · [`DisableFrontendThisFrame`](#disablefrontendthisframe) · [`DisableMultiplayerChat`](#disablemultiplayerchat) · [`DisplayAmmoThisFrame`](#displayammothisframe) · [`DisplayAreaName`](#displayareaname) · [`DisplayCash`](#displaycash) · [`DisplayHelpTextThisFrame`](#displayhelptextthisframe) · [`DisplayHud`](#displayhud) · [`DisplayHudWhenDeadThisFrame`](#displayhudwhendeadthisframe) · [`DisplayHudWhenPausedThisFrame`](#displayhudwhenpausedthisframe) · [`DisplayPlayerNameTagsOnBlips`](#displayplayernametagsonblips) · [`DisplayRadar`](#displayradar) · [`DisplaySniperScopeThisFrame`](#displaysniperscopethisframe) · [`DoesBlipExist`](#doesblipexist) · [`DoesBlipHaveGpsRoute`](#doesbliphavegpsroute) · [`DoesPedHaveAiBlip`](#doespedhaveaiblip) · [`DoesTextBlockExist`](#doestextblockexist) · [`DoesTextLabelExist`](#doestextlabelexist) · [`DontTiltMinimapThisFrame`](#donttiltminimapthisframe) · [`DrawHudOverFadeThisFrame`](#drawhudoverfadethisframe) · [`EndTextCommandBusyspinnerOn`](#endtextcommandbusyspinneron) · [`EndTextCommandClearPrint`](#endtextcommandclearprint) · [`EndTextCommandDisplayHelp`](#endtextcommanddisplayhelp) · [`EndTextCommandDisplayText`](#endtextcommanddisplaytext) · [`EndTextCommandGetWidth`](#endtextcommandgetwidth) · [`EndTextCommandIsMessageDisplayed`](#endtextcommandismessagedisplayed) · [`EndTextCommandIsThisHelpMessageBeingDisplayed`](#endtextcommandisthishelpmessagebeingdisplayed) · [`EndTextCommandLineCount`](#endtextcommandlinecount) · [`EndTextCommandObjective`](#endtextcommandobjective) · [`EndTextCommandOverrideButtonText`](#endtextcommandoverridebuttontext) · [`EndTextCommandPrint`](#endtextcommandprint) · [`EndTextCommandSetBlipName`](#endtextcommandsetblipname) · [`EndTextCommandThefeedPostAward`](#endtextcommandthefeedpostaward) · [`EndTextCommandThefeedPostCrewRankup`](#endtextcommandthefeedpostcrewrankup) · [`EndTextCommandThefeedPostCrewtag`](#endtextcommandthefeedpostcrewtag) · [`EndTextCommandThefeedPostCrewtagWithGameName`](#endtextcommandthefeedpostcrewtagwithgamename) · [`EndTextCommandThefeedPostMessagetext`](#endtextcommandthefeedpostmessagetext) · [`EndTextCommandThefeedPostMessagetextGxtEntry`](#endtextcommandthefeedpostmessagetextgxtentry) · [`EndTextCommandThefeedPostMessagetextTu`](#endtextcommandthefeedpostmessagetexttu) · [`EndTextCommandThefeedPostMessagetextWithCrewTag`](#endtextcommandthefeedpostmessagetextwithcrewtag) · [`EndTextCommandThefeedPostMessagetextWithCrewTagAndAdditionalIcon`](#endtextcommandthefeedpostmessagetextwithcrewtagandadditionalicon) · [`EndTextCommandThefeedPostMpticker`](#endtextcommandthefeedpostmpticker) · [`EndTextCommandThefeedPostReplayIcon`](#endtextcommandthefeedpostreplayicon) · [`EndTextCommandThefeedPostReplayInput`](#endtextcommandthefeedpostreplayinput) · [`EndTextCommandThefeedPostStats`](#endtextcommandthefeedpoststats) · [`EndTextCommandThefeedPostTicker`](#endtextcommandthefeedpostticker) · [`EndTextCommandThefeedPostTickerForced`](#endtextcommandthefeedposttickerforced) · [`EndTextCommandThefeedPostTickerWithTokens`](#endtextcommandthefeedposttickerwithtokens) · [`EndTextCommandThefeedPostUnlock`](#endtextcommandthefeedpostunlock) · [`EndTextCommandThefeedPostUnlockTu`](#endtextcommandthefeedpostunlocktu) · [`EndTextCommandThefeedPostUnlockTuWithColor`](#endtextcommandthefeedpostunlocktuwithcolor) · [`EndTextCommandThefeedPostVersusTu`](#endtextcommandthefeedpostversustu) · [`FlagPlayerContextInTournament`](#flagplayercontextintournament) · [`FlashAbilityBar`](#flashabilitybar) · [`FlashMinimapDisplay`](#flashminimapdisplay) · [`FlashMinimapDisplayWithColor`](#flashminimapdisplaywithcolor) · [`FlashWantedDisplay`](#flashwanteddisplay) · [`ForceCloseReportugcMenu`](#forceclosereportugcmenu) · [`ForceCloseTextInputBox`](#forceclosetextinputbox) · [`ForceSonarBlipsThisFrame`](#forcesonarblipsthisframe) · [`GetAiBlip`](#getaiblip) · [`GetAiBlip_2`](#getaiblip_2) · [`GetBlipAlpha`](#getblipalpha) · [`GetBlipColour`](#getblipcolour) · [`GetBlipCoords`](#getblipcoords) · [`GetBlipFromEntity`](#getblipfromentity) · [`GetBlipHudColour`](#getbliphudcolour) · [`GetBlipInfoIdCoord`](#getblipinfoidcoord) · [`GetBlipInfoIdDisplay`](#getblipinfoiddisplay) · [`GetBlipInfoIdEntityIndex`](#getblipinfoidentityindex) · [`GetBlipInfoIdPickupIndex`](#getblipinfoidpickupindex) · [`GetBlipInfoIdType`](#getblipinfoidtype) · [`GetBlipRotation`](#getbliprotation) · [`GetBlipSprite`](#getblipsprite) · [`GetClosestBlipOfType`](#getclosestblipoftype) · [`GetCurrentFrontendMenuVersion`](#getcurrentfrontendmenuversion) · [`GetCurrentWebpageId`](#getcurrentwebpageid) · [`GetCurrentWebsiteId`](#getcurrentwebsiteid) · [`GetDefaultScriptRendertargetRenderId`](#getdefaultscriptrendertargetrenderid) · [`GetFilenameForAudioConversation`](#getfilenameforaudioconversation) · [`GetFirstBlipInfoId`](#getfirstblipinfoid) · [`GetGlobalActionscriptFlag`](#getglobalactionscriptflag) · [`GetHudColour`](#gethudcolour) · [`GetHudComponentPosition`](#gethudcomponentposition) · [`GetHudScreenPositionFromWorldPosition`](#gethudscreenpositionfromworldposition) · [`GetLengthOfLiteralString`](#getlengthofliteralstring) · [`GetLengthOfLiteralStringInBytes`](#getlengthofliteralstringinbytes) · [`GetLengthOfStringWithThisTextLabel`](#getlengthofstringwiththistextlabel) · [`GetMainPlayerBlipId`](#getmainplayerblipid) · [`GetMenuLayoutChangedEventDetails`](#getmenulayoutchangedeventdetails) · [`GetMenuPedBoolStat`](#getmenupedboolstat) · [`GetMenuPedFloatStat`](#getmenupedfloatstat) · [`GetMenuPedIntStat`](#getmenupedintstat) · [`GetMenuPedMaskedIntStat`](#getmenupedmaskedintstat) · [`GetMinimapFowCoordinateIsRevealed`](#getminimapfowcoordinateisrevealed) · [`GetMinimapFowDiscoveryRatio`](#getminimapfowdiscoveryratio) · [`GetMouseEvent`](#getmouseevent) · [`GetNamedRendertargetRenderId`](#getnamedrendertargetrenderid) · [`GetNewSelectedMissionCreatorBlip`](#getnewselectedmissioncreatorblip) · [`GetNextBlipInfoId`](#getnextblipinfoid) · [`GetNorthRadarBlip`](#getnorthradarblip) · [`GetNumberOfActiveBlips`](#getnumberofactiveblips) · [`GetPauseMenuPosition`](#getpausemenuposition) · [`GetPauseMenuSelection`](#getpausemenuselection) · [`GetPauseMenuState`](#getpausemenustate) · [`GetRenderedCharacterHeight`](#getrenderedcharacterheight) · [`GetStandardBlipEnumId`](#getstandardblipenumid) · [`GetStreetNameFromHashKey`](#getstreetnamefromhashkey) · [`GetTextSubstring`](#gettextsubstring) · [`GetTextSubstringSafe`](#gettextsubstringsafe) · [`GetTextSubstringSlice`](#gettextsubstringslice) · [`GetWarningMessageTitleHash`](#getwarningmessagetitlehash) · [`GetWaypointBlipEnumId`](#getwaypointblipenumid) · [`GivePedToPauseMenu`](#givepedtopausemenu) · [`HasAdditionalTextLoaded`](#hasadditionaltextloaded) · [`HasDirectorModeBeenTriggered`](#hasdirectormodebeentriggered) · [`HasMenuLayoutChangedEventOccurred`](#hasmenulayoutchangedeventoccurred) · [`HasThisAdditionalTextLoaded`](#hasthisadditionaltextloaded) · [`HideAreaAndVehicleNameThisFrame`](#hideareaandvehiclenamethisframe) · [`HideHelpTextThisFrame`](#hidehelptextthisframe) · [`HideHudAndRadarThisFrame`](#hidehudandradarthisframe) · [`HideHudComponentThisFrame`](#hidehudcomponentthisframe) · [`HideLoadingOnFadeThisFrame`](#hideloadingonfadethisframe) · [`HideMinimapExteriorMapThisFrame`](#hideminimapexteriormapthisframe) · [`HideMinimapInteriorMapThisFrame`](#hideminimapinteriormapthisframe) · [`HideNumberOnBlip`](#hidenumberonblip) · [`HideScriptedHudComponentThisFrame`](#hidescriptedhudcomponentthisframe) · [`HudDisplayLoadingScreenTips`](#huddisplayloadingscreentips) · [`HudForceWeaponWheel`](#hudforceweaponwheel) · [`HudSetWeaponWheelTopSlot`](#hudsetweaponwheeltopslot) · [`HudWeaponWheelGetSelectedHash`](#hudweaponwheelgetselectedhash) · [`HudWeaponWheelGetSlotHash`](#hudweaponwheelgetslothash) · [`HudWeaponWheelIgnoreControlInput`](#hudweaponwheelignorecontrolinput) · [`HudWeaponWheelIgnoreSelection`](#hudweaponwheelignoreselection) · [`IsBlipFlashing`](#isblipflashing) · [`IsBlipOnMinimap`](#isbliponminimap) · [`IsBlipShortRange`](#isblipshortrange) · [`IsFloatingHelpTextOnScreen`](#isfloatinghelptextonscreen) · [`IsFrontendReadyForControl`](#isfrontendreadyforcontrol) · [`IsHelpMessageBeingDisplayed`](#ishelpmessagebeingdisplayed) · [`IsHelpMessageFadingOut`](#ishelpmessagefadingout) · [`IsHelpMessageOnScreen`](#ishelpmessageonscreen) · [`IsHoveringOverMissionCreatorBlip`](#ishoveringovermissioncreatorblip) · [`IsHudComponentActive`](#ishudcomponentactive) · [`IsHudHidden`](#ishudhidden) · [`IsHudPreferenceSwitchedOn`](#ishudpreferenceswitchedon) · [`IsMessageBeingDisplayed`](#ismessagebeingdisplayed) · [`IsMinimapRendering`](#isminimaprendering) · [`IsMissionCreatorBlip`](#ismissioncreatorblip) · [`IsMouseRolledOverInstructionalButtons`](#ismouserolledoverinstructionalbuttons) · [`IsMpGamerTagActive`](#ismpgamertagactive) · [`IsMpGamerTagFree`](#ismpgamertagfree) · [`IsMpGamerTagMovieActive`](#ismpgamertagmovieactive) · [`IsMultiplayerChatActive`](#ismultiplayerchatactive) · [`IsNamedRendertargetLinked`](#isnamedrendertargetlinked) · [`IsNamedRendertargetRegistered`](#isnamedrendertargetregistered) · [`IsNavigatingMenuContent`](#isnavigatingmenucontent) · [`IsOnlinePoliciesMenuActive`](#isonlinepoliciesmenuactive) · [`IsPauseMenuActive`](#ispausemenuactive) · [`IsPauseMenuRestarting`](#ispausemenurestarting) · [`IsPausemapInInteriorMode`](#ispausemapininteriormode) · [`IsRadarHidden`](#isradarhidden) · [`IsRadarPreferenceSwitchedOn`](#isradarpreferenceswitchedon) · [`IsReportugcMenuOpen`](#isreportugcmenuopen) · [`IsScriptedHudComponentActive`](#isscriptedhudcomponentactive) · [`IsScriptedHudComponentHiddenThisFrame`](#isscriptedhudcomponenthiddenthisframe) · [`IsSocialClubActive`](#issocialclubactive) · [`IsStreamingAdditionalText`](#isstreamingadditionaltext) · [`IsSubtitlePreferenceSwitchedOn`](#issubtitlepreferenceswitchedon) · [`IsUpdatingMpGamerTagNameAndCrewDetails`](#isupdatingmpgamertagnameandcrewdetails) · [`IsWarningMessageActive`](#iswarningmessageactive) · [`IsWarningMessageReadyForControl`](#iswarningmessagereadyforcontrol) · [`IsWaypointActive`](#iswaypointactive) · [`LinkNamedRendertarget`](#linknamedrendertarget) · [`LockMinimapAngle`](#lockminimapangle) · [`LockMinimapPosition`](#lockminimapposition) · [`LogDebugInfo`](#logdebuginfo) · [`N_0x04655f9d075d0ae5`](#n_0x04655f9d075d0ae5) · [`N_0x0c698d8f099174c7`](#n_0x0c698d8f099174c7) · [`N_0x0cf54f20de43879c`](#n_0x0cf54f20de43879c) · [`N_0x211c4ef450086857`](#n_0x211c4ef450086857) · [`N_0x214cd562a939246a`](#n_0x214cd562a939246a) · [`N_0x243296a510b562b6`](#n_0x243296a510b562b6) · [`N_0x24a49beaf468dc90`](#n_0x24a49beaf468dc90) · [`N_0x2790f4b17d098e26`](#n_0x2790f4b17d098e26) · [`N_0x2c173ae2bdb9385e`](#n_0x2c173ae2bdb9385e) · [`N_0x2c9f302398e13141`](#n_0x2c9f302398e13141) · [`N_0x2f057596f2bd0061`](#n_0x2f057596f2bd0061) · [`N_0x35a3cd97b2c0a6d2`](#n_0x35a3cd97b2c0a6d2) · [`N_0x4b5b620c9b59ed34`](#n_0x4b5b620c9b59ed34) · [`N_0x55f5a5f07134de60`](#n_0x55f5a5f07134de60) · [`N_0x57d760d55f54e071`](#n_0x57d760d55f54e071) · [`N_0x593feae1f73392d4`](#n_0x593feae1f73392d4) · [`N_0x62e849b7eb28e770`](#n_0x62e849b7eb28e770) · [`N_0x66e7cb63c97b7d20`](#n_0x66e7cb63c97b7d20) · [`N_0x7c226d5346d4d10a`](#n_0x7c226d5346d4d10a) · [`N_0x801879a9b4f4b2fb`](#n_0x801879a9b4f4b2fb) · [`N_0x817b86108eb94e51`](#n_0x817b86108eb94e51) · [`N_0x8410c5e0cd847b9d`](#n_0x8410c5e0cd847b9d) · [`N_0x8f08017f9d7c47bd`](#n_0x8f08017f9d7c47bd) · [`N_0x98c3cf913d895111`](#n_0x98c3cf913d895111) · [`N_0x9fcb3cbfb3ead69a`](#n_0x9fcb3cbfb3ead69a) · [`N_0xa17784fca9548d15`](#n_0xa17784fca9548d15) · [`N_0xa238192f33110615`](#n_0xa238192f33110615) · [`N_0xb552929b85fc27ec`](#n_0xb552929b85fc27ec) · [`N_0xb7b873520c84c118`](#n_0xb7b873520c84c118) · [`N_0xba8d65c1c65702e5`](#n_0xba8d65c1c65702e5) · [`N_0xc2d2ad9eaae265b8`](#n_0xc2d2ad9eaae265b8) · [`N_0xc594b315edf2d4af`](#n_0xc594b315edf2d4af) · [`N_0xc8e1071177a23be5`](#n_0xc8e1071177a23be5) · [`N_0xca6b2f7ce32ab653`](#n_0xca6b2f7ce32ab653) · [`N_0xcd74233600c4ea6b`](#n_0xcd74233600c4ea6b) · [`N_0xd1942374085c8469`](#n_0xd1942374085c8469) · [`N_0xd2049635deb9c375`](#n_0xd2049635deb9c375) · [`N_0xdaf87174be7454ff`](#n_0xdaf87174be7454ff) · [`N_0xde03620f8703a9df`](#n_0xde03620f8703a9df) · [`N_0xe4c3b169876d33d7`](#n_0xe4c3b169876d33d7) · [`N_0xeb81a3dadd503187`](#n_0xeb81a3dadd503187) · [`N_0xf13fe2a80c05c561`](#n_0xf13fe2a80c05c561) · [`N_0xf284ac67940c6812`](#n_0xf284ac67940c6812) · [`N_0xf83d0febe75e62c9`](#n_0xf83d0febe75e62c9) · [`OpenOnlinePoliciesMenu`](#openonlinepoliciesmenu) · [`OpenReportugcMenu`](#openreportugcmenu) · [`OpenSocialClubMenu`](#opensocialclubmenu) · [`OverrideMultiplayerChatColour`](#overridemultiplayerchatcolour) · [`OverrideMultiplayerChatPrefix`](#overridemultiplayerchatprefix) · [`PauseMenuActivateContext`](#pausemenuactivatecontext) · [`PauseMenuDeactivateContext`](#pausemenudeactivatecontext) · [`PauseMenuDisableBusyspinner`](#pausemenudisablebusyspinner) · [`PauseMenuGetMouseHoverIndex`](#pausemenugetmousehoverindex) · [`PauseMenuGetMouseHoverUniqueId`](#pausemenugetmousehoveruniqueid) · [`PauseMenuIsContextActive`](#pausemenuiscontextactive) · [`PauseMenuIsContextMenuActive`](#pausemenuiscontextmenuactive) · [`PauseMenuRedrawInstructionalButtons`](#pausemenuredrawinstructionalbuttons) · [`PauseMenuSetBusySpinner`](#pausemenusetbusyspinner) · [`PauseMenuSetWarnOnTabChange`](#pausemenusetwarnontabchange) · [`PauseMenuceptionGoDeeper`](#pausemenuceptiongodeeper) · [`PauseMenuceptionTheKick`](#pausemenuceptionthekick) · [`PauseToggleFullscreenMap`](#pausetogglefullscreenmap) · [`PreloadBusyspinner`](#preloadbusyspinner) · [`PulseBlip`](#pulseblip) · [`RaceGalleryAddBlip`](#racegalleryaddblip) · [`RaceGalleryFullscreen`](#racegalleryfullscreen) · [`RaceGalleryNextBlipSprite`](#racegallerynextblipsprite) · [`RefreshWaypoint`](#refreshwaypoint) · [`RegisterNamedRendertarget`](#registernamedrendertarget) · [`ReleaseControlOfFrontend`](#releasecontroloffrontend) · [`ReleaseNamedRendertarget`](#releasenamedrendertarget) · [`ReloadMapMenu`](#reloadmapmenu) · [`RemoveBlip`](#removeblip) · [`RemoveMpGamerTag`](#removempgamertag) · [`RemoveMultiplayerBankCash`](#removemultiplayerbankcash) · [`RemoveMultiplayerHudCash`](#removemultiplayerhudcash) · [`RemoveMultiplayerWalletCash`](#removemultiplayerwalletcash) · [`RemoveWarningMessageListItems`](#removewarningmessagelistitems) · [`ReplaceHudColour`](#replacehudcolour) · [`ReplaceHudColourWithRgba`](#replacehudcolourwithrgba) · [`RequestAdditionalText`](#requestadditionaltext) · [`RequestAdditionalTextForDlc`](#requestadditionaltextfordlc) · [`ResetGlobalActionscriptFlag`](#resetglobalactionscriptflag) · [`ResetHudComponentValues`](#resethudcomponentvalues) · [`ResetReticuleValues`](#resetreticulevalues) · [`RestartFrontendMenu`](#restartfrontendmenu) · [`SetAbilityBarValue`](#setabilitybarvalue) · [`SetAbilityBarVisibilityInMultiplayer`](#setabilitybarvisibilityinmultiplayer) · [`SetAllowAbilityBarInMultiplayer`](#setallowabilitybarinmultiplayer) · [`SetAllowCommaOnTextInput`](#setallowcommaontextinput) · [`SetBigmapActive`](#setbigmapactive) · [`SetBlipAlpha`](#setblipalpha) · [`SetBlipAsFriendly`](#setblipasfriendly) · [`SetBlipAsMissionCreatorBlip`](#setblipasmissioncreatorblip) · [`SetBlipAsShortRange`](#setblipasshortrange) · [`SetBlipBright`](#setblipbright) · [`SetBlipCategory`](#setblipcategory) · [`SetBlipColour`](#setblipcolour) · [`SetBlipCoords`](#setblipcoords) · [`SetBlipDisplay`](#setblipdisplay) · [`SetBlipDisplayIndicatorOnBlip`](#setblipdisplayindicatoronblip) · [`SetBlipFade`](#setblipfade) · [`SetBlipFlashInterval`](#setblipflashinterval) · [`SetBlipFlashTimer`](#setblipflashtimer) · [`SetBlipFlashes`](#setblipflashes) · [`SetBlipFlashesAlternate`](#setblipflashesalternate) · [`SetBlipHiddenOnLegend`](#setbliphiddenonlegend) · [`SetBlipHighDetail`](#setbliphighdetail) · [`SetBlipNameFromTextFile`](#setblipnamefromtextfile) · [`SetBlipNameToPlayerName`](#setblipnametoplayername) · [`SetBlipPriority`](#setblippriority) · [`SetBlipRotation`](#setbliprotation) · [`SetBlipRoute`](#setbliproute) · [`SetBlipRouteColour`](#setbliproutecolour) · [`SetBlipScale`](#setblipscale) · [`SetBlipScaleTransformation`](#setblipscaletransformation) · [`SetBlipSecondaryColour`](#setblipsecondarycolour) · [`SetBlipShowCone`](#setblipshowcone) · [`SetBlipShrink`](#setblipshrink) · [`SetBlipSprite`](#setblipsprite) · [`SetBlipSquaredRotation`](#setblipsquaredrotation) · [`SetColourOfNextTextComponent`](#setcolourofnexttextcomponent) · [`SetCustomMpHudColor`](#setcustommphudcolor) · [`SetDirectorModeClearTriggeredFlag`](#setdirectormodecleartriggeredflag) · [`SetFakePausemapPlayerPositionThisFrame`](#setfakepausemapplayerpositionthisframe) · [`SetFloatingHelpTextScreenPosition`](#setfloatinghelptextscreenposition) · [`SetFloatingHelpTextStyle`](#setfloatinghelptextstyle) · [`SetFloatingHelpTextToEntity`](#setfloatinghelptexttoentity) · [`SetFloatingHelpTextWorldPosition`](#setfloatinghelptextworldposition) · [`SetFrontendActive`](#setfrontendactive) · [`SetGpsCustomRouteRender`](#setgpscustomrouterender) · [`SetGpsFlags`](#setgpsflags) · [`SetGpsFlashes`](#setgpsflashes) · [`SetGpsMultiRouteRender`](#setgpsmultirouterender) · [`SetHealthHudDisplayValues`](#sethealthhuddisplayvalues) · [`SetHelpMessageTextStyle`](#sethelpmessagetextstyle) · [`SetHudComponentPosition`](#sethudcomponentposition) · [`SetInteriorZoomLevelDecreased`](#setinteriorzoomleveldecreased) · [`SetInteriorZoomLevelIncreased`](#setinteriorzoomlevelincreased) · [`SetMainPlayerBlipColour`](#setmainplayerblipcolour) · [`SetMaxArmourHudDisplay`](#setmaxarmourhuddisplay) · [`SetMaxHealthHudDisplay`](#setmaxhealthhuddisplay) · [`SetMinimapAltitudeIndicatorLevel`](#setminimapaltitudeindicatorlevel) · [`SetMinimapBlockWaypoint`](#setminimapblockwaypoint) · [`SetMinimapComponent`](#setminimapcomponent) · [`SetMinimapFowRevealCoordinate`](#setminimapfowrevealcoordinate) · [`SetMinimapGolfCourse`](#setminimapgolfcourse) · [`SetMinimapGolfCourseOff`](#setminimapgolfcourseoff) · [`SetMinimapHideFow`](#setminimaphidefow) · [`SetMinimapInPrologue`](#setminimapinprologue) · [`SetMinimapInSpectatorMode`](#setminimapinspectatormode) · [`SetMinimapSonarSweep`](#setminimapsonarsweep) · [`SetMissionName`](#setmissionname) · [`SetMissionName_2`](#setmissionname_2) · [`SetMouseCursorStyle`](#setmousecursorstyle) · [`SetMouseCursorThisFrame`](#setmousecursorthisframe) · [`SetMouseCursorVisible`](#setmousecursorvisible) · [`SetMpGamerTagAlpha`](#setmpgamertagalpha) · [`SetMpGamerTagBigText`](#setmpgamertagbigtext) · [`SetMpGamerTagColour`](#setmpgamertagcolour) · [`SetMpGamerTagDisablePlayerHealthSync`](#setmpgamertagdisableplayerhealthsync) · [`SetMpGamerTagHealthBarColour`](#setmpgamertaghealthbarcolour) · [`SetMpGamerTagMpBagLargeCount`](#setmpgamertagmpbaglargecount) · [`SetMpGamerTagName`](#setmpgamertagname) · [`SetMpGamerTagOverridePlayerHealth`](#setmpgamertagoverrideplayerhealth) · [`SetMpGamerTagUseVehicleHealth`](#setmpgamertagusevehiclehealth) · [`SetMpGamerTagVisibility`](#setmpgamertagvisibility) · [`SetMpGamerTagVisibilityAll`](#setmpgamertagvisibilityall) · [`SetMpGamerTagWantedLevel`](#setmpgamertagwantedlevel) · [`SetMultiplayerBankCash`](#setmultiplayerbankcash) · [`SetMultiplayerHudCash`](#setmultiplayerhudcash) · [`SetMultiplayerWalletCash`](#setmultiplayerwalletcash) · [`SetNewWaypoint`](#setnewwaypoint) · [`SetPauseMenuActive`](#setpausemenuactive) · [`SetPauseMenuPedLighting`](#setpausemenupedlighting) · [`SetPauseMenuPedSleepState`](#setpausemenupedsleepstate) · [`SetPedAiBlipForcedOn`](#setpedaiblipforcedon) · [`SetPedAiBlipGangId`](#setpedaiblipgangid) · [`SetPedAiBlipHasCone`](#setpedaibliphascone) · [`SetPedAiBlipNoticeRange`](#setpedaiblipnoticerange) · [`SetPedAiBlipSprite`](#setpedaiblipsprite) · [`SetPedHasAiBlip`](#setpedhasaiblip) · [`SetPedHasAiBlipWithColor`](#setpedhasaiblipwithcolor) · [`SetPlayerIsInDirectorMode`](#setplayerisindirectormode) · [`SetPmWarningscreenActive`](#setpmwarningscreenactive) · [`SetRaceTrackRender`](#setracetrackrender) · [`SetRadarAsExteriorThisFrame`](#setradarasexteriorthisframe) · [`SetRadarAsInteriorThisFrame`](#setradarasinteriorthisframe) · [`SetRadarZoom`](#setradarzoom) · [`SetRadarZoomPrecise`](#setradarzoomprecise) · [`SetRadarZoomToBlip`](#setradarzoomtoblip) · [`SetRadarZoomToDistance`](#setradarzoomtodistance) · [`SetRadiusBlipEdge`](#setradiusblipedge) · [`SetScriptVariableHudColour`](#setscriptvariablehudcolour) · [`SetScriptVariable_2HudColour`](#setscriptvariable_2hudcolour) · [`SetSocialClubTour`](#setsocialclubtour) · [`SetTextCentre`](#settextcentre) · [`SetTextColour`](#settextcolour) · [`SetTextDropShadow`](#settextdropshadow) · [`SetTextDropshadow`](#settextdropshadow) · [`SetTextEdge`](#settextedge) · [`SetTextFont`](#settextfont) · [`SetTextInputBoxEnabled`](#settextinputboxenabled) · [`SetTextJustification`](#settextjustification) · [`SetTextLeading`](#settextleading) · [`SetTextOutline`](#settextoutline) · [`SetTextProportional`](#settextproportional) · [`SetTextRenderId`](#settextrenderid) · [`SetTextRightJustify`](#settextrightjustify) · [`SetTextScale`](#settextscale) · [`SetTextWrap`](#settextwrap) · [`SetUseIslandMap`](#setuseislandmap) · [`SetUseWaypointAsDestination`](#setusewaypointasdestination) · [`SetWarningMessage`](#setwarningmessage) · [`SetWarningMessageOptionItems`](#setwarningmessageoptionitems) · [`SetWarningMessageWithAlert`](#setwarningmessagewithalert) · [`SetWarningMessageWithHeader`](#setwarningmessagewithheader) · [`SetWarningMessageWithHeaderAndSubstringFlags`](#setwarningmessagewithheaderandsubstringflags) · [`SetWarningMessageWithHeaderExtended`](#setwarningmessagewithheaderextended) · [`SetWaypointOff`](#setwaypointoff) · [`SetWidescreenFormat`](#setwidescreenformat) · [`ShowContactInstructionalButton`](#showcontactinstructionalbutton) · [`ShowCrewIndicatorOnBlip`](#showcrewindicatoronblip) · [`ShowFriendIndicatorOnBlip`](#showfriendindicatoronblip) · [`ShowHasCompletedIndicatorOnBlip`](#showhascompletedindicatoronblip) · [`ShowHeadingIndicatorOnBlip`](#showheadingindicatoronblip) · [`ShowHeightOnBlip`](#showheightonblip) · [`ShowHudComponentThisFrame`](#showhudcomponentthisframe) · [`ShowNumberOnBlip`](#shownumberonblip) · [`ShowOutlineIndicatorOnBlip`](#showoutlineindicatoronblip) · [`ShowPurchaseInstructionalButton`](#showpurchaseinstructionalbutton) · [`ShowScriptedHudComponentThisFrame`](#showscriptedhudcomponentthisframe) · [`ShowSigninUi`](#showsigninui) · [`ShowStartMissionInstructionalButton`](#showstartmissioninstructionalbutton) · [`ShowTickOnBlip`](#showtickonblip) · [`StartGpsCustomRoute`](#startgpscustomroute) · [`StartGpsMultiRoute`](#startgpsmultiroute) · [`SuppressFrontendRenderingThisFrame`](#suppressfrontendrenderingthisframe) · [`TakeControlOfFrontend`](#takecontroloffrontend) · [`ThefeedAutoPostGametipsOff`](#thefeedautopostgametipsoff) · [`ThefeedAutoPostGametipsOn`](#thefeedautopostgametipson) · [`ThefeedClearFrozenPost`](#thefeedclearfrozenpost) · [`ThefeedDisableLoadingScreenTips`](#thefeeddisableloadingscreentips) · [`ThefeedDisplayLoadingScreenTips`](#thefeeddisplayloadingscreentips) · [`ThefeedFlushQueue`](#thefeedflushqueue) · [`ThefeedForceRenderOff`](#thefeedforcerenderoff) · [`ThefeedForceRenderOn`](#thefeedforcerenderon) · [`ThefeedFreezeNextPost`](#thefeedfreezenextpost) · [`ThefeedGetFirstVisibleDeleteRemaining`](#thefeedgetfirstvisibledeleteremaining) · [`ThefeedHideThisFrame`](#thefeedhidethisframe) · [`ThefeedIsPaused`](#thefeedispaused) · [`ThefeedOnlyShowTooltips`](#thefeedonlyshowtooltips) · [`ThefeedPause`](#thefeedpause) · [`ThefeedRemoveItem`](#thefeedremoveitem) · [`ThefeedResetAllParameters`](#thefeedresetallparameters) · [`ThefeedResume`](#thefeedresume) · [`ThefeedSetAnimpostfxColor`](#thefeedsetanimpostfxcolor) · [`ThefeedSetAnimpostfxCount`](#thefeedsetanimpostfxcount) · [`ThefeedSetAnimpostfxSound`](#thefeedsetanimpostfxsound) · [`ThefeedSetFlushAnimpostfx`](#thefeedsetflushanimpostfx) · [`ThefeedSetNextPostBackgroundColor`](#thefeedsetnextpostbackgroundcolor) · [`ThefeedSetScriptedMenuHeight`](#thefeedsetscriptedmenuheight) · [`ThefeedSpsExtendWidescreenOff`](#thefeedspsextendwidescreenoff) · [`ThefeedSpsExtendWidescreenOn`](#thefeedspsextendwidescreenon) · [`ThefeedUpdateItemTexture`](#thefeedupdateitemtexture) · [`ToggleStealthRadar`](#togglestealthradar) · [`TriggerSonarBlip`](#triggersonarblip) · [`UnlockMinimapAngle`](#unlockminimapangle) · [`UnlockMinimapPosition`](#unlockminimapposition) · [`UseFakeMpCash`](#usefakempcash)

---
### ActivateFrontendMenu

`ACTIVATE_FRONTEND_MENU` · hash `0xEF01D36B9C9D0C7B` · jhash `0x01D83872` · **Cliente**

```lua
ActivateFrontendMenu(menuhash, togglePause, component)
```
```c
void ACTIVATE_FRONTEND_MENU(Hash menuhash, BOOL togglePause, int component);
```

**Parámetros**

- `menuhash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `togglePause` (`BOOL`)
- `component` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Does stuff like this:\
gyazo.com/7fcb78ea3520e3dbc5b2c0c0f3712617\
Example:\
int GetHash = GET_HASH_KEY("fe_menu_version_corona_lobby");\
ACTIVATE_FRONTEND_MENU(GetHash, 0, -1);\
BOOL p1 is a toggle to define the game in pause.\
int p2 is unknown but -1 always works, not sure why though.\
\[30/03/2017] ins1de :\
the int p2 is actually a component variable. When the pause menu is visible, it opens the tab related to it.\
Example : Function.Call(Hash.ACTIVATE_FRONTEND_MENU,-1171018317, 0, 42);\
Result : Opens the "Online" tab without pausing the menu, with -1 it opens the map.

Below is a list of all known Frontend Menu Hashes.

*   FE_MENU_VERSION_SP_PAUSE
*   FE_MENU_VERSION_MP_PAUSE
*   FE_MENU_VERSION_CREATOR_PAUSE
*   FE_MENU_VERSION_CUTSCENE_PAUSE
*   FE_MENU_VERSION_SAVEGAME
*   FE_MENU_VERSION_PRE_LOBBY
*   FE_MENU_VERSION_LOBBY
*   FE_MENU_VERSION_MP_CHARACTER_SELECT
*   FE_MENU_VERSION_MP_CHARACTER_CREATION
*   FE_MENU_VERSION_EMPTY
*   FE_MENU_VERSION_EMPTY_NO_BACKGROUND
*   FE_MENU_VERSION_TEXT_SELECTION
*   FE_MENU_VERSION_CORONA
*   FE_MENU_VERSION_CORONA_LOBBY
*   FE_MENU_VERSION_CORONA_JOINED_PLAYERS
*   FE_MENU_VERSION_CORONA_INVITE_PLAYERS
*   FE_MENU_VERSION_CORONA_INVITE_FRIENDS
*   FE_MENU_VERSION_CORONA_INVITE_CREWS
*   FE_MENU_VERSION_CORONA_INVITE_MATCHED_PLAYERS
*   FE_MENU_VERSION_CORONA_INVITE_LAST_JOB_PLAYERS
*   FE_MENU_VERSION_CORONA_RACE
*   FE_MENU_VERSION_CORONA_BETTING
*   FE_MENU_VERSION_JOINING_SCREEN
*   FE_MENU_VERSION_LANDING_MENU
*   FE_MENU_VERSION_LANDING_KEYMAPPING_MENU

---
### AddBlipForArea

`_ADD_BLIP_FOR_AREA` · hash `0xCE5D0E5E315DB238` · **Cliente · también en el servidor (RPC)**

```lua
local retval = AddBlipForArea(x, y, z, width, height)
```
```c
Blip _ADD_BLIP_FOR_AREA(float x, float y, float z, float width, float height);
```

**Parámetros**

- `x` (`float`): The X coordinate of the center of the blip.
- `y` (`float`): The Y coordinate of the center of the blip.
- `z` (`float`): The Z coordinate of the center of the blip.
- `width` (`float`): The width of the blip.
- `height` (`float`): The height of the blip.

**Devuelve:** `Blip` — A handle to the blip.

**Descripción oficial:**

Adds a rectangular blip for the specified coordinates/area.

It is recommended to use [SET_BLIP_ROTATION](#setbliprotation) and [SET_BLIP_COLOUR](#setblipcolour) to make the blip not rotate along with the camera.

By default, the blip will show as a *regular* blip with the specified color/sprite if it is outside of the minimap view.

(Native name is *likely* to actually be ADD_BLIP_FOR_AREA, but due to the usual reasons this can't be confirmed)

**Nombres antiguos (alias):** `0xCE5D0E5E315DB238` (`N_0xce5d0e5e315db238`)

**Ejemplo (lua):**

```lua
local coords = GetEntityCoords(PlayerPedId())
local blip = AddBlipForArea(coords.x, coords.y, coords.z, 100.0, 50.0)
SetBlipRotation(blip, 0)
SetBlipColour(blip, 0xFF00FF80)
```

---
### AddBlipForCoord

`ADD_BLIP_FOR_COORD` · hash `0x5A039BB0BCA604B6` · jhash `0xC6F43D0E` · **Cliente · también en el servidor (RPC)**

```lua
local retval = AddBlipForCoord(x, y, z)
```
```c
Blip ADD_BLIP_FOR_COORD(float x, float y, float z);
```

**Parámetros**

- `x` (`float`): The X coordinate to create the blip on.
- `y` (`float`): The Y coordinate.
- `z` (`float`): The Z coordinate.

**Devuelve:** `Blip` — A blip handle.

**Descripción oficial:**

Creates a blip for the specified coordinates. You can use `SET_BLIP_` natives to change the blip.

**Ejemplo (lua):**

```lua
local destination = AddBlipForCoord(200.0, 200.0, 5.0)
```

---
### AddBlipForEntity

`ADD_BLIP_FOR_ENTITY` · hash `0x5CDE92C702A8FCE7` · jhash `0x30822554` · **Cliente · también en el servidor (RPC)**

```lua
local retval = AddBlipForEntity(entity)
```
```c
Blip ADD_BLIP_FOR_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to create the blip.

**Devuelve:** `Blip` — A blip handle.

**Descripción oficial:**

Create a blip that by default is red (enemy), you can use [SET_BLIP_AS_FRIENDLY](../cfx/servidor.md#addblipforcoord) to make it blue (friend).\
Can be used for objects, vehicles and peds.

Example of enemy:
![enemy](https://i.imgur.com/LIizV6S.png)
Example of friend:
![friend](https://i.imgur.com/XrCuvZP.png)

**Ejemplo (lua):**

```lua
local blip = AddBlipForEntity(PlayerPedId()) -- This adds an enemy blip to yourself
```

**Ejemplo (js):**

```js
const blip = AddBlipForEntity(PlayerPedId()); // This adds an enemy blip to yourself
```

---
### AddBlipForPickup

`ADD_BLIP_FOR_PICKUP` · hash `0xBE339365C863BD36` · jhash `0x16693C3A` · **Cliente**

```lua
local retval = AddBlipForPickup(pickup)
```
```c
Blip ADD_BLIP_FOR_PICKUP(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `Blip`

---
### AddBlipForRadius

`ADD_BLIP_FOR_RADIUS` · hash `0x46818D79B1F7499A` · jhash `0x4626756C` · **Cliente · también en el servidor (RPC)**

```lua
local retval = AddBlipForRadius(posX, posY, posZ, radius)
```
```c
Blip ADD_BLIP_FOR_RADIUS(float posX, float posY, float posZ, float radius);
```

**Parámetros**

- `posX` (`float`): The x position of the blip (you can also send a vector3 instead of the bulk coordinates)
- `posY` (`float`): The y position of the blip (you can also send a vector3 instead of the bulk coordinates)
- `posZ` (`float`): The z position of the blip (you can also send a vector3 instead of the bulk coordinates)
- `radius` (`float`): The number that defines the radius of the blip circle

**Devuelve:** `Blip` — The blip handle that can be manipulated with every `SetBlip` natives

**Descripción oficial:**

Create a blip with a radius for the specified coordinates (it doesnt create the blip sprite, so you need to use [AddBlipCoords](../cfx/servidor.md#addblipforcoord))

Example image:
![example](https://i.imgur.com/fDCmHVD.png)

**Ejemplo (lua):**

```lua
local coords = vector3(0.0, 0.0, 0.0)

local blip = AddBlipForRadius(coords, 100.0) -- need to have .0
SetBlipColour(blip, 1)
SetBlipAlpha(blip, 128)
```

**Ejemplo (js):**

```js
const blip = AddBlipForRadius(0.0, 0.0, 0.0, 100.0);
SetBlipColour(blip, 1);
SetBlipAlpha(blip, 128);
```

---
### AddNextMessageToPreviousBriefs

`ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS` · hash `0x60296AF4BA14ABC5` · jhash `0xB58B25BD` · **Cliente**

```lua
AddNextMessageToPreviousBriefs(addToBrief)
```
```c
void ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS(BOOL addToBrief);
```

**Parámetros**

- `addToBrief` (`BOOL`): Toggles if the next help message will be shown in Pause Menu > Info > Help.

**Devuelve:** `void`

---
### AddPointToGpsCustomRoute

`ADD_POINT_TO_GPS_CUSTOM_ROUTE` · hash `0x311438A071DD9B1A` · jhash `0xEEBDFE55` · **Cliente**

```lua
AddPointToGpsCustomRoute(x, y, z)
```
```c
void ADD_POINT_TO_GPS_CUSTOM_ROUTE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x311438A071DD9B1A` (`N_0x311438a071dd9b1a`)

---
### AddPointToGpsMultiRoute

`ADD_POINT_TO_GPS_MULTI_ROUTE` · hash `0xA905192A6781C41B` · jhash `0xFE485135` · **Cliente**

```lua
AddPointToGpsMultiRoute(x, y, z)
```
```c
void ADD_POINT_TO_GPS_MULTI_ROUTE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA905192A6781C41B` (`N_0xa905192a6781c41b`)

---
### AddTextComponentFloat

`ADD_TEXT_COMPONENT_FLOAT` · hash `0xE7DCB5B874BCD96E` · jhash `0x24D78013` · **Cliente**

```lua
AddTextComponentFloat(value, decimalPlaces)
```
```c
void ADD_TEXT_COMPONENT_FLOAT(float value, int decimalPlaces);
```

**Parámetros**

- `value` (`float`): The number to substitute in the label.
- `decimalPlaces` (`int`): How many decimal places to add

**Devuelve:** `void`

**Descripción oficial:**

Adds a float to a text component placeholder, replacing `~1~` in the current text command's text label.

![Example output](https://i.imgur.com/jvuQ0II.png)

**Ejemplo (lua):**

```lua
-- on initialization
AddTextEntry('TEST_LABEL', 'Label: ~1~')

-- when drawing
BeginTextCommandThefeedPost('TEST_LABEL')
AddTextComponentFloat(1000.0, 2)
EndTextCommandThefeedPostTicker(false, true)
```

---
### AddTextComponentFormattedInteger

`ADD_TEXT_COMPONENT_FORMATTED_INTEGER` · hash `0x0E4C749FF9DE9CC4` · jhash `0x12929BDF` · **Cliente**

```lua
AddTextComponentFormattedInteger(value, commaSeparated)
```
```c
void ADD_TEXT_COMPONENT_FORMATTED_INTEGER(int value, BOOL commaSeparated);
```

**Parámetros**

- `value` (`int`): The integer to add to the string
- `commaSeparated` (`BOOL`): Whether or not to add comma seperators. So if true 1000 would become 1,000.

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0E4C749FF9DE9CC4` (`N_0x0e4c749ff9de9cc4`)

**Ejemplo (lua):**

```lua
-- on initialization
AddTextEntry('TEST_LABEL', '€~a~')

-- when drawing
BeginTextCommandThefeedPost('TEST_LABEL')
AddTextComponentFormattedInteger(1000, true)
EndTextCommandThefeedPostTicker(false, true)
```

---
### AddTextComponentInteger

`ADD_TEXT_COMPONENT_INTEGER` · hash `0x03B504CF259931BC` · jhash `0xFE272A57` · **Cliente**

```lua
AddTextComponentInteger(value)
```
```c
void ADD_TEXT_COMPONENT_INTEGER(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

---
### AddTextComponentSubstringBlipName

`ADD_TEXT_COMPONENT_SUBSTRING_BLIP_NAME` · hash `0x80EAD8E2E1D5D52E` · jhash `0x5DE98F0A` · **Cliente**

```lua
AddTextComponentSubstringBlipName(blip)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_BLIP_NAME(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x80EAD8E2E1D5D52E` (`N_0x80ead8e2e1d5d52e`)

---
### AddTextComponentSubstringKeyboardDisplay

`ADD_TEXT_COMPONENT_SUBSTRING_KEYBOARD_DISPLAY` · hash `0x5F68520888E69014` · jhash `0x0829A799` · **Cliente**

```lua
AddTextComponentSubstringKeyboardDisplay(string)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_KEYBOARD_DISPLAY(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Certain characters like `<` will have to be escaped using html entities (e.g. `&lt;`), otherwise the text wont display properly.

**Nombres antiguos (alias):** `_ADD_TEXT_COMPONENT_STRING3` (`AddTextComponentString3`), `_ADD_TEXT_COMPONENT_SCALEFORM` (`AddTextComponentScaleform`)

---
### AddTextComponentSubstringPhoneNumber

`ADD_TEXT_COMPONENT_SUBSTRING_PHONE_NUMBER` · hash `0x761B77454205A61D` · jhash `0x65E1D404` · **Cliente**

```lua
AddTextComponentSubstringPhoneNumber(p0, p1)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_PHONE_NUMBER(char* p0, int p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 was always -1
```

**Nombres antiguos (alias):** `0x761B77454205A61D` (`N_0x761b77454205a61d`), `_ADD_TEXT_COMPONENT_APP_TITLE` (`AddTextComponentAppTitle`)

---
### AddTextComponentSubstringPlayerName

`ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME` · hash `0x6C188BE134E074AA` · jhash `0x27A244D8` · **Cliente**

```lua
AddTextComponentSubstringPlayerName(text)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(char* text);
```

**Parámetros**

- `text` (`char*`): A string to add of up to 99 characters. This can contain additional `~` formatting directives.

**Devuelve:** `void`

**Descripción oficial:**

Adds an arbitrary string as a text component placeholder, replacing `~a~` in the current text command's text label.

See the documentation on text formatting for more information.

**Nombres antiguos (alias):** `_ADD_TEXT_COMPONENT_STRING` (`AddTextComponentString`)

**Ejemplo (lua):**

```lua
-- on initialization
AddTextEntry('TEST_LABEL', 'Label: ~a~')

-- when drawing
BeginTextCommandDisplayText('TEST_LABEL')
AddTextComponentSubstringPlayerName('Hello, World!')
EndTextCommandDisplayText(0.5, 0.5)
```

---
### AddTextComponentSubstringTextLabel

`ADD_TEXT_COMPONENT_SUBSTRING_TEXT_LABEL` · hash `0xC63CD5D2920ACBE7` · jhash `0xDCE05406` · **Cliente**

```lua
AddTextComponentSubstringTextLabel(labelName)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_TEXT_LABEL(char* labelName);
```

**Parámetros**

- `labelName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ADD_TEXT_COMPONENT_ITEM_STRING` (`AddTextComponentItemString`)

---
### AddTextComponentSubstringTextLabelHashKey

`ADD_TEXT_COMPONENT_SUBSTRING_TEXT_LABEL_HASH_KEY` · hash `0x17299B63C7683A2B` · jhash `0x150E03B6` · **Cliente**

```lua
AddTextComponentSubstringTextLabelHashKey(gxtEntryHash)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_TEXT_LABEL_HASH_KEY(Hash gxtEntryHash);
```

**Parámetros**

- `gxtEntryHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
It adds the localized text of the specified GXT entry name. Eg. if the argument is GET_HASH_KEY("ES_HELP"), adds "Continue". Just uses a text labels hash key  
```

**Nombres antiguos (alias):** `0x17299B63C7683A2B` (`N_0x17299b63c7683a2b`)

---
### AddTextComponentSubstringTime

`ADD_TEXT_COMPONENT_SUBSTRING_TIME` · hash `0x1115F16B8AB9E8BF` · jhash `0x135B3CD0` · **Cliente**

```lua
AddTextComponentSubstringTime(timestamp, format)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_TIME(int timestamp, int format);
```

**Parámetros**

- `timestamp` (`int`): The timestamp in milliseconds
- `format` (`int`): The format of the timestamp, as bitwise flags

**Devuelve:** `void`

**Descripción oficial:**

Takes a time in milliseconds and converts it to a string. Use `~a~` to mark the position in your line of text where you want this substring inserted.

```cpp
enum eTimeFormat {
    TEXT_FORMAT_MILLISECONDS = 1,
    TEXT_FORMAT_SECONDS = 2,
    TEXT_FORMAT_MINUTES = 4,
    TEXT_FORMAT_HOURS = 8,
    TEXT_FORMAT_DAYS = 16,
    // e.g. show 12:20 not 00:12:20
    TEXT_FORMAT_HIDE_LEADING_UNITS_EQUAL_TO_ZERO = 32,
    // e.g. show 1:14 not 01:14
    TEXT_FORMAT_HIDE_LEADING_ZEROS_ON_LEADING_UNITS = 64,
    // e.g. show 3m24s not 3:24
    TEXT_FORMAT_SHOW_UNIT_DIVIDERS_AS_LETTERS = 128,
    // e.g. show 3m24 not 3m24s
    TEXT_FORMAT_HIDE_UNIT_LETTER_FOR_SMALLEST_UNITS = 256,
    // e.g. show 05:51 not 05:519
    TEXT_FORMAT_HIDE_MILLISECONDS_UNITS_DIGIT = 512,
    // e.g. show 05:5 not 05:519
    TEXT_FORMAT_HIDE_MILLISECONDS_TENS_DIGIT = 1024,
    // e.g. show 12.345 not 12:345
    TEXT_FORMAT_USE_DOT_FOR_MILLISECOND_DIVIDER = 2048
}
```

**Ejemplo (lua):**

```lua
-- Renders the current game time in hours, minutes and seconds
local time = GetGameTimer()
AddTextEntry('TIME_LABEL', 'Game time: ~a~')
BeginTextCommandDisplayText("TIME_LABEL")
AddTextComponentSubstringTime(time, 2 | 4 | 8)
EndTextCommandDisplayText(0, 0)
```

---
### AddTextComponentSubstringWebsite

`ADD_TEXT_COMPONENT_SUBSTRING_WEBSITE` · hash `0x94CF4AC034C9C986` · jhash `0xC736999E` · **Cliente**

```lua
AddTextComponentSubstringWebsite(website)
```
```c
void ADD_TEXT_COMPONENT_SUBSTRING_WEBSITE(char* website);
```

**Parámetros**

- `website` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native (along with 0x5F68520888E69014 and 0x6C188BE134E074AA) do not actually filter anything. They simply add the provided text (as of 944)  
```

**Nombres antiguos (alias):** `_ADD_TEXT_COMPONENT_STRING2` (`AddTextComponentString2`)

---
### AllowDisplayOfMultiplayerCashText

`ALLOW_DISPLAY_OF_MULTIPLAYER_CASH_TEXT` · hash `0xE67C6DFD386EA5E7` · jhash `0x5476B9FD` · **Cliente**

```lua
AllowDisplayOfMultiplayerCashText(allow)
```
```c
void ALLOW_DISPLAY_OF_MULTIPLAYER_CASH_TEXT(BOOL allow);
```

**Parámetros**

- `allow` (`BOOL`): Toggles if MP Cash HUD displays 'Cash' and 'Bank' texts before the balance.

**Devuelve:** `void`

**Descripción oficial:**

Before:
![](https://imgur.com/a/RF1JHOS)
After:
![](https://imgur.com/a/Z8LnHHc)

**Nombres antiguos (alias):** `0xE67C6DFD386EA5E7` (`N_0xe67c6dfd386ea5e7`)

---
### AllowPauseMenuWhenDeadThisFrame

`_ALLOW_PAUSE_MENU_WHEN_DEAD_THIS_FRAME` · hash `0xCC3FDDED67BCFC63` · jhash `0x630CD8EE` · **Cliente**

```lua
AllowPauseMenuWhenDeadThisFrame()
```
```c
void _ALLOW_PAUSE_MENU_WHEN_DEAD_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Allows opening the pause menu this frame, when the player is dead.

**Nombres antiguos (alias):** `0xCC3FDDED67BCFC63` (`N_0xcc3fdded67bcfc63`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
	while true do
		N_0xcc3fdded67bcfc63()
		Wait(0)
	end
end)
```

---
### AllowSonarBlips

`ALLOW_SONAR_BLIPS` · hash `0x60734CC207C9833C` · jhash `0xE7E1E32B` · **Cliente**

```lua
AllowSonarBlips(toggle)
```
```c
void ALLOW_SONAR_BLIPS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x60734CC207C9833C` (`N_0x60734cc207c9833c`)

---
### BeginTextCommandBusyspinnerOn

`BEGIN_TEXT_COMMAND_BUSYSPINNER_ON` · hash `0xABA17D7CE615ADBF` · jhash `0xCB7C8994` · **Cliente**

```lua
BeginTextCommandBusyspinnerOn(string)
```
```c
void BEGIN_TEXT_COMMAND_BUSYSPINNER_ON(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Initializes the text entry for the the text next to a loading prompt. All natives for for building UI texts can be used here  
BEGIN_TEXT_COMMAND_PRINT  
e.g  
void StartLoadingMessage(char *text, int spinnerType = 3)  
	{  
_SET_LOADING_PROMPT_TEXT_ENTRY("STRING");  
ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);  
_SHOW_LOADING_PROMPT(spinnerType);  
	}  
/*OR*/  
	void ShowLoadingMessage(char *text, int spinnerType = 3, int timeMs = 10000)  
	{  
_SET_LOADING_PROMPT_TEXT_ENTRY("STRING");  
ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);  
_SHOW_LOADING_PROMPT(spinnerType);  
WAIT(timeMs);  
_REMOVE_LOADING_PROMPT();  
	}  
These are some localized strings used in the loading spinner.  
"PM_WAIT"                   = Please Wait  
"CELEB_WPLYRS"              = Waiting For Players.  
"CELL_SPINNER2"             = Scanning storage.  
"ERROR_CHECKYACHTNAME" = Registering your yacht's name. Please wait.  
"ERROR_CHECKPROFANITY"   = Checking your text for profanity. Please wait.  
"FM_COR_AUTOD"                        = Just spinner no text  
"FM_IHELP_WAT2"                        = Waiting for other players  
"FM_JIP_WAITO"                            = Game options are being set  
"FMMC_DOWNLOAD"                    = Downloading  
"FMMC_PLYLOAD"                         = Loading  
"FMMC_STARTTRAN"                    = Launching session  
"HUD_QUITTING"                           =  Quiting session  
"KILL_STRIP_IDM"                         = Waiting for to accept  
"MP_SPINLOADING"                      = Loading  
```

**Nombres antiguos (alias):** `0xABA17D7CE615ADBF` (`N_0xaba17d7ce615adbf`), `_SET_LOADING_PROMPT_TEXT_ENTRY` (`SetLoadingPromptTextEntry`), `_BEGIN_TEXT_COMMAND_BUSY_STRING` (`BeginTextCommandBusyString`)

---
### BeginTextCommandClearPrint

`BEGIN_TEXT_COMMAND_CLEAR_PRINT` · hash `0xE124FA80A759019C` · jhash `0x550665AE` · **Cliente**

```lua
BeginTextCommandClearPrint(text)
```
```c
void BEGIN_TEXT_COMMAND_CLEAR_PRINT(char* text);
```

**Parámetros**

- `text` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
clears a print text command with this text  
```

**Nombres antiguos (alias):** `0xE124FA80A759019C` (`N_0xe124fa80a759019c`)

---
### BeginTextCommandDisplayHelp

`BEGIN_TEXT_COMMAND_DISPLAY_HELP` · hash `0x8509B634FBE7DA11` · jhash `0xB245FC10` · **Cliente**

```lua
BeginTextCommandDisplayHelp(inputType)
```
```c
void BEGIN_TEXT_COMMAND_DISPLAY_HELP(char* inputType);
```

**Parámetros**

- `inputType` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used to be known as _SET_TEXT_COMPONENT_FORMAT  
```

**Nombres antiguos (alias):** `_SET_TEXT_COMPONENT_FORMAT` (`SetTextComponentFormat`)

---
### BeginTextCommandDisplayText

`BEGIN_TEXT_COMMAND_DISPLAY_TEXT` · hash `0x25FBB336DF1804CB` · jhash `0x3E35563E` · **Cliente**

```lua
BeginTextCommandDisplayText(text)
```
```c
void BEGIN_TEXT_COMMAND_DISPLAY_TEXT(char* text);
```

**Parámetros**

- `text` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
The following were found in the decompiled script files:  
STRING, TWOSTRINGS, NUMBER, PERCENTAGE, FO_TWO_NUM, ESMINDOLLA, ESDOLLA, MTPHPER_XPNO, AHD_DIST, CMOD_STAT_0, CMOD_STAT_1, CMOD_STAT_2, CMOD_STAT_3, DFLT_MNU_OPT, F3A_TRAFDEST, ES_HELP_SOC3  
ESDOLLA   
ESMINDOLLA - cash (negative)  
Used to be known as _SET_TEXT_ENTRY  
```

**Nombres antiguos (alias):** `_SET_TEXT_ENTRY` (`SetTextEntry`)

---
### BeginTextCommandGetWidth

`_BEGIN_TEXT_COMMAND_GET_WIDTH` · hash `0x54CE8AC98E120CAB` · jhash `0x51E7A037` · **Cliente**

```lua
BeginTextCommandGetWidth(text)
```
```c
void _BEGIN_TEXT_COMMAND_GET_WIDTH(char* text);
```

**Parámetros**

- `text` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
BEGIN_TEXT_COMMAND_*
Example:
_BEGIN_TEXT_COMMAND_GET_WIDTH("NUMBER");
ADD_TEXT_COMPONENT_FLOAT(69.420f, 2);
float width = _END_TEXT_COMMAND_GET_WIDTH(1);
```

**Nombres antiguos (alias):** `_SET_TEXT_ENTRY_FOR_WIDTH` (`SetTextEntryForWidth`), `_BEGIN_TEXT_COMMAND_WIDTH` (`BeginTextCommandWidth`)

---
### BeginTextCommandIsMessageDisplayed

`BEGIN_TEXT_COMMAND_IS_MESSAGE_DISPLAYED` · hash `0x853648FD1063A213` · jhash `0xDD524A11` · **Cliente**

```lua
BeginTextCommandIsMessageDisplayed(text)
```
```c
void BEGIN_TEXT_COMMAND_IS_MESSAGE_DISPLAYED(char* text);
```

**Parámetros**

- `text` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
nothin doin.   
BOOL Message(char* text)  
	{  
BEGIN_TEXT_COMMAND_IS_MESSAGE_DISPLAYED("STRING");  
ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);  
return END_TEXT_COMMAND_IS_MESSAGE_DISPLAYED();  
	}  
```

**Nombres antiguos (alias):** `0x853648FD1063A213` (`N_0x853648fd1063a213`)

---
### BeginTextCommandIsThisHelpMessageBeingDisplayed

`BEGIN_TEXT_COMMAND_IS_THIS_HELP_MESSAGE_BEING_DISPLAYED` · hash `0x0A24DA3A41B718F5` · jhash `0x00E20F2D` · **Cliente**

```lua
BeginTextCommandIsThisHelpMessageBeingDisplayed(labelName)
```
```c
void BEGIN_TEXT_COMMAND_IS_THIS_HELP_MESSAGE_BEING_DISPLAYED(char* labelName);
```

**Parámetros**

- `labelName` (`char*`): Text entry name. This can be created using [`AddTextEntry`](../cfx/cliente-1.md#addtextentry).

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0A24DA3A41B718F5` (`N_0x0a24da3a41b718f5`)

**Ejemplo (lua):**

```lua
-- Create new text entry
AddTextEntry('TEST_LABEL', 'Hello world.')

-- Draw help message
BeginTextCommandDisplayHelp('TEST_LABEL')
EndTextCommandDisplayHelp(0, false, true, -1)

-- Test if the message has been displayed
BeginTextCommandIsThisHelpMessageBeingDisplayed("TEST_LABEL")
local isDisplayed = EndTextCommandIsThisHelpMessageBeingDisplayed(0)
```

---
### BeginTextCommandLineCount

`_BEGIN_TEXT_COMMAND_LINE_COUNT` · hash `0x521FB041D93DD0E4` · jhash `0x94B82066` · **Cliente**

```lua
BeginTextCommandLineCount(entry)
```
```c
void _BEGIN_TEXT_COMMAND_LINE_COUNT(char* entry);
```

**Parámetros**

- `entry` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
get's line count  
int GetLineCount(char *text, float x, float y)  
	{  
_BEGIN_TEXT_COMMAND_LINE_COUNT("STRING");  
                ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);  
return _END_TEXT_COMMAND_GET_LINE_COUNT(x, y);  
	}  
```

**Nombres antiguos (alias):** `_SET_TEXT_GXT_ENTRY` (`SetTextGxtEntry`)

---
### BeginTextCommandObjective

`_BEGIN_TEXT_COMMAND_OBJECTIVE` · hash `0x23D69E0465570028` · jhash `0x0E103475` · **Cliente**

```lua
BeginTextCommandObjective(p0)
```
```c
void _BEGIN_TEXT_COMMAND_OBJECTIVE(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x23D69E0465570028` (`N_0x23d69e0465570028`)

---
### BeginTextCommandOverrideButtonText

`BEGIN_TEXT_COMMAND_OVERRIDE_BUTTON_TEXT` · hash `0x8F9EE5687F8EECCD` · jhash `0xBF855650` · **Cliente**

```lua
BeginTextCommandOverrideButtonText(gxtEntry)
```
```c
void BEGIN_TEXT_COMMAND_OVERRIDE_BUTTON_TEXT(char* gxtEntry);
```

**Parámetros**

- `gxtEntry` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8F9EE5687F8EECCD` (`N_0x8f9ee5687f8eeccd`), `_BEGIN_TEXT_COMMAND_TIMER` (`BeginTextCommandTimer`)

---
### BeginTextCommandPrint

`BEGIN_TEXT_COMMAND_PRINT` · hash `0xB87A37EEB7FAA67D` · jhash `0xF42C43C7` · **Cliente**

```lua
BeginTextCommandPrint(GxtEntry)
```
```c
void BEGIN_TEXT_COMMAND_PRINT(char* GxtEntry);
```

**Parámetros**

- `GxtEntry` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used to be known as _SET_TEXT_ENTRY_2  
void ShowSubtitle(char *text)  
{  
	BEGIN_TEXT_COMMAND_PRINT("STRING");  
	ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);  
	END_TEXT_COMMAND_PRINT(2000, 1);  
}  
```

**Nombres antiguos (alias):** `_SET_TEXT_ENTRY_2` (`SetTextEntry_2`)

---
### BeginTextCommandSetBlipName

`BEGIN_TEXT_COMMAND_SET_BLIP_NAME` · hash `0xF9113A30DE5C6670` · jhash `0xF4C211F6` · **Cliente**

```lua
BeginTextCommandSetBlipName(textLabel)
```
```c
void BEGIN_TEXT_COMMAND_SET_BLIP_NAME(char* textLabel);
```

**Parámetros**

- `textLabel` (`char*`): The text label to set.

**Devuelve:** `void`

**Descripción oficial:**

Starts a text command to change the name of a blip displayed in the pause menu.

This should be paired with [`END_TEXT_COMMAND_SET_BLIP_NAME`](#endtextcommandsetblipname), once adding all required text components.

**Ejemplo (lua):**

```lua
-- creates a blip called 'Food for me!' at 0.0, 0.0, 0.0
AddTextEntry('MYBLIP', 'Food for ~a~!')

local blip = AddBlipForCoord(0.0, 0.0, 0.0)
BeginTextCommandSetBlipName('MYBLIP')
AddTextComponentSubstringPlayerName('me')
EndTextCommandSetBlipName(blip)
```

---
### BeginTextCommandThefeedPost

`BEGIN_TEXT_COMMAND_THEFEED_POST` · hash `0x202709F4C58A0424` · jhash `0x574EE85C` · **Cliente**

```lua
BeginTextCommandThefeedPost(text)
```
```c
void BEGIN_TEXT_COMMAND_THEFEED_POST(char* text);
```

**Parámetros**

- `text` (`char*`): The text label to use.

**Devuelve:** `void`

**Descripción oficial:**

Declares the entry type of a notification, for example "STRING".
int ShowNotification(char \*text)
{
BEGIN_TEXT_COMMAND_THEFEED_POST("STRING");
ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);
return \_DRAW_NOTIFICATION(1, 1);
}

**Nombres antiguos (alias):** `_SET_NOTIFICATION_TEXT_ENTRY` (`SetNotificationTextEntry`)

**Ejemplo (lua):**

```lua
BeginTextCommandThefeedPost("STRING")
AddTextComponentSubstringPlayerName("Hello " .. GetPlayerName(PlayerId()) .. ".")
EndTextCommandThefeedPostTicker(true, true)
```

---
### BusyspinnerIsDisplaying

`BUSYSPINNER_IS_DISPLAYING` · hash `0xB2A592B04648A9CB` · jhash `0x3AF34DEF` · **Cliente**

```lua
local retval = BusyspinnerIsDisplaying()
```
```c
BOOL BUSYSPINNER_IS_DISPLAYING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB2A592B04648A9CB` (`N_0xb2a592b04648a9cb`)

---
### BusyspinnerIsOn

`BUSYSPINNER_IS_ON` · hash `0xD422FCC5F239A915` · jhash `0xB8B3A5D0` · **Cliente**

```lua
local retval = BusyspinnerIsOn()
```
```c
BOOL BUSYSPINNER_IS_ON();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD422FCC5F239A915` (`N_0xd422fcc5f239a915`), `_IS_LOADING_PROMPT_BEING_DISPLAYED` (`IsLoadingPromptBeingDisplayed`)

---
### BusyspinnerOff

`BUSYSPINNER_OFF` · hash `0x10D373323E5B9C0D` · jhash `0x94119534` · **Cliente**

```lua
BusyspinnerOff()
```
```c
void BUSYSPINNER_OFF();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Removes the loading prompt at the bottom right of the screen.
```

**Nombres antiguos (alias):** `0x10D373323E5B9C0D` (`N_0x10d373323e5b9c0d`), `_REMOVE_LOADING_PROMPT` (`RemoveLoadingPrompt`)

---
### ChangeFakeMpCash

`CHANGE_FAKE_MP_CASH` · hash `0x0772DF77852C2E30` · jhash `0xE319F90B` · **Cliente**

```lua
ChangeFakeMpCash(cash, bank)
```
```c
void CHANGE_FAKE_MP_CASH(int cash, int bank);
```

**Parámetros**

- `cash` (`int`)
- `bank` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Displays cash change notifications on HUD.  
```

**Nombres antiguos (alias):** `_SET_SINGLEPLAYER_HUD_CASH` (`SetSingleplayerHudCash`), `_SET_PLAYER_CASH_CHANGE` (`SetPlayerCashChange`)

---
### ClearAdditionalText

`CLEAR_ADDITIONAL_TEXT` · hash `0x2A179DF17CCF04CD` · jhash `0x518141E0` · **Cliente**

```lua
ClearAdditionalText(p0, p1)
```
```c
void CLEAR_ADDITIONAL_TEXT(int p0, BOOL p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### ClearAllBlipRoutes

`_CLEAR_ALL_BLIP_ROUTES` · hash `0xD12882D3FF82BF11` · **Cliente**

```lua
ClearAllBlipRoutes()
```
```c
void _CLEAR_ALL_BLIP_ROUTES();
```

**Devuelve:** `void`

**Descripción oficial:**

Clears all active blip routes that have been set with [`SetBlipRoute`](#setbliproute).

**Nombres antiguos (alias):** `0xD12882D3FF82BF11` (`N_0xd12882d3ff82bf11`)

---
### ClearAllHelpMessages

`CLEAR_ALL_HELP_MESSAGES` · hash `0x6178F68A87A4D3A0` · jhash `0x9E5D9198` · **Cliente**

```lua
ClearAllHelpMessages()
```
```c
void CLEAR_ALL_HELP_MESSAGES();
```

**Devuelve:** `void`

---
### ClearBrief

`CLEAR_BRIEF` · hash `0x9D292F73ADBD9313` · jhash `0x9F75A929` · **Cliente**

```lua
ClearBrief()
```
```c
void CLEAR_BRIEF();
```

**Devuelve:** `void`

---
### ClearDynamicPauseMenuErrorMessage

`CLEAR_DYNAMIC_PAUSE_MENU_ERROR_MESSAGE` · hash `0x7792424AA0EAC32E` · jhash `0x2F9A309C` · **Cliente**

```lua
ClearDynamicPauseMenuErrorMessage()
```
```c
void CLEAR_DYNAMIC_PAUSE_MENU_ERROR_MESSAGE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7792424AA0EAC32E` (`N_0x7792424aa0eac32e`)

---
### ClearFloatingHelp

`CLEAR_FLOATING_HELP` · hash `0x50085246ABD3FEFA` · jhash `0xB181F88F` · **Cliente**

```lua
ClearFloatingHelp(hudIndex, p1)
```
```c
void CLEAR_FLOATING_HELP(int hudIndex, BOOL p1);
```

**Parámetros**

- `hudIndex` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### ClearGpsCustomRoute

`CLEAR_GPS_CUSTOM_ROUTE` · hash `0xE6DE0561D9232A64` · jhash `0xCF2E3E24` · **Cliente**

```lua
ClearGpsCustomRoute()
```
```c
void CLEAR_GPS_CUSTOM_ROUTE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE6DE0561D9232A64` (`N_0xe6de0561d9232a64`)

---
### ClearGpsFlags

`CLEAR_GPS_FLAGS` · hash `0x21986729D6A3A830` · jhash `0x056AFCE6` · **Cliente**

```lua
ClearGpsFlags()
```
```c
void CLEAR_GPS_FLAGS();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Clears the GPS flags. Only the script that originally called SET_GPS_FLAGS can clear them.  
Doesn't seem like the flags are actually read by the game at all.  
```

---
### ClearGpsMultiRoute

`CLEAR_GPS_MULTI_ROUTE` · hash `0x67EEDEA1B9BAFD94` · jhash `0x0D9969E4` · **Cliente**

```lua
ClearGpsMultiRoute()
```
```c
void CLEAR_GPS_MULTI_ROUTE();
```

**Devuelve:** `void`

**Descripción oficial:**

Does the same as [`SET_GPS_MULTI_ROUTE_RENDER(false)`](#setgpsmultirouterender)

**Nombres antiguos (alias):** `0x67EEDEA1B9BAFD94` (`N_0x67eedea1b9bafd94`)

---
### ClearGpsPlayerWaypoint

`CLEAR_GPS_PLAYER_WAYPOINT` · hash `0xFF4FB7C8CDFA3DA7` · jhash `0x0B9C7FC2` · **Cliente**

```lua
ClearGpsPlayerWaypoint()
```
```c
void CLEAR_GPS_PLAYER_WAYPOINT();
```

**Devuelve:** `void`

---
### ClearGpsRaceTrack

`CLEAR_GPS_RACE_TRACK` · hash `0x7AA5B4CE533C858B` · jhash `0x40C59829` · **Cliente**

```lua
ClearGpsRaceTrack()
```
```c
void CLEAR_GPS_RACE_TRACK();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Does the same as SET_RACE_TRACK_RENDER(false);
```

---
### ClearHelp

`CLEAR_HELP` · hash `0x8DFCED7A656F8802` · jhash `0xE6D85741` · **Cliente**

```lua
ClearHelp(toggle)
```
```c
void CLEAR_HELP(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### ClearPedInPauseMenu

`CLEAR_PED_IN_PAUSE_MENU` · hash `0x5E62BE5DC58E9E06` · jhash `0x28058ACF` · **Cliente**

```lua
ClearPedInPauseMenu()
```
```c
void CLEAR_PED_IN_PAUSE_MENU();
```

**Devuelve:** `void`

---
### ClearPrints

`CLEAR_PRINTS` · hash `0xCC33FA791322B9D9` · jhash `0x216CB1C5` · **Cliente**

```lua
ClearPrints()
```
```c
void CLEAR_PRINTS();
```

**Devuelve:** `void`

---
### ClearRaceGalleryBlips

`_CLEAR_RACE_GALLERY_BLIPS` · hash `0x2708FC083123F9FF` · jhash `0xCBEC9369` · **Cliente**

```lua
ClearRaceGalleryBlips()
```
```c
void _CLEAR_RACE_GALLERY_BLIPS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2708FC083123F9FF` (`N_0x2708fc083123f9ff`)

---
### ClearReminderMessage

`CLEAR_REMINDER_MESSAGE` · hash `0xB57D8DD645CFA2CF` · jhash `0x5BBCC934` · **Cliente**

```lua
ClearReminderMessage()
```
```c
void CLEAR_REMINDER_MESSAGE();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

**Nombres antiguos (alias):** `0xB57D8DD645CFA2CF` (`N_0xb57d8dd645cfa2cf`)

---
### ClearSmallPrints

`CLEAR_SMALL_PRINTS` · hash `0x2CEA2839313C09AC` · jhash `0xA869A238` · **Cliente**

```lua
ClearSmallPrints()
```
```c
void CLEAR_SMALL_PRINTS();
```

**Devuelve:** `void`

---
### ClearThisPrint

`CLEAR_THIS_PRINT` · hash `0xCF708001E1E536DD` · jhash `0x06878327` · **Cliente**

```lua
ClearThisPrint(p0)
```
```c
void CLEAR_THIS_PRINT(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
p0: found arguments in the b617d scripts: pastebin.com/X5akCN7z  
```

---
### CloseMultiplayerChat

`_CLOSE_MULTIPLAYER_CHAT` · hash `0x1AC8F4AD40E22127` · **Cliente**

```lua
CloseMultiplayerChat()
```
```c
void _CLOSE_MULTIPLAYER_CHAT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ABORT_TEXT_CHAT` (`AbortTextChat`)

---
### CloseSocialClubMenu

`CLOSE_SOCIAL_CLUB_MENU` · hash `0xD2B32BE3FC1626C6` · jhash `0x5F86AA39` · **Cliente**

```lua
CloseSocialClubMenu()
```
```c
void CLOSE_SOCIAL_CLUB_MENU();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD2B32BE3FC1626C6` (`N_0xd2b32be3fc1626c6`)

---
### CreateFakeMpGamerTag

`CREATE_FAKE_MP_GAMER_TAG` · hash `0xBFEFE3321A3F5015` · jhash `0xF5CD2AA4` · **Cliente**

```lua
local retval = CreateFakeMpGamerTag(ped, username, crewIsPrivate, crewIsRockstar, crewName, crewRank)
```
```c
int CREATE_FAKE_MP_GAMER_TAG(Ped ped, char* username, BOOL crewIsPrivate, BOOL crewIsRockstar, char* crewName, int crewRank);
```

**Parámetros**

- `ped` (`Ped`): The ped that the fake gamer tag will be attached to.
- `username` (`char*`): The name displayed on the gamer tag.
- `crewIsPrivate` (`BOOL`): If the crew is private. Public crews have a pointed end cap, private crews do not.
- `crewIsRockstar` (`BOOL`): If the crew is a Rockstar crew. Rockstar crews include a Rockstar logo before the name.
- `crewName` (`char*`): The name of the crew.
- `crewRank` (`int`): The rank from 1-5 that the player is within the crew. Use 0 if the player is the founder of the crew. Only relevant for private crews.

**Devuelve:** `int` — The ID of the new gamer tag.

**Descripción oficial:**

As per the name, this native creates a "fake" gamer tag that is attached to a specific ped.
Unlike "real" gamer tags, you cannot set the crew colour of these gamer tags.

To create gamer tags for actual players and for more gamer tag information, see [CREATE_MP_GAMER_TAG_WITH_CREW_COLOR](#creatempgamertagwithcrewcolor).

**Nombres antiguos (alias):** `0xBFEFE3321A3F5015` (`N_0xbfefe3321a3f5015`), `_CREATE_MP_GAMER_TAG` (`CreateMpGamerTag`)

---
### CreateMpGamerTagWithCrewColor

`CREATE_MP_GAMER_TAG_WITH_CREW_COLOR` · hash `0x6DD05E9D83EFA4C9` · jhash `0xC969F2D0` · **Cliente**

```lua
CreateMpGamerTagWithCrewColor(player, username, crewIsPrivate, crewIsRockstar, crewName, crewRank, crewR, crewG, crewB)
```
```c
void CREATE_MP_GAMER_TAG_WITH_CREW_COLOR(Player player, char* username, BOOL crewIsPrivate, BOOL crewIsRockstar, char* crewName, int crewRank, int crewR, int crewG, int crewB);
```

**Parámetros**

- `player` (`Player`): The local player ID to assign the gamer tag to.
- `username` (`char*`): The name displayed on the gamer tag.
- `crewIsPrivate` (`BOOL`): If the crew is private. Public crews have a pointed end cap, private crews do not.
- `crewIsRockstar` (`BOOL`): If the crew is a Rockstar crew. Rockstar crews include a Rockstar logo before the name.
- `crewName` (`char*`): The name of the crew.
- `crewRank` (`int`): The rank from 1-5 that the player is within the crew. Use 0 if the player is the founder of the crew. Only relevant for private crews.
- `crewR` (`int`): Red component of the crew colour.
- `crewG` (`int`): Green component of the crew colour.
- `crewB` (`int`): Blue component of the crew colour.

**Devuelve:** `void`

**Descripción oficial:**

Creates a gamer tag for the specified local player ID, automatically attached to the player's current ped.
The created gamer tag will have the same ID as the player. You can use [IS_MP_GAMER_TAG_ACTIVE](#ismpgamertagactive) to check if a gamer tag already exists for a player.
After the gamer tag is created, all components will be set as invisible. Use [SET_MP_GAMER_TAG_VISIBILITY](#setmpgamertagvisibility) to change the visibility of individual components or [\_SET_MP_GAMER_TAG_VISIBILITY_ALL](#setmpgamertagvisibilityall) to set all of them at once.

To create a gamer tag for a ped that is not a player, see [CREATE_FAKE_MP_GAMER_TAG](#createfakempgamertag).

**Nombres antiguos (alias):** `0x6DD05E9D83EFA4C9` (`N_0x6dd05e9d83efa4c9`), `_CREATE_MP_GAMER_TAG_COLOR` (`CreateMpGamerTagColor`), `_SET_MP_GAMER_TAG_COLOR` (`SetMpGamerTagColor`), `_CREATE_MP_GAMER_TAG_FOR_NET_PLAYER` (`CreateMpGamerTagForNetPlayer`)

**Ejemplo (lua):**

```lua
local playerId = PlayerId() -- you can use any local player ID here

-- clear any already existing gamer tag associated with this player
if IsMpGamerTagActive(playerId) then
	RemoveMpGamerTag(playerId)

	-- wait until the gamer tag actually becomes free
	repeat Wait(0) until IsMpGamerTagFree(playerId)
end

-- create the gamer tag
CreateMpGamerTagWithCrewColor(playerId, "jaymoo", false, true, "RSG", 0, 200, 0, 200)

-- set the name, crew and typing indicator components as visible
SetMpGamerTagVisibility(playerId, 0, true)
SetMpGamerTagVisibility(playerId, 1, true)
SetMpGamerTagVisibility(playerId, 16, true)
```

---
### DeleteWaypointsFromThisPlayer

`DELETE_WAYPOINTS_FROM_THIS_PLAYER` · hash `0xD8E694757BCEA8E9` · jhash `0x62BABF2C` · **Cliente**

```lua
DeleteWaypointsFromThisPlayer()
```
```c
void DELETE_WAYPOINTS_FROM_THIS_PLAYER();
```

**Devuelve:** `void`

**Descripción oficial:**

Same as [`SET_WAYPOINT_OFF`](#setwaypointoff), except it checks if the local player is the owner of the waypoint.

**Nombres antiguos (alias):** `0xD8E694757BCEA8E9` (`N_0xd8e694757bcea8e9`), `_DELETE_WAYPOINT` (`DeleteWaypoint`)

---
### DisableFrontendThisFrame

`DISABLE_FRONTEND_THIS_FRAME` · hash `0x6D3465A73092F0E6` · jhash `0xD86A029E` · **Cliente**

```lua
DisableFrontendThisFrame()
```
```c
void DISABLE_FRONTEND_THIS_FRAME();
```

**Devuelve:** `void`

---
### DisableMultiplayerChat

`_DISABLE_MULTIPLAYER_CHAT` · hash `0x1DB21A44B09E8BA3` · **Cliente**

```lua
DisableMultiplayerChat(disable)
```
```c
void _DISABLE_MULTIPLAYER_CHAT(BOOL disable);
```

**Parámetros**

- `disable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

If true is passed, the player won't be able to open the multiplayer chat

**Nombres antiguos (alias):** `_SET_TEXT_CHAT_UNK` (`SetTextChatUnk`)

---
### DisplayAmmoThisFrame

`DISPLAY_AMMO_THIS_FRAME` · hash `0xA5E78BA2B1331C55` · jhash `0x60693CEE` · **Cliente**

```lua
DisplayAmmoThisFrame(display)
```
```c
void DISPLAY_AMMO_THIS_FRAME(BOOL display);
```

**Parámetros**

- `display` (`BOOL`)

**Devuelve:** `void`

---
### DisplayAreaName

`DISPLAY_AREA_NAME` · hash `0x276B6CE369C33678` · jhash `0x489FDD41` · **Cliente**

```lua
DisplayAreaName(toggle)
```
```c
void DISPLAY_AREA_NAME(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### DisplayCash

`DISPLAY_CASH` · hash `0x96DEC8D5430208B7` · jhash `0x0049DF83` · **Cliente**

```lua
DisplayCash(display)
```
```c
void DISPLAY_CASH(BOOL display);
```

**Parámetros**

- `display` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
"DISPLAY_CASH(true);" makes the cash amount render on the screen when appropriate  
"DISPLAY_CASH(false);" disables cash amount rendering  
```

---
### DisplayHelpTextThisFrame

`DISPLAY_HELP_TEXT_THIS_FRAME` · hash `0x960C9FF8F616E41C` · jhash `0x18E3360A` · **Cliente**

```lua
DisplayHelpTextThisFrame(pTextLabel, bCurvedWindow)
```
```c
void DISPLAY_HELP_TEXT_THIS_FRAME(char* pTextLabel, BOOL bCurvedWindow);
```

**Parámetros**

- `pTextLabel` (`char*`): Text label for this message.
- `bCurvedWindow` (`BOOL`): Unused parameter.

**Devuelve:** `void`

**Descripción oficial:**

Shows a help message for one frame.
Do note that this message doesn't get added to the Pause Menu info section.

---
### DisplayHud

`DISPLAY_HUD` · hash `0xA6294919E56FF02A` · jhash `0xD10E4E31` · **Cliente**

```lua
DisplayHud(toggle)
```
```c
void DISPLAY_HUD(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If Hud should be displayed  
```

---
### DisplayHudWhenDeadThisFrame

`_DISPLAY_HUD_WHEN_DEAD_THIS_FRAME` · hash `0x7669F9E39DC17063` · jhash `0xC380AC85` · **Cliente**

```lua
DisplayHudWhenDeadThisFrame()
```
```c
void _DISPLAY_HUD_WHEN_DEAD_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Enables drawing some hud components, such as help labels, this frame, when the player is dead.

**Nombres antiguos (alias):** `0x7669F9E39DC17063` (`N_0x7669f9e39dc17063`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
	while true do
		N_0x7669f9e39dc17063()
		Wait(0)
	end
end)
```

---
### DisplayHudWhenPausedThisFrame

`DISPLAY_HUD_WHEN_PAUSED_THIS_FRAME` · hash `0x402F9ED62087E898` · jhash `0xC47AB1B0` · **Cliente**

```lua
DisplayHudWhenPausedThisFrame()
```
```c
void DISPLAY_HUD_WHEN_PAUSED_THIS_FRAME();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x402F9ED62087E898` (`N_0x402f9ed62087e898`)

---
### DisplayPlayerNameTagsOnBlips

`DISPLAY_PLAYER_NAME_TAGS_ON_BLIPS` · hash `0x82CEDC33687E1F50` · jhash `0x2F28F0A6` · **Cliente**

```lua
DisplayPlayerNameTagsOnBlips(toggle)
```
```c
void DISPLAY_PLAYER_NAME_TAGS_ON_BLIPS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): the toggle boolean

**Devuelve:** `void`

**Descripción oficial:**

Toggles whether or not name labels are shown on the expanded minimap next to player blips, like in GTA:O.
Doesn't need to be called every frame.
Make sure to call SET_BLIP_CATEGORY with index 7 for this to work on the desired blip.

**Nombres antiguos (alias):** `0x82CEDC33687E1F50` (`N_0x82cedc33687e1f50`)

---
### DisplayRadar

`DISPLAY_RADAR` · hash `0xA0EBB943C300E693` · jhash `0x52816BD4` · **Cliente**

```lua
DisplayRadar(toggle)
```
```c
void DISPLAY_RADAR(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If Minimap / Radar should be displayed.
```

---
### DisplaySniperScopeThisFrame

`DISPLAY_SNIPER_SCOPE_THIS_FRAME` · hash `0x73115226F4814E62` · jhash `0xBC6C73CB` · **Cliente**

```lua
DisplaySniperScopeThisFrame()
```
```c
void DISPLAY_SNIPER_SCOPE_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Displays the crosshair for this frame.  
```

---
### DoesBlipExist

`DOES_BLIP_EXIST` · hash `0xA6DB27D19ECBB7DA` · jhash `0xAE92DD96` · **Cliente**

```lua
local retval = DoesBlipExist(blip)
```
```c
BOOL DOES_BLIP_EXIST(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `BOOL`

---
### DoesBlipHaveGpsRoute

`DOES_BLIP_HAVE_GPS_ROUTE` · hash `0xDD2238F57B977751` · jhash `0x3E47F357` · **Cliente**

```lua
local retval = DoesBlipHaveGpsRoute(blip)
```
```c
BOOL DOES_BLIP_HAVE_GPS_ROUTE(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDD2238F57B977751` (`N_0xdd2238f57b977751`)

---
### DoesPedHaveAiBlip

`DOES_PED_HAVE_AI_BLIP` · hash `0x15B8ECF844EE67ED` · jhash `0x3BE1257F` · **Cliente**

```lua
local retval = DoesPedHaveAiBlip(ped)
```
```c
BOOL DOES_PED_HAVE_AI_BLIP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the ped's blip is controlled by the game.   
It's the default blip you can see on enemies during freeroam in singleplayer (the one that fades out quickly).  
```

---
### DoesTextBlockExist

`DOES_TEXT_BLOCK_EXIST` · hash `0x1C7302E725259789` · jhash `0x96F74838` · **Cliente**

```lua
local retval = DoesTextBlockExist(gxt)
```
```c
BOOL DOES_TEXT_BLOCK_EXIST(char* gxt);
```

**Parámetros**

- `gxt` (`char*`)

**Devuelve:** `BOOL`

---
### DoesTextLabelExist

`DOES_TEXT_LABEL_EXIST` · hash `0xAC09CA973C564252` · jhash `0x6ECAE560` · **Cliente**

```lua
local retval = DoesTextLabelExist(gxt)
```
```c
BOOL DOES_TEXT_LABEL_EXIST(char* gxt);
```

**Parámetros**

- `gxt` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if the passed gxt name exists in the game files.  
```

---
### DontTiltMinimapThisFrame

`DONT_TILT_MINIMAP_THIS_FRAME` · hash `0x6D14BFDC33B34F55` · jhash `0x334EFD46` · **Cliente**

```lua
DontTiltMinimapThisFrame()
```
```c
void DONT_TILT_MINIMAP_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
When calling this, the current frame will have the players "arrow icon" be focused on the dead center of the radar.
```

**Nombres antiguos (alias):** `_CENTER_PLAYER_ON_RADAR_THIS_FRAME` (`CenterPlayerOnRadarThisFrame`)

---
### DrawHudOverFadeThisFrame

`DRAW_HUD_OVER_FADE_THIS_FRAME` · hash `0xBF4F34A85CA2970C` · jhash `0x317775DF` · **Cliente**

```lua
DrawHudOverFadeThisFrame()
```
```c
void DRAW_HUD_OVER_FADE_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Allows HUD to be drawn over screen fade every frame this function is called.

**Nombres antiguos (alias):** `0xBF4F34A85CA2970C` (`N_0xbf4f34a85ca2970c`)

---
### EndTextCommandBusyspinnerOn

`END_TEXT_COMMAND_BUSYSPINNER_ON` · hash `0xBD12F8228410D9B4` · jhash `0x903F5EE4` · **Cliente**

```lua
EndTextCommandBusyspinnerOn(busySpinnerType)
```
```c
void END_TEXT_COMMAND_BUSYSPINNER_ON(int busySpinnerType);
```

**Parámetros**

- `busySpinnerType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eBusySpinnerType
{
	BUSY_SPINNER_LEFT = 0,
	BUSY_SPINNER_LEFT_2 = 1,
	BUSY_SPINNER_LEFT_3 = 2,
	BUSY_SPINNER_SAVE = 3,
	BUSY_SPINNER_RIGHT = 4,
};
```

**Nombres antiguos (alias):** `0xBD12F8228410D9B4` (`N_0xbd12f8228410d9b4`), `_SHOW_LOADING_PROMPT` (`ShowLoadingPrompt`), `_END_TEXT_COMMAND_BUSY_STRING` (`EndTextCommandBusyString`)

---
### EndTextCommandClearPrint

`END_TEXT_COMMAND_CLEAR_PRINT` · hash `0xFCC75460ABA29378` · jhash `0x67785AF2` · **Cliente**

```lua
EndTextCommandClearPrint()
```
```c
void END_TEXT_COMMAND_CLEAR_PRINT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFCC75460ABA29378` (`N_0xfcc75460aba29378`)

---
### EndTextCommandDisplayHelp

`END_TEXT_COMMAND_DISPLAY_HELP` · hash `0x238FFE5C7B0498A6` · jhash `0xB59B530D` · **Cliente**

```lua
EndTextCommandDisplayHelp(shape, loop, beep, duration)
```
```c
void END_TEXT_COMMAND_DISPLAY_HELP(int shape, BOOL loop, BOOL beep, int duration);
```

**Parámetros**

- `shape` (`int`): 0 for a normal rectangle shape, 1 and 2 has rounded edges, and can be used for floating help text hud component `FLOATING_HELP_TEXT_1` and `FLOATING_HELP_TEXT_2`. Use 1 for `FLOATING_HELP_TEXT_1` and 2 for `FLOATING_HELP_TEXT_2`, otherwise the help text will be reset to a normal help text on the top left corner on your screen.
- `loop` (`BOOL`): If this is true, the message will stay forever unless you call [`CLEAR_ALL_HELP_MESSAGES`](#clearallhelpmessages).
- `beep` (`BOOL`): If this is true, the beeping sound will play. Beeping sound name is `INFO` in sound set `HUD_FRONTEND_DEFAULT_SOUNDSET`.
- `duration` (`int`): Duration in ms of how long this help message should display for. -1 for default.

**Devuelve:** `void`

**Nombres antiguos (alias):** `_DISPLAY_HELP_TEXT_FROM_STRING_LABEL` (`DisplayHelpTextFromStringLabel`)

**Ejemplo (lua):**

```lua
-- Help texts support text formatting, check out https://docs.fivem.net/docs/game-references/text-formatting/
AddTextEntry('HelpMsg', 'Press ~INPUT_CONTEXT~ to do something.')

BeginTextCommandDisplayHelp('HelpMsg')
EndTextCommandDisplayHelp(0, false, true, -1)

-- Shows a floating help text which uses FLOATING_HELP_TEXT_1 hud component.
AddTextEntry('FloatingHelpText', 'Press E to show respect.')
SetFloatingHelpTextWorldPosition(0, vector3(100, 100, 100))
SetFloatingHelpTextStyle(0, true, 2, -1, 3, 0)
BeginTextCommandDisplayHelp('FloatingHelpText')
EndTextCommandDisplayHelp(1, false, false, -1)
```

---
### EndTextCommandDisplayText

`END_TEXT_COMMAND_DISPLAY_TEXT` · hash `0xCD015E5BB0D96A57` · jhash `0x6F8350CE` · **Cliente**

```lua
EndTextCommandDisplayText(x, y)
```
```c
void END_TEXT_COMMAND_DISPLAY_TEXT(float x, float y);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
After applying the properties to the text (See UI::SET_TEXT_), this will draw the text in the applied position. Also 0.0f < x, y < 1.0f, percentage of the axis.  
```

```
NativeDB Added Parameter 3: int p2
```

**Nombres antiguos (alias):** `_DRAW_TEXT` (`DrawText`)

---
### EndTextCommandGetWidth

`_END_TEXT_COMMAND_GET_WIDTH` · hash `0x85F061DA64ED2F67` · jhash `0xD12A643A` · **Cliente**

```lua
local retval = EndTextCommandGetWidth(p0)
```
```c
float _END_TEXT_COMMAND_GET_WIDTH(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `float`

**Descripción oficial:**

```
END_TEXT_COMMAND_*
In scripts font most of the time is passed as 1.
Use _BEGIN_TEXT_GET_COMMAND_GET_WIDTH
param is not font from what i've tested
```

**Nombres antiguos (alias):** `_GET_TEXT_SCREEN_WIDTH` (`GetTextScreenWidth`)

---
### EndTextCommandIsMessageDisplayed

`END_TEXT_COMMAND_IS_MESSAGE_DISPLAYED` · hash `0x8A9BA1AB3E237613` · jhash `0x672EFB45` · **Cliente**

```lua
local retval = EndTextCommandIsMessageDisplayed()
```
```c
BOOL END_TEXT_COMMAND_IS_MESSAGE_DISPLAYED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8A9BA1AB3E237613` (`N_0x8a9ba1ab3e237613`)

---
### EndTextCommandIsThisHelpMessageBeingDisplayed

`END_TEXT_COMMAND_IS_THIS_HELP_MESSAGE_BEING_DISPLAYED` · hash `0x10BDDBFC529428DD` · jhash `0xF63A13EC` · **Cliente**

```lua
local retval = EndTextCommandIsThisHelpMessageBeingDisplayed(hudIndex)
```
```c
BOOL END_TEXT_COMMAND_IS_THIS_HELP_MESSAGE_BEING_DISPLAYED(int hudIndex);
```

**Parámetros**

- `hudIndex` (`int`): The hud index for help message.

**Devuelve:** `BOOL` — `true`: Indicates if the specific help message has been displayed.\ `false`: Indicates that the specific help message is still being displayed.

**Descripción oficial:**

Returns whether a specific help message is being displayed or not.

```cpp
enum HudIndexes {
    HELP_TEXT = 0,
    FLOATING_HELP_TEXT_1 = 1,
    FLOATING_HELP_TEXT_2 = 2,
}
```

**Nombres antiguos (alias):** `0x10BDDBFC529428DD` (`N_0x10bddbfc529428dd`)

---
### EndTextCommandLineCount

`_END_TEXT_COMMAND_LINE_COUNT` · hash `0x9040DFB09BE75706` · jhash `0xAA318785` · **Cliente**

```lua
local retval = EndTextCommandLineCount(x, y)
```
```c
int _END_TEXT_COMMAND_LINE_COUNT(float x, float y);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)

**Devuelve:** `int`

**Descripción oficial:**

```
END_TEXT_COMMAND_*
Determines how many lines the text string will use when drawn on screen.
Must use 0x521FB041D93DD0E4 for setting up
```

**Nombres antiguos (alias):** `0x9040DFB09BE75706` (`N_0x9040dfb09be75706`), `_GET_TEXT_SCREEN_LINE_COUNT` (`GetTextScreenLineCount`), `_END_TEXT_COMMAND_GET_LINE_COUNT` (`EndTextCommandGetLineCount`)

---
### EndTextCommandObjective

`_END_TEXT_COMMAND_OBJECTIVE` · hash `0xCFDBDF5AE59BA0F4` · jhash `0x2944A6C5` · **Cliente**

```lua
EndTextCommandObjective(p0)
```
```c
void _END_TEXT_COMMAND_OBJECTIVE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCFDBDF5AE59BA0F4` (`N_0xcfdbdf5ae59ba0f4`)

---
### EndTextCommandOverrideButtonText

`END_TEXT_COMMAND_OVERRIDE_BUTTON_TEXT` · hash `0xA86911979638106F` · jhash `0x6E7FDA1C` · **Cliente**

```lua
EndTextCommandOverrideButtonText(buttonIndex)
```
```c
void END_TEXT_COMMAND_OVERRIDE_BUTTON_TEXT(int buttonIndex);
```

**Parámetros**

- `buttonIndex` (`int`): Index of the instructional button

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA86911979638106F` (`N_0xa86911979638106f`), `_END_TEXT_COMMAND_TIMER` (`EndTextCommandTimer`)

---
### EndTextCommandPrint

`END_TEXT_COMMAND_PRINT` · hash `0x9D77056A530643F6` · jhash `0x38F82261` · **Cliente**

```lua
EndTextCommandPrint(duration, drawImmediately)
```
```c
void END_TEXT_COMMAND_PRINT(int duration, BOOL drawImmediately);
```

**Parámetros**

- `duration` (`int`)
- `drawImmediately` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Draws the subtitle at middle center of the screen.  
int duration = time in milliseconds to show text on screen before disappearing  
drawImmediately = If true, the text will be drawn immediately, if false, the text will be drawn after the previous subtitle has finished  
Used to be known as _DRAW_SUBTITLE_TIMED  
```

**Nombres antiguos (alias):** `_DRAW_SUBTITLE_TIMED` (`DrawSubtitleTimed`)

---
### EndTextCommandSetBlipName

`END_TEXT_COMMAND_SET_BLIP_NAME` · hash `0xBC38B49BCB83BC9B` · jhash `0xE8E59820` · **Cliente**

```lua
EndTextCommandSetBlipName(blip)
```
```c
void END_TEXT_COMMAND_SET_BLIP_NAME(Blip blip);
```

**Parámetros**

- `blip` (`Blip`): The blip to change the name for.

**Devuelve:** `void`

**Descripción oficial:**

Finalizes a text command started with [`BEGIN_TEXT_COMMAND_SET_BLIP_NAME`](#begintextcommandsetblipname), setting the name
of the specified blip.

**Ejemplo (lua):**

```lua
-- creates a blip called 'Food for me!' at 0.0, 0.0, 0.0
AddTextEntry('MYBLIP', 'Food for ~a~!')

local blip = AddBlipForCoords(0.0, 0.0, 0.0)
BeginTextCommandSetBlipName('MYBLIP')
AddTextComponentSubstringPlayerName('me')
EndTextCommandSetBlipName(blip)
```

---
### EndTextCommandThefeedPostAward

`END_TEXT_COMMAND_THEFEED_POST_AWARD` · hash `0xAA295B6F28BD587D` · jhash `0x02DED2B8` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostAward(textureDict, textureName, rpBonus, colorOverlay, titleLabel)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_AWARD(char* textureDict, char* textureName, int rpBonus, int colorOverlay, char* titleLabel);
```

**Parámetros**

- `textureDict` (`char*`): The texture dictionary name for the icon on the left.
- `textureName` (`char*`): The texture name for the icon on the left.
- `rpBonus` (`int`): The gained "RP" amount that will be displayed on the right side of the notification.
- `colorOverlay` (`int`): Hudcolor overlay that gets applied on top of the notification, conflicts with text/image visibility in most cases if set to something other than 0.
- `titleLabel` (`char*`): The label that will be displayed at the top of the notification (title).

**Devuelve:** `int` — The notification handle.

**Descripción oficial:**

Shows an "award" notification above the minimap, lua example result:

![](https://i.imgur.com/9U2x4ek.png)

Old description:

```
Example:  
UI::_SET_NOTIFICATION_TEXT_ENTRY("HUNT");  
UI::_0xAA295B6F28BD587D("Hunting", "Hunting_Gold_128", 0, 109, "HUD_MED_UNLKED");  
```

**Nombres antiguos (alias):** `0xAA295B6F28BD587D` (`N_0xaa295b6f28bd587d`), `_DRAW_NOTIFICATION_ICON` (`DrawNotificationIcon`), `_DRAW_NOTIFICATION_AWARD` (`DrawNotificationAward`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    -- Get the ped headshot image.
    local handle = RegisterPedheadshot(PlayerPedId())
    while not IsPedheadshotReady(handle) or not IsPedheadshotValid(handle) do
        Citizen.Wait(0)
    end
    local txd = GetPedheadshotTxdString(handle)

    -- Add the notification text, the more text you add the smaller the font
    -- size will become (text is forced on 1 line only), so keep this short!
    BeginTextCommandThefeedPost("STRING")
    AddTextComponentSubstringPlayerName("You won the match!")

    -- Draw the notification
    EndTextCommandThefeedPostAward(txd, txd, 200, 0, "FM_GEN_UNLOCK")
    
    -- Cleanup after yourself!
    UnregisterPedheadshot(handle)
end)
```

---
### EndTextCommandThefeedPostCrewRankup

`END_TEXT_COMMAND_THEFEED_POST_CREW_RANKUP` · hash `0x8EFCCF6EC66D85E4` · jhash `0x76FB0F21` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostCrewRankup(chTitle, clanTxd, clanTxn, isImportant, showSubtitle)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_CREW_RANKUP(char* chTitle, char* clanTxd, char* clanTxn, BOOL isImportant, BOOL showSubtitle);
```

**Parámetros**

- `chTitle` (`char*`)
- `clanTxd` (`char*`)
- `clanTxn` (`char*`)
- `isImportant` (`BOOL`)
- `showSubtitle` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x8EFCCF6EC66D85E4` (`N_0x8efccf6ec66d85e4`)

---
### EndTextCommandThefeedPostCrewtag

`END_TEXT_COMMAND_THEFEED_POST_CREWTAG` · hash `0x97C9E4E7024A8F2C` · jhash `0xA9CCEF66` · **Cliente**

```lua
local retval, crewTag = EndTextCommandThefeedPostCrewtag(crewTypeIsPrivate, crewTagContainsRockstar, rank, hasFounderStatus, isImportant, clanHandle, r, g, b)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_CREWTAG(BOOL crewTypeIsPrivate, BOOL crewTagContainsRockstar, int* crewTag, int rank, BOOL hasFounderStatus, BOOL isImportant, int clanHandle, int r, int g, int b);
```

**Parámetros**

- `crewTypeIsPrivate` (`BOOL`)
- `crewTagContainsRockstar` (`BOOL`)
- `crewTag` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rank` (`int`)
- `hasFounderStatus` (`BOOL`)
- `isImportant` (`BOOL`)
- `clanHandle` (`int`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
This function and the one below it are for after you receive an invite, not sending it.  
p0 = 1 or 0  
nothin doin.   
int invite(Player player)  
	{  
int iVar2, iVar3;  
networkHandleMgr handle;  
NETWORK_HANDLE_FROM_PLAYER(player, &handle.netHandle, 13);  
networkClanMgr clan;  
char *playerName = GET_PLAYER_NAME(player);  
_SET_NOTIFICATION_TEXT_ENTRY("STRING");  
_SET_NOTIFACTION_COLOR_NEXT(0);  
ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(playerName);  
if (NETWORK_CLAN_PLAYER_GET_DESC(&clan, 35, &handle.netHandle))  
{  
	iVar2 = 0;  
	if (ARE_STRINGS_EQUAL(clan.unk22, "Leader") && clan.unk30 == 0)  
	{  
iVar2 = 1;  
	}  
	if (clan.unk21 > 0)  
	{  
iVar3 = 0;  
	}  
	else  
	{  
iVar3 = 1;  
	}  
	BOOL unused = _0x54E79E9C(&clan.clanHandle, 35);  
	return _DRAW_NOTIFICATION_APARTMENT_INVITE(iVar3, 0 /*unused*/, &clan.unk17, clan.unk30, iVar2, 0, clan.clanHandle, 0, 0, 0);  
}  
	}  
```

**Nombres antiguos (alias):** `0x97C9E4E7024A8F2C` (`N_0x97c9e4e7024a8f2c`), `_NOTIFICATION_SEND_APARTMENT_INVITE` (`NotificationSendApartmentInvite`), `_DRAW_NOTIFICATION_APARTMENT_INVITE` (`DrawNotificationApartmentInvite`)

---
### EndTextCommandThefeedPostCrewtagWithGameName

`END_TEXT_COMMAND_THEFEED_POST_CREWTAG_WITH_GAME_NAME` · hash `0x137BC35589E34E1E` · jhash `0x88B9B909` · **Cliente**

```lua
local retval, crewTag = EndTextCommandThefeedPostCrewtagWithGameName(crewTypeIsPrivate, crewTagContainsRockstar, rank, isLeader, isImportant, clanHandle, gamerStr, r, g, b)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_CREWTAG_WITH_GAME_NAME(BOOL crewTypeIsPrivate, BOOL crewTagContainsRockstar, int* crewTag, int rank, BOOL isLeader, BOOL isImportant, int clanHandle, char* gamerStr, int r, int g, int b);
```

**Parámetros**

- `crewTypeIsPrivate` (`BOOL`)
- `crewTagContainsRockstar` (`BOOL`)
- `crewTag` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rank` (`int`)
- `isLeader` (`BOOL`)
- `isImportant` (`BOOL`)
- `clanHandle` (`int`)
- `gamerStr` (`char*`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
p0 = 1 or 0  
crashes my game...  
this is for sending invites to network players - jobs/apartment/ect...   
return notification handle  
int invite(Player player)  
	{  
networkHandleMgr netHandle;  
networkClanMgr clan;  
char *playerName = GET_PLAYER_NAME(player);  
_SET_NOTIFICATION_TEXT_ENTRY("STRING");  
_SET_NOTIFACTION_COLOR_NEXT(1);  
ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(playerName);  
NETWORK_HANDLE_FROM_PLAYER(player, &netHandle.netHandle, 13);  
if (NETWORK_CLAN_PLAYER_IS_ACTIVE(&netHandle.netHandle))  
{  
	NETWORK_CLAN_PLAYER_GET_DESC(&clan.clanHandle, 35, &netHandle.netHandle);  
	_DRAW_NOTIFICATION_CLAN_INVITE(0, _0x54E79E9C(&clan.clanHandle, 35), &clan.unk17, clan.isLeader, 0, 0, clan.clanHandle, playerName, 0, 0, 0);  
}  
	}  
```

**Nombres antiguos (alias):** `0x137BC35589E34E1E` (`N_0x137bc35589e34e1e`), `_NOTIFICATION_SEND_CLAN_INVITE` (`NotificationSendClanInvite`), `_DRAW_NOTIFICATION_CLAN_INVITE` (`DrawNotificationClanInvite`)

---
### EndTextCommandThefeedPostMessagetext

`END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT` · hash `0x1CCD9A37359072CF` · jhash `0xE7E3C98B` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostMessagetext(textureDict, textureName, flash, iconType, sender, subject)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT(char* textureDict, char* textureName, BOOL flash, int iconType, char* sender, char* subject);
```

**Parámetros**

- `textureDict` (`char*`): The texture dictionary for the icon.
- `textureName` (`char*`): The texture name for the icon.
- `flash` (`BOOL`): Flash, doesn't seem to work no matter what.
- `iconType` (`int`): The icon type, see the list in the description below.
- `sender` (`char*`): The notification title.
- `subject` (`char*`): The notification subtitle.

**Devuelve:** `int` — The notification handle.

**Descripción oficial:**

Sets some extra options for a notification. It adds an image (or icon type) and sets a notification title (sender) and subtitle (subject).

Texture dictionary and texture name parameters are usually the same exact value.

Example result:

![](https://i.imgur.com/c2P5KBn.png)

Old description with list of possible icons and texture names:

```
List of picNames: pastebin.com/XdpJVbHz  
flash is a bool for fading in.  
iconTypes:  
1 : Chat Box  
2 : Email  
3 : Add Friend Request  
4 : Nothing  
5 : Nothing  
6 : Nothing  
7 : Right Jumping Arrow  
8 : RP Icon  
9 : $ Icon  
"sender" is the very top header. This can be any old string.  
"subject" is the header under the sender.  
```

**Nombres antiguos (alias):** `_SET_NOTIFICATION_MESSAGE` (`SetNotificationMessage`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    -- Get the ped headshot image.
    local handle = RegisterPedheadshot(PlayerPedId())
    while not IsPedheadshotReady(handle) or not IsPedheadshotValid(handle) do
        Citizen.Wait(0)
    end
    local txd = GetPedheadshotTxdString(handle)

    -- Add the notification text
    BeginTextCommandThefeedPost("STRING")
    AddTextComponentSubstringPlayerName("This is the private message :o")

    -- Set the notification icon, title and subtitle.
    local title = GetPlayerName(PlayerId())
    local subtitle = "Private Message"
    local iconType = 0
    local flash = false -- Flash doesn't seem to work no matter what.
    EndTextCommandThefeedPostMessagetext(txd, txd, flash, iconType, title, subtitle)

    -- Draw the notification
    local showInBrief = true
    local blink = false -- blink doesn't work when using icon notifications.
    EndTextCommandThefeedPostTicker(blink, showInBrief)
    
    -- Cleanup after yourself!
    UnregisterPedheadshot(handle)
end)
```

---
### EndTextCommandThefeedPostMessagetextGxtEntry

`_END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_GXT_ENTRY` · hash `0xC6F580E4C94926AC` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostMessagetextGxtEntry(txdName, textureName, flash, iconType, sender, subject)
```
```c
int _END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_GXT_ENTRY(char* txdName, char* textureName, BOOL flash, int iconType, char* sender, char* subject);
```

**Parámetros**

- `txdName` (`char*`)
- `textureName` (`char*`)
- `flash` (`BOOL`)
- `iconType` (`int`)
- `sender` (`char*`)
- `subject` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

This function can show pictures of every texture that can be requested by REQUEST_STREAMED_TEXTURE_DICT.
Needs more research.
Only one type of usage in the scripts:
HUD::\_C6F580E4C94926AC("CHAR_ACTING_UP", "CHAR_ACTING_UP", 0, 0, "DI_FEED_CHAR", a\_0);

**Nombres antiguos (alias):** `0xC6F580E4C94926AC` (`N_0xc6f580e4c94926ac`), `_SET_NOTIFICATION_MESSAGE_3` (`SetNotificationMessage_3`), `_END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_ENTRY` (`EndTextCommandThefeedPostMessagetextEntry`)

---
### EndTextCommandThefeedPostMessagetextTu

`END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_TU` · hash `0x1E6611149DB3DB6B` · jhash `0x0EB382B7` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostMessagetextTu(picTxd, picTxn, flash, iconType, nameStr, subtitleStr, durationMultiplier)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_TU(char* picTxd, char* picTxn, BOOL flash, int iconType, char* nameStr, char* subtitleStr, float durationMultiplier);
```

**Parámetros**

- `picTxd` (`char*`)
- `picTxn` (`char*`)
- `flash` (`BOOL`)
- `iconType` (`int`): The icon type, you can find those here: [`END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT`](#endtextcommandthefeedpostmessagetext)
- `nameStr` (`char*`)
- `subtitleStr` (`char*`)
- `durationMultiplier` (`float`): 1.0 is normal, 2.0 is twice as long, and 0.5 is half its normal display time.

**Devuelve:** `int`

**Descripción oficial:**

Example, only occurrence in the scripts:

```
v_8 = UI::END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_TU("CHAR_SOCIAL_CLUB", "CHAR_SOCIAL_CLUB", 0, 0, &v_9, "", a_5);
```

Example result:

![](https://i.imgur.com/Qrf486G.png)

**Nombres antiguos (alias):** `0x1E6611149DB3DB6B` (`N_0x1e6611149db3db6b`), `_SET_NOTIFICATION_MESSAGE_4` (`SetNotificationMessage_4`)

---
### EndTextCommandThefeedPostMessagetextWithCrewTag

`END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_WITH_CREW_TAG` · hash `0x5CBF7BADE20DB93E` · jhash `0x3E807FE3` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostMessagetextWithCrewTag(picTxd, picTxn, flash, iconType, nameStr, subtitleStr, duration, crewPackedStr)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_WITH_CREW_TAG(char* picTxd, char* picTxn, BOOL flash, int iconType, char* nameStr, char* subtitleStr, float duration, char* crewPackedStr);
```

**Parámetros**

- `picTxd` (`char*`)
- `picTxn` (`char*`)
- `flash` (`BOOL`)
- `iconType` (`int`)
- `nameStr` (`char*`)
- `subtitleStr` (`char*`)
- `duration` (`float`)
- `crewPackedStr` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
List of picNames pastebin.com/XdpJVbHz  
flash is a bool for fading in.  
iconTypes:  
1 : Chat Box  
2 : Email  
3 : Add Friend Request  
4 : Nothing  
5 : Nothing  
6 : Nothing  
7 : Right Jumping Arrow  
8 : RP Icon  
9 : $ Icon  
"sender" is the very top header. This can be any old string.  
"subject" is the header under the sender.  
"duration" is a multiplier, so 1.0 is normal, 2.0 is twice as long (very slow), and 0.5 is half as long.  
"clanTag" shows a crew tag in the "sender" header, after the text. You need to use 3 underscores as padding. Maximum length of this field seems to be 7. (e.g. "MK" becomes "___MK", "ACE" becomes "___ACE", etc.)  
```

**Nombres antiguos (alias):** `_SET_NOTIFICATION_MESSAGE_CLAN_TAG` (`SetNotificationMessageClanTag`)

---
### EndTextCommandThefeedPostMessagetextWithCrewTagAndAdditionalIcon

`END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_WITH_CREW_TAG_AND_ADDITIONAL_ICON` · hash `0x531B84E7DA981FB6` · jhash `0xDEB491C8` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostMessagetextWithCrewTagAndAdditionalIcon(picTxd, picTxn, flash, iconType1, nameStr, subtitleStr, duration, crewPackedStr, iconType2, textColor)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_MESSAGETEXT_WITH_CREW_TAG_AND_ADDITIONAL_ICON(char* picTxd, char* picTxn, BOOL flash, int iconType1, char* nameStr, char* subtitleStr, float duration, char* crewPackedStr, int iconType2, int textColor);
```

**Parámetros**

- `picTxd` (`char*`)
- `picTxn` (`char*`)
- `flash` (`BOOL`)
- `iconType1` (`int`)
- `nameStr` (`char*`)
- `subtitleStr` (`char*`)
- `duration` (`float`)
- `crewPackedStr` (`char*`)
- `iconType2` (`int`)
- `textColor` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
List of picNames: pastebin.com/XdpJVbHz  
flash is a bool for fading in.  
iconTypes:  
1 : Chat Box  
2 : Email  
3 : Add Friend Request  
4 : Nothing  
5 : Nothing  
6 : Nothing  
7 : Right Jumping Arrow  
8 : RP Icon  
9 : $ Icon  
"sender" is the very top header. This can be any old string.  
"subject" is the header under the sender.  
"duration" is a multiplier, so 1.0 is normal, 2.0 is twice as long (very slow), and 0.5 is half as long.  
"clanTag" shows a crew tag in the "sender" header, after the text. You need to use 3 underscores as padding. Maximum length of this field seems to be 7. (e.g. "MK" becomes "___MK", "ACE" becomes "___ACE", etc.)  
iconType2 is a mirror of iconType. It shows in the "subject" line, right under the original iconType.  
int IconNotification(char *text, char *text2, char *Subject)  
{  
	_SET_NOTIFICATION_TEXT_ENTRY("STRING");  
	ADD_TEXT_COMPONENT_SUBSTRING_PLAYER_NAME(text);  
	_SET_NOTIFICATION_MESSAGE_CLAN_TAG_2("CHAR_SOCIAL_CLUB", "CHAR_SOCIAL_CLUB", 1, 7, text2, Subject, 1.0f, "__EXAMPLE", 7);  
	return _DRAW_NOTIFICATION(1, 1);  
}  
```

**Nombres antiguos (alias):** `_SET_NOTIFICATION_MESSAGE_CLAN_TAG_2` (`SetNotificationMessageClanTag_2`)

---
### EndTextCommandThefeedPostMpticker

`END_TEXT_COMMAND_THEFEED_POST_MPTICKER` · hash `0xF020C96915705B3A` · jhash `0x8E319AB8` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostMpticker(isImportant, showInBrief)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_MPTICKER(BOOL isImportant, BOOL showInBrief);
```

**Parámetros**

- `isImportant` (`BOOL`): If true, the notification will flash.
- `showInBrief` (`BOOL`): If true, the message will be shown in Pause Menu > Info > Notifications.

**Devuelve:** `int` — The notification handle.

**Descripción oficial:**

Exactly the same as [`END_TEXT_COMMAND_THEFEED_POST_TICKER`](#endtextcommandthefeedpostticker).

**Nombres antiguos (alias):** `_DRAW_NOTIFICATION_4` (`DrawNotification_4`)

---
### EndTextCommandThefeedPostReplayIcon

`_END_TEXT_COMMAND_THEFEED_POST_REPLAY_ICON` · hash `0xD202B92CBF1D816F` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostReplayIcon(eType, iIcon, sTitle)
```
```c
int _END_TEXT_COMMAND_THEFEED_POST_REPLAY_ICON(int eType, int iIcon, char* sTitle);
```

**Parámetros**

- `eType` (`int`)
- `iIcon` (`int`)
- `sTitle` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
returns a notification handle, prints out a notification like below:  
type range: 0   
if you set type to 1, image goes from 0 - 39 - Xbox you can add text to  
example:   
UI::_0xD202B92CBF1D816F(1, 20, "Who you trynna get crazy with, ese? Don't you know I'm LOCO?!");  
```

**Nombres antiguos (alias):** `0xD202B92CBF1D816F` (`N_0xd202b92cbf1d816f`), `_DRAW_NOTIFICATION_WITH_ICON` (`DrawNotificationWithIcon`)

---
### EndTextCommandThefeedPostReplayInput

`_END_TEXT_COMMAND_THEFEED_POST_REPLAY_INPUT` · hash `0xDD6CB2CCE7C2735C` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostReplayInput(type, button, text)
```
```c
int _END_TEXT_COMMAND_THEFEED_POST_REPLAY_INPUT(int type, char* button, char* text);
```

**Parámetros**

- `type` (`int`)
- `button` (`char*`)
- `text` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
returns a notification handle, prints out a notification like below:
type range: 0 - 2
if you set type to 1, button accepts "~INPUT_SOMETHING~"
example:
HUD::_0xDD6CB2CCE7C2735C(1, "~INPUT_TALK~", "Who you trynna get crazy with, ese? Don't you know I'm LOCO?!");
Examples from the scripts:
l_D1[1/*1*/]=HUD::_DD6CB2CCE7C2735C(1,"~INPUT_REPLAY_START_STOP_RECORDING~","");
l_D1[2/*1*/]=HUD::_DD6CB2CCE7C2735C(1,"~INPUT_SAVE_REPLAY_CLIP~","");
l_D1[1/*1*/]=HUD::_DD6CB2CCE7C2735C(1,"~INPUT_REPLAY_START_STOP_RECORDING~","");
l_D1[2/*1*/]=HUD::_DD6CB2CCE7C2735C(1,"~INPUT_REPLAY_START_STOP_RECORDING_SECONDARY~","");
```

Preview:
![](https://i.imgur.com/gw6kWOe.jpeg)

**Nombres antiguos (alias):** `0xDD6CB2CCE7C2735C` (`N_0xdd6cb2cce7c2735c`), `_DRAW_NOTIFICATION_WITH_BUTTON` (`DrawNotificationWithButton`)

---
### EndTextCommandThefeedPostStats

`END_TEXT_COMMAND_THEFEED_POST_STATS` · hash `0x2B7E9A4EAAA93C89` · jhash `0xED130FA1` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostStats(statTitle, iconEnum, stepVal, barValue, isImportant, picTxd, picTxn)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_STATS(char* statTitle, int iconEnum, BOOL stepVal, int barValue, BOOL isImportant, char* picTxd, char* picTxn);
```

**Parámetros**

- `statTitle` (`char*`)
- `iconEnum` (`int`)
- `stepVal` (`BOOL`)
- `barValue` (`int`)
- `isImportant` (`BOOL`)
- `picTxd` (`char*`)
- `picTxn` (`char*`)

**Devuelve:** `int` — The notification handle.

**Descripción oficial:**

[List of picture names](https://pastebin.com/XdpJVbHz)

Example result:

![](https://i.imgur.com/eyXFAyN.png)

**Nombres antiguos (alias):** `0x2B7E9A4EAAA93C89` (`N_0x2b7e9a4eaaa93c89`), `_SET_NOTIFICATION_MESSAGE_2` (`SetNotificationMessage_2`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    -- Get the ped headshot image.
    local handle = RegisterPedheadshot(PlayerPedId())
    while not IsPedheadshotReady(handle) or not IsPedheadshotValid(handle) do
        Citizen.Wait(0)
    end
    local txd = GetPedheadshotTxdString(handle)

    -- Add the notification text
    BeginTextCommandThefeedPost("PS_UPDATE")
    AddTextComponentInteger(50)

    -- Set the notification title and progress
    local title = "PSF_STAMINA"
    local p1 = 14
    local lastProgress = 25
    local newProgress = 50
    local unknownBool = false
    EndTextCommandThefeedPostStats(title, p1, newProgress, lastProgress, unknownBool, txd, txd)

    -- Draw the notification
    local showInBrief = true
    local blink = false -- blink doesn't work when using icon notifications.
    EndTextCommandThefeedPostTicker(blink, showInBrief)
    
    -- Cleanup after yourself!
    UnregisterPedheadshot(handle)
end)
```

---
### EndTextCommandThefeedPostTicker

`END_TEXT_COMMAND_THEFEED_POST_TICKER` · hash `0x2ED7843F8F801023` · jhash `0x08F7AF78` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostTicker(isImportant, showInBrief)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_TICKER(BOOL isImportant, BOOL showInBrief);
```

**Parámetros**

- `isImportant` (`BOOL`): Makes the notification flash on the screen.
- `showInBrief` (`BOOL`): Makes the notification appear in the "Pause Menu > Info/Brief > Notifications" section.

**Devuelve:** `int` — The notification handle.

**Descripción oficial:**

Posts a generic feed notification:

![](https://i.ibb.co/GkHcFvf/image.png)

**Nombres antiguos (alias):** `_DRAW_NOTIFICATION` (`DrawNotification`)

**Ejemplo (lua):**

```lua
AddTextEntry("MyFeedMessage", "Hello " .. GetPlayerName(PlayerId()) .. ".")
BeginTextCommandThefeedPost("MyFeedMessage")
EndTextCommandThefeedPostTicker(true, true)
```

---
### EndTextCommandThefeedPostTickerForced

`END_TEXT_COMMAND_THEFEED_POST_TICKER_FORCED` · hash `0x44FA03975424A0EE` · jhash `0x57B8D0D4` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostTickerForced(isImportant, showInBrief)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_TICKER_FORCED(BOOL isImportant, BOOL showInBrief);
```

**Parámetros**

- `isImportant` (`BOOL`): If true, the notification will flash.
- `showInBrief` (`BOOL`): If true, shows in Pause Menu > Info > Notifications.

**Devuelve:** `int` — The notification handle.

**Descripción oficial:**

Posts an above minimap feed notification that is forced (Previous messages will be cleared).

**Nombres antiguos (alias):** `_DRAW_NOTIFICATION_2` (`DrawNotification_2`)

---
### EndTextCommandThefeedPostTickerWithTokens

`END_TEXT_COMMAND_THEFEED_POST_TICKER_WITH_TOKENS` · hash `0x378E809BF61EC840` · jhash `0x02BCAF9B` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostTickerWithTokens(isImportant, showInBrief)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_TICKER_WITH_TOKENS(BOOL isImportant, BOOL showInBrief);
```

**Parámetros**

- `isImportant` (`BOOL`): Makes the notification flash.
- `showInBrief` (`BOOL`): Shows in Pause Menu > Info > Notifications.

**Devuelve:** `int` — Notification handle.

**Descripción oficial:**

Posts an above minimap feed message with tokens support (blips, input keys, etc...)

**Nombres antiguos (alias):** `_DRAW_NOTIFICATION_3` (`DrawNotification_3`)

---
### EndTextCommandThefeedPostUnlock

`END_TEXT_COMMAND_THEFEED_POST_UNLOCK` · hash `0x33EE12743CCD6343` · jhash `0xE05E7052` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostUnlock(chTitle, iconType, chSubtitle)
```
```c
Any END_TEXT_COMMAND_THEFEED_POST_UNLOCK(char* chTitle, int iconType, char* chSubtitle);
```

**Parámetros**

- `chTitle` (`char*`)
- `iconType` (`int`)
- `chSubtitle` (`char*`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x33EE12743CCD6343` (`N_0x33ee12743ccd6343`)

---
### EndTextCommandThefeedPostUnlockTu

`END_TEXT_COMMAND_THEFEED_POST_UNLOCK_TU` · hash `0xC8F3AAF93D0600BF` · jhash `0x4FA43BA4` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostUnlockTu(chTitle, iconType, chSubtitle, isImportant)
```
```c
Any END_TEXT_COMMAND_THEFEED_POST_UNLOCK_TU(char* chTitle, int iconType, char* chSubtitle, BOOL isImportant);
```

**Parámetros**

- `chTitle` (`char*`)
- `iconType` (`int`)
- `chSubtitle` (`char*`)
- `isImportant` (`BOOL`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xC8F3AAF93D0600BF` (`N_0xc8f3aaf93d0600bf`)

---
### EndTextCommandThefeedPostUnlockTuWithColor

`END_TEXT_COMMAND_THEFEED_POST_UNLOCK_TU_WITH_COLOR` · hash `0x7AE0589093A2E088` · jhash `0x8C90D22F` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostUnlockTuWithColor(chTitle, iconType, chSubtitle, isImportant, titleColor, p5)
```
```c
Any END_TEXT_COMMAND_THEFEED_POST_UNLOCK_TU_WITH_COLOR(char* chTitle, int iconType, char* chSubtitle, BOOL isImportant, int titleColor, BOOL p5);
```

**Parámetros**

- `chTitle` (`char*`)
- `iconType` (`int`)
- `chSubtitle` (`char*`)
- `isImportant` (`BOOL`)
- `titleColor` (`int`)
- `p5` (`BOOL`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x7AE0589093A2E088` (`N_0x7ae0589093a2e088`)

---
### EndTextCommandThefeedPostVersusTu

`END_TEXT_COMMAND_THEFEED_POST_VERSUS_TU` · hash `0xB6871B0555B02996` · jhash `0x5E93FBFA` · **Cliente**

```lua
local retval = EndTextCommandThefeedPostVersusTu(ch1TXD, ch1TXN, val1, ch2TXD, ch2TXN, val2)
```
```c
int END_TEXT_COMMAND_THEFEED_POST_VERSUS_TU(char* ch1TXD, char* ch1TXN, int val1, char* ch2TXD, char* ch2TXN, int val2);
```

**Parámetros**

- `ch1TXD` (`char*`)
- `ch1TXN` (`char*`)
- `val1` (`int`)
- `ch2TXD` (`char*`)
- `ch2TXN` (`char*`)
- `val2` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Added Parameter 7: int hudColorIndex1
NativeDB Added Parameter 8: int hudColorIndex2
```

**Nombres antiguos (alias):** `0xB6871B0555B02996` (`N_0xb6871b0555b02996`)

---
### FlagPlayerContextInTournament

`FLAG_PLAYER_CONTEXT_IN_TOURNAMENT` · hash `0xCEF214315D276FD1` · jhash `0xFF06772A` · **Cliente**

```lua
FlagPlayerContextInTournament(toggle)
```
```c
void FLAG_PLAYER_CONTEXT_IN_TOURNAMENT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCEF214315D276FD1` (`N_0xcef214315d276fd1`), `_SET_IS_IN_TOURNAMENT` (`SetIsInTournament`)

---
### FlashAbilityBar

`FLASH_ABILITY_BAR` · hash `0x02CFBA0C9E9275CE` · jhash `0x3648960D` · **Cliente**

```lua
FlashAbilityBar(millisecondsToFlash)
```
```c
void FLASH_ABILITY_BAR(int millisecondsToFlash);
```

**Parámetros**

- `millisecondsToFlash` (`int`)

**Devuelve:** `void`

---
### FlashMinimapDisplay

`FLASH_MINIMAP_DISPLAY` · hash `0xF2DD778C22B15BDA` · jhash `0xB8359952` · **Cliente**

```lua
FlashMinimapDisplay()
```
```c
void FLASH_MINIMAP_DISPLAY();
```

**Devuelve:** `void`

**Descripción oficial:**

```
adds a short flash to the Radar/Minimap  
Usage: UI.FLASH_MINIMAP_DISPLAY  
```

---
### FlashMinimapDisplayWithColor

`FLASH_MINIMAP_DISPLAY_WITH_COLOR` · hash `0x6B1DE27EE78E6A19` · jhash `0x79A6CAF6` · **Cliente**

```lua
FlashMinimapDisplayWithColor(hudColorIndex)
```
```c
void FLASH_MINIMAP_DISPLAY_WITH_COLOR(int hudColorIndex);
```

**Parámetros**

- `hudColorIndex` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6B1DE27EE78E6A19` (`N_0x6b1de27ee78e6a19`)

---
### FlashWantedDisplay

`FLASH_WANTED_DISPLAY` · hash `0xA18AFB39081B6A1F` · jhash `0x629F866B` · **Cliente**

```lua
FlashWantedDisplay(p0)
```
```c
void FLASH_WANTED_DISPLAY(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### ForceCloseReportugcMenu

`FORCE_CLOSE_REPORTUGC_MENU` · hash `0xEE4C0E6DBC6F2C6F` · jhash `0x67649EE0` · **Cliente**

```lua
ForceCloseReportugcMenu()
```
```c
void FORCE_CLOSE_REPORTUGC_MENU();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEE4C0E6DBC6F2C6F` (`N_0xee4c0e6dbc6f2c6f`)

---
### ForceCloseTextInputBox

`FORCE_CLOSE_TEXT_INPUT_BOX` · hash `0x8817605C2BA76200` · **Cliente**

```lua
ForceCloseTextInputBox()
```
```c
void FORCE_CLOSE_TEXT_INPUT_BOX();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8817605C2BA76200` (`N_0x8817605c2ba76200`), `_FORCE_CLOSE_TEXT_INPUT_BOX` (`ForceCloseTextInputBox`)

---
### ForceSonarBlipsThisFrame

`FORCE_SONAR_BLIPS_THIS_FRAME` · hash `0x1121BFA1A1A522A8` · jhash `0x3F4AFB13` · **Cliente**

```lua
local retval = ForceSonarBlipsThisFrame()
```
```c
Any FORCE_SONAR_BLIPS_THIS_FRAME();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
Doesn't actually return anything.
```

**Nombres antiguos (alias):** `0x1121BFA1A1A522A8` (`N_0x1121bfa1a1a522a8`)

---
### GetAiBlip

`_GET_AI_BLIP` · hash `0x56176892826A4FE8` · jhash `0xCA52CF43` · **Cliente**

```lua
local retval = GetAiBlip(ped)
```
```c
Blip _GET_AI_BLIP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Blip`

**Descripción oficial:**

```
Returns the current AI BLIP for the specified ped  
```

**Nombres antiguos (alias):** `0x56176892826A4FE8` (`N_0x56176892826a4fe8`)

---
### GetAiBlip_2

`_GET_AI_BLIP_2` · hash `0x7CD934010E115C2C` · jhash `0x06349065` · **Cliente**

```lua
local retval = GetAiBlip_2(ped)
```
```c
Blip _GET_AI_BLIP_2(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Blip`

**Nombres antiguos (alias):** `0x7CD934010E115C2C` (`N_0x7cd934010e115c2c`)

---
### GetBlipAlpha

`GET_BLIP_ALPHA` · hash `0x970F608F0EE6C885` · jhash `0x297AF6C8` · **Cliente**

```lua
local retval = GetBlipAlpha(blip)
```
```c
int GET_BLIP_ALPHA(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `int`

---
### GetBlipColour

`GET_BLIP_COLOUR` · hash `0xDF729E8D20CF7327` · jhash `0xDD6A1E54` · **Cliente**

```lua
local retval = GetBlipColour(blip)
```
```c
int GET_BLIP_COLOUR(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `int`

---
### GetBlipCoords

`GET_BLIP_COORDS` · hash `0x586AFE3FF72D996E` · jhash `0xEF6FF47B` · **Cliente**

```lua
local retval = GetBlipCoords(blip)
```
```c
Vector3 GET_BLIP_COORDS(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `Vector3`

---
### GetBlipFromEntity

`GET_BLIP_FROM_ENTITY` · hash `0xBC8DBDCA2436F7E8` · jhash `0x005A2A47` · **Cliente**

```lua
local retval = GetBlipFromEntity(entity)
```
```c
Blip GET_BLIP_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Blip`

**Descripción oficial:**

```
Returns the Blip handle of given Entity.  
```

---
### GetBlipHudColour

`GET_BLIP_HUD_COLOUR` · hash `0x729B5F1EFBC0AAEE` · jhash `0xE88B4BC2` · **Cliente**

```lua
local retval = GetBlipHudColour(blip)
```
```c
int GET_BLIP_HUD_COLOUR(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `int`

---
### GetBlipInfoIdCoord

`GET_BLIP_INFO_ID_COORD` · hash `0xFA7C7F0AADF25D09` · jhash `0xB7374A66` · **Cliente**

```lua
local retval = GetBlipInfoIdCoord(blip)
```
```c
Vector3 GET_BLIP_INFO_ID_COORD(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `Vector3`

---
### GetBlipInfoIdDisplay

`GET_BLIP_INFO_ID_DISPLAY` · hash `0x1E314167F701DC3B` · jhash `0xD0FC19F4` · **Cliente**

```lua
local retval = GetBlipInfoIdDisplay(blip)
```
```c
int GET_BLIP_INFO_ID_DISPLAY(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `int`

---
### GetBlipInfoIdEntityIndex

`GET_BLIP_INFO_ID_ENTITY_INDEX` · hash `0x4BA4E2553AFEDC2C` · jhash `0xA068C40B` · **Cliente**

```lua
local retval = GetBlipInfoIdEntityIndex(blip)
```
```c
Entity GET_BLIP_INFO_ID_ENTITY_INDEX(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `Entity`

---
### GetBlipInfoIdPickupIndex

`GET_BLIP_INFO_ID_PICKUP_INDEX` · hash `0x9B6786E4C03DD382` · jhash `0x86913D37` · **Cliente**

```lua
local retval = GetBlipInfoIdPickupIndex(blip)
```
```c
Pickup GET_BLIP_INFO_ID_PICKUP_INDEX(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `Pickup`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### GetBlipInfoIdType

`GET_BLIP_INFO_ID_TYPE` · hash `0xBE9B0959FFD0779B` · jhash `0x501D7B4E` · **Cliente**

```lua
local retval = GetBlipInfoIdType(blip)
```
```c
int GET_BLIP_INFO_ID_TYPE(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns a value based on what the blip is attached to
1 - Vehicle
2 - Ped
3 - Object
4 - Coord
5 - unk
6 - Pickup
7 - Radius
```

---
### GetBlipRotation

`_GET_BLIP_ROTATION` · hash `0x003E92BA477F9D7F` · **Cliente**

```lua
local retval = GetBlipRotation(blip)
```
```c
int _GET_BLIP_ROTATION(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

**Nombres antiguos (alias):** `0x003E92BA477F9D7F` (`N_0x003e92ba477f9d7f`)

---
### GetBlipSprite

`GET_BLIP_SPRITE` · hash `0x1FC877464A04FC4F` · jhash `0x72FF2E73` · **Cliente**

```lua
local retval = GetBlipSprite(blip)
```
```c
int GET_BLIP_SPRITE(Blip blip);
```

**Parámetros**

- `blip` (`Blip`): The blip handle.

**Devuelve:** `int`

**Descripción oficial:**

Gets the sprite id of the specified blip. Blip sprite ids and images can be found [here](https://docs.fivem.net/docs/game-references/blips/).

---
### GetClosestBlipOfType

`_GET_CLOSEST_BLIP_OF_TYPE` · hash `0xD484BF71050CA1EE` · **Cliente**

```lua
local retval = GetClosestBlipOfType(blipSprite)
```
```c
Blip _GET_CLOSEST_BLIP_OF_TYPE(int blipSprite);
```

**Parámetros**

- `blipSprite` (`int`)

**Devuelve:** `Blip`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0xD484BF71050CA1EE` (`N_0xd484bf71050ca1ee`)

---
### GetCurrentFrontendMenuVersion

`GET_CURRENT_FRONTEND_MENU_VERSION` · hash `0x2309595AD6145265` · jhash `0x33D6868F` · **Cliente**

```lua
local retval = GetCurrentFrontendMenuVersion()
```
```c
Hash GET_CURRENT_FRONTEND_MENU_VERSION();
```

**Devuelve:** `Hash`

**Descripción oficial:**

```
if (HUD::GET_CURRENT_FRONTEND_MENU_VERSION() == joaat("fe_menu_version_empty_no_background"))
```

**Nombres antiguos (alias):** `0x2309595AD6145265` (`N_0x2309595ad6145265`), `_GET_CURRENT_FRONTEND_MENU` (`GetCurrentFrontendMenu`)

---
### GetCurrentWebpageId

`GET_CURRENT_WEBPAGE_ID` · hash `0x01A358D9128B7A86` · jhash `0xAB5B7C18` · **Cliente**

```lua
local retval = GetCurrentWebpageId()
```
```c
int GET_CURRENT_WEBPAGE_ID();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x01A358D9128B7A86` (`N_0x01a358d9128b7a86`), `_GET_ACTIVE_WEBSITE_ID` (`GetActiveWebsiteId`)

---
### GetCurrentWebsiteId

`GET_CURRENT_WEBSITE_ID` · hash `0x97D47996FC48CBAD` · jhash `0x42A55B14` · **Cliente**

```lua
local retval = GetCurrentWebsiteId()
```
```c
int GET_CURRENT_WEBSITE_ID();
```

**Devuelve:** `int`

---
### GetDefaultScriptRendertargetRenderId

`GET_DEFAULT_SCRIPT_RENDERTARGET_RENDER_ID` · hash `0x52F0982D7FD156B6` · jhash `0x8188935F` · **Cliente**

```lua
local retval = GetDefaultScriptRendertargetRenderId()
```
```c
int GET_DEFAULT_SCRIPT_RENDERTARGET_RENDER_ID();
```

**Devuelve:** `int`

**Descripción oficial:**

```
This function is hard-coded to always return 1.  
```

---
### GetFilenameForAudioConversation

`GET_FILENAME_FOR_AUDIO_CONVERSATION` · hash `0x7B5280EBA9840C72` · jhash `0x95C4B5AD` · **Cliente**

```lua
local retval = GetFilenameForAudioConversation(labelName)
```
```c
char* GET_FILENAME_FOR_AUDIO_CONVERSATION(char* labelName);
```

**Parámetros**

- `labelName` (`char*`): The label name for which the audio conversation filename is requested.

**Devuelve:** `char*` — Returns the filename associated with the provided labelName.

**Descripción oficial:**

Gets a localized string literal from a label name. This is used to get the filename of the audio conversation associated with the provided label name.

**Nombres antiguos (alias):** `0x7B5280EBA9840C72` (`N_0x7b5280eba9840c72`), `_GET_LABEL_TEXT` (`GetLabelText`)

**Ejemplo (lua):**

```lua
-- Get the vehicle in which the player is currently seated
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

-- Get the model of the vehicle
local model = GetEntityModel(vehicle)

-- Get the display name of the vehicle model
local displayName = GetDisplayNameFromVehicleModel(model)

-- Get the label text for the audio conversation associated with the display name
local label = GetFilenameForAudioConversation(displayName)

-- Print the label text
print(label)
```

**Ejemplo (js):**

```js
// Get the vehicle in which the player is currently seated
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

// Get the model of the vehicle
const model = GetEntityModel(vehicle);

// Get the display name of the vehicle model
const displayName = GetDisplayNameFromVehicleModel(model);

// Get the label text for the audio conversation associated with the display name
const label = GetFilenameForAudioConversation(displayName);

// Log the label text to the console
console.log(label);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Get the vehicle in which the player is currently seated
Vehicle vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

// Get the model of the vehicle
uint model = (uint)GetEntityModel(vehicle);

// Get the display name of the vehicle model
string displayName = GetDisplayNameFromVehicleModel(model);

// Get the label text for the audio conversation associated with the display name
string label = GetFilenameForAudioConversation(displayName);

// Print the label text
Debug.WriteLine(label);
```

---
### GetFirstBlipInfoId

`GET_FIRST_BLIP_INFO_ID` · hash `0x1BEDE233E6CD2A1F` · jhash `0x64C0273D` · **Cliente**

```lua
local retval = GetFirstBlipInfoId(blipSprite)
```
```c
Blip GET_FIRST_BLIP_INFO_ID(int blipSprite);
```

**Parámetros**

- `blipSprite` (`int`): Sprite ID, see the [Blips Game Reference](https://docs.fivem.net/docs/game-references/blips/) for the full list.

**Devuelve:** `Blip` — Returns the first blip ID in an interator that has the specified blip sprite.

**Descripción oficial:**

Also see [`GET_NEXT_BLIP_INFO_ID`](#getnextblipinfoid) for an example.

---
### GetGlobalActionscriptFlag

`GET_GLOBAL_ACTIONSCRIPT_FLAG` · hash `0xE3B05614DCE1D014` · jhash `0xD217EE7E` · **Cliente**

```lua
local retval = GetGlobalActionscriptFlag(flagIndex)
```
```c
int GET_GLOBAL_ACTIONSCRIPT_FLAG(int flagIndex);
```

**Parámetros**

- `flagIndex` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the ActionScript flagValue.
ActionScript flags are global flags that scaleforms use
Flags found during testing
0: Returns 1 if the web_browser keyboard is open, otherwise 0
1: Returns 1 if the player has clicked back twice on the opening page, otherwise 0 (web_browser)
2: Returns how many links the player has clicked in the web_browser scaleform, returns 0 when the browser gets closed
9: Returns the current selection on the mobile phone scaleform
There are 20 flags in total.
```

**Nombres antiguos (alias):** `0xE3B05614DCE1D014` (`N_0xe3b05614dce1d014`)

---
### GetHudColour

`GET_HUD_COLOUR` · hash `0x7C9C91AB74A0360F` · jhash `0x63F66A0B` · **Cliente**

```lua
local r, g, b, a = GetHudColour(hudColorIndex)
```
```c
void GET_HUD_COLOUR(int hudColorIndex, int* r, int* g, int* b, int* a);
```

**Parámetros**

- `hudColorIndex` (`int`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `a` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

Gets hud color RGBA parameter values by passing a hud color index (hudColorIndex).

HUD colors can be found [here](https://docs.fivem.net/docs/game-references/hud-colors/)

---
### GetHudComponentPosition

`GET_HUD_COMPONENT_POSITION` · hash `0x223CA69A8C4417FD` · jhash `0x080DCED6` · **Cliente**

```lua
local retval = GetHudComponentPosition(id)
```
```c
Vector3 GET_HUD_COMPONENT_POSITION(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `Vector3`

---
### GetHudScreenPositionFromWorldPosition

`GET_HUD_SCREEN_POSITION_FROM_WORLD_POSITION` · hash `0xF9904D11F1ACBEC3` · jhash `0xFE9A39F8` · **Cliente**

```lua
local retval, screenX, screenY = GetHudScreenPositionFromWorldPosition(worldX, worldY, worldZ)
```
```c
BOOL GET_HUD_SCREEN_POSITION_FROM_WORLD_POSITION(float worldX, float worldY, float worldZ, float* screenX, float* screenY);
```

**Parámetros**

- `worldX` (`float`)
- `worldY` (`float`)
- `worldZ` (`float`)
- `screenX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `screenY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
World to relative screen coords
this world to screen will keep the text on screen. it will keep it in the screen pos
```

**Nombres antiguos (alias):** `0xF9904D11F1ACBEC3` (`N_0xf9904d11f1acbec3`), `_GET_2D_COORD_FROM_3D_COORD` (`Get_2dCoordFrom_3dCoord`)

---
### GetLengthOfLiteralString

`GET_LENGTH_OF_LITERAL_STRING` · hash `0xF030907CCBB8A9FD` · jhash `0x99379D55` · **Cliente**

```lua
local retval = GetLengthOfLiteralString(string)
```
```c
int GET_LENGTH_OF_LITERAL_STRING(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the length of the string passed (much like strlen).  
```

---
### GetLengthOfLiteralStringInBytes

`GET_LENGTH_OF_LITERAL_STRING_IN_BYTES` · hash `0x43E4111189E54F0E` · jhash `0x7DBC0764` · **Cliente**

```lua
local retval = GetLengthOfLiteralStringInBytes(string)
```
```c
int GET_LENGTH_OF_LITERAL_STRING_IN_BYTES(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x43E4111189E54F0E` (`N_0x43e4111189e54f0e`), `_GET_LENGTH_OF_STRING` (`GetLengthOfString`)

---
### GetLengthOfStringWithThisTextLabel

`GET_LENGTH_OF_STRING_WITH_THIS_TEXT_LABEL` · hash `0x801BD273D3A23F74` · jhash `0xA4CA7BE5` · **Cliente**

```lua
local retval = GetLengthOfStringWithThisTextLabel(gxt)
```
```c
int GET_LENGTH_OF_STRING_WITH_THIS_TEXT_LABEL(char* gxt);
```

**Parámetros**

- `gxt` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the string length of the string from the gxt string .  
```

---
### GetMainPlayerBlipId

`GET_MAIN_PLAYER_BLIP_ID` · hash `0xDCD4EC3F419D02FA` · jhash `0xAB93F020` · **Cliente**

```lua
local retval = GetMainPlayerBlipId()
```
```c
Blip GET_MAIN_PLAYER_BLIP_ID();
```

**Devuelve:** `Blip`

---
### GetMenuLayoutChangedEventDetails

`GET_MENU_LAYOUT_CHANGED_EVENT_DETAILS` · hash `0x7E17BE53E1AAABAF` · jhash `0x6025AA2F` · **Cliente**

```lua
local previousScreen, currentScreen, uniqueId = GetMenuLayoutChangedEventDetails()
```
```c
void GET_MENU_LAYOUT_CHANGED_EVENT_DETAILS(int* previousScreen, int* currentScreen, int* uniqueId);
```

**Parámetros**

- `previousScreen` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Screen id of the last selected item minus 1000. See [`PAUSE_MENUCEPTION_GO_DEEPER`](#pausemenuceptiongodeeper) for a list of screens.
- `currentScreen` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Current menu it's screen id.
- `uniqueId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Unique ID of the menu item.

**Devuelve:** `void`

**Descripción oficial:**

Returns details of a layout changed event.
Be sure this is called only when [`HAS_MENU_LAYOUT_CHANGED_EVENT_OCCURRED`](#hasmenulayoutchangedeventoccurred) returns true in a frame.
Can only be called by one script at a time.
Layout changed events become active whenever the menu is navigated up or down.

**Nombres antiguos (alias):** `0x7E17BE53E1AAABAF` (`N_0x7e17be53e1aaabaf`), `_GET_PAUSE_MENU_SELECTION_DATA` (`GetPauseMenuSelectionData`)

---
### GetMenuPedBoolStat

`GET_MENU_PED_BOOL_STAT` · hash `0x052991E59076E4E4` · jhash `0xD43BB56D` · **Cliente**

```lua
local retval, p1 = GetMenuPedBoolStat(p0, p1)
```
```c
BOOL GET_MENU_PED_BOOL_STAT(Hash p0, Any* p1);
```

**Parámetros**

- `p0` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p0 was always 0xAE2602A3.
```

**Nombres antiguos (alias):** `0x052991E59076E4E4` (`N_0x052991e59076e4e4`)

---
### GetMenuPedFloatStat

`GET_MENU_PED_FLOAT_STAT` · hash `0x5FBD7095FE7AE57F` · jhash `0x51972B04` · **Cliente**

```lua
local retval, p1 = GetMenuPedFloatStat(p0, p1)
```
```c
BOOL GET_MENU_PED_FLOAT_STAT(Any p0, float* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5FBD7095FE7AE57F` (`N_0x5fbd7095fe7ae57f`)

---
### GetMenuPedIntStat

`GET_MENU_PED_INT_STAT` · hash `0xEF4CED81CEBEDC6D` · jhash `0x4370999E` · **Cliente**

```lua
local retval, p1 = GetMenuPedIntStat(p0, p1)
```
```c
BOOL GET_MENU_PED_INT_STAT(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `SET_USERIDS_UIHIDDEN` (`SetUseridsUihidden`), `0xEF4CED81CEBEDC6D` (`N_0xef4ced81cebedc6d`)

---
### GetMenuPedMaskedIntStat

`GET_MENU_PED_MASKED_INT_STAT` · hash `0x90A6526CF0381030` · jhash `0xD6CC4766` · **Cliente**

```lua
local retval, p1 = GetMenuPedMaskedIntStat(p0, p2, p3)
```
```c
BOOL GET_MENU_PED_MASKED_INT_STAT(Any p0, Any* p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x90A6526CF0381030` (`N_0x90a6526cf0381030`)

---
### GetMinimapFowCoordinateIsRevealed

`GET_MINIMAP_FOW_COORDINATE_IS_REVEALED` · hash `0x6E31B91145873922` · jhash `0x65B705F6` · **Cliente**

```lua
local retval = GetMinimapFowCoordinateIsRevealed(x, y, z)
```
```c
BOOL GET_MINIMAP_FOW_COORDINATE_IS_REVEALED(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6E31B91145873922` (`N_0x6e31b91145873922`), `_IS_MINIMAP_AREA_REVEALED` (`IsMinimapAreaRevealed`)

---
### GetMinimapFowDiscoveryRatio

`GET_MINIMAP_FOW_DISCOVERY_RATIO` · hash `0xE0130B41D3CF4574` · jhash `0xA4098ACC` · **Cliente**

```lua
local retval = GetMinimapFowDiscoveryRatio()
```
```c
float GET_MINIMAP_FOW_DISCOVERY_RATIO();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xE0130B41D3CF4574` (`N_0xe0130b41d3cf4574`), `_GET_MINIMAP_REVEAL_PERCENTAGE` (`GetMinimapRevealPercentage`)

---
### GetMouseEvent

`GET_MOUSE_EVENT` · hash `0x632B2940C67F4EA9` · **Cliente**

```lua
local retval, received, selectionType, context, slotIndex = GetMouseEvent(scaleformHandle)
```
```c
BOOL GET_MOUSE_EVENT(int scaleformHandle, bool* received, int* selectionType, int* context, int* slotIndex);
```

**Parámetros**

- `scaleformHandle` (`int`): Handle of the scaleform
- `received` (`bool*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Returns a boolean indicating if the data was received successfully (in Lua).
- `selectionType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The type of MouseEvent specified above.
- `context` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Context of the slot the mouse is hovering on.
- `slotIndex` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Index of the slot the mouse is hovering on.

**Devuelve:** `BOOL` — *   **retVal** Returns true if MOUSE_EVENT callback from Scaleforms has been called.

**Descripción oficial:**

Gets mouse event data from scaleforms with mouse support. Must be checked every frame.
Returns item index if using the COLOUR_SWITCHER\_02 scaleform.
Selection types, found in MOUSE_EVENTS.as:
MOUSE_DRAG_OUT = 0;
MOUSE_DRAG_OVER = 1;
MOUSE_DOWN = 2;
MOUSE_MOVE = 3;
MOUSE_UP = 4;
MOUSE_PRESS = 5;
MOUSE_RELEASE = 6;
MOUSE_RELEASE_OUTSIDE = 7;
MOUSE_ROLL_OUT = 8;
MOUSE_ROLL_OVER = 9;
MOUSE_WHEEL_UP = 10;
MOUSE_WHEEL_DOWN = 11;

Scaleforms that this works with:

*   COLOUR_SWITCHER\_02
*   MP_RESULTS_PANEL
*   MP_NEXT_JOB_SELECTION
*   SC_LEADERBOARD
    Probably works with other scaleforms, needs more research.
    In order to use this Native you MUST have controls 239, 240, 237, 238 enabled!
    This native, due to its erroneous redundancy of the returned boolean value, works differently in C#: shifting the parameters (where `received` becomes `selectionType` and so on making the fourth parameter unused and always 0).

**Nombres antiguos (alias):** `0x632B2940C67F4EA9` (`N_0x632b2940c67f4ea9`), `_GET_SCALEFORM_MOVIE_CURSOR_SELECTION` (`GetScaleformMovieCursorSelection`)

**Ejemplo (lua):**

```lua
local success, _eventType, _context, _itemId = GetMouseEvent(scaleform)
```

**Ejemplo (cs):**

```cs
int eventType = 0;
int itemId = 0;
int context = 0;
int unused = 0;

var success = GetMouseEvent(scaleform.Handle, ref eventType, ref context, ref itemId, ref unused);
```

---
### GetNamedRendertargetRenderId

`GET_NAMED_RENDERTARGET_RENDER_ID` · hash `0x1A6478B61C6BDC3B` · jhash `0xF9D7A401` · **Cliente**

```lua
local retval = GetNamedRendertargetRenderId(name)
```
```c
int GET_NAMED_RENDERTARGET_RENDER_ID(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `int`

---
### GetNewSelectedMissionCreatorBlip

`GET_NEW_SELECTED_MISSION_CREATOR_BLIP` · hash `0x5C90988E7C8E1AF4` · jhash `0xFFD7476C` · **Cliente**

```lua
local retval = GetNewSelectedMissionCreatorBlip()
```
```c
Blip GET_NEW_SELECTED_MISSION_CREATOR_BLIP();
```

**Devuelve:** `Blip`

**Nombres antiguos (alias):** `DISABLE_BLIP_NAME_FOR_VAR` (`DisableBlipNameForVar`), `0x5C90988E7C8E1AF4` (`N_0x5c90988e7c8e1af4`)

---
### GetNextBlipInfoId

`GET_NEXT_BLIP_INFO_ID` · hash `0x14F96AA50D6FBEA7` · jhash `0x9356E92F` · **Cliente**

```lua
local retval = GetNextBlipInfoId(blipSprite)
```
```c
Blip GET_NEXT_BLIP_INFO_ID(int blipSprite);
```

**Parámetros**

- `blipSprite` (`int`): Sprite ID, see the [Game Reference](https://docs.fivem.net/docs/game-references/blips/) for the full list.

**Devuelve:** `Blip` — Returns the next blip ID in an interator that has the specified blip sprite.

**Ejemplo (lua):**

```lua
function GetAllBlipsWithSprite(blip_sprite)
  local current_blip = GetFirstBlipInfoId(blip_sprite)
  local blips_array = {}

  if not DoesBlipExist(current_blip) then 
    print('there are no blips with this sprite set') 
    return blips_array 
  end

  while DoesBlipExist(current_blip) do
    table.insert(blips_array, current_blip)
    current_blip = GetNextBlipInfoId(blip_sprite)
  end

  return blips_array
end
```

---
### GetNorthRadarBlip

`_GET_NORTH_RADAR_BLIP` · hash `0x3F0CF9CB7E589B88` · **Cliente**

```lua
local retval = GetNorthRadarBlip()
```
```c
Blip _GET_NORTH_RADAR_BLIP();
```

**Devuelve:** `Blip`

**Nombres antiguos (alias):** `0x3F0CF9CB7E589B88` (`N_0x3f0cf9cb7e589b88`)

---
### GetNumberOfActiveBlips

`GET_NUMBER_OF_ACTIVE_BLIPS` · hash `0x9A3FF3DE163034E8` · jhash `0x144020FA` · **Cliente**

```lua
local retval = GetNumberOfActiveBlips()
```
```c
int GET_NUMBER_OF_ACTIVE_BLIPS();
```

**Devuelve:** `int`

---
### GetPauseMenuPosition

`GET_PAUSE_MENU_POSITION` · hash `0x5BFF36D6ED83E0AE` · **Cliente**

```lua
local retval = GetPauseMenuPosition()
```
```c
Vector3 GET_PAUSE_MENU_POSITION();
```

**Devuelve:** `Vector3` — This function returns the starting position (Top left) of the Pause Menu's body.

**Nombres antiguos (alias):** `_GET_PAUSE_MENU_CURSOR_POSITION` (`GetPauseMenuCursorPosition`), `0x5BFF36D6ED83E0AE` (`N_0x5bff36d6ed83e0ae`)

---
### GetPauseMenuSelection

`_GET_PAUSE_MENU_SELECTION` · hash `0x36C1451A88A09630` · jhash `0x8543AAC8` · **Cliente**

```lua
local lastItemMenuId, selectedItemUniqueId = GetPauseMenuSelection()
```
```c
void _GET_PAUSE_MENU_SELECTION(int* lastItemMenuId, int* selectedItemUniqueId);
```

**Parámetros**

- `lastItemMenuId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `selectedItemUniqueId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x36C1451A88A09630` (`N_0x36c1451a88a09630`)

---
### GetPauseMenuState

`GET_PAUSE_MENU_STATE` · hash `0x272ACD84970869C5` · jhash `0x92F50134` · **Cliente**

```lua
local retval = GetPauseMenuState()
```
```c
int GET_PAUSE_MENU_STATE();
```

**Devuelve:** `int`

**Descripción oficial:**

```cpp
enum ePauseMenuState
{
    PM_INACTIVE 	 =  0,
    PM_STARTING_UP 	 =  5,
    PM_RESTARTING 	 = 10,
    PM_READY 		 = 15,
    PM_IN_STORE 	 = 20,
    PM_IN_SC_MENU 	 = 25,
    PM_SHUTTING_DOWN = 30,
    PM_IN_VIDEOEDITOR = 35,
}
```

---
### GetRenderedCharacterHeight

`GET_RENDERED_CHARACTER_HEIGHT` · hash `0xDB88A37483346780` · jhash `0x3330175B` · **Cliente**

```lua
local retval = GetRenderedCharacterHeight(size, font)
```
```c
float GET_RENDERED_CHARACTER_HEIGHT(float size, int font);
```

**Parámetros**

- `size` (`float`)
- `font` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

```
This gets the height of the FONT and not the total text. You need to get the number of lines your text uses, and get the height of a newline (I'm using a smaller value) to get the total text height.
Old name: _GET_TEXT_SCALE_HEIGHT
```

**Nombres antiguos (alias):** `0xDB88A37483346780` (`N_0xdb88a37483346780`), `_GET_TEXT_SCALE_HEIGHT` (`GetTextScaleHeight`)

---
### GetStandardBlipEnumId

`GET_STANDARD_BLIP_ENUM_ID` · hash `0x4A9923385BDB9DAD` · jhash `0x87871CE0` · **Cliente**

```lua
local retval = GetStandardBlipEnumId()
```
```c
int GET_STANDARD_BLIP_ENUM_ID();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x4A9923385BDB9DAD` (`N_0x4a9923385bdb9dad`), `_GET_LEVEL_BLIP_SPRITE` (`GetLevelBlipSprite`)

---
### GetStreetNameFromHashKey

`GET_STREET_NAME_FROM_HASH_KEY` · hash `0xD0EF8A959B8A4CB9` · jhash `0x1E8E310C` · **Cliente**

```lua
local retval = GetStreetNameFromHashKey(hash)
```
```c
char* GET_STREET_NAME_FROM_HASH_KEY(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `char*`

**Descripción oficial:**

Converts the hash of a street name into a readable string. To retrieve a hash for a given (street) coordinate, see [`GET_STREET_NAME_AT_COORD`](PATHFIND.md#getstreetnameatcoord).

---
### GetTextSubstring

`_GET_TEXT_SUBSTRING` · hash `0x169BD9382084C8C0` · jhash `0x34A396EE` · **Cliente**

```lua
local retval = GetTextSubstring(text, position, length)
```
```c
char* _GET_TEXT_SUBSTRING(char* text, int position, int length);
```

**Parámetros**

- `text` (`char*`)
- `position` (`int`)
- `length` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns a substring of a specified length starting at a specified position.
Example:
// Get "STRING" text from "MY_STRING"
subStr = HUD::_GET_TEXT_SUBSTRING("MY_STRING", 3, 6);
```

---
### GetTextSubstringSafe

`_GET_TEXT_SUBSTRING_SAFE` · hash `0xB2798643312205C5` · jhash `0x0183A66C` · **Cliente**

```lua
local retval = GetTextSubstringSafe(text, position, length, maxLength)
```
```c
char* _GET_TEXT_SUBSTRING_SAFE(char* text, int position, int length, int maxLength);
```

**Parámetros**

- `text` (`char*`)
- `position` (`int`)
- `length` (`int`)
- `maxLength` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns a substring of a specified length starting at a specified position. The result is guaranteed not to exceed the specified max length.
NOTE: The 'maxLength' parameter might actually be the size of the buffer that is returned. More research is needed. -CL69
Example:
// Condensed example of how Rockstar uses this function
strLen = HUD::GET_LENGTH_OF_LITERAL_STRING(MISC::GET_ONSCREEN_KEYBOARD_RESULT());
subStr = HUD::_GET_TEXT_SUBSTRING_SAFE(MISC::GET_ONSCREEN_KEYBOARD_RESULT(), 0, strLen, 63);
--
"fm_race_creator.ysc", line 85115:
// parameters modified for clarity
BOOL sub_8e5aa(char *text, int length) {
    for (i = 0; i <= (length - 2); i += 1) {
        if (!MISC::ARE_STRINGS_EQUAL(HUD::_GET_TEXT_SUBSTRING_SAFE(text, i, i + 1, 1), " ")) {
            return FALSE;
        }
    }
    return TRUE;
}
```

---
### GetTextSubstringSlice

`_GET_TEXT_SUBSTRING_SLICE` · hash `0xCE94AEBA5D82908A` · jhash `0xFA6373BB` · **Cliente**

```lua
local retval = GetTextSubstringSlice(text, startPosition, endPosition)
```
```c
char* _GET_TEXT_SUBSTRING_SLICE(char* text, int startPosition, int endPosition);
```

**Parámetros**

- `text` (`char*`)
- `startPosition` (`int`)
- `endPosition` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns a substring that is between two specified positions. The length of the string will be calculated using (endPosition - startPosition).
Example:
// Get "STRING" text from "MY_STRING"
subStr = HUD::_GET_TEXT_SUBSTRING_SLICE("MY_STRING", 3, 9);
// Overflows are possibly replaced with underscores (needs verification)
subStr = HUD::_GET_TEXT_SUBSTRING_SLICE("MY_STRING", 3, 10); // "STRING_"?
```

---
### GetWarningMessageTitleHash

`_GET_WARNING_MESSAGE_TITLE_HASH` · hash `0x81DF9ABA6C83DFF9` · **Cliente**

```lua
local retval = GetWarningMessageTitleHash()
```
```c
Hash _GET_WARNING_MESSAGE_TITLE_HASH();
```

**Devuelve:** `Hash`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### GetWaypointBlipEnumId

`GET_WAYPOINT_BLIP_ENUM_ID` · hash `0x186E5D252FA50E7D` · jhash `0xB9827942` · **Cliente**

```lua
local retval = GetWaypointBlipEnumId()
```
```c
int GET_WAYPOINT_BLIP_ENUM_ID();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `_GET_BLIP_INFO_ID_ITERATOR` (`GetBlipInfoIdIterator`)

---
### GivePedToPauseMenu

`GIVE_PED_TO_PAUSE_MENU` · hash `0xAC0BFBDC3BE00E14` · jhash `0x2AD2C9CE` · **Cliente**

```lua
GivePedToPauseMenu(ped, p1)
```
```c
void GIVE_PED_TO_PAUSE_MENU(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is either 1 or 2 in the PC scripts.  
```

This native is used to "give"/duplicate a player ped to a frontend menu as configured via the `ACTIVATE_FRONTEND_MENU` native, you first must utilize the [CLONE_PED](PED-1.md#cloneped) to clone said ped.

---
### HasAdditionalTextLoaded

`HAS_ADDITIONAL_TEXT_LOADED` · hash `0x02245FE4BED318B8` · jhash `0xB0E56045` · **Cliente**

```lua
local retval = HasAdditionalTextLoaded(slot)
```
```c
BOOL HAS_ADDITIONAL_TEXT_LOADED(int slot);
```

**Parámetros**

- `slot` (`int`)

**Devuelve:** `BOOL`

---
### HasDirectorModeBeenTriggered

`_HAS_DIRECTOR_MODE_BEEN_TRIGGERED` · hash `0xA277800A9EAE340E` · **Cliente**

```lua
local retval = HasDirectorModeBeenTriggered()
```
```c
BOOL _HAS_DIRECTOR_MODE_BEEN_TRIGGERED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
HAS_*
```

**Nombres antiguos (alias):** `0xA277800A9EAE340E` (`N_0xa277800a9eae340e`)

---
### HasMenuLayoutChangedEventOccurred

`HAS_MENU_LAYOUT_CHANGED_EVENT_OCCURRED` · hash `0x2E22FEFA0100275E` · jhash `0x96863460` · **Cliente**

```lua
local retval = HasMenuLayoutChangedEventOccurred()
```
```c
BOOL HAS_MENU_LAYOUT_CHANGED_EVENT_OCCURRED();
```

**Devuelve:** `BOOL` — Returns true every frame when a layout change event is active. Do note you can only check this with one script at a time. Layout change events become active whenever the player navigates the menu up or down.

**Descripción oficial:**

Make sure to use [`GET_MENU_LAYOUT_CHANGED_EVENT_DETAILS`](#getmenulayoutchangedeventdetails) when this function returns true in a frame.

**Nombres antiguos (alias):** `0x2E22FEFA0100275E` (`N_0x2e22fefa0100275e`)

---
### HasThisAdditionalTextLoaded

`HAS_THIS_ADDITIONAL_TEXT_LOADED` · hash `0xADBF060E2B30C5BC` · jhash `0x80A52040` · **Cliente**

```lua
local retval = HasThisAdditionalTextLoaded(gxt, slot)
```
```c
BOOL HAS_THIS_ADDITIONAL_TEXT_LOADED(char* gxt, int slot);
```

**Parámetros**

- `gxt` (`char*`)
- `slot` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if the specified gxt has loaded into the passed slot.  
```

---
### HideAreaAndVehicleNameThisFrame

`_HIDE_AREA_AND_VEHICLE_NAME_THIS_FRAME` · hash `0xA4DEDE28B1814289` · jhash `0x52746FE1` · **Cliente**

```lua
HideAreaAndVehicleNameThisFrame()
```
```c
void _HIDE_AREA_AND_VEHICLE_NAME_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
HIDE_*_THIS_FRAME

Hides area and vehicle name HUD components for one frame.
```

**Nombres antiguos (alias):** `0xA4DEDE28B1814289` (`N_0xa4dede28b1814289`)

---
### HideHelpTextThisFrame

`HIDE_HELP_TEXT_THIS_FRAME` · hash `0xD46923FC481CA285` · jhash `0xF3807BED` · **Cliente**

```lua
HideHelpTextThisFrame()
```
```c
void HIDE_HELP_TEXT_THIS_FRAME();
```

**Devuelve:** `void`

---
### HideHudAndRadarThisFrame

`HIDE_HUD_AND_RADAR_THIS_FRAME` · hash `0x719FF505F097FD20` · jhash `0xB75D4AD2` · **Cliente**

```lua
HideHudAndRadarThisFrame()
```
```c
void HIDE_HUD_AND_RADAR_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
I think this works, but seems to prohibit switching to other weapons (or accessing the weapon wheel)  
```

---
### HideHudComponentThisFrame

`HIDE_HUD_COMPONENT_THIS_FRAME` · hash `0x6806C51AD12B83B8` · jhash `0xDB2D0762` · **Cliente**

```lua
HideHudComponentThisFrame(id)
```
```c
void HIDE_HUD_COMPONENT_THIS_FRAME(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

This function hides various HUD (Heads-up Display) components.

Listed below are the integers and the corresponding HUD component.

*   1 : WANTED_STARS
*   2 : WEAPON_ICON
*   3 : CASH
*   4 : MP_CASH
*   5 : MP_MESSAGE
*   6 : VEHICLE_NAME
*   7 : AREA_NAME
*   8 : VEHICLE_CLASS
*   9 : STREET_NAME
*   10 : HELP_TEXT
*   11 : FLOATING_HELP_TEXT\_1
*   12 : FLOATING_HELP_TEXT\_2
*   13 : CASH_CHANGE
*   14 : RETICLE
*   15 : SUBTITLE_TEXT
*   16 : RADIO_STATIONS
*   17 : SAVING_GAME
*   18 : GAME_STREAM
*   19 : WEAPON_WHEEL
*   20 : WEAPON_WHEEL_STATS
*   21 : HUD_COMPONENTS
*   22 : HUD_WEAPONS

These integers also work for the [`SHOW_HUD_COMPONENT_THIS_FRAME`](#showhudcomponentthisframe) native, but instead shows the HUD Component.

---
### HideLoadingOnFadeThisFrame

`HIDE_LOADING_ON_FADE_THIS_FRAME` · hash `0x4B0311D3CDC4648F` · jhash `0x35087963` · **Cliente**

```lua
HideLoadingOnFadeThisFrame()
```
```c
void HIDE_LOADING_ON_FADE_THIS_FRAME();
```

**Devuelve:** `void`

---
### HideMinimapExteriorMapThisFrame

`HIDE_MINIMAP_EXTERIOR_MAP_THIS_FRAME` · hash `0x5FBAE526203990C9` · jhash `0x1A4318F7` · **Cliente**

```lua
HideMinimapExteriorMapThisFrame()
```
```c
void HIDE_MINIMAP_EXTERIOR_MAP_THIS_FRAME();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `_DISABLE_RADAR_THIS_FRAME` (`DisableRadarThisFrame`)

---
### HideMinimapInteriorMapThisFrame

`HIDE_MINIMAP_INTERIOR_MAP_THIS_FRAME` · hash `0x20FE7FDFEEAD38C0` · jhash `0xCE36E3FE` · **Cliente**

```lua
HideMinimapInteriorMapThisFrame()
```
```c
void HIDE_MINIMAP_INTERIOR_MAP_THIS_FRAME();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x20FE7FDFEEAD38C0` (`N_0x20fe7fdfeead38c0`)

---
### HideNumberOnBlip

`HIDE_NUMBER_ON_BLIP` · hash `0x532CFF637EF80148` · jhash `0x0B6D610D` · **Cliente**

```lua
HideNumberOnBlip(blip)
```
```c
void HIDE_NUMBER_ON_BLIP(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `void`

---
### HideScriptedHudComponentThisFrame

`HIDE_SCRIPTED_HUD_COMPONENT_THIS_FRAME` · hash `0xE374C498D8BADC14` · jhash `0x31ABA127` · **Cliente**

```lua
HideScriptedHudComponentThisFrame(id)
```
```c
void HIDE_SCRIPTED_HUD_COMPONENT_THIS_FRAME(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

---
### HudDisplayLoadingScreenTips

`_HUD_DISPLAY_LOADING_SCREEN_TIPS` · hash `0x488043841BBE156F` · **Cliente**

```lua
HudDisplayLoadingScreenTips()
```
```c
void _HUD_DISPLAY_LOADING_SCREEN_TIPS();
```

**Devuelve:** `void`

**Descripción oficial:**

Displays loading screen tips.
Seems to do the same as [`_THEFEED_DISPLAY_LOADING_SCREEN_TIPS`](#thefeeddisplayloadingscreentips).
Requires [`THEFEED_AUTO_POST_GAMETIPS_ON`](#thefeedautopostgametipson) to be called beforehand.
Call [`_THEFEED_DISABLE_LOADING_SCREEN_TIPS`](#thefeeddisableloadingscreentips) to disable immediately, or [`THEFEED_AUTO_POST_GAMETIPS_OFF`](#thefeedautopostgametipsoff) to disable after the current tip.

Example result:
![](https://i.imgur.com/hzaHuPb.png)

**Nombres antiguos (alias):** `0x488043841BBE156F` (`N_0x488043841bbe156f`)

**Ejemplo (lua):**

```lua
HudDisplayLoadingScreenTips()
```

---
### HudForceWeaponWheel

`HUD_FORCE_WEAPON_WHEEL` · hash `0xEB354E5376BC81A7` · jhash `0x1EFFB02A` · **Cliente**

```lua
HudForceWeaponWheel(show)
```
```c
void HUD_FORCE_WEAPON_WHEEL(BOOL show);
```

**Parámetros**

- `show` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Forces the weapon wheel to show/hide.
```

**Nombres antiguos (alias):** `0xEB354E5376BC81A7` (`N_0xeb354e5376bc81a7`), `_SHOW_WEAPON_WHEEL` (`ShowWeaponWheel`)

---
### HudSetWeaponWheelTopSlot

`HUD_SET_WEAPON_WHEEL_TOP_SLOT` · hash `0x72C1056D678BB7D8` · jhash `0x83B608A0` · **Cliente**

```lua
HudSetWeaponWheelTopSlot(weaponHash)
```
```c
void HUD_SET_WEAPON_WHEEL_TOP_SLOT(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Set the active slotIndex in the wheel weapon to the slot associated with the provided Weapon hash
```

**Nombres antiguos (alias):** `0x72C1056D678BB7D8` (`N_0x72c1056d678bb7d8`), `_HUD_WEAPON_WHEEL_SET_SLOT_HASH` (`HudWeaponWheelSetSlotHash`)

---
### HudWeaponWheelGetSelectedHash

`_HUD_WEAPON_WHEEL_GET_SELECTED_HASH` · hash `0xA48931185F0536FE` · jhash `0x22E9F555` · **Cliente**

```lua
local retval = HudWeaponWheelGetSelectedHash()
```
```c
Hash _HUD_WEAPON_WHEEL_GET_SELECTED_HASH();
```

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns the weapon hash to the selected/highlighted weapon in the wheel
```

**Nombres antiguos (alias):** `0xA48931185F0536FE` (`N_0xa48931185f0536fe`)

---
### HudWeaponWheelGetSlotHash

`_HUD_WEAPON_WHEEL_GET_SLOT_HASH` · hash `0xA13E93403F26C812` · **Cliente**

```lua
local retval = HudWeaponWheelGetSlotHash(weaponTypeIndex)
```
```c
Hash _HUD_WEAPON_WHEEL_GET_SLOT_HASH(int weaponTypeIndex);
```

**Parámetros**

- `weaponTypeIndex` (`int`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns the weapon hash active in a specific weapon wheel slotList
```

**Nombres antiguos (alias):** `0xA13E93403F26C812` (`N_0xa13e93403f26c812`)

---
### HudWeaponWheelIgnoreControlInput

`_HUD_WEAPON_WHEEL_IGNORE_CONTROL_INPUT` · hash `0x14C9FDCC41F81F63` · jhash `0xE70D1F43` · **Cliente**

```lua
HudWeaponWheelIgnoreControlInput(toggle)
```
```c
void _HUD_WEAPON_WHEEL_IGNORE_CONTROL_INPUT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets a global that disables many weapon input tasks (shooting, aiming, etc.). Does not work with vehicle weapons, only used in selector.ysc
```

**Nombres antiguos (alias):** `0x14C9FDCC41F81F63` (`N_0x14c9fdcc41f81f63`)

---
### HudWeaponWheelIgnoreSelection

`_HUD_WEAPON_WHEEL_IGNORE_SELECTION` · hash `0x0AFC4AF510774B47` · jhash `0xB26FED2B` · **Cliente**

```lua
HudWeaponWheelIgnoreSelection()
```
```c
void _HUD_WEAPON_WHEEL_IGNORE_SELECTION();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Calling this each frame, stops the player from receiving a weapon via the weapon wheel.
```

**Nombres antiguos (alias):** `_BLOCK_WEAPON_WHEEL_THIS_FRAME` (`BlockWeaponWheelThisFrame`), `0x0AFC4AF510774B47` (`N_0x0afc4af510774b47`)

---
### IsBlipFlashing

`IS_BLIP_FLASHING` · hash `0xA5E41FD83AD6CEF0` · jhash `0x52E111D7` · **Cliente**

```lua
local retval = IsBlipFlashing(blip)
```
```c
BOOL IS_BLIP_FLASHING(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `BOOL`

---
### IsBlipOnMinimap

`IS_BLIP_ON_MINIMAP` · hash `0xE41CA53051197A27` · jhash `0x258CBA3A` · **Cliente**

```lua
local retval = IsBlipOnMinimap(blip)
```
```c
BOOL IS_BLIP_ON_MINIMAP(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `BOOL`

---
### IsBlipShortRange

`IS_BLIP_SHORT_RANGE` · hash `0xDA5F8727EB75B926` · jhash `0x1226765A` · **Cliente**

```lua
local retval = IsBlipShortRange(blip)
```
```c
BOOL IS_BLIP_SHORT_RANGE(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `BOOL`

---
### IsFloatingHelpTextOnScreen

`IS_FLOATING_HELP_TEXT_ON_SCREEN` · hash `0x2432784ACA090DA4` · jhash `0x45472FD5` · **Cliente**

```lua
local retval = IsFloatingHelpTextOnScreen(hudIndex)
```
```c
BOOL IS_FLOATING_HELP_TEXT_ON_SCREEN(int hudIndex);
```

**Parámetros**

- `hudIndex` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2432784ACA090DA4` (`N_0x2432784aca090da4`)

---
### IsFrontendReadyForControl

`IS_FRONTEND_READY_FOR_CONTROL` · hash `0x3BAB9A4E4F2FF5C7` · jhash `0xD3BF3ABD` · **Cliente**

```lua
local retval = IsFrontendReadyForControl()
```
```c
BOOL IS_FRONTEND_READY_FOR_CONTROL();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3BAB9A4E4F2FF5C7` (`N_0x3bab9a4e4f2ff5c7`)

---
### IsHelpMessageBeingDisplayed

`IS_HELP_MESSAGE_BEING_DISPLAYED` · hash `0x4D79439A6B55AC67` · jhash `0xA65F262A` · **Cliente**

```lua
local retval = IsHelpMessageBeingDisplayed()
```
```c
BOOL IS_HELP_MESSAGE_BEING_DISPLAYED();
```

**Devuelve:** `BOOL`

---
### IsHelpMessageFadingOut

`IS_HELP_MESSAGE_FADING_OUT` · hash `0x327EDEEEAC55C369` · jhash `0x3E50AE92` · **Cliente**

```lua
local retval = IsHelpMessageFadingOut()
```
```c
BOOL IS_HELP_MESSAGE_FADING_OUT();
```

**Devuelve:** `BOOL`

---
### IsHelpMessageOnScreen

`IS_HELP_MESSAGE_ON_SCREEN` · hash `0xDAD37F45428801AE` · jhash `0x4B3C9CA9` · **Cliente**

```lua
local retval = IsHelpMessageOnScreen()
```
```c
BOOL IS_HELP_MESSAGE_ON_SCREEN();
```

**Devuelve:** `BOOL`

---
### IsHoveringOverMissionCreatorBlip

`IS_HOVERING_OVER_MISSION_CREATOR_BLIP` · hash `0x4167EFE0527D706E` · jhash `0xC5EB849A` · **Cliente**

```lua
local retval = IsHoveringOverMissionCreatorBlip()
```
```c
BOOL IS_HOVERING_OVER_MISSION_CREATOR_BLIP();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4167EFE0527D706E` (`N_0x4167efe0527d706e`)

---
### IsHudComponentActive

`IS_HUD_COMPONENT_ACTIVE` · hash `0xBC4C9EA5391ECC0D` · jhash `0x6214631F` · **Cliente**

```lua
local retval = IsHudComponentActive(id)
```
```c
BOOL IS_HUD_COMPONENT_ACTIVE(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Full list of components below  
HUD = 0;  
HUD_WANTED_STARS = 1;  
HUD_WEAPON_ICON = 2;  
HUD_CASH = 3;  
HUD_MP_CASH = 4;  
HUD_MP_MESSAGE = 5;  
HUD_VEHICLE_NAME = 6;  
HUD_AREA_NAME = 7;  
HUD_VEHICLE_CLASS = 8;  
HUD_STREET_NAME = 9;  
HUD_HELP_TEXT = 10;  
HUD_FLOATING_HELP_TEXT_1 = 11;  
HUD_FLOATING_HELP_TEXT_2 = 12;  
HUD_CASH_CHANGE = 13;  
HUD_RETICLE = 14;  
HUD_SUBTITLE_TEXT = 15;  
HUD_RADIO_STATIONS = 16;  
HUD_SAVING_GAME = 17;  
HUD_GAME_STREAM = 18;  
HUD_WEAPON_WHEEL = 19;  
HUD_WEAPON_WHEEL_STATS = 20;  
MAX_HUD_COMPONENTS = 21;  
MAX_HUD_WEAPONS = 22;  
MAX_SCRIPTED_HUD_COMPONENTS = 141;  
```

---
### IsHudHidden

`IS_HUD_HIDDEN` · hash `0xA86478C6958735C5` · jhash `0x40BADA1D` · **Cliente**

```lua
local retval = IsHudHidden()
```
```c
BOOL IS_HUD_HIDDEN();
```

**Devuelve:** `BOOL`

---
### IsHudPreferenceSwitchedOn

`IS_HUD_PREFERENCE_SWITCHED_ON` · hash `0x1930DFA731813EC4` · jhash `0xC3BC1B4F` · **Cliente**

```lua
local retval = IsHudPreferenceSwitchedOn()
```
```c
BOOL IS_HUD_PREFERENCE_SWITCHED_ON();
```

**Devuelve:** `BOOL`

---
### IsMessageBeingDisplayed

`IS_MESSAGE_BEING_DISPLAYED` · hash `0x7984C03AA5CC2F41` · jhash `0x6A77FE8D` · **Cliente**

```lua
local retval = IsMessageBeingDisplayed()
```
```c
BOOL IS_MESSAGE_BEING_DISPLAYED();
```

**Devuelve:** `BOOL`

---
### IsMinimapRendering

`IS_MINIMAP_RENDERING` · hash `0xAF754F20EB5CD51A` · jhash `0x9CD18314` · **Cliente**

```lua
local retval = IsMinimapRendering()
```
```c
BOOL IS_MINIMAP_RENDERING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xAF754F20EB5CD51A` (`N_0xaf754f20eb5cd51a`), `_IS_RADAR_ENABLED` (`IsRadarEnabled`)

---
### IsMissionCreatorBlip

`IS_MISSION_CREATOR_BLIP` · hash `0x26F49BF3381D933D` · jhash `0x24ACC4E9` · **Cliente**

```lua
local retval = IsMissionCreatorBlip(blip)
```
```c
BOOL IS_MISSION_CREATOR_BLIP(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `BOOL`

---
### IsMouseRolledOverInstructionalButtons

`IS_MOUSE_ROLLED_OVER_INSTRUCTIONAL_BUTTONS` · hash `0x3D9ACB1EB139E702` · **Cliente**

```lua
local retval = IsMouseRolledOverInstructionalButtons()
```
```c
BOOL IS_MOUSE_ROLLED_OVER_INSTRUCTIONAL_BUTTONS();
```

**Devuelve:** `BOOL` — Returns `true` if the cursor is hovering above instructional buttons.

**Descripción oficial:**

**Note:** The buttons need to support mouse (with the `TOGGLE_MOUSE_SUPPORT` scaleform movie method) for it to return `true`.

**Nombres antiguos (alias):** `0x3D9ACB1EB139E702` (`N_0x3d9acb1eb139e702`), `_IS_MOUSE_CURSOR_ABOVE_INSTRUCTIONAL_BUTTONS` (`IsMouseCursorAboveInstructionalButtons`)

---
### IsMpGamerTagActive

`IS_MP_GAMER_TAG_ACTIVE` · hash `0x4E929E7A5796FD26` · jhash `0x60118951` · **Cliente**

```lua
local retval = IsMpGamerTagActive(gamerTagId)
```
```c
BOOL IS_MP_GAMER_TAG_ACTIVE(int gamerTagId);
```

**Parámetros**

- `gamerTagId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4E929E7A5796FD26` (`N_0x4e929e7a5796fd26`)

---
### IsMpGamerTagFree

`IS_MP_GAMER_TAG_FREE` · hash `0x595B5178E412E199` · jhash `0x63959059` · **Cliente**

```lua
local retval = IsMpGamerTagFree(gamerTagId)
```
```c
BOOL IS_MP_GAMER_TAG_FREE(int gamerTagId);
```

**Parámetros**

- `gamerTagId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `ADD_TREVOR_RANDOM_MODIFIER` (`AddTrevorRandomModifier`)

---
### IsMpGamerTagMovieActive

`IS_MP_GAMER_TAG_MOVIE_ACTIVE` · hash `0x6E0EB3EB47C8D7AA` · jhash `0xEFD2564A` · **Cliente**

```lua
local retval = IsMpGamerTagMovieActive()
```
```c
BOOL IS_MP_GAMER_TAG_MOVIE_ACTIVE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6E0EB3EB47C8D7AA` (`N_0x6e0eb3eb47c8d7aa`), `_HAS_MP_GAMER_TAG` (`HasMpGamerTag`)

---
### IsMultiplayerChatActive

`_IS_MULTIPLAYER_CHAT_ACTIVE` · hash `0xB118AF58B5F332A1` · **Cliente**

```lua
local retval = IsMultiplayerChatActive()
```
```c
BOOL _IS_MULTIPLAYER_CHAT_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether or not the text chat (MULTIPLAYER_CHAT Scaleform component) is active.  
```

**Nombres antiguos (alias):** `_IS_TEXT_CHAT_ACTIVE` (`IsTextChatActive`)

---
### IsNamedRendertargetLinked

`IS_NAMED_RENDERTARGET_LINKED` · hash `0x113750538FA31298` · jhash `0x8B52601F` · **Cliente**

```lua
local retval = IsNamedRendertargetLinked(modelHash)
```
```c
BOOL IS_NAMED_RENDERTARGET_LINKED(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsNamedRendertargetRegistered

`IS_NAMED_RENDERTARGET_REGISTERED` · hash `0x78DCDC15C9F116B4` · jhash `0x284057F5` · **Cliente**

```lua
local retval = IsNamedRendertargetRegistered(name)
```
```c
BOOL IS_NAMED_RENDERTARGET_REGISTERED(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

---
### IsNavigatingMenuContent

`IS_NAVIGATING_MENU_CONTENT` · hash `0x4E3CD0EF8A489541` · jhash `0xDA7951A2` · **Cliente**

```lua
local retval = IsNavigatingMenuContent()
```
```c
Any IS_NAVIGATING_MENU_CONTENT();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x4E3CD0EF8A489541` (`N_0x4e3cd0ef8a489541`)

---
### IsOnlinePoliciesMenuActive

`IS_ONLINE_POLICIES_MENU_ACTIVE` · hash `0x6F72CD94F7B5B68C` · jhash `0x9D4934F4` · **Cliente**

```lua
local retval = IsOnlinePoliciesMenuActive()
```
```c
BOOL IS_ONLINE_POLICIES_MENU_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

Returns the same as `IS_SOCIAL_CLUB_ACTIVE`.

**Nombres antiguos (alias):** `0x6F72CD94F7B5B68C` (`N_0x6f72cd94f7b5b68c`)

---
### IsPauseMenuActive

`IS_PAUSE_MENU_ACTIVE` · hash `0xB0034A223497FFCB` · jhash `0xD3600591` · **Cliente**

```lua
local retval = IsPauseMenuActive()
```
```c
BOOL IS_PAUSE_MENU_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsPauseMenuRestarting

`IS_PAUSE_MENU_RESTARTING` · hash `0x1C491717107431C7` · jhash `0x3C4CF4D9` · **Cliente**

```lua
local retval = IsPauseMenuRestarting()
```
```c
BOOL IS_PAUSE_MENU_RESTARTING();
```

**Devuelve:** `BOOL`

---
### IsPausemapInInteriorMode

`IS_PAUSEMAP_IN_INTERIOR_MODE` · hash `0x9049FE339D5F6F6F` · jhash `0x199DED14` · **Cliente**

```lua
local retval = IsPausemapInInteriorMode()
```
```c
BOOL IS_PAUSEMAP_IN_INTERIOR_MODE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9049FE339D5F6F6F` (`N_0x9049fe339d5f6f6f`), `_IS_MINIMAP_IN_INTERIOR` (`IsMinimapInInterior`)

---
### IsRadarHidden

`IS_RADAR_HIDDEN` · hash `0x157F93B036700462` · jhash `0x1AB3B954` · **Cliente**

```lua
local retval = IsRadarHidden()
```
```c
BOOL IS_RADAR_HIDDEN();
```

**Devuelve:** `BOOL`

---
### IsRadarPreferenceSwitchedOn

`IS_RADAR_PREFERENCE_SWITCHED_ON` · hash `0x9EB6522EA68F22FE` · jhash `0x14AEAA28` · **Cliente**

```lua
local retval = IsRadarPreferenceSwitchedOn()
```
```c
BOOL IS_RADAR_PREFERENCE_SWITCHED_ON();
```

**Devuelve:** `BOOL`

---
### IsReportugcMenuOpen

`IS_REPORTUGC_MENU_OPEN` · hash `0x9135584D09A3437E` · jhash `0x9D2C94FA` · **Cliente**

```lua
local retval = IsReportugcMenuOpen()
```
```c
BOOL IS_REPORTUGC_MENU_OPEN();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9135584D09A3437E` (`N_0x9135584d09a3437e`)

---
### IsScriptedHudComponentActive

`IS_SCRIPTED_HUD_COMPONENT_ACTIVE` · hash `0xDD100EB17A94FF65` · jhash `0x2B86F382` · **Cliente**

```lua
local retval = IsScriptedHudComponentActive(id)
```
```c
BOOL IS_SCRIPTED_HUD_COMPONENT_ACTIVE(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

---
### IsScriptedHudComponentHiddenThisFrame

`IS_SCRIPTED_HUD_COMPONENT_HIDDEN_THIS_FRAME` · hash `0x09C0403ED9A751C2` · jhash `0xE8C8E535` · **Cliente**

```lua
local retval = IsScriptedHudComponentHiddenThisFrame(id)
```
```c
BOOL IS_SCRIPTED_HUD_COMPONENT_HIDDEN_THIS_FRAME(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x09C0403ED9A751C2` (`N_0x09c0403ed9a751c2`)

---
### IsSocialClubActive

`IS_SOCIAL_CLUB_ACTIVE` · hash `0xC406BE343FC4B9AF` · jhash `0xD4DA14EF` · **Cliente**

```lua
local retval = IsSocialClubActive()
```
```c
BOOL IS_SOCIAL_CLUB_ACTIVE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC406BE343FC4B9AF` (`N_0xc406be343fc4b9af`)

---
### IsStreamingAdditionalText

`IS_STREAMING_ADDITIONAL_TEXT` · hash `0x8B6817B71B85EBF0` · jhash `0xF079E4EB` · **Cliente**

```lua
local retval = IsStreamingAdditionalText(p0)
```
```c
BOOL IS_STREAMING_ADDITIONAL_TEXT(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

---
### IsSubtitlePreferenceSwitchedOn

`IS_SUBTITLE_PREFERENCE_SWITCHED_ON` · hash `0xAD6DACA4BA53E0A4` · jhash `0x63BA19F5` · **Cliente**

```lua
local retval = IsSubtitlePreferenceSwitchedOn()
```
```c
BOOL IS_SUBTITLE_PREFERENCE_SWITCHED_ON();
```

**Devuelve:** `BOOL`

---
### IsUpdatingMpGamerTagNameAndCrewDetails

`IS_UPDATING_MP_GAMER_TAG_NAME_AND_CREW_DETAILS` · hash `0xEB709A36958ABE0D` · jhash `0xF11414C4` · **Cliente**

```lua
local retval = IsUpdatingMpGamerTagNameAndCrewDetails(playerId)
```
```c
BOOL IS_UPDATING_MP_GAMER_TAG_NAME_AND_CREW_DETAILS(int playerId);
```

**Parámetros**

- `playerId` (`int`): Local ID of the player.

**Devuelve:** `BOOL` — Returns if game code is currently updating gamer tag and crew details for a player's name tag.

**Descripción oficial:**

When this native returns true, do not call [`SET_MP_GAMER_TAG_NAME`](#setmpgamertagname).

**Nombres antiguos (alias):** `0xEB709A36958ABE0D` (`N_0xeb709a36958abe0d`), `_HAS_MP_GAMER_TAG_2` (`HasMpGamerTag_2`), `_HAS_MP_GAMER_TAG_CREW_FLAGS_SET` (`HasMpGamerTagCrewFlagsSet`), `_IS_VALID_MP_GAMER_TAG_MOVIE` (`IsValidMpGamerTagMovie`)

---
### IsWarningMessageActive

`IS_WARNING_MESSAGE_ACTIVE` · hash `0xE18B138FABC53103` · jhash `0x94C834AD` · **Cliente**

```lua
local retval = IsWarningMessageActive()
```
```c
BOOL IS_WARNING_MESSAGE_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

Returns true if a Warning Message or ReportUGC menu is active.

**Nombres antiguos (alias):** `IS_MEDICAL_DISABLED` (`IsMedicalDisabled`)

---
### IsWarningMessageReadyForControl

`IS_WARNING_MESSAGE_READY_FOR_CONTROL` · hash `0xAF42195A42C63BBA` · **Cliente**

```lua
local retval = IsWarningMessageReadyForControl()
```
```c
BOOL IS_WARNING_MESSAGE_READY_FOR_CONTROL();
```

**Devuelve:** `BOOL` — Returns if the warning message scaleform/ui movie is loaded and ready to be controlled.

**Nombres antiguos (alias):** `0xAF42195A42C63BBA` (`N_0xaf42195a42c63bba`), `_IS_WARNING_MESSAGE_ACTIVE_2` (`IsWarningMessageActive_2`)

---
### IsWaypointActive

`IS_WAYPOINT_ACTIVE` · hash `0x1DD1F58F493F1DA5` · jhash `0x5E4DF47B` · **Cliente**

```lua
local retval = IsWaypointActive()
```
```c
BOOL IS_WAYPOINT_ACTIVE();
```

**Devuelve:** `BOOL`

---
### LinkNamedRendertarget

`LINK_NAMED_RENDERTARGET` · hash `0xF6C09E276AEB3F2D` · jhash `0x6844C4B9` · **Cliente**

```lua
LinkNamedRendertarget(modelHash)
```
```c
void LINK_NAMED_RENDERTARGET(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### LockMinimapAngle

`LOCK_MINIMAP_ANGLE` · hash `0x299FAEBB108AE05B` · jhash `0xDEC733E4` · **Cliente**

```lua
LockMinimapAngle(angle)
```
```c
void LOCK_MINIMAP_ANGLE(int angle);
```

**Parámetros**

- `angle` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Locks the minimap to the specified angle in integer degrees.  
angle: The angle in whole degrees. If less than 0 or greater than 360, unlocks the angle.  
```

---
### LockMinimapPosition

`LOCK_MINIMAP_POSITION` · hash `0x1279E861A329E73F` · jhash `0xB9632A91` · **Cliente**

```lua
LockMinimapPosition(x, y)
```
```c
void LOCK_MINIMAP_POSITION(float x, float y);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Locks the minimap to the specified world position.  
```

---
### LogDebugInfo

`_LOG_DEBUG_INFO` · hash `0x2162C446DFDF38FD` · jhash `0x2DFD35C7` · **Cliente**

```lua
LogDebugInfo(p0)
```
```c
void _LOG_DEBUG_INFO(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Not present in retail version of the game, actual definiton seems to be
_LOG_DEBUG_INFO(const char* category, const char* debugText);
```

**Nombres antiguos (alias):** `0x2162C446DFDF38FD` (`N_0x2162c446dfdf38fd`)

---
### N_0x04655f9d075d0ae5

`0x04655F9D075D0AE5` · hash `0x04655F9D075D0AE5` · **Cliente**

```lua
N_0x04655f9d075d0ae5(toggle)
```
```c
void 0x04655F9D075D0AE5(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
```

---
### N_0x0c698d8f099174c7

`0x0C698D8F099174C7` · hash `0x0C698D8F099174C7` · **Cliente**

```lua
N_0x0c698d8f099174c7(p0)
```
```c
void 0x0C698D8F099174C7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x0cf54f20de43879c

`0x0CF54F20DE43879C` · hash `0x0CF54F20DE43879C` · **Cliente**

```lua
N_0x0cf54f20de43879c(p0)
```
```c
void 0x0CF54F20DE43879C(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x211c4ef450086857

`0x211C4EF450086857` · hash `0x211C4EF450086857` · jhash `0x801D0D86` · **Cliente**

```lua
N_0x211c4ef450086857()
```
```c
void 0x211C4EF450086857();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x214cd562a939246a

`0x214CD562A939246A` · hash `0x214CD562A939246A` · jhash `0x812CBE0E` · **Cliente**

```lua
local retval = N_0x214cd562a939246a()
```
```c
BOOL 0x214CD562A939246A();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
HAS_S*
```

---
### N_0x243296a510b562b6

`0x243296A510B562B6` · hash `0x243296A510B562B6` · **Cliente**

```lua
N_0x243296a510b562b6()
```
```c
void 0x243296A510B562B6();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0x24a49beaf468dc90

`0x24A49BEAF468DC90` · hash `0x24A49BEAF468DC90` · **Cliente**

```lua
local retval, p1 = N_0x24a49beaf468dc90(p0, p2, p3, p4)
```
```c
BOOL 0x24A49BEAF468DC90(Any p0, Any* p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x2790f4b17d098e26

`0x2790F4B17D098E26` · hash `0x2790F4B17D098E26` · **Cliente**

```lua
N_0x2790f4b17d098e26(toggle)
```
```c
void 0x2790F4B17D098E26(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_F*
```

---
### N_0x2c173ae2bdb9385e

`0x2C173AE2BDB9385E` · hash `0x2C173AE2BDB9385E` · **Cliente**

```lua
local retval = N_0x2c173ae2bdb9385e(blip)
```
```c
int 0x2C173AE2BDB9385E(Blip blip);
```

**Parámetros**

- `blip` (`Blip`): The blip to check.

**Devuelve:** `int` — Seems to always return 0 from what I can tell. I've tried a lot of different blip related natives and it always seems to return 0.

**Descripción oficial:**

GET_BLIP_\*
Seems to always return 0 from what I can tell. I've tried a lot of different blip related natives and it always seems to return 0. Decompiled scripts always pass a blip handle as p0.

---
### N_0x2c9f302398e13141

`0x2C9F302398E13141` · hash `0x2C9F302398E13141` · jhash `0xCA95C487` · **Cliente**

```lua
N_0x2c9f302398e13141(blip, p1)
```
```c
void 0x2C9F302398E13141(Blip blip, Any p1);
```

**Parámetros**

- `blip` (`Blip`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

Correct native name lies between SET_BLIP_SPRITE and SET_RADIUS_BLIP_EDGE alphabetically.

---
### N_0x2f057596f2bd0061

`0x2F057596F2BD0061` · hash `0x2F057596F2BD0061` · jhash `0xC85C4487` · **Cliente**

```lua
local retval = N_0x2f057596f2bd0061()
```
```c
BOOL 0x2F057596F2BD0061();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Appears to return whether the player is using the pause menu store. Can't be sure though.  
```

---
### N_0x35a3cd97b2c0a6d2

`0x35A3CD97B2C0A6D2` · hash `0x35A3CD97B2C0A6D2` · **Cliente**

```lua
N_0x35a3cd97b2c0a6d2(blip)
```
```c
void 0x35A3CD97B2C0A6D2(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x4b5b620c9b59ed34

`0x4B5B620C9B59ED34` · hash `0x4B5B620C9B59ED34` · **Cliente**

```lua
N_0x4b5b620c9b59ed34(p0, p1)
```
```c
void 0x4B5B620C9B59ED34(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x55f5a5f07134de60

`0x55F5A5F07134DE60` · hash `0x55F5A5F07134DE60` · jhash `0x7A569F78` · **Cliente**

```lua
N_0x55f5a5f07134de60()
```
```c
void 0x55F5A5F07134DE60();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x57d760d55f54e071

`0x57D760D55F54E071` · hash `0x57D760D55F54E071` · jhash `0x9854485F` · **Cliente**

```lua
N_0x57d760d55f54e071(p0)
```
```c
void 0x57D760D55F54E071(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
FORCE_*
```

---
### N_0x593feae1f73392d4

`0x593FEAE1F73392D4` · hash `0x593FEAE1F73392D4` · jhash `0x22CA9F2A` · **Cliente**

```lua
local retval = N_0x593feae1f73392d4()
```
```c
Any 0x593FEAE1F73392D4();
```

**Devuelve:** `Any`

---
### N_0x62e849b7eb28e770

`0x62E849B7EB28E770` · hash `0x62E849B7EB28E770` · **Cliente**

```lua
N_0x62e849b7eb28e770(p0)
```
```c
void 0x62E849B7EB28E770(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x66e7cb63c97b7d20

`0x66E7CB63C97B7D20` · hash `0x66E7CB63C97B7D20` · jhash `0x92DAFA78` · **Cliente**

```lua
local retval = N_0x66e7cb63c97b7d20()
```
```c
Any 0x66E7CB63C97B7D20();
```

**Devuelve:** `Any`

---
### N_0x7c226d5346d4d10a

`0x7C226D5346D4D10A` · hash `0x7C226D5346D4D10A` · **Cliente**

```lua
N_0x7c226d5346d4d10a(p0)
```
```c
void 0x7C226D5346D4D10A(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x801879a9b4f4b2fb

`0x801879A9B4F4B2FB` · hash `0x801879A9B4F4B2FB` · **Cliente**

```lua
local retval = N_0x801879a9b4f4b2fb()
```
```c
BOOL 0x801879A9B4F4B2FB();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

---
### N_0x817b86108eb94e51

`0x817B86108EB94E51` · hash `0x817B86108EB94E51` · jhash `0xD2161E77` · **Cliente**

```lua
local p1, p2, p3, p4, p5, p6, p7, p8 = N_0x817b86108eb94e51(p0)
```
```c
void 0x817B86108EB94E51(BOOL p0, Any* p1, Any* p2, Any* p3, Any* p4, Any* p5, Any* p6, Any* p7, Any* p8);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p5` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p6` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p7` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p8` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
UI::_817B86108EB94E51(1, &g_189F36._f10CD1[0/*16*/], &g_189F36._f10CD1[1/*16*/], &g_189F36._f10CD1[2/*16*/], &g_189F36._f10CD1[3/*16*/], &g_189F36._f10CD1[4/*16*/], &g_189F36._f10CD1[5/*16*/], &g_189F36._f10CD1[6/*16*/], &g_189F36._f10CD1[7/*16*/]);  
```

---
### N_0x8410c5e0cd847b9d

`0x8410C5E0CD847B9D` · hash `0x8410C5E0CD847B9D` · **Cliente**

```lua
N_0x8410c5e0cd847b9d()
```
```c
void 0x8410C5E0CD847B9D();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x8f08017f9d7c47bd

`0x8F08017F9D7C47BD` · hash `0x8F08017F9D7C47BD` · **Cliente**

```lua
local retval, p1 = N_0x8f08017f9d7c47bd(p0, p2)
```
```c
BOOL 0x8F08017F9D7C47BD(Any p0, Any* p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x98c3cf913d895111

`0x98C3CF913D895111` · hash `0x98C3CF913D895111` · **Cliente**

```lua
local retval = N_0x98c3cf913d895111(string, length)
```
```c
char* 0x98C3CF913D895111(char* string, int length);
```

**Parámetros**

- `string` (`char*`)
- `length` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
GET_F*
```

---
### N_0x9fcb3cbfb3ead69a

`0x9FCB3CBFB3EAD69A` · hash `0x9FCB3CBFB3EAD69A` · **Cliente**

```lua
N_0x9fcb3cbfb3ead69a(p0, p1)
```
```c
void 0x9FCB3CBFB3EAD69A(int p0, float p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

SET_C\*

```
NativeDB Introduced: v1734
```

---
### N_0xa17784fca9548d15

`0xA17784FCA9548D15` · hash `0xA17784FCA9548D15` · **Cliente**

```lua
N_0xa17784fca9548d15(p0, p1, p2)
```
```c
void 0xA17784FCA9548D15(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0xa238192f33110615

`0xA238192F33110615` · hash `0xA238192F33110615` · jhash `0x46794EB2` · **Cliente**

```lua
local retval, p0, p1, p2 = N_0xa238192f33110615()
```
```c
BOOL 0xA238192F33110615(int* p0, int* p1, int* p2);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0xb552929b85fc27ec

`0xB552929B85FC27EC` · hash `0xB552929B85FC27EC` · **Cliente**

```lua
N_0xb552929b85fc27ec(p0, p1)
```
```c
void 0xB552929B85FC27EC(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xb7b873520c84c118

`0xB7B873520C84C118` · hash `0xB7B873520C84C118` · **Cliente**

```lua
N_0xb7b873520c84c118()
```
```c
void 0xB7B873520C84C118();
```

**Devuelve:** `void`

**Descripción oficial:**

SET_C\*

```
NativeDB Introduced: v1734
```

---
### N_0xba8d65c1c65702e5

`0xBA8D65C1C65702E5` · hash `0xBA8D65C1C65702E5` · jhash `0x58612465` · **Cliente**

```lua
N_0xba8d65c1c65702e5(toggle)
```
```c
void 0xBA8D65C1C65702E5(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
FORCE_*
```

---
### N_0xc2d2ad9eaae265b8

`0xC2D2AD9EAAE265B8` · hash `0xC2D2AD9EAAE265B8` · **Cliente**

```lua
local retval = N_0xc2d2ad9eaae265b8()
```
```c
BOOL 0xC2D2AD9EAAE265B8();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Getter for 0xCD74233600C4EA6B

GET_*
```

---
### N_0xc594b315edf2d4af

`0xC594B315EDF2D4AF` · hash `0xC594B315EDF2D4AF` · jhash `0x41B0D022` · **Cliente**

```lua
N_0xc594b315edf2d4af(ped)
```
```c
void 0xC594B315EDF2D4AF(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### N_0xc8e1071177a23be5

`0xC8E1071177A23BE5` · hash `0xC8E1071177A23BE5` · **Cliente**

```lua
local retval, p0, p1, p2 = N_0xc8e1071177a23be5()
```
```c
BOOL 0xC8E1071177A23BE5(Any* p0, Any* p1, Any* p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0xca6b2f7ce32ab653

`0xCA6B2F7CE32AB653` · hash `0xCA6B2F7CE32AB653` · **Cliente**

```lua
local retval, p1 = N_0xca6b2f7ce32ab653(p0, p2)
```
```c
BOOL 0xCA6B2F7CE32AB653(Any p0, Any* p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)

**Devuelve:** `BOOL`

---
### N_0xcd74233600c4ea6b

`0xCD74233600C4EA6B` · hash `0xCD74233600C4EA6B` · **Cliente**

```lua
N_0xcd74233600c4ea6b(toggle)
```
```c
void 0xCD74233600C4EA6B(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Setter for 0xC2D2AD9EAAE265B8

SET_*
```

---
### N_0xd1942374085c8469

`0xD1942374085C8469` · hash `0xD1942374085C8469` · **Cliente**

```lua
N_0xd1942374085c8469(p0)
```
```c
void 0xD1942374085C8469(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xd2049635deb9c375

`0xD2049635DEB9C375` · hash `0xD2049635DEB9C375` · jhash `0xE8D3A910` · **Cliente**

```lua
N_0xd2049635deb9c375()
```
```c
void 0xD2049635DEB9C375();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xdaf87174be7454ff

`0xDAF87174BE7454FF` · hash `0xDAF87174BE7454FF` · **Cliente**

```lua
local retval = N_0xdaf87174be7454ff(p0)
```
```c
BOOL 0xDAF87174BE7454FF(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0xde03620f8703a9df

`0xDE03620F8703A9DF` · hash `0xDE03620F8703A9DF` · **Cliente**

```lua
local retval = N_0xde03620f8703a9df()
```
```c
Any 0xDE03620F8703A9DF();
```

**Devuelve:** `Any`

---
### N_0xe4c3b169876d33d7

`0xE4C3B169876D33D7` · hash `0xE4C3B169876D33D7` · **Cliente**

```lua
N_0xe4c3b169876d33d7(p0)
```
```c
void 0xE4C3B169876D33D7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xeb81a3dadd503187

`0xEB81A3DADD503187` · hash `0xEB81A3DADD503187` · **Cliente**

```lua
N_0xeb81a3dadd503187()
```
```c
void 0xEB81A3DADD503187();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xf13fe2a80c05c561

`0xF13FE2A80C05C561` · hash `0xF13FE2A80C05C561` · jhash `0x850690FF` · **Cliente**

```lua
local retval = N_0xf13fe2a80c05c561()
```
```c
BOOL 0xF13FE2A80C05C561();
```

**Devuelve:** `BOOL`

---
### N_0xf284ac67940c6812

`0xF284AC67940C6812` · hash `0xF284AC67940C6812` · jhash `0x7D95AFFF` · **Cliente**

```lua
local retval = N_0xf284ac67940c6812()
```
```c
Any 0xF284AC67940C6812();
```

**Devuelve:** `Any`

---
### N_0xf83d0febe75e62c9

`0xF83D0FEBE75E62C9` · hash `0xF83D0FEBE75E62C9` · **Cliente**

```lua
N_0xf83d0febe75e62c9(blip, p1, p2, width, p4, length, heading, p7)
```
```c
void 0xF83D0FEBE75E62C9(Blip blip, Any p1, Any p2, float width, Any p4, float length, float heading, Any p7);
```

**Parámetros**

- `blip` (`Blip`): A blip from an entity. The entity can not be a ped. The width and length will not change if it is a ped.
- `p1` (`Any`): \-1.0 in decompiled scripts (unk)
- `p2` (`Any`): 1.0 in decompiled scripts (unk)
- `width` (`float`): Width of the cone (0.0 to ~3.0)
- `p4` (`Any`): 1.0 in decompiled scripts (unk)
- `length` (`float`): Length of the cone. (8.2 is 'normal' sized)
- `heading` (`float`): This heading is in radians, this can be calculated with (heading + 180.00) \* (pi/180)
- `p7` (`Any`): 1 in decompiled scripts (unk)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 9: int hudColour
NativeDB Introduced: v1290
```

Sets the 'data' for a cone for a blip

See [here](https://docs.fivem.net/docs/game-references/hud-colors/) for the hud colours for the cone

Name in scripts: `SETUP_FAKE_CONE_DATA()`

For people who don't know how to convert degrees to radians and the other way around:

```
degrees = radians * 180 / pi
radians = degrees * pi / 180
```

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local blip = AddBlipForEntity(ped)

Citizen.InvokeNative(0xF83D0FEBE75E62C9, blip, -1.0, 1.0, 0.36, 1.0, 8.2, (0.5 * math.pi), 0, 11)
SetBlipShowCone(blip, true, 11)
```

---
### OpenOnlinePoliciesMenu

`OPEN_ONLINE_POLICIES_MENU` · hash `0x805D7CBB36FD6C4C` · jhash `0x19FCBBB2` · **Cliente**

```lua
OpenOnlinePoliciesMenu()
```
```c
void OPEN_ONLINE_POLICIES_MENU();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SHOW_SOCIAL_CLUB_LEGAL_SCREEN` (`ShowSocialClubLegalScreen`)

---
### OpenReportugcMenu

`OPEN_REPORTUGC_MENU` · hash `0x523A590C1A3CC0D3` · jhash `0x10DE5150` · **Cliente**

```lua
OpenReportugcMenu()
```
```c
void OPEN_REPORTUGC_MENU();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Shows a menu for reporting UGC content.
```

**Nombres antiguos (alias):** `0x523A590C1A3CC0D3` (`N_0x523a590c1a3cc0d3`), `_DISPLAY_JOB_REPORT` (`DisplayJobReport`)

---
### OpenSocialClubMenu

`OPEN_SOCIAL_CLUB_MENU` · hash `0x75D3691713C3B05A` · jhash `0x57218529` · **Cliente**

```lua
OpenSocialClubMenu()
```
```c
void OPEN_SOCIAL_CLUB_MENU();
```

**Devuelve:** `void`

**Descripción oficial:**

Uses the `SOCIAL_CLUB2` scaleform.

**Nombres antiguos (alias):** `0x75D3691713C3B05A` (`N_0x75d3691713c3b05a`)

---
### OverrideMultiplayerChatColour

`_OVERRIDE_MULTIPLAYER_CHAT_COLOUR` · hash `0xF47E567B3630DD12` · **Cliente**

```lua
OverrideMultiplayerChatColour(p0, hudColor)
```
```c
void _OVERRIDE_MULTIPLAYER_CHAT_COLOUR(int p0, int hudColor);
```

**Parámetros**

- `p0` (`int`)
- `hudColor` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF47E567B3630DD12` (`N_0xf47e567b3630dd12`)

---
### OverrideMultiplayerChatPrefix

`_OVERRIDE_MULTIPLAYER_CHAT_PREFIX` · hash `0x6A1738B4323FE2D9` · **Cliente**

```lua
OverrideMultiplayerChatPrefix(gxtEntryHash)
```
```c
void _OVERRIDE_MULTIPLAYER_CHAT_PREFIX(Hash gxtEntryHash);
```

**Parámetros**

- `gxtEntryHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6A1738B4323FE2D9` (`N_0x6a1738b4323fe2d9`)

---
### PauseMenuActivateContext

`PAUSE_MENU_ACTIVATE_CONTEXT` · hash `0xDD564BDD0472C936` · jhash `0x9FE8FD5E` · **Cliente**

```lua
PauseMenuActivateContext(hash)
```
```c
void PAUSE_MENU_ACTIVATE_CONTEXT(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Context name hash.

**Devuelve:** `void`

**Descripción oficial:**

Activates the specified frontend menu context.

pausemenu.xml defines some specific menu options using 'context'. Context is basically a 'condition'.

The `*ALL*` part of the context means that whatever is being defined, will be active when any or all of those conditions after `*ALL*` are met.

The `*NONE*` part of the context section means that whatever is being defined, will NOT be active if any or all of the conditions after `*NONE*` are met.

This basically allows you to hide certain menu sections, or things like instructional buttons.

See the old description below for more info.

***

> Seems to add/set the current menu context (to show/hide buttons?)
> Pausemenu.xml:
> `<Contexts>*ALL*, DISPLAY_CORONA_BUTTONS, *NONE*, BET_LOCKED, BET_AVAILABLE, SCROLL_OPTION</Contexts>`
> Code:
>
> ```
> if (...) {
>     sub_bbd34(a_0, 0, "FM_BET_HELP");
>     UI::PAUSE_MENU_ACTIVATE_CONTEXT(${bet_available}); // This native
>     UI::OBJECT_DECAL_TOGGLE(${bet_locked});
> } else {
>     sub_bbd34(a_0, 0, "");
>     UI::OBJECT_DECAL_TOGGLE(${bet_available});
>     UI::PAUSE_MENU_ACTIVATE_CONTEXT(${bet_locked}); // This native
> }
> ```
>
> OBJECT_DECAL_TOGGLE seems to remove a context, It also has a hash collision
> // Old
> Scripts do not make this native's purpose clear. However, this native most likely has something to do with decals since in nearly every instance, "OBJECT_DECAL_TOGGLE" is called prior.

**Nombres antiguos (alias):** `0xDD564BDD0472C936` (`N_0xdd564bdd0472c936`), `_ADD_FRONTEND_MENU_CONTEXT` (`AddFrontendMenuContext`)

---
### PauseMenuDeactivateContext

`PAUSE_MENU_DEACTIVATE_CONTEXT` · hash `0x444D8CF241EC25C5` · jhash `0x0029046E` · **Cliente**

```lua
PauseMenuDeactivateContext(contextHash)
```
```c
void PAUSE_MENU_DEACTIVATE_CONTEXT(Hash contextHash);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `OBJECT_DECAL_TOGGLE` (`ObjectDecalToggle`)

---
### PauseMenuDisableBusyspinner

`_PAUSE_MENU_DISABLE_BUSYSPINNER` · hash `0x9245E81072704B8A` · **Cliente**

```lua
PauseMenuDisableBusyspinner(toggle)
```
```c
void _PAUSE_MENU_DISABLE_BUSYSPINNER(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): true to disable and false to re-enable the loading icon.

**Devuelve:** `void`

**Descripción oficial:**

Disables the loading spinner in Pause Menu when switching from one header tab to another.

**Nombres antiguos (alias):** `0x9245e81072704b8a` (`N_0x9245e81072704b8a`)

---
### PauseMenuGetMouseHoverIndex

`PAUSE_MENU_GET_MOUSE_HOVER_INDEX` · hash `0x359AF31A4B52F5ED` · **Cliente**

```lua
local retval = PauseMenuGetMouseHoverIndex()
```
```c
int PAUSE_MENU_GET_MOUSE_HOVER_INDEX();
```

**Devuelve:** `int` — Returns the index of a menu item the mouse is hovering on in Pause Menu. -1 if nothing is being hovered on.

**Nombres antiguos (alias):** `0x359AF31A4B52F5ED` (`N_0x359af31a4b52f5ed`), `_PAUSE_MENU_GET_INDEX_OF_MOUSE_HOVERED_SLOT` (`PauseMenuGetIndexOfMouseHoveredSlot`)

---
### PauseMenuGetMouseHoverUniqueId

`PAUSE_MENU_GET_MOUSE_HOVER_UNIQUE_ID` · hash `0x13C4B962653A5280` · **Cliente**

```lua
local retval = PauseMenuGetMouseHoverUniqueId()
```
```c
int PAUSE_MENU_GET_MOUSE_HOVER_UNIQUE_ID();
```

**Devuelve:** `int` — Returns the uniqueID of the pause menu item the mouse is hovering on. -1 if the mouse isn't rolled over any item.

**Nombres antiguos (alias):** `0x13C4B962653A5280` (`N_0x13c4b962653a5280`), `_PAUSE_MENU_GET_UNIQUE_ID_OF_MOUSE_HOVERED_SLOT` (`PauseMenuGetUniqueIdOfMouseHoveredSlot`)

---
### PauseMenuIsContextActive

`PAUSE_MENU_IS_CONTEXT_ACTIVE` · hash `0x84698AB38D0C6636` · jhash `0xC51BC42F` · **Cliente**

```lua
local retval = PauseMenuIsContextActive(contextHash)
```
```c
BOOL PAUSE_MENU_IS_CONTEXT_ACTIVE(Hash contextHash);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x84698AB38D0C6636` (`N_0x84698ab38d0c6636`)

---
### PauseMenuIsContextMenuActive

`PAUSE_MENU_IS_CONTEXT_MENU_ACTIVE` · hash `0x2A25ADC48F87841F` · jhash `0x016D7AF9` · **Cliente**

```lua
local retval = PauseMenuIsContextMenuActive()
```
```c
Any PAUSE_MENU_IS_CONTEXT_MENU_ACTIVE();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x2A25ADC48F87841F` (`N_0x2a25adc48f87841f`)

---
### PauseMenuRedrawInstructionalButtons

`PAUSE_MENU_REDRAW_INSTRUCTIONAL_BUTTONS` · hash `0x4895BDEA16E7C080` · jhash `0x15B24768` · **Cliente**

```lua
PauseMenuRedrawInstructionalButtons(p0)
```
```c
void PAUSE_MENU_REDRAW_INSTRUCTIONAL_BUTTONS(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Updates instructional buttons in Pause Menu after menu contexts have been toggled. p0 purpose is currently unknown, only 0 is used in scripts.

**Nombres antiguos (alias):** `_ENABLE_DEATHBLOOD_SEETHROUGH` (`EnableDeathbloodSeethrough`), `0x4895BDEA16E7C080` (`N_0x4895bdea16e7c080`)

---
### PauseMenuSetBusySpinner

`PAUSE_MENU_SET_BUSY_SPINNER` · hash `0xC78E239AC5B2DDB9` · jhash `0x6C67131A` · **Cliente**

```lua
PauseMenuSetBusySpinner(bVisible, iColumnID, iSpinnerIndex)
```
```c
void PAUSE_MENU_SET_BUSY_SPINNER(BOOL bVisible, int iColumnID, int iSpinnerIndex);
```

**Parámetros**

- `bVisible` (`BOOL`): Sets or removes this spinner.
- `iColumnID` (`int`): Location of this spinner (0 - 17). Indexes can be found in `common:\data\ui\frontend.xml`, `PauseMenu\PersistentData\Spinner\Offsets`. If `bVisible` is `false`, this will be ignored.
- `iSpinnerIndex` (`int`): Index of this spinner. Can have a maximum of three spinners at a time.

**Devuelve:** `void`

**Descripción oficial:**

Sets a loading icon in the pause menu.

**Nombres antiguos (alias):** `0xC78E239AC5B2DDB9` (`N_0xc78e239ac5b2ddb9`)

---
### PauseMenuSetWarnOnTabChange

`PAUSE_MENU_SET_WARN_ON_TAB_CHANGE` · hash `0xF06EBB91A81E09E3` · jhash `0x11D09737` · **Cliente**

```lua
PauseMenuSetWarnOnTabChange(setWarn)
```
```c
void PAUSE_MENU_SET_WARN_ON_TAB_CHANGE(BOOL setWarn);
```

**Parámetros**

- `setWarn` (`BOOL`): Wether to show the message or not.

**Devuelve:** `void`

**Descripción oficial:**

Shows this warning message when trying to switch pause menu header tabs:
![](https://imgur.com/a/5jugFi9)

**Nombres antiguos (alias):** `0xF06EBB91A81E09E3` (`N_0xf06ebb91a81e09e3`)

---
### PauseMenuceptionGoDeeper

`PAUSE_MENUCEPTION_GO_DEEPER` · hash `0x77F16B447824DA6C` · jhash `0x0A89336C` · **Cliente**

```lua
PauseMenuceptionGoDeeper(pageId)
```
```c
void PAUSE_MENUCEPTION_GO_DEEPER(int pageId);
```

**Parámetros**

- `pageId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Sets current pause menu page/component to the specified value.
Available page IDs: https://pastebin.com/qxuhwjPT

**Nombres antiguos (alias):** `0x77F16B447824DA6C` (`N_0x77f16b447824da6c`)

---
### PauseMenuceptionTheKick

`PAUSE_MENUCEPTION_THE_KICK` · hash `0xCDCA26E80FAECB8F` · jhash `0xC84BE309` · **Cliente**

```lua
PauseMenuceptionTheKick()
```
```c
void PAUSE_MENUCEPTION_THE_KICK();
```

**Devuelve:** `void`

**Descripción oficial:**

Forces the Pause Menu to back out of unique pages such as Awards, Unlocks, Key Bindings etc

**Nombres antiguos (alias):** `0xCDCA26E80FAECB8F` (`N_0xcdca26e80faecb8f`)

---
### PauseToggleFullscreenMap

`PAUSE_TOGGLE_FULLSCREEN_MAP` · hash `0x2DE6C5E2E996F178` · **Cliente**

```lua
PauseToggleFullscreenMap(enabled)
```
```c
void PAUSE_TOGGLE_FULLSCREEN_MAP(BOOL enabled);
```

**Parámetros**

- `enabled` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Toggles pause menu map rendering.

**Nombres antiguos (alias):** `0x2DE6C5E2E996F178` (`N_0x2de6c5e2e996f178`)

---
### PreloadBusyspinner

`PRELOAD_BUSYSPINNER` · hash `0xC65AB383CD91DF98` · jhash `0x71077FBD` · **Cliente**

```lua
PreloadBusyspinner()
```
```c
void PRELOAD_BUSYSPINNER();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC65AB383CD91DF98` (`N_0xc65ab383cd91df98`)

---
### PulseBlip

`PULSE_BLIP` · hash `0x742D6FD43115AF73` · jhash `0x44253855` · **Cliente**

```lua
PulseBlip(blip)
```
```c
void PULSE_BLIP(Blip blip);
```

**Parámetros**

- `blip` (`Blip`)

**Devuelve:** `void`

---
### RaceGalleryAddBlip

`_RACE_GALLERY_ADD_BLIP` · hash `0x551DF99658DB6EE8` · jhash `0x786CA0A2` · **Cliente**

```lua
local retval = RaceGalleryAddBlip(x, y, z)
```
```c
Any _RACE_GALLERY_ADD_BLIP(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Add a BLIP_GALLERY at the specific coordinate. Used in fm_maintain_transition_players to display race track points.
```

**Nombres antiguos (alias):** `0x551DF99658DB6EE8` (`N_0x551df99658db6ee8`)

---
### RaceGalleryFullscreen

`_RACE_GALLERY_FULLSCREEN` · hash `0x5354C5BA2EA868A4` · jhash `0xE4FD20D8` · **Cliente**

```lua
RaceGalleryFullscreen(toggle)
```
```c
void _RACE_GALLERY_FULLSCREEN(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If toggle is true, the map is shown in full screen
If toggle is false, the map is shown in normal mode
```

**Nombres antiguos (alias):** `0x5354C5BA2EA868A4` (`N_0x5354c5ba2ea868a4`), `_SET_MAP_FULL_SCREEN` (`SetMapFullScreen`)

---
### RaceGalleryNextBlipSprite

`_RACE_GALLERY_NEXT_BLIP_SPRITE` · hash `0x1EAE6DD17B7A5EFA` · jhash `0x13E7A5A9` · **Cliente**

```lua
RaceGalleryNextBlipSprite(spriteId)
```
```c
void _RACE_GALLERY_NEXT_BLIP_SPRITE(int spriteId);
```

**Parámetros**

- `spriteId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the sprite of the next BLIP_GALLERY blip, values used in the native scripts: 143 (ObjectiveBlue), 144 (ObjectiveGreen), 145 (ObjectiveRed), 146 (ObjectiveYellow).
```

**Nombres antiguos (alias):** `0x1EAE6DD17B7A5EFA` (`N_0x1eae6dd17b7a5efa`)

---
### RefreshWaypoint

`REFRESH_WAYPOINT` · hash `0x81FA173F170560D1` · jhash `0xB395D753` · **Cliente**

```lua
RefreshWaypoint()
```
```c
void REFRESH_WAYPOINT();
```

**Devuelve:** `void`

---
### RegisterNamedRendertarget

`REGISTER_NAMED_RENDERTARGET` · hash `0x57D9C12635E25CE3` · jhash `0xFAE5D6F0` · **Cliente**

```lua
local retval = RegisterNamedRendertarget(name, p1)
```
```c
BOOL REGISTER_NAMED_RENDERTARGET(char* name, BOOL p1);
```

**Parámetros**

- `name` (`char*`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

---
### ReleaseControlOfFrontend

`RELEASE_CONTROL_OF_FRONTEND` · hash `0x14621BB1DF14E2B2` · jhash `0xB9392CE7` · **Cliente**

```lua
ReleaseControlOfFrontend()
```
```c
void RELEASE_CONTROL_OF_FRONTEND();
```

**Devuelve:** `void`

**Descripción oficial:**

Enables frontend (works in custom frontends, not sure about regular pause menu) navigation keys on keyboard if they were disabled using the native below.

To disable the keys, use [`0xEC9264727EEC0F28`](#takecontroloffrontend).

**Nombres antiguos (alias):** `0x14621BB1DF14E2B2` (`N_0x14621bb1df14e2b2`)

---
### ReleaseNamedRendertarget

`RELEASE_NAMED_RENDERTARGET` · hash `0xE9F6FFE837354DD4` · jhash `0xD3F6C892` · **Cliente**

```lua
local retval = ReleaseNamedRendertarget(name)
```
```c
BOOL RELEASE_NAMED_RENDERTARGET(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

---
### ReloadMapMenu

`RELOAD_MAP_MENU` · hash `0x2916A928514C9827` · **Cliente**

```lua
ReloadMapMenu()
```
```c
void RELOAD_MAP_MENU();
```

**Devuelve:** `void`

**Descripción oficial:**

Forces the map menu to reload.

**Nombres antiguos (alias):** `0x2916A928514C9827` (`N_0x2916a928514c9827`)

**Ejemplo (lua):**

```lua
if GetNumberOfReferencesOfScriptWithNameHash(`pausemenu_map`) > 0 then -- Ensure we're on the map screen
  ReloadMapMenu()
  print('Reloaded map menu!')
end
```

---
### RemoveBlip

`REMOVE_BLIP` · hash `0x86A652570E5F25DD` · jhash `0xD8C3C1CD` · **Cliente · también en el servidor (RPC)**

```lua
local blip = RemoveBlip(blip)
```
```c
void REMOVE_BLIP(Blip* blip);
```

**Parámetros**

- `blip` (`Blip*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: Blip handle to remove.

**Devuelve:** `void`

**Descripción oficial:**

Removes the blip from your map.

**Note:** This function only works on the script that created the blip, if you wish to remove blips created by other scripts, see [`SET_THIS_SCRIPT_CAN_REMOVE_BLIPS_CREATED_BY_ANY_SCRIPT`](MISC.md#setthisscriptcanremoveblipscreatedbyanyscript).

**Ejemplo (lua):**

```lua
-- Create the blip
local coords = vector3(200.0, 200.0, 5.0)
local blip = AddBlipForCoord(coords)

-- When you want to remove it
RemoveBlip(blip)
```

---
### RemoveMpGamerTag

`REMOVE_MP_GAMER_TAG` · hash `0x31698AA80E0223F8` · jhash `0x3D081FE4` · **Cliente**

```lua
RemoveMpGamerTag(gamerTagId)
```
```c
void REMOVE_MP_GAMER_TAG(int gamerTagId);
```

**Parámetros**

- `gamerTagId` (`int`): A player ID with a gamer tag or a fake gamer tag ID.

**Devuelve:** `void`

**Descripción oficial:**

Removes the gamer tag associated with the provided ID. This does not happen instantly. Use [IS_MP_GAMER_TAG_FREE](#ismpgamertagfree) to determine when the ID is free for reuse.

**Nombres antiguos (alias):** `0x31698AA80E0223F8` (`N_0x31698aa80e0223f8`)

---
### RemoveMultiplayerBankCash

`REMOVE_MULTIPLAYER_BANK_CASH` · hash `0xC7C6789AA1CFEDD0` · jhash `0x728B4EF4` · **Cliente**

```lua
RemoveMultiplayerBankCash()
```
```c
void REMOVE_MULTIPLAYER_BANK_CASH();
```

**Devuelve:** `void`

---
### RemoveMultiplayerHudCash

`REMOVE_MULTIPLAYER_HUD_CASH` · hash `0x968F270E39141ECA` · jhash `0x07BF4A7D` · **Cliente**

```lua
RemoveMultiplayerHudCash()
```
```c
void REMOVE_MULTIPLAYER_HUD_CASH();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Removes multiplayer cash hud each frame  
```

---
### RemoveMultiplayerWalletCash

`REMOVE_MULTIPLAYER_WALLET_CASH` · hash `0x95CF81BD06EE1887` · jhash `0x7BFFE82F` · **Cliente**

```lua
RemoveMultiplayerWalletCash()
```
```c
void REMOVE_MULTIPLAYER_WALLET_CASH();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x95CF81BD06EE1887` (`N_0x95cf81bd06ee1887`)

---
### RemoveWarningMessageListItems

`_REMOVE_WARNING_MESSAGE_LIST_ITEMS` · hash `0x6EF54AB721DC6242` · **Cliente**

```lua
RemoveWarningMessageListItems()
```
```c
void _REMOVE_WARNING_MESSAGE_LIST_ITEMS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6EF54AB721DC6242` (`N_0x6ef54ab721dc6242`)

---
### ReplaceHudColour

`REPLACE_HUD_COLOUR` · hash `0x1CCC708F0F850613` · jhash `0x3B216749` · **Cliente**

```lua
ReplaceHudColour(hudColorIndex, hudColorIndex2)
```
```c
void REPLACE_HUD_COLOUR(int hudColorIndex, int hudColorIndex2);
```

**Parámetros**

- `hudColorIndex` (`int`)
- `hudColorIndex2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Changes the hud color at a given index (hudColorIndex) by another one (hudColorIndex2).

HUD colors can be found [here](https://docs.fivem.net/docs/game-references/hud-colors/)

**Nombres antiguos (alias):** `0x1CCC708F0F850613` (`N_0x1ccc708f0f850613`), `_SET_HUD_COLOURS_SWITCH` (`SetHudColoursSwitch`)

---
### ReplaceHudColourWithRgba

`REPLACE_HUD_COLOUR_WITH_RGBA` · hash `0xF314CF4F0211894E` · jhash `0xF6E7E92B` · **Cliente**

```lua
ReplaceHudColourWithRgba(hudColorIndex, r, g, b, a)
```
```c
void REPLACE_HUD_COLOUR_WITH_RGBA(int hudColorIndex, int r, int g, int b, int a);
```

**Parámetros**

- `hudColorIndex` (`int`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Hud colors can be found [here](https://docs.fivem.net/docs/game-references/hud-colors/)

**Nombres antiguos (alias):** `0xF314CF4F0211894E` (`N_0xf314cf4f0211894e`), `_SET_HUD_COLOUR` (`SetHudColour`)

---
### RequestAdditionalText

`REQUEST_ADDITIONAL_TEXT` · hash `0x71A78003C8E71424` · jhash `0x9FA9175B` · **Cliente**

```lua
RequestAdditionalText(gxt, slot)
```
```c
void REQUEST_ADDITIONAL_TEXT(char* gxt, int slot);
```

**Parámetros**

- `gxt` (`char*`)
- `slot` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Request a gxt into the passed slot.  
```

---
### RequestAdditionalTextForDlc

`REQUEST_ADDITIONAL_TEXT_FOR_DLC` · hash `0x6009F9F1AE90D8A6` · jhash `0xF4D27EBE` · **Cliente**

```lua
RequestAdditionalTextForDlc(gxt, slot)
```
```c
void REQUEST_ADDITIONAL_TEXT_FOR_DLC(char* gxt, int slot);
```

**Parámetros**

- `gxt` (`char*`)
- `slot` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_REQUEST_ADDITIONAL_TEXT_2` (`RequestAdditionalText_2`)

---
### ResetGlobalActionscriptFlag

`RESET_GLOBAL_ACTIONSCRIPT_FLAG` · hash `0xB99C4E4D9499DF29` · jhash `0x4C4C10CF` · **Cliente**

```lua
ResetGlobalActionscriptFlag(flagIndex)
```
```c
void RESET_GLOBAL_ACTIONSCRIPT_FLAG(int flagIndex);
```

**Parámetros**

- `flagIndex` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB99C4E4D9499DF29` (`N_0xb99c4e4d9499df29`)

---
### ResetHudComponentValues

`RESET_HUD_COMPONENT_VALUES` · hash `0x450930E616475D0D` · jhash `0xD15B46DA` · **Cliente**

```lua
ResetHudComponentValues(id)
```
```c
void RESET_HUD_COMPONENT_VALUES(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

---
### ResetReticuleValues

`RESET_RETICULE_VALUES` · hash `0x12782CE0A636E9F0` · jhash `0xBE27AA3F` · **Cliente**

```lua
ResetReticuleValues()
```
```c
void RESET_RETICULE_VALUES();
```

**Devuelve:** `void`

---
### RestartFrontendMenu

`RESTART_FRONTEND_MENU` · hash `0x10706DC6AD2D49C0` · jhash `0xB07DAF98` · **Cliente**

```lua
RestartFrontendMenu(menuHash, highlightedTab)
```
```c
void RESTART_FRONTEND_MENU(Hash menuHash, int highlightedTab);
```

**Parámetros**

- `menuHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Hash of the frontend menu. See [`ACTIVATE_FRONTEND_MENU`](#activatefrontendmenu) for the list of available menus.
- `highlightedTab` (`int`): Menu ID (from PauseMenuLUT (in pause_menu_sp_content.gfx files), but the value - 1000) of which tab to have highlighted on the header, or -1.

**Devuelve:** `void`

**Descripción oficial:**

Changes the current frontend menu to the desired frontend menu version.

---
### SetAbilityBarValue

`SET_ABILITY_BAR_VALUE` · hash `0x9969599CCFF5D85E` · jhash `0x24E53FD8` · **Cliente**

```lua
SetAbilityBarValue(value, maxValue)
```
```c
void SET_ABILITY_BAR_VALUE(float value, float maxValue);
```

**Parámetros**

- `value` (`float`)
- `maxValue` (`float`)

**Devuelve:** `void`

---
### SetAbilityBarVisibilityInMultiplayer

`_SET_ABILITY_BAR_VISIBILITY_IN_MULTIPLAYER` · hash `0x1DFEDD15019315A9` · **Cliente**

```lua
SetAbilityBarVisibilityInMultiplayer(visible)
```
```c
void _SET_ABILITY_BAR_VISIBILITY_IN_MULTIPLAYER(BOOL visible);
```

**Parámetros**

- `visible` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### SetAllowAbilityBarInMultiplayer

`_SET_ALLOW_ABILITY_BAR_IN_MULTIPLAYER` · hash `0x889329C80FE5963C` · **Cliente**

```lua
SetAllowAbilityBarInMultiplayer(toggle)
```
```c
void _SET_ALLOW_ABILITY_BAR_IN_MULTIPLAYER(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### SetAllowCommaOnTextInput

`SET_ALLOW_COMMA_ON_TEXT_INPUT` · hash `0x577599CCED639CA2` · **Cliente**

```lua
SetAllowCommaOnTextInput(allow)
```
```c
void SET_ALLOW_COMMA_ON_TEXT_INPUT(BOOL allow);
```

**Parámetros**

- `allow` (`BOOL`): Toggles if the comma can be used in conjuction with the `filename` text input box type.

**Devuelve:** `void`

**Descripción oficial:**

**NOTE:** This must be called before you open the text input box.

**Nombres antiguos (alias):** `0x577599CCED639CA2` (`N_0x577599cced639ca2`)

---
### SetBigmapActive

`SET_BIGMAP_ACTIVE` · hash `0x231C8F89D0539D8F` · jhash `0x08EB83D2` · **Cliente**

```lua
SetBigmapActive(toggleBigMap, showFullMap)
```
```c
void SET_BIGMAP_ACTIVE(BOOL toggleBigMap, BOOL showFullMap);
```

**Parámetros**

- `toggleBigMap` (`BOOL`): Enable or disable the expanded minimap.
- `showFullMap` (`BOOL`): Enable or disable the full map from being shown on the minimap, requires p0 to be true.

**Devuelve:** `void`

**Descripción oficial:**

Toggles the big minimap state like in GTA:Online.

To get the current state of the minimap, use [`IS_BIGMAP_ACTIVE`](../cfx/cliente-1.md#isbigmapactive).

**Nombres antiguos (alias):** `_SET_RADAR_BIGMAP_ENABLED` (`SetRadarBigmapEnabled`)

---
### SetBlipAlpha

`SET_BLIP_ALPHA` · hash `0x45FF974EEE1C8734` · jhash `0xA791FCCD` · **Cliente**

```lua
SetBlipAlpha(blip, alpha)
```
```c
void SET_BLIP_ALPHA(Blip blip, int alpha);
```

**Parámetros**

- `blip` (`Blip`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets alpha-channel for blip color.
Example:
Blip blip = HUD::ADD_BLIP_FOR_ENTITY(entity);
HUD::SET_BLIP_COLOUR(blip , 3);
HUD::SET_BLIP_ALPHA(blip , 64);
```

---
### SetBlipAsFriendly

`SET_BLIP_AS_FRIENDLY` · hash `0x6F6F290102C02AB4` · jhash `0xF290CFD8` · **Cliente**

```lua
SetBlipAsFriendly(blip, toggle)
```
```c
void SET_BLIP_AS_FRIENDLY(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`): The blip handle
- `toggle` (`BOOL`): True for friendly, false for enemy

**Devuelve:** `void`

**Descripción oficial:**

Allows the user to set a blip as friendly or enemy based on the toggle.

---
### SetBlipAsMissionCreatorBlip

`SET_BLIP_AS_MISSION_CREATOR_BLIP` · hash `0x24AC0137444F9FD5` · jhash `0x802FB686` · **Cliente**

```lua
SetBlipAsMissionCreatorBlip(blip, toggle)
```
```c
void SET_BLIP_AS_MISSION_CREATOR_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetBlipAsShortRange

`SET_BLIP_AS_SHORT_RANGE` · hash `0xBE8BE4FE60E27B72` · jhash `0x5C67725E` · **Cliente**

```lua
SetBlipAsShortRange(blip, toggle)
```
```c
void SET_BLIP_AS_SHORT_RANGE(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`): The blip handle.
- `toggle` (`BOOL`): True to only display the blip as 'short range', false to display the blip from a longer distance.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether or not the specified blip should only be displayed when nearby, or on the minimap.

---
### SetBlipBright

`SET_BLIP_BRIGHT` · hash `0xB203913733F27884` · jhash `0x72BEE6DF` · **Cliente**

```lua
SetBlipBright(blip, toggle)
```
```c
void SET_BLIP_BRIGHT(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetBlipCategory

`SET_BLIP_CATEGORY` · hash `0x234CDD44D996FD9A` · jhash `0xEF72F533` · **Cliente**

```lua
SetBlipCategory(blip, index)
```
```c
void SET_BLIP_CATEGORY(Blip blip, int index);
```

**Parámetros**

- `blip` (`Blip`): The blip to change the category index of
- `index` (`int`): The category index to change to

**Devuelve:** `void`

**Descripción oficial:**

Examples result:

![](https://i.imgur.com/8MrVdmB.png)

**index:**

```
1 = No distance shown in legend
2 = Distance shown in legend
7 = "Other Players" category, also shows distance in legend
10 = "Property" category
11 = "Owned Property" category
12 - 133 = Custom named categories
134 - 254 = Custom unnamed categories
```

`index` wraps around after 255.

Blips with categories `7`, `10`, `11` or `12 - 254` (custom categories) will all show under the specific categories listing in the map legend, regardless of sprite or name.

**Legend entries**

| index | Legend entry | Label |
| --- | --- | --- |
| 7 | Other Players | `BLIP_OTHPLYR` |
| 10 | Property | `BLIP_PROPCAT` |
| 11 | Owned Property | `BLIP_APARTCAT` |
| 12 - 133 | Custom categories (Named) | `BLIP_CAT_` + `index` |
| 134 - 254 | Custom categories (Unnamed) | `-` |

**Ejemplo (lua):**

```lua
blip = AddBlipForCoord(-702.97290039063, -1393.2911376953, 5.1502623558044)
SetBlipSprite(blip, 370) -- Helipad For Sale
SetBlipCategory(blip, 10)

blip = AddBlipForCoord(-712.40521240234, -1298.7811279297, 5.1019215583801)
SetBlipSprite(blip, 371) -- Dock For Sale
SetBlipCategory(blip, 10)

blip = AddBlipForCoord(-927.92755126953, -2824.1362304688, 13.947744369507)
SetBlipSprite(blip, 372) -- Hangar For Sale
SetBlipCategory(blip, 10)

-- Custom named categories
blip = AddBlipForCoord(0.0, 0.0, 0.0)
SetBlipSprite(blip, 375) -- Business For Sale
SetBlipCategory(blip, 12)
AddTextEntry("BLIP_CAT_" .. 12, "Businesses For Sale")
```

---
### SetBlipColour

`SET_BLIP_COLOUR` · hash `0x03D7FB09E75D6B7E` · jhash `0xBB3C5A41` · **Cliente**

```lua
SetBlipColour(blip, color)
```
```c
void SET_BLIP_COLOUR(Blip blip, int color);
```

**Parámetros**

- `blip` (`Blip`): The blip handle to set the color of
- `color` (`int`): This can be a hex color code, or a [blip color](https://docs.fivem.net/docs/game-references/blips/#blip-colors).

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local coords = GetEntityCoords(PlayerPedId())
local blip = AddBlipForCoord(coords.x, coords.y, coords.z)

SetBlipColour(blip, 1) -- Sets the color to red (see list above)

-- You can also use a hex like so:
SetBlipColour(blip, 0x3A7F3AFF) -- Our custom green
```

---
### SetBlipCoords

`SET_BLIP_COORDS` · hash `0xAE2AF67E9D9AF65D` · jhash `0x680A34D4` · **Cliente**

```lua
SetBlipCoords(blip, posX, posY, posZ)
```
```c
void SET_BLIP_COORDS(Blip blip, float posX, float posY, float posZ);
```

**Parámetros**

- `blip` (`Blip`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `void`

---
### SetBlipDisplay

`SET_BLIP_DISPLAY` · hash `0x9029B2F3DA924928` · jhash `0x2B521F91` · **Cliente**

```lua
SetBlipDisplay(blip, displayId)
```
```c
void SET_BLIP_DISPLAY(Blip blip, int displayId);
```

**Parámetros**

- `blip` (`Blip`)
- `displayId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

**displayId Behaviour**

| display ID 	| Behaviour                                                   	|
|------------	|-------------------------------------------------------------	|
| 0          	| Doesn't show up, ever, anywhere.                            	|
| 1          	| Doesn't show up, ever, anywhere.                            	|
| 2          	| Shows on both main map and minimap. (Selectable on map)     	|
| 3          	| Shows on main map only. (Selectable on map)                 	|
| 4          	| Shows on main map only. (Selectable on map)                 	|
| 5          	| Shows on minimap only.                                      	|
| 6          	| Shows on both main map and minimap. (Selectable on map)     	|
| 7          	| Doesn't show up, ever, anywhere.                            	|
| 8          	| Shows on both main map and minimap. (Not selectable on map) 	|
| 9          	| Shows on minimap only.                                      	|
| 10         	| Shows on both main map and minimap. (Not selectable on map) 	|

Anything higher than 10 seems to be exactly the same as 10.

Rockstar seem to only use 0, 2, 3, 4, 5 and 8 in the decompiled scripts.

---
### SetBlipDisplayIndicatorOnBlip

`_SET_BLIP_DISPLAY_INDICATOR_ON_BLIP` · hash `0xC4278F70131BAA6D` · jhash `0x6AA6A1CC` · **Cliente**

```lua
SetBlipDisplayIndicatorOnBlip(blip, toggle)
```
```c
void _SET_BLIP_DISPLAY_INDICATOR_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Must be toggled before being queued for animation
```

**Nombres antiguos (alias):** `0xC4278F70131BAA6D` (`N_0xc4278f70131baa6d`)

---
### SetBlipFade

`SET_BLIP_FADE` · hash `0x2AEE8F8390D2298C` · jhash `0xA5999031` · **Cliente**

```lua
SetBlipFade(blip, opacity, duration)
```
```c
void SET_BLIP_FADE(Blip blip, int opacity, int duration);
```

**Parámetros**

- `blip` (`Blip`)
- `opacity` (`int`)
- `duration` (`int`)

**Devuelve:** `void`

---
### SetBlipFlashInterval

`SET_BLIP_FLASH_INTERVAL` · hash `0xAA51DB313C010A7E` · jhash `0xEAF67377` · **Cliente**

```lua
SetBlipFlashInterval(blip, interval)
```
```c
void SET_BLIP_FLASH_INTERVAL(Blip blip, int interval);
```

**Parámetros**

- `blip` (`Blip`): The blip to change flashing interval
- `interval` (`int`): Interval in milliseconds before flashing the blip

**Devuelve:** `void`

**Descripción oficial:**

Sets the interval in milliseconds before flashing the blip.

**Ejemplo (lua):**

```lua
local blip = AddBlipForCoord(0, 0, 0)

SetBlipFlashes(blip, true)

-- flash the blip every 50ms
SetBlipFlashInterval(blip, 50)
```

**Ejemplo (js):**

```js
const blip = AddBlipForCoord(0, 0, 0)

SetBlipFlashes(blip, true)

// flash the blip every 50ms
SetBlipFlashInterval(blip, 50)
```

---
### SetBlipFlashTimer

`SET_BLIP_FLASH_TIMER` · hash `0xD3CD6FD297AE87CC` · jhash `0x8D5DF611` · **Cliente**

```lua
SetBlipFlashTimer(blip, duration)
```
```c
void SET_BLIP_FLASH_TIMER(Blip blip, int duration);
```

**Parámetros**

- `blip` (`Blip`): The blip to start flashing
- `duration` (`int`): Time in milliseconds to flash the blip before stopping

**Devuelve:** `void`

**Descripción oficial:**

Flashes blip for time in milliseconds before stopping.

**Ejemplo (lua):**

```lua
local blip = AddBlipForCoord(0, 0, 0)

-- flash blip for seven seconds then stop
SetBlipFlashTimer(blip, 7000)
```

**Ejemplo (js):**

```js
const blip = AddBlipForCoord(0, 0, 0)

//flash blip for seven seconds then stop
SetBlipFlashTimer(blip, 7000)
```

---
### SetBlipFlashes

`SET_BLIP_FLASHES` · hash `0xB14552383D39CE3E` · jhash `0xC0047F15` · **Cliente**

```lua
SetBlipFlashes(blip, toggle)
```
```c
void SET_BLIP_FLASHES(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetBlipFlashesAlternate

`SET_BLIP_FLASHES_ALTERNATE` · hash `0x2E8D9498C56DD0D1` · jhash `0x1A81202B` · **Cliente**

```lua
SetBlipFlashesAlternate(blip, toggle)
```
```c
void SET_BLIP_FLASHES_ALTERNATE(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetBlipHiddenOnLegend

`SET_BLIP_HIDDEN_ON_LEGEND` · hash `0x54318C915D27E4CE` · jhash `0x43996428` · **Cliente**

```lua
SetBlipHiddenOnLegend(blip, toggle)
```
```c
void SET_BLIP_HIDDEN_ON_LEGEND(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x54318C915D27E4CE` (`N_0x54318c915d27e4ce`)

---
### SetBlipHighDetail

`SET_BLIP_HIGH_DETAIL` · hash `0xE2590BC29220CEBB` · jhash `0xD5842BFF` · **Cliente**

```lua
SetBlipHighDetail(blip, toggle)
```
```c
void SET_BLIP_HIGH_DETAIL(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetBlipNameFromTextFile

`SET_BLIP_NAME_FROM_TEXT_FILE` · hash `0xEAA0FFE120D92784` · jhash `0xAC8A5461` · **Cliente**

```lua
SetBlipNameFromTextFile(blip, gxtEntry)
```
```c
void SET_BLIP_NAME_FROM_TEXT_FILE(Blip blip, char* gxtEntry);
```

**Parámetros**

- `blip` (`Blip`)
- `gxtEntry` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Doesn't work if the label text of gxtEntry is >= 80.  
```

---
### SetBlipNameToPlayerName

`SET_BLIP_NAME_TO_PLAYER_NAME` · hash `0x127DE7B20C60A6A3` · jhash `0x03A0B8F9` · **Cliente**

```lua
SetBlipNameToPlayerName(blip, player)
```
```c
void SET_BLIP_NAME_TO_PLAYER_NAME(Blip blip, Player player);
```

**Parámetros**

- `blip` (`Blip`)
- `player` (`Player`)

**Devuelve:** `void`

---
### SetBlipPriority

`SET_BLIP_PRIORITY` · hash `0xAE9FC9EF6A9FAC79` · jhash `0xCE87DA6F` · **Cliente**

```lua
SetBlipPriority(blip, priority)
```
```c
void SET_BLIP_PRIORITY(Blip blip, int priority);
```

**Parámetros**

- `blip` (`Blip`)
- `priority` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
See this topic for more details : gtaforums.com/topic/717612-v-scriptnative-documentation-and-research/page-35?p=1069477935  
```

---
### SetBlipRotation

`SET_BLIP_ROTATION` · hash `0xF87683CDF73C3F6E` · jhash `0x6B8F44FE` · **Cliente**

```lua
SetBlipRotation(blip, rotation)
```
```c
void SET_BLIP_ROTATION(Blip blip, int rotation);
```

**Parámetros**

- `blip` (`Blip`)
- `rotation` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
After some testing, looks like you need to use CEIL() on the rotation (vehicle/ped heading) before using it there.
```

---
### SetBlipRoute

`SET_BLIP_ROUTE` · hash `0x4F7D8A9BFB0B43E9` · jhash `0x3E160C90` · **Cliente**

```lua
SetBlipRoute(blip, enabled)
```
```c
void SET_BLIP_ROUTE(Blip blip, BOOL enabled);
```

**Parámetros**

- `blip` (`Blip`)
- `enabled` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enable / disable showing route for the Blip-object.  
```

---
### SetBlipRouteColour

`SET_BLIP_ROUTE_COLOUR` · hash `0x837155CD2F63DA09` · jhash `0xDDE7C65C` · **Cliente**

```lua
SetBlipRouteColour(blip, colour)
```
```c
void SET_BLIP_ROUTE_COLOUR(Blip blip, int colour);
```

**Parámetros**

- `blip` (`Blip`)
- `colour` (`int`)

**Devuelve:** `void`

---
### SetBlipScale

`SET_BLIP_SCALE` · hash `0xD38744167B2FA257` · jhash `0x1E6EC434` · **Cliente**

```lua
SetBlipScale(blip, scale)
```
```c
void SET_BLIP_SCALE(Blip blip, float scale);
```

**Parámetros**

- `blip` (`Blip`)
- `scale` (`float`)

**Devuelve:** `void`

---
### SetBlipScaleTransformation

`_SET_BLIP_SCALE_TRANSFORMATION` · hash `0xCD6524439909C979` · **Cliente**

```lua
SetBlipScaleTransformation(blip, xScale, yScale)
```
```c
void _SET_BLIP_SCALE_TRANSFORMATION(Blip blip, float xScale, float yScale);
```

**Parámetros**

- `blip` (`Blip`)
- `xScale` (`float`)
- `yScale` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Preview:
![](https://i.imgur.com/jH2JMUl.png)

```
NativeDB Introduced: v1734
```

---
### SetBlipSecondaryColour

`SET_BLIP_SECONDARY_COLOUR` · hash `0x14892474891E09EB` · jhash `0xC6384D32` · **Cliente**

```lua
SetBlipSecondaryColour(blip, r, g, b)
```
```c
void SET_BLIP_SECONDARY_COLOUR(Blip blip, int r, int g, int b);
```

**Parámetros**

- `blip` (`Blip`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

---
### SetBlipShowCone

`SET_BLIP_SHOW_CONE` · hash `0x13127EC3665E8EE1` · jhash `0xFF545AD8` · **Cliente**

```lua
SetBlipShowCone(blip, toggle)
```
```c
void SET_BLIP_SHOW_CONE(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 3: Any p2
```

---
### SetBlipShrink

`_SET_BLIP_SHRINK` · hash `0x2B6D467DAB714E8D` · jhash `0xC575F0BC` · **Cliente**

```lua
SetBlipShrink(blip, toggle)
```
```c
void _SET_BLIP_SHRINK(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes a blip go small when off the minimap.
SET_BLIP_AS_*
```

**Nombres antiguos (alias):** `0x2B6D467DAB714E8D` (`N_0x2b6d467dab714e8d`)

---
### SetBlipSprite

`SET_BLIP_SPRITE` · hash `0xDF735600A4696DAF` · jhash `0x8DBBB0B9` · **Cliente · también en el servidor (RPC)**

```lua
SetBlipSprite(blip, spriteId)
```
```c
void SET_BLIP_SPRITE(Blip blip, int spriteId);
```

**Parámetros**

- `blip` (`Blip`): The blip to change.
- `spriteId` (`int`): The sprite ID to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets the displayed sprite for a specific blip.

There's a [list of sprites](https://docs.fivem.net/docs/game-references/blips/) on the FiveM documentation site.

**Ejemplo (lua):**

```lua
SetBlipSprite(blip, 588) -- changes `blip` to radar_nhp_orbit
```

---
### SetBlipSquaredRotation

`_SET_BLIP_SQUARED_ROTATION` · hash `0xA8B6AFDAC320AC87` · **Cliente**

```lua
SetBlipSquaredRotation(blip, heading)
```
```c
void _SET_BLIP_SQUARED_ROTATION(Blip blip, float heading);
```

**Parámetros**

- `blip` (`Blip`)
- `heading` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does not require whole number/integer rotations.
```

**Nombres antiguos (alias):** `0xA8B6AFDAC320AC87` (`N_0xa8b6afdac320ac87`)

---
### SetColourOfNextTextComponent

`SET_COLOUR_OF_NEXT_TEXT_COMPONENT` · hash `0x39BBF623FC803EAC` · jhash `0x6F1A1901` · **Cliente**

```lua
SetColourOfNextTextComponent(hudColor)
```
```c
void SET_COLOUR_OF_NEXT_TEXT_COMPONENT(int hudColor);
```

**Parámetros**

- `hudColor` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x39BBF623FC803EAC` (`N_0x39bbf623fc803eac`), `_SET_NOTIFICATION_COLOR_NEXT` (`SetNotificationColorNext`)

---
### SetCustomMpHudColor

`SET_CUSTOM_MP_HUD_COLOR` · hash `0x2ACCB195F3CCD9DE` · **Cliente**

```lua
SetCustomMpHudColor(hudColorId)
```
```c
void SET_CUSTOM_MP_HUD_COLOR(int hudColorId);
```

**Parámetros**

- `hudColorId` (`int`): The ID of the custom HUD color. Use -1 (`HUD_COLOUR_INVALID`) to clear the custom color. Refer to the `eHudColours` enum for valid color IDs.

**Devuelve:** `void`

**Descripción oficial:**

Set a custom color for the MP HUD, providing a way to customize the HUD's appearance similar to character color changes in MP.

```cpp
enum eHudColours {
    HUD_COLOUR_PURE_WHITE = 0,
    HUD_COLOUR_WHITE = 1,
    HUD_COLOUR_BLACK = 2,
    HUD_COLOUR_GREY = 3,
    HUD_COLOUR_GREYLIGHT = 4,
    HUD_COLOUR_GREYDARK = 5,
    HUD_COLOUR_RED = 6,
    HUD_COLOUR_REDLIGHT = 7,
    HUD_COLOUR_REDDARK = 8,
    HUD_COLOUR_BLUE = 9,
    HUD_COLOUR_BLUELIGHT = 10,
    HUD_COLOUR_BLUEDARK = 11,
    HUD_COLOUR_YELLOW = 12,
    HUD_COLOUR_YELLOWLIGHT = 13,
    HUD_COLOUR_YELLOWDARK = 14,
    HUD_COLOUR_ORANGE = 15,
    HUD_COLOUR_ORANGELIGHT = 16,
    HUD_COLOUR_ORANGEDARK = 17,
    HUD_COLOUR_GREEN = 18,
    HUD_COLOUR_GREENLIGHT = 19,
    HUD_COLOUR_GREENDARK = 20,
    HUD_COLOUR_PURPLE = 21,
    HUD_COLOUR_PURPLELIGHT = 22,
    HUD_COLOUR_PURPLEDARK = 23,
    HUD_COLOUR_PINK = 24,
    HUD_COLOUR_STAR = 25,
    HUD_COLOUR_STARLIGHT = 26,
    HUD_COLOUR_STARDARK = 27,
    HUD_COLOUR_NET_PLAYER1 = 28,
    HUD_COLOUR_NET_PLAYER2 = 29,
    HUD_COLOUR_NET_PLAYER3 = 30,
    HUD_COLOUR_NET_PLAYER4 = 31,
    HUD_COLOUR_NET_PLAYER5 = 32,
    HUD_COLOUR_NET_PLAYER6 = 33,
    HUD_COLOUR_NET_PLAYER7 = 34,
    HUD_COLOUR_NET_PLAYER8 = 35,
    HUD_COLOUR_NET_PLAYER9 = 36,
    HUD_COLOUR_NET_PLAYER10 = 37,
    HUD_COLOUR_NET_PLAYER11 = 38,
    HUD_COLOUR_NET_PLAYER12 = 39,
    HUD_COLOUR_NET_PLAYER13 = 40,
    HUD_COLOUR_NET_PLAYER14 = 41,
    HUD_COLOUR_NET_PLAYER15 = 42,
    HUD_COLOUR_NET_PLAYER16 = 43,
    HUD_COLOUR_NET_PLAYER17 = 44,
    HUD_COLOUR_NET_PLAYER18 = 45,
    HUD_COLOUR_NET_PLAYER19 = 46,
    HUD_COLOUR_NET_PLAYER20 = 47,
    HUD_COLOUR_NET_PLAYER21 = 48,
    HUD_COLOUR_NET_PLAYER22 = 49,
    HUD_COLOUR_NET_PLAYER23 = 50,
    HUD_COLOUR_NET_PLAYER24 = 51,
    HUD_COLOUR_NET_PLAYER25 = 52,
    HUD_COLOUR_NET_PLAYER26 = 53,
    HUD_COLOUR_NET_PLAYER27 = 54,
    HUD_COLOUR_NET_PLAYER28 = 55,
    HUD_COLOUR_NET_PLAYER29 = 56,
    HUD_COLOUR_NET_PLAYER30 = 57,
    HUD_COLOUR_NET_PLAYER31 = 58,
    HUD_COLOUR_NET_PLAYER32 = 59,
    HUD_COLOUR_SIMPLEBLIP_DEFAULT = 60,
    HUD_COLOUR_MENU_BLUE = 61,
    HUD_COLOUR_MENU_GREY_LIGHT = 62,
    HUD_COLOUR_MENU_BLUE_EXTRA_DARK = 63,
    HUD_COLOUR_MENU_YELLOW = 64,
    HUD_COLOUR_MENU_YELLOW_DARK = 65,
    HUD_COLOUR_MENU_GREEN = 66,
    HUD_COLOUR_MENU_GREY = 67,
    HUD_COLOUR_MENU_GREY_DARK = 68,
    HUD_COLOUR_MENU_HIGHLIGHT = 69,
    HUD_COLOUR_MENU_STANDARD = 70,
    HUD_COLOUR_MENU_DIMMED = 71,
    HUD_COLOUR_MENU_EXTRA_DIMMED = 72,
    HUD_COLOUR_BRIEF_TITLE = 73,
    HUD_COLOUR_MID_GREY_MP = 74,
    HUD_COLOUR_NET_PLAYER1_DARK = 75,
    HUD_COLOUR_NET_PLAYER2_DARK = 76,
    HUD_COLOUR_NET_PLAYER3_DARK = 77,
    HUD_COLOUR_NET_PLAYER4_DARK = 78,
    HUD_COLOUR_NET_PLAYER5_DARK = 79,
    HUD_COLOUR_NET_PLAYER6_DARK = 80,
    HUD_COLOUR_NET_PLAYER7_DARK = 81,
    HUD_COLOUR_NET_PLAYER8_DARK = 82,
    HUD_COLOUR_NET_PLAYER9_DARK = 83,
    HUD_COLOUR_NET_PLAYER10_DARK = 84,
    HUD_COLOUR_NET_PLAYER11_DARK = 85,
    HUD_COLOUR_NET_PLAYER12_DARK = 86,
    HUD_COLOUR_NET_PLAYER13_DARK = 87,
    HUD_COLOUR_NET_PLAYER14_DARK = 88,
    HUD_COLOUR_NET_PLAYER15_DARK = 89,
    HUD_COLOUR_NET_PLAYER16_DARK = 90,
    HUD_COLOUR_NET_PLAYER17_DARK = 91,
    HUD_COLOUR_NET_PLAYER18_DARK = 92,
    HUD_COLOUR_NET_PLAYER19_DARK = 93,
    HUD_COLOUR_NET_PLAYER20_DARK = 94,
    HUD_COLOUR_NET_PLAYER21_DARK = 95,
    HUD_COLOUR_NET_PLAYER22_DARK = 96,
    HUD_COLOUR_NET_PLAYER23_DARK = 97,
    HUD_COLOUR_NET_PLAYER24_DARK = 98,
    HUD_COLOUR_NET_PLAYER25_DARK = 99,
    HUD_COLOUR_NET_PLAYER26_DARK = 100,
    HUD_COLOUR_NET_PLAYER27_DARK = 101,
    HUD_COLOUR_NET_PLAYER28_DARK = 102,
    HUD_COLOUR_NET_PLAYER29_DARK = 103,
    HUD_COLOUR_NET_PLAYER30_DARK = 104,
    HUD_COLOUR_NET_PLAYER31_DARK = 105,
    HUD_COLOUR_NET_PLAYER32_DARK = 106,
    HUD_COLOUR_BRONZE = 107,
    HUD_COLOUR_SILVER = 108,
    HUD_COLOUR_GOLD = 109,
    HUD_COLOUR_PLATINUM = 110,
    HUD_COLOUR_GANG1 = 111,
    HUD_COLOUR_GANG2 = 112,
    HUD_COLOUR_GANG3 = 113,
    HUD_COLOUR_GANG4 = 114,
    HUD_COLOUR_SAME_CREW = 115,
    HUD_COLOUR_FREEMODE = 116,
    HUD_COLOUR_PAUSE_BG = 117,
    HUD_COLOUR_FRIENDLY = 118,
    HUD_COLOUR_ENEMY = 119,
    HUD_COLOUR_LOCATION = 120,
    HUD_COLOUR_PICKUP = 121,
    HUD_COLOUR_PAUSE_SINGLEPLAYER = 122,
    HUD_COLOUR_FREEMODE_DARK = 123,
    HUD_COLOUR_INACTIVE_MISSION = 124,
    HUD_COLOUR_DAMAGE = 125,
    HUD_COLOUR_PINKLIGHT = 126,
    HUD_COLOUR_PM_MITEM_HIGHLIGHT = 127,
    HUD_COLOUR_SCRIPT_VARIABLE = 128,
    HUD_COLOUR_YOGA = 129,
    HUD_COLOUR_TENNIS = 130,
    HUD_COLOUR_GOLF = 131,
    HUD_COLOUR_SHOOTING_RANGE = 132,
    HUD_COLOUR_FLIGHT_SCHOOL = 133,
    HUD_COLOUR_NORTH_BLUE = 134,
    HUD_COLOUR_SOCIAL_CLUB = 135,
    HUD_COLOUR_PLATFORM_BLUE = 136,
    HUD_COLOUR_PLATFORM_GREEN = 137,
    HUD_COLOUR_PLATFORM_GREY = 138,
    HUD_COLOUR_FACEBOOK_BLUE = 139,
    HUD_COLOUR_INGAME_BG = 140,
    HUD_COLOUR_DARTS = 141,
    HUD_COLOUR_WAYPOINT = 142,
    HUD_COLOUR_MICHAEL = 143,
    HUD_COLOUR_FRANKLIN = 144,
    HUD_COLOUR_TREVOR = 145,
    HUD_COLOUR_GOLF_P1 = 146,
    HUD_COLOUR_GOLF_P2 = 147,
    HUD_COLOUR_GOLF_P3 = 148,
    HUD_COLOUR_GOLF_P4 = 149,
    HUD_COLOUR_WAYPOINTLIGHT = 150,
    HUD_COLOUR_WAYPOINTDARK = 151,
    HUD_COLOUR_PANEL_LIGHT = 152,
    HUD_COLOUR_MICHAEL_DARK = 153,
    HUD_COLOUR_FRANKLIN_DARK = 154,
    HUD_COLOUR_TREVOR_DARK = 155,
    HUD_COLOUR_OBJECTIVE_ROUTE = 156,
    HUD_COLOUR_PAUSEMAP_TINT = 157,
    HUD_COLOUR_PAUSE_DESELECT = 158,
    HUD_COLOUR_PM_WEAPONS_PURCHASABLE = 159,
    HUD_COLOUR_PM_WEAPONS_LOCKED = 160,
    HUD_COLOUR_END_SCREEN_BG = 161,
    HUD_COLOUR_CHOP = 162,
    HUD_COLOUR_PAUSEMAP_TINT_HALF = 163,
    HUD_COLOUR_NORTH_BLUE_OFFICIAL = 164,
    HUD_COLOUR_SCRIPT_VARIABLE_2 = 165,
    HUD_COLOUR_H = 166,
    HUD_COLOUR_HDARK = 167,
    HUD_COLOUR_T = 168,
    HUD_COLOUR_TDARK = 169,
    HUD_COLOUR_HSHARD = 170,
    HUD_COLOUR_CONTROLLER_MICHAEL = 171 
    HUD_COLOUR_CONTROLLER_FRANKLIN = 172 
    HUD_COLOUR_CONTROLLER_TREVOR = 173 
    HUD_COLOUR_CONTROLLER_CHOP = 174,
    HUD_COLOUR_VIDEO_EDITOR_VIDEO = 175,
    HUD_COLOUR_VIDEO_EDITOR_AUDIO = 176,
    HUD_COLOUR_VIDEO_EDITOR_TEXT = 177,
    HUD_COLOUR_HB_BLUE = 178,
    HUD_COLOUR_HB_YELLOW = 179,
    HUD_COLOUR_VIDEO_EDITOR_SCORE = 180,
    HUD_COLOUR_VIDEO_EDITOR_AUDIO_FADEOUT = 181,
    HUD_COLOUR_VIDEO_EDITOR_TEXT_FADEOUT = 182,
    HUD_COLOUR_VIDEO_EDITOR_SCORE_FADEOUT = 183,
    HUD_COLOUR_HEIST_BACKGROUND = 184,
    HUD_COLOUR_VIDEO_EDITOR_AMBIENT = 185,
    HUD_COLOUR_VIDEO_EDITOR_AMBIENT_FADEOUT = 186,
    HUD_COLOUR_GANG_BOSS = 187,
    HUD_COLOUR_GOON = 188,
    HUD_COLOUR_BOSS = 189,
    HUD_COLOUR_LOW_FLOW = 190,
    HUD_COLOUR_LOW_FLOW_DARK = 191,
    HUD_COLOUR_G1 = 192,
    HUD_COLOUR_G2 = 193,
    HUD_COLOUR_G3 = 194,
    HUD_COLOUR_G4 = 195,
    HUD_COLOUR_G5 = 196,
    HUD_COLOUR_G6 = 197,
    HUD_COLOUR_G7 = 198,
    HUD_COLOUR_G8 = 199,
    HUD_COLOUR_G9 = 200,
    HUD_COLOUR_G10 = 201,
    HUD_COLOUR_G11 = 202,
    HUD_COLOUR_G12 = 203,
    HUD_COLOUR_G13 = 204,
    HUD_COLOUR_G14 = 205,
    HUD_COLOUR_G15 = 206,
    HUD_COLOUR_ADVERSARY = 207,
    HUD_COLOUR_DEGEN_RED = 208,
    HUD_COLOUR_DEGEN_YELLOW = 209,
    HUD_COLOUR_DEGEN_GREEN = 210,
    HUD_COLOUR_DEGEN_CYAN = 211,
    HUD_COLOUR_DEGEN_BLUE = 212,
    HUD_COLOUR_DEGEN_MAGENTA = 213,
    HUD_COLOUR_STUNT_1 = 214,
    HUD_COLOUR_STUNT_2 = 215,
    HUD_COLOUR_SPECIAL_RACE_SERIES = 216 
    HUD_COLOUR_SPECIAL_RACE_SERIES_DARK = 217,
    HUD_COLOUR_CS = 218 
    HUD_COLOUR_CS_DARK = 219,
    HUD_COLOUR_TECH_GREEN = 220,
    HUD_COLOUR_TECH_GREEN_DARK = 221,
    HUD_COLOUR_TECH_RED = 222,
    HUD_COLOUR_TECH_GREEN_VERY_DARK = 223,
    HUD_COLOUR_PLACEHOLDER_01 = 224,
    HUD_COLOUR_PLACEHOLDER_02 = 225,
    HUD_COLOUR_PLACEHOLDER_03 = 226,
    HUD_COLOUR_PLACEHOLDER_04 = 227,
    HUD_COLOUR_PLACEHOLDER_05 = 228,
    HUD_COLOUR_PLACEHOLDER_06 = 229,
    HUD_COLOUR_PLACEHOLDER_07 = 230,
    HUD_COLOUR_PLACEHOLDER_08 = 231,
    HUD_COLOUR_PLACEHOLDER_09 = 232,
    HUD_COLOUR_PLACEHOLDER_10 = 233,
    HUD_COLOUR_JUNK_ENERGY = 234
};
```

```
NativeDB Introduced: 2545
```

---
### SetDirectorModeClearTriggeredFlag

`_SET_DIRECTOR_MODE_CLEAR_TRIGGERED_FLAG` · hash `0x2632482FD6B9AB87` · **Cliente**

```lua
SetDirectorModeClearTriggeredFlag()
```
```c
void _SET_DIRECTOR_MODE_CLEAR_TRIGGERED_FLAG();
```

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
```

**Nombres antiguos (alias):** `0x2632482FD6B9AB87` (`N_0x2632482fd6b9ab87`)

---
### SetFakePausemapPlayerPositionThisFrame

`SET_FAKE_PAUSEMAP_PLAYER_POSITION_THIS_FRAME` · hash `0x77E2DD177910E1CF` · jhash `0x54E75C7D` · **Cliente**

```lua
SetFakePausemapPlayerPositionThisFrame(x, y)
```
```c
void SET_FAKE_PAUSEMAP_PLAYER_POSITION_THIS_FRAME(float x, float y);
```

**Parámetros**

- `x` (`float`): X coord of the position.
- `y` (`float`): Y coord of the position.

**Devuelve:** `void`

**Descripción oficial:**

Overrides the position of the main player blip for the current frame.

**Nombres antiguos (alias):** `0x77E2DD177910E1CF` (`N_0x77e2dd177910e1cf`), `_SET_PLAYER_BLIP_POSITION_THIS_FRAME` (`SetPlayerBlipPositionThisFrame`)

**Ejemplo (lua):**

```lua
-- Function to check if player is using the map
local function IsPlayerUsingPausemap()
  return IsPauseMenuActive() and GetNumberOfReferencesOfScriptWithNameHash(`pausemenu_map`) > 0
end

Citizen.CreateThread(function()
  while true do
    Wait(0) -- Not using Wait will cause the game to hang.

    if IsPlayerUsingPausemap() and not IsPausemapInInteriorMode() then -- Make sure the player using the map and the map has switched view
      SetFakePausemapPlayerPositionThisFrame(0.0, 0.0) -- Override position
    end
  end
end)
```

---
### SetFloatingHelpTextScreenPosition

`SET_FLOATING_HELP_TEXT_SCREEN_POSITION` · hash `0x7679CC1BCEBE3D4C` · jhash `0x198F32D7` · **Cliente**

```lua
SetFloatingHelpTextScreenPosition(hudIndex, x, y)
```
```c
void SET_FLOATING_HELP_TEXT_SCREEN_POSITION(int hudIndex, float x, float y);
```

**Parámetros**

- `hudIndex` (`int`)
- `x` (`float`)
- `y` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7679CC1BCEBE3D4C` (`N_0x7679cc1bcebe3d4c`)

---
### SetFloatingHelpTextStyle

`SET_FLOATING_HELP_TEXT_STYLE` · hash `0x788E7FD431BD67F1` · jhash `0x97852A82` · **Cliente**

```lua
SetFloatingHelpTextStyle(hudIndex, style, hudColor, alpha, arrowPosition, boxOffset)
```
```c
void SET_FLOATING_HELP_TEXT_STYLE(int hudIndex, int style, int hudColor, int alpha, int arrowPosition, int boxOffset);
```

**Parámetros**

- `hudIndex` (`int`): The hud index for the floating help message
- `style` (`int`): Value 0 won't show an arrow at all. Values 1, 2 and -2 will display an arrow.
- `hudColor` (`int`): https://docs.fivem.net/docs/game-references/hud-colors/
- `alpha` (`int`): Value for the help box opacity, from 0-255. Anything greater will simply ignore the alpha value. Always 191 in R\* scripts.
- `arrowPosition` (`int`): Used to set the arrow positon. No value will hide the arrow
- `boxOffset` (`int`): Offset for the floating help box. Note: Arrow stays fixed

**Devuelve:** `void`

**Descripción oficial:**

**Arrow Positions**

*   0 = Off / No arrow
*   1 = Top
*   2 = Left
*   3 = Bottom
*   4 = Right

**Note**

Any numeric value greater than 4 will result in a right arrow (Index 4)

**Important**

Needs to be called every frame

![Preview of the provided example code](https://forum.cfx.re/uploads/default/original/4X/7/f/3/7f319bc93c3a00b8829bd4ac8dddc235fbf3a9ef.png)

**Nombres antiguos (alias):** `0x788E7FD431BD67F1` (`N_0x788e7fd431bd67f1`)

**Ejemplo (lua):**

```lua
function DisplayHelpText(string)
    BeginTextCommandDisplayHelp("STRING")
    AddTextComponentSubstringPlayerName(string)
    EndTextCommandDisplayHelp(1, false, false, 0)
end

CreateThread(function()
    while true do
        Wait(0)

        local Ped = PlayerPedId()

        DisplayHelpText('Example Text')
        SetFloatingHelpTextStyle(0, 2, 2, 0, 3, 0)
        SetFloatingHelpTextToEntity(0, Ped, 0, 0)
    end
end)
```

**Ejemplo (js):**

```js
function DisplayHelpText(string) {
    BeginTextCommandDisplayHelp("STRING")
    AddTextComponentSubstringPlayerName(string)
    EndTextCommandDisplayHelp(1, false, false, 0)
}

setTick(() => {
    const Ped = PlayerPedId()

    DisplayHelpText('Example Text')
    SetFloatingHelpTextStyle(0, 2, 2, 0, 3, 0)
    SetFloatingHelpTextToEntity(0, Ped, 0, 0)
})
```

---
### SetFloatingHelpTextToEntity

`SET_FLOATING_HELP_TEXT_TO_ENTITY` · hash `0xB094BC1DB4018240` · jhash `0x18B012B7` · **Cliente**

```lua
SetFloatingHelpTextToEntity(hudIndex, entity, offsetX, offsetY)
```
```c
void SET_FLOATING_HELP_TEXT_TO_ENTITY(int hudIndex, Entity entity, float offsetX, float offsetY);
```

**Parámetros**

- `hudIndex` (`int`)
- `entity` (`Entity`)
- `offsetX` (`float`)
- `offsetY` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB094BC1DB4018240` (`N_0xb094bc1db4018240`)

---
### SetFloatingHelpTextWorldPosition

`SET_FLOATING_HELP_TEXT_WORLD_POSITION` · hash `0x784BA7E0ECEB4178` · jhash `0x93045157` · **Cliente**

```lua
SetFloatingHelpTextWorldPosition(hudIndex, x, y, z)
```
```c
void SET_FLOATING_HELP_TEXT_WORLD_POSITION(int hudIndex, float x, float y, float z);
```

**Parámetros**

- `hudIndex` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x784BA7E0ECEB4178` (`N_0x784ba7e0eceb4178`)

---
### SetFrontendActive

`SET_FRONTEND_ACTIVE` · hash `0x745711A75AB09277` · jhash `0x81E1AD32` · **Cliente**

```lua
SetFrontendActive(active)
```
```c
void SET_FRONTEND_ACTIVE(BOOL active);
```

**Parámetros**

- `active` (`BOOL`)

**Devuelve:** `void`

---
### SetGpsCustomRouteRender

`SET_GPS_CUSTOM_ROUTE_RENDER` · hash `0x900086F371220B6F` · jhash `0xDA0AF00E` · **Cliente**

```lua
SetGpsCustomRouteRender(toggle, radarThickness, mapThickness)
```
```c
void SET_GPS_CUSTOM_ROUTE_RENDER(BOOL toggle, int radarThickness, int mapThickness);
```

**Parámetros**

- `toggle` (`BOOL`)
- `radarThickness` (`int`): The width of the GPS route on the radar
- `mapThickness` (`int`): The width of the GPS route on the map

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x900086F371220B6F` (`N_0x900086f371220b6f`)

---
### SetGpsFlags

`SET_GPS_FLAGS` · hash `0x5B440763A4C8D15B` · jhash `0x60539BAB` · **Cliente**

```lua
SetGpsFlags(p0, p1)
```
```c
void SET_GPS_FLAGS(int p0, float p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only the script that originally called SET_GPS_FLAGS can set them again. Another script cannot set the flags, until the first script that called it has called CLEAR_GPS_FLAGS.
Doesn't seem like the flags are actually read by the game at all.
```

---
### SetGpsFlashes

`SET_GPS_FLASHES` · hash `0x320D0E0D936A0E9B` · jhash `0xE991F733` · **Cliente**

```lua
SetGpsFlashes(toggle)
```
```c
void SET_GPS_FLASHES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetGpsMultiRouteRender

`SET_GPS_MULTI_ROUTE_RENDER` · hash `0x3DDA37128DD1ACA8` · jhash `0xE87CBE4C` · **Cliente**

```lua
SetGpsMultiRouteRender(toggle)
```
```c
void SET_GPS_MULTI_ROUTE_RENDER(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3DDA37128DD1ACA8` (`N_0x3dda37128dd1aca8`)

---
### SetHealthHudDisplayValues

`SET_HEALTH_HUD_DISPLAY_VALUES` · hash `0x3F5CC444DCAAA8F2` · jhash `0x7FB6FB2A` · **Cliente**

```lua
SetHealthHudDisplayValues(health, capacity, wasAdded)
```
```c
void SET_HEALTH_HUD_DISPLAY_VALUES(int health, int capacity, BOOL wasAdded);
```

**Parámetros**

- `health` (`int`)
- `capacity` (`int`)
- `wasAdded` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3F5CC444DCAAA8F2` (`N_0x3f5cc444dcaaa8f2`)

---
### SetHelpMessageTextStyle

`_SET_HELP_MESSAGE_TEXT_STYLE` · hash `0xB9C362BABECDDC7A` · **Cliente**

```lua
SetHelpMessageTextStyle(style, hudColor, alpha, p3, p4)
```
```c
void _SET_HELP_MESSAGE_TEXT_STYLE(int style, int hudColor, int alpha, int p3, int p4);
```

**Parámetros**

- `style` (`int`)
- `hudColor` (`int`)
- `alpha` (`int`)
- `p3` (`int`)
- `p4` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB9C362BABECDDC7A` (`N_0xb9c362babecddc7a`)

---
### SetHudComponentPosition

`SET_HUD_COMPONENT_POSITION` · hash `0xAABB1F56E2A17CED` · jhash `0x2F3A0D15` · **Cliente**

```lua
SetHudComponentPosition(id, x, y)
```
```c
void SET_HUD_COMPONENT_POSITION(int id, float x, float y);
```

**Parámetros**

- `id` (`int`)
- `x` (`float`)
- `y` (`float`)

**Devuelve:** `void`

---
### SetInteriorZoomLevelDecreased

`_SET_INTERIOR_ZOOM_LEVEL_DECREASED` · hash `0x7EC8ABA5E74B3D7A` · **Cliente**

```lua
SetInteriorZoomLevelDecreased(toggle)
```
```c
void _SET_INTERIOR_ZOOM_LEVEL_DECREASED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x7EC8ABA5E74B3D7A` (`N_0x7ec8aba5e74b3d7a`)

---
### SetInteriorZoomLevelIncreased

`_SET_INTERIOR_ZOOM_LEVEL_INCREASED` · hash `0x504DFE62A1692296` · **Cliente**

```lua
SetInteriorZoomLevelIncreased(toggle)
```
```c
void _SET_INTERIOR_ZOOM_LEVEL_INCREASED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x504DFE62A1692296` (`N_0x504dfe62a1692296`)

---
### SetMainPlayerBlipColour

`_SET_MAIN_PLAYER_BLIP_COLOUR` · hash `0x7B21E0BB01E8224A` · **Cliente**

```lua
SetMainPlayerBlipColour(color)
```
```c
void _SET_MAIN_PLAYER_BLIP_COLOUR(int color);
```

**Parámetros**

- `color` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7B21E0BB01E8224A` (`N_0x7b21e0bb01e8224a`)

---
### SetMaxArmourHudDisplay

`SET_MAX_ARMOUR_HUD_DISPLAY` · hash `0x06A320535F5F0248` · jhash `0x827F14DE` · **Cliente**

```lua
SetMaxArmourHudDisplay(maximumValue)
```
```c
void SET_MAX_ARMOUR_HUD_DISPLAY(int maximumValue);
```

**Parámetros**

- `maximumValue` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x06A320535F5F0248` (`N_0x06a320535f5f0248`)

---
### SetMaxHealthHudDisplay

`SET_MAX_HEALTH_HUD_DISPLAY` · hash `0x975D66A0BC17064C` · jhash `0xF07D8CEF` · **Cliente**

```lua
SetMaxHealthHudDisplay(maximumValue)
```
```c
void SET_MAX_HEALTH_HUD_DISPLAY(int maximumValue);
```

**Parámetros**

- `maximumValue` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x975D66A0BC17064C` (`N_0x975d66a0bc17064c`)

---
### SetMinimapAltitudeIndicatorLevel

`_SET_MINIMAP_ALTITUDE_INDICATOR_LEVEL` · hash `0xD201F3FF917A506D` · jhash `0x0308EDF6` · **Cliente**

```lua
SetMinimapAltitudeIndicatorLevel(altitude, p1)
```
```c
void _SET_MINIMAP_ALTITUDE_INDICATOR_LEVEL(float altitude, BOOL p1);
```

**Parámetros**

- `altitude` (`float`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Argument must be 0.0f or above 38.0f, or it will be ignored.  
```

```
NativeDB Added Parameter 3: Any p2
```

**Nombres antiguos (alias):** `_SET_MINIMAP_ATTITUDE_INDICATOR_LEVEL` (`SetMinimapAttitudeIndicatorLevel`)

---
### SetMinimapBlockWaypoint

`SET_MINIMAP_BLOCK_WAYPOINT` · hash `0x58FADDED207897DC` · jhash `0xA41C3B62` · **Cliente**

```lua
SetMinimapBlockWaypoint(toggle)
```
```c
void SET_MINIMAP_BLOCK_WAYPOINT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetMinimapComponent

`SET_MINIMAP_COMPONENT` · hash `0x75A9A10948D1DEA6` · jhash `0x419DCDC4` · **Cliente**

```lua
local retval = SetMinimapComponent(componentID, toggle, hudColor)
```
```c
int SET_MINIMAP_COMPONENT(int componentID, BOOL toggle, int hudColor);
```

**Parámetros**

- `componentID` (`int`): The component ID to change.
- `toggle` (`BOOL`): True to enable/colorize, false to disable.
- `hudColor` (`int`): The hudcolor index, the list of hud colors can be found [here](https://docs.fivem.net/docs/game-references/hud-colors/).

**Devuelve:** `int` — Hardcoded to always return 1 (int)

**Descripción oficial:**

This native is used to colorize/toggle certain map components like the army base.

Component IDs 6 through 14 are used by the freemode event King of the Castle in GTA Online.

**An incomplete list of component IDs:**

*   **0**: Los Santos International Airport yellow runway markers
*   **1**: Sandy Shores Airfield yellow runway markers
*   **2**: McKenzie Field yellow runway markers
*   **6**: Vespucci Beach lifeguard building
*   **7**: Top level zone of Alien Camp (Hippy Camp)
*   **8**: Paleto Bay fire station drill tower
*   **9** Land Act Dam tower
*   **10** Pala Springs Aerial Tramway
*   **11** Galileo Observatory power unit
*   **12** Small zone (empty "interior") near Central Los Santos Medical Center
*   **13** Richman Mansion grotto
*   **14** 2 Alien Camp (Hippy Camp) circles
*   **15** Fort Zancudo

**Ejemplo (lua):**

```lua
-- Enables Fort Zancudo on the map
SetMinimapComponent(15, true, 0)
```

---
### SetMinimapFowRevealCoordinate

`SET_MINIMAP_FOW_REVEAL_COORDINATE` · hash `0x0923DBF87DFF735E` · jhash `0xE010F081` · **Cliente**

```lua
SetMinimapFowRevealCoordinate(x, y, z)
```
```c
void SET_MINIMAP_FOW_REVEAL_COORDINATE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0923DBF87DFF735E` (`N_0x0923dbf87dff735e`)

---
### SetMinimapGolfCourse

`SET_MINIMAP_GOLF_COURSE` · hash `0x71BDB63DBAF8DA59` · jhash `0x5133A750` · **Cliente**

```lua
SetMinimapGolfCourse(hole)
```
```c
void SET_MINIMAP_GOLF_COURSE(int hole);
```

**Parámetros**

- `hole` (`int`): The ID of the hole to draw on the map. ID starts with 1 for hole 1, 2 for hole 2, etc. 0 disables the golf map behaviour.

**Devuelve:** `void`

**Descripción oficial:**

Not much is known so far on what it does *exactly*.
All I know for sure is that it draws the specified hole ID on the pause menu map as well as on the mini-map/radar. This native also seems to change some other things related to the pause menu map's behaviour, for example: you can no longer set waypoints, the pause menu map starts up in a 'zoomed in' state. This native does not need to be executed every tick.

You need to center the minimap manually as well as change/lock it's zoom and angle in order for it to appear correctly on the minimap.
You'll also need to use the `GOLF` scaleform in order to get the correct minmap border to show up.

Use [`SET_MINIMAP_GOLF_COURSE_OFF()`](#setminimapgolfcourseoff) to reset the map when you no longer want to display any golf holes (you still need to unlock zoom, position and angle of the radar manually after calling this).

**Nombres antiguos (alias):** `0x71BDB63DBAF8DA59` (`N_0x71bdb63dbaf8da59`)

**Ejemplo (cs):**

```cs
// draw hole 2
SetMinimapGolfCourse(2);

// set the other minimap properties for this specific hole:
SetRadarZoom(850);
LockMinimapPosition(-1220.0f, 240.0f);
LockMinimapAngle(90);
ToggleStealthRadar(false);
SetRadarBigmapEnabled(false, false);

// Create the flag blip and set the sprite to the flag sprite.
int blip = AddBlipForCoord(-1321.98f, 158.93f, 57.8f);
SetBlipSprite(blip, 358);
```

---
### SetMinimapGolfCourseOff

`SET_MINIMAP_GOLF_COURSE_OFF` · hash `0x35EDD5B2E3FF01C0` · jhash `0x20FD3E87` · **Cliente**

```lua
SetMinimapGolfCourseOff()
```
```c
void SET_MINIMAP_GOLF_COURSE_OFF();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x35EDD5B2E3FF01C0` (`N_0x35edd5b2e3ff01c0`)

---
### SetMinimapHideFow

`SET_MINIMAP_HIDE_FOW` · hash `0xF8DEE0A5600CBB93` · jhash `0xD8D77733` · **Cliente**

```lua
SetMinimapHideFow(toggle)
```
```c
void SET_MINIMAP_HIDE_FOW(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If true, the entire map will be revealed.
```

**Nombres antiguos (alias):** `0xF8DEE0A5600CBB93` (`N_0xf8dee0a5600cbb93`), `_SET_MINIMAP_REVEALED` (`SetMinimapRevealed`)

---
### SetMinimapInPrologue

`SET_MINIMAP_IN_PROLOGUE` · hash `0x9133955F1A2DA957` · jhash `0x02F5F1D1` · **Cliente**

```lua
SetMinimapInPrologue(toggle)
```
```c
void SET_MINIMAP_IN_PROLOGUE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles the North Yankton map
```

**Nombres antiguos (alias):** `_SET_DRAW_MAP_VISIBLE` (`SetDrawMapVisible`), `_SET_NORTH_YANKTON_MAP` (`SetNorthYanktonMap`)

---
### SetMinimapInSpectatorMode

`SET_MINIMAP_IN_SPECTATOR_MODE` · hash `0x1A5CD7752DD28CD3` · jhash `0xD5BFCADB` · **Cliente**

```lua
SetMinimapInSpectatorMode(toggle, ped)
```
```c
void SET_MINIMAP_IN_SPECTATOR_MODE(BOOL toggle, Ped ped);
```

**Parámetros**

- `toggle` (`BOOL`)
- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `KEY_HUD_COLOUR` (`KeyHudColour`)

---
### SetMinimapSonarSweep

`SET_MINIMAP_SONAR_SWEEP` · hash `0x6B50FC8749632EC1` · **Cliente**

```lua
SetMinimapSonarSweep(toggle)
```
```c
void SET_MINIMAP_SONAR_SWEEP(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): A boolean value where `true` activates the sonar sweep animation on the minimap, and `false` turns it off.

**Devuelve:** `void` — This native does not return any value.

**Descripción oficial:**

Enables or disables the sonar sweep animation on the minimap.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `_SET_MINIMAP_SONAR_ENABLED` (`SetMinimapSonarEnabled`)

---
### SetMissionName

`SET_MISSION_NAME` · hash `0x5F28ECF5FC84772F` · jhash `0x68DCAE10` · **Cliente**

```lua
SetMissionName(p0, name)
```
```c
void SET_MISSION_NAME(BOOL p0, char* name);
```

**Parámetros**

- `p0` (`BOOL`)
- `name` (`char*`)

**Devuelve:** `void`

---
### SetMissionName_2

`_SET_MISSION_NAME_2` · hash `0xE45087D85F468BC2` · jhash `0x8D9A1734` · **Cliente**

```lua
SetMissionName_2(p0, name)
```
```c
void _SET_MISSION_NAME_2(BOOL p0, char* name);
```

**Parámetros**

- `p0` (`BOOL`)
- `name` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE45087D85F468BC2` (`N_0xe45087d85f468bc2`)

---
### SetMouseCursorStyle

`SET_MOUSE_CURSOR_STYLE` · hash `0x8DB8CFFD58B62552` · **Cliente**

```lua
SetMouseCursorStyle(style)
```
```c
void SET_MOUSE_CURSOR_STYLE(int style);
```

**Parámetros**

- `style` (`int`): Which sprite to change to, see declared enum `eMousePointerStyle`.

**Devuelve:** `void`

**Descripción oficial:**

Changes the mouse style.

```cpp
enum eMousePointerStyle {
	ARROW = 1,
	ARROW_DIMMED = 2,
	HAND_OPEN = 3,
	HAND_GRAB = 4,
	HAND_MIDDLE_FINGER = 5,
	ARROW_LEFT = 6,
	ARROW_RIGHT = 7,
	ARROW_UP = 8,
	ARROW_DOWN = 9,
	ARROW_TRIMMING = 10,
	ARROW_PLUS = 11,
	ARROW_MINUS = 12
};
```

**Nombres antiguos (alias):** `0x8DB8CFFD58B62552` (`N_0x8db8cffd58b62552`), `_SET_CURSOR_SPRITE` (`SetCursorSprite`), `_SET_MOUSE_CURSOR_SPRITE` (`SetMouseCursorSprite`)

---
### SetMouseCursorThisFrame

`SET_MOUSE_CURSOR_THIS_FRAME` · hash `0xAAE7CE1D63167423` · **Cliente**

```lua
SetMouseCursorThisFrame()
```
```c
void SET_MOUSE_CURSOR_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Sets the mouse pointer to be active on current frame.

**Nombres antiguos (alias):** `_SHOW_CURSOR_THIS_FRAME` (`ShowCursorThisFrame`), `_SET_MOUSE_CURSOR_ACTIVE_THIS_FRAME` (`SetMouseCursorActiveThisFrame`)

**Ejemplo (lua):**

```lua
CreateThread(function()
  while true do
    Wait(0)
    SetMouseCursorThisFrame()
  end
end)
```

---
### SetMouseCursorVisible

`SET_MOUSE_CURSOR_VISIBLE` · hash `0x98215325A695E78A` · **Cliente**

```lua
SetMouseCursorVisible(isVisible)
```
```c
void SET_MOUSE_CURSOR_VISIBLE(BOOL isVisible);
```

**Parámetros**

- `isVisible` (`BOOL`): If the mouse cursor is visible

**Devuelve:** `void`

**Descripción oficial:**

Toggles the visibility of the cursor. Do note that if the game loses focus and then regains it, the cursor will become visible again.

**Nombres antiguos (alias):** `0x98215325A695E78A` (`N_0x98215325a695e78a`), `_SET_MOUSE_CURSOR_VISIBLE_IN_MENUS` (`SetMouseCursorVisibleInMenus`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    local menuType = "FE_MENU_VERSION_CORONA_LOBBY"
    ActivateFrontendMenu(GetHashKey(menuType), false, -1)
    --100 works as well
    Citizen.Wait(1000)
    --Hide frontend cursor
    SetMouseCursorVisible(false)
end)
```

---
### SetMpGamerTagAlpha

`SET_MP_GAMER_TAG_ALPHA` · hash `0xD48FE545CD46F857` · jhash `0xF4418611` · **Cliente**

```lua
SetMpGamerTagAlpha(gamerTagId, component, alpha)
```
```c
void SET_MP_GAMER_TAG_ALPHA(int gamerTagId, int component, int alpha);
```

**Parámetros**

- `gamerTagId` (`int`)
- `component` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets flag's sprite transparency. 0-255.  
```

**Nombres antiguos (alias):** `0xD48FE545CD46F857` (`N_0xd48fe545cd46f857`)

---
### SetMpGamerTagBigText

`SET_MP_GAMER_TAG_BIG_TEXT` · hash `0x7B7723747CCB55B6` · jhash `0x939218AB` · **Cliente**

```lua
SetMpGamerTagBigText(gamerTagId, string)
```
```c
void SET_MP_GAMER_TAG_BIG_TEXT(int gamerTagId, char* string);
```

**Parámetros**

- `gamerTagId` (`int`)
- `string` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7B7723747CCB55B6` (`N_0x7b7723747ccb55b6`), `_SET_MP_GAMER_TAG_CHATTING` (`SetMpGamerTagChatting`)

---
### SetMpGamerTagColour

`SET_MP_GAMER_TAG_COLOUR` · hash `0x613ED644950626AE` · jhash `0x7E3AA40A` · **Cliente**

```lua
SetMpGamerTagColour(gamerTagId, component, hudColorIndex)
```
```c
void SET_MP_GAMER_TAG_COLOUR(int gamerTagId, int component, int hudColorIndex);
```

**Parámetros**

- `gamerTagId` (`int`): a gamerTagId obtained using  for example: [`CREATE_FAKE_MP_GAMER_TAG`](#createfakempgamertag).
- `component` (`int`): a component id, see the full list here: [link](https://docs.fivem.net/docs/game-references/gamer-tags/#components-list)
- `hudColorIndex` (`int`): a hud color index, see the full list here: [link](https://docs.fivem.net/docs/game-references/hud-colors/)

**Devuelve:** `void`

**Descripción oficial:**

Sets a gamer tag's component colour

**Nombres antiguos (alias):** `0x613ED644950626AE` (`N_0x613ed644950626ae`)

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId() --get our players ped
local playerName = GetPlayerName(PlayerId()) --get our players name
local gamerTagId = CreateFakeMpGamerTag(playerPed, playerName, 0, 0, "", 0) --create a gamer tag
SetMpGamerTagColour(gamerTagId, 0, 129) --set component 0(GAMER_NAME) color to 129(HUD_COLOUR_YOGA)
```

**Ejemplo (cs):**

```cs
Player player = Game.Player; //get our player
int gamerTagId = CreateFakeMpGamerTag(player.Character.Handle, player.Name, false, false, null, 0); //create a gamer tag
SetMpGamerTagColour(gamerTagId, 0, 129); //set component 0(GAMER_NAME) color to 129(HUD_COLOUR_YOGA)
```

---
### SetMpGamerTagDisablePlayerHealthSync

`_SET_MP_GAMER_TAG_DISABLE_PLAYER_HEALTH_SYNC` · hash `0xD29EC58C2F6B5014` · **Cliente**

```lua
SetMpGamerTagDisablePlayerHealthSync(gamerTagId, toggle)
```
```c
void _SET_MP_GAMER_TAG_DISABLE_PLAYER_HEALTH_SYNC(int gamerTagId, BOOL toggle);
```

**Parámetros**

- `gamerTagId` (`int`)
- `toggle` (`BOOL`): If player health synchronisation should be disabled.

**Devuelve:** `void`

**Descripción oficial:**

By default, the player health value shown by a gamer tag's health bar is synchronised with the health of the ped it is attached to.
This native disables that behaviour, allowing [`_SET_MP_GAMER_TAG_OVERRIDE_PLAYER_HEALTH`](#setmpgamertagoverrideplayerhealth) to have an effect.

**Nombres antiguos (alias):** `0xD29EC58C2F6B5014` (`N_0xd29ec58c2f6b5014`), `_SET_MP_GAMER_HEALTH_BAR_DISPLAY` (`SetMpGamerHealthBarDisplay`)

---
### SetMpGamerTagHealthBarColour

`SET_MP_GAMER_TAG_HEALTH_BAR_COLOUR` · hash `0x3158C77A7E888AB4` · jhash `0x5777EC77` · **Cliente**

```lua
SetMpGamerTagHealthBarColour(gamerTagId, hudColorIndex)
```
```c
void SET_MP_GAMER_TAG_HEALTH_BAR_COLOUR(int gamerTagId, int hudColorIndex);
```

**Parámetros**

- `gamerTagId` (`int`): a gamerTagId obtained using  for example: [CREATE_FAKE_MP_GAMER_TAG](#createfakempgamertag)
- `hudColorIndex` (`int`): a hud color index, see the full list here: [link](https://docs.fivem.net/docs/game-references/hud-colors/)

**Devuelve:** `void`

**Descripción oficial:**

Should be enabled as component (2). Has 0 alpha by default.

**Nombres antiguos (alias):** `0x3158C77A7E888AB4` (`N_0x3158c77a7e888ab4`), `_SET_MP_GAMER_TAG_HEALTH_BAR_COLOR` (`SetMpGamerTagHealthBarColor`)

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId() --get our players ped
local playerName = GetPlayerName(PlayerId()) --get our players name
local gamerTagId = CreateFakeMpGamerTag(playerPed, playerName, 0, 0, "", 0) --create a gamer tag
SetMpGamerTagVisibility(gamerTagId, 2, 1)  --set the visibility of component 2(healthArmour) to true
SetMpGamerTagAlpha(gamerTagId, 2, 255) --set the alpha of component 2(healthArmour) to 255
SetMpGamerTagHealthBarColor(gamerTagId, 129) --set component 2(healthArmour) color to 129(HUD_COLOUR_YOGA)
```

**Ejemplo (cs):**

```cs
Player player = Game.Player; //get our player
int gamerTagId = CreateFakeMpGamerTag(player.Character.Handle, player.Name, false, false, null, 0); //create a gamer tag
SetMpGamerTagVisibility(gamerTagId, 2, true); //set the visibility of component 2(healthArmour) to true
SetMpGamerTagAlpha(gamerTagId, 2, 255); //set the alpha of component 2(healthArmour) to 255
SetMpGamerTagHealthBarColor(gamerTagId, 129); //set component 2(healthArmour) color to 129(HUD_COLOUR_YOGA)
```

---
### SetMpGamerTagMpBagLargeCount

`_SET_MP_GAMER_TAG_MP_BAG_LARGE_COUNT` · hash `0x9C16459B2324B2CF` · **Cliente**

```lua
SetMpGamerTagMpBagLargeCount(gamerTagId, count)
```
```c
void _SET_MP_GAMER_TAG_MP_BAG_LARGE_COUNT(int gamerTagId, int count);
```

**Parámetros**

- `gamerTagId` (`int`)
- `count` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
displays wanted star above head  
```

**Nombres antiguos (alias):** `0x9B9AA95688F78DD3` (`N_0x9b9aa95688f78dd3`), `_SET_MP_GAMER_TAG_UNK` (`SetMpGamerTagUnk`)

---
### SetMpGamerTagName

`SET_MP_GAMER_TAG_NAME` · hash `0xDEA2B8283BAA3944` · jhash `0x627A559B` · **Cliente**

```lua
SetMpGamerTagName(gamerTagId, string)
```
```c
void SET_MP_GAMER_TAG_NAME(int gamerTagId, char* string);
```

**Parámetros**

- `gamerTagId` (`int`)
- `string` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDEA2B8283BAA3944` (`N_0xdea2b8283baa3944`)

---
### SetMpGamerTagOverridePlayerHealth

`_SET_MP_GAMER_TAG_OVERRIDE_PLAYER_HEALTH` · hash `0x1563FE35E9928E67` · **Cliente**

```lua
SetMpGamerTagOverridePlayerHealth(gamerTagId, health, maximumHealth)
```
```c
void _SET_MP_GAMER_TAG_OVERRIDE_PLAYER_HEALTH(int gamerTagId, int health, int maximumHealth);
```

**Parámetros**

- `gamerTagId` (`int`)
- `health` (`int`): The amount the health the player has.
- `maximumHealth` (`int`): The maximum amount of health the player could have.

**Devuelve:** `void`

**Descripción oficial:**

Manually sets the player health value for a gamer tag, using the maximum health to calculate what percentage of the bar should be filled.
Has no effect unless [\_SET_MP_GAMER_TAG_DISABLE_PLAYER_HEALTH_SYNC](#setmpgamertagdisableplayerhealthsync) has been called prior to disable synchronisation with the attached ped.

**Nombres antiguos (alias):** `0x1563FE35E9928E67` (`N_0x1563fe35e9928e67`), `_SET_MP_GAMER_HEALTH_BAR_MAX` (`SetMpGamerHealthBarMax`)

---
### SetMpGamerTagUseVehicleHealth

`_SET_MP_GAMER_TAG_USE_VEHICLE_HEALTH` · hash `0xA67F9C46D612B6F1` · jhash `0xB01A5434` · **Cliente**

```lua
SetMpGamerTagUseVehicleHealth(gamerTagId, toggle)
```
```c
void _SET_MP_GAMER_TAG_USE_VEHICLE_HEALTH(int gamerTagId, BOOL toggle);
```

**Parámetros**

- `gamerTagId` (`int`)
- `toggle` (`BOOL`): If vehicle health should be displayed instead of player health.

**Devuelve:** `void`

**Descripción oficial:**

Sets the health bar of a gamer tag to show the health of the last (or current) vehicle of the ped the gamer tag is attached to.
The vehicle health value is stored separate from the player health and using it won't clear any player health overrides.

**Nombres antiguos (alias):** `0xA67F9C46D612B6F1` (`N_0xa67f9c46d612b6f1`), `_SET_MP_GAMER_TAG_ICONS` (`SetMpGamerTagIcons`)

---
### SetMpGamerTagVisibility

`SET_MP_GAMER_TAG_VISIBILITY` · hash `0x63BB75ABEDC1F6A0` · jhash `0xD41DF479` · **Cliente**

```lua
SetMpGamerTagVisibility(gamerTagId, component, toggle)
```
```c
void SET_MP_GAMER_TAG_VISIBILITY(int gamerTagId, int component, BOOL toggle);
```

**Parámetros**

- `gamerTagId` (`int`)
- `component` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eMpGamerTagComponent
{
	MP_TAG_GAMER_NAME = 0,
	MP_TAG_CREW_TAG = 1,
	MP_TAG_HEALTH_ARMOUR = 2,
	MP_TAG_BIG_TEXT = 3,
	MP_TAG_AUDIO_ICON = 4,
	MP_TAG_USING_MENU = 5,
	MP_TAG_PASSIVE_MODE = 6,
	MP_TAG_WANTED_STARS = 7,
	MP_TAG_DRIVER = 8,
	MP_TAG_CO_DRIVER = 9,
	MP_TAG_TAGGED = 10,
	MP_TAG_GAMER_NAME_NEARBY = 11,
	MP_TAG_ARROW = 12,
	MP_TAG_PACKAGES = 13,
	MP_TAG_INV_IF_PED_FOLLOWING = 14,
	MP_TAG_RANK_TEXT = 15,
	MP_TAG_TYPING = 16,
	MP_TAG_BAG_LARGE = 17,
	MP_TAG_ARROW = 18,
	MP_TAG_GANG_CEO = 19,
	MP_TAG_GANG_BIKER = 20,
	MP_TAG_BIKER_ARROW = 21,
	MP_TAG_MC_ROLE_PRESIDENT = 22,
	MP_TAG_MC_ROLE_VICE_PRESIDENT = 23,
	MP_TAG_MC_ROLE_ROAD_CAPTAIN = 24,
	MP_TAG_MC_ROLE_SARGEANT = 25,
	MP_TAG_MC_ROLE_ENFORCER = 26,
	MP_TAG_MC_ROLE_PROSPECT = 27,
	MP_TAG_TRANSMITTER = 28,
	MP_TAG_BOMB = 29
};
```

```
NativeDB Added Parameter 4: Any p3
```

**Nombres antiguos (alias):** `0x63BB75ABEDC1F6A0` (`N_0x63bb75abedc1f6a0`)

---
### SetMpGamerTagVisibilityAll

`_SET_MP_GAMER_TAG_VISIBILITY_ALL` · hash `0xEE76FF7E6A0166B0` · jhash `0x767DED29` · **Cliente**

```lua
SetMpGamerTagVisibilityAll(gamerTagId, toggle)
```
```c
void _SET_MP_GAMER_TAG_VISIBILITY_ALL(int gamerTagId, BOOL toggle);
```

**Parámetros**

- `gamerTagId` (`int`)
- `toggle` (`BOOL`): The new visibility state of all gamer tag components.

**Devuelve:** `void`

**Descripción oficial:**

Sets the visibility of all components of the gamer tag to the specified value.

**Nombres antiguos (alias):** `0xEE76FF7E6A0166B0` (`N_0xee76ff7e6a0166b0`), `_SET_MP_GAMER_TAG_` (`SetMpGamerTag_`), `_SET_MP_GAMER_TAG` (`SetMpGamerTag`), `_SET_MP_GAMER_TAG_ENABLED` (`SetMpGamerTagEnabled`)

---
### SetMpGamerTagWantedLevel

`SET_MP_GAMER_TAG_WANTED_LEVEL` · hash `0xCF228E2AA03099C3` · jhash `0x0EBB003F` · **Cliente**

```lua
SetMpGamerTagWantedLevel(gamerTagId, wantedlvl)
```
```c
void SET_MP_GAMER_TAG_WANTED_LEVEL(int gamerTagId, int wantedlvl);
```

**Parámetros**

- `gamerTagId` (`int`)
- `wantedlvl` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
displays wanted star above head  
```

**Nombres antiguos (alias):** `0xCF228E2AA03099C3` (`N_0xcf228e2aa03099c3`)

---
### SetMultiplayerBankCash

`SET_MULTIPLAYER_BANK_CASH` · hash `0xDD21B55DF695CD0A` · jhash `0x2C842D03` · **Cliente**

```lua
SetMultiplayerBankCash()
```
```c
void SET_MULTIPLAYER_BANK_CASH();
```

**Devuelve:** `void`

**Descripción oficial:**

Preview:

![](https://i.imgur.com/b7lU2nl.png)

To change the bank balance use [`STAT_SET_INT`](STATS.md#statsetint) with "BANK_BALANCE" to whatever value you need to.

**Ejemplo (cs):**

```cs
// Code to show both Money and Bank HUD
N_0x170f541e1cadd1de(true);
SetMultiplayerWalletCash();
SetMultiplayerBankCash();
N_0x170f541e1cadd1de(false);

// Add a delay to let the player read his money
await Delay(5000);

// Hide both Bank and Money HUD
RemoveMultiplayerWalletCash();
RemoveMultiplayerBankCash();
```

---
### SetMultiplayerHudCash

`SET_MULTIPLAYER_HUD_CASH` · hash `0xFD1D220394BCB824` · jhash `0xA8DB435E` · **Cliente**

```lua
SetMultiplayerHudCash(p0, p1)
```
```c
void SET_MULTIPLAYER_HUD_CASH(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### SetMultiplayerWalletCash

`SET_MULTIPLAYER_WALLET_CASH` · hash `0xC2D15BEF167E27BC` · jhash `0xF4F3C796` · **Cliente**

```lua
SetMultiplayerWalletCash()
```
```c
void SET_MULTIPLAYER_WALLET_CASH();
```

**Devuelve:** `void`

**Descripción oficial:**

Preview:

![](https://i.imgur.com/b7lU2nl.png)

To change money value use [`STAT_SET_INT`](STATS.md#statsetint) with "MP0\_WALLET_BALANCE" to whatever value you need to.

**Nombres antiguos (alias):** `0xC2D15BEF167E27BC` (`N_0xc2d15bef167e27bc`)

**Ejemplo (cs):**

```cs
// Code to show both Money and Bank HUD
N_0x170f541e1cadd1de(true);
SetMultiplayerWalletCash();
SetMultiplayerBankCash();
N_0x170f541e1cadd1de(false);

// Add a delay to let the player read his money
await Delay(5000);

// Hide both Bank and Money HUD
RemoveMultiplayerWalletCash();
RemoveMultiplayerBankCash();
```

---
### SetNewWaypoint

`SET_NEW_WAYPOINT` · hash `0xFE43368D2AA4F2FC` · jhash `0x8444E1F0` · **Cliente**

```lua
SetNewWaypoint(x, y)
```
```c
void SET_NEW_WAYPOINT(float x, float y);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)

**Devuelve:** `void`

---
### SetPauseMenuActive

`SET_PAUSE_MENU_ACTIVE` · hash `0xDF47FC56C71569CF` · jhash `0x1DCD878E` · **Cliente**

```lua
SetPauseMenuActive(toggle)
```
```c
void SET_PAUSE_MENU_ACTIVE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This native is deprecated.

If you're looking to:

*   Toggle the pause menu on, use [`ACTIVATE_FRONTEND_MENU`](#activatefrontendmenu)
*   Toggle the pause menu off, use [`SET_FRONTEND_ACTIVE`](#setfrontendactive)
*   Disable toggling the pause menu, use [`DISABLE_FRONTEND_THIS_FRAME`](#disablefrontendthisframe)

---
### SetPauseMenuPedLighting

`SET_PAUSE_MENU_PED_LIGHTING` · hash `0x3CA6050692BC61B0` · jhash `0x127310EB` · **Cliente**

```lua
SetPauseMenuPedLighting(state)
```
```c
void SET_PAUSE_MENU_PED_LIGHTING(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): True enables the light, false disables the light.

**Devuelve:** `void`

**Descripción oficial:**

Toggles the light state for the pause menu ped in frontend menus.

This is used by R\* in combination with [`SET_PAUSE_MENU_PED_SLEEP_STATE`](#setpausemenupedsleepstate) to toggle the "offline" or "online" state in the "friends" tab of the pause menu in GTA Online.

Example:
On: ![lights on](https://vespura.com/hi/i/2019-04-01\_16-09\_540ee\_1015.png)
Off: ![lights off](https://vespura.com/hi/i/2019-04-01\_16-10\_8b5e7\_1016.png)

**Nombres antiguos (alias):** `0x3CA6050692BC61B0` (`N_0x3ca6050692bc61b0`)

---
### SetPauseMenuPedSleepState

`SET_PAUSE_MENU_PED_SLEEP_STATE` · hash `0xECF128344E9FF9F1` · jhash `0x8F45D327` · **Cliente**

```lua
SetPauseMenuPedSleepState(state)
```
```c
void SET_PAUSE_MENU_PED_SLEEP_STATE(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): 0 will make the ped slowly fall asleep, 1 will slowly wake the ped up.

**Devuelve:** `void`

**Descripción oficial:**

Toggles the pause menu ped sleep state for frontend menus.

[Example GIF](https://vespura.com/hi/i/2019-04-01\_15-51\_8ed38\_1014.gif)

**Nombres antiguos (alias):** `0xECF128344E9FF9F1` (`N_0xecf128344e9ff9f1`)

---
### SetPedAiBlipForcedOn

`SET_PED_AI_BLIP_FORCED_ON` · hash `0x0C4BBF625CA98C4E` · jhash `0xFFDF46F0` · **Cliente**

```lua
SetPedAiBlipForcedOn(ped, toggle)
```
```c
void SET_PED_AI_BLIP_FORCED_ON(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
if "flag" is true, the AI blip will always be displayed for the specified ped, if it has an AI blip  
If "flag" is false, the AI blip will only be displayed when the player is in combat with the specified ped, if it has an AI blip  
```

**Nombres antiguos (alias):** `0x0C4BBF625CA98C4E` (`N_0x0c4bbf625ca98c4e`), `_IS_AI_BLIP_ALWAYS_SHOWN` (`IsAiBlipAlwaysShown`)

---
### SetPedAiBlipGangId

`SET_PED_AI_BLIP_GANG_ID` · hash `0xE52B8E7F85D39A08` · jhash `0xD8E31B1A` · **Cliente**

```lua
SetPedAiBlipGangId(ped, gangId)
```
```c
void SET_PED_AI_BLIP_GANG_ID(Ped ped, int gangId);
```

**Parámetros**

- `ped` (`Ped`)
- `gangId` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE52B8E7F85D39A08` (`N_0xe52b8e7f85d39a08`), `_SET_AI_BLIP_TYPE` (`SetAiBlipType`)

---
### SetPedAiBlipHasCone

`SET_PED_AI_BLIP_HAS_CONE` · hash `0x3EED80DFF7325CAA` · jhash `0x872C2CFB` · **Cliente**

```lua
SetPedAiBlipHasCone(ped, toggle)
```
```c
void SET_PED_AI_BLIP_HAS_CONE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `HIDE_SPECIAL_ABILITY_LOCKON_OPERATION` (`HideSpecialAbilityLockonOperation`)

---
### SetPedAiBlipNoticeRange

`SET_PED_AI_BLIP_NOTICE_RANGE` · hash `0x97C65887D4B37FA9` · jhash `0xF9DC2AF7` · **Cliente**

```lua
SetPedAiBlipNoticeRange(ped, range)
```
```c
void SET_PED_AI_BLIP_NOTICE_RANGE(Ped ped, float range);
```

**Parámetros**

- `ped` (`Ped`)
- `range` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x97C65887D4B37FA9` (`N_0x97c65887d4b37fa9`), `_SET_AI_BLIP_MAX_DISTANCE` (`SetAiBlipMaxDistance`)

---
### SetPedAiBlipSprite

`_SET_PED_AI_BLIP_SPRITE` · hash `0xFCFACD0DB9D7A57D` · **Cliente**

```lua
SetPedAiBlipSprite(ped, spriteId)
```
```c
void _SET_PED_AI_BLIP_SPRITE(Ped ped, int spriteId);
```

**Parámetros**

- `ped` (`Ped`)
- `spriteId` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFCFACD0DB9D7A57D` (`N_0xfcfacd0db9d7a57d`)

---
### SetPedHasAiBlip

`SET_PED_HAS_AI_BLIP` · hash `0xD30C50DF888D58B5` · jhash `0x96C4C4DD` · **Cliente**

```lua
SetPedHasAiBlip(ped, hasCone)
```
```c
void SET_PED_HAS_AI_BLIP(Ped ped, BOOL hasCone);
```

**Parámetros**

- `ped` (`Ped`)
- `hasCone` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native turns on the AI blip on the specified ped. It also disappears automatically when the ped is too far or if the ped is dead. You don't need to control it with other natives.
See gtaforums.com/topic/884370-native-research-ai-blips for further information.
```

**Nombres antiguos (alias):** `0xD30C50DF888D58B5` (`N_0xd30c50df888d58b5`), `_SET_PED_ENEMY_AI_BLIP` (`SetPedEnemyAiBlip`), `_SET_PED_AI_BLIP` (`SetPedAiBlip`)

---
### SetPedHasAiBlipWithColor

`_SET_PED_HAS_AI_BLIP_WITH_COLOR` · hash `0xB13DCB4C6FAAD238` · **Cliente**

```lua
SetPedHasAiBlipWithColor(ped, hasCone, color)
```
```c
void _SET_PED_HAS_AI_BLIP_WITH_COLOR(Ped ped, BOOL hasCone, int color);
```

**Parámetros**

- `ped` (`Ped`)
- `hasCone` (`BOOL`)
- `color` (`int`): See [`SET_BLIP_COLOUR`](#setblipcolour).

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB13DCB4C6FAAD238` (`N_0xb13dcb4c6faad238`)

---
### SetPlayerIsInDirectorMode

`_SET_PLAYER_IS_IN_DIRECTOR_MODE` · hash `0x808519373FD336A3` · **Cliente**

```lua
SetPlayerIsInDirectorMode(toggle)
```
```c
void _SET_PLAYER_IS_IN_DIRECTOR_MODE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If toggle is true, hides special ability bar / character name in the pause menu
If toggle is false, shows special ability bar / character name in the pause menu
SET_PLAYER_*
```

**Nombres antiguos (alias):** `0x808519373FD336A3` (`N_0x808519373fd336a3`), `_SET_DIRECTOR_MODE` (`SetDirectorMode`)

---
### SetPmWarningscreenActive

`SET_PM_WARNINGSCREEN_ACTIVE` · hash `0x41350B4FC28E3941` · **Cliente**

```lua
SetPmWarningscreenActive(isActive)
```
```c
void SET_PM_WARNINGSCREEN_ACTIVE(BOOL isActive);
```

**Parámetros**

- `isActive` (`BOOL`): Lets the game code know that a pause menu warning message is active.

**Devuelve:** `void`

**Descripción oficial:**

Doesn't seem to change anything visual and input-wise. Scripts use this in conjuction with the [`SHOW_WARNING_MESSAGE`](GRAPHICS.md#beginscaleformmoviemethodonfrontend) scaleform function.
Example of a "Pause Menu Warning Screen":
![](https://imgur.com/a/LJERmPC)

**Nombres antiguos (alias):** `0x41350B4FC28E3941` (`N_0x41350b4fc28e3941`)

---
### SetRaceTrackRender

`SET_RACE_TRACK_RENDER` · hash `0x1EAC5F91BCBC5073` · jhash `0xFB9BABF5` · **Cliente**

```lua
SetRaceTrackRender(toggle)
```
```c
void SET_RACE_TRACK_RENDER(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1EAC5F91BCBC5073` (`N_0x1eac5f91bcbc5073`)

---
### SetRadarAsExteriorThisFrame

`SET_RADAR_AS_EXTERIOR_THIS_FRAME` · hash `0xE81B7D2A3DAB2D81` · jhash `0x39ABB10E` · **Cliente**

```lua
SetRadarAsExteriorThisFrame()
```
```c
void SET_RADAR_AS_EXTERIOR_THIS_FRAME();
```

**Devuelve:** `void`

---
### SetRadarAsInteriorThisFrame

`SET_RADAR_AS_INTERIOR_THIS_FRAME` · hash `0x59E727A1C9D3E31A` · jhash `0x6F2626E1` · **Cliente**

```lua
SetRadarAsInteriorThisFrame(interior, x, y, heading, zoom)
```
```c
void SET_RADAR_AS_INTERIOR_THIS_FRAME(Hash interior, float x, float y, int heading, int zoom);
```

**Parámetros**

- `interior` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `heading` (`int`)
- `zoom` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
List of interior hashes: pastebin.com/1FUyXNqY  
Not for every interior zoom > 0 available.  
```

---
### SetRadarZoom

`SET_RADAR_ZOOM` · hash `0x096EF57A0C999BBA` · jhash `0x2A50D1A6` · **Cliente**

```lua
SetRadarZoom(zoomLevel)
```
```c
void SET_RADAR_ZOOM(int zoomLevel);
```

**Parámetros**

- `zoomLevel` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
zoomLevel ranges from 0 to 200  
```

---
### SetRadarZoomPrecise

`SET_RADAR_ZOOM_PRECISE` · hash `0xBD12C5EEE184C337` · jhash `0xDCA3F423` · **Cliente**

```lua
SetRadarZoomPrecise(zoom)
```
```c
void SET_RADAR_ZOOM_PRECISE(float zoom);
```

**Parámetros**

- `zoom` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `RESPONDING_AS_TEMP` (`RespondingAsTemp`)

---
### SetRadarZoomToBlip

`SET_RADAR_ZOOM_TO_BLIP` · hash `0xF98E4B3E56AFC7B1` · jhash `0x25EC28C0` · **Cliente**

```lua
SetRadarZoomToBlip(blip, zoom)
```
```c
void SET_RADAR_ZOOM_TO_BLIP(Blip blip, float zoom);
```

**Parámetros**

- `blip` (`Blip`)
- `zoom` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF98E4B3E56AFC7B1` (`N_0xf98e4b3e56afc7b1`)

---
### SetRadarZoomToDistance

`SET_RADAR_ZOOM_TO_DISTANCE` · hash `0xCB7CC0D58405AD41` · jhash `0x09CF1CE5` · **Cliente**

```lua
SetRadarZoomToDistance(zoom)
```
```c
void SET_RADAR_ZOOM_TO_DISTANCE(float zoom);
```

**Parámetros**

- `zoom` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_RADAR_ZOOM_LEVEL_THIS_FRAME` (`SetRadarZoomLevelThisFrame`)

---
### SetRadiusBlipEdge

`SET_RADIUS_BLIP_EDGE` · hash `0x25615540D894B814` · jhash `0x40E25DB8` · **Cliente**

```lua
SetRadiusBlipEdge(blip, toggle)
```
```c
void SET_RADIUS_BLIP_EDGE(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`): The blip handle
- `toggle` (`BOOL`): Whether to turn off or on the effect

**Devuelve:** `void`

**Descripción oficial:**

Enabling this on a radius blip will make it outline only.\
Please note that this only works on a **radius** blip (i.e. one generated using [`ADD_BLIP_FOR_RADIUS`](../cfx/servidor.md#addblipforradius)), not a normal blip.

**Nombres antiguos (alias):** `0x25615540D894B814` (`N_0x25615540d894b814`)

**Ejemplo (lua):**

```lua
local coords = GetEntityCoords(PlayerPedId())
local radiusBlip = AddBlipForRadius(coords, 100.0) -- need to have .0
SetBlipColour(radiusBlip, 1)
SetBlipAlpha(radiusBlip, 255)
SetRadiusBlipEdge(radiusBlip, true)
```

---
### SetScriptVariableHudColour

`SET_SCRIPT_VARIABLE_HUD_COLOUR` · hash `0xD68A5FF8A3A89874` · jhash `0x0E41E45C` · **Cliente**

```lua
SetScriptVariableHudColour(r, g, b, a)
```
```c
void SET_SCRIPT_VARIABLE_HUD_COLOUR(int r, int g, int b, int a);
```

**Parámetros**

- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the color of HUD_COLOUR_SCRIPT_VARIABLE
```

**Nombres antiguos (alias):** `0xD68A5FF8A3A89874` (`N_0xd68a5ff8a3a89874`)

---
### SetScriptVariable_2HudColour

`_SET_SCRIPT_VARIABLE_2_HUD_COLOUR` · hash `0x16A304E6CB2BFAB9` · jhash `0x6BE3ACA8` · **Cliente**

```lua
SetScriptVariable_2HudColour(r, g, b, a)
```
```c
void _SET_SCRIPT_VARIABLE_2_HUD_COLOUR(int r, int g, int b, int a);
```

**Parámetros**

- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the color of HUD_COLOUR_SCRIPT_VARIABLE_2
```

**Nombres antiguos (alias):** `0x16A304E6CB2BFAB9` (`N_0x16a304e6cb2bfab9`)

---
### SetSocialClubTour

`SET_SOCIAL_CLUB_TOUR` · hash `0x9E778248D6685FE0` · jhash `0x7AD67C95` · **Cliente**

```lua
SetSocialClubTour(name)
```
```c
void SET_SOCIAL_CLUB_TOUR(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
HUD::SET_SOCIAL_CLUB_TOUR("Gallery");
HUD::SET_SOCIAL_CLUB_TOUR("Missions");
HUD::SET_SOCIAL_CLUB_TOUR("General");
HUD::SET_SOCIAL_CLUB_TOUR("Playlists");
```

**Nombres antiguos (alias):** `0x9E778248D6685FE0` (`N_0x9e778248d6685fe0`)

---
### SetTextCentre

`SET_TEXT_CENTRE` · hash `0xC02F4DBFB51D988B` · jhash `0xE26D39A1` · **Cliente**

```lua
SetTextCentre(align)
```
```c
void SET_TEXT_CENTRE(BOOL align);
```

**Parámetros**

- `align` (`BOOL`)

**Devuelve:** `void`

---
### SetTextColour

`SET_TEXT_COLOUR` · hash `0xBE6B23FFA53FB442` · jhash `0xE54DD2C8` · **Cliente**

```lua
SetTextColour(red, green, blue, alpha)
```
```c
void SET_TEXT_COLOUR(int red, int green, int blue, int alpha);
```

**Parámetros**

- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
colors you input not same as you think?
A: for some reason its R B G A
```

---
### SetTextDropShadow

`SET_TEXT_DROP_SHADOW` · hash `0x1CA3E9EAC9D93E5E` · jhash `0xE2A11511` · **Cliente**

```lua
SetTextDropShadow()
```
```c
void SET_TEXT_DROP_SHADOW();
```

**Devuelve:** `void`

---
### SetTextDropshadow

`SET_TEXT_DROPSHADOW` · hash `0x465C84BC39F1C351` · jhash `0xE6587517` · **Cliente**

```lua
SetTextDropshadow(distance, r, g, b, a)
```
```c
void SET_TEXT_DROPSHADOW(int distance, int r, int g, int b, int a);
```

**Parámetros**

- `distance` (`int`): Shadow distance in pixels, both horizontal and vertical.
- `r` (`int`): Red color.
- `g` (`int`): Green color.
- `b` (`int`): Blue color.
- `a` (`int`): Alpha.

**Devuelve:** `void`

**Descripción oficial:**

distance - shadow distance in pixels, both horizontal and vertical
r, g, b, a - color

---
### SetTextEdge

`SET_TEXT_EDGE` · hash `0x441603240D202FA6` · jhash `0x3F1A5DAB` · **Cliente**

```lua
SetTextEdge(p0, r, g, b, a)
```
```c
void SET_TEXT_EDGE(int p0, int r, int g, int b, int a);
```

**Parámetros**

- `p0` (`int`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### SetTextFont

`SET_TEXT_FONT` · hash `0x66E0276CC5F6B9DA` · jhash `0x80BC530D` · **Cliente**

```lua
SetTextFont(fontType)
```
```c
void SET_TEXT_FONT(int fontType);
```

**Parámetros**

- `fontType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eTextFonts
{
    FONT_STANDARD = 0,
    FONT_CURSIVE = 1,
    FONT_ROCKSTAR_TAG = 2,
    FONT_LEADERBOAR0D = 3,
    FONT_CONDENSED = 4,
    FONT_STYLE_FIXED_WIDTH_NUMBERS = 5,
    FONT_CONDENSED_NOT_GAMERNAME = 6,
    FONT_STYLE_PRICEDOWN = 7,
    FONT_STYLE_TAXI = 8,
}
```

---
### SetTextInputBoxEnabled

`SET_TEXT_INPUT_BOX_ENABLED` · hash `0x1185A8087587322C` · **Cliente**

```lua
SetTextInputBoxEnabled(state)
```
```c
void SET_TEXT_INPUT_BOX_ENABLED(BOOL state);
```

**Parámetros**

- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Toggles if the text input box can be opened with [`DISPLAY_ONSCREEN_KEYBOARD`](MISC.md#displayonscreenkeyboard).

**Nombres antiguos (alias):** `0x1185A8087587322C` (`N_0x1185a8087587322c`)

---
### SetTextJustification

`SET_TEXT_JUSTIFICATION` · hash `0x4E096588B13FFECA` · jhash `0x68CDFA60` · **Cliente**

```lua
SetTextJustification(justifyType)
```
```c
void SET_TEXT_JUSTIFICATION(int justifyType);
```

**Parámetros**

- `justifyType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Types -  
0: Center-Justify  
1: Left-Justify  
2: Right-Justify  
Right-Justify requires SET_TEXT_WRAP, otherwise it will draw to the far right of the screen  
```

**Nombres antiguos (alias):** `0x4E096588B13FFECA` (`N_0x4e096588b13ffeca`)

---
### SetTextLeading

`SET_TEXT_LEADING` · hash `0xA50ABC31E3CDFAFF` · jhash `0x98CE21D4` · **Cliente**

```lua
SetTextLeading(p0)
```
```c
void SET_TEXT_LEADING(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### SetTextOutline

`SET_TEXT_OUTLINE` · hash `0x2513DFB0FB8400FE` · jhash `0xC753412F` · **Cliente**

```lua
SetTextOutline()
```
```c
void SET_TEXT_OUTLINE();
```

**Devuelve:** `void`

---
### SetTextProportional

`SET_TEXT_PROPORTIONAL` · hash `0x038C1F517D7FDCF8` · jhash `0xF49D8A08` · **Cliente**

```lua
SetTextProportional(p0)
```
```c
void SET_TEXT_PROPORTIONAL(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### SetTextRenderId

`SET_TEXT_RENDER_ID` · hash `0x5F15302936E07111` · jhash `0xC5C3B7F3` · **Cliente**

```lua
SetTextRenderId(renderId)
```
```c
void SET_TEXT_RENDER_ID(int renderId);
```

**Parámetros**

- `renderId` (`int`)

**Devuelve:** `void`

---
### SetTextRightJustify

`SET_TEXT_RIGHT_JUSTIFY` · hash `0x6B3C4650BC8BEE47` · jhash `0x45B60520` · **Cliente**

```lua
SetTextRightJustify(toggle)
```
```c
void SET_TEXT_RIGHT_JUSTIFY(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetTextScale

`SET_TEXT_SCALE` · hash `0x07C837F9A01C34C9` · jhash `0xB6E15B23` · **Cliente**

```lua
SetTextScale(scale, size)
```
```c
void SET_TEXT_SCALE(float scale, float size);
```

**Parámetros**

- `scale` (`float`)
- `size` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Size range : 0F to 1.0F
p0 is unknown and doesn't seem to have an effect, yet in the game scripts it changes to 1.0F sometimes.
```

---
### SetTextWrap

`SET_TEXT_WRAP` · hash `0x63145D9C883A1A70` · jhash `0x6F60AB54` · **Cliente**

```lua
SetTextWrap(start, end)
```
```c
void SET_TEXT_WRAP(float start, float end);
```

**Parámetros**

- `start` (`float`)
- `end` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
It sets the text in a specified box and wraps the text if it exceeds the boundries. Both values are for X axis. Useful when positioning text set to center or aligned to the right.  
start - left boundry on screen position (0.0 - 1.0)  
end - right boundry on screen position (0.0 - 1.0)  
```

---
### SetUseIslandMap

`SET_USE_ISLAND_MAP` · hash `0x5E1460624D194A38` · **Cliente**

```lua
SetUseIslandMap(toggle)
```
```c
void SET_USE_ISLAND_MAP(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): A boolean value where `true` switches the minimap to the Cayo Perico map, and `false` reverts it to the standard map.

**Devuelve:** `void` — This native does not return any value.

**Descripción oficial:**

Switches the display of the in-game minimap to the Cayo Perico map. This native needs to be called every frame to maintain the toggled state effectively.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `_SET_TOGGLE_MINIMAP_HEIST_ISLAND` (`SetToggleMinimapHeistIsland`)

---
### SetUseWaypointAsDestination

`_SET_USE_WAYPOINT_AS_DESTINATION` · hash `0x6CDD58146A436083` · **Cliente**

```lua
SetUseWaypointAsDestination(toggle)
```
```c
void _SET_USE_WAYPOINT_AS_DESTINATION(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): `true` to show 'Destination', `false` to show 'Waypoint' (the default)

**Devuelve:** `void`

**Descripción oficial:**

Sets a global mode which makes the pause menu map show 'Destination' instead of 'Waypoint' in the key legend on the
bottom of the screen.

<!--

Name guess:

  - alphabetical function order, below [SET_USER_RADIO_CONTROL_ENABLED, SET_USE_HI_DOF], above SET_VARIABLE_ON_SOUND.

-->

**Nombres antiguos (alias):** `0x6CDD58146A436083` (`N_0x6cdd58146a436083`)

---
### SetWarningMessage

`SET_WARNING_MESSAGE` · hash `0x7B1776B3B53F8D74` · jhash `0xBE699BDE` · **Cliente**

```lua
SetWarningMessage(entryLine1, instructionalKey, entryLine2, p3, p4, background, p6, showBg, errorCode)
```
```c
void SET_WARNING_MESSAGE(char* entryLine1, int instructionalKey, char* entryLine2, BOOL p3, int p4, char* background, char* p6, BOOL showBg, int errorCode);
```

**Parámetros**

- `entryLine1` (`char*`): The text label to display as the first line of the warning message.
- `instructionalKey` (`int`): This is an enum, check the description for a list.
- `entryLine2` (`char*`): The text label to display as the second line of the warning message.
- `p3` (`BOOL`): Purpose unknown.
- `p4` (`int`): Purpose unknown.
- `background` (`char*`): Set to anything other than 0 or false (even any string) and it will draw a background. Setting it to 0 or false will draw no background.
- `p6` (`char*`): Purpose unknown.
- `showBg` (`BOOL`): Purpose unknown.
- `errorCode` (`int`): When not 0, adds a field displaying the value as 'error code' to the warning message.

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eInstructionalButtonTypes
{
    NONE = 0,
    SELECT = 1,
    OK = 2,
    YES = 4,
    BACK = 8,
    BACK_SELECT = 9,
    BACK_OK = 10,
    BACK_YES = 12,
    CANCEL = 16,
    CANCEL_SELECT = 17,
    CANCEL_OK = 18,
    CANCEL_YES = 20,
    NO = 32,
    NO_SELECT = 33,
    NO_OK = 34,
    YES_NO = 36,
    RETRY = 64,
    RETRY_SELECT = 65,
    RETRY_OK = 66,
    RETRY_YES = 68,
    RETRY_BACK = 72,
    RETRY_BACK_SELECT = 73,
    RETRY_BACK_OK = 74,
    RETRY_BACK_YES = 76,
    RETRY_CANCEL = 80,
    RETRY_CANCEL_SELECT = 81,
    RETRY_CANCEL_OK = 82,
    RETRY_CANCEL_YES = 84,
    SKIP = 256,
    SKIP_SELECT = 257,
    SKIP_OK = 258,
    SKIP_YES = 260,
    SKIP_BACK = 264,
    SKIP_BACK_SELECT = 265,
    SKIP_BACK_OK = 266,
    SKIP_BACK_YES = 268,
    SKIP_CANCEL = 272,
    SKIP_CANCEL_SELECT = 273,
    SKIP_CANCEL_OK = 274,
    SKIP_CANCEL_YES = 276,
    CONTINUE = 16384,
    BACK_CONTINUE = 16392,
    CANCEL_CONTINUE = 16400,
    LOADING_SPINNER = 134217728,
    SELECT_LOADING_SPINNER = 134217729,
    OK_LOADING_SPINNER = 134217730,
    YES_LOADING_SPINNER = 134217732,
    BACK_LOADING_SPINNER = 134217736,
    BACK_SELECT_LOADING_SPINNER = 134217737,
    BACK_OK_LOADING_SPINNER = 134217738,
    BACK_YES_LOADING_SPINNER = 134217740,
    CANCEL_LOADING_SPINNER = 134217744,
    CANCEL_SELECT_LOADING_SPINNER = 134217745,
    CANCEL_OK_LOADING_SPINNER = 134217746,
    CANCEL_YES_LOADING_SPINNER = 134217748
}
```

Note: this list is definitely NOT complete, but these are the ones I've been able to find before giving up because it's such a boring thing to look for 'good' combinations.

**Result of the example code:**
![](https://i.imgur.com/aG6ROkP.png)

**Ejemplo (lua):**

```lua
-- Make the first line using custom text.
AddTextEntry("warning_message_first_line", "This is the first line.")

-- Make the second line using custom text.
AddTextEntry("warning_message_second_line", "This is the second line!")

-- Add an event handler for when the screen is dismissed.
AddEventHandler("optionSelected", function(selected)
    print(selected) -- do whatever you want with the selected choice.
    -- players can either press the physicial buttons, or they can click
    -- the instructional buttons with their mouse and it will trigger
    -- the event as well.
end)


-- Create a thread to loop this warning message.
CreateThread(function()
    while true do
        Wait(0)
        -- Display the warning message every tick.
        SetWarningMessage("warning_message_first_line", 82, "warning_message_second_line", 0, -1, true, 0, 0, 0)
        
        -- Check for key presses or instructional button clicks.
        -- Input group of 2 is required for this to work while the warning is being displayed.
        
        if (IsControlJustReleased(2, 201) or IsControlJustReleased(2, 217)) then -- any select/confirm key was pressed.
            TriggerEvent("optionSelected", "select")
            break
        elseif (IsControlJustReleased(2, 203)) then -- spacebar/x on controller (alt option) was pressed.
            TriggerEvent("optionSelected", "alt")
            break
        elseif (IsControlJustReleased(2, 202)) then -- any of the cancel/back buttons was pressed
            TriggerEvent("optionSelected", "cancel")
            break
        end
    end
end)
```

---
### SetWarningMessageOptionItems

`SET_WARNING_MESSAGE_OPTION_ITEMS` · hash `0x0C5A80A9E096D529` · **Cliente**

```lua
local retval = SetWarningMessageOptionItems(index, name, cash, rp, lvl, colour)
```
```c
BOOL SET_WARNING_MESSAGE_OPTION_ITEMS(int index, char* name, int cash, int rp, int lvl, int colour);
```

**Parámetros**

- `index` (`int`)
- `name` (`char*`)
- `cash` (`int`)
- `rp` (`int`)
- `lvl` (`int`)
- `colour` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0C5A80A9E096D529` (`N_0x0c5a80a9e096d529`), `_SET_WARNING_MESSAGE_LIST_ROW` (`SetWarningMessageListRow`)

---
### SetWarningMessageWithAlert

`_SET_WARNING_MESSAGE_WITH_ALERT` · hash `0x15803FEC3B9A872B` · **Cliente**

```lua
SetWarningMessageWithAlert(labelTitle, labelMsg, p2, p3, labelMsg2, p5, p6, p7, p8, p9, background, errorCode)
```
```c
void _SET_WARNING_MESSAGE_WITH_ALERT(char* labelTitle, char* labelMsg, int p2, int p3, char* labelMsg2, BOOL p5, int p6, int p7, char* p8, char* p9, BOOL background, int errorCode);
```

**Parámetros**

- `labelTitle` (`char*`): Label of the alert's title.
- `labelMsg` (`char*`): Label of the alert's message.
- `p2` (`int`): This is an enum, check the description for a list.
- `p3` (`int`): This is an enum, check the description for a list.
- `labelMsg2` (`char*`): Label of another message line
- `p5` (`BOOL`): usually 0
- `p6` (`int`): usually -1
- `p7` (`int`): usually 0
- `p8` (`char*`): unknown label
- `p9` (`char*`): unknown label
- `background` (`BOOL`): Set to anything other than 0 or false (even any string) and it will draw a background. Setting it to 0 or false will draw no background.
- `errorCode` (`int`): Error code, shown at the bottom left if set to value other than 0.

**Devuelve:** `void`

**Descripción oficial:**

instructionalKey enum list:

```
Buttons = {
      Empty = 0,
      Select = 1, -- (RETURN)
      Ok = 2, -- (RETURN)
      Yes = 4, -- (RETURN)
      Back = 8, -- (ESC)
      Cancel = 16, -- (ESC)
      No = 32, -- (ESC)
      RetrySpace = 64, -- (SPACE)
      Restart = 128, -- (SPACE)
      Skip = 256, -- (SPACE)
      Quit = 512, -- (ESC)
      Adjust = 1024, -- (ARROWS)
      SpaceKey = 2048, -- (SPACE)
      Share = 4096, -- (SPACE)
      SignIn = 8192, -- (SPACE)
      Continue = 16384, -- (RETURN)
      AdjustLeftRight = 32768, -- (SCROLL L/R)
      AdjustUpDown = 65536, -- (SCROLL U/D)
      Overwrite = 131072, -- (SPACE)
      SocialClubSignup = 262144, -- (RETURN)
      Confirm = 524288, -- (RETURN)
      Queue = 1048576, -- (RETURN)
      RetryReturn = 2097152, -- (RETURN)
      BackEsc = 4194304, -- (ESC)
      SocialClub = 8388608, -- (RETURN)
      Spectate = 16777216, -- (SPACE)
      OkEsc = 33554432, -- (ESC)
      CancelTransfer = 67108864, -- (ESC)
      LoadingSpinner = 134217728,
      NoReturnToGTA = 268435456, -- (ESC)
      CancelEsc = 536870912, -- (ESC)
}

Alt = {
      Empty = 0,
      No = 1, -- (SPACE)
      Host = 2, -- (ESC)
      SearchForJob = 4, -- (RETURN)
      ReturnKey = 8, -- (TURN)
      Freemode = 16, -- (ESC)
}
```

**Result of the example code:**
![](https://i.imgur.com/Cw5GoGs.png)

**Nombres antiguos (alias):** `0x15803FEC3B9A872B` (`N_0x15803fec3b9a872b`), `_DRAW_FRONTEND_ALERT` (`DrawFrontendAlert`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
	AddTextEntry("FACES_WARNH2", "Nice title")
	AddTextEntry("QM_NO_0", "Cool message")
	AddTextEntry("QM_NO_3", "Cool message 2")
	while true do
		Citizen.Wait(0)
		DrawFrontendAlert("FACES_WARNH2", "QM_NO_0", 3, 3, "QM_NO_3", 2, -1, false, "FM_NXT_RAC", "QM_NO_1", true, 10)
	end
end)
```

---
### SetWarningMessageWithHeader

`SET_WARNING_MESSAGE_WITH_HEADER` · hash `0xDC38CC1E35B6A5D7` · jhash `0x2DB9EAB5` · **Cliente**

```lua
local p7 = SetWarningMessageWithHeader(titleMsg, entryLine1, flags, promptMsg, p4, p5, background, showBg)
```
```c
void SET_WARNING_MESSAGE_WITH_HEADER(char* titleMsg, char* entryLine1, int flags, char* promptMsg, BOOL p4, Any p5, BOOL background, Any* p7, BOOL showBg);
```

**Parámetros**

- `titleMsg` (`char*`)
- `entryLine1` (`char*`)
- `flags` (`int`)
- `promptMsg` (`char*`)
- `p4` (`BOOL`)
- `p5` (`Any`)
- `background` (`BOOL`)
- `p7` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `showBg` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
You can only use text entries. No custom text.  
C# Example :  
Function.Call(Hash._SET_WARNING_MESSAGE_2, "HUD_QUIT", "HUD_CGIGNORE", 2, "HUD_CGINVITE", 0, -1, 0, 0, 1);  
you can recreate this easily with scaleforms  
---------------  
Fixed native name, from before nativedb restoration.  
```

```
NativeDB Added Parameter 10: Any p9
```

**Nombres antiguos (alias):** `_SET_WARNING_MESSAGE_2` (`SetWarningMessage_2`)

---
### SetWarningMessageWithHeaderAndSubstringFlags

`SET_WARNING_MESSAGE_WITH_HEADER_AND_SUBSTRING_FLAGS` · hash `0x701919482C74B5AB` · jhash `0x749929D3` · **Cliente**

```lua
local p7, p8 = SetWarningMessageWithHeaderAndSubstringFlags(entryHeader, entryLine1, instructionalKey, entryLine2, p4, p5, p6, p9)
```
```c
void SET_WARNING_MESSAGE_WITH_HEADER_AND_SUBSTRING_FLAGS(char* entryHeader, char* entryLine1, Any instructionalKey, char* entryLine2, BOOL p4, Any p5, Any p6, Any* p7, Any* p8, BOOL p9);
```

**Parámetros**

- `entryHeader` (`char*`)
- `entryLine1` (`char*`)
- `instructionalKey` (`Any`)
- `entryLine2` (`char*`)
- `p4` (`BOOL`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p8` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p9` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
You can only use text entries. No custom text.  
```

```
NativeDB Added Parameter 11: Any p10
```

**Nombres antiguos (alias):** `_SET_WARNING_MESSAGE_3` (`SetWarningMessage_3`)

---
### SetWarningMessageWithHeaderExtended

`SET_WARNING_MESSAGE_WITH_HEADER_EXTENDED` · hash `0x38B55259C2E078ED` · **Cliente**

```lua
SetWarningMessageWithHeaderExtended(headerTextLabel, line1TextLabel, buttonsBitField, buttonsBitFieldUpper, line2TextLabel, addNumber, numberToAdd, firstSubstring, secondSubstring, showBackground, errorCode)
```
```c
void SET_WARNING_MESSAGE_WITH_HEADER_EXTENDED(char* headerTextLabel, char* line1TextLabel, int buttonsBitField, int buttonsBitFieldUpper, char* line2TextLabel, BOOL addNumber, int numberToAdd, char* firstSubstring, char* secondSubstring, BOOL showBackground, int errorCode);
```

**Parámetros**

- `headerTextLabel` (`char*`): Text label to set on the header/title.
- `line1TextLabel` (`char*`): Text label to set on the first line of the body..
- `buttonsBitField` (`int`): Bit field of the button flags. See [`SET_WARNING_MESSAGE`](#setwarningmessage).
- `buttonsBitFieldUpper` (`int`): Bit field of the upper button flags. See [`SET_WARNING_MESSAGE_WITH_HEADER_AND_SUBSTRING_FLAGS_EXTENDED`](#setwarningmessagewithalert).
- `line2TextLabel` (`char*`): Text label to set on the second line of the body.
- `addNumber` (`BOOL`): If number should be inserted into `~1~` in the body.
- `numberToAdd` (`int`): What number to insert into `~1~` in the body.
- `firstSubstring` (`char*`): First substring text label to insert into `~a~` in the body.
- `secondSubstring` (`char*`): Second substring text label to insert into `~a~` in the body.
- `showBackground` (`BOOL`): Bool indicating if the message should have a black background.
- `errorCode` (`int`): Error number to show at the bottom of the message. `0` is the default.

**Devuelve:** `void`

**Descripción oficial:**

Sets a warning message for one frame with header and upper buttons bit field that don't fit the standard 32 bit set.

**Nombres antiguos (alias):** `0x38B55259C2E078ED` (`N_0x38b55259c2e078ed`), `_SET_WARNING_MESSAGE_WITH_HEADER_UNK` (`SetWarningMessageWithHeaderUnk`)

---
### SetWaypointOff

`SET_WAYPOINT_OFF` · hash `0xA7E4E2D361C2627F` · jhash `0xB3496E1B` · **Cliente**

```lua
SetWaypointOff()
```
```c
void SET_WAYPOINT_OFF();
```

**Devuelve:** `void`

**Descripción oficial:**

```
This native removes the current waypoint from the map.
Example:
C#:
Function.Call(Hash.SET_WAYPOINT_OFF);
C++:
HUD::SET_WAYPOINT_OFF();
```

---
### SetWidescreenFormat

`SET_WIDESCREEN_FORMAT` · hash `0xC3B07BA00A83B0F1` · jhash `0xF016E08F` · **Cliente**

```lua
SetWidescreenFormat(p0)
```
```c
void SET_WIDESCREEN_FORMAT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### ShowContactInstructionalButton

`SHOW_CONTACT_INSTRUCTIONAL_BUTTON` · hash `0xC772A904CDE1186F` · **Cliente**

```lua
ShowContactInstructionalButton(toggle)
```
```c
void SHOW_CONTACT_INSTRUCTIONAL_BUTTON(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Set to `true` to show the instructional buttons, or `false` to hide them.

**Devuelve:** `void`

**Descripción oficial:**

Controls the visibility of the "Contact" instructional buttons on the map screen.

```
NativeDB Introduced: 2545
```

---
### ShowCrewIndicatorOnBlip

`SHOW_CREW_INDICATOR_ON_BLIP` · hash `0xDCFB5D4DB8BF367E` · jhash `0xABBE1E45` · **Cliente**

```lua
ShowCrewIndicatorOnBlip(blip, toggle)
```
```c
void SHOW_CREW_INDICATOR_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`): The blip to toggle the half blue circle around the blip on.
- `toggle` (`BOOL`): Enables or disables the half blue circle around the blip (on the left side).

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables the blue half circle around the specified blip on the left side of the blip. This is used to indicate that the player is in your crew in GTA:O. Color is changeable by using [`SET_BLIP_SECONDARY_COLOUR`](#setblipsecondarycolour).

Preview:

![](https://i.imgur.com/JgRMbHb.png)

To toggle the right side of the circle use: [`SHOW_FRIEND_INDICATOR_ON_BLIP`](#showfriendindicatoronblip).

**Nombres antiguos (alias):** `0xDCFB5D4DB8BF367E` (`N_0xdcfb5d4db8bf367e`), `SET_BLIP_CREW` (`SetBlipCrew`)

**Ejemplo (lua):**

```lua
local player = 1 -- make sure this is an actual player, dont just use this example code!
local blip = GetBlipFromEntity(GetPlayerPed(player))

-- Toggle the crew display.
ShowCrewIndicatorOnBlip(blip, true)

-- Set the crew circle color.
-- hud color 18 seems to be the closest color to the green crew color from GTA:O.
SetBlipSecondaryColour(blip, GetHudColour(18))


-- result: https://i.imgur.com/iZ9tNWl.png
```

---
### ShowFriendIndicatorOnBlip

`SHOW_FRIEND_INDICATOR_ON_BLIP` · hash `0x23C3EB807312F01A` · jhash `0x4C8F02B4` · **Cliente**

```lua
ShowFriendIndicatorOnBlip(blip, toggle)
```
```c
void SHOW_FRIEND_INDICATOR_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`): The blip to toggle the half circle on.
- `toggle` (`BOOL`): Enables or disables the half circle around the blip (on the right side of the blip).

**Devuelve:** `void`

**Descripción oficial:**

Highlights a blip by a half cyan circle on the right side of the blip, indicating that that player is a friend (in GTA:O). This color can not be changed.

Preview:

![](https://i.imgur.com/v9FsjYl.png)

To toggle the left side (crew member indicator) of the half circle around the blip, use: [`SHOW_CREW_INDICATOR_ON_BLIP`](#showcrewindicatoronblip).

**Nombres antiguos (alias):** `0x23C3EB807312F01A` (`N_0x23c3eb807312f01a`), `SET_BLIP_FRIEND` (`SetBlipFriend`)

**Ejemplo (lua):**

```lua
local player = 1 -- make sure this is an actual player, dont just use this example code!
local blip = GetBlipFromEntity(GetPlayerPed(player))

-- Toggle the friend outline indicator on the blip.
ShowFriendIndicatorOnBlip(blip, true)
```

---
### ShowHasCompletedIndicatorOnBlip

`_SHOW_HAS_COMPLETED_INDICATOR_ON_BLIP` · hash `0xCAC2031EBF79B1A8` · **Cliente**

```lua
ShowHasCompletedIndicatorOnBlip(blip, toggle)
```
```c
void _SHOW_HAS_COMPLETED_INDICATOR_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Adds a orange checkmark on top of a given blip handle.

Preview:

![](https://i.imgur.com/KG9k6Fk.png)

```
_SHOW_FRIEND_INDICATOR_ON_BLIP* - _SHOW_HEADING_INDICATOR_ON_BLIP*
```

```
NativeDB Introduced: v2699
```

---
### ShowHeadingIndicatorOnBlip

`SHOW_HEADING_INDICATOR_ON_BLIP` · hash `0x5FBCA48327B914DF` · jhash `0xD1C3D71B` · **Cliente**

```lua
ShowHeadingIndicatorOnBlip(blip, toggle)
```
```c
void SHOW_HEADING_INDICATOR_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Adds the GTA: Online player heading indicator to a blip.  
```

**Nombres antiguos (alias):** `0x5FBCA48327B914DF` (`N_0x5fbca48327b914df`)

---
### ShowHeightOnBlip

`SHOW_HEIGHT_ON_BLIP` · hash `0x75A16C3DA34F1245` · jhash `0x1D99F676` · **Cliente**

```lua
ShowHeightOnBlip(blip, toggle)
```
```c
void SHOW_HEIGHT_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x75A16C3DA34F1245` (`N_0x75a16c3da34f1245`)

---
### ShowHudComponentThisFrame

`SHOW_HUD_COMPONENT_THIS_FRAME` · hash `0x0B4DF1FA60C0E664` · jhash `0x95E1546E` · **Cliente**

```lua
ShowHudComponentThisFrame(id)
```
```c
void SHOW_HUD_COMPONENT_THIS_FRAME(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

This function shows various HUD (Heads-up Display) components.

Listed below are the integers and the corresponding HUD component.

*   1 : WANTED_STARS
*   2 : WEAPON_ICON
*   3 : CASH
*   4 : MP_CASH
*   5 : MP_MESSAGE
*   6 : VEHICLE_NAME
*   7 : AREA_NAME
*   8 : VEHICLE_CLASS
*   9 : STREET_NAME
*   10 : HELP_TEXT
*   11 : FLOATING_HELP_TEXT\_1
*   12 : FLOATING_HELP_TEXT\_2
*   13 : CASH_CHANGE
*   14 : RETICLE
*   15 : SUBTITLE_TEXT
*   16 : RADIO_STATIONS
*   17 : SAVING_GAME
*   18 : GAME_STREAM
*   19 : WEAPON_WHEEL
*   20 : WEAPON_WHEEL_STATS
*   21 : HUD_COMPONENTS
*   22 : HUD_WEAPONS

These integers also work for the [`HIDE_HUD_COMPONENT_THIS_FRAME`](#hidehudcomponentthisframe) native, but instead hides the HUD component.

---
### ShowNumberOnBlip

`SHOW_NUMBER_ON_BLIP` · hash `0xA3C0B359DCB848B6` · jhash `0x7BFC66C6` · **Cliente**

```lua
ShowNumberOnBlip(blip, number)
```
```c
void SHOW_NUMBER_ON_BLIP(Blip blip, int number);
```

**Parámetros**

- `blip` (`Blip`)
- `number` (`int`)

**Devuelve:** `void`

---
### ShowOutlineIndicatorOnBlip

`SHOW_OUTLINE_INDICATOR_ON_BLIP` · hash `0xB81656BC81FE24D1` · jhash `0x8DE82C15` · **Cliente**

```lua
ShowOutlineIndicatorOnBlip(blip, toggle)
```
```c
void SHOW_OUTLINE_INDICATOR_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`): The blip to toggle the outline on.
- `toggle` (`BOOL`): Enables or disables the outline.

**Devuelve:** `void`

**Descripción oficial:**

Toggles a cyan outline around the blip.

Color can be changed with [`SET_BLIP_SECONDARY_COLOUR`](#setblipsecondarycolour). Enabling this circle will override the "crew" and "friend" half-circles (see [`SHOW_CREW_INDICATOR_ON_BLIP`](#showcrewindicatoronblip) and [`SHOW_FRIEND_INDICATOR_ON_BLIP`](#showfriendindicatoronblip)).

**Nombres antiguos (alias):** `0xB81656BC81FE24D1` (`N_0xb81656bc81fe24d1`), `SET_BLIP_FRIENDLY` (`SetBlipFriendly`)

---
### ShowPurchaseInstructionalButton

`_SHOW_PURCHASE_INSTRUCTIONAL_BUTTON` · hash `0xF6865E26067B708C` · **Cliente**

```lua
ShowPurchaseInstructionalButton(toggle)
```
```c
void _SHOW_PURCHASE_INSTRUCTIONAL_BUTTON(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### ShowScriptedHudComponentThisFrame

`_SHOW_SCRIPTED_HUD_COMPONENT_THIS_FRAME` · hash `0x4F38DCA127DAAEA2` · **Cliente**

```lua
ShowScriptedHudComponentThisFrame(id)
```
```c
void _SHOW_SCRIPTED_HUD_COMPONENT_THIS_FRAME(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

SHOW_\*

```
NativeDB Introduced: v1734
```

---
### ShowSigninUi

`_SHOW_SIGNIN_UI` · hash `0x60E892BA4F5BDCA4` · **Cliente**

```lua
ShowSigninUi()
```
```c
void _SHOW_SIGNIN_UI();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x60E892BA4F5BDCA4` (`N_0x60e892ba4f5bdca4`)

---
### ShowStartMissionInstructionalButton

`SHOW_START_MISSION_INSTRUCTIONAL_BUTTON` · hash `0xF1A6C18B35BCADE6` · jhash `0xA2CAAB4F` · **Cliente**

```lua
ShowStartMissionInstructionalButton(p0)
```
```c
void SHOW_START_MISSION_INSTRUCTIONAL_BUTTON(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF1A6C18B35BCADE6` (`N_0xf1a6c18b35bcade6`)

---
### ShowTickOnBlip

`SHOW_TICK_ON_BLIP` · hash `0x74513EA3E505181E` · jhash `0x3DCF0092` · **Cliente**

```lua
ShowTickOnBlip(blip, toggle)
```
```c
void SHOW_TICK_ON_BLIP(Blip blip, BOOL toggle);
```

**Parámetros**

- `blip` (`Blip`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Adds a green checkmark on top of a blip.  
```

**Nombres antiguos (alias):** `0x74513EA3E505181E` (`N_0x74513ea3e505181e`), `_SET_BLIP_CHECKED` (`SetBlipChecked`)

---
### StartGpsCustomRoute

`START_GPS_CUSTOM_ROUTE` · hash `0xDB34E8D56FC13B08` · jhash `0x7F93799B` · **Cliente**

```lua
StartGpsCustomRoute(hudColor, displayOnFoot, followPlayer)
```
```c
void START_GPS_CUSTOM_ROUTE(int hudColor, BOOL displayOnFoot, BOOL followPlayer);
```

**Parámetros**

- `hudColor` (`int`): The HUD color of the GPS path.
- `displayOnFoot` (`BOOL`): Draws the path regardless if the player is in a vehicle or not.
- `followPlayer` (`BOOL`): Draw the path partially between the previous and next point based on the players position between them. When false, the GPS appears to not disappear after the last leg is completed.

**Devuelve:** `void`

**Descripción oficial:**

Starts a new GPS custom-route, allowing you to plot lines on the map.
Lines are drawn directly between points.
The GPS custom route works like the GPS multi route, except it does not follow roads.

**Example result:**

![](https://i.imgur.com/DqmZyp2.png)

**Nombres antiguos (alias):** `0xDB34E8D56FC13B08` (`N_0xdb34e8d56fc13b08`)

**Ejemplo (lua):**

```lua
-- Clear any old route first
ClearGpsCustomRoute()

-- Start a new route
StartGpsCustomRoute(6, false, true)

-- Add the points
AddPointToGpsCustomRoute(1638.2155761719, -2344.685546875, 95.610511779785)
AddPointToGpsCustomRoute(1653.0858154297, -2068.8654785156, 96.737915039063)
AddPointToGpsCustomRoute(1451.9561767578, -2113.5344238281, 56.082130432129)
AddPointToGpsCustomRoute(1540.6088867188, -2514.4519042969, 58.842422485352)
AddPointToGpsCustomRoute(1638.2155761719, -2344.685546875, 95.610511779785)

-- Set the route to render
SetGpsCustomRouteRender(true, 16, 16)
```

---
### StartGpsMultiRoute

`START_GPS_MULTI_ROUTE` · hash `0x3D3D15AF7BCAAF83` · jhash `0xC3DCBEDB` · **Cliente**

```lua
StartGpsMultiRoute(hudColor, routeFromPlayer, displayOnFoot)
```
```c
void START_GPS_MULTI_ROUTE(int hudColor, BOOL routeFromPlayer, BOOL displayOnFoot);
```

**Parámetros**

- `hudColor` (`int`): The HUD color of the GPS path.
- `routeFromPlayer` (`BOOL`): Makes the GPS draw a path from the player to the next point, rather than the original path from the previous point.
- `displayOnFoot` (`BOOL`): Draws the GPS path regardless if the player is in a vehicle or not.

**Devuelve:** `void`

**Descripción oficial:**

Starts a new GPS multi-route, allowing you to create custom GPS paths.
GPS functions like the waypoint, except it can contain multiple points it's forced to go through.
Once the player has passed a point, the GPS will no longer force its path through it.

Works independently from the player-placed waypoint and blip routes.

**Example result:**

![](https://i.imgur.com/xIuEhwA.png)

**Nombres antiguos (alias):** `0x3D3D15AF7BCAAF83` (`N_0x3d3d15af7bcaaf83`)

**Ejemplo (lua):**

```lua
-- Clear any old route first
ClearGpsMultiRoute()

-- Start a new route
StartGpsMultiRoute(6, false, true)

-- Add the points
AddPointToGpsMultiRoute(1638.2155761719, -2344.685546875, 95.610511779785)
AddPointToGpsMultiRoute(1653.0858154297, -2068.8654785156, 96.737915039063)
AddPointToGpsMultiRoute(1451.9561767578, -2113.5344238281, 56.082130432129)
AddPointToGpsMultiRoute(1540.6088867188, -2514.4519042969, 58.842422485352)
AddPointToGpsMultiRoute(1638.2155761719, -2344.685546875, 95.610511779785)

-- Set the route to render
SetGpsMultiRouteRender(true)
```

---
### SuppressFrontendRenderingThisFrame

`SUPPRESS_FRONTEND_RENDERING_THIS_FRAME` · hash `0xBA751764F0821256` · jhash `0x7F349900` · **Cliente**

```lua
SuppressFrontendRenderingThisFrame()
```
```c
void SUPPRESS_FRONTEND_RENDERING_THIS_FRAME();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBA751764F0821256` (`N_0xba751764f0821256`)

---
### TakeControlOfFrontend

`TAKE_CONTROL_OF_FRONTEND` · hash `0xEC9264727EEC0F28` · jhash `0xC06B763D` · **Cliente**

```lua
TakeControlOfFrontend()
```
```c
void TAKE_CONTROL_OF_FRONTEND();
```

**Devuelve:** `void`

**Descripción oficial:**

Disables frontend (works in custom frontends, not sure about regular pause menu) navigation keys on keyboard. Not sure about controller. Does not disable mouse controls. No need to call this every tick.

To enable the keys again, use [`0x14621BB1DF14E2B2`](#releasecontroloffrontend).

**Nombres antiguos (alias):** `0xEC9264727EEC0F28` (`N_0xec9264727eec0f28`)

---
### ThefeedAutoPostGametipsOff

`THEFEED_AUTO_POST_GAMETIPS_OFF` · hash `0xADED7F5748ACAFE6` · jhash `0x1D6859CA` · **Cliente**

```lua
ThefeedAutoPostGametipsOff()
```
```c
void THEFEED_AUTO_POST_GAMETIPS_OFF();
```

**Devuelve:** `void`

**Descripción oficial:**

Disables tip notifications enabled by [`THEFEED_AUTO_POST_GAMETIPS_ON`](#thefeedautopostgametipson)

**Nombres antiguos (alias):** `0xADED7F5748ACAFE6` (`N_0xaded7f5748acafe6`), `_THEFEED_SHOW_GTAO_TOOLTIPS` (`ThefeedShowGtaoTooltips`), `_THEFEED_COMMENT_TELEPORT_POOL_OFF` (`ThefeedCommentTeleportPoolOff`)

---
### ThefeedAutoPostGametipsOn

`THEFEED_AUTO_POST_GAMETIPS_ON` · hash `0x56C8B608CFD49854` · jhash `0xF881AB87` · **Cliente**

```lua
ThefeedAutoPostGametipsOn()
```
```c
void THEFEED_AUTO_POST_GAMETIPS_ON();
```

**Devuelve:** `void`

**Descripción oficial:**

Enables loading screen tips to be be shown, blocks other kinds of notifications from being displayed.
Call [`THEFEED_AUTO_POST_GAMETIPS_OFF`](#thefeedautopostgametipsoff) to disable.

Example result:
![](https://i.imgur.com/GdRa0kw.png)

**Nombres antiguos (alias):** `0x56C8B608CFD49854` (`N_0x56c8b608cfd49854`), `_THEFEED_COMMENT_TELEPORT_POOL_ON` (`ThefeedCommentTeleportPoolOn`)

**Ejemplo (lua):**

```lua
ThefeedAutoPostGametipsOn()
```

---
### ThefeedClearFrozenPost

`THEFEED_CLEAR_FROZEN_POST` · hash `0x80FE4F3AB4E1B62A` · jhash `0x3CD4307C` · **Cliente**

```lua
ThefeedClearFrozenPost()
```
```c
void THEFEED_CLEAR_FROZEN_POST();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x80FE4F3AB4E1B62A` (`N_0x80fe4f3ab4e1b62a`), `_THEFEED_FLUSH_PERSISTENT` (`ThefeedFlushPersistent`)

---
### ThefeedDisableLoadingScreenTips

`_THEFEED_DISABLE_LOADING_SCREEN_TIPS` · hash `0x32888337579A5970` · **Cliente**

```lua
ThefeedDisableLoadingScreenTips()
```
```c
void _THEFEED_DISABLE_LOADING_SCREEN_TIPS();
```

**Devuelve:** `void`

**Descripción oficial:**

Stops loading screen tips shown by invoking either `0x488043841BBE156F` or `0x15CFA549788D35EF`

**Nombres antiguos (alias):** `0x32888337579A5970` (`N_0x32888337579a5970`), `_THEFEED_DISABLE` (`ThefeedDisable`)

---
### ThefeedDisplayLoadingScreenTips

`_THEFEED_DISPLAY_LOADING_SCREEN_TIPS` · hash `0x15CFA549788D35EF` · **Cliente**

```lua
ThefeedDisplayLoadingScreenTips()
```
```c
void _THEFEED_DISPLAY_LOADING_SCREEN_TIPS();
```

**Devuelve:** `void`

**Descripción oficial:**

Displays loading screen tips.
Seems to do the same as [`_HUD_DISPLAY_LOADING_SCREEN_TIPS`](#huddisplayloadingscreentips).
Requires [`THEFEED_AUTO_POST_GAMETIPS_ON`](#thefeedautopostgametipson) to be called beforehand.
Call [`_THEFEED_DISABLE_LOADING_SCREEN_TIPS`](#thefeeddisableloadingscreentips) to disable immediately, or [`THEFEED_AUTO_POST_GAMETIPS_OFF`](#thefeedautopostgametipsoff) to disable after the current tip.

Example result:
![](https://i.imgur.com/hzaHuPb.png)

**Nombres antiguos (alias):** `0x15CFA549788D35EF` (`N_0x15cfa549788d35ef`), `_THEFEED_ENABLE` (`ThefeedEnable`)

**Ejemplo (lua):**

```lua
ThefeedDisplayLoadingScreenTips()
```

---
### ThefeedFlushQueue

`THEFEED_FLUSH_QUEUE` · hash `0xA8FDB297A8D25FBA` · jhash `0x5205C6F5` · **Cliente**

```lua
ThefeedFlushQueue()
```
```c
void THEFEED_FLUSH_QUEUE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA8FDB297A8D25FBA` (`N_0xa8fdb297a8d25fba`)

---
### ThefeedForceRenderOff

`THEFEED_FORCE_RENDER_OFF` · hash `0x583049884A2EEE3C` · jhash `0xC8BAB2F2` · **Cliente**

```lua
ThefeedForceRenderOff()
```
```c
void THEFEED_FORCE_RENDER_OFF();
```

**Devuelve:** `void`

**Descripción oficial:**

Enables loading screen tips to be be shown (`_0x15CFA549788D35EF` and `_0x488043841BBE156F`), blocks other kinds of notifications from being displayed (at least from current script). Call `0xADED7F5748ACAFE6` to display those again.

**Nombres antiguos (alias):** `0x583049884A2EEE3C` (`N_0x583049884a2eee3c`), `_THEFEED_HIDE_GTAO_TOOLTIPS` (`ThefeedHideGtaoTooltips`)

---
### ThefeedForceRenderOn

`THEFEED_FORCE_RENDER_ON` · hash `0xA13C11E1B5C06BFC` · jhash `0x520FCB6D` · **Cliente**

```lua
ThefeedForceRenderOn()
```
```c
void THEFEED_FORCE_RENDER_ON();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA13C11E1B5C06BFC` (`N_0xa13c11e1b5c06bfc`)

---
### ThefeedFreezeNextPost

`THEFEED_FREEZE_NEXT_POST` · hash `0xFDEC055AB549E328` · jhash `0xAFA1148B` · **Cliente**

```lua
ThefeedFreezeNextPost()
```
```c
void THEFEED_FREEZE_NEXT_POST();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Requires manual management of game stream handles (i.e., 0xBE4390CB40B3E627).
```

**Nombres antiguos (alias):** `0xFDEC055AB549E328` (`N_0xfdec055ab549e328`), `_THEFEED_SET_NEXT_POST_PERSISTENT` (`ThefeedSetNextPostPersistent`)

---
### ThefeedGetFirstVisibleDeleteRemaining

`THEFEED_GET_FIRST_VISIBLE_DELETE_REMAINING` · hash `0x82352748437638CA` · jhash `0x294405D4` · **Cliente**

```lua
local retval = ThefeedGetFirstVisibleDeleteRemaining()
```
```c
int THEFEED_GET_FIRST_VISIBLE_DELETE_REMAINING();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the handle for the notification currently displayed on the screen. Name may be a hash collision, but describes the function accurately.
```

**Nombres antiguos (alias):** `0x82352748437638CA` (`N_0x82352748437638ca`), `_GET_CURRENT_NOTIFICATION` (`GetCurrentNotification`), `_THEFEED_GET_CURRENT_NOTIFICATION` (`ThefeedGetCurrentNotification`)

---
### ThefeedHideThisFrame

`THEFEED_HIDE_THIS_FRAME` · hash `0x25F87B30C382FCA7` · jhash `0x1E63088A` · **Cliente**

```lua
ThefeedHideThisFrame()
```
```c
void THEFEED_HIDE_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Once called each frame hides all above radar notifications.

**Nombres antiguos (alias):** `0x25F87B30C382FCA7` (`N_0x25f87b30c382fca7`), `_HIDE_HUD_NOTIFICATIONS_THIS_FRAME` (`HideHudNotificationsThisFrame`)

---
### ThefeedIsPaused

`THEFEED_IS_PAUSED` · hash `0xA9CBFD40B3FA3010` · jhash `0xC5223796` · **Cliente**

```lua
local retval = ThefeedIsPaused()
```
```c
BOOL THEFEED_IS_PAUSED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA9CBFD40B3FA3010` (`N_0xa9cbfd40b3fa3010`)

---
### ThefeedOnlyShowTooltips

`THEFEED_ONLY_SHOW_TOOLTIPS` · hash `0x6F1554B0CC2089FA` · jhash `0xA7C8594B` · **Cliente**

```lua
ThefeedOnlyShowTooltips(toggle)
```
```c
void THEFEED_ONLY_SHOW_TOOLTIPS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6F1554B0CC2089FA` (`N_0x6f1554b0cc2089fa`)

---
### ThefeedPause

`THEFEED_PAUSE` · hash `0xFDB423997FA30340` · jhash `0x4D0449C6` · **Cliente**

```lua
ThefeedPause()
```
```c
void THEFEED_PAUSE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFDB423997FA30340` (`N_0xfdb423997fa30340`)

---
### ThefeedRemoveItem

`THEFEED_REMOVE_ITEM` · hash `0xBE4390CB40B3E627` · jhash `0xECA8ACB9` · **Cliente**

```lua
ThefeedRemoveItem(notificationId)
```
```c
void THEFEED_REMOVE_ITEM(int notificationId);
```

**Parámetros**

- `notificationId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Removes a notification instantly instead of waiting for it to disappear  
```

**Nombres antiguos (alias):** `_REMOVE_NOTIFICATION` (`RemoveNotification`)

---
### ThefeedResetAllParameters

`THEFEED_RESET_ALL_PARAMETERS` · hash `0xFDD85225B2DEA55E` · jhash `0xA4524B23` · **Cliente**

```lua
ThefeedResetAllParameters()
```
```c
void THEFEED_RESET_ALL_PARAMETERS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFDD85225B2DEA55E` (`N_0xfdd85225b2dea55e`), `_THEFEED_CLEAR_ANIMPOSTFX` (`ThefeedClearAnimpostfx`)

---
### ThefeedResume

`THEFEED_RESUME` · hash `0xE1CD1E48E025E661` · jhash `0xD3F40140` · **Cliente**

```lua
ThefeedResume()
```
```c
void THEFEED_RESUME();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE1CD1E48E025E661` (`N_0xe1cd1e48e025e661`)

---
### ThefeedSetAnimpostfxColor

`_THEFEED_SET_ANIMPOSTFX_COLOR` · hash `0x17430B918701C342` · jhash `0xCF14D7F2` · **Cliente**

```lua
ThefeedSetAnimpostfxColor(red, green, blue, alpha)
```
```c
void _THEFEED_SET_ANIMPOSTFX_COLOR(int red, int green, int blue, int alpha);
```

**Parámetros**

- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x17430B918701C342` (`N_0x17430b918701c342`), `_SET_NOTIFICATION_FLASH_COLOR` (`SetNotificationFlashColor`)

---
### ThefeedSetAnimpostfxCount

`_THEFEED_SET_ANIMPOSTFX_COUNT` · hash `0x17AD8C9706BDD88A` · jhash `0x24A97AF8` · **Cliente**

```lua
ThefeedSetAnimpostfxCount(count)
```
```c
void _THEFEED_SET_ANIMPOSTFX_COUNT(int count);
```

**Parámetros**

- `count` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Related to notification color flashing, setting p0 to 0 invalidates a `_SET_NOTIFICATION_FLASH_COLOR` call for the target notification.

**Nombres antiguos (alias):** `0x17AD8C9706BDD88A` (`N_0x17ad8c9706bdd88a`)

---
### ThefeedSetAnimpostfxSound

`_THEFEED_SET_ANIMPOSTFX_SOUND` · hash `0x4A0C7C9BB10ABB36` · jhash `0x44018EDB` · **Cliente**

```lua
ThefeedSetAnimpostfxSound(toggle)
```
```c
void _THEFEED_SET_ANIMPOSTFX_SOUND(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Requires GAME_STREAM_ENUMS.MSGTEXT. Default sounds: "DPAD_WEAPON_SCROLL" and "HUD_FRONTEND_DEFAULT_SOUNDSET"
```

**Nombres antiguos (alias):** `0x4A0C7C9BB10ABB36` (`N_0x4a0c7c9bb10abb36`)

---
### ThefeedSetFlushAnimpostfx

`_THEFEED_SET_FLUSH_ANIMPOSTFX` · hash `0xBAE4F9B97CD43B30` · **Cliente**

```lua
ThefeedSetFlushAnimpostfx(toggle)
```
```c
void _THEFEED_SET_FLUSH_ANIMPOSTFX(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If true, remove all feed components instantly. Otherwise tween/animate close each component
```

**Nombres antiguos (alias):** `0xBAE4F9B97CD43B30` (`N_0xbae4f9b97cd43b30`)

---
### ThefeedSetNextPostBackgroundColor

`_THEFEED_SET_NEXT_POST_BACKGROUND_COLOR` · hash `0x92F0DA1E27DB96DC` · jhash `0x07CE2EA4` · **Cliente**

```lua
ThefeedSetNextPostBackgroundColor(hudColorIndex)
```
```c
void _THEFEED_SET_NEXT_POST_BACKGROUND_COLOR(int hudColorIndex);
```

**Parámetros**

- `hudColorIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
From the decompiled scripts:
HUD::_92F0DA1E27DB96DC(6);
HUD::_92F0DA1E27DB96DC(184);
HUD::_92F0DA1E27DB96DC(190);
sets background color for the next notification
6 = red
184 = green
190 = yellow
Here is a list of some colors that can be used: gyazo.com/68bd384455fceb0a85a8729e48216e15
```

**Nombres antiguos (alias):** `0x92F0DA1E27DB96DC` (`N_0x92f0da1e27db96dc`), `_SET_NOTIFICATION_BACKGROUND_COLOR` (`SetNotificationBackgroundColor`), `_THEFEED_NEXT_POST_BACKGROUND_COLOR` (`ThefeedNextPostBackgroundColor`)

---
### ThefeedSetScriptedMenuHeight

`THEFEED_SET_SCRIPTED_MENU_HEIGHT` · hash `0x55598D21339CB998` · jhash `0x1DA7E41A` · **Cliente**

```lua
ThefeedSetScriptedMenuHeight(pos)
```
```c
void THEFEED_SET_SCRIPTED_MENU_HEIGHT(float pos);
```

**Parámetros**

- `pos` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x55598D21339CB998` (`N_0x55598d21339cb998`), `_CLEAR_NOTIFICATIONS_POS` (`ClearNotificationsPos`)

---
### ThefeedSpsExtendWidescreenOff

`THEFEED_SPS_EXTEND_WIDESCREEN_OFF` · hash `0xB695E2CD0A2DA9EE` · jhash `0x4A4A40A4` · **Cliente**

```lua
ThefeedSpsExtendWidescreenOff()
```
```c
void THEFEED_SPS_EXTEND_WIDESCREEN_OFF();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB695E2CD0A2DA9EE` (`N_0xb695e2cd0a2da9ee`), `_THEFEED_DISABLE_BASELINE_OFFSET` (`ThefeedDisableBaselineOffset`)

---
### ThefeedSpsExtendWidescreenOn

`THEFEED_SPS_EXTEND_WIDESCREEN_ON` · hash `0xD4438C0564490E63` · jhash `0x709B4BCB` · **Cliente**

```lua
ThefeedSpsExtendWidescreenOn()
```
```c
void THEFEED_SPS_EXTEND_WIDESCREEN_ON();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD4438C0564490E63` (`N_0xd4438c0564490e63`), `_THEFEED_ENABLE_BASELINE_OFFSET` (`ThefeedEnableBaselineOffset`)

---
### ThefeedUpdateItemTexture

`THEFEED_UPDATE_ITEM_TEXTURE` · hash `0x317EBA71D7543F52` · jhash `0x6A3F747D` · **Cliente**

```lua
ThefeedUpdateItemTexture(txdString1, txnString1, txdString2, txnString2)
```
```c
void THEFEED_UPDATE_ITEM_TEXTURE(char* txdString1, char* txnString1, char* txdString2, char* txnString2);
```

**Parámetros**

- `txdString1` (`char*`)
- `txnString1` (`char*`)
- `txdString2` (`char*`)
- `txnString2` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used in the native scripts to reference "GET_PEDHEADSHOT_TXD_STRING" and "CHAR_DEFAULT".

NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x317EBA71D7543F52` (`N_0x317eba71d7543f52`), `_THEFEED_ADD_TXD_REF` (`ThefeedAddTxdRef`)

---
### ToggleStealthRadar

`TOGGLE_STEALTH_RADAR` · hash `0x6AFDFB93754950C7` · jhash `0xC68D47C4` · **Cliente**

```lua
ToggleStealthRadar(toggle)
```
```c
void TOGGLE_STEALTH_RADAR(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### TriggerSonarBlip

`TRIGGER_SONAR_BLIP` · hash `0x72DD432F3CDFC0EE` · jhash `0xBF25E7B2` · **Cliente**

```lua
TriggerSonarBlip(posX, posY, posZ, radius, p4)
```
```c
void TRIGGER_SONAR_BLIP(float posX, float posY, float posZ, float radius, int p4);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `radius` (`float`)
- `p4` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x72DD432F3CDFC0EE` (`N_0x72dd432f3cdfc0ee`)

---
### UnlockMinimapAngle

`UNLOCK_MINIMAP_ANGLE` · hash `0x8183455E16C42E3A` · jhash `0x742043F9` · **Cliente**

```lua
UnlockMinimapAngle()
```
```c
void UNLOCK_MINIMAP_ANGLE();
```

**Devuelve:** `void`

---
### UnlockMinimapPosition

`UNLOCK_MINIMAP_POSITION` · hash `0x3E93E06DB8EF1F30` · jhash `0x5E8E6F54` · **Cliente**

```lua
UnlockMinimapPosition()
```
```c
void UNLOCK_MINIMAP_POSITION();
```

**Devuelve:** `void`

---
### UseFakeMpCash

`USE_FAKE_MP_CASH` · hash `0x170F541E1CADD1DE` · jhash `0x6253B9D7` · **Cliente**

```lua
UseFakeMpCash(p0)
```
```c
void USE_FAKE_MP_CASH(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Related to displaying cash on the HUD
Always called before HUD::CHANGE_FAKE_MP_CASH in decompiled scripts
```

**Nombres antiguos (alias):** `0x170F541E1CADD1DE` (`N_0x170f541e1cadd1de`)

---
