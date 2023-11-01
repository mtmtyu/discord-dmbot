import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.channel.id == 1076190674770210843:
        # 絵文字を追加
        emoji ="👍"
        await message.add_reaction(emoji)
        # メッセージを投稿したユーザーにロールを追加
        user = message.author
        role_id = 1169189492511481896
        role = discord.utils.get(user.guild.roles, id=role_id)
        if role:
            await user.add_roles(role)
        # メッセージを投稿したユーザーにDMを送信
        await message.author.send('もちもちサーバーにご参加ありがとうございます！自己紹介をしてくれたようですね！私からプレゼントがあります！サーバーに入った際に使ってみてください！それではサーバーでの生活をお楽しみください！　コマンド：/redeem WELCOME!MOCHISERVER')

from keep_alive import keep_alive
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
try:
    client.run(TOKEN)
except:
    os.system("kill 1")