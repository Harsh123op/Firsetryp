from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from pymongo import MongoClient
from shivu import application, sudo_users

async def mongo_command(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text("Nouu.. it's Sudo user's Command..")
        return

    if len(context.args) != 1:
        await update.message.reply_text("Usage: /mongo <mongo_url>")
        return

    mongo_url = context.args[0]
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        
        # List all databases
        databases = client.list_database_names()
        if not databases:
            await update.message.reply_text("No databases found.")
            return
        
        response = "Databases and Collections:\n"
        
        for db_name in databases:
            db = client[db_name]
            collections = db.list_collection_names()
            response += f"Database: {db_name}\n"
            if collections:
                for coll_name in collections:
                    response += f"  Collection: {coll_name}\n"
            else:
                response += "  No collections found.\n"
        
        await update.message.reply_text(response)
    
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

async def formatmongo_command(update: Update, context: CallbackContext) -> None:
    if str(update.effective_user.id) not in sudo_users:
        await update.message.reply_text("Nouu.. it's Sudo user's Command..")
        return

    if len(context.args) != 1:
        await update.message.reply_text("Usage: /formatmongo <mongo_url>")
        return

    mongo_url = context.args[0]
    try:
        # Connect to MongoDB
        client = MongoClient(mongo_url)
        
        # List all databases
        databases = client.list_database_names()
        if not databases:
            await update.message.reply_text("No databases found to format.")
            return
        
        # Drop all databases
        for db_name in databases:
            client.drop_database(db_name)
        
        await update.message.reply_text("All databases have been deleted. MongoDB instance is now empty.")
    
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

# Add handlers
application.add_handler(CommandHandler("mongo", mongo_command))
application.add_handler(CommandHandler("formatmongo", formatmongo_command))
