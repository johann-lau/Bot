# Bot Documentation

## General description

SuperBot is a non-profit Discord bot. The purpose of creating the bot is to literally provide service to users. There are no premium plans, forced advertising or command cooldown. Computer resources are limited, please do not spam commands to allow others to access commands quickly.

Support hosting fees by [watching an ad](http://evolterr.com/1aza) or directly [support me on Patreon](https://www.patreon.com/user?u=48151089&fan_landing=true).

## Commands

### Basic Commands

**help {Command or Category}** Show a list of all commands.

**invite** Invites the bot to your server.

**prefix** Just in case you don't know the prefix of the bot (`=`), you can use @SuperBot as a prefix.

**ping** Checks the speed of the bot.

**speedtest** Does the `ping` command 5 times.

**botpurge [Number of messages]** Purges messages from the bot. Note: the bot will check for the most recent messages and delete exactly as many messages as [number of messages].

### Discord Information

**server** Shows information about the current server.

**invitelink [Invite link or ID]** Shows information about the invite link.

**role [Role ID or Mention]** Shows information about the role.

**channel {Channel Name or ID}** Shows information about the channel.

**voicechannel [Voice Channel Name or ID]** Shows information about the voice Channel.

**voicechannel [(Voice) Channel Name or ID]** Shows information about the text or voice Channel.

**user {User Name, Nickname, ID or Mention} {Channel Name, ID or Mention}** Shows information about the user. Specify the channel to show the permissions accurately.

**avatar {User Name, Nickname, ID or Mention}** Shows the avatar of a user.

**status {User Name, Nickname, ID or Mention}** Shows the status of a user.

**uservoice [User Name, Nickname, ID or Mention] [Voice Channel Name or ID]** Shows information about a user in the specific voice channel.

**leftuser [User ID]** Shows information about a user who is not in the server.

**message [Message Link or ID]** Shows information about a message.

**raw [Message Link or ID]** Shows the content of a message. Does not work with embeds yet.

**reactions [Message Link or ID]** Shows reactions of a message.

**emojiinfo [Emoji Name, ID or Usage]** Shows information about an custom emoji.

**template [Template ID]** Shows information about the server template. This command is still in BETA.

### Discord

**react [Message Link or ID] [Emoji Name, ID or Usage]** Temporarily reacts to the message with the custom emoji. Mostly used if you don't have nitro and would like to use an animated emoji.

**snipe {Argument}** Fetches the 5 recently deleted message. Use `disable` or `enable` as the argument to toggle sniping.

**clearsnipe** Clears the cache (information) of the snipe command.

**pretend [User Name, Nickname, ID or Mention] [Text]** Pretends as a user and send something, using the magic of webhooks.

**pretendembed [User Name, Nickname, ID or Mention] [Arguments]** Pretends as a user and generates an embed. One line for each argument.
Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**embed [Arguments]** Generates an embed. One line for each argument. Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**editembed [Arguments]** Edits an embed previously sent with `=embed`. Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**simpleembed [Title] {Description} {Image link} {field(s)}** A simplified version of `=embed`. One line for each argument. Use `{{{newline}}}` for a line break. For each field, 3 lines should be specified. The first is the title; the second is the description; the third is either `0` or `1` depending on whether you want inline or not. Additional information on embeds can be found [here](https://github.com/johann-lau/Bot#embed-message-help).

**ett [Message Link or ID]** Turns the embed of the message to SuperBot form. Basically a reverse of `=embed`.

### Text Manipulation

**poll [Options] [Title]** Starts a poll with no automation (yet). E.g. `=poll Great👍 Bad👎 What do you think about this server?`

**insert [Emoji] [Text]** Replaces the spaces in the text with emojis. Protip: also works with multiple emojis by wrapping all emojis in quotation marks. E.g. `=insert ":thumbsup: :heart:" I love this bot!` will return `I 👍 ❤️ love 👍 ❤️ this 👍 ❤️ bot!`

**spoiler [Text]** Generates an annoying spoiler.

**rawspoiler [Text]** Generates an annoying spoiler for you to copy and paste.

**rawrawspoiler [Text]** Similar to `rawspoiler`, but the recursion depth is 2 instead of 1.

**reverse [Text]** sesrever the provided text. E.g. `=reverse nggyu nglyd` will return `dylgn uyggn`.

**emoji [Text]** Generates emoji text. Supported characters: `A-Z a-z 0-9 ! ? $ # * + - × ÷`

### Moderation

**Most of these commands will not work if the relevant permissions are not granted to the bot.** Use `=user 796686363604680755` to check the granted permissions.

**kick [User Name, Nickname, ID or Mention] {Reason}** Kicks the user.

**ban [User Name, Nickname, ID or Mention] {Reason}** Bans the user.

**ban [User ID] {Reason}** Unbans the user.

**slowmode [Delay] {Channel mentions}** Sets the slowmode to the delay. If there are no channel mentions, it will set the slowmode of the current channel.

**purge [Number of messages]** Deletes messages in the current channel.

**purgeuser [Nubmer of messages] [User Name, Nickname, ID or Mention]** Deletes messages as long as the message returns true in the python function. Note: the bot will check for the most recent messages and delete exactly as many messages as [Number of messages].

**purgeregex [Number of messages] [Regex rule]** Deletes messages as long as the message matches the regular expression rule. Note: the bot will check for the most recent messages and delete exactly as many messages as [Number of messages]. Starter: `=purgeregex 5 [\s\S]*john[\s\S]*` will delete 5 latest messages with small letters "john".

**purgepy [Number of messages] [Python boolean]** Deletes messages as long as the message returns true in the python function. Note: the bot will check for the most recent messages and delete exactly as many messages as [Number of messages]. Starter: `=purgepy 5 msg.author.id==123456789012345678` will delete 5 latest messages sent by someone with that user ID.

**purgepygex [Number of messages] [Regex rule] [Python boolean]** Purges messages as long as the message matches the regular expression rule and returns true in the python function. Note: the bot will check for the most recent messages and delete exactly as many messages as [Number of messages].

**nick [New nickname]** Sets the nickname of the bot.

**makeinvite [Time until expiration] {Max. uses}** Creates an invite. Use `s` (seconds), `m` (minutes), `h` (hours), `d` (days) and `w` (weeks) for [Time until expiration]. If you specify a unit twice (e.g. `10s5s`), the last one will be used and the others will be omitted. Default to seconds if no unit is specified. Use `0` for {Max. uses} to indicate that an infinite amount of users can join with the link.

### Information

**colo(u)r [3 RGB values, 1 hex code or 1 decimal value]** Convert between colour formats. If you want to explicitly specify a hex code instead of a decimal value, add a hash `#` before the value. E.g. `=color 255 0 0`, `=color #ff0000` or `=color 16711680`

**simp(le)colo(u)r [Name of color/gradient]** View beautiful colours or gradients.

![Available colo(u)rs](/Colours001.jpeg)

**translate [Destination language] [Text]** Translate the text to the language.

**definition [Word]** Looks up the word in a dictionary.

**calc [Equation]** Does boring math for you. Logical comparisons, scientific math, variables and user-defined functions are available. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**define [Name] [definition] [arguments separated by spaces]** Defines a custom function. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**time {Timezone}** Checks the time in your timezone. If Timezone is not specified, you will see the UTC time.

**rtimer [Time to count] {Text}** Starts a timer. Use `s` (seconds), `m` (minutes), `h` (hours), `d` (days) and `w` (weeks) for [Time to count]. If you specify a unit twice (e.g. `10s5s`), the last one will be used and the others will be omitted. Default to seconds if no unit is specified.

**ttimer [Time to count] {Text}** Similar to `=rtimer`, but the timer is optimized for mobile users.

**terminate [Timer ID]** Properly terminates a running timer generated by `rtime`. The Timer ID is a random 5-alphabet code that can be found at the beginning of a timer.

**minecraft [Item]** Looks up an article in the Minecraft wiki.

### Web

**screenshot [URL] {Size}** Screenshots the webpage. If you don't specify "short" or "full" in the "size" argument, both a regular screenshot and a full screenshot will be shown.

**youtube [URL]** Downloads a youtube video.

**wiki [Query]** Finds a Wikipedia article.

**engrave [Product] [Text]** Engraves the text on an Apple Product. Airpods, iPad and more are available. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#apple-engrave-help) for more information.

**covid [Country]**

**population [Country]**

### Plotting and Drawing

**ascii [Text]** Renders an ASCII representation in three different fonts.

**table [Header] [Footer] [Regular rows]** In the arguments, items should be separated with a comma (and no spaces). Regular rows should be separated with lines. To specify a style, add the style and three bars, before header in the first line.

Styles: `markdown` `minimalist` `simple` `borderless` `ascii(borderless/box/compact/double/minimalist/simple)` `double(box/compact/thin_compact)` `thick(box/compact)` `thin (box/compact/double/thick/rounded/compact_rounded/double_rounded/thick_rounded)`

Values in brackets are optional sub-styles. Add an underscore between the parent style and sub-style, e.g. `ascii_borderless`. Example usage:

```
=table double_box|||Name,Price,Units,Total
,,,3200
Soda,1,300,300
Pizza,12,200,2400
Steak,25,20,500
```

**render [Upload an image]** Can you imagine that? Convert an image to a txt file.

**captcha [Text]** SuperBot can't solve what he made himself 😀

**pie/barv/barh [Numbers] [Labels] [Title]** Plots a pie chart, vertical bar chart or horizontal bar chart. Separate the numbers and labels with commas. E.g. `=pie/barv/barh 1,2,3 Small,Medium,Large Some random numbers`

**hist [Numbers] [Title]** Plots a histogram. Separate the numbers with commas. E.g. `=hist 1,2,1,1,2,3 Some random numbers`

**snow [Recursion]** Plots a Koch Snowflake. Specify a recursion between 0 and 10 (inclusive).

**mandelbrot** Plots a Mandelbrot set.

### Developer and Miscellaneous

**ocr [Image]** Does an OCR scan for the image.

**text [PDF]** Turns the PDF to plain text.

**html [Code]** Renders an HTML5 code snippet.

**md [Code]** Renders a markdown code snippet.

**regex [Origin] [Destination] [Text]** Substitutes regular expression matches in the text with the destination. Supports substitution flags (`\1` instead of `$1`)

**regsub [Regex rule] [Text]** Looks for regular expression matches in the text.

### Embed Message help
For the `embed` command, please add 11 lines to your message, as follows.

```
=embed Title of embed
Title URL
Description
Color
Author
Author URL
Author Image Link
Footer
Footer Image Link
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

For very simple setup, use the `simpembed` or `simpleembed` command.

```
=simpembed Title
Description
```

You may insert the three lines for fields, just as the `embed` command.

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
- The entire embed is limited to 6000 characters

### Python Help

Who doesn't like running Python scripts without leaving Discord? That's why we introduced our Python command. Use our python command to execute any code and see its result.

To avoid spamming, the result is truncated to a maximum of 10 lines. In addition, only selected modules can be imported.

If you participate in any of the following activities, you will be banned from using the bot.

- Illegal activities
- Hosting cloud services, e.g. other Discord bots
- Attempt to bypass any rule, ToS or Community Guidelines

### Math help

For technics: Any Python function in the math, cmath, numpy, random or default module is available.

From | Import as
:--: | :-------:
Math | N/A
Cmath | N/A
Numpy| np
Random | ra

#### Basic Arithmetic

Use `+`, `-`, `*`, `/`, `×`, `÷`, `^`, `**` to do basic arithmetic. (`**` is equal to `^`)

`float()` explicitly makes the result a float number, i.e. a number with a decimal point. E.g. `float(5)` will return `5.0`.

`floor()` and `ceil()` rounds the number down/up to the closest integer. E.g. `floor(5.9)` will return `5` and `ceil(5.1)` will return `6`.

`round()` rounds the number to the closest integer. E.g. `round(5.5)` will return `6`.

#### Scientific Math
Function | Usage | Example
:---:|:---:|:---:
`mod` or `%` | [Modulus](https://en.wikipedia.org/wiki/Modulo_operation) | `128%10`=8
`factorial()` | [Factorial](https://en.wikipedia.org/wiki/Factorial) | `factorial(5)`=5×4×3×2×1
`sqrt()` or `√()` | [Square root](https://en.wikipedia.org/wiki/Square_root) | `sqrt(144)`=12
`sin()` `cos()` `tan()` | [Trigonometry](https://en.wikipedia.org/wiki/Trigonometry) | -
`asin()` `acos()` `atan()` | [Inverse trigonometry](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) | -
`gcd()` or `hcf()` \*| [Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) | `gcd(10, 8)`=40
`lcm()` \*| [Least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple) | `lcm(28, 35)`=7
`exp()` | [Exponential](https://en.wikipedia.org/wiki/Exponential_function) | -
`log(x, base)` | [Logarithm](https://en.wikipedia.org/wiki/Logarithm) (The base is optional, default to 10) | -
`degrees()` `radians()` | Converts between degrees and radians | -

\* You can have as many arguments as you want in the parenthesis.

#### Comparisons and Logic Gates

Comparisons

Function | Meaning
:---:|:---:
`==` | Equal to
`!=` | Not equal to
`>` | Greater than
`<` | Smaller than
`>=` | Greater than or equal to
`<=` | Smaller than or equal to

Logic Gates

`and`, `or` and `not` are the only available logic gates.

#### Variable Assignment

To Assign a value to a variable, use `{variable} = {value}`. For example, to assign 3 to a, use `a = 3`.

You can assign multiple variables at once, for example, `a = b = c = sqrt(9)`.

#### Custom unctions

Do you want to make a convenient function that you can call easily? If yes, you can use custom functions!

First, you need to define the function. Its syntax is `=define {name} {definition} {arguments separated by spaces}`. If it was sucessful you will see a 👍 reaction.

For example, to define a function that adds two numbers together, use `=define add x+y x y`.

Now that you have defined some awesome functions, how do you use them? Simply use `=calc {function name}({arguments})`. To use the example add function, use `=calc add(1,2)` and you get 3.

### Apple Engrave Help

Use `=engrave {product name} {text}` to engrave text on a product. Here is a list of products and their respective colors:

|    Product    | Default Only |  Space Gray  | Silver |   Gold   | Rose Gold | Red | Pink | Green | Sky Blue |
|    :-----:    | :----------: | :----------: | :----: | :------: | :-------: | :-: | :--: | :---: | :------: |
|    Airpods    |      ✓       |              |        |          |           |     |      |       |          |
|   Airpods Pro |      ✓       |              |        |          |           |     |      |       |          |
|   Airpods Max |              |      ✓       |    ✓   |          |           |     |  ✓   |   ✓   |    ✓     |
|      iPad     |              |      ✓       |    ✓   |    ✓     |           |     |      |       |          |
|    iPad Pro   |              |      ✓       |    ✓   |          |           |     |      |       |          |
|    iPad Air   |              |      ✓       |    ✓   |          |     ✓     |     |      |   ✓   |    ✓     |
|    iPad Mini  |              |      ✓       |    ✓   |    ✓     |           |     |      |       |          |
|  iPod (Touch) |              |      ✓       |    ✓   |    ✓     |           |  ✓  |  ✓   |       |    ✓     |
|    Pencil     |      ✓       |              |        |          |           |     |      |       |          |

The product name is composed of the product and the color. For any product with only default color, the color shall be omitted. If the color is omitted on another product, it will be space gray by default.

Space gray can be aliased as gray; Gray can be aliased as grey; Rose gold can be aliased as rose; Gold can be aliased as golden; Sky blue can be aliased as blue.
