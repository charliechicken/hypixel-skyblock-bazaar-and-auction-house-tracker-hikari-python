from multiprocessing import context
import hikari
import lightbulb
import requests
import json
import schedule
from time import time, sleep


bot = lightbulb.BotApp(token='TOKEN_HERE',
 default_enabled_guilds=('YOUR_GUILD_ID')) #You can delte default_enabled_guilds to have the bot in multiple servers
api = "https://api.hypixel.net/skyblock/bazaar" # Fetch API for Bazaar Data
r = requests.get("https://api.hypixel.net/skyblock/auctions").json() # Auction House data

total_pages = int(r['totalPages']) # Total amount of auction house pages
print(f"Total Pages: {total_pages}")


#This function is used to turn api data into JSON so I can manipulate it here to my liking
def get_info(call):
    r = requests.get(call)
    return r.json()

# This function takes two paramaters; the first searches for whatever bazaar item you want to track, the second is the channel id you want to send it in.
def easy_function(item_name, channelid):
    return bot.rest.create_message(channelid, "Buy Order Price of " + item_name + ": " + "**" + str(get_info(api)["products"][item_name]["sell_summary"][1]["pricePerUnit"]) + "**" + "\n" + "Sell Offer of " + item_name + ": " + "**" + str(get_info(api)["products"][item_name]["buy_summary"][1]["pricePerUnit"]) + "**" + "\n---------------------------------------------------------")

# Event when bot is started
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')
    #Preliminary variables, items will be used to filer for Amber-polished Drill Engines, tempstring to display a message in a channel of your liking
    items = []
    tempstring = ""
    # Loop every 300 seconds; 5 minutes. You can change this variable to get more frequent updates
    while True:
        sleep(300 - time() % 1)
        # Calls to my function
        await easy_function("ENCHANTED_OBSIDIAN", "channel_id_here")
        await easy_function("HAMSTER_WHEEL", "channel_id_here")
        await easy_function("HYPER_CATALYST", "channel_id_here")
        await easy_function("CATALYST", "channel_id_here")
        await easy_function("HEAVY_GABAGOOL", "channel_id_here")
        await easy_function("ENCHANTED_QUARTZ_BLOCK", "channel_id_here")
        await easy_function("NULL_OVOID", "channel_id_here")
        await easy_function("HYPERGOLIC_GABAGOOL", "channel_id_here")
        await easy_function("TITANIC_EXP_BOTTLE", "channel_id_here")
        # Loop Through Every Page
        for i in range(0, total_pages):
            r = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={i}").json()
            auctions = r['auctions']

            # Get each individual auction
            for auction in auctions:
                # Check if auction name is Amber-polished
                if(auction['item_name'] == "Amber-polished Drill Engine"):
                    # Once found, append the amount of coins for the Amber-polished
                    items.append(auction["starting_bid"])
        # Sort through the numbers, lowest to highest
        newarr = sorted(items)
        # Loop to create a message displaying all of the Amber-polished drill engines on BIN
        for i in range(0, len(newarr)): 
            tempstring = tempstring + str(i+1) + ": " + "**" + str(float(newarr[i]) / 1000000) + " Million" + "** coins.\n"
            
        #Sends the message with Amber-polished values to a channel
        await bot.rest.create_message("channel_id_here", tempstring + "----------------------------------------------------")
        # Resets the variables
        items = []
        newarr = []
        tempstring = ""

# Run the bot
bot.run()
