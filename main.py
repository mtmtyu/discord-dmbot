import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.channel.id == 対象チャンネルID:
      # 絵文字を追加
      emoji ="👍"
      await message.add_reaction(emoji)
      # メッセージを投稿したユーザーにロールを追加
      user = message.author
      add_role_id = 追加したいロールID
      add_role = discord.utils.get(user.guild.roles, id=add_role_id)
      if add_role:
            await user.add_roles(add_role)
      remove_role_id = 削除したいロールID
      remove_role = discord.utils.get(user.guild.roles, id=remove_role_id)
      if remove_role:
        await user.remove_roles(remove_role)
        
      # メッセージを投稿したユーザーにDMを送信
      await message.author.send('送信したいメッセージ')

from keep_alive import keep_alive
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")
try:
    client.run(TOKEN)
except:
    os.system("kill 1")
