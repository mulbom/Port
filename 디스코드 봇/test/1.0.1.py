# 시간,날짜 확인 명령어 추가 / youtube API 활용시 url 재생이 아닌 검색 후 최상단 표기물 재생 함수

import asyncio

import discord
from datetime import datetime
import youtube_dl
from discord.ext import commands
#from googleapiclient.discovery import build



Token = ""
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
        """(사전 다운로드하지 않음)"""
        try:
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
                await ctx.send(f'현재 재생중: {player.title}')
        except Exception as e:
            print("에러 : ", e)
            await ctx.send("음악을 재생하는 중에 오류가 발생했습니다.")

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"볼륨을 {volume}%로 바꿨어요.")

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("가볼게요.")
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused() or not ctx.voice_client.is_playing():
            await ctx.send("음악이 멈춰져있거나 없어요.")

        ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client.is_playing() or not ctx.voice_client.is_paused():
            await ctx.send("음악이 이미 재생 중이거나 재생할 음악이 없습니다.")

        ctx.voice_client.resume()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
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
            q=query,
            type='video'
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    """

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('!'):
            command = message.content[1:]
            response = self.get_Ans(command)
            await message.channel.send(response)

    def get_Day(self):
        Daylist = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        Day = Daylist[datetime.today().weekday()]
        return Day

    def get_Date(self):
        return datetime.today().strftime("%Y년 %m월 %d일")

    def get_Time(self):
        return datetime.today().strftime("%H시 %M분")

    def get_Ans(self, text):
        trim_text = text.replace(" ", "")

        ans = {
            '날짜': ':calendar: 오늘은 {}이에요.'.format(self.get_Date()),
            '요일': ':calendar: 오늘은 {}이에요.'.format(self.get_Day()),
            '시간': ':clock9: 현재 시간은 {}이에요.'.format(self.get_Time())
        }

        if trim_text in ans:
            return ans[trim_text]
        else:
            return "그런건 몰라요."

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
        await bot.start(Token)


asyncio.run(main())

