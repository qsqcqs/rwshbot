import discord
from discord.ui import Select, View

import os
from discord.ext import commands
from dotenv import load_dotenv
import discord.ui
import re
load_dotenv()
intents=discord.Intents.all()
client=commands.Bot(intents=intents)
slugcats = ['Survivor','Monk','Hunter','Artificer','Gourmand','Rivulet','Spearmaster','Saint','Sofanthiel','Nightcat']
iterators = ['Five Pebbles','Looks to the Moon','Seven Red Suns','No Significant Harassment', 'Sliver of Straw', 'Unparalleled Innocence', 'Chasing Wind']
flags = ['gayflag', 'lesbianflag', 'queerflag', 'straightflag']
dumbshitlist=['Survivor','Monk','Hunter','Artificer','Gourmand','Rivulet','Spearmaster','Saint','Sofanthiel','Nightcat','Five Pebbles','Looks to the Moon','Seven Red Suns','No Significant Harassment', 'Sliver of Straw', 'Unparalleled Innocence', 'Chasing Wind']
@client.event
async def on_ready():
    print(f'Successfully logged into Discord as "{client.user}"\nAwaiting user input...')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Rain World: Downpour Dating Sim"))

@client.slash_command()
async def kill(ctx: discord.ApplicationContext,argx,argy):
    if ctx.author.id == 625221549544177665:

        await ctx.response.send_message("PID " + str(os.getpid()) + " killed.")
        sys.exit()
@client.slash_command()
async def help(ctx: discord.ApplicationContext,argx,argy):
    await ctx.response.send_message("\'/kill\'")
    nickname = random.choice(['Sofanthiel', '???', 'Inv', 'Enot', 'Paincat'])
    await message.guild.get_member(client.user.id).edit(nick=nickname.upper())
@client.slash_command()
async def inv(ctx: discord.ApplicationContext,argx,argy,argz):
    nickname = random.choice(['Sofanthiel', '???', 'Inv', 'Enot', 'Paincat'])
    await message.guild.get_member(client.user.id).edit(nick=nickname.upper())
    if argx == "who":
        while len(re.findall("\swho(?=[\'\s])",argy)) != 0: 
            argx=re.sub('\swho(?=[\'\s])',dumbshitlist[random.randint(0,15)],'message.content',count=1)
        await ctx.response.send_message(argx)
    if argx == "www":
        if random.randint(0,1)==1:
            await ctx.response.send_message(f"In a fight betweeen {argy.lower()} and {arzz.lower()}. {argy.lower()} would win")
        else:
            await ctx.response.send_message(f"In a fight betweeen {argy.lower()} and {arzz.lower()}. {argz.lower()} would win")
    if argx == "crackship":
        if argy == "scug":
            lis=slugcats
        else:
            if argy == "iterators":
                lis=iterators
            else:
                return
        if len(argz) == 0:
            argz = flags[random.randint(0,3)]
        else:
            argz = (str(argz)+"flag")
        
        char1=lis[random.randint(0,len(lis-1))]
        char2=lis[random.randint(0,len(lis-1))]
        while char2==char1:
            char2=lis[random.randint(0,len(lis-1))]
        img1 = img1 = Image.open(f'1{char1.lower()}.png')
        img2 = Image.open(f'2{char2.lower}.png')
        img3 = Image.open(f'{argz}.png')
        imageoutput = Image.open("output.png")
        imageoutput.paste(img3,(0,0))
        imageoutput.paste(img2, (0,0), img2)
        imageoutput.paste(img1, (0, 0), img1)
        imageoutput.save("output.png")
        await ctx.response.send_message(f"{char1.lower()}x{char2.lower()}", file=discord.File('output.png'))


client.run(os.environ.get('DISCORD_TOKEN'))