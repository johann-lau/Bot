import discord
from discord.ext import commands
import random as ra
import time
from datetime import datetime

client = discord.Client()
bot = commands.Bot(command_prefix='=')
bot.remove_command('help')

@bot.command()
async def help(ctx):
  ti="Tunnelers' Bot Help"
  desc="""**=admins**
  Show admins of the server.
  **Alias:** `=administrators`
  
  **=mods**
  Show mods of the server.
  **Alias:** `=moderators`
  
  **=random [lower] [upper]**
  Pick a pseudo-random number between the lower and upper numbers. If the provided numbers are not integers, they will be rounded off.
  
  **=spam [times to spam] [message to spam]**
  Spam the provided message.
  
  **=gsmrl**
  Shows information about GSMRL.
  
  **=tttl**
  Shows information about TTTL.
  """
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def time(ctx,timezone):
  now = datetime.now()
  current = now.strftime("%H:%M:%S")
  await ctx.send(current)

@bot.command()
async def timer(ctx,seconds):
  newsec=seconds
  newsec=newsec.replace("1",":one: ")
  newsec=newsec.replace("2",":two: ")
  newsec=newsec.replace("3",":three: ")
  newsec=newsec.replace("4",":four: ")
  newsec=newsec.replace("5",":five: ")
  newsec=newsec.replace("6",":six: ")
  newsec=newsec.replace("7",":seven: ")
  newsec=newsec.replace("8",":eight: ")
  newsec=newsec.replace("9",":nine: ")
  newsec=newsec.replace("0",":zero: ")

  if seconds=="1":
    desc=newsec+"second left"
  else:
    desc=newsec+"seconds left"
  message=await ctx.send(desc)
  seconds=str(int(seconds)-1)
  while seconds!="0":
    time.sleep(0.8)
    newsec=seconds
    newsec=newsec.replace("1",":one: ")
    newsec=newsec.replace("2",":two: ")
    newsec=newsec.replace("3",":three: ")
    newsec=newsec.replace("4",":four: ")
    newsec=newsec.replace("5",":five: ")
    newsec=newsec.replace("6",":six: ")
    newsec=newsec.replace("7",":seven: ")
    newsec=newsec.replace("8",":eight: ")
    newsec=newsec.replace("9",":nine: ")
    newsec=newsec.replace("0",":zero: ")
    if seconds=="1":
      desc=newsec+"second left"
    else:
      desc=newsec+"seconds left"
    await message.edit(content=desc)
    seconds=str(int(seconds)-1)
  await ctx.send("Countdown complete!")
    

@bot.command()
async def admins(ctx):
  embed=discord.Embed(title="Administrators", description="Admins on this server: Hume2, CalebJ, Coram.", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def administrators(ctx):
  embed=discord.Embed(title="Administrators", description="Admins on this server: Hume2, CalebJ, Coram.", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def mods(ctx):
  embed=discord.Embed(title="Moderators", description="Mods on this server: Josselin, sivarajan, Sokomine, onePlayer, Vikthor", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def moderators(ctx):
  embed=discord.Embed(title="Moderators", description="Mods on this server: Josselin, sivarajan, Sokomine, onePlayer, Vikthor", color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def random(ctx,lower,upper):
  ti="Random number between "+lower+" and "+upper
  lower=int(lower)
  upper=int(upper)
  rand=ra.randint(lower,upper)
  rand=str(rand)
  desc="Your random number is "+rand
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def spam(ctx,message,times):
  await ctx.channel.purge(limit=1)
  for count in range(0,int(times)):
    await ctx.send(message)

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        embed = discord.Embed(title=f"{user.name} was kicked.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        channel = client.get_channel(796721534676762664)
        await ctx.channel.send(embed=embed)
        embed = discord.Embed(title=f"You were kicked from the server.", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await user.send(embed=embed)

@bot.command()
async def gsmrl(ctx):
  ti="Grapeyard Superb Metro Rail Line (GSMRL)"
  desc="Basically Trains in Tunneler's Abyss(TA) is managed by TTTL (Tunneler's Train Transist Limited) project but, in Grapeyard Superb trains are managed by Grapeyard Superb Metro Train Limited(GSMRL) project. These projects are under taken by sivarajan and Hume2. Railway is essential part when it comes to traveling around TA."
  f1v="""Samson and Delilah. Laurel and Hardy. Holmes and Watson. Cheese and cucumber. These names could hardly fit together more naturally than Hume2 and Sivarajan, the latter the owner of the GSMRL company, the former his mentor and inspiration. GSMRL is by far the largest metro network in the Tunnelers' Abyss.

The first line, opened on October 12th 2019 by Hume2, connected the iconic Castle of Glass with Grapeyard Harbor. The indomitable duo opened a second line on November 22nd, and a third (the Narsh Express) on December 3rd.

On December 29th, and with generous assistance from InitialD and ModiJi, the fourth and fifth lines were revealed. Sivarajan constructed a sixth line (with ModiJi) on January 26th, 2020, a seventh line (with balancedAct) on April 10th, and an eighth assisted by tomracer and ShivTiwari on June 10th.

Sivarajan proclaims that this Herculean effort is far from complete. None less than the famous Sokomine, is currently occupied in constructing a Mountain Line."""
  embed=discord.Embed(title=ti,color=0x0061ff, url="https://h2mm.gitlab.io/web/rail.html", description=desc)
  embed.add_field(name="Story", value=f1v, inline=False)
  embed.set_image(url="https://h2mm.gitlab.io/web/screenshots/cog.jpg")
  await ctx.send(embed=embed)

@bot.command()
async def tttl(ctx):
  ti="Tunneler's Train Transist Limited (TTTL)"
  desc="Basically Trains in Tunneler's Abyss(TA) is managed by TTTL (Tunneler's Train Transist Limited) project but, in Grapeyard Superb trains are managed by Grapeyard Superb Metro Train Limited(GSMRL) project. These projects are under taken by sivarajan and Hume2. Railway is essential part when it comes to traveling around TA."
  f1v="""It was a bright spring morning when three weary travellers, refugees fleeing persecution in a faraway land, arrived at the dazzling natural spectacle we now know as Spawn, and decided to call it home.

These intrepid explorers - let us drink a toast to their names! Hume2, hip hip hurrah! CalebJ, hip hip hurrah! Coram, hip hip hurrah! - these intrepid explorers cared little for the basic comforts of life. Whereas lesser men would have occupied themselves in a search for food or shelter, it is said that our heroes spent the famous morning constructing the first railway platform.

Hume2 was quickly distracted by some bushes which produced berries exclusively in prime numbers, but CalebJ and Coram pressed on, hewing a tunnel through the mountains with their bare hands."""

  f2v="""Dreaming of a mighty train line stretching all the way to the far north, they discovered (to their dismay) that Spawn was surrounded by ocean in most directions. After tossing a coin, the track was extended to the west, where they found that Hume2, having decided that the prime number bushes were just a miraculous coincidence, had built a little wooden house. Thus, the town of Fractal Plains was born.

History does not record the names of the passengers on the first train journey to Fractal Plains, but it appears that on departure from Spawn, they all received a complimentary box of bananas."""

  f3v="""We are so used to modern technology, and trains that effortlessly pilot themselves from destination to destination, that it is difficult to imagine how primitive the early train network was. Stories abound of how CalebJ would trot in front of the moving train, waving a big red flag and yelling raucously, while Coram would wander up and down the line, sweeping away fallen apples and leaves with a big broom. This ad-hoc system was known as "Apple Tree Curtailment", or ATC (Automatic Train Control)for short. (In yet another coincidence, the modern system is also called ATC.)

It wasn't long before the competition was heating up. The existing line was extended as far as Red Erosion, while Hume2 began building a new line to the south(dragon Forest)

Hume2 was even more fiercely dedicated to Pure Logic than the original, and soon interlocking technology had been discovered, allowing trains to use the full length of the existing line, and effectively merging the two double tracks into one (the current S2 line)."""

  f4v="""Work soon began on new lines: a second line to Red Erosion, passing through Lava Oasis (S4), and another to the slightly mysterious Thorviss Farm, stopping at several even more mysterious locations (S5).

Around this date, the first train map appeared. Josselin has frequently claimed that a crack team of cartographers work long into the night to keep it updated, but occasional reports suggest the whole thing has been put together in MS Paint.

As news arrived of an idyllic settlement in the east, Grapeyard Superb, work on the celebrated Abyssal Express (S1) line commenced almost immediately. The area attracted an eclectic mix of builders, and soon the town (later re-classified as a city) was expanding rapidly. Meanwhile, the S2 line was extended all the way to Cody Island, this work apparently motivated by a desire for easier access to coconuts."""

  f5v="""With passenger numbers rising ever higher, a third line from Red Erosion was built, this time extending to the far north and stopping at Desert Trap (S3). In the opposite direction, the S1 line was re-routed to the far south, terminating at the world-famous invisible cliffs at Southern Cliff.

October 12th, 2019 was the date of the founding of the Grapeyard Superb metro (GSMRL). Its visionary chief engineer, Sivarajan, dreamed of uniting the disparate settlements along the Sakura Plains into one grand metropolis. Today his vision stands enacted as a metro system encompassing nearly thirty stations. Not content with that feat, Sivarajan and Hume2 established a settlement even further to the east. Narsh, or Legendria, can today be reached via the Narsh Express (R1) line."""

  f6v="""The existing line to Southern Cliff hugged the eastern side of the Poisson Mountains. An additional line (S6) was established along the western side. To help coordinate the construction efforts, Hume2 and Sivarajan built the TA Train transit office in Grapeyard. Around March 2020, the Abyssal Express was extended to Exfactor. Soon afterwards, the brand new S15 line connected little-explored territories between Coram Beach and Green Shore.

By April, and besieged by a mountain of passenger complaints, the decision was taken to re-name and re-number several lines. The trains themselves were modernised to more clearly show their line numbers and destinations. Alas, thrill-seeking passengers were still not entirely satisfied, so in July the average train speed across the network was greatly increased. R1 had been extended to Crystal Farm by Hume2, and the new R2 line was built to connect the charming seaside town of Will Beach with the rest of civilisation, later terminating at End of File station near Narsh."""

  f7v="""The newest line in the Tunnelers' Abyss is the S8, whose grand opening was the 28th September, 2020.Basically Trains in Tunneler's Abyss(TA) is managed by TTTL (Tunneler's Train Transist Limited) project but, in Grapeyard Superb trains are managed by Grapeyard Superb Metro Train Limited(GSMRL) project. These projects are under taken by sivarajan and Hume2. Railway is essential part when it comes to traveling around TA."""
  embed=discord.Embed(title=ti,color=0x0061ff, url="https://h2mm.gitlab.io/web/rail.html", description=desc)
  embed.add_field(name="⠀", value=f1v, inline=False)
  embed.add_field(name="⠀", value=f2v, inline=False)
  embed.add_field(name="⠀", value=f3v, inline=False)
  embed.add_field(name="⠀", value=f4v, inline=False)
  embed.add_field(name="⠀", value=f5v, inline=False)
  embed.add_field(name="⠀", value=f6v, inline=False)
  embed.add_field(name="⠀", value=f7v, inline=False)
  embed.set_image(url="https://h2mm.gitlab.io/web/screenshots/trainoffice.png")
  await ctx.send(embed=embed)

bot.run('TOKEN IS ENCLOSED')
