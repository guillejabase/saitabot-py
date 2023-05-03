from __future__ import annotations
from typing import TYPE_CHECKING
from discord.ext import commands
import assets.constants as constants
import datetime
import discord

if TYPE_CHECKING:
    from main import Saita


class Information(commands.Cog):
    'This Cog has commands that show information from different sources.'

    def __init__(self, bot: Saita):
        self.bot: Saita = bot

    color = 2829617

    @discord.app_commands.command(
        name='ping',
        description='Check the latency of the bot.'
    )
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=self.color,
            description=f'**Latency:** {round(self.bot.latency * 1000)} ms.'
        )

        await interaction.response.send_message(embed=embed)

    @discord.app_commands.command(
        name='about',
        description='About me.'
    )
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=self.color,
            description=f'''**Developer:** Willyy#9111
**Language:** Python
**Library:** discord.py v2.2.2'''
        )

        await interaction.response.send_message(embed=embed)

    @discord.app_commands.command(
        name='userinfo',
        description='Show all the info about any user.'
    )
    @discord.app_commands.describe(
        user='Choose user with mention or ID.'
    )
    async def userinfo(
        self,
        interaction: discord.Interaction,
        user: discord.User = None
    ):
        user = await self.bot.fetch_user(user.id if user else interaction.user.id)
        created_timestamp = round(user.created_at.timestamp())
        member = interaction.guild.get_member(user.id)
        joined_timestamp = round(member.joined_at.timestamp())

        user_embed = discord.Embed(
            color=self.color,
            description=f'''__**User information**__

**Tag:** {user}
**ID:** {user.id}
**Type:** {'Bot' if user.bot else 'User'}
**Flags:** {', '.join(list(map(lambda flag: constants.user_flags[flag], user.public_flags.all()))) or None}
**Created at:** <t:{created_timestamp}> (<t:{created_timestamp}:R>)'''
        )

        user_embed.set_thumbnail(
            url=user.avatar.url
        ) if user.avatar else None
        user_embed.set_image(
            url=user.banner.url
        ) if user.banner else None

        if member:
            client_status = []
            custom_status = None
            activities = []

            if member.status != discord.Status.offline:
                if member.desktop_status != discord.Status.offline:
                    client_status.append(
                        f'\n> **Desktop:** {constants.member_status[member.desktop_status]}'
                    )

                if member.mobile_status != discord.Status.offline:
                    client_status.append(
                        f'\n> **Mobile:** {constants.member_status[member.mobile_status]}'
                    )

                if member.web_status != discord.Status.offline:
                    client_status.append(
                        f'\n> **Web:** {constants.member_status[member.web_status]}'
                    )

                if member.activities:
                    def chop_microseconds(delta: datetime.timedelta):
                        return delta - datetime.timedelta(microseconds=delta.microseconds)

                    for activity in member.activities:
                        if isinstance(activity, discord.CustomActivity):
                            custom_status = activity
                        elif isinstance(activity, discord.Spotify):
                            activities.append(f'''
> **{constants.member_activity_type[activity.type]} *{activity.title}***
> **Duration:** {chop_microseconds(activity.duration)}
> **Artist/s:** {', '.join(activity.artists)}
> **Album:** {activity.album}\n''')
                        elif isinstance(activity, discord.Game):
                            activities.append(f'''
> **{constants.member_activity_type[activity.type]} {activity.name}**
> **Started:** <t:{round(activity.start.timestamp())}:R>\n''')
                        elif isinstance(activity, discord.Activity):
                            activities.append(f'''
> **{constants.member_activity_type[activity.type]} {activity.name}**
> **Started:** <t:{round(activity.start.timestamp())}:R>\n''')

            member_embed = discord.Embed(
                color=self.color,
                description=f'''__**Member information**__

**Nick:** {member.nick}
**Boosting:** {f'<t:{round(member.premium_since)}:R>' if member.premium_since else 'No'}
**Joined at:** <t:{joined_timestamp}> (<t:{joined_timestamp}:R>)

**Roles:** {f"""({len(member.roles) - 1})
{' '.join(role.mention for role in member.roles if role.id != interaction.guild.id)}""" if len(member.roles) > 1 else None}

**Status:** {f"""{''.join(client_status)}
**Custom status:** {custom_status}
**Activities:** {''.join(activities) if activities else None}""" if member.status != discord.Status.offline else 'Offline/Invisible'}'''
            )

            member_embed.set_thumbnail(
                url=member.guild_avatar.url
            ) if member.guild_avatar else None

            await interaction.response.send_message(embeds=[user_embed, member_embed])
        else:
            await interaction.response.send_message(embed=user_embed)

    @discord.app_commands.command(
        name='serverinfo',
        description='Show all the info about this server.'
    )
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        created_timestamp = round(guild.created_at.timestamp())
        users = list(filter(
            lambda member: not member._user.bot, guild.members
        ))
        bots = list(filter(
            lambda member: member._user.bot, guild.members
        ))
        online_users = list(filter(
            lambda user: user.status != discord.Status.offline, users
        ))
        offline_users = list(filter(
            lambda user: user.status == discord.Status.offline, users
        ))
        online_bots = list(filter(
            lambda bot: bot.status != discord.Status.offline, bots
        ))
        offline_bots = list(filter(
            lambda bot: bot.status == discord.Status.offline, bots
        ))
        regular_emojis = list(filter(
            lambda emoji: not emoji.animated, guild.emojis
        ))
        animated_emojis = list(filter(
            lambda emoji: emoji.animated, guild.emojis
        ))

        embed = discord.Embed(
            color=self.color,
            description=f'''__**Server information**__

**Name:** {guild.name}
**ID:** {guild.id}
**Description:** {guild.description}
**Boosted:** {f'{guild.premium_subscription_count} (lvl {guild.premium_tier})' if guild.premium_subscribers else 'No'}
**Features:** {', '.join(list(map(lambda feature: constants.guild_features[feature], guild.features)))}
**Created at:** <t:{created_timestamp}> (<t:{created_timestamp}:R>)

**Moderation 2FA:** {constants.guild_mfa_level[guild.mfa_level]}
**Explicit content filter:** {constants.guild_explicit_content_filter[guild.explicit_content_filter]}
**NSFW:** {constants.guild_nsfw_level[guild.nsfw_level]}

**Members:** ({guild.member_count})
> **Users:** {len(users)} (Online: {len(online_users)}, Offline: {len(offline_users)})
> **Bots:** {len(bots)} (Online: {len(online_bots)}, Offline: {len(offline_bots)})

**Emojis:** {len(guild.emojis)} (Regular: {len(regular_emojis)}, Animated: {len(animated_emojis)})
**Stickers:** {len(guild.stickers)}

**Roles:** ({len(guild.roles) - 1})
{' '.join(role.mention for role in guild.roles if role.id != guild.id)}

**Channels:** ({len(guild.channels)})
> **Categories:** {len(guild.categories)}
> **Text:** {len(guild.text_channels)}
> **Voice:** {len(guild.voice_channels)}'''
        )

        embed.set_thumbnail(
            url=interaction.guild.icon.url
        ) if interaction.guild.icon else None

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Information(bot))
