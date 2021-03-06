import discord
from discord.ext import commands
from discord.utils import get
import classyjson as cj
import asyncio
class Krew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='goods')

    async def goods(self, ctx, island='All'):
        async with ctx.typing():
            await asyncio.sleep(1)
            island = island.capitalize()
            if island == 'All':
                embed=discord.Embed(title='Goods Prices', color=discord.Color.orange())
                embed.add_field(name="Brazil", value="Rum: 60\nCoffee: 26\nSpice: 25 \nSilk: 150", inline=True)
                embed.add_field(name="Guinea", value="Rum: 38\nCoffee: 22\nSpice: 22\nSilk: 310", inline=True)
                embed.add_field(name="Labrador", value="Rum: 48\nCoffee: 40\nSpice: 14\nSilk: 230", inline=True)
                embed.add_field(name="Spain", value="Rum: 52\nCoffee: 65 \nSpice: 53\nSilk: 180", inline=True)
                embed.add_field(name="Jamaica", value="Rum: 32\nCoffee: 70\nSpice: 40\nSilk: 240", inline=True)
                await ctx.send(embed=embed)

            elif island == "Brazil" or island == "Guinea" or island == "Labrador" or island == "Spain" or island == "Jamaica":
                with open( 'data/goods.json', 'r') as stuff:
                    goods = cj.load(stuff)

                if island in goods:
                    embed=discord.Embed(title=island, color=discord.Color.orange())

                    temp = []
                    for k, v in goods[island].items():

                        temp.append(str(k + ': ' + v))
                    val = '\n'.join(temp)
                    embed.add_field(name=island, value=val, inline=True)
                await ctx.send(embed=embed)

    @commands.command(name='ships')
    async def ships(self, ctx, ship='All'):
        async with ctx.typing():
            await asyncio.sleep(1)
            ship = ship.capitalize()
            if ship == 'All':
                embed=discord.Embed(color=discord.Color.orange())
                embed.add_field(name="Ship Prices", value="*Raft 1:* 500\n*Raft 2:* 1300\n*Raft 3:* 2400\n*Trader 1:* 4350\n*Trader 2:* 11k\n*Trader 3:* 30k\n*Boat 1:* 6900\n*Boat 2:* 11k\n*Boat 3:* 16k\n*Destroyer 1:* 50k\n*Destroyer 2:* 80k\n*Destroyer 3:* 130k\n*Baby Fancy:* 8k\n*Baby Fancy 2:* 40k\n*Royal Fortune:* 70k\n*Royal Fortune 2:* 110k\n*Calm Spirit:* 120k\n*Calm Spirit 2:* 170k\n*Queen Barb's Justice:* 200k\n*Queen Barb's Justice 2:* 350k", inline=True)
                embed.set_footer(text=f'Do {ctx.prefix}ships <ship name> for more info on a ship!')
                await ctx.send(embed=embed)
            elif ship == 'Raft1' or ship == 'Raft2' or ship == 'Raft3' or ship == 'Trader1' or ship == 'Trader2' or ship == 'Trader3' or ship == 'Boat1' or ship == 'Boat2' or ship == 'Boat3' or ship == 'Destroyer1' or ship == 'Destroyer2' or ship == 'Destroyer3' or ship == 'Babyfancy' or ship == 'Babyfancy2' or ship == 'Royalfortune' or ship == 'Royalfortune2' or ship == 'Calmspirit' or ship == 'Calmspirit2' or ship == 'Qbj' or ship == 'Qbj2':
                with open( 'data/ships.json', 'r') as stuff:
                    ships = cj.load(stuff)

                if ship in ships:
                    embed=discord.Embed(color=discord.Color.orange())

                    temp = []
                    for k, v in ships[ship].items():

                        temp.append(str(k + ': ' + v))
                    val = '\n'.join(temp)
                    embed.add_field(name=ship, value=val, inline=True)
                    embed.set_footer(text="Need more help? DM @Emerald#8617 or @Sh-wayz#4749")
                await ctx.send(embed=embed)



    @commands.command(name='items')
    async def items(self, ctx, item='All'):
        async with ctx.typing():
            await asyncio.sleep(1)
            item = item.capitalize()
            if item == "All":
                embed=discord.Embed(title='Item Prices', color=discord.Color.orange())
                embed.add_field(name='Brazil', value='*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k\n*Bruiser: 20k*', inline=True)
                embed.add_field(name='Guinea', value='*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k\n*Drifter:* 25k')
                embed.add_field(name='Labrador', value='*Steel Cannon:* 35k\n*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade*: 3k')
                embed.add_field(name='Spain', value='*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k')
                embed.add_field(name='Jamaica', value='*Air Pegleg:* 22k\n*Blue Gunpowder:* 50k\n*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k\n*Demolisher:* 100k')
                embed.set_footer(text='Do k! items <item name> for more info on an item.')
                await ctx.send(embed=embed)
            elif item == "CannonDistance" or item == "AttackSpeed" or item == "Damage" or item == "ShipSpeed" or item == "Bruiser" or item == "Drifter" or item == "SteelCannon" or item == "AirPegleg" or item == "BlueGunpowder" or item == "Demolisher":
                with open( 'data/items.json', 'r') as stuff:
                    items = cj.load(stuff)

                if item in items:
                    embed=discord.Embed(title="Items", color=discord.Color.orange())

                    temp = []
                    for k, v in items[item].items():

                        temp.append(str(k + ': ' + v))
                    val = '\n'.join(temp)
                    embed.add_field(name=item, value=val, inline=True)
                await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Krew(bot))
