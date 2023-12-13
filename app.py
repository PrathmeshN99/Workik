import discord
from discord.ext import commands
import mysql.connector

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'discord_bot_db',
}

try:
    db_conn = mysql.connector.connect(**db_config)
    db_cursor = db_conn.cursor()


except mysql.connector.Error as err:
    print(f"Error: {err}")


# Initialize the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=intents)



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    channel_id = 1184427500307234890  
    
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send(f'Hello! I am now connected as {bot.user.name}')
    else:
        print(f"Error: Channel with ID {channel_id} not found.")


# Bot command: !hello

@bot.command(name='hello')
async def hello(ctx):
    print("Hello command executed!")
    
    if ctx.guild is None:
        print("Error: Command cannot be used in private messages. Please use it in a server.")
        await ctx.send('This command cannot be used in private messages. Please use it in a server.')
        return

    server_id = ctx.guild.id
    print(f"Server ID: {server_id}")
    
    try:
        db_cursor.execute('SELECT token FROM auth_tokens WHERE server_id = %s', (server_id,))
        result = db_cursor.fetchone()
        print(f"Database Query Result: {result}")

        if result:
            await ctx.send(f'Hello World! This is {ctx.guild.name}')
        else:
            await ctx.send('Unauthorized. Please authenticate the bot in this server.')

    except Exception as e:
        print(f"Error in database query: {e}")
        await ctx.send('An error occurred. Please try again later.')


@bot.command(name='test')
async def test_command(ctx):
    print("Hello command executed!")
    await ctx.send("Test command executed!")

# Run the bot
bot.run('MTE4NDQyNTEyODAxNzI4NTE3MQ.GyYpQw.ZM2zEfMLt1DsMKh5Lxs_benl2UoaYlohWyhuOY')

