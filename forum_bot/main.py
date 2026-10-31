import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

MENU = [
    ["📋 Подать заявку"],
    ["🛡️ Заявка на администратора"],
    ["👑 Заявка на лидера"],
    ["🎬 Заявка на медиа"],
    ["🆘 Техническая поддержка"],
    ["📚 Правила проекта"],
    ["👤 Мой профиль", "📊 Статус заявок"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        MENU,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Добро пожаловать на форум WEZING RUSSIA!\n\n"
        "Здесь ты можешь подать заявку, ознакомиться "
        "с правилами и обратиться в техническую поддержку.",
        reply_markup=keyboard
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    answers = {
        "📋 Подать заявку": "Выбери направление подачи заявки.",
        "🛡️ Заявка на администратора": "Заявка на администратора скоро будет доступна.",
        "👑 Заявка на лидера": "Заявка на лидера скоро будет доступна.",
        "🎬 Заявка на медиа": "Заявка в медиа скоро будет доступна.",
        "🆘 Техническая поддержка": "Опиши свою проблему одним сообщением.",
        "📚 Правила проекта": "Правила WEZING RUSSIA скоро появятся здесь.",
        "👤 Мой профиль": "Профиль пока пуст.",
        "📊 Статус заявок": "У тебя пока нет заявок."
    }

    await update.message.reply_text(
        answers.get(text, "Используй кнопки главного меню.")
    )

def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN в переменных окружения!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

    print("WEZING RUSSIA BOT запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
