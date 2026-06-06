import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
REGISTER_URL = os.getenv("REGISTER_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    telegram_id = user.id
    username = user.username
    first_name = user.first_name

    print(f"New user: ID={telegram_id}, Username=@{username}, Name={first_name}")

    keyboard = [
        [InlineKeyboardButton("立即註冊", url=REGISTER_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"歡迎來到 EU9 HUAT 🎉\n\n"
        f"你的 Telegram ID：{telegram_id}\n\n"
        f"點擊下方按鈕立即註冊 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("EU9 HUAT Bot 已啟動...")
app.run_polling()
