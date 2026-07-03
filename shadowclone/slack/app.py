# slack/app.py

from slack_bolt import App

app = App(token="BOT_TOKEN",
          signing_secret="SIGNING_SECRET")

@app.event("app_mention")
def mention(event, say):
    say("Searching employee knowledge...")

if __name__ == "__main__":
    app.start(port=3000)