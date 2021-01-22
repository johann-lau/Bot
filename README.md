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

For technics: Any Python function in the math, numpy, random or default module is available.

From | Import as
:--: | :-------:
Math | N/A
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

Category |    Product    | Default Only | (Space) Gray | Silver | Gold(en) | Rose Gold | Red | Pink | Green | Blue | Sky Blue
:------: |    :-----:    | :----------: | :----------: | :----: | :------: |           | :-: | :--: | :---: | :--: | :------:
 Airpods |    Airpods    |      ✓       |              |        |          |           |     |      |       |      | 
         |   Airpods Pro |      ✓       |              |        |          |           |     |      |       |      | 
         |   Airpods Max |              |      ✓       |    ✓   |          |           |     |  ✓   |   ✓   |  ✓   | 
  iPad   |      iPad     |              |      ✓       |    ✓   |    ✓     |           |     |      |       |      | 
         |    iPad Pro   |              |      ✓       |    ✓   |          |           |     |      |       |      | 
         |    iPad Air   |              |      ✓       |    ✓   |          |     ✓     |     |      |   ✓   |      |    ✓
         |    iPad Mini  |              |      ✓       |    ✓   |    ✓     |           |     |      |       |      | 
 Others  |  iPod (Touch) |              |      ✓       |    ✓   |    ✓     |           |  ✓  |  ✓   |       |  ✓   | 
         |    Pencil     |      ✓       |              |        |          |           |     |      |       |      | 

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

Brackets between the tick means that the information is not accurate.

Of course, the commands doesn't stop here. TA Bot provides other commands (e.g. screenshot) which won't appear in **any other bot**. However, to make a conclusion, TA Bot stuffs everything possible from the library, while Dyno picks the most "important" ones only.
