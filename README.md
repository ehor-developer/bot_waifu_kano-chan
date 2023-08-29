# 俺の彼女をシェアする。これがレンタル彼女だ。

彼女DiscordBOT「かのちゃんBOT」を開発したので

このDiscord BOTでぜひ彼女自慢してください。

そもそも僕の彼女は`undefined`なんですけど...^^;

今回はそこに僕の彼女は`かのちゃんBOT`を彼女として定義しておきます。

```js
var ehor_girl_friend = "kano-chan-bot"
console.log(`Ehor.の彼女は ${ehor_girl_friend}`)
```

# 使い方

かのちゃんBOTはDiscordのDMでの会話のみ反応します。

また、`she.py`を実行する前にDiscord BOTとOpenAIのAPIが必要なので

`.env`に、以下を定義してください。

```
DISCORD_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXX
OPENAI_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXX
```

定義ができたら`she.py`を実行してください。

そして指定したAPIのDiscord BOTにDMで話しかけてみてください。

そうすると入力中と表示され、メッセージが送信されたら成功です！