import discord
from discord.ext import commands
from discord.utils import get

class Krew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='goods')
    async def goods(self, ctx):
        embed=discord.Embed(title="Goods Prices", color=discord.Color.orange())
        embed.add_field(name="Brazil", value="Rum: 60\nCoffee: 26\nSpice: 25 \nSilk: 150", inline=True)
        embed.add_field(name="Guinea", value="Rum: 38\nCoffee: 22\nSpice: 22\nSilk: 310", inline=True)
        embed.add_field(name="Labrador", value="Rum: 48\nCoffee: 40\nSpice: 14\nSilk: 230", inline=True)
        embed.add_field(name="Spain", value="Rum: 52\nCoffee: 65 \nSpice: 53\nSilk: 180", inline=True)
        embed.add_field(name="Jamaica", value="Rum: 32\nCoffee: 70\nSpice: 40\nSilk: 240", inline=True)
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
def setup(bot):
    bot.add_cog(Krew(bot))
