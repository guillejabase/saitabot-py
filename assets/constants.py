import discord

user_flags = {
    discord.UserFlags.partner: 'Partner',
    discord.UserFlags.staff: 'Staff',
    discord.UserFlags.bug_hunter: 'Bug Hunter Level 1',
    discord.UserFlags.bug_hunter_level_2: 'Bug Hunter Level 2',
    discord.UserFlags.hypesquad: 'HypeSquad Events',
    discord.UserFlags.hypesquad_bravery: 'Bravery HypeSquad',
    discord.UserFlags.hypesquad_brilliance: 'Brilliance HypeSquad',
    discord.UserFlags.hypesquad_balance: 'Balance HypeSquad',
    discord.UserFlags.early_supporter: 'Early Supporter',
    discord.UserFlags.verified_bot_developer: 'Verified Bot Developer',
    discord.UserFlags.discord_certified_moderator: 'Certified Moderator',
    discord.UserFlags.active_developer: 'Active Developer',
    discord.UserFlags.spammer: 'Spammer',
    discord.UserFlags.verified_bot: 'Verified Bot',
    discord.UserFlags.bot_http_interactions: 'Bot HTTP Interactions',
    discord.UserFlags.team_user: 'Team User'
}

member_status = {
    discord.Status.online: 'Online',
    discord.Status.idle: 'Idle',
    discord.Status.do_not_disturb: 'Do Not Disturb',
    discord.Status.invisible: 'Invisible',
    discord.Status.offline: 'Offline'
}

member_activity_type = {
    discord.ActivityType.playing: 'Playing',
    discord.ActivityType.competing: 'Competing',
    discord.ActivityType.listening: 'Listening',
    discord.ActivityType.streaming: 'Streaming',
    discord.ActivityType.watching: 'Watching'
}

guild_features = {
    'ANIMATED_BANNER': 'Animated banner',
    'ANIMATED_ICON': 'Animated icon',
    'APPLICATION_COMMAND_PERMISSIONS_V2': 'App command permissions v2',
    'AUTO_MODERATION': 'Auto moderation',
    'BANNER': 'Banner',
    'COMMUNITY': 'Community',
    'CREATOR_MONETIZABLE_PROVISIONAL': 'Creator monetizable provisional',
    'CREATOR_STORE_PAGE': 'Creator store page',
    'DEVELOPER_SUPPORT_SERVER': 'Developer support server',
    'DISCOVERABLE': 'Discoverable',
    'FEATURABLE': 'Featurable',
    'INVITES_DISABLED': 'Invites disabled',
    'INVITE_SPLASH': 'Invite splash',
    'MEMBER_VERIFICATION_GATE_ENABLED': 'Member verification gate enabled',
    'MORE_STICKERS': 'More stickers',
    'NEWS': 'News',
    'PARTNERED': 'Partnered',
    'PREVIEW_ENABLED': 'Preview enabled',
    'ROLE_ICONS': 'Role icons',
    'ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE': 'Role subscriptions avaivable for purchase',
    'ROLE_SUBSCRIPTIONS_ENABLED': 'Role subscriptions enabled',
    'TICKETED_EVENTS_ENABLED': 'Ticketed events enabled',
    'VANITY_URL': 'Vanity URL',
    'VERIFIED': 'Verified',
    'VIP_REGIONS': 'VIP regions',
    'WELCOME_SCREEN_ENABLED': 'Welcome screen enabled',
    'TEXT_IN_VOICE_ENABLED': 'Text in voice enabled'
}

guild_mfa_level = {
    discord.MFALevel.require_2fa: 'Enabled',
    discord.MFALevel.disabled: 'Disabled'
}

guild_explicit_content_filter = {
    discord.ContentFilter.all_members: 'All members',
    discord.ContentFilter.no_role: 'No role',
    discord.ContentFilter.disabled: 'Disabled'
}

guild_nsfw_level = {
    discord.NSFWLevel.safe: 'Safe',
    discord.NSFWLevel.age_restricted: 'Age restricted',
    discord.NSFWLevel.default: 'Default',
    discord.NSFWLevel.explicit: 'Explicit',
}