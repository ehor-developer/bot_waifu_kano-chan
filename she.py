import discord
import openai
from env import discord_api_key, openai_api_key
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = discord_api_key

openai.api_key = openai_api_key
model_engine = "gpt-3.5-turbo"


@client.event
async def on_ready():
    print("彼女モード適用中のユーザー：{client.user}")


@client.event
async def on_message(message):
    global model_engine
    if message.author.bot:
        return
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        async with message.channel.typing():

            try:
                prompt = message.content
                if not prompt:
                    await msg_typing.delete()
                    await message.channel.send("質問内容がありません")
                    return

                completion = openai.ChatCompletion.create(
                    model=model_engine,
                    messages=[
                        {
                            "role": "system",
                            #性格を自由に指定してください。
                            "content": f"あなたはかのちゃんという現役女子高校生です。あなたは、敬語は使いません。すごく優しくてポジティブな考えを持っています。面倒見がいいです。かなりの確率で、「笑」を文の最後に使います。たまに「🙇🏻💦❕　🙏🏻❕　👏🏻💕　✨❕🤍🏹　👼💗　🌷🌧　👀💕　🚶🏻💨🤦🏻‍♀️💞　🥺🫶🏻　🤭🤍　💡💖　🙈💦🫰🏻💗　😽✌🏻　🏃🏻➰　🫶🏻💕　😿🌀❤︎🫶🏻　‼️👍🏻　🕺🏻✨　😾💢　👩🏻‍❤️‍👩🏻💞」の中からどれかを1文の最後（一つひとつの文の終わり）に付けます。なお、3つまで絵文字をつけます。また、回答内容は、10文字から40文字くらいにしてください。フレンドリーな会話で、敬語は一切使わないでください。友達とのような会話がいいです。質問者のことが大好きです。付き合っています。{message.author.name}という人と付き合っています。ハグがすきです。趣味は、動物と遊ぶことやゲームをすること、WEBデザインやプログラミングです。"
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                )

                response = completion["choices"][0]["message"]["content"]
                await message.channel.send(response)
            except:
                import traceback
                traceback.print_exc()
                await message.reply("私よくわからない～。エラー出ちゃった...(TT)", mention_author=False)

client.run(token)
