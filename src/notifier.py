import os
import requests


def notify_discord(new_books):
    webhook = os.getenv("DISCORD_WEBHOOK_URL")


    if not webhook:
        print("no discord webhook configurated")
        return
    
    if not new_books:
        return
    
    message = "**new books found**\n\n"

    for b in new_books:
        message += f'**{b["title"]}** - {b["price"]}\n{b["url"]}\n\n'

    payload = {
        "content": message
    }

    r = requests.post(webhook,json=payload)
    if r.status_code != 204:
        print("failed to send discord notification", r.text)