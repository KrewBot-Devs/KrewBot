import discord
from discord.ext import commands
from discord.utils import get

class Krew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='goods')
    async def goods(self, ctx):
        embed=discord.Embed(title="Goods Prices", color=discord.Color.orange())
        embed.add_field(name="Brazil", value="*Rum:* 60\n*Coffee:* 26\n*Spice:* 25 \n*Silk:* 150", inline=True)
        embed.add_field(name="Guinea", value="*Rum:* 38\n*Coffee:* 22\n*Spice:* 22\n*Silk:* 310", inline=True)
        embed.add_field(name="Labrador", value="*Rum:* 48\n*Coffee:* 40\n*Spice:* 14\n*Silk:* 230", inline=True)
        embed.add_field(name="Spain", value="*Rum:* 52\n*Coffee:* 65 \n*Spice:* 53\n*Silk:* 180", inline=True)
        embed.add_field(name="Jamaica", value="*Rum:* 32\n*Coffee:* 70\n*Spice:* 40\n*Silk:* 240", inline=True)
        await ctx.send(embed=embed)

    @commands.command(name='ships')
    async def ships(self, ctx):
        embed=discord.Embed(title="Ship Prices", color=discord.Color.orange())
        embed.add_field(name="Brazil", value="*Raft 1:* 500\n*Raft 2:* 1300\n*Raft 3:* 2400\n*Trader 1:* 4350\n*Boat 1:* 6900\n*Boat 2:* 11k\n*Boat 3:* 16k\n*Destroyer 1:* 50k\n*Destroyer 2:* 80k\n*Destroyer 3:* 130k\n*Baby Fancy:* 8k", inline=True)
        embed.add_field(name="Guinea", value="*Raft 1:* 500\n*Raft 2:* 1300\n*Raft 3:* 2400\n*Trader 1:* 4350\n*Boat 1:* 6900\n*Boat 2:* 11k\n*Boat 3:* 16k\n*Destroyer 1:* 50k\n*Destroyer 2:* 80k\n*Destroyer 3:* 130k\n*Calm Spirit:* 120k", inline=True)
        embed.add_field(name="Labrador", value="*Raft 1:* 500\n*Raft 2:* 1300\n*Raft 3:* 2400\n*Trader 1:* 4350\n*Boat 1:* 6900\n*Boat 2:* 11k\n*Boat 3:* 16k\n*Destroyer 1:* 50k\n**Destroyer 2:* 80k\n*Destroyer 3:* 130k\n*Royal Fortune:* 70k", inline=True)
        embed.add_field(name="Spain", value="*Raft 1:* 500\n*Raft 2:* 1300\n*Raft 3:* 2400\n*Trader 1:* 4350\n*Boat 1:* 6900\n*Boat 2:* 11k\n*Boat 3:* 16k\n*Destroyer 1:* 50k\n*Destroyer 2:* 80k\n*Destroyer 3:* 130k\n*Baby Fancy:* 8k\n*Royal Fortune:* 70k\n*Calm Spirit:* 120k\n*Queen Barb's Justice:* 200k", inline=True)
        embed.add_field(name="Jamaica", value="*Trader 2:* 11k\n*Trader 3:* 30k\n*Baby Fancy 2:* 40k\n*Royal Fortune 2:* 110k\n*Calm Spirit 2:* 170k\n*Queen Barb's Justice 2:* 350k", inline=True)
        await ctx.send(embed=embed)


    @commands.command(name='items')
    async def items(self, ctx):
        embed=discord.Embed(title='Item Prices', color=discord.Color.orange())
        embed.add_field(name='Brazil', value='*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k\n*Bruiser: 20k*', inline=True)
        embed.add_field(name='Guinea', value='*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k\n*Drifter:* 25k')
        embed.add_field(name='Labrador', value='*Steel Cannon:* 35k\n*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade*: 3k')
        embed.add_field(name='Spain', value='*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k')
        embed.add_field(name='Jamaica', value='*Air Pegleg:* 22k\n*Blue Gunpowder:* 50k\n*Cannon Distance Upgrade:* 4k\n*Attack Speed Upgrade:* 2k\n*Damage Upgrade:* 5k\n*Ship Speed Upgrade:* 3k\n*Demolisher:* 100k')
        embed.set_footer(text='Do k! items <item name> for more info on an item.')
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Krew(bot))
