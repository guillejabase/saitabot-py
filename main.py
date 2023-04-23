import os
import discord
from discord.ext import commands
from assets import config

class SaitaTree(discord.app_commands.CommandTree):
    async def on_error(
        self,
        interaction: discord.Interaction,
        error: discord.app_commands.AppCommandError
    ):
        if isinstance(
            error,
            discord.app_commands.BotMissingPermissions
        ):
            missing = [
                perm
                .replace('_', ' ')
                .replace('guild', 'server')
                .title()
                for perm in error.missing_permissions
            ]

            if len(missing) > 2:
                permissions = '{}, and {}'.format(
                    ', '.join(missing[:-1]),
                    missing[-1]
                )
            else:
                permissions = ' and '.join(missing)

            embed = discord.Embed(
                color=2829617,
                description=f'I need **{permissions}** permissions to run this command.'
            )

            await interaction.response.send_message(embed=embed)
        else:
            await super().on_error(
                interaction,
                error
            )


class Saita(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='s!',
            help_command=None,
            intents=discord.Intents.all(),
            application_id=config.app_id,
            tree_cls=SaitaTree
        )

        self.config = config

    async def setup_hook(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

        await bot.tree.sync()

    async def on_ready(self):
        print(f'{self.user} online.')


bot = Saita()

bot.run(config.token)
