# 디스코드 봇 만들어보기
# 24.03.12
# - 정상작동 확인
import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.voice_states = True
client = commands.Bot(command_prefix='!', intents=intents)
#dicord.py 1.5v부터는 intents 지정필요
#command 지정  ex>> !입장 , !퇴장, !(검색내용) ...

#봇이 준비 되었을 때의 이벤트 핸들러
@client.event
async def on_ready():
    print('Bot is ready.')
    # 정상 실행 확인용

# 이벤트 핸들러
@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요!')

@client.command()
async def 종료(ctx):
    await ctx.send("봇을 종료합니다.")
    await client.close()

# 유튜브에서 음악 검색하여 재생하는 함수
async def play_youtube(ctx, search_query):
    if ctx.voice_client is None:
        await join_voice_channel(ctx)

    # 유튜브 검색 및 음악 재생
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search_query}", download=False)
        if 'entries' in info:
            url = info['entries'][0]['formats'][0]['url']
            ctx.voice_client.play(discord.FFmpegPCMAudio(url, **ydl_opts))
        else:
            await ctx.send("검색 결과를 찾을 수 없습니다.")

client.run('사용할 봇의 토큰 값을 입력해주세요.')
