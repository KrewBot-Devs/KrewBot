import discord
from discord.ext import commands
from discord.utils import get
import KrewMain



bot = commands.Bot(command_prefix='!k ')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    server = len(self.bot.guilds)

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name=f'{server}', type=3)
        await self.bot.change_presence(status=discord.Status.online, activity=activity)


    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(
            embed = discord.Embed(color=discord.Color.orange(), description=f'`Pls use {KrewMain.get_prefixes(bot, message)} to use a command.`'))
            await bot.process_commands(message)



    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name="join-leave")
        await channel.send(f"Everyone welcome {member.mention} aboard!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = get(member.guild.channels, name="join-leave")
        await channel.send(f"{member.mention} has abandoned ship.")


    @bot.event
    async def on_guild_join(guild):
        with open('data/joinleave.json', 'r') as f:
            jlc = cj.load(f)


        jlc[str(guild.id)] = 'join-leave'

        with open('data/joinleave.json', 'w') as f:
            cj.dump(jlc, f, indent=4)


    @bot.event
    async def on_guild_remove(guild):
        with open('data/joinleave.json', 'r') as f:
            pjlc = cj.load(f)

            jlc.pop(str(guild.id))

            with open('data/joinleave.json', 'w') as f:
                cj.dump(jlc, f, indent=4)






def setup(bot):
    bot.add_cog(Events(bot))
