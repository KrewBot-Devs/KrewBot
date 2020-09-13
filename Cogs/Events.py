import discord
from discord.ext import commands
from discord.utils import get
import classyjson as cj
bot = commands.Bot(command_prefix='!k ')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name='Krew.io | https://github.com/KrewBot-Devs/KrewBot', type=3)
        await self.bot.change_presence(status=discord.Status.online, activity=activity)


    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(
            embed = discord.Embed(color=discord.Color.orange(), description='`Pls use !k to use a command.`'))
            await bot.process_commands(message)



    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name="🚪front-door")
        await channel.send(f"Everyone welcome {member.mention} aboard!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = get(member.guild.channels, name="🚪front-door")
        await channel.send(f"{member.mention} has abandoned ship.")
    @commands.Cog.listener()#message when joins guild
    async def on_guild_join(self, guild):
        await asyncio.sleep(1)
        if guild.system_channel is not None:
            try:
                await guild.system_channel.send(embed=discord.Embed(color=discord.Color.green(),
                                                                    description="Whats up guy, I'm KrewBot, a [Krew.io](Krew.io) themed bot, use !k help to get started."
                                                                                "Want a feature? [Submit a pull request.](https://github.com/KrewBot-Devs/KrewBot)"))
            except discord.errors.Forbidden:
                pass

    @commands.Cog.listener()
    async def on_guild_join(self, ctx, pass_context=True):
        data = {}
        data[ctx.message.guild] = ({
            'dojoinleave': False,
            'announcechannel': str(guild.system_channel)
        })
        with open('data/config.json','r') as config_stuffs:
            cj.dump(data, config_stuffs)
            print(data)





def setup(bot):
    bot.add_cog(Events(bot))
