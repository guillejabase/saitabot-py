import os
import discord
from discord.ext import commands
from assets import config

class Saita(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "s!",
            help_command = None,
            intents = discord.Intents.all(),
            application_id = config.app_id
        )

        self.config = config
    
    async def setup_hook(self):
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension(f"cogs.{file[:-3]}")
        
        await bot.tree.sync()
    
    async def on_ready(self):
        print(f"{self.user} online.")

bot = Saita()

@bot.tree.error
async def on_command_error(interaction: discord.Interaction, exception: discord.app_commands.AppCommandError):
    if isinstance(exception, discord.app_commands.BotMissingPermissions):
        embed = discord.Embed(color = discord.Color.red, description = exception)

        await interaction.response.send_message(embed = embed, ephemeral = True)

bot.run(config.token)