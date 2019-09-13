import discord
import datetime
from discord.ext import commands
from random import *
import json
import random
import requests
import asyncio
import aiohttp
from datetime import date
import time
import wikipedia
import dataIO

bot = commands.Bot(command_prefix='.')
today = datetime.date.today()
@bot.event
async def on_ready():
    game = discord.Game("Killing Saracens")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    guilds = await bot.fetch_guilds(limit=150).flatten()
    print(guilds) 
    print('------')

#---------------------------------PurgeMessages------------------------------
@bot.command()
async def purge(ctx, number: int):
	deleted = await ctx.channel.purge(limit=number)
	await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))
	time.sleep(3)
	await ctx.channel.purge(limit=1)
	print("Someone purged some messages")

#---------------------------------Advertise--------------------------------------
@bot.command(description="This command announces something to everyones dms!",aliases=["tell","dm all","announcement"])
async def dm(ctx,*,message:str):
    for member in ctx.guild.members
            try:
                await member.send(message)
                print(f"{member} recieved the message!")
            except:
                print(f"{member} has their dms closed")


#---------------------------------CreateRole---------------------------------------------
@bot.command()
async def role(ctx, message:str):
	guild = ctx.guild
	perms = discord.Permissions()
	perms.update(administrator=False)
	await guild.create_role(name=message, colour=discord.Colour(0x00d1a0))
	print("Someone created a role")
#------------------------------------GiveRole--------------------------------------------
@bot.command()
async def giverole(ctx, message:discord.Role):
	await ctx.message.author.add_roles(message)
	print("Someone used give role")
	await ctx.channel.purge(limit=1)
#--------------------------------------Servers-----------------------------------------
#--------------------------------------------Filter-------------------------------------
'''
@bot.event
async def on_message(message):
    contents = message.content.split("") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await bot.delete_message(message)
                    await bot.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
'''
#-------------------------------------------Joined----------------------------------------
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
    print("Someone joined")
#---------------------------------------Server Info----------------------------------------
@bot.command()
async def server(ctx):
	embed = discord.Embed(title="ServerInfo", description="History of this server", color=0x2ecc71)
	embed.add_field(name="ServerCreationTime:", value="test", inline=False)
	embed.add_field(name="NumberOfPeople:", value= len(set(bot.get_all_members())), inline=False)

	await ctx.send(embed=embed)
	print("Someone used server")

#-------------------------------------Mute-User---------------------------------------

@bot.command()
async def mute(ctx, member : discord.Member, *, reason=None):
	role6 = discord.utils.get(ctx.guild.roles, name="muted")
	await member.add_roles(role6)
	print("Someone used mute")
#---------------------------------------Date--------------------------------------
@bot.command()
async def date(ctx):
    await ctx.send(today.strftime('%b %d %Y'))
    print("Someone used date")

#--------------------------------------Circumcise--------------------------------------
'''
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@bot.command()
async def ban(ctx):
	await ctx.message.delete()
	for user in list(ctx.guild.members):
		try:
			await ctx.guild.ban(user)
			print (f"{user.name} has been kicked from {ctx.guild.name}")
		except:
			print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")

		print ("Action Completed: Everyone Has Been Circumcised")
'''
#---------------------------Info-------------------------------------------------------

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="𝐏𝐡𝐨𝐞𝐧𝐢𝐱", description="Simplifies the server managment scene while also adding some fun games", color=0xf40f6b)

    # give info about you here
    embed.add_field(name="Author", value="Technic_Smile")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    #Creation Date of Bot
    embed.add_field(name="Bot was created in", value="9/1/19")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite the bot to your server", value="https://discordapp.com/api/oauth2/authorize?client_id=618180011370872885&permissions=8&scope=bot")

    await ctx.send(embed=embed)
    print("Someone used info")

bot.remove_command('help')
#Icode
#------------------------------------Help---------------------------------------------

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="__**Phoenix**__", description="Phoenix is a powerful tool to try and simplify your server tasks and improve the server quality here are a list of current commands.", color=0x44CC77)

    embed.add_field(name='-games', value="Brings up game library.", inline=False)
    embed.add_field(name='-art', value="Brings up ascii art emotes.", inline=False)
    embed.add_field(name='-manage',value="For managing your server.")
    embed.add_field(name='-misc',value="Server management commands")  
    embed.add_field(name="-server", value="Gives information about the server.", inline=False)
    embed.add_field(name='-joined "user"', value="Shows the date, time, and year a user joined.", inline=False)
    embed.add_field(name="-info", value="Lists bot information.", inline=False) 
    await ctx.send(embed=embed)

    print("Someone used help")
#----------------------------------------------Management---------------------------
@bot.command()
async def manage(ctx):
    embed = discord.Embed(title="__**Management**__", description="Here are a list of commands to help you manage and improve the quality of your discord server.", color=0x1D242E)
    embed.add_field(name='-role "name"', value="Creates a custom role.", inline=False)
    embed.add_field(name='-giverole "rolename"', value="Gives user the role of their choosing.", inline=False)
    embed.add_field(name='-purge "number"', value="Deletes any number of messages.", inline=False)
    embed.add_field(name='-announce "message"', value="Messages the entire server with a custom messge.", inline=False)
    embed.add_field(name='-mute "user"', value="Mutes user.", inline=False)
    

    await ctx.send(embed=embed)
    print("Someone used manage")
#----------------------------------------------Misc---------------------------------
@bot.command()
async def misc(ctx):
    embed = discord.Embed(title="__**Misc**__", description="All of the commands that dont fit to a catagory.", color=0x1084C1)
    embed.add_field(name="-date", value="Tells you todays date.", inline=False)


    await ctx.send(embed=embed)
    print("Someone used misc")
#---------------------------------------------Games----------------------------------

@bot.command()
async def games(ctx):
    embed = discord.Embed(title="__**Games**__", description="Here is a list of the current game library.", color=0xF6B92B)
    embed.add_field(name='art_plane', value="Russian roulette is a classic game, but theres a twist with this version it has a chance to kick you.", inline=False) 
    embed.add_field(name="rps (rock/paper/scissors)", value="A classic game of rock, paper, scissors.",inline=False)
    embed.add_field(name="wiki (term)", value="Searches wikipedia for the person of your choice", inline=False)


    await ctx.send(embed=embed)
    print("Someone used games")



 #---------------------------------------Wiki-------------------------------------------------------
@bot.command()
async def wiki(ctx, *, q: str):
    """Returns a 1 sentence summary and link to wiki article"""
    try:
        page = wikipedia.page(q)
    except wikipedia.exceptions.DisambiguationError:
        await ctx.send("Could not find Page :(")
    else:
        summary = wikipedia.summary(q, sentences=6)
        msg = "{}\n{}".format(page.url, summary)
        await ctx.send(msg)	
#--------------------------------------------Rock-Paper-Scissors-----------------------------------
@bot.command()
async def rps(ctx, msg: str):
        print('Someone used rps')
        t = ["rock", "paper", "scissors"]
        computer = t[randint(0, 2)]
        player = msg.lower()
        if player == computer:
            await ctx.send("Tie!")
        elif player == "rock":
            if computer == "paper":
                await ctx.send("You lose! {0} covers {1}".format(computer, player))
            else:
                await ctx.send("You win! {0} smashes {1}".format(player, computer))
        elif player == "paper":
            if computer == "scissors":
                await ctx.send("You lose! {0} cut {1}".format(computer, player))
            else:
                await ctx.send("You win! {0} covers {1}".format(player, computer))
        elif player == "scissors":
            if computer == "rock":
                await ctx.send("You lose! {0} smashes {1}".format(computer, player))
            else:
                await ctx.send("You win! {0} cut {1}".format(player, computer))
        else:
            await ctx.send("That's not a valid play. Check your spelling!")


@bot.command()
async def roulette(ctx):
	user = ctx.message.author
	randomnum = random.randint(0, 2)
	if randomnum == 0:
		await ctx.send("You survived")
	elif randomnum == 1:
		await ctx.send("You survived")
	else:
		try:
			await user.kick()
			await ctx.send("Better luck next time")
			print("Someone used roulette and was kicked")
		except:
			await ctx.send("You are somehow untouchable")


#---------------------------------------------MemberRole-----------------------------------
@bot.command()
async def member(ctx):
	role = discord.utils.get(ctx.guild.roles, name="Member")
	user = ctx.message.author
	await user.add_roles(role)
	await ctx.message.delete()
	await ctx.send("You have been given Member")
	time.sleep(3)
	await ctx.channel.purge(limit=1)
	print("User has recieved Member")				

#-------------------------------------------Web-Exploiter-Role------------------------------------
@bot.command()
async def Web(ctx):
	role2 = discord.utils.get(ctx.guild.roles, name="Web-Exploiter")
	user = ctx.message.author
	await user.add_roles(role2)
	await ctx.message.delete()
	await ctx.send("You have been given Web-Exploiter")	
	time.sleep(3)
	await ctx.channel.purge(limit=1)
	print("User has recieved Web")			
#------------------------------------------Hardware-Hacker-Role-------------------------------
@bot.command()
async def Hardware(ctx):
	role3 = discord.utils.get(ctx.guild.roles, name="Hardware-Hacker")
	user = ctx.message.author
	await user.add_roles(role3)
	await ctx.message.delete()
	await ctx.send("You have been given Hardware-Hacker")
	time.sleep(3)
	await ctx.channel.purge(limit=1)
	print("User has recieved Hardware")				
#------------------------------------------Software-Hacker-Role-------------------------------
@bot.command()
async def Software(ctx):
	role4 = discord.utils.get(ctx.guild.roles, name="Software-Hacker")
	user = ctx.message.author
	await user.add_roles(role4)
	await ctx.message.delete()
	await ctx.send("You have been given Software-Hacker")
	time.sleep(3)
	await ctx.channel.purge(limit=1)		
	print("User has recieved Software")		
#-------------------------------------------Reverse-Engineer-Role-------------------------------

@bot.command()
async def Reverse(ctx):
	role5 = discord.utils.get(ctx.guild.roles, name="Reverse-Engineer")
	user = ctx.message.author
	await user.add_roles(role5)
	await ctx.message.delete()
	await ctx.send("You have been given Reverse-Engineer")
	time.sleep(3)
	await ctx.channel.purge(limit=1)
	print("User has recieved Reverse")	



#--------------------------------------------Art-----------------------------------------------
@bot.command()
async def art(ctx):
    embed = discord.Embed(title="__**Art**__", description="If you love art then you have come to the right place, here are a list of all the different ascii art commands.", color=0xde2338)
    embed.add_field(name='art_plane', value="ASCII plane", inline=False)
    embed.add_field(name='art_cake', value="ASCII cake", inline=False)
    embed.add_field(name='art_mlg', value="ASCII mlg glasses", inline=False)
    embed.add_field(name='art_smash', value="ASCII smash ball", inline=False)
    embed.add_field(name='art_trump', value="ASCII trump", inline=False)
    embed.add_field(name='art_fingerpuppets', value="ASCII fingerpuppets", inline=False)
    embed.add_field(name='art_oraemon', value="ASCII oraemon", inline=False)
    embed.add_field(name='art_anime', value="ASCII anime", inline=False)
    embed.add_field(name='art_herewego', value="ASCII awww shit here we go again", inline=False)
    embed.add_field(name='art_breathtaking', value="ASCII breathtaking by Keanu", inline=False)
    embed.add_field(name='art_owo', value="ASCII OWO", inline=False)
    embed.add_field(name='art_pizza', value="ASCII pizza", inline=False)
    embed.add_field(name='art_oi', value="ASCII OI", inline=False)
    embed.add_field(name='art_onepunchman', value="ASCII one punch man", inline=False)
    embed.add_field(name='art_shrek', value="ASCII shrek", inline=False)
    embed.add_field(name='art_FBI', value="ASCII FBI badge", inline=False)
    embed.add_field(name='art_ricardo', value="ASCII art_ricardo", inline=False)
    embed.add_field(name='art_pablo', value="ASCII pablo from the backyardigans", inline=False)
    embed.add_field(name='art_plane', value="ASCII plane", inline=False)
    embed.add_field(name='art_pika', value="ASCII Suprised pikachu", inline=False)
    embed.add_field(name='art_thick', value="ASCII fat yoshi", inline=False)
    embed.add_field(name='art_liquid', value="ASCII Team Liquid Logo", inline=False)
    embed.add_field(name='art_medal', value="ASCII Medal", inline=False)
    embed.add_field(name='art_momo', value="ASCII momo", inline=False)
    embed.add_field(name='art_alien', value="ASCII Alien", inline=False)
    embed.add_field(name='art_shock', value="ASCII Shocked face", inline=False)
    embed.add_field(name='art_reverse', value="ASCII Uno Reverse", inline=False)
    embed.add_field(name='art_thomas', value="ASCII Thomas the tank engine", inline=False)
    embed.add_field(name='art_gnomed', value='ASCII Ho ho ho ha ha, ho ho ho he ha. Hello there, old chum. I’m gnot an elf. I’m gnot a goblin. I’m a gnome. And you’ve been, GNOMED’')
    embed.add_field(name='art_uwu', value="ASCII UwU", inline=False)
    embed.add_field(name='art_fedora', value="ASCII Tips Fedora mlady'", inline=False)
    embed.add_field(name='art_dance', value="ASCII Default dance", inline=False)
    embed.add_field(name='art_thonking', value="ASCII To thonk or not to thonk.", inline=False)





   
    await ctx.send(embed=embed)

@bot.command()
async def art_plane(ctx):
	await ctx.send('''	

	⠀⠀⠀⣖⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⡇⠀⠀⠀⠀⠀⠀⠀ 
	⠀⠀⠀⠸⡆⠹⡀⣠⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⡧⢤⡄⠀⠀⠀⠀⠀ 
	⠀⠀⠀⡧⢄⣹⣅⣜⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⢹⠚⠃⠀⠀⠀⠀⠀ 
	⠀⣀⠴⢒⣉⡹⣶⣤⣀⡉⠉⠒⠒⠒⠤⠤⣀⣀⣀⠇⠀⠀⢸⠠⣄⠀⠀
	⠀⠈⠉⠁⠀⠀⠀⠉⠒⠯⣟⣲⠦⣤⣀⡀⠀⠀⠈⠉⠉⠉⠛⠒⠻⢥⣀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠈⠙⣲⡬⠭⠿⢷⣦⣤⢄⣀⠀⠀⠚⠛⠛⠓⢦⡀ 
	⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠚⠉⠁⠀⠀⠀⠀⣀⣉⡽⣕⣯⡉⠉⠉⠑⢒⣒⡾ 
⠀⠀⣀⡠⠴⠒⠉⠉⠀⢀⣀⣀⠤⡤⢶⣶⣋⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀ 
⣖⣉⣁⣠⠤⠶⡶⡶⢍⡉⠀⠀⠀⠙⠒⠯⠜⠀⠀⠀⠀
⠀⠁⠀⠀⠀⠀⠑⢦⣯⠇
	''')
@bot.command()
async def art_cake(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀ 
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀ 
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀ 
⢸⣿⣿⣿⠟⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀ 
⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇ 
⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇ 
⢸⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣶⣶⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿ 
⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠻⠿⢿⣿⣿⣷⣶⣶⣶⣤⣤⣿⣿⣿⣿ 
⢸⣿⣿⣿⣦⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿ 
⢸⣿⣿⣿⠛⠻⠿⠿⣿⣿⣿⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿ 
⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠿⠿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣿⣿⣿⣿ 
⢸⣿⣿⣿⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠿⣿⣿⣿⣿ 
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿ 
⠀⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣤⣤⣿⣿⣿⣿ 
⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
⠀⠀⠀⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠻⠿⠿⢿⣿⣿⣿⣿⠇		
		''')

@bot.command()
async def art_mlg(ctx):
	await ctx.send('''
	▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
	█░░░░░░░░▀█▄▀▄▀██████░▀█▄▀▄▀██████ 
	░░░░ ░░░░░░░▀█▄█▄███▀░░░ ▀█▄█▄███

		''')

@bot.command()
async def art_smash(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣦⣾⢟⢁⡄⠀⠀⠀⠀⠀⠀⠀⢀⡤⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢟⣿⣿⣾⠟⠁⠀⣠⣾⠀⠀⠀⢠⣿⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠀⠀⣼⣧⠀⢺⣿⣿⡃⠀⣴⣿⡟⠁⣼⠅⣠⣿⡗⡠⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣧⣠⣾⣿⣿⣆⣼⣿⣿⣡⢀⣿⣿⣿⣾⣿⣾⣿⣷⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⡿⠟⢛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣠⣾⣿⣿⣿⡏⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣋⣀⣤⣏⠀⠀⠀⠀⠀⠀⠀
⠀⣤⣿⣿⠋⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣿⠃⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢻⣿⡟⠀⠀⠀⠀⣠⠆⠀⠀⠀⠀⠀
⢀⣼⡏⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⡉⢀⣀⣤⣾⠇⠀⠀⠀⠀⣀⠄
⢻⣿⣧⣤⣤⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⡿⠋⠁⠀⠀⠀⣠⣾⡁⠀
⠈⢻⣿⡍⠉⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⣽⣿⣿⣿⣯⣴⣿⣥⣶⡾⢟⠉⠀⠀
⠀⢨⣿⣿⣦⣿⣿⣿⡇⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⡿⠿⠿⠿⠾⠛⠁⠀⠀⠀
⠀⠀⠻⠿⢿⣿⣿⣿⣇⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⠶⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠛⠛⠻⠟⠛⠿⠿⠿⢿⣷⣤⡾⠯⠁⠀
''')
@bot.command()
async def art_trump(ctx):
	await ctx.send('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠟⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠋⠛⠿⣿⣿
⠋⠉⠁⠄⠄⠄⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⣿⡀⠄⠄⠄⠄⢹
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠉⠛⠿⢦⣀⡀⡀⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠄⠄⠈⠹⣿⣀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⠄⠄⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠄⠄⠘
			''')
@bot.command()
async def art_fingerpuppets(ctx):
	await ctx.send('''
⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠁⣀⣤⣤⣄⢿⣿⣿⣿⣿⣿⣿⣿⠋⠁⣀⣀⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠁⢀⣟⣓⡲⣿⡡⣿⣿⣿⣿⣿⣿⠃⢠⣽⠿⢿⣿⣦⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣄⣘⣿⡟⡽⠾⠜⢹⣿⣿⣿⣿⠫⡆⣿⣿⣭⣰⡟⢉⢺⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡵⣿⣿⣿⣶⣬⡶⣸⣿⣿⣿⣿⢺⣻⣿⡟⡵⢿⡅⡇⣿⣿⠟⠻⠿⢿⣿⣿
⣿⣿⣷⣸⣿⣿⣿⣿⢧⣿⣿⣿⡿⣡⣿⣧⢻⣿⣮⣅⢗⣽⠋⢀⣄⡀⠄⠄⠹⣿
⣿⣿⣿⢱⣿⣿⣿⣿⣼⣿⣿⢋⣼⣿⣿⣿⠗⣬⣯⣵⣿⡧⢱⣿⢛⢿⣷⣦⣀⣿
⣿⣿⣿⢸⣿⣿⣿⡇⣿⡿⢡⣿⣿⣿⡿⣣⣾⣿⡿⢟⣻⣅⣿⡷⣾⣟⣑⡮⣼⣿
⣿⣿⣿⢸⣿⣿⣿⣧⢿⢧⣾⣿⣿⣿⣱⡿⢟⣭⣾⣿⣿⣿⢿⠒⡭⡞⠟⣼⣿⣿
⣿⣿⣿⡎⣿⣿⣿⣿⣶⣼⣿⣿⣿⣗⣩⣾⣿⣿⡿⢟⣛⣭⣭⣽⣯⣵⣿⣿⣿⣿
⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣩⣾⣿⣿⣿⣿⠿⠛⠛⠛⢿⣿⣿
⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿⣿⡏⣤⣶⣤⣄⡀⣼⣿
⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢾⣿⣿⣿⣿⣿⣿⢽⣏⣩⡟⠛⠇⣿⣿
⣿⣿⣿⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣯⣭⣽⣾⡯⢛⣨⡿⣰⣿⣿
⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣛⣛⣛⣱⣊⣴⣿⣿⣿

			''')
@bot.command()
async def art_oraemon(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀ 
⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄ 
⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇ 
⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷ 
⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃ 
⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀ 
⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀ 
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁
			''')
@bot.command()
async def art_herewego(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Ah shit, here we go again.
			''')
@bot.command()
async def art_pepe(ctx):
	await ctx.send('''
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⡿⠟⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠹⠟⣡⣶⡿⢟⣛⣛⡻⢿⣦⣩⣤⣤⣤⣬⡉⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⣛⡻⠿⢿⠈⣿⣿⣿⣿⣿⣿⣿
⣿⡟⢡⣴⣯⣿⣿⣿⣉⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⠛⠛⢓⠦⠈⢻⣿⣿⣿⣿⣿
⠏⣠⣿⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣿⣶⣮⣄⠙⣿⣿⣿⣿
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠿⠿⠇⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⡛⢋⣥⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢿⠱⣿⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿
⠑⠽⡻⢿⣿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⣛⣿⡇⢸⣿⣿⣿⣿⣿⣿
⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣿⣷⣾⣭⣿⣛⠷⠶⠶⠂⣴⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣉⣡⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
			''')
@bot.command()
async def art_anime(ctx):
	await ctx.send('''
⠄⠄⠄⢀⣤⣾⣿⡟⠋⠄⠄⠄⣀⡿⠄⠊⠄⠄⠄⠄⠄⠄⢸⠇⠄⢀⠃⠙⣿⣿
⣤⠒⠛⠛⠛⠛⠛⠛⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⠄⢀⠊⠄⠄⠈⢿
⣿⣠⠤⠴⠶⠒⠶⠶⠤⠤⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠃⠄⠂⣀⣀⣀⡀⠄
⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠂⠄⠄⠄⠄⠄⠄⢀⢎⠐⠛⠋⠉⠉⠉⠉⠛
⡇⠄⠄⠄⣀⡀⠄⠄⠄⢀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠎⠁⠄⠄⠄⠄⠄⠄⠄⠄
⡧⠶⣿⣿⣿⣿⣿⣿⠲⠦⣭⡃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀⠄⠄⠄⠄⠄⠄
⡇⠄⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣾⣿⣿⣿⡟⠛⠶⠄
⡇⠄⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿⡇⠄⠄⢀
⡇⠄⢿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⡇⠄⠄⢊
⢠⠄⠈⠛⠛⠛⠛⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⡦⠁⠄⠄⣼
⢸⠄⠈⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠄⠄⠄⠄⢰⣿
⢸⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠉⠄⢸⣿
⠄⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
⠄⢿⣷⣶⣄⡀⠄⠄⠄⠄⠄⠄⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⣿
⠄⢸⣿⣿⣿⣿⣷⣦⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣶⣿⣿⣿⣿⣿

			''')
@bot.command()
async def art_owo(ctx):
	await ctx.send('''
⠀⠀⠀⣠⣾⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣷⣄⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⢰⣿⡆⠀⣾⣿⡆⠀⣾⣷⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⠘⣿⣿⣤⣿⣿⣿⣤⣿⡇⠀⢻⣿⡇⠀⠀⢸⣿⣿⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢸⡿⠀⢹⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣇⠀⠀⢸⣿⣿⠀
⠀⠀⠀⠙⢿⣷⣶⣶⡿⠁⠀⠈⣿⣿⠟⠀⣿⣿⠇⠀⠀⠈⠻⣿⣿⣿⣿⡿⠋
			''')
@bot.command()
async def art_breathtaking(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣧⢀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⠋⠀⠀⠀⠀⠀⠙⠀⠙⣿⣿⣿⣷⢳⢀⠀⠀⠀
⠀⠀⣠⣿⣿⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⢀
⠀⠀⣸⣿⣿⣿⠸⠀⠀⠀⠒⠒⠒⠐⠀⠀⢿⣿⣿⣿⣿⣿⠀⠀
⠀⣴⣿⣿⣿⡿⠀⠒⣋⣙⡒⢰⠀⠤⣖⠒⢾⣿⣿⣿⣿⣧⠀⠀
⢺⣿⣿⣿⣿⢀⠀⠀⠉⠉⠉⠸⠀⡇⠉⠉⠀⢿⣿⣿⣿⣄⠀⠀
⠀⠙⣿⣿⣧⢻⠀⠀⠀⠀⠀⠠⠀⠰⠀⠀⠀⣸⠸⣿⣿⠿⠰⠀
⠀⠀⠀⠹⣿⣿⣿⣷⠀⡠⠙⣲⣔⣅⢡⣰⣷⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⠀⡿⠭⠭⠭⠭⢿⠀⣿⢻⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠙⠛⣿⢻⠹⣿⠐⠙⠛⠟⠉⢀⣴⡟⢿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡟⠀⠀⠻⣦⣤⣶⠾⠋⠀⠀⠁⡦⢄⢀⠀⠀⠀
⠀⠀⠀⠀⡠⠁⡇⠑⢄⠀⠀⠀⠀⠀⠀⠔⠀⠀⠁⠀⠀⠀⠉⠁
⠀⠔⠊⠁⠀⠀⣇⠀⠀⠀⠑⡤⠤⢎⠁⠀⠀⡘⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢢⠠⠀⡠⢆⠀⠀⡠⠙⢄⠀⡸⠀⠀⠀⠀⠀⠀ You're breathtaking
			''')
@bot.command()
async def art_pizza(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀
⠀⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀
⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠓⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
			''')
@bot.command()
async def art_oi(ctx):
	await ctx.send('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠙⠻⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣠⣴⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿
⣿⣿⣿⡿⠛⠉⠂⠂⠂⠂⠂⠂⠂⠂⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⡏⠂⠂⠂⠈⣿
⣿⣿⠋⠂⠂⠂⠂⠂⣀⣤⣤⣀⡀⠂⠂⠂⠂⠙⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⣿⠃⠂⠂⠂⠂⣰⣿⣿⣿⣿⣿⣿⣦⠂⠂⠂⠂⠘⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⡏⠂⠂⠂⠂⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⢹⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⡇⠂⠂⠂⠂⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⢸⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⡇⠂⠂⠂⠂⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⢸⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⣿⡀⠂⠂⠂⠂⢿⣿⣿⣿⣿⣿⣿⡿⠁⠂⠂⠂⢀⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⣿⣷⡀⠂⠂⠂⠂⠙⠻⠿⠿⠟⠋⠂⠂⠂⠂⢀⣾⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⣿⣿⣿⣦⣀⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢀⣴⣿⣿⣿⣿⣿⣿⣿⡇⠂⠂⠂⠂⣿
⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣾⣿
''')
@bot.command()
async def art_onepunchman(ctx):
	await ctx.send('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠉⠉⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⣿⣿⣿⣿⠀⠀⠀⠀⠀⢠⡴⠶⠶⠶⠶⠄⠀⠀⠀⠀⠀⠴⠶⠶⠤⠀⢠⡿
⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⣿⣿⢋⣽⣿⠷⠀⠀⠀⡞⠁⠀⢀⠈⠉⠦⠀⠀⢠⣠⡞⠉⡉⠉⠳⠄⣼⣿
⣿⣿⢸⣿⣿⡇⠀⠀⠀⠳⣄⡀⠀⢀⡠⠃⠀⠀⣼⠉⢧⣀⣀⣠⠴⠀⣿⣿
⠇⢻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⣿⡆⠀⠈⠁⠀⠀⢀⣿⣿
⠀⢸⣿⣷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⢸⣿⣿
⠀⢸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢀⣿⣿⣿
⣶⣾⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⢠⣤⣤⣄⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠙⠛⠋⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿
''')
@bot.command()
async def art_shrek(ctx):
	await ctx.send('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠫⢻⣿⣿⣿⣿⢟⣩⡍⣙⠛⢛⣿⣿⣿⠛⠛⠛⠛⠻⣿⣿⣿⣿⣿⡿⢿⣿
⣿⠤⠄⠄⠙⢿⣿⣿⣿⡿⠿⠛⠛⢛⣧⣿⠇⠄⠂⠄⠄⠄⠘⣿⣿⣿⣿⠁⠄⢻
⣿⣿⣿⣿⣶⣄⣾⣿⢟⣼⠒⢲⡔⣺⣿⣧⠄⠄⣠⠤⢤⡀⠄⠟⠉⣠⣤⣤⣤⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣀⣬⣵⣿⣿⣿⣶⡤⠙⠄⠘⠃⠄⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⢿⣿⣿⠿⠋⠁⠄⠂⠉⠒⢘⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣡⣷⣶⣤⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣷⣦⣰⠄⠄⠄⠄⢾⠿⢿⣿⣿⣿⣿
⣿⡿⠋⣡⣾⣿⣿⣿⡟⠉⠉⠈⠉⠉⠉⠉⠉⠄⠄⠄⠑⠄⠄⠐⡇⠄⠈⠙⠛⠋
⠋⠄⣾⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⡇⠄⠄⠄⠄⠄
⠄⢸⣿⣿⣿⣿⣿⣯⠄⢠⡀⠄⠄⠄⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄
⠁⢸⣿⣿⣿⣿⣿⣯⣧⣬⣿⣤⣐⣂⣄⣀⣠⡴⠖⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠈⠈⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣽⣉⡉⠉⠈⠁⠄⠁⠄⠄⠄⠄⡂⠄⠄⠄⠄⠄
⠄⠄⠙⣿⣿⠿⣿⣿⣿⣿⣷⡤⠈⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠠⠔⠄⠄⠄⠄⠄
⠄⠄⠄⡈⢿⣷⣿⣿⢿⣿⣿⣷⡦⢤⡀⠄⠄⠄⠄⠄⠄⢐⣠⡿⠁⠄⠄⠄⠄⠄
''')
@bot.command()
async def art_FBI(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
⠀⠀⢠⣿⡿⠿⠿⠿⠿⠿⠿⠿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⠿⠿⢿⣿⡄⠀⠀
⠀⢀⣿⣿⡇⠀⠀⣠⣤⣄⣀⣠⣿⠀⠀⢀⣤⣀⡀⠀⠘⣿⣿⠀⠀⢸⣿⣿⡀⠀
⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⠟⠀⠀⣿⣿⠀⠀⢸⣿⣿⡇⠀
⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀ ⢸⣿⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⠀⠀⢸⣿⣿⡧⠀
⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⠀⠀⢹⣿⠀⠀⢸⣿⣿⡇⠀
⠀⠈⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠛⠉⠀⢀⣾⣿⠀⠀⢸⣿⣿⠃⠀
⠀⠀⠸⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣶⣶⣾⣿⠇⠀⠀
⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀
''')
@classmethod
async def art_ricardo(ctx):
	await ctx.send('''
⠄⠄⠄⠄⠄⠄⢴⡶⣶⣶⣶⡒⣶⣶⣖⠢⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⢠⣿⣋⣿⣿⣉⣿⣿⣯⣧⡰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣿⣿⣹⣿⣿⣏⣿⣿⡗⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠟⡛⣉⣭⣭⣭⠌⠛⡻⢿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣤⡌⣿⣷⣯⣭⣿⡆⣈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣷⢛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢻⣷⣽⣿⣿⣿⢿⠃⣼⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣛⣻⣿⠟⣀⡜⣻⢿⣿⣿⣶⣤⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢠⣤⣀⣨⣥⣾⢟⣧⣿⠸⣿⣿⣿⣿⣿⣤⡀⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢟⣫⣯⡻⣋⣵⣟⡼⣛⠴⣫⣭⣽⣿⣷⣭⡻⣦⡀⠄
⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⢏⣽⣿⢋⣾⡟⢺⣿⣿⣿⣿⣿⣿⣷⢹⣷⠄
⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢣⣿⣿⣿⢸⣿⡇⣾⣿⠏⠉⣿⣿⣿⡇⣿⣿⡆
⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢸⣿⣿⣿⠸⣿⡇⣿⣿⡆⣼⣿⣿⣿⡇⣿⣿⡇
⠇⢀⠄⠄⠄⠄⠄⠘⣿⣿⡘⣿⣿⣷⢀⣿⣷⣿⣿⡿⠿⢿⣿⣿⡇⣩⣿⡇
⣿⣿⠃⠄⠄⠄⠄⠄⠄⢻⣷⠙⠛⠋⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡇⣿⣿⡇
''')
@bot.command()
async def art_pablo(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠄⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⠖⢋⡤⠊⠁⠀⠀⣀⣠⣤⣤⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⠁⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⣫⣶⣿What's⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿a⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⢀⣿fella⣿⣿⣿⣿⣿⡿⠛⠉⠛⢿⣿⣿⣿⣿⣿⡟⠁⠈⠻⣿⣷⡀⠀⠀
⠀⠀⣾⣿gotta⣿⣿⣿⣿⣿⠀⠀⣀⡀⠈⣿⣿⣿⣿⣿⢠⣤⡀⠀⣿⣿⣧⠀⠀
⠀⢸⣿⣿do⣿⣿⣿⣿⣿⣿⣄⢸⣿⣿⢀⣿⣿⣿⣿⣿⣿⡿⠃⢠⣿⣿⣿⠀⠀
⠀⣼⣿⣿around⣿⣿⣿⣿⣷⣾⣷⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⢸⣿⣿here⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠋⠀⠀⣀⡈⠉⢻⣿⣿⣿⣿⠁⠀
⠀⢸⣿⣿to⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⠾⠛⣿⡶⣿⣿⣿⣿⣿⠀⠀
⠀⠀⢿⣿get⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠳⣄⣀⡿⣸⣿⣿⣿⣿⡏⠀⢀
⠀⠀⠈⢿⣿some⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣭⣴⣿⣿⣿⣿⡟⢀⣴⣿
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿apple juice?⣿⣿⣿⣿⣿⣿⣫⣶⣿⣿⣿
⣿⣶⣤⣄⡀⠈⠛⢿⣿⣿⣿⣿⣿
''')
@bot.command()
async def art_pika(ctx):
	await ctx.send('''
⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
''')
@bot.command()
async def art_thick(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⢿⣧⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣧⣆⣘⡄⢹⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⡀⣾⡿⠀⠉⠉⠛⠋⠛⠛⠚⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣍⠹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣷⣾⣿⣿⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣟⢻⣿⣄⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⠿⠟⠁⠑⢶⣤⣴⣿⣿⣿⣷⣶⣬⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢛⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
@bot.command()
async def art_liquid(ctx):
    await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠀⠀⢰⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣠⣤⡀⠀⠹⣿⣿⡆⠀⢸⣿⡿⢻⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣷⡄⠀⠹⣿⣷⠀⠸⠋⠀⣰⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
⠀⠀⠀⣤⡀⠀⠈⠻⢿⣿⣦⡀⠛⠁⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⣿⣿⣷⣦⣄⡀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⢻⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠉⠙⠛⠻⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠈⢿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⢠⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠸⠿⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣀⠀⠀⠀⠀⠈⢿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣤⡆⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣷⡀⢄⡈⠒⣨⣿⡇⠀⠀⠀
⠀⠀⠀⠀⢿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣤⣿⣿⣿⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠛⠁⠀⠀⠀⠀⠀
            ''')
@bot.command()
async def art_medal(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⣤⣶⣶⡶⠦⠴⠶⠶⠶⠶⡶⠶⠦⠶⠶⠶⠶⠶⠶⠶⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⠀⢀⣤⠄⠀⠀⣶⢤⣄⠀⠀⠀⣤⣤⣄⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⡷⠋⠁⠀⠀⠀⠙⠢⠙⠻⣿⡿⠿⠿⠫⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⠞⠉⠀⠀⠀⠀⣴⣶⣄⠀⠀⠀⢀⣕⠦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⠾⠋⠁⠀⠀⠀⠀⢀⣼⣿⠟⢿⣆⠀⢠⡟⠉⠉⠊⠳⢤⣀⠀⠀⠀
⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⢀⣀⣾⣿⠃⠀⡀⠹⣧⣘⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀
⠀⣿⡀⠀⠀⢠⣶⣶⣿⣿⣿⣿⡿⠁⠀⣼⠃⠀⢹⣿⣿⣿⣶⣶⣤⠀⠀⠀⢰⣷
⠀⢿⣇⠀⠀⠈⠻⡟⠛⠋⠉⠉⠀⠀⡼⠃⠀⢠⣿⠋⠉⠉⠛⠛⠋⠀⢀⢀⣿⡏
⠀⠘⣿⡄⠀⠀⠀⠈⠢⡀⠀⠀⠀⡼⠁⠀⢠⣿⠇⠀⠀⡀⠀⠀⠀⠀⡜⣼⡿⠀
⠀⠀⢻⣷⠀⠀⠀⠀⠀⢸⡄⠀⢰⠃⠀⠀⣾⡟⠀⠀⠸⡇⠀⠀⠀⢰⢧⣿⠃⠀
⠀⠀⠘⣿⣇⠀⠀⠀⠀⣿⠇⠀⠇⠀⠀⣼⠟⠀⠀⠀⠀⣇⠀⠀⢀⡟⣾⡟⠀⠀
⠀⠀⠀⢹⣿⡄⠀⠀⠀⣿⠀⣀⣠⠴⠚⠛⠶⣤⣀⠀⠀⢻⠀⢀⡾⣹⣿⠃⠀⠀
⠀⠀⠀⠀⢿⣷⠀⠀⠀⠙⠊⠁⠀⢠⡆⠀⠀⠀⠉⠛⠓⠋⠀⠸⢣⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣷⣦⣤⣤⣄⣀⣀⣿⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣾⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀
		''')
@bot.command()
async def art_momo(ctx):
	await ctx.send('''
⣿⣿⣿⣿⠏⠄⣰⣿⡋⡴⣁⣿⣿⣿⣿⣯⡖⣄⠘⢿⣆⠄⠄⠄⠈⢻⣿⣿⣿⣿
⣿⣿⣿⠇⠂⣴⡿⡃⡜⡰⣾⣿⣿⣿⣿⣿⣟⠸⢠⠸⣿⡆⠄⠄⠄⠄⠹⣿⣿⣿
⣿⣿⡟⢀⢠⡿⡝⡌⣼⣻⣿⣿⣿⣿⣿⣿⣿⡄⠄⡆⣿⡇⠄⠄⠄⠄⠄⢿⣿⣿
⣿⣿⡇⡏⣸⣷⣳⣹⡿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⣷⣿⡇⠄⠄⠄⠄⠄⠸⣿⣿
⣿⣿⣿⣧⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠻⢿⣿⣿⣦⡸⣿⣷⠄⠄⠄⠄⠄⠄⢻⣿
⣿⣿⣿⡡⠦⣄⡹⣿⣿⣿⣿⠃⢠⣶⣶⣦⡌⢿⣿⣿⣾⣿⡆⠄⠄⠄⠄⠄⢸⣿
⣿⣿⣿⣇⠄⣿⡇⣿⣿⣿⣿⡀⠊⠄⢸⣿⡿⢸⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⣿
⣿⣿⣿⣿⣝⣋⣠⣿⣿⣿⣿⣧⡈⠒⠚⢛⣡⣾⣿⣿⣿⣿⠇⠄⠄⠄⠄⠄⠠⢻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣭⣽⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⢘⢻
⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠄⠄⠄⠄⠄⠄⠈⣿
⣿⣿⣿⡷⠄⢿⣿⣹⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⠟⣫⡶⡀⠄⠄⠄⠄⠄⠄⠄⣿
⣿⣿⣿⡟⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣡⣾⣿⡕⠁⠄⠄⠄⠄⠄⠄⠄⣿
⣿⣿⣿⡟⡅⠄⠘⣿⣿⣿⣿⡿⠟⠋⣡⣴⣿⣿⣿⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿
⣿⣿⣿⣷⡇⠄⠄⠘⢯⣍⣡⣤⣶⣿⣿⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿
⣿⣿⣿⣿⡇⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣟⣡⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿
		''')
@bot.command()
async def art_alien(ctx):
	await ctx.send('''
⣿⣿⣿⣿⡿⠋⠄⢀⣀⣠⣤⣤⣤⣤⣤⣀⣀⡀⠄⠈⠙⢿⣿⣿⣿⣿
⣿⣿⣿⠋⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠄⠙⣿⣿⣿
⣿⡿⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⢿⣿
⣿⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⣿
⡟⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸
⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠄
⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠄
⣇⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⡇⢠
⣿⡀⠈⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⣀⠄⠄⣾
⣿⣧⢠⣖⣀⡀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣤⡶⢿⣿⡄⣼⣿
⣿⣿⣏⢿⣦⣬⣙⣒⡤⣌⣙⣿⣿⣿⣿⣿⣷⣚⣭⣴⣶⣿⡟⣼⣾⣿
⣿⣿⣿⣬⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣾⣿⣿⣿
⣿⣿⣿⣿⣧⡹⣯⣿⠿⠦⠬⣭⣭⣥⣼⠾⢿⣿⡿⠟⣠⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣮⡙⢷⣯⣭⣭⣭⣭⣽⣿⠟⠋⣠⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣦⣝⠛⠛⠟⠛⢛⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿		
		''')
@bot.command()
async def art_shock(ctx):
	await ctx.send('''
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢛⣉⣩⣤⣬⣉⣉⣉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠋⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣈⠻⢿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡙⠿⣿⣿⣿
⣿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢻⣷⡆⠹⣿⣿
⣿⡇⢠⣿⣿⣿⣿⣿⣿⡟⠋⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣴⣿⣿⡄⢹⣿
⡟⢀⣿⣿⣿⣿⣿⣿⣿⣧⣀⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻
⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⢛⣋⣉⣉⣉⠙⢿⣿⣿⣿⣿⣿⡇⢸
⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣡⣴⣶⣿⣿⣿⣿⣿⣿⣧⠄⢿⣿⣿⣿⣿⡇⢸
⣇⠈⣿⣿⣿⣿⣿⣿⣿⡟⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⣿⠃⣼
⣿⣆⠘⣿⣿⣿⣿⣿⣿⡇⣴⣤⣤⣬⣉⡛⠻⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠃⢸⣿
⣿⣿⣆⠘⢿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⠿⠷⠌⠛⢛⣋⣉⣁⣸⣿⡿⠋⣠⣿⣿
⣿⣿⣿⣶⡈⠙⢿⣿⣟⣈⣉⣩⣥⣤⣶⣶⣶⣾⣿⣿⣿⣿⣿⡿⠟⢁⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⣉⣤⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣈⡉⠉⠛⣋⣉⣉⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿		
		''')
@bot.command()
async def art_reverse(ctx):
	await ctx.send('''
⠐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠂
⠄⠄⣰⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄
⠄⠄⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿⠄⠄
⠄⠄⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹⠄⠄
⠄⠄⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄
⠄⠄⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
⠄⠄⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄
⠄⠄⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄
⠄⠄⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⠄⠄
⠄⠄⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⠄⠄
⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⠄⠄
⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿⠄⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿⠄⠄
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿⠄⠄
⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⠄⠄
⠄⠄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿⠄⠄
⠄⠄⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿⠄⠄
⠄⠄⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿⠄⠄
⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟⠄⠄
⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄		
		''')
@bot.command()
async def art_sans(ctx):
	await ctx.send('''

░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░
░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░
░░░░░░░░█░░░░░░░░░░▄▄▄░░█░░░░░░░░
░░░░░░░░█░░▄▄▄░░▄░░███░░█░░░░░░░░
░░░░░░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░░░░░░
░░░░░░░░█░░▀█▀█▀█▀█▀█▀░░█░░░░░░░░
░░░░░░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░░░░░░
░░░░░░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░░░░░░
░░░░░▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄░░░░░
░░░░░█░░░░▀▄░█▄░░░▄█░▄▀░░░░█░░░░░
░░░░░░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░░░░░░
░░░░░░░░▀██▄▄███████▄▄██▀░░░░░░░░
░░░░░░░░████████▀████████░░░░░░░░
░░░░░░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░░░░░░
░░░░░░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░﻿░░░░░		
		''')
@bot.command()
async def art_thomas(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣤⣼⣷⣿⣿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣾⢟⣭⣝⢿⣿⣿⣿⣿⠟⠩⢒⠂⠀⠀⠀⠤⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⣸⣯⣻⣿⣾⣿⣿⣿⠏⠀⠈⡉⠙⠄⠀⠐⠉⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠁⠀⠀⠀⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢀⣠⣤⡤⠒⠺⠛⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⠁⠀⠤⠤⠤⠂⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣧⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⣿⣿⣿⡇⣽⡿⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⢀⣸⣿⣿⣿⠉⠑⠛⠀⠄⠀⠙⠛⢿⣿⡿⠿⢿⠿⢿⣿⠛⠛⠛⢠⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⡄⠀⣀⣀⣀⣀⣀⣀⣈⣿⣆⣀⣸⣀⣘⣿⣀⣀⣀⣸⣀⣀⣀⡀⠀
⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠛⠛⠛⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⡟⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀		
		''')
@bot.command()
async def art_gnomed(ctx):
	await ctx.send('''
⣿⣿⣿⣿⣿⠟⠉⠁⠄⠄⠄⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣏⠄⡠⡤⡤⡤⡤⡤⡤⡠⡤⡤⣸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣗⢝⢮⢯⡺⣕⢡⡑⡕⡍⣘⢮⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡧⣝⢮⡪⡪⡪⡎⡎⡮⡲⣱⣻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⠁⢸⡳⡽⣝⢝⢌⢣⢃⡯⣗⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠟⠁⠄⠄⠄⠹⡽⣺⢽⢽⢵⣻⢮⢯⠟⠿⠿⢿⣿⣿⣿⣿⣿
⡟⢀⠄⠄⠄⠄⠄⠙⠽⠽⡽⣽⣺⢽⠝⠄⠄⢰⢸⢝⠽⣙⢝⢿
⡄⢸⢹⢸⢱⢘⠄⠄⠄⠄⠄⠈⠄⠄⠄⣀⠄⠄⣵⣧⣫⣶⣜⣾
⣧⣬⣺⠸⡒⠬⡨⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⣷⣽⣿⣿
⣿⣿⣿⣷⠡⠑⠂⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣄⠠⢀⢀⢀⡀⡀⠠⢀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢐⢀⠂⢄⠇⠠⠈⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⠄⠠⠈⢈⡄⠄⢁⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠠⠐⣼⠇⠄⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣯⠄⠄⡀⠈⠂⣀⠄⢀⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⣀⠐⢀⣸⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')
@bot.command()
async def art_uwu(ctx):
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡆⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⣾⣿⡆⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⢰⣿⡆⠀⣾⣿⡆⠀⣾⣷ ⣿⣿⡇⠀⠀⣿⣿⡇⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⠘⣿⣿⣤⣿⣿⣿⣤⣿⡇⢻⣿⡇⠀⠀⣿⣿⡇⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢸⡿⠀⢹⣿⣿⣿⣿⣿⣿⣿⠁⢸⣿⣇⠀⢀⣿⣿⠇⠀
⠀⠀⠀⠙⢿⣷⣶⣶⡿⠁⠀⠈⣿⣿⠟⠀⣿⣿⠇⠀⠈⠻⣿⣶⣾⡿⠋⠀⠀
		''')
@bot.command()
async def art_fedora(ctx):
	await ctx.send('''
░░░░░░░░▄▀█▀█▄██████████▄▄░░░░░░ 
░░░░░░░▐██████████████████▌░░░░░ 
░░░░░░░████le██fedora██████▌░░░░  
░░░░░░▐███████████████████▌░░░░░ 
░░░░░░████has████arrived███████▄ 
░░░▄█▐█▄█▀█████████████▀█▄█▐█▄░░ 
░▄██▌██████▄█▄█▄█▄█▄█▄█████▌██▌░ 
▐████▄▀▀▀▀████████████▀▀▀▀▄███░░ 
▐█████████▄▄▄▄▄▄▄▄▄▄▄▄██████▀░░░ 
░░░▀▀████████████████████░░░░░░░
		''')
@bot.command()
async def art_dance():
	await ctx.send('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛

		''')
@bot.command()
async def art_thonking(ctx):
	await ctx.send('''
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒
▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒
▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒
▒█▀░░░░███░░░░▄█▄░░░░▀█▒
▒█░░░░░░▀░░░░░▀█▀░░░░░█▒
▒█░░░░░░░░░░░░░░░░░░░░█▒
▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒
▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒
▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒
▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒
▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒
▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒
		''')

bot.run("NjEzNTUzMTU2NTUwNTU3Njk2.XW7Zog.kIgY7JGQsV25Wukld8M7wF-u1wk")
