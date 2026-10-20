# Using the Profiler

*A guide to using the built-in resource profiler.*

> Fuente original: https://docs.fivem.net/docs/scripting-manual/debugging/using-profiler/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

*Publicación de la comunidad por **kn0pee** (foro de Cfx.re, tema 809058).*

**Introduction**

In a recent update to FiveM, we have a very easy and in game tool which we can use to identify the exact lines of code and threads causing issues within your server!

This can be used both server side, to help find hitch warnings, or client side to improve FPS. This guide will not explain how to fix these issues, simply how to identify where they are so you can tweak and research to fix them

*Prerequisites*

To ensure profiler works, make sure your client is up to date, and you are using the latest server artifacts. You also **need** google chrome installed to properly view the profile. If you are viewing the profile without saving first make sure you keep your game / the server open and running!

**Usage of the Profiler**

Capturing a Profile
To begin the profiling, open your console (F8 on client, or the server console), and type the following command

`profiler record (frames to record)`

A good starting point is 500 frames, as this captures things over a substantial period of time. All going well you should see a message which says start

![](https://forum-cfx-re.akamaized.net/original/4X/9/6/c/96c684197eacac782079076fc948eec7b1e59f0e.png)

To check the status of the profiler, such as whether the capture is active, and how many frame it has captured, use `profiler status`. It will display something like this

![](https://forum-cfx-re.akamaized.net/original/4X/6/0/c/60cb0eb100186e077caab97f635db1bde7f2b923.png)

Once the profile is complete, it will display that it is no longer recording

![](https://forum-cfx-re.akamaized.net/original/4X/1/1/8/118be3be7c82962942cbbc00d45af2c20bb916a5.png)

Viewing the Profiles
You can immediately view the capture using `profiler view`, which will open google chrome and begin loading the profile.

NOTE: Viewing profiles server side will not automatically load chrome, you will need to copy the provided link to chrome.

Saving a Profile
You can save a profile by using the command

`profiler saveJSON filename.json`

This will save a file to the folder where your run.bat file lives.

![](https://forum-cfx-re.akamaized.net/original/4X/3/6/1/361637fb8cba63d44418afa3f97369a3174c6af6.png)

Once you have saved the file, copy it to your computer into a folder you can navigate to easily and complete the following steps

- Open a new tab on Google Chrome

- Open the dev tools by pressing CTRL + SHIFT + I or `Settings > More Tools > Developer Tools`

- Select the `Performance` tab

![](https://forum-cfx-re.akamaized.net/original/4X/3/4/7/3478bad4516a59b45a161f72af303faeb6da60d5.png)

- Right click anywhere on the panel, and select `load profile`

![](https://forum-cfx-re.akamaized.net/original/4X/5/f/6/5f698e2c4181838375adf7cdfdad5fe2d73b223e.png)

- Navigate to the saved file, open it and continue the rest of the guide

**Reading the Profiles**

![](https://forum-cfx-re.akamaized.net/original/4X/8/b/4/8b433f899e6089b2a8f3e1498f3b876ab2cd5e48.png)

When you open the profile, you will be presented with a similar screen (I recommend adjusting the size to view it easier).

Starting from the top bar, we have the time stamp of the recording, followed by an FPS graph (green) and finally a CPU time graph (yellow, this one is important). This can be used to identify peaks, which correlate to frame drops / micro stuttering or server hitches.

Server Hitch Example
We can identify server hitches by sudden spikes in the CPU time, which exceed normal frames.

[![](https://forum-cfx-re.akamaized.net/original/4X/4/7/3/47337c19657cfc85463a15fe87755fcc24c68580.png)image887×57 6.99 KB](https://docs.fivem.net/uploads/short-url/a9ScLQOKEsDYuwdQqrfkop8udIQ.png?dl=1)

**Viewing Specific Frame Information**

Scrolling on the time bar will cause the whole display to zoom in on the specific period of time your cursor is hovering on. At this point, you will want to zoom in on specific frames, such as the one below.

![](https://forum-cfx-re.akamaized.net/original/4X/c/8/2/c822ba3e6ca08e80ab693279117ff55248b02c48.png)

The information above shows the recording timestamp, the total frame time (green section) and the script threads which executed that frame. Hovering over the frame time also displays average FPS at that time.

**Viewing the resource tick breakdown**

Next, zoom on the yellow resource tick event so we can identify what is exactly causing the FPS drop / loss.

[![](https://forum-cfx-re.akamaized.net/original/4X/4/5/6/456be283c7a1ad2ad1ebfd1350d964296ad44701.png)image822×70 5.5 KB](https://docs.fivem.net/uploads/short-url/9U85qQpUAxALaN24yl0HpsmPcZ3.png?dl=1)

In this example, I have a script named `debug` which has a problematic thread causing significant performance loss. Hovering over any of the events will outline how many ms it is taking to process this thread, and display the file and even line numbers of the thread causing problems.

In this example, it is located in a file called client.lua, on lines 29 to 34.

Hope this helps people, if you need a hand or better explanation of something with the profiler, comment or send me a DM and I will do my best to help
