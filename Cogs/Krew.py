import discord
from discord.ext import commands
from discord.utils import get

class Krew(commands.Cog):
    @commands.command(name='goods')
    async def economy(self, ctx):
        embed=discord.Embed(title="Goods Prices", color=discord.Color.orange())
        embed.add_field(name="Brazil", value="Rum: 60 \nCoffee: 26\n Spice: 25 \n Silk: 150", inline=True)
        embed.add_field(name="Guinea", value="Rum: 38 \nCoffee: 22 \nSpice: 22\nSilk: 310", inline=True)
        embed.add_field(name="Labrador", value="Rum: 48 \nCoffee: 40 \nSpice: 14\nSilk: 230", inline=True)
        embed.add_field(name="Spain", value="Rum: 52 \nCoffee: 65 \nSpice: 53\nSilk: 180", inline=True)
        embed.add_field(name="Jamaica", value="Rum: 32 \nCoffee: 70 \nSpice: 40\nSilk: 240", inline=True)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Krew(bot))
