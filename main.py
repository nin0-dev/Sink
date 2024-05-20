import os
import dotenv
import lightbulb
from hikari import Intents

dotenv.load_dotenv()

bot = lightbulb.BotApp(
    os.environ["BOT_TOKEN"],
    intents=Intents.ALL,
    banner=None,
)
bot.load_extensions_from("./extensions/")


if __name__ == "__main__":
    bot.run()
