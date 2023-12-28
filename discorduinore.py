

slugcats = ['Survivor','Monk','Hunter','Artificer','Gourmand','Rivulet','Spearmaster','Saint','Sofanthiel','Nightcat']
iterators = ['Five Pebbles','Looks to the Moon','Seven Red Suns','No Significant Harassment', 'Sliver of Straw', 'Unparalleled Innocence', 'Chasing Wind']
flags = ['gayflag', 'lesbianflag', 'queerflag', 'straightflag']
dumbshitlist=['Survivor','Monk','Hunter','Artificer','Gourmand','Rivulet','Spearmaster','Saint','Sofanthiel','Nightcat','Five Pebbles','Looks to the Moon','Seven Red Suns','No Significant Harassment', 'Sliver of Straw', 'Unparalleled Innocence', 'Chasing Wind']
from math import sqrt

import os
import discord
from dotenv import load_dotenv
import random
import re
from PIL import Image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.all()
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Successfully logged into Discord as "{client.user}"\nAwaiting user input...')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Rain World: Downpour Dating Sim"))

@client.event
async def on_message(message):
    k=str(message.content)
    print(k)
    print(k[0:4])
    if k.find("inv!") != -1:
        
        nickname = ['Sofanthiel', '???', 'Inv', 'Enot', 'Paincat'][random.randint(0,4)]
        await message.guild.get_member(client.user.id).edit(nick=nickname)
        k=k[4:]
        print(k)
        if k == "help":
            print(dir(message))
            await message.channel.send("\`inv!who:replaces instances of who with char\ninv!who who did it -> artificer did it\ninv!www:who would win\ninv!www someone vs a cat -> (some garbage here) a cat would win\ninv!crackship:generates a ship\ninv!crackship lesbian scug -> someonexsomeone with a png\`")
            return
        if k[0:3] == "who":
            k=k[4:]+" "
            while len(re.findall("\s?who(?=[\b\'\s])",k)) != 0:
 
                k=re.sub('\s?who(?=[\b\'\s])'," "+dumbshitlist[random.randint(0,15)],k,count=1)    
            await message.channel.send(k)
            
            return
        
        if k[0:3] == "www":
            k=k[4:]
            s=k.find(" vs ")
            
            
               

            
            if random.randint(0,1)==1:
                await message.channel.send(f"In a fight betweeen {k[:s].lower()} and {k[s+4:].lower()}. {k[:s].lower()} would win")
            else:
                await message.channel.send(f"In a fight betweeen {k[:s].lower()} and {k[s+4:].lower()}. {k[s+4:].lower()} would win")
        if k[0:9] == "crackship":
            k=k[10:]
            # soi=random.randint(0,1)
            soi=0
            flag=random.randint(0,3)
            if k.find("scug")!=-1:
                soi=0
            # if k.find("iter")!=-1:
            #     soi=1
            if k.find("straight")!=-1:
                flag=3
            if k.find("lesbian")!=-1:
                flag=1
            if k.find("gay")!=-1:
                flag=0
            if k.find("queer")!=-1:
                flag=2
            i=["gayflag","lesbianflag","queerflag","straightflag"][flag]
            if soi==0:
                lis=slugcats
            if soi==1:
                lis=iterators
            char1=lis[random.randint(0,len(lis)-1)]
            char2=lis[random.randint(0,len(lis)-1)]
            while char2==char1:
                char2=lis[random.randint(0,len(lis-1))]
            print(f"1{char2.lower()}")
            img1 = img1 = Image.open(f'1{char1.lower()}.png')
            
            img2 = Image.open(f'2{char2.lower()}.png')
            img3 = Image.open(f'{i}.png')
            imageoutput = Image.open("output.png")
            imageoutput.paste(img3,(0,0))
            imageoutput.paste(img2, (0,0), img2)
            imageoutput.paste(img1, (0, 0), img1)
            imageoutput.save("output.png")
            await message.channel.send(f"{char1.lower()}x{char2.lower()}", file=discord.File('output.png'))
            return
        if k[0:2]=="sd":
            k=k[3:]
            usw=eval(open("thrpre.txt","r").read())
            x=0
            cn=0
            while x<len(usw):
                cn=cn+usw[x][1]
                x=x+1
            cn=cn/len(usw)
            x=0
            ck=0
            while x<len(usw):
                ck=ck+(usw[x][1]-cn)**2
                x=x+1
            x=0
            while x<len(usw):
                if k.find(usw[x][0]) != -1:
                    i=x
                x=x+1
            
            await message.channel.send((usw[i][1]-cn)/sqrt(ck/len(usw)))
client.run(TOKEN)

