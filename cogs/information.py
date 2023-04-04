from __future__ import annotations
from typing import TYPE_CHECKING
from discord.ext import commands
import discord

if TYPE_CHECKING:
    from main import Saita

class Information(commands.Cog):
    """This Cog has commands that show information from different sources."""

    def __init__(self, bot: Saita):
        self.bot: Saita = bot

    @discord.app_commands.command(name = "ping", description = "Check the latency of the bot.")
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(color = 2829617, description = f"**Latency:** {round(self.bot.latency * 1000)} ms.")

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Information(bot))