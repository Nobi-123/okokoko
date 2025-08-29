from EsproMusic import app
from pyrogram import filters
from pyrogram.types import Message
import asyncio
import random

# Minimal placeholder dataset. Replace/extend with your real character pool.
CHARACTERS = [
    {"img_url": "https://te.legra.ph/file/29f784eb49d230ab62e9e.jpg", "rarity": "Common 🟠"},
    {"img_url": "https://te.legra.ph/file/0af5c8a3d2d6d1d2b1b9a.jpg", "rarity": "Legendary 🟡"},
    {"img_url": "https://te.legra.ph/file/6b6d7f7d5c3a9f1ad3b2f.jpg", "rarity": "Exclusive 💮"},
]

async def _delete_after_delay(client, chat_id: int, message_id: int, delay: int = 300):
    await asyncio.sleep(delay)
    try:
        await client.delete_messages(chat_id, message_id)
    except Exception:
        pass

@app.on_message(filters.command(["spawn", "waifu"]))
async def spawn_character(client, message: Message):
    """Send a random character image and auto-delete after 5 minutes."""
    chat_id = message.chat.id
    selected = random.choice(CHARACTERS)

    caption = (
        f"✨ A {selected['rarity']} Character Appears! ✨\n"
        f"🔍 Use /guess to claim this mysterious slave!\n"
        f"🥂 Hurry, before someone else snatches them!🤭"
    )

    sent = await client.send_photo(
        chat_id=chat_id,
        photo=selected["img_url"],
        caption=caption
    )

    # schedule deletion in background
    asyncio.create_task(_delete_after_delay(client, chat_id, sent.id, 300))
