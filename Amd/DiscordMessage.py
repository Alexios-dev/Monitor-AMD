#https://discordpy.readthedocs.io/en/stable/
from discord import Webhook,RequestsWebhookAdapter

def SendMessage(DC_Url,Message):
    webhook = Webhook.from_url(DC_Url, adapter=RequestsWebhookAdapter())
    webhook.send(Message)
