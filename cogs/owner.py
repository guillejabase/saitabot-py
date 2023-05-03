from __future__ import annotations
from typing import TYPE_CHECKING
from discord.ext import commands
import os
import discord

if TYPE_CHECKING:
    from main import Saita


class Owner(commands.Cog):
    'This cog has commands for the bot developer.'

    def __init__(self, bot: Saita):
        self.bot: Saita = bot

    def im_developer(interaction: discord.Interaction):
        return interaction.user.id == interaction.client.application.owner.id

    color = 2829617

    @discord.app_commands.command(
        name='reload',
        description='Reload all cogs.'
    )
    @discord.app_commands.check(im_developer)
    async def reload(self, interaction: discord.Interaction):
        embed = discord.Embed(color=self.color)

        for file in os.listdir('./cogs'):
            try:
                if file.endswith('.py'):
                    await self.bot.reload_extension(f'cogs.{file[:-3]}')
            except commands.ExtensionError as error:
                embed.description = '{}: {}'.format(
                    type(error).__name__, error)

                break
            else:
                embed.description = '**All cogs has been reloaded.**'

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Owner(bot))
