import discord
from discord.ext import commands
from discord.utils import get
import classyjson as cj
class Krew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='goods')
    async def goods(self, ctx, island='All'):
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
    async def ships(self, ctx):
        embed=discord.Embed(title="Ship Prices", color=discord.Color.orange())
        embed.add_field(name="Brazil", value="Raft 1: 500\nRaft 2: 1300\nRaft 3: 2400\nTrader 1: 4350\nBoat 1: 6900\nBoat 2: 11k\nBoat 3: 16k\nDestroyer 1: 50k\nDestroyer 2: 80k\nDestroyer 3: 130k\nBaby Fancy: 8k", inline=True)
        embed.add_field(name="Guinea", value="Raft 1: 500\nRaft 2: 1300\nRaft 3: 2400\nTrader 1: 4350\nBoat 1: 6900\nBoat 2: 11k\nBoat 3: 16k\nDestroyer 1: 50k\nDestroyer 2: 80k\nDestroyer 3: 130k\nCalm Spirit: 120k", inline=True)
        embed.add_field(name="Labrador", value="Raft 1: 500\nRaft 2: 1300\nRaft 3: 2400\nTrader 1: 4350\nBoat 1: 6900\nBoat 2: 11k\nBoat 3: 16k\nDestroyer 1: 50k\nDestroyer 2: 80k\nDestroyer 3: 130k\nRoyal Fortune: 70k", inline=True)
        embed.add_field(name="Spain", value="Raft 1: 500\nRaft 2: 1300\nRaft 3: 2400\nTrader 1: 4350\nBoat 1: 6900\nBoat 2: 11k\nBoat 3: 16k\nDestroyer 1: 50k\nDestroyer 2: 80k\nDestroyer 3: 130k\nBaby Fancy: 8k\nRoyal Fortune: 70k\nCalm Spirit: 120k\nQueen Barb's Justice: 200k", inline=True)
        embed.add_field(name="Jamaica", value="Trader 2: 11k\nTrader 3: 30k\nBaby Fancy 2: 40k\nRoyal Fortune 2: 110k\nCalm Spirit 2: 170k\nQueen Barb's Justice 2: 350k", inline=True)
        await ctx.send(embed=embed)


    @commands.command(name='items')
    async def items(self, ctx):
        embed=discord.Embed(title='Item Prices', color=discord.Color.orange())
        embed.add_field(name='Brazil', value='Cannon Distance Upgrade: 4k\nAttack Speed Upgrade: 2k\nDamage Upgrade: 5k\nShip Speed Upgrade: 3k\nBruiser: 20k', inline=True)
        embed.add_field(name='Guinea', value='Cannon Distance Upgrade: 4k\nAttack Speed Upgrade: 2k\nDamage Upgrade: 5k\nShip Speed Upgrade: 3k\nDrifter: 25k')
        embed.add_field(name='Labrador', value='Steel Cannon: 35k\nCannon Distance Upgrade: 4k\nAttack Speed Upgrade: 2k\nDamage Upgrade: 5k\nShip Speed Upgrade: 3k')
        embed.add_field(name='Spain', value='Cannon Distance Upgrade: 4k\nAttack Speed Upgrade: 2k\nDamage Upgrade: 5k\nShip Speed Upgrade: 3k')
        embed.add_field(name='Jamaica', value='Air Pegleg: 22k\nBlue Gunpowder: 50k\nCannon Distance Upgrade: 4k\nAttack Speed Upgrade: 2k\nDamage Upgrade: 5k\nShip Speed Upgrade: 3k\nDemolisher: 100k')
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Krew(bot))
