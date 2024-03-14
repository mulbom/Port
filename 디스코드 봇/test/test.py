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

@commands.command()
    async def play(self, ctx, *, url):
        """(사전 다운로드하지 않음)"""
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
                await ctx.send(f'현재 재생중: {player.title}')  # 이 줄을 try 블록 안으로 옮겼습니다
        except Exception as e:
            print("에러 : ", e)
            await ctx.send("음악을 재생하는 중에 오류가 발생했습니다.")

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused() or not ctx.voice_client.is_playing():
            await ctx.send("음악이 이미 일시 정지 중이거나 재생 중이지 않습니다.")

        ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client.is_playing() or not ctx.voice_client.is_paused():
            await ctx.send("음악이 이미 재생 중이거나 재생할 음악이 존재하지 않습니다.")

        ctx.voice_client.resume()

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
