from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from pymongo import MongoClient
from shivu import application

sudo_users = 7058928258

# Store MongoDB client instances and database names to maintain state
mongo_clients = {}

async def delete_command(update: Update, context: CallbackContext) -> None:
    # Check if the user is a sudo user
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text("This command is only for sudo users.")
        return

    # Check if the user provided the MongoDB URL
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /delete <mongo_url>")
        return

    mongo_url = context.args[0]
    
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        
        # List all databases
        databases = client.list_database_names()
        if not databases:
            await update.message.reply_text("No databases found to delete.")
            return

        # Save the client instance for later use
        mongo_clients[update.effective_user.id] = client

        # Create buttons for each database
        buttons = [
            [InlineKeyboardButton(db_name, callback_data=f'delete_db_{db_name}')]
            for db_name in databases
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.reply_text("Select the database to delete:", reply_markup=reply_markup)

    except Exception as e:
        await update.message.reply_text(f"Error connecting to MongoDB: {str(e)}")

async def handle_database_deletion(update: Update, context: CallbackContext) -> None:
    # Extract the user ID and the database name from callback data
    query = update.callback_query
    user_id = query.from_user.id
    callback_data = query.data

    if not callback_data.startswith('delete_db_'):
        return

    # Extract the database name from callback data
    db_name = callback_data.split('delete_db_')[1]

    # Check if a client for this user exists
    if user_id not in mongo_clients:
        await query.answer("No MongoDB connection found. Please use /delete <mongo_url> first.")
        return

    try:
        # Get the MongoDB client
        client = mongo_clients[user_id]
        
        # Drop the selected database
        client.drop_database(db_name)

        # Notify the user
        await query.message.reply_text(f"Database '{db_name}' has been successfully deleted.")
        
        # Remove the button after deletion
        await query.message.delete()

    except Exception as e:
        await query.message.reply_text(f"Failed to delete database '{db_name}': {str(e)}")

# Add handlers
application.add_handler(CommandHandler("delete", delete_command))
application.add_handler(CallbackQueryHandler(handle_database_deletion, pattern=r'^delete_db_'))
