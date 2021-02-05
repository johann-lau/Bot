# Cheatsheet for Purgepy and Purgeregex commands

## Introduction

The bot has two versatile purging commands, `purgepy` and `purgeregex`, which allows you to setup complex rules when purging messages. No more worries while purging.

## Knowlege required

While being versatile, the commmands have high demands on your knowlege. You need to know how to write Python scripts or Regular Expression filters. **We recommend you to learn them, since you won't need to rely on this cheatsheet and is useful for your life too. However, if you just want quick reference, you can refer to this cheatsheet.**

## Purgepy (Python) Cheatsheet

Recommended article: [Full tutorial](https://discordpy.readthedocs.io/en/latest/api.html#message)

|           To do this…             |      Write this script.      |
| :-------------------------------: | :---––-----------–---------: |
| Purge messages from specific user | `msg.author.id == {User id}` |
|     Purge messages with roles     | `msg.author.roles.count(await msg.guild.get_role({Role id}))==1`|
