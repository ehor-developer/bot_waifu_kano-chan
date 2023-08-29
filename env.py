import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルから環境変数を読み込む

discord_api_key = os.getenv("DISCORD_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")