from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import getToken

token=getToken.get_token()

def bot_status(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is active")

def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("bot_status",bot_status))

    updater.start_polling()
    print("🥸 Bot is here")
    update.idle()


if __name__ == "__main__":
    main()


