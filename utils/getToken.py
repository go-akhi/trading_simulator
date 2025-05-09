from dotenv import load_dotenv
import os 

#Load environment variables from .env file
def get_token():
    load_dotenv()

    #Access the token

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    return(token)
