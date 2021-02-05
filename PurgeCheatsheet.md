# Cheatsheet for Purgepy and Purgeregex commands

## Introduction

The bot has two versatile purging commands, `purgepy` and `purgeregex`, which allows you to setup complex rules when purging messages. No more worries while purging.

## Knowlege required

While being versatile, the commmands have high demands on your knowlege. You need to know how to write Python scripts or Regular Expression filters. **We recommend you to learn them, since you won't need to rely on this cheatsheet, and Python itself is useful for your life, too. However, if you just want quick reference, you can refer to this cheatsheet.**

## Purgepy (Python) Cheatsheet

##### Used for complex rules when regex cannot fullfill your requirements.

Recommended article: [Full tutorial](https://discordpy.readthedocs.io/en/latest/api.html#message) on discord.py module

When using the following cheatsheets, remember to replace values inside {Curly Brackets} with their actual value! To copy something's ID, go to **User Settings › Appearance › Advanced › Developer Mode**. Then, right click on an object and select "Copy ID".

### User and Roles

| To do this…  |Write this script.|
|    :---:     |     :---:        |
|Purge messages from specific user|`msg.author.id == {User id}`|
|Purge messages from users with roles |`msg.author.roles.count(await msg.guild.get_role({Role id}))==1`|
|Purge messages from users with discriminator|`msg.author.discriminator=="{Discriminator, e.g. 1234}"`|
|Purge messages from bots|`msg.author.bot`|
|Purge messages from humans|`msg.author.bot==False`|
|Purge messages from users with nickname|`msg.author.display_name=="{Nickname}"`|
|Purge messages from users without any nicknames|`msg.author.nick==None`|

### Logic
| To define this…  |Write this script.|
|    :---:     |     :---:        |
|Both statements are True|`{Statement 1} and {Statement 2}`|
|At least one statement is True|`{Statement 1} or {Statement 2}`|
|The opposite of a statement|`not {Statement}}`|

