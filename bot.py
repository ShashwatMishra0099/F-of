from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7049444312:AAEr1d-KXTz0mVR6QOPzRy-Nwa5NVk9o4rA"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Type /fetchmembers to fetch members.')

def fetch_members(update: Update, context: CallbackContext) -> None:
    try:
        chat_id = update.message.chat_id
        members = context.bot.get_chat_members(chat_id)  # Retrieve all chat members
        
        member_usernames = [member.user.username for member in members if member.user.username is not None]  # Extract usernames of members
        members_count = len(member_usernames)  # Get the count of members with usernames
        
        update.message.reply_text(f'The number of members in the chat: {members_count}')
        update.message.reply_text('Usernames of members:')
        update.message.reply_text('\n'.join(member_usernames))  # Display the usernames in a list
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
