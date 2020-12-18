import discord
from random import choice
import random
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = '.', intents = intents)




@client.event
async def on_ready():
    print('Bot is ready. ')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@client.command()
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

# Moderation Commands

@client.command()
async def clear(ctx, amount=5):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(title="Messages Have Been Cleared!", color=0xf90101)
        embed.set_footer(text="Solar Moderation")
        await ctx.send(embed=embed)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).kick_members):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f"{member} Has been kicked successfully", color=0xf90101)
        embed.set_footer(text="Solar Moderation ")
        await ctx.send(embed=embed)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
        await member.ban(reason=reason)
        embed=discord.Embed(title=f"{member} Has been banned successfully", color=0xf90101)
        embed.set_footer(text="Solar Moderation ")
        await ctx.send(embed=embed)

@client.command()
async def unban(ctx, *, member):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed=discord.Embed(title=f"{user.mention} Has been unbanned successfully!", color=0xf90101)
            embed.set_footer(text="Solar Moderation ")
            await ctx.send(embed=embed)
            return


# Moderation Commands

@client.command()
async def apply(ctx):
    embed=discord.Embed(title="How to apply for staff", description="If you are interested in joining our staff team make sure to read this!", color=0x05ff44)
    embed.add_field(name="Discord Moderation Team", value="We are sorry to inform you the Moderation applications are closed for the Discord Team. We will announce once they open again.", inline=False)
    embed.add_field(name="Minecraft Moderation Team", value="If you are interested in joining the Minecraft Moderation team please navigate yourself to this page   https://netsolar.cf/apply/", inline=True)
    embed.set_footer(text="Solar Information ")
    await ctx.send(embed=embed)

@client.command()
async def staff(ctx):
    embed=discord.Embed(title="Our Management and Staff Team", description="This is a list of our hard working staff and management members!", color=0x05ff44)
    embed.add_field(name="Allekup", value="The Current Network Owner and Founder of Solar Networks.", inline=False)
    embed.add_field(name="WarStylez", value="The Current Network Manager of Solar Networks.", inline=True)
    embed.add_field(name="Scout", value="The Current Discord Manager for Solar Networks.", inline=True)
    embed.add_field(name="Creeperchu", value="The Current Server Owner of one of our Minecraft Servers.", inline=True)
    embed.add_field(name="z_8", value="The Current Head-Builder of the Netsolar Minecraft Server.", inline=True)
    embed.add_field(name="Hamish", value="A Discord Moderator for the Solar Network Discords.", inline=True)
    embed.add_field(name="Pure Salt HLM", value="A Discord Moderator for the Solar Network Discords.", inline=True)
    embed.add_field(name="qlukaas", value="A Discord Moderator for the Solar Network Discords.", inline=True)
    embed.add_field(name="brêg", value="A Senior Builder for the Netsolar Minecraft server.", inline=True)
    embed.add_field(name="ColorClicker", value="A Builder for the Netsolar Minecraft server.", inline=True)
    embed.set_footer(text="Solar Information ")
    await ctx.send(embed=embed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    embed=discord.Embed(title=f'**Question:** *{question}*\n\n**Answer:** *{random.choice(responses)}*', color=0xf90101)
    embed.set_footer(text="Solar Fun ")
    await ctx.send(embed=embed)

client.run('Nzg3MjU2NDkyMDI4OTg1Mzc1.X9STvg.2l1LfMjt2yzQn_h_cNLHnU36f8I')
