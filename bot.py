import discord
from discord.ext import commands
import random as ra
import time as tm
from datetime import datetime
from discord_webhook import DiscordWebhook
from discord.ext.commands import *
from discord import Webhook, AsyncWebhookAdapter, RequestsWebhookAdapter
import json
import os
import aiohttp
import requests
from bs4 import BeautifulSoup
from PIL import Image
from urllib.request import urlopen
import re
hexstring_pattern = re.compile(r'#?([0-9A-F]{2})([0-9A-F]{2})([0-9A-F]{2})', re.IGNORECASE)

client = discord.Client()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("=" or "!"))
bot.remove_command('help')
typer=0

"""@bot.event
async def on_message(message):
  if autodel!=None and not(message.content.startswith("=")):
    tm.sleep(autodel)
    await message.channel.purge(limit=1)
    await bot.process_commands(message)
  return"""

@bot.command()
async def pretend(ctx, member : discord.Member, *, message):
  await ctx.channel.purge(limit=1)
  async with aiohttp.ClientSession() as session:
    #webhook = Webhook.from_url('https://discord.com/api/webhooks/797029335424434186/op96Pi7p-F4mGNWPUbMW5iKwUiQ1tPU_1p-9CkcVpzfrXLYhRMK6E--C0s1rG76BtX9m', adapter=AsyncWebhookAdapter(session))
    webhook = Webhook.partial(797029335424434186, 'op96Pi7p-F4mGNWPUbMW5iKwUiQ1tPU_1p-9CkcVpzfrXLYhRMK6E--C0s1rG76BtX9m', adapter=RequestsWebhookAdapter())
  await webhook.send(message, username=member.name, avatar_url=member.avatar_url)

@bot.command()
async def type(ctx):
  global typer
  if typer==0:
    channel=ctx.channel
    await ctx.send("Started typing")
    async with channel.typing():
      typer=1
      var=0
  else:
    typer=0
    await ctx.send("Stopped typing")

@bot.command()
async def embed(ctx,*,text):
  textlist=text.splitlines()
  embed=discord.Embed(title=textlist[0], url=textlist[1], description=textlist[2].replace("{{{newline}}}","\n"), color=int(textlist[3]))
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  embed.set_author(name=textlist[0], url=textlist[1], icon_url=textlist[2])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  textlist.remove(textlist[0])
  embed.set_footer(text=textlist[0])
  textlist.remove(textlist[0])
  for count in range(0,len(textlist)//3):
    if textlist[2].lower()=="y" or textlist[2].lower()=="yes" or textlist[2].lower()=="true" or textlist[2].lower()=="1":
      inl=True
    else:
      inl=False
    embed.add_field(name=textlist[0], value=textlist[1].replace("{{{newline}}}","\n"), inline=inl)
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
    textlist.remove(textlist[0])
  await ctx.send(embed=embed)
  

@bot.command()
async def insert(ctx,emoji,*,text):
  text=text.replace(" "," "+emoji+" ")
  await ctx.send(text)

@bot.command()
async def purge(ctx,num):
  await ctx.channel.purge(limit=1)
  num=int(num)
  await ctx.channel.purge(limit=num)
"""@bot.command()
async def autodelete(ctx,num):
  isnum=num.isnumeric()
  if isnum:
    autodel=int(num)
    await ctx.send("Autodelete has been set to "+num+" seconds.")
  else:
    autodel=None
    await ctx.send("Autodelete has been disabled.")"""

@bot.command()
async def help(ctx,cat=None):
  if cat!=None:
    cat=cat.lower()
  ti="Commands: Tunnelers' Abyss"
  if cat=="ta":
    desc="""
  **admins**
  Show admins of the server.
  **Alias:** `=administrators`
  
  **mods**
  Show mods of the server.
  **Alias:** `=moderators`
  
  **gsmrl**
  Shows information about GSMRL.
  
  **tttl**
  Shows information about TTTL.
  """
  elif cat=="admins":
    ti="Admins"
    desc="""**=admins**
  Show admins of the server.
  **Alias:** `=administrators`"""
  elif cat=="admins":
    ti="Admins"
    desc="""**=admins**
  Show admins of the server.
  **Alias:** `=administrators`"""
  else:
    ti="Tunnelers' Bot Help"
    desc="""
  Prefix: =
  
  Commands available:
  `admins` `emoji` `gsmrl` `kick` `mods` `random` `reverse` `role` `spam` `spoiler` `time` `timer` `tttl`
  """
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(embed=embed)

@bot.command()
async def color(ctx,arg1,arg2=None,arg3=None):
  arg1=arg1.lower()
  if arg2==None and arg3==None:
    arg1=arg1.lstrip("#")
    if len(arg1)==6 and (arg1.count("1")+arg1.count("2")+arg1.count("3")+arg1.count("4")+arg1.count("5")+arg1.count("6")+arg1.count("7")+arg1.count("8")+arg1.count("9")+arg1.count("a")+arg1.count("b")+arg1.count("c")+arg1.count("d")+arg1.count("e")+arg1.count("f")+arg1.count("0")==6):
      hexc=(str(arg1))
      desc="Hex: #"+hexc
      deci=int(hexc, 16)
      rgb=tuple(int(hexc[i:i+2], 16) for i in (0, 2, 4))
      rgb=str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])
    elif int(arg1)<=16777216:
      hexc=str(hex(int(arg1))).lstrip("0x")
      desc="Decimal: "+arg1
      rgb=tuple(int(hexc[i:i+2], 16) for i in (0, 2, 4))
      rgb=str(rgb[0])+","+str(rgb[1])+","+str(rgb[2])
      deci=int(arg1)
    else:
      await ctx.send("Please specify a correct color value.")
  elif int(arg1)>=0 and int(arg1)<=256 and int(arg2)>=0 and int(arg2)<=256 and int(arg3)>=0 and int(arg3)<=256:
    hexc='#%02x%02x%02x' % (int(arg1), int(arg2), int(arg3))
    desc="RGB: "+arg1+","+arg2+","+arg3
    rgb=arg1+","+arg2+","+arg3
    hexc=(str(hexc))[1:]
    deci=int(hexc, 16)
  else:
    await ctx.send("Please specify a correct color value.")
    return
  ti="Color information"
  embed=discord.Embed(title=ti, description=desc, color=deci)
  embed.add_field(name="RGB", value=rgb, inline=True)
  embed.add_field(name="Hex Code", value="#"+hexc, inline=True)
  embed.add_field(name="Decimal Value", value=deci, inline=True)
  embed.set_image(url="https://htmlcolors.com/color-image/"+hexc+".png")
  await ctx.send(embed=embed)
  
@bot.command()
async def colour(ctx, arg1, arg2=None, arg3=None):
    args = arg1, arg2, arg3
    match = hexstring_pattern.fullmatch(arg1)
    if match:
        desc = f'Hex: {arg1}'
        r, g, b = (int(val, 16) for val in match.groups())

    elif all(arg and arg.isdigit() and 0 <= int(arg) < 256 for arg in args):
        desc = f'RGB: {arg1},{arg2},{arg3}'
        r, g, b = map(int, args)

    elif arg1.isdigit() and 0 <= int(arg1) < 2 ** 24:
        # note that the first pattern can match some entries of this type, and and cause a bug.
        # but the bug is really in the input specification, not my interpretation of your code
        desc = f'Decimal: {arg1}'
        n = int(arg1)
        r, g, b = n >> 16, (n >> 8) & 255, n & 255

    else:
        await ctx.send('Please specify a correct colour value.')
        return

    deci = (r << 16) + (g << 8) + b
    hex_ = f'{deci:02x}'.upper()

    embed = discord.Embed(title='Colour information', description=desc, color=deci)
    embed.add_field(name='RGB', value=f'{r},{g},{b}', inline=True)
    embed.add_field(name='Hex Code', value=f'#{hex_}', inline=True)
    embed.add_field(name='Decimal Value', value=deci, inline=True)
    embed.set_image(url=f'https://htmlcolors.com/color-image/{hex_}.png')
    await ctx.send(embed=embed)


@bot.command()
async def time(ctx,timezoneinput="0"):
  timezone=float(timezoneinput)
  if timezone>-15 and timezone<15:
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    h = float(h)+timezone//1-8
    m = timezone%1*60
    if h>=24:
      h=h-24
    if h<0:
      h=h+24
    hdis=str(int(h))
    if int(h)<10:
      hdis="0"+hdis
    mdis=str(int(m))
    if int(m)<10:
      mdis="0"+mdis
    current = "Time in UTC " + timezoneinput + " is `" + now.strftime(hdis+" : "+mdis+" : %S") + "`"
    await ctx.send(current)
  else:
    await ctx.send("Invalid timezone. Please try again.")

@bot.command()
async def spoiler(ctx,*,text):
  text="||||".join(text)
  text="||"+text+"||"
  await ctx.send(text)

@bot.command()
async def getprefix(bot, message):
    extras = await prefixes_for(message.guild) # returns a list
    return commands.when_mentioned_or(*extras)(bot, message)

@bot.command()
async def emojiinfo(ctx,emojiarg : discord.Emoji):
  ti="Emoji Info"
  desc=str(emojiarg)+emojiarg.name+"\ncreated by"+str(emojiarg.user)+"at"+str(emojiarg.created_at.strftime("%d %b, %Y (%a) %H:%M:%S"))
  embed=discord.Embed(title=ti, description=desc, color=0x0061ff)
  await ctx.send(desc)

@bot.command()
async def reverse(ctx,*,text):
  text = text[::-1]
  await ctx.send(text)

@bot.command()
async def emoji(ctx,*,newsec):
  newsec=newsec.replace(" ","   ")
  newsec=newsec.lower()
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
  newsec=newsec.replace("a","$_a: ")
  newsec=newsec.replace("b","$_b: ")
  newsec=newsec.replace("c","$_c: ")
  newsec=newsec.replace("d","$_d: ")
  newsec=newsec.replace("e","$_e: ")
  newsec=newsec.replace("f","$_f: ")
  newsec=newsec.replace("g","$_g: ")
  newsec=newsec.replace("h","$_h: ")
  newsec=newsec.replace("i","$_i: ")
  newsec=newsec.replace("j","$_j: ")
  newsec=newsec.replace("k","$_k: ")
  newsec=newsec.replace("l","$_l: ")
  newsec=newsec.replace("m","$_m: ")
  newsec=newsec.replace("n","$_n: ")
  newsec=newsec.replace("o","$_o: ")
  newsec=newsec.replace("p","$_p: ")
  newsec=newsec.replace("q","$_q: ")
  newsec=newsec.replace("r","$_r: ")
  newsec=newsec.replace("s","$_s: ")
  newsec=newsec.replace("t","$_t: ")
  newsec=newsec.replace("u","$_u: ")
  newsec=newsec.replace("v","$_v: ")
  newsec=newsec.replace("w","$_w: ")
  newsec=newsec.replace("x","$_x: ")
  newsec=newsec.replace("y","$_y: ")
  newsec=newsec.replace("z","$_z: ")
  newsec=newsec.replace("$_a",":regional_indicator_a")
  newsec=newsec.replace("$_b",":regional_indicator_b")
  newsec=newsec.replace("$_c",":regional_indicator_c")
  newsec=newsec.replace("$_d",":regional_indicator_d")
  newsec=newsec.replace("$_e",":regional_indicator_e")
  newsec=newsec.replace("$_f",":regional_indicator_f")
  newsec=newsec.replace("$_g",":regional_indicator_g")
  newsec=newsec.replace("$_h",":regional_indicator_h")
  newsec=newsec.replace("$_i",":regional_indicator_i")
  newsec=newsec.replace("$_j",":regional_indicator_j")
  newsec=newsec.replace("$_k",":regional_indicator_k")
  newsec=newsec.replace("$_l",":regional_indicator_l")
  newsec=newsec.replace("$_m",":regional_indicator_m")
  newsec=newsec.replace("$_n",":regional_indicator_n")
  newsec=newsec.replace("$_o",":regional_indicator_o")
  newsec=newsec.replace("$_p",":regional_indicator_p")
  newsec=newsec.replace("$_q",":regional_indicator_q")
  newsec=newsec.replace("$_r",":regional_indicator_r")
  newsec=newsec.replace("$_s",":regional_indicator_s")
  newsec=newsec.replace("$_t",":regional_indicator_t")
  newsec=newsec.replace("$_u",":regional_indicator_u")
  newsec=newsec.replace("$_v",":regional_indicator_v")
  newsec=newsec.replace("$_w",":regional_indicator_w")
  newsec=newsec.replace("$_x",":regional_indicator_x")
  newsec=newsec.replace("$_y",":regional_indicator_y")
  newsec=newsec.replace("$_z",":regional_indicator_z")
  newsec=newsec.replace("!",":exclamation:")
  newsec=newsec.replace("$",":heavy_dollar_sign:")
  newsec=newsec.replace("?",":question:")
  newsec=newsec.replace("#",":hash:")
  newsec=newsec.replace("*",":asterisk:")
  newsec=newsec.replace("+",":heavy_plus_sign:")
  newsec=newsec.replace("-",":heavy_minus_sign:")
  newsec=newsec.replace("×",":heavy_multiplication_x:")
  newsec=newsec.replace("÷",":heavy_division_sign:")
  await ctx.send(newsec)

@bot.command()
async def timer(ctx,seconds,*,Text=None):
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
    tm.sleep(0.8)
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
  if Text==None:
    await message.reply("Countdown complete!")
  else:
        await message.reply("Countdown complete! "+Text)


@bot.command()
async def getrole(ctx, member : discord.Member, role : discord.Role):
    
    roles=member.roles
    if roles.count(role)==1:
      await member.remove_roles(role)
      await ctx.send("Removed "+str(role)+" from "+str(member)+".")
    else:
      await member.add_roles(role)
      await ctx.send("Added "+str(role)+" to "+str(member)+".")

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
async def avatar(ctx,user: discord.Member=None):
  ti="Avatar"
  if user==None:
    user=ctx.author
  desc=f"Avatar of {user.mention}"
  embed=discord.Embed(title=ti,color=0x0061ff, description=desc)
  embed.set_image(url=user.avatar_url)
  await ctx.send(embed=embed)

@bot.command()
async def role(ctx,role: discord.Role=None):
  ti="Role Information: "+role.name
  if role==None:
    role=ctx.authortop_role
  desc=role.mention
  embed=discord.Embed(title=ti,color=role.color, description=desc)
  memberlist=role.members
  if len(memberlist)==0:
    f0v="No members assigned with "+role.name
  else:
    f0v=""
    for count in memberlist:
      f0v=f0v+count.name
  mention=role.mentionable
  if mention:
    f1v="Mentionable"
  else:
    f1v="Not mentionable"
  f1v=f1v+"""
  Mention: `<&"""+str(role.id)+">`"
  hoisted=role.hoist
  if hoisted:
    f2v="Yes"
  else:
    f2v="No"
  f3v=role.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f4v=role.id
  f5v=role.position
  f6v=role.color
  embed.add_field(name="Mentions", value=f1v, inline=True)
  embed.add_field(name="Members", value=f0v, inline=True)
  embed.add_field(name="Displayed separately?", value=f2v, inline=True)
  embed.add_field(name="Role ID", value=f4v, inline=True)
  embed.add_field(name="Position in hierarchy", value=f5v, inline=True)
  embed.add_field(name="Color", value=f6v, inline=True)
  embed.add_field(name="Created at", value=f3v, inline=True)
  if role.is_integration():
    f7v="This role is managed by an integration, such as a bot."
    embed.add_field(name="Integration", value=f7v, inline=False)
  #embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def user(ctx,user: discord.Member=None, channel: discord.TextChannel=None):
  ti="User Information"
  if user==None:
    user=ctx.author
  if channel==None:
    channel=ctx.channel
  bot=user.bot
  if bot==True:
    desc=f"{user.mention} (bot) "
  else:
    desc=f"{user.mention} (human) "
    embed=discord.Embed(title=ti,color=user.color, description=desc)
  embed.set_thumbnail(url=user.avatar_url)
  if user.name==user.display_name:
    f0v=user.name+"#"+user.discriminator
  else:
    f0v=user.name+"#"+user.discriminator+"  a.k.a. "+user.display_name
  f1v=user.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  allroles=user.roles
  f3v="⠀⠀"
  if user.permissions_in(ctx.channel).administrator:
    f3v=f3v+"Admin, "
  if user.permissions_in(ctx.channel).manage_guild:
    f3v=f3v+"Manage Server, "
  if user.permissions_in(ctx.channel).manage_roles:
    f3v=f3v+"Manage Roles, "
  if user.permissions_in(ctx.channel).administrator:
    f3v=f3v+"Manage Permissions, "
  if user.permissions_in(ctx.channel).view_audit_log:
    f3v=f3v+"View Audit Logs, "
  if user.permissions_in(ctx.channel).view_guild_insights:
    f3v=f3v+"View Server Insights, "
  if user.permissions_in(ctx.channel).kick_members:
    f3v=f3v+"Kick Members, "
  if user.permissions_in(ctx.channel).ban_members:
    f3v=f3v+"Ban Members, "
  if user.permissions_in(ctx.channel).manage_nicknames:
    f3v=f3v+"Manage Nicknames, "
  if user.permissions_in(ctx.channel).manage_webhooks:
    f3v=f3v+"Manage Webhooks, "
  if user.permissions_in(ctx.channel).manage_emojis:
    f3v=f3v+"Manage Emojis, "
  if user.permissions_in(ctx.channel).manage_nicknames:
    f3v=f3v+"Change Nickname, "
  if user.permissions_in(ctx.channel).mention_everyone:
    f3v=f3v+"Mention Everyone, "
  if user.permissions_in(ctx.channel).create_instant_invite:
    f3v=f3v+"Create Invite, "
  f3v=f3v[:-2]
  f3vb="⠀"
  if user.permissions_in(ctx.channel).view_channel:
    f3vb=f3vb+"View Channel, "
  if user.permissions_in(ctx.channel).read_messages:
    f3vb=f3vb+"Read Messages, "
  if user.permissions_in(ctx.channel).read_message_history:
    f3vb=f3vb+"Read Message History, "
  if user.permissions_in(ctx.channel).send_messages:
    f3vb=f3vb+"Send Messages, "
  if user.permissions_in(ctx.channel).send_tts_messages:
    f3vb=f3vb+"Send TTS Messages, "
  if user.permissions_in(ctx.channel).add_reactions:
    f3vb=f3vb+"Add Reactions, "
  if user.permissions_in(ctx.channel).external_emojis:
    f3vb=f3vb+"External Emojis, "
  if user.permissions_in(ctx.channel).attach_files:
    f3vb=f3vb+"Attach Files, "
  if user.permissions_in(ctx.channel).embed_links:
    f3vb=f3vb+"Embed Links, "
  f3vb=f3vb[:-2]
  f4v=""
  if len(allroles)>1:
    for count in allroles:
      if count.position!=0:
        f4v=f4v+count.mention+"⠀"
  else:
    f4v="No roles"
  """prof=profile(user)
  if prof.nitro:
    f5v="Nitro since "
    f5v=f5v+prof.premium_since.strftime("%d %b, %Y (%a) %H:%M:%S")
  else:
    f5v="No Nitro subscriptions"""
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Registered", value=f1v, inline=True)
  embed.add_field(name="Joined", value=f2v, inline=True)
  embed.add_field(name="Server Permissions", value=f3v, inline=False)
  embed.add_field(name="Channel Permissions", value=f3vb, inline=False)
  #embed.add_field(name="Voice Permissions", value=f3vc, inline=False)
  embed.add_field(name="Roles", value=f4v, inline=True)
  #embed.add_field(name="Nitro", value=f5v, inline=True)
  #embed.add_field(name="User", value=f6v, inline=True)
  #embed.add_field(name="", value=f7v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def uservoice(ctx,channel: discord.VoiceChannel, user: discord.Member=None):
  ti="User Information"
  if user==None:
    user=ctx.author
  bot=user.bot
  if bot==True:
    desc=f"{user.mention} (bot) "
  else:
    desc=f"{user.mention} (human) "
    embed=discord.Embed(title=ti,color=user.color, description=desc)
  embed.set_thumbnail(url=user.avatar_url)
  if user.name==user.display_name:
    f0v=user.name+"#"+user.discriminator
  else:
    f0v=user.name+"#"+user.discriminator+"  a.k.a. "+user.display_name
  f1v=user.created_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  f2v=user.joined_at.strftime("%d %b, %Y (%a) %H:%M:%S")
  allroles=user.roles
  f3v=""
  if user.permissions_in(channel).administrator:
    f3v=f3v+"Admin, "
  if user.permissions_in(channel).manage_guild:
    f3v=f3v+"Manage Server, "
  if user.permissions_in(channel).manage_roles:
    f3v=f3v+"Manage Roles, "
  if user.permissions_in(channel).administrator:
    f3v=f3v+"Manage Permissions, "
  if user.permissions_in(channel).view_audit_log:
    f3v=f3v+"View Audit Logs, "
  if user.permissions_in(channel).view_guild_insights:
    f3v=f3v+"View Server Insights, "
  if user.permissions_in(channel).kick_members:
    f3v=f3v+"Kick Members, "
  if user.permissions_in(channel).ban_members:
    f3v=f3v+"Ban Members, "
  if user.permissions_in(channel).manage_nicknames:
    f3v=f3v+"Manage Nicknames, "
  if user.permissions_in(channel).manage_webhooks:
    f3v=f3v+"Manage Webhooks, "
  if user.permissions_in(channel).manage_emojis:
    f3v=f3v+"Manage Emojis, "
  if user.permissions_in(channel).manage_nicknames:
    f3v=f3v+"Change Nickname, "
  if user.permissions_in(channel).mention_everyone:
    f3v=f3v+"Mention Everyone, "
  if user.permissions_in(channel).create_instant_invite:
    f3v=f3v+"Create Invite, "
  f3v=f3v[:-2]
  f3vc=""
  if user.permissions_in(channel).connect:
    f3vc=f3vc+"Connect, "
  if user.permissions_in(channel).speak:
    f3vc=f3vc+"Speak, "
  if user.permissions_in(channel).stream:
    f3vc=f3vc+"Video, "
  if user.permissions_in(channel).use_voice_activation:
    f3vc=f3vc+"Voice Activity, "
  if user.permissions_in(channel).priority_speaker:
    f3vc=f3vc+"Priority Speaker, "
  if user.permissions_in(channel).mute_members:
    f3vc=f3vc+"Mute Members, "
  if user.permissions_in(channel).deafen_members:
    f3vc=f3vc+"Deafen Members, "
  f3vc=f3vc[:-2]
  f4v=""
  if len(allroles)>1:
    for count in allroles:
      if count.position!=0:
        f4v=f4v+count.mention+"⠀"
  else:
    f4v="No roles"
  embed.add_field(name="Name", value=f0v, inline=False)
  embed.add_field(name="Registered", value=f1v, inline=True)
  embed.add_field(name="Joined", value=f2v, inline=True)
  embed.add_field(name="Server Permissions", value=f3v, inline=False)
  embed.add_field(name="Channel Permissions", value=f3vc, inline=False)
  embed.add_field(name="Roles", value=f4v, inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def spam(ctx,times,*,message):
  await ctx.channel.purge(limit=1)
  for count in range(0,int(times)):
    await ctx.send(message)

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
  embed.add_field(name="Story", value=f1v, inline=False)
  embed.add_field(name="⠀", value=f2v, inline=False)
  embed.add_field(name="⠀", value=f3v, inline=False)
  embed.add_field(name="⠀", value=f4v, inline=False)
  embed.add_field(name="⠀", value=f5v, inline=False)
  embed.add_field(name="⠀", value=f6v, inline=False)
  embed.add_field(name="⠀", value=f7v, inline=False)
  embed.set_image(url="https://h2mm.gitlab.io/web/screenshots/trainoffice.png")
  await ctx.send(embed=embed)


@bot.event
async def on_ready():
    activity = discord.Game(name="with TA members", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
    
bot.run('Token')
