# Cheatsheet for Purgepy and Purgeregex commands

## Introduction

The bot has two versatile purging commands, `purgepy` and `purgeregex`, which allows you to setup complex rules when purging messages. No more worries while purging.

## Knowlege required

While being versatile, the commmands have high demands on your knowlege. You need to know how to write Python scripts or Regular Expression filters. **We recommend you to learn them, since you won't need to rely on this cheatsheet, and Python itself is useful for your life, too. However, if you just want quick reference, you can refer to this cheatsheet.**

## Purgeregex (Regular Expression) Cheatsheet

##### Used for complex rules that only defines the content of the message.

Recommended article: [Regex Cheatsheets and tutorials](https://regexr.com) 

### General knowlege

| To match this…  |Write this regex.|
|    :---:     |     :---:        |
|A digit| `\d`|
|A non-digit| `\D`|
|A whitespace| `\s`|
|A non-whitespace| `\S`|
|Anything| `[\s\S]`|

### Usage
| To match this…  |Write this regex.|
|    :---:     |     :---:        |
|The word 'hello'|`[\d\D]*hello[\d\D]*`|
|The word 'hello' (but not case-sensitive)|`/[\d\D]*fuck[\d\D]*/i`|
|Any alphabet between i and p |`[d\D]*[i-p][\d\D]*`|
|A date in `DD-MM-YYYY` format<sup>[1](#myfootnote1)</sup>|`\d{2}\-\d{2}\-\d{4}`|
|The words 'bad', 'bed', 'bid', 'bod' or 'bud'|`b{a|e|i|o|u}d`|

<a name="myfootnote1">1</a>: Note that however, this will match invalid dates, such as 99-30-2030 or 29-2-2013.

## Purgepy (Python) Cheatsheet

##### Used for complex rules when regex cannot fullfill your requirements.

Recommended article: [Full tutorial on discord.py module](https://discordpy.readthedocs.io/en/latest/api.html#message)

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
|Purge messages from users with nickname starting with something|`msg.author.display_name.startswith("{Something}")`|
|Purge messages from users with nickname ending with something|`msg.author.display_name.endswith("{Something}")`|
|Purge messages from users with nickname containing with something|`msg.author.display_name.count("{Something}")>0`|
|Purge messages from users without any nicknames|`msg.author.nick==None`|

### Message content
| To do this…  |Write this script.|
|    :---:     |     :---:        |
|Purge messages with attachment(s)|`len(msg.attachments)>0`|
|Purge messages with embed(s)|`len(msg.embeds)>0`|
|Purge messages with sticker(s)|`len(msg.stickers)>0`|
|Purge messages that mentions everyone|`msg.mention_everyone`|
|Purge messages that mentions someone|`len(msg.mentions)>0`|
|Purge messages that mentions at least 3 users|`len(msg.mentions)>=3`|
|Purge messages that mentions exactly 5 users|`len(msg.mentions)==5`|
|Purge messages that mentions a role|`len(msg.role_mentions)>0`|
|Purge pinned messages|`msg.pinned`|



### Logic
| To define this…  |Write this script.|
|    :---:     |     :---:        |
|Both statements are True|`{Statement 1} and {Statement 2}`|
|At least one statement is True|`{Statement 1} or {Statement 2}`|
|The opposite of a statement|`not {Statement}`|
