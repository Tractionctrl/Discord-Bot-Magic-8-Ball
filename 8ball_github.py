import discord
from discord.ext import commands

# Create a new bot using the `commands.Bot` class
bot = commands.Bot(command_prefix='/')

# Define a list of responses that the 8 ball can choose from
responses = [
    "It is certain.",
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
    "Very doubtful.",
    "Bitch it might!",
    "It all points to drinking alone tonight... You should do that.",
    "Nah",
    "Yuuuuuuuuuuuuuuuurrrrrrrr",
    "They let people like you vote?",
    "Are you dense?",
    "Fuck you",
    "Sumn like that",
    "Does your mom know you asked that?",
    "Basically",
    "Try again",
    "Try it",
    "Fuck around and find out",
    "Ed says yes"
]

# Create a new command called `shake` using the `bot.command` decorator
@bot.command(name='shake')
async def shake(ctx):
    # Use the `ctx.send` method to send a random response from the list
    await ctx.send(f"TractionCTRL's 8-ball says: {random.choice(responses)}")

# Start the bot
bot.run('YOUR_TOKEN_HERE')