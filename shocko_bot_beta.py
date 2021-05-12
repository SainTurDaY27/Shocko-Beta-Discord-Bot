import discord
from discord.ext import commands
import datetime
from datetime import datetime, timedelta
from urllib import parse, request
import re
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

message_last_seen = datetime.now()
message_last_seen2 = datetime.now()

client = commands.Bot(command_prefix="!", help_command=None)


@client.command()
async def help(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="All available bot commands", color=0xd4a935)
    emBed.add_field(name="!help", value="Get help command", inline=False)
    emBed.add_field(name="!ping", value="Display ping of Shocko", inline=False)
    emBed.add_field(name="!page", value="Display Shocko facebook page", inline=False)
    emBed.add_field(name="!test", value="Display previous word", inline=False)
    emBed.add_field(name="!user", value="Say 'Hi' to you", inline=False)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def ping(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="ping", value=f'Shocko Beta ping is at {round(client.latency * 1000)} ms!!!', inline=False)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def user(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="Hello!!!", value=str(ctx.author.name) + ". How are you ?", inline=False)
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def page(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="Facebook Page", value="https://www.facebook.com/Shockocoa/", inline=False)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def test(ctx, *, par):
    # emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    # emBed.add_field(name="", value="https://www.facebook.com/Shockocoa/", inline=False)
    # emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    # emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
    #                                                  "/841995594775658496/page_pro.png")
    # await ctx.channel.send(embed=emBed)
    await ctx.channel.send("You typed '{0}".format(par) + "'.")


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name="VALORANT", url="https://www.youtube.com/user/HEARTROCKERChannel"))
    print(f"Logged in as {client.user}")


@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")


@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")


@client.event
async def on_message(message):
    global message_last_seen, message_last_seen2
    if message.content == "hello":
        await message.channel.send("Hi!!!")
    elif message.content == "Who are you" and datetime.now() >= message_last_seen:
        message_last_seen = datetime.now() + timedelta(seconds=5)
        await message.channel.send("My name is " + str(client.user.name))
    elif message.content == "Who are you" and datetime.now() >= message_last_seen2:
        message_last_seen2 = datetime.now() + timedelta(seconds=5)
        await message.channel.send("His/Her name is " + str(client.user.name))
    await client.process_commands(message)


# still disable
@client.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


# still disable
@client.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(client.voice_clients, guild=ctx.guild)

    if voice_client is None:
        ctx.channel.send("Joined")
        await channel.connect()
        voice_client = get(client.voice_clients, guild=ctx.guild)

    YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "True"}
    FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}

    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info["formats"][0]["url"]
        voice_client.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice_client.is_playing()
    else:
        await ctx.channel.send("Already playing song")
        return


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

