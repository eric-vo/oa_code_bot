import os

from dotenv import load_dotenv
import discord
from discord import app_commands

# Get variables from .env file
load_dotenv()
token = os.environ['TOKEN']
logo_url = os.environ['LOGO_URL']
logo_square_url = os.environ['LOGO_SQUARE_URL']

# Set guild ID
GUILD_ID = 1016499658471780392

# Set up logging
discord.utils.setup_logging()

# Set intents
intents = discord.Intents.default()
intents.members = True

# Create client with intents and set up slash commands
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
# commands_synced = False


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    # global commands_synced
    # if not commands_synced:
    #     await tree.sync(guild=discord.Object(id=GUILD_ID))
    #     commands_synced = True


@client.event
async def on_member_join(member):
    guild = client.get_guild(GUILD_ID)
    general_channel = guild.get_channel(1016499658962501674)

    # Create welcome embed
    embed = discord.Embed(
        color=discord.Color.blue(),
        title=f"Welcome to OA Code, {member.display_name}!",
        description="Be sure to read <#1016514622943146054>, " +
                    "and enjoy your stay! " +
                    "Let's make some awesome stuff this year! :D",
        timestamp=member.joined_at
    )
    embed.set_image(url=logo_url)
    embed.set_footer(text=member, icon_url=member.display_avatar)

    await general_channel.send(member.mention, embed=embed)


# Slash commands
@tree.command(description="Sends contact information for OA Code.",
              guild=discord.Object(id=GUILD_ID))
async def contact(interaction: discord.Interaction):
    embed = discord.Embed(
        color=discord.Color.blue(),
        title="Contact OA Code",
        description="Here is our contact information!",
    )

    embed.set_thumbnail(url=logo_square_url)

    embed.add_field(
        name="Instagram",
        value=("<:instagram:1019078879396249620> " +
               "[@oa.code](https://www.instagram.com/oa.code/)"),
        inline=False
    )
    embed.add_field(
        name="Discord",
        value=("<:discord:1019079092995362867> " +
               "[is.gd/oacodediscord](https://is.gd/oacodediscord)"),
        inline=False
    )

    embed.add_field(
        name="Anna Lee (President)",
        value=("📧 1040030@student.auhsd.us"),
        inline=False
    )
    embed.add_field(
        name="Angelina Zhang (President)",
        value=("📧 1041599@student.auhsd.us"),
        inline=False
    )
    embed.add_field(
        name="Mr. Wai (Advisor)",
        value=("📧 wai_j@auhsd.us"),
        inline=False
    )

    await interaction.response.send_message(embed=embed)

client.run(token)
