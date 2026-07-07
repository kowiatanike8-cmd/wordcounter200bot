# Word Counter Telegram Bot

A simple Telegram bot that counts words, characters, sentences, and paragraphs in any text you send it.

## 1. Create the bot on Telegram

1. Open Telegram, search for **@BotFather**.
2. Send `/newbot`.
3. Choose a display name (e.g. "Word Counter").
4. Choose a username ending in `bot` (e.g. `WordCounterProBot`) — BotFather will tell you instantly if it's taken.
5. BotFather will give you a **token** like `123456789:ABCdefGhIJKlmNoPQRstuVwxyZ`. Save it — you'll need it below.

## 2. Push this project to GitHub

```bash
cd wordcounterbot
git init
git add .
git commit -m "Initial commit: word counter bot"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 3. Deploy on Railway

1. Go to [railway.app](https://railway.app) and log in (GitHub login works well).
2. Click **New Project** → **Deploy from GitHub repo**.
3. Select the repo you just pushed.
4. Once the project is created, go to **Variables** and add:
   - `BOT_TOKEN` = the token you got from BotFather.
5. Railway will detect the `Procfile` and run `python bot.py` as a **worker** process (not a web service — it doesn't listen on a port, it just polls Telegram).
6. Under **Settings**, make sure the service type is set to worker/background (not exposed as a web service), since this bot uses polling, not webhooks.
7. Deploy. Check the **Logs** tab — you should see `Bot starting...`.
8. Open Telegram, search for your bot's username, and send `/start`.

## 4. Test it

- Send `/start` — get a welcome message.
- Send any plain text — get instant word/character/sentence/paragraph stats.
- Or use `/count Your text here` to count specific text.

## Notes

- This bot uses **long polling**, so no public URL or webhook setup is needed — it just needs to stay running, which Railway handles automatically.
- If you ever regenerate your bot token in BotFather (via `/revoke`), update the `BOT_TOKEN` variable in Railway too.
- To rename or add features (e.g. reading time, unique word count), edit `bot.py`, push to GitHub, and Railway will auto-redeploy.
