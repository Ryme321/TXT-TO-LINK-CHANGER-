import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Get the Telegram Bot Token from environment variable
TOKEN = os.environ.get('TELEGRAM_TOKEN')

if TOKEN is None:
    print("Error: TELEGRAM_TOKEN environment variable not set.")
    exit()

# Define the echo function
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    print("Bot is starting...")
    updater.start_polling()
    print("Bot is polling.")

    # Run the bot until you press Ctrl-C
    updater.idle()
    print("Bot has stopped.")

if __name__ == '__main__':
    main()
    
