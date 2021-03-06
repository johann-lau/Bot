# Purgepy and Purgeregex commands

## Introduction

The bot has two versatile purging commands, `purgepy` and `purgeregex`, which allows you to setup complex rules when purging messages. No more worries while purging.

This cheetsheet mainly aims at teaching regex/python newbies how to purge messages conveniently.

## Knowlege required

While being versatile, the commmands have high demands on your knowlege. You need to know how to write Python scripts or Regular Expression filters. **We recommend you to learn them since you won't need to rely on this cheatsheet, and Python and Regex themselves are useful for your life, too. However, if you only want a quick reference, you can refer to this cheatsheet.**

## Purgeregex (Regular Expression) Cheatsheet

##### Used for complex rules that only defines the content of the message.

Syntax: `=purgeregex [Number of messages to purge] [Regex]`

Recommended website: [Regex Cheatsheets and tutorials](https://regexr.com) 

### General knowlege

| To match this…  |Write this regex.|
|    :---:     |     :---:        |
|A digit| `\d`|
|A non-digit| `\D`|
|A whitespace| `\s`|
|A non-whitespace| `\S`|
|Any capital alphabet between A and S| `[A-S]`|
|Any alphabet between A and S| `[A-Sa-s]`|
|Any digit between 3 and 7| `[3-7]`|
|Either 'hi' or 'hello' or 'world'| `(hi\|hello\|world)`|
|Anything| `[\s\S]`|

### Usage
| To match this…  |Write this regex.|
|    :---:     |     :---:        |
|The word 'hello'|`[\s\S]*hello[\s\S]*`|
|The word 'hello' (but not case-sensitive)|`/[\s\S]*hello[\s\S]*/i`|
|A date in `DD-MM-YYYY` format<sup>[1](#footnote1)</sup>|`\d{2}\-\d{2}\-\d{4}`|
|The words 'bad', 'bed', 'bid', 'bod' or 'bud'|`b(a\|e\|i\|o\|u)d`|

<a name="footnote1">¹</a>: Note that however, this will match invalid dates, such as 99-30-2030 or 29-2-2013.

## Purgepy (Python) Cheatsheet

##### Used for complex rules when regex cannot satisfy your requirements.

Syntax: `=purgepy [Number of messages to purge] [Python script]`

Recommended article: [Full tutorial on discord.py module](https://discordpy.readthedocs.io/en/latest/api.html#message)

When using the following cheatsheets, remember to replace values inside {Curly Brackets} with their actual value! To copy something's ID, go to **User Settings › Appearance › Advanced › Developer Mode** and enable the option. Then, right click an format<sup>[object](#objectfootnote)</sup> and select "Copy ID".

<a name="objectfootnote">An "object" can be a role, user, server, channel, category, etc.</a>

### User and Roles

| To do this…  |Write this script.|
|    :---:     |     :---:        |
|Purge messages from specific user|`msg.author.id == {User id}`|
|Purge messages from users with role |`msg.author.roles.count(await msg.guild.get_role({Role id}))==1`|
|Purge messages from users with discriminator|`msg.author.discriminator=="{Discriminator, e.g. 1234}"`|
|Purge messages from bots|`msg.author.bot`|
|Purge messages from humans|`msg.author.bot==False`|
|Purge messages from users with nickname|`msg.author.display_name=="{Nickname}"`|
|Purge messages from users with nickname starting with something|`msg.author.display_name.startswith("{Something}")`|
|Purge messages from users with nickname ending with something|`msg.author.display_name.endswith("{Something}")`|
|Purge messages from users with nickname containing something|`msg.author.display_name.count("{Something}")>0`|
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
