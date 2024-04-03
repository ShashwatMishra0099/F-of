from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ChatAction

# Define a function to fetch members and their usernames
def fetch_members(update: Update, context: CallbackContext):
    chat_id = update.message.text.split()[1]

    # Send "typing" action while fetching data
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    members = context.bot.get_chat_members_count(chat_id)
    usernames = [member.user.username for member in context.bot.get_chat(chat_id).get_members()]

    update.message.reply_text(f"Total members in the group: {members}\nUsernames: {', '.join(usernames)}")

# Set up the Telegram bot
updater = Updater("7049444312:AAEr1d-KXTz0mVR6QOPzRy-Nwa5NVk9o4rA", use_context=True)
dispatcher = updater.dispatcher

# Register the command handler
dispatcher.add_handler(CommandHandler("fetchmembers", fetch_members))

# Start the bot
updater.start_polling()
updater.idle()
