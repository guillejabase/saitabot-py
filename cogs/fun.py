from __future__ import annotations
from typing import TYPE_CHECKING
from discord.ext import commands
import discord
import random

if TYPE_CHECKING:
    from main import Saita

class Fun(commands.Cog):
    """This Cog has commands made for fun and enjoyment."""

    def __init__(self, bot: Saita):
        self.bot: Saita = bot

    @discord.app_commands.command(name = "eightball", description = "Ask the magic 8 ball a question.")
    @discord.app_commands.describe(question = "Type a question.")
    async def eightball(self, interaction: discord.Interaction, question: discord.app_commands.Range[str, 0, 1000]):
        if not question.endswith("?"):
            question = f"{question}?"

        answers = [
            "Yes.", "No.",
            "✨ Y E S ✨", "✨ N O ✨", "✨ I D K ✨",
            "✨ A L W A Y S ✨", "✨ N E V E R ✨",
            "Always.", "Never.",
            "I don't know.", "Possibly.",
            "Maybe.", "Better change the question.",
            "WTF.", "???",
            "This is an 8ball, not a reality changer.", "Nice question ngl.",
            "I don't understand.", "Well as you can see, the grass is green too. Wait- you've never seen it!",
            "Another question like this and I'll blacklist you.", "SHUT UP!", "I DON'T KNOW!"
        ]

        embed = discord.Embed(color = 2829617, description = f"**Question:** {question}\n\n**Answer:** {random.choice(answers)}")

        await interaction.response.send_message(embed = embed)

    @discord.app_commands.command(name = "percentage", description = "Calculate how much something is someone.")
    @discord.app_commands.describe(target = "Type in what or who you want to calculate the percentage of.", input = "Type in what you want to calculate.")
    async def percentage(self, interaction: discord.Interaction, target: discord.app_commands.Range[str, 0, 500], input: discord.app_commands.Range[str, 0, 500]):
        embed = discord.Embed(color = 2829617, description = f"{target} is **{random.randint(0, 100)}%** {input}.")

        await interaction.response.send_message(embed = embed)

    @discord.app_commands.command(name = "rate", description = "Let me rate something from 1 to 5.")
    @discord.app_commands.describe(input = "Type in what you want to rate.")
    async def rate(self, interaction: discord.Interaction, input: discord.app_commands.Range[str, 0, 500]):
        number = round(random.uniform(1, 5), 1)
        text = "stars"

        if number < 1.1:
            text = "star"

        embed = discord.Embed(color = 2829617, description = f"I rate {input} **{number} {text}**.")

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))