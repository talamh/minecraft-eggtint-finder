Minecraft egg tint finder
===============

When run for the first time this script downloads the official vanilla resource pack template for bedrock edition from here:
https://feedback.minecraft.net/hc/en-us/articles/4414295731725-Bedrock-Add-On-Templates

![alt text](https://github.com/talamh/minecraft-eggtint-finder/blob/main/screenshot1.png)

Once that is downloaded and cached, subsequent runs will print a list of the colors used to tint the spawn eggs.

![alt text](https://github.com/talamh/minecraft-eggtint-finder/blob/main/screenshot2.png)

The output is in a form that can be used in Minetest mods for example the mule egg texture can be created using:

`"(spawn_egg.png^[multiply:#1b0200)^(spawn_egg_overlay.png^[multiply:#51331d)"`


Requirements
------------
```bash
pip install Pillow
pip install rich
```

Useage
------------
```bash
python3 eggtints.py
```

