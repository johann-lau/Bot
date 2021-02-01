# Bot Documentation
## Commands

### Basic Commands

**help {Command or Category}** Show the help for a specific command/category. The command/category is optional.

**invite** Invites the bot to your server.

**ping** Checks the speed of the bot.

**speedtest** Does the `ping` command 5 times, thus more accurate.

### Discord Information

**server** Shows information about the current server.

**role [Role ID or Mention]** Shows information about the desired role.

**channel {Channel Name or ID}** Shows information about the desired channel.

**voicechannel [Channel Name or ID]** Shows information about the desired Voice Channel.

**user [User Name, Nickname, ID or Mention] [Channel Name, ID or Mention]** Shows information about the desired User in a specific channel. The arguments are optional.

**uservoice [User Name, Nickname, ID or Mention] [Channel Name or ID]** Shows information about the desired User in a specific voice channel.

**avatar {User Name, Nickname, ID or Mention}** Shows the avatar of the desired user.

**voicechannel [Invite link or ID]** Shows information about the desired invite link.

**template [Template ID]** Shows information about the desired server template. This command is still in BETA.

### Discord

**spam [Number of times to spam] [Text to spam]** Spams the text. It must be less than 30 times and without any mentions.

**embed [Arguments]** Generates an embed. One line for each argument. Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**pretend [User Name, Nickname, ID or Mention] [Text]** Pretends as a user and send something, using the magic of webhooks.

**pretendembed [Arguments]** Pretends as a user and generates an embed. One line for each argument.
Please check [here](https://github.com/johann-lau/Bot#embed-message-help) for more information.

**pretendspam [User Name, Nickname, ID or Mention] [Text]** Pretends as a user and spams the text. It must be less than 30 times and without any mentions.

### Text Manipulation

**insert [Emoji] [Text]** Replaces the spaces in the text with emojis. Protip: also works with multiple emojis by wrapping all emojis in quotation marks. E.g. `=insert ":thumbsup: :heart:" I love this bot!`

**spoiler [Text]** Generates an annoying spoiler.

**rawspoiler [Text]** Generates an annoying spoiler for you to copy and paste.

**reverse [Text]** sesrever the provided text.

**emoji [Text]** Generates emoji text. Supported characters: `A-Z a-z 0-9 ! ? $ # * + - × ÷`

### Moderation

**kick [User Name, Nickname, ID or Mention] {Reason}** Kicks a desired user. The Reason is optional.

**ban [User Name, Nickname, ID or Mention] {Reason}** Bans a desired user. The Reason is optional.

### Information

**math [Formula]** Does boring math for you. Logical comparisons, scientific math, variables and user-defined functions are available. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**define [name] [definition] [arguments separated by spaces]** Defines a custom function. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#math-help) for more information.

**time {Timezone}** Checks the time in your timezone. If Timezone is not specified, you will see the UTC time.

**rtimer [Time to count] {Text}**
Starts a timer. Use `s` (seconds), `m` (minutes), `h` (hours), `d` (days) and `w` (weeks). If you specify a unit twice (e.g. `10s5s`), the first one will be omitted. Default to seconds if no unit is specified. The Text is optional."

**terminate [Timer ID]** Properly terminates a running timer generated by `rtime`. The Timer ID is a random 5-alphabet code and can be found at the beginning of a timer.

**timer [Seconds] {Text}** Starts a timer. The Text is optional. **Alert: This command is outdated. Consider using** `rtimer` **instead.**

### Web and Developer

**screenshot [URL]** Screenshots the desired webpage. A regular-sized screenshot and a whole-webpage-sized screenshot will be shown.

**youtube [URL]** Downloads a youtube video and the captions. If the video size is larger than 8MB, only the captions will be uploaded.

**wiki [Query]** Finds a related Wikipedia article.

**engrave [Product] [Text]** Engraves the text on an Apple Product. Airpods, iPad, iPod and Apple Pencil are available. Please check [here](https://github.com/johann-lau/Bot/blob/main/README.md#apple-engrave-help) for more information.

**ocr [Image]** Does an OCR scan for the image.

**text [PDF]** Turns the PDF to plain text.

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

## Dyno disadvantages

Ever wanted to use Dyno to replace Tunnelers' Bot? Before you made your decision…

#### Branding

What happens when you use a command? Instead of only seeing the result, you also see a Dyno avatar… an advertisement… or a premium-only message. Remember - whenever you add a bot, you also advertise it. You are advertising Dyno. How to fix the problem? Use ad-free TA Bot.

#### Premium

Spend money on a bot? Don't be stupid, we already provided an alternative. Tunnelers' Bot is absolutely free for forever and there will not be additional charges. Not to surprise you, but I don't even accept donations. Huh?

#### Hosting problems

Dyno is slower in speed (often 200\~450 ms, can reach \~1660) while Tunnelers' Bot is quick (80\~100 ms, can reach \~200) when hosted. Even if TA bot is locally hosted it still gives \~300 ms speed. This is mainly because it is in a single server and doesn't have to deal with many simultaneous commands.

#### Third-party

Using a third-party bot means a bunch of disadvantages. You have no control over them and you cannot make them add or modify commands, or change the avatar or logo. The new commands might lead to problems. They don't have true 24/7 uptime which is crucial for spam management. Getting the bost independently hosted for a single server solves all these problems.

#### Slowmode

An annoying "A little quick here" message appears once you use the commands quickly. This is annoying when you want to purge messages or run a speedtest.

#### Better commands

Our bot features shorter commands but more context. Here you can see the comparison between server information commands for Dyno and TA Bot:

Feature | Dyno | TA Bot
:-----: | :--: | :----:
Icon | ✓ | ✓
Name | ✓ | ✓
Description |  | ✓
Created at | (✓) | ✓
Creator | ✓ | ✓
ID | ✓ | ✓
Voice Region  | ✓ | ✓
Categories | ✓ | ✓
Text Channels |  | ✓
Voice Channels |  | ✓
Roles | ✓ | ✓
Members |  | ✓
Max. bitrate |  | ✓
Max. filesize |  | ✓
Max. emojis |  | ✓
2FA for Moderation |  | ✓
Verification Level |  | ✓
Explict Content Filter |  | ✓
AFK Timeout |  | ✓
AFK Channel |  | ✓
Emojis |  | ✓
Community |  | ✓
Welcome Screen |  | ✓

Not convinced? Another comparison between user information commands:

Feature | Dyno | TA Bot
:-----: | :--: | :----:
Avatar | ✓ | ✓
Name | ✓ | ✓
Discriminator | ✓ | ✓
Registered at | (✓) | ✓
Joined at | (✓) | ✓
ID | ✓ | ✓
Human/Bot |  | ✓
Server Permissions |  | ✓
Channel Permissions |  | ✓
Status/Game |  | ✓
Roles | ✓ | ✓

Brackets between the tick means that the information is not accurate. For example, the time is not accurate to seconds.

Of course, the commands doesn't stop here. Superior Bot provides other commands (e.g. screenshot) which won't appear in **any other bot**. However, to make a conclusion, Superior Bot stuffs everything possible from the library, while Dyno picks the most "important" ones only.
