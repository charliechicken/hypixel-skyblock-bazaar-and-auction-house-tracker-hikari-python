from multiprocessing
import context
import hikari
import lightbulb
import requests
from time
import time, sleep


bot = lightbulb.BotApp(token = 'TOKEN_HERE')
api = "https://api.hypixel.net/skyblock/bazaar"
r = requests.get("https://api.hypixel.net/skyblock/auctions").json()

total_pages = int(r['totalPages'])
print(f "Total Pages: {total_pages}")

def get_info(call):
    r = requests.get(call)
return r.json()

def easy_function(item_name, channelid):
    return bot.rest.create_message(channelid, "Buy Order Price of " + item_name + ": " + "**" + str(get_info(api)["products"][item_name]["sell_summary"][1]["pricePerUnit"]) + "**" + "\n" + "Sell Offer of " + item_name + ": " + "**" + str(get_info(api)["products"][item_name]["buy_summary"][1]["pricePerUnit"]) + "**" + "\n---------------------------------------------------------")

@ bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')
items = []
tempstring = ""
while True:
    sleep(300 - time() % 1)
await easy_function("ENCHANTED_OBSIDIAN", channel_id_here)
await easy_function("HAMSTER_WHEEL", channel_id_here)
await easy_function("HYPER_CATALYST", channel_id_here)
await easy_function("CATALYST", channel_id_here)
await easy_function("HEAVY_GABAGOOL", channel_id_here)
await easy_function("ENCHANTED_QUARTZ_BLOCK", channel_id_here)
await easy_function("NULL_OVOID", channel_id_here)

for i in range(0, total_pages):
    r = requests.get(f "https://api.hypixel.net/skyblock/auctions?page={i}").json()
auctions = r['auctions']

for auction in auctions:
    if (auction['item_name'] == "Amber-polished Drill Engine"):
        items.append(auction["starting_bid"])
newarr = sorted(items)
for i in range(0, len(newarr)):
    tempstring = tempstring + str(i + 1) + ": " + "**" + str(float(newarr[i]) / 1000000) + " Million" + "** coins.\n"

await bot.rest.create_message(channel_id_here, tempstring + "----------------------------------------------------")

items = []
newarr = []
tempstring = ""


bot.run()
