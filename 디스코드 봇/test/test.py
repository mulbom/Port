import asyncio

import discord

from discord.ext import commands

@commands.command(aliases=['입장'])
    async def join(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            await ctx.send(f"지금 {channel.name} 채널로 갈게요.")
            try:
                if ctx.voice_client is not None:
                    await ctx.voice_client.move_to(channel)
                else:
                    await channel.connect()
                print("음성 채널 정보:", ctx.author.voice)
                print("음성 채널 이름:", ctx.author.voice.channel)
            except Exception as e:
                print("에러 발생:", e)
                await ctx.send("채널에 연결하는 중에 오류가 발생했습니다.")
        else:
            await ctx.send("어디에 계신지 모르겠어요.")

@commands.command(aliases=['나가기'])
    async def out(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
            await ctx.send("안녕히 계세요.")
        else:
            await ctx.send("이미 밖이에요")


@bot.event
async def on_ready():
    await discord.client.change_presence(status=discord.Status.online, activity=discord.Game("궁시렁 대기"))
    print("봇 실행됨!")
    print(discord.client.user.name)
    print(discord.client.user.id)

# 이벤트 핸들러
@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요!')

@client.command()
async def 종료(ctx):
    await ctx.send("봇을 종료합니다.")
    await client.close()

async def main():
    async with bot:
        await bot.start(Token)
        
client.run('사용할 봇의 토큰 값을 입력해주세요.')
