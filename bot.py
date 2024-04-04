from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Type /fetchmembers to fetch members.')

def fetch_members(update: Update, context: CallbackContext) -> None:
    try:
        chat_id = -1002076123692
        members_count = context.bot.get_chat_member_count(chat_id)
        update.message.reply_text(f'The number of members in the chat: {members_count}')
    except Exception as e:
        update.message.reply_text('An error occurred while fetching members. Please try again later.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("fetchmembers", fetch_members))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
