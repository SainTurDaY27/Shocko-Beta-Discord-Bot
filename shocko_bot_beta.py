import asyncio
import random
import discord
from discord.ext import commands
import datetime
from datetime import datetime, timedelta
from urllib import parse, request
import re
import youtube_dl
from random import choice

message_last_seen = datetime.now()
message_last_seen2 = datetime.now()

client = commands.Bot(command_prefix="!", help_command=None)


@client.command()
async def help(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot 1.0.1", description="All available bot commands", color=0xd4a935)
    emBed.add_field(name="`!help`", value="Get help command", inline=True)
    emBed.add_field(name="`!ping`", value="Display ping of Shocko", inline=True)
    emBed.add_field(name="`!page`", value="Display Shocko facebook page", inline=True)
    emBed.add_field(name="`!test (word)`", value="Display (word)", inline=True)
    emBed.add_field(name="`!user`", value="Say 'Hi' to you", inline=True)
    emBed.add_field(name="`!die`", value="Test respond of Shocko Beta", inline=True)
    emBed.add_field(name="`!clear (int)`", value="Clear previous (int) message", inline=True)
    emBed.add_field(name="`!play (url only)`", value="Play audio in your VC", inline=True)
    emBed.add_field(name="`!stop`", value="Stop playing & leave VC", inline=True)
    emBed.add_field(name="`!server`", value="Show server information", inline=True)
    emBed.add_field(name="`!tictactoe (@p1)(@p2)`", value="Tic Tac Toe game. (!place (int)) to place", inline=True)
    emBed.add_field(name="`!credits`", value="Show credits information", inline=True)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    # description = str(ctx.guild.description)
    # owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    emBed = discord.Embed(
        title=name + " Server Information",
        description=" ",
        color=0xd4a935
    )
    emBed.set_thumbnail(url=icon)
    # emBed.add_field(name="Owner", value=owner, inline=True)
    emBed.add_field(name="Server ID", value=id, inline=True)
    emBed.add_field(name="Region", value=region, inline=True)
    emBed.add_field(name="Member Count", value=memberCount, inline=True)
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")

    await ctx.send(embed=emBed)


@client.command()
async def ping(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="ping", value=f'Shocko Beta ping is at {round(client.latency * 1000)} ms!!!', inline=True)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def user(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="Hello!!!", value=str(ctx.author.name) + ". How are you ?", inline=True)
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def page(ctx):
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="Facebook Page", value="https://www.facebook.com/Shockocoa/", inline=True)
    emBed.set_thumbnail(url='https://cdn.discordapp.com/attachments/841626021375246344/841995594775658496/page_pro.png')
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command()
async def test(ctx, *, par):
    # emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    # emBed.add_field(name="", value="You typed '`{0}`".format(par) + "'.", inline=False)
    # emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
    #                                                  "/841995594775658496/page_pro.png")
    # await ctx.channel.send(embed=emBed)
    await ctx.channel.send("You typed '`{0}`".format(par) + "'.")


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="Invalid command used. Use !help to view all commands.", inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="Please specify an amount of messages to delete. (like !clear 5)",
                        inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)


# @client.command()
# async def kick(ctx, member: discord.Member, *, reason=None):
#     await member.kick(reason=reason)


# @client.command()
# async def ban(ctx, member: discord.Member, *, reason=None):
#     await member.ban(reason=reason)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name="Making Shocko Beta", url="https://www.youtube.com/user/HEARTROCKERChannel"))
    print(f"Logged in as {client.user}")


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!')


@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")


# @client.event
# async def on_member_remove(member):
#     channel = discord.utils.get(member.guild.channels, name='general')
#     await channel.send(f'Welcome {member.mention}!')

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


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['Why have you brought my short life to an end?', 'I could have done so much more...',
                 'I have a friend, kill them instead!!']
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="Ohh!", value=choice(responses),
                    inline=True)
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `RK Coding`')
    await ctx.send('Thanks to `DiamondSlasher` for coming up with the idea')
    await ctx.send('Thanks to `KingSticky` for helping with the `?die` and `?creditz` command')
    await ctx.send('Thanks to `lozer`')
    await ctx.send('Thanks to `Robotic Nation` for server commands, Tic Tac Toe game')


@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="You are not connected to a voice channel.", inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
    emBed.add_field(name="Now playing", value="** ** {}".format(player.title), inline=True)
    emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                     "/841995594775658496/page_pro.png")
    await ctx.channel.send(embed=emBed)


@client.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="A game is already in progress! Finish it before starting a new one.",
                        inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)
        # await ctx.send("A game is already in progress! Finish it before starting a new one.")


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver:
                    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
                    emBed.add_field(name="Error!",
                                    value=mark + "wins!.",
                                    inline=True)
                    emBed.set_footer(text=f"{client.user}",
                                     icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                              "/841995594775658496/page_pro.png")
                    await ctx.channel.send(embed=emBed)
                    # await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
                    emBed.add_field(name="Error!",
                                    value="It's a tie!",
                                    inline=True)
                    emBed.set_footer(text=f"{client.user}",
                                     icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                              "/841995594775658496/page_pro.png")
                    await ctx.channel.send(embed=emBed)
                    # await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
                emBed.add_field(name="Error!",
                                value="Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.",
                                inline=True)
                emBed.set_footer(text=f"{client.user}",
                                 icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                          "/841995594775658496/page_pro.png")
                await ctx.channel.send(embed=emBed)
                # await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
            emBed.add_field(name="Error!",
                            value="It is not your turn.",
                            inline=True)
            emBed.set_footer(text=f"{client.user}",
                             icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                      "/841995594775658496/page_pro.png")
            await ctx.channel.send(embed=emBed)
            # await ctx.send("It is not your turn.")
    else:
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!",
                        value="Please start a new game using the !tictactoe command.",
                        inline=True)
        emBed.set_footer(text=f"{client.user}",
                         icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                  "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)
        # await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="Please mention 2 players for this command.",
                        inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)
        # await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="Please make sure to mention/ping players (ie. <@688534433879556134>).", inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)
        # await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="Please enter a position you would like to mark.", inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        await ctx.channel.send(embed=emBed)
        # await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        emBed = discord.Embed(title="Shocko Beta Bot", description="", color=0xd4a935)
        emBed.add_field(name="Error!", value="Please make sure to enter an integer.", inline=True)
        emBed.set_footer(text=f"{client.user}", icon_url="https://cdn.discordapp.com/attachments/841626021375246344"
                                                         "/841995594775658496/page_pro.png")
        # await ctx.send("Please make sure to enter an integer.")


client.run('bot token')
