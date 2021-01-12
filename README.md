# Bot Documentation
## Commands
### Regular Commands
**help** Shows a help message.

**insert {Emoji} {Text}** Inserts the emoji every word, just 👍 like 👍 this 👍 one.

**spoiler {Text}** Adds a spoiler for every character of the text.

**reverse {Text}** Reverses the text.

**color {R G B} or {hex} or {decimal}** Searches for information about the color. Alias: `colour`

**pretend {User} {Text}** Pretends as the user and talk.

**spam {Times} {Text}** Spams the text for a number of times.

**embed {arguments}** Gives a custom embed. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#embed-message-help).

**embed {User} {arguments}** Pretends as a user and send a custom embed. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#embed-message-help).

**math {arguments}** Calculates a formula. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help).

### Tunnelers' Abyss

**admins** Lists all admins of the server.

**mods** Lists all moderators of the server.

**gsmrl** View information about GSMRL.

**tttl** View information about TTTL.

### Information Commands

**time {timezone}** Shows the time in the timezone. Timezone can be a value between -14 and 14.

**timer {seconds} {optional text}** Counts the specified number of seconds.

### Embed Message help
For the `embed` command, please add 8 lines to your message, as follows.

```
=embed Title of embed
Title URL
Description
Color
Author
Author URL
Author Image Link
Footer
Thumbnail Image Link
Image Link
```
For the color, please input a decimal value from 0 to 16777215. Not sure which color? Use our `=color R G B` or `=color #hex` command to fetch the decimal value.

You might want to add fields to your embed. For every field, insert 3 lines to the bottom of your command.
```
Field Title
Field Description
Field Inline
```
Notice "Field Inline". If you set it to `true`, `y`, `yes` or `1`, it will be True. Else, it will be False. Making it True means that it can stick to other fields if applicable. This function is useless if you only have 1 field for your embed.

Inline is true for both fields

![IT](https://u.cubeupload.com/Johann/Screenshot20210108at.png)


Inline is false for at least one field

![IF](https://u.cubeupload.com/Johann/b16Screenshot20210108at.png)


#### Notes

Masked URLS can be done with `[Mask](URL)`, such as `[Google](https://google.com)`. This is only possible in embed or field descriptions.

If you leave a line empty, it will not be processed. If you leave the color empty, it will be considered as transparent.

To add a new line to embed or field descriptions, type `{{{newline}}}`.

#### Limits
There are certain character limits:

- Embed titles are limited to 256 characters
- Embed descriptions are limited to 2048 characters
- There can be up to 25 fields
- A field's name is limited to 256 characters and its description to 1024 characters
- The footer text is limited to 2048 characters
- The author name is limited to 256 characters

### Math help

#### Basic arithmetic

Use `+`, `-`, `*`, `/`, `×`, `÷`, `^`, `**` to do basic arithmetic. (`**` is equal to `^`)

#### Scientific math

Use `mod` or `%` to calculate [modulus](https://en.wikipedia.org/wiki/Modulo_operation).
