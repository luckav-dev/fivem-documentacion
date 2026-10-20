# Part 4 - Placing Assets & Creating Simple Map Mods

> Fuente original: https://docs.fivem.net/docs/assets-manual/beginner-series/part-4/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

🎬 Vídeo de YouTube: https://www.youtube.com/watch?v=dVBO3_ZGL_Q

## What We'll Cover in This Part

- Placing assets in CodeWalker
- Creating simple map mods
- Basic mod structure overview

## Step 1: YMAP Creation

1. In the CodeWalker World View, navigate to the top-left corner, and open the project panel.
2. Once open, go to **File -> New -> Ymap File**.
3. Select your new YMAP in the project, and to add a new entity to it, go to **Ymap** at the top and click **New Entity**
4. You can now transform your entity as you wish.
5. Find the entity/model name you wish to place in the YMAP, and change the **Archetype** setting for the entity.
6. To duplicate entities, hold SHIFT and drag the 3D Gizmo.
7. Once you are happy with your YMAP, select it and click the **Calculate Extents** and **Calculate All Flags** buttons.
8. You can now save your YMAP file to your FiveM map resource. Ensure you name the file something that makes sense as good practice.
9. Next, in the project window, go to Tools -> Manifest Generator, then click Generate and save _manifest.ymf. This is necessary to load the models correctly.

## Step 2: FiveM Map Resource

1. Set up a new folder in your resources folder, for example, "map_mod".
2. Inside map_mod, create a new folder named "stream".
3. Create a new text file and name it "fxmanifest.lua".
4. Paste the following contents into your fxmanifest.lua file:

   ```lua
   fx_version 'cerulean'
   game 'gta5'
   lua54 'yes'
   this_is_a_map 'yes'
   ```

5. Move any game asset files into the stream folder to ensure the files load properly.
6. Make sure your new resource is included in your server configuration file.
