import discord, datetime, os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} 봇을 연결했습니다'.format(client))


@client.event
async def on_message(message):
    if message.content == "~도움":
            if message.author.dm_channel:
                await message.author.dm_channel.send("DM 채널이 있어서 그냥 보냈어요!")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("~공지(당신들은 사용 불가), ~청소(이것도 당신들은 사용 불가), ~투표 (이건 가능함)")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)