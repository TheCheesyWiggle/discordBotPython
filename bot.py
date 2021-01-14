import discord
from discord.ext import commands
from discord.ext import tasks
import random
from itertools import cycle

token = ""

bot = commands.Bot(command_prefix = '.')


@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(activity = discord.Streaming(name="Minecraft", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
#@bot.event
#async def on_member_join(member):
#    print(f'{member} has joined a server')

#@bot.event
#async def on_member_remove(member):
#    print(f'{member} has left a server')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong {round(bot.latency*1000)}ms')
#############################################################    
@bot.command(aliases = ['8ball','eightball','8bollock'])
async def _8ball(ctx,*,question):
    responses =['It is certian',
                'Without a doubt',
                'You may rely on it',
                'Yes definitely',
                'It is decidedly so',
                'As I see it, yes',
                'Yes',
                'Most likey',
                'Outlook good',
                'Signs point to yes',
                'Reply hazy try again',
                'Better not tell you now',
                'Ask again later',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don’t count on it',
                'Outlook not so good',
                'My sources say no',
                'Very doubtful',
                'My reply is no']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
############################################################
@bot.command(aliases = ['rockpaperscissors','RPS','rps'])
async def _rps (ctx,*,choice):

    comp = random.randint(0,2)

    if comp == 0:
        await ctx.send("Computer chose: Rock")
    elif comp == 1:
        await ctx.send("Computer chose: Paper")
    elif comp == 2:
        await ctx.send("Computer chose: scissors")
    else:
        print("Something went wrong try again")

    if choice == "rock":
        if comp == 0:
            await ctx.send("Its a draw")
        elif comp == 1:
            await ctx.send("The computer wins!")
        elif comp == 2:
            await ctx.send("You win!")
        else:
            await ctx.send("Something went wrong try again")

    if choice == "paper":
        if comp == 1:
            await ctx.send("Its a draw")
        elif comp == 2:
            await ctx.send("The computer wins!")
        elif comp == 0:
            await ctx.send("You win!")
        else:
            await ctx.send("Something went wrong try again")

    if choice == "scissors":
        if comp == 2:
            await ctx.send("Its a draw")
        elif comp == 0:
            await ctx.send("The computer wins!")
        elif comp == 1:
            await ctx.send("You win!")
        else:
            await ctx.send("Something went wrong try again")
##############################################

    


    

    
bot.run(token)
