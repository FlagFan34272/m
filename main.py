import discord

from discord.ext import commands



client = commands.Bot(command_prefix = '+')


@client.event
async def on_ready():
        print('ready')
        ch = 0 
        for g in client.guilds: ch += len(g.channels)
        await client.change_presence(status = discord.Status.online, activity = discord.Game(f'{ch}개의 서버에서 일'))
        
       
	    
@client.command() 
async def 스킨(ctx, arg1): 
        embed=discord.Embed(title="**플레이어 스킨 입니다!**", color=0x0067a3) 
        embed.set_thumbnail(url="https://minotar.net/helm/{}/100.png".format(arg1))
        embed.set_image(url="https://minotar.net/armor/body/{}/100.png".format(arg1))
        await ctx.send(embed=embed)

@client.command()
async def 서버인원수(ctx):
        guild = ctx.guild    
        embed=discord.Embed(title="**서버 인원수 입니다!**", color=0x0067a3) 
        embed.add_field(name=f'{ctx.guild.name}서버의 인원수', value=f'{guild.member_count}명', inline=True)
        await ctx.send(embed = embed)
      
@client.command()
async def report(ctx, arg1, arg2):
	    channel = client.get_channel(991313436015337642)
	    await channel.send('플레이어: {}, 이유: {}'.format(arg1, arg2))
	    await ctx.send('완료!')
	    
@client.command() 
async def ArgsTest(ctx, arg1): 
        channel = client.get_channel(988815368829153369)
        embed=discord.Embed(title="**공지!**", color=0x0067a3) 
        embed.add_field(name="공지입니다!", value='{}'.format(arg1), inline=True)
        await channel.send(embed=embed)
        
@client.command()
async def 도움말(ctx):
        embed=discord.Embed(title="**도움말 입니다!**", description=" 봇 접두사:**+**", color=0x0067a3) 
        embed.add_field(name="**서버인원수**", value="현재 서버의 인원수를 보여줍니다.", inline=True)
        embed.add_field(name="**report**", value="플레이어를 신고합니다. 사용법: +report <uName> <Reason> **참고로 이유를 작성하실 때는 한 단어로 요약해 적어주세요!(띄어쓰기 X) (기술적 문제..?)**", inline=True)
        embed.add_field(name="**스킨**", value="플레이어의 스킨을 보여줍니다. 사용법 : +스킨 <uName>", inline=True)
        await ctx.send(embed = embed)
        


@client.event
async def on_command_error(ctx, error):
        embed=discord.Embed(title="**없는 명령어 입니다!**", description="`+도움말` 을 통해 알맞은 명령어를 알아보세요!", color=0x0067a3) 
        embed.set_thumbnail(url="https://minotar.net/helm/Flag_Fan/100.png")
        embed.add_field(name="봇 접두사", value="+", inline=True)
        embed.add_field(name="제작자", value="너냐너Flag_Fan#2092", inline=True) 
        
        await ctx.send(embed = embed)
        

client.run('OTg5NDI5NDM3MDcyMjc3NTI1.GyAzfQ.jw-LlZ1W9RVr--wx5QyKGSQJOaJn9aqnUSgN5A')
