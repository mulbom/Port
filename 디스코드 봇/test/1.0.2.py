import asyncio
import discord
from datetime import datetime
import youtube_dl
from discord.ext import commands
import random

import requests
import json
#from googleapiclient.discovery import build



Token = "디스코드 봇 토큰"
youtube_dl.utils.bug_reports_message = lambda: ''

response = requests.get('웨더 api 키')
jsonObj = json.loads(response.text)

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
    'source_address': '0.0.0.0',
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

#youtubeApiKey = ""
#youtube = build('youtube', 'v3', developerKey=youtubeApiKey)

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


# 음악 재생 클래스. 커맨드 포함.
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
                embed = discord.Embed(
                    title="재생 시작",
                    description=f'현재 재생중: {player.title}',
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
        except Exception as e:
            print("에러 : ", e)
            await ctx.send("음악을 재생하는 중에 오류가 발생했습니다.")

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        embed = discord.Embed(
            title="볼륨 조절",
            description=f"볼륨을 {volume}%로 조절했어요.",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("가볼게요.")
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused() or not ctx.voice_client.is_playing():
            await ctx.send("음악이 멈춰져있거나 없어요.")

        ctx.voice_client.pause()
        embed = discord.Embed(
            title="일시 정지",
            description="음악을 일시 정지했어요.",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client.is_playing() or not ctx.voice_client.is_paused():
            await ctx.send("음악이 이미 재생 중이거나 재생할 음악이 없습니다.")

        ctx.voice_client.resume()
        embed = discord.Embed(
            title="재개",
            description="음악을 다시 재생합니다.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("음성 채널에 연결되어 있지 않아요.")
                raise commands.CommandError("음성 채널에 연결되어 있지 않음.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

    """@commands.command() # **youtube api**
    async def play(self, ctx, *, query):
        try:
            async with ctx.typing():
                video_url = await self.search_video(query)
                player = await YTDLSource.from_url(video_url, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
                await ctx.send(f'현재 재생중: {player.title}')
        except Exception as e:
            print("에러 : ", e)
            await ctx.send("실패")

    async def search_video(self, query):
        request = youtube.search().list(
            part='snippet',
            maxResults=1,
            q=query,  # 검색할 쿼리
            type='video'
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    """
class Alarm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.alarms = {}

    @commands.command()
    async def 알람(self, ctx, time: int):
        """알람을 설정합니다. 시간은 초 단위로 입력하세요."""
        if time <= 0:
            await ctx.send("양수의 시간을 입력해주세요.")
            return

        self.alarms[ctx.author.id] = time

        embed = discord.Embed(
            title="알람 설정",
            description=f"{time}초 후에 알람이 울립니다!",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

        await asyncio.sleep(time)

        embed = discord.Embed(
            title="알람",
            description="알람이 울렸습니다!",
            color=discord.Color.green()
        )
        await ctx.author.send(embed=embed)

        del self.alarms[ctx.author.id]
        

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!'):
            command = message.content[1:]
            embed = self.get_Ans(command)
            if embed:
                await message.channel.send(embed=embed)
    def get_Day(self):
        Daylist = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        Day = Daylist[datetime.today().weekday()]
        return Day

    def get_Date(self):
        return datetime.today().strftime("%Y년 %m월 %d일")

    def get_Time(self):
        return datetime.today().strftime("%H시 %M분")

    def get_Lotto(self):
        Lotto = [[0 for j in range(6)] for i in range(5)]
        for i in range(5):
            for j in range(6):
                Lotto[i][j] = self.unique_Number(Lotto, i, j)
        return Lotto

    def unique_Number(self, Lotto, row, col):
        number = random.randint(1, 45)
        while self.Duplicate(Lotto, row, col, number):
            number = random.randint(1, 45)
        return number

    def Duplicate(self, Lotto, row, col, number):
        for i in range(row):
            if Lotto[i][col] == number:
                return True
        return False

    def send_Lotto(self, Lotto):
        Lotto_Num = "\n"
        for i in range(5):
            for j in range(6):
                Lotto_Num += str(Lotto[i][j]) + "\n" if j == 5 else str(Lotto[i][j]) + ", "
        return Lotto_Num

    def get_Weather(self):
        weather = '\n'
        if 'current' in jsonObj and 'temp_c' in jsonObj['current'] and 'condition' in jsonObj['current'] and 'text' in \
                jsonObj['current']['condition']:
            weather += ('기온은 ' + str(jsonObj['current']['temp_c']) + '도이며, 날씨는 ' + jsonObj['current']['condition']['text'] + '입니다.')
        else:
            weather += ("날씨 정보를 가져올 수 없습니다.")
        return weather
    def get_Ans(self, text):
        trim_text = text.replace(" ", "")

        ans = {
            '날짜': discord.Embed(
                title=":calendar: 오늘은",
                description=self.get_Date(),
                color=discord.Color.blue()
            ),
            '요일': discord.Embed(
                title=":calendar_spiral: 오늘은",
                description=self.get_Day(),
                color=discord.Color.blue()
            ),
            '시간': discord.Embed(
                title=":clock9: 지금은",
                description=self.get_Time(),
                color=discord.Color.blue()
            ),
            '로또': discord.Embed(
                title="제 추천 번호는",
                description=self.send_Lotto(self.get_Lotto()),
                color=discord.Color.blue()
            ),
            '날씨': discord.Embed(
                title=":white_sun_small_cloud: 오늘의 날씨는",
                description=self.get_Weather(),
                color=discord.Color.blue()
            )
        }

        if trim_text in ans:
            return ans[trim_text]
        else:
            pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Relatively simple music bot example',
    intents=intents,
)


@bot.event
async def on_ready():
    await discord.client.change_presence(status=discord.Status.online, activity=discord.Game("연결"))
    print("봇 실행됨!")
    print(discord.client.user.name)
    print(discord.client.user.id)


@bot.command(aliases=['안녕'])
async def say_hello(ctx):
    await ctx.send('안녕하세요!')

async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.add_cog(Talk(bot))
        await bot.add_cog(Alarm(bot))
        await bot.start(Token)


asyncio.run(main())

