import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__ (self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCog is ready")
        print("________________")

    @commands.command(name ="bchelp", help = "Displays all available bot commands.")
    async def bchelp(self,ctx):
        prefix = self.bot.command_prefix
        embed = discord.Embed(
            title = "Bot Command Help",
            description = " Here is a list of all commands and their descriptions:",
            color = 0x3498db
        )

        for cog_name, cog in self.bot.cogs.items():
            command_list = cog.get_commands()
            if command_list:
                command_info = "\n".join(
                    [f"{prefix}{command.name}: {command.help}" for command in command_list]
                )
                embed.add_field(name = f"{cog_name} Commands", value= command_info, inline = False)
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
