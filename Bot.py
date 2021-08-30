import discord
import asyncio
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '-')
token = "ODgxODQzOTU3NzY2NzA5MjQ4.YSyvLw.uzYMtYbi2H2qtxZYPc3V3oTsno8"
glist = ["자고있는중", "밥먹는중", "화장실감", "노는중", "누워있는중", "앉아있는중", "귀여움"]
game = discord.Game(glist[0])
version = discord.__version__

@client.event
async def on_ready():
    print(f"{client.user.name} 봇이 정상적으로 실행되었습니다")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!후추 정보"):
        embed = discord.Embed(title="후추", description=f"version : {version}")
        embed.add_field(name="현재 상태", value=glist[0])
        embed.set_footer(text="Bot Made by ☆고주원★", icon_url="https://cdn.discordapp.com/attachments/881538580370055228/881809110088155196/8f95ad6ffc562634.png")
        await message.channel.send(embed=embed)

    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description=f"채팅 {amount}개가\n{message.author}님의 요청으로 삭제 되었습니다", color=0x000000)
            embed.set_footer(text="Bot Made by ☆고주원★", icon_url="https://cdn.discordapp.com/attachments/881538580370055228/881809110088155196/8f95ad6ffc562634.png")
            await message.channel.send(embed=embed)
                
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send(f"{message.author.mention}, 당신은 명령어를 사용할 수 있는 권한이 없습니다")

    if message.content.startswith("!내 정보"):
        embed = discord.Embed(title=f"{message.author}", description=f"{message.author.mention}")
        embed.set_footer(text="Bot Made by ☆고주원★", icon_url="https://cdn.discordapp.com/attachments/881538580370055228/881809110088155196/8f95ad6ffc562634.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("!뽑기"):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            amount = message.content[4:]
            amount = amount.split()
            ran = random.choice(amount)
            await message.channel.send(ran)
        if i is False:
            await message.channel.send(f"{message.author.mention}, 당신은 명령어를 사용할 수 있는 권한이 없습니다")

    if message.content.startswith("!타이머"):
        s = int(message.content[5:])
        msg = await message.channel.send(s)
        while True:
            s -= 1
            await asyncio.sleep(1)
            await msg.edit(content=s)
            if s == 0:
                await message.channel.send("타이머 종료")
                break
                

client.run(token)