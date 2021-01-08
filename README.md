# Bot Documentation
## Commands
### Regular Commands
**help** Shows a help message.

**insert {Emoji} {Text}** Inserts the emoji every word, just 👍 like 👍 this 👍 one.

**spoiler {Text}** Adds a spoiler for every character of the text.

**reverse {Text}** Reverses the text.

**embed** Gives a custom embed. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#embed-message-help).
### Tunnelers' Abyss

### Embed Message help
For the `embed` command, please add at least 7 lines to your message, as follows.

```
=embed Title of embed
Title URL
Description
Author
Author URL
Author Image Link
Footer
```

You might want to add fields to your embed. For every field, insert 3 lines to the bottom of your command.
```
Field Title
Field Description
Field Inline
```
Notice "Field Inline". If you set it to `true`, `y`, `yes` or `1`, it will be True. Else, it will be False. Making it True means that it can stick to other fields if applicable. This function is useless if you only have 1 field for your embed.

Inline is true for both fields

![IT](https://u.cubeupload.com/Johann/Screenshot20210108at.png =250x)


Inline is false for at least one field

![IF](https://u.cubeupload.com/Johann/b16Screenshot20210108at.png =250x)
