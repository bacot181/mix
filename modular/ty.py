import os
import logging
import asyncio
from pyrogram import Client, filters, idle

from Mix import *

__modles__ = "tesy"
__help__ = """
 Github
• Perintah: ua.
• Penjelasan: Untuk melihat.
"""

chat_id = []


@ky.ubot("ad", sudo=True)
async def add_user(c, m):
    try:
        args = m.text.split(maxsplit=1)
        if len(args) < 2:
            await m.reply_text("Usage: cadd <dmute_id>")
            return
        dmute = int(args[1])  # Extract the dmute ID from the command
        await save_dmute(dmute)
        await m.reply_text("ID successfully added to the database.")
        logger.info(f"ID {dmute} added to the database.")
    except ValueError:
        await m.reply_text("Invalid ID format. Please provide an integer.")
    except Exception as e:
        await mreply_text(f"Error: {e}")
        logger.error(f"Error in add_user: {e}")

@ky.ubot("del", sudo=True)
async def remove_user(c, m):
    try:
        args = m.text.split()
        if len(args) < 2:
            await m.reply_text("Usage: cdel <dmute_id>")
            return
        dmute = int(args[1])  # Extract the dmute from the command
        await remove_dmute(dmute)
        await m.reply_text("ID berhasil dihapus dari database.")
        logger.info(f"ID {dmute} removed from the database.")
    except ValueError:
        await m.reply_text("Invalid ID format. Please provide an integer.")
    except Exception as e:
        await m.reply_text(f"Error: {e}")
        logger.error(f"Error in remove_user: {e}")

@ky.ubot("cek", sudo=True)
async def check_dmutes(c, m):
    try:
        dmute_list = await get_all_dmute()
        if dmute_list:
            await m.reply_text(f"ID values in the database: {dmute_list}")
        else:
            await m.reply_text("No ID values found in the database.")
        logger.info("Checked the database for IDs.")
    except Exception as e:
        await m.reply_text(f"Error: {e}")
        logger.error(f"Error in check_dmutes: {e}")

@ky.ubot.on_message(filters.chat(chat_id))
async def delete_messages(c, m):
    try:
        dmute_list = await get_all_dmute()
        if str(message.from_user.id) in dmute_list:
            await client.delete_messages(chat_id=message.chat.id, message_ids=[message.message_id])
            logger.info(f"Deleted message from user ID {message.from_user.id} in chat {message.chat.id}.")
    except Exception as e:
        logger.error(f"Error deleting message: {e}")
