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

For technics: Any Python function in the math module or default is available.

#### Basic Arithmetic

Use `+`, `-`, `*`, `/`, `×`, `÷`, `^`, `**` to do basic arithmetic. (`**` is equal to `^`)

`float()` explicitly makes the result a float number, i.e. a number with a decimal point.

`floor()` and `ceil()` rounds the number down/up to the closest integer.

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

#### Lists

Lists are wrapped in square brackets and elements are separated by commas. An example list can be `[1, 2, 3]`.

To extract the n-1 th element from a list, use `{List}[{n}]`. An example can be `[1, 2, 4, 8, 16][3] = 8`.
