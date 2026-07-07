import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm a Word Counter Bot.\n\n"
        "Just send me any text and I'll count:\n"
        "• Words\n"
        "• Characters (with & without spaces)\n"
        "• Sentences\n"
        "• Paragraphs\n\n"
        "Or use /count followed by text."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me any message and I'll return word/character stats.\n"
        "Commands:\n"
        "/start - welcome message\n"
        "/help - this message\n"
        "/count <text> - count stats for given text"
    )


def analyze_text(text: str) -> str:
    words = text.split()
    word_count = len(words)
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    sentence_count = sum(text.count(p) for p in [".", "!", "?"]) or (1 if text.strip() else 0)
    paragraph_count = len([p for p in text.split("\n") if p.strip()]) or (1 if text.strip() else 0)

    return (
        f"📊 *Text Stats*\n\n"
        f"📝 Words: {word_count}\n"
        f"🔤 Characters (with spaces): {char_count_with_spaces}\n"
        f"🔡 Characters (no spaces): {char_count_no_spaces}\n"
        f"🔵 Sentences: {sentence_count}\n"
        f"📄 Paragraphs: {paragraph_count}"
    )


async def count_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text.strip():
        await update.message.reply_text("Please provide text after /count, e.g.\n/count Hello world!")
        return
    await update.message.reply_text(analyze_text(text), parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(analyze_text(text), parse_mode="Markdown")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("count", count_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
