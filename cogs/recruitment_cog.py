import discord
from discord.ext import commands
from discord.ui import Select, View

class RecruitmentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("RecruitmentCog is ready")
        print("----------------")

    @commands.command()
    async def recruit(self, ctx):
        select = Select(
            options=[
                discord.SelectOption(
                    label="Lander Application",
                    emoji="📄",
                    description="Have you completed your application to Lander?"
                ),
                discord.SelectOption(
                    label="Recruitment Form",
                    emoji="📄",
                    description="Have you completed your Recruiting Form?"
                ),
                discord.SelectOption(
                    label="Transcripts",
                    emoji="📄",
                    description="Have you submitted your transcript?"
                ),
                discord.SelectOption(
                    label="Test Scores",
                    emoji="📄",
                    description="Have you sent your test scores?"
                ),
                discord.SelectOption(
                    label="FAFSA",
                    emoji="📄",
                    description="Have you completed your FAFSA form?"
                ),
                discord.SelectOption(
                    label="Accepted Student",
                    emoji="📄",
                    description="Have you been accepted to Lander?"
                ),
                discord.SelectOption(
                    label="ARMS Registration",
                    emoji="📄",
                    description="Have you registered on ARMS for scholarship?"
                ),
                discord.SelectOption(
                    label="Sign Esports Scholarship",
                    emoji="📄",
                    description="Have you signed your esports scholarship?"
                ),
                discord.SelectOption(
                    label="Housing Application",
                    emoji="📄",
                    description="Have you finished your housing application?"
                ),
                discord.SelectOption(
                    label="Class Enrollment",
                    emoji="📄",
                    description="Have you enrolled in all your classes?"
                ),
            ]
        )

        async def select_callback(interaction):
            await interaction.response.send_message(f"You selected: {select.values[0]}")

        select.callback = select_callback
        view = View()
        view.add_item(select)

        await ctx.send("Choose the desired portion of the application process", view=view)


# This is required for the bot to load the cog
async def setup(bot):
    await bot.add_cog(RecruitmentCog(bot))
