import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
REGISTER_URL = os.getenv("REGISTER_URL")
CHANNEL_URL = os.getenv("CHANNEL_URL", "https://t.me/Eu9huat99")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_id = user.id
    first_name = user.first_name or "Friend"

    keyboard = [
        [InlineKeyboardButton("🔥 立即注册", url=REGISTER_URL)],
        [InlineKeyboardButton("📢 官方频道", url=CHANNEL_URL)]
    ]

    await update.message.reply_text(
        f"🏆 欢迎来到 EU9 HUAT 🏆\n\n"
        f"🇸🇬 SG Players' Choice\n"
        f"🏆 FIFA World Cup 2026\n"
        f"⚽ Every Match. Every Moment.\n\n"
        f"Hi {first_name} 👋\n"
        f"你的 Telegram ID：{telegram_id}\n\n"
        f"👇 点击下方按钮开始 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        first_name = user.first_name or "朋友"

        keyboard = [
            [InlineKeyboardButton("🔥 立即注册", url=REGISTER_URL)],
            [InlineKeyboardButton("📢 官方频道", url=CHANNEL_URL)]
        ]

        await update.message.reply_text(
            f"🎉 欢迎 {first_name} 加入 EU9 HUAT 官方群 🎉\n\n"
            f"🇸🇬 SG Players' Choice\n"
            f"🏆 FIFA World Cup 2026\n"
            f"⚽ Every Match. Every Moment.\n\n"
            f"🎯 注册入口已开启\n"
            f"👇 点击下方按钮完成注册 👇\n\n"
            f"🔥 精彩赛事 · 尽在 EU9 🔥",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))

print("EU9 HUAT Bot 已启动...")
app.run_polling()
