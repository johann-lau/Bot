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

**invite** Invites the bot to your server.

### Discord Information

**server** Shows information about the current server.

**role [Role ID or Mention]** Shows information about the desired role.

**channel {Channel Name or ID}** Shows information about the desired channel.

**voicechannel [Channel Name or ID]** Shows information about the desired Voice Channel.

**user [User Name, Nickname, ID or Mention] [Channel Name, ID or Mention]** Shows information about the user in a specific channel. The arguments are optional.

**uservoice [User Name, Nickname, ID or Mention] [Channel Name or ID]** Shows information about the user in a specific voice channel.

**avatar {User Name, Nickname, ID or Mention}** Shows the avatar of the desired user.

**invitelink [Invite link or ID]** Shows information about the desired invite link.

**reactions [Message link or ID]** Shows reactions of a message.

**template [Template ID]** Shows information about the desired server template. This command is still in BETA.

### Discord

**embed [Arguments]** Generates an embed. One line for each argument. Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**pretend [User Name, Nickname, ID or Mention] [Text]** Pretends as a user and send something, using the magic of webhooks.

**pretendembed [Arguments]** Pretends as a user and generates an embed. One line for each argument.
Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

### Text Manipulation

**insert [Emoji] [Text]** Replaces the spaces in the text with emojis. Protip: also works with multiple emojis by wrapping all emojis in quotation marks. E.g. `=insert ":thumbsup: :heart:" I love this bot!` will return `I 👍 ❤️ love 👍 ❤️ this 👍 ❤️ bot!`

**spoiler [Text]** Generates an annoying spoiler.

**rawspoiler [Text]** Generates an annoying spoiler for you to copy and paste.

**rawrawspoiler [Text]** Similar to `rawspoiler`, but the recursion depth is 2 instead of 1.

**reverse [Text]** sesrever the provided text. E.g. `=reverse nggyu nglyd` will return `dylgn uyggn`.

**emoji [Text]** Generates emoji text. Supported characters: `A-Z a-z 0-9 ! ? $ # * + - × ÷`

### Moderation

**kick [User Name, Nickname, ID or Mention] {Reason}** Kicks the user. The Reason is optional.

**ban [User Name, Nickname, ID or Mention] {Reason}** Bans the user. The Reason is optional.

**slowmode [Delay] {Channel mentions}** Sets the slowmode to the delay. If there are no channel mentions, it will set the slowmode of the current channel.

**nick [New nickname]** Sets the nickname of the bot.

**purge [Number of messages]** Purges some messages in the current channel.

**purgeregex [Number of messages] [Regex rule]** Purges messages as long as the message matches the regular expression rule. Note: the bot will check for the most recent messages and delete exactly as many messages as [number of messages]. Starter: `=purgeregex 5 [\s\S]*john[\s\S]*` will delete 5 latest messages with small letters "john".

**purgepy [Number of messages] [Python boolean]** Purges messages as long as the message returns true in the python function. Note: the bot will check for the most recent messages and delete exactly as many messages as [number of messages]. Starter: `=purgepy 5 msg.author.id==123456789012345678` will delete 5 latest messages sent by someone with that user ID.

**purgepygex [Number of messages] [Regex rule] [Python boolean]** Purges messages as long as the message matches the regular expression rule and returns true in the python function. Note: the bot will check for the most recent messages and delete exactly as many messages as [number of messages].

### Information

**math [Formula]** Does boring math for you. Logical comparisons, scientific math, variables and user-defined functions are available. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**define [name] [definition] [arguments separated by spaces]** Defines a custom function. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**time {Timezone}** Checks the time in your timezone. If Timezone is not specified, you will see the UTC time.

**rtimer [Time to count] {Text}**
Starts a timer. Use `s` (seconds), `m` (minutes), `h` (hours), `d` (days) and `w` (weeks). If you specify a unit twice (e.g. `10s5s`), the last one will be used and the others will be omitted. Default to seconds if no unit is specified. The Text is optional."

**terminate [Timer ID]** Properly terminates a running timer generated by `rtime`. The Timer ID is a random 5-alphabet code that can be found at the beginning of a timer.

### Web and Developer

**screenshot [URL]** Screenshots the desired webpage. A regular-sized screenshot and a whole-webpage-sized screenshot will be shown.

**youtube [URL]** Downloads a youtube video and the captions. If the video size is larger than 8MB, only the captions will be uploaded.

**wiki [Query]** Finds a related Wikipedia article.

**engrave [Product] [Text]** Engraves the text on an Apple Product. Airpods, iPad, iPod and Apple Pencil are available. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#apple-engrave-help) for more information.

**ocr [Image]** Does an OCR scan for the image.

**text [PDF]** Turns the PDF to plain text.

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
- Phishing
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

`float()` explicitly makes the result a float number, i.e. a number with a decimal point.

`floor()` and `ceil()` rounds the number down/up to the closest integer

`round()` rounds the number to the closest integer.

#### Scientific Math
Function | Usage
:---:|:---:
`mod` or `%` | [Modulus](https://en.wikipedia.org/wiki/Modulo_operation)
`factorial()` | [Factorial](https://en.wikipedia.org/wiki/Factorial) e.g. factorial(5)=5×4×3×2×1
`sqrt()` or `√()` | [Square root](https://en.wikipedia.org/wiki/Square_root)
`sin()` `cos()` `tan()` | [Trigonometry](https://en.wikipedia.org/wiki/Trigonometry)
`asin()` `acos()` `atan()` | [Inverse trigonometry](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)
`gcd()` or `hcf()` \*| [Greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor)
`lcm()` \*| [Least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple)
`exp()` | [Exponential](https://en.wikipedia.org/wiki/Exponential_function)
`log(x, base)` | [Logarithm](https://en.wikipedia.org/wiki/Logarithm) base is optional, default to 10
`degrees()` `radians()` | Converts between degrees and radians

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

Use `=engrave {product name} {text}` to engrave text on a desired product. Here is a list of products and their respective colors:

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
