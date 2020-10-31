import discord
from discord.ext import commands

TOKEN = 'NzcxMzU2NDM5MzczMjgzMzI4.X5q7qg.64HHwEdMej4ww7e0UQYe7PmxAxo'

bot = commands.Bot(command_prefix='/')

@bot.command()
async def team(ctx, a: discord.Member, b: discord.Member, c: discord.Member, name):
	whitelist = []

	whitelist = []

	if str(ctx.author) not in whitelist:
		vlad = ctx.message.author.id
		t = a.mention + " " + b.mention + " " + c.mention + " " + d.mention + " " + name
		await ctx.send(vlad.mention + ", подтвердите команду")
	else:

		vc = bot.get_channel(772148009814458378)
		tc = bot.get_channel(772148347553316874)

		vc1 = await vc.clone(name=name)
		tc1 = await tc.clone(name=name)

		await vc1.set_permissions(a, view_channel=True)
		await vc1.set_permissions(b, view_channel=True)
		await vc1.set_permissions(c, view_channel=True)
		await vc1.set_permissions(d, view_channel=True)


		await tc1.set_permissions(a, read_messages=True)
		await tc1.set_permissions(b, read_messages=True)
		await tc1.set_permissions(c, read_messages=True)

		await ctx.send('Текстовый и голосовой чат для команды с названием "' + name + '" созданы')

@bot.command()
async def test(ctx):
	vlad = bot.get_user(595182111112036352)

	if vlad != ctx.author:
		await ctx.send("Not for you")
		return

	cat = bot.get_channel(722106424318099566).guild

	tc = cat.text_channels
	vc = cat.voice_channels

	for t in tc:
		print(t.name)

	print("-----------------------")
	for v in vc:
		print(v.name)

	await ctx.send("Текстовых: " + str(len(tc)) + "\nГолосовых: " + str(len(vc)))

@bot.event
async def on_reaction_add(reaction, user):
	Channel = bot.get_channel(772139106406105139)
	if reaction.message.channel != Channel:
		return

	vlad = bot.get_user(595182111112036352)

	if vlad != user:
		return

	name = reaction.message.content.split('>')[-1].replace('"', "")

	vc = bot.get_channel(772148009814458378)
	tc = bot.get_channel(772148347553316874)

	vc1 = await vc.clone(name=name)
	tc1 = await tc.clone(name=name)

	for a in reaction.message.mentions:
		await vc1.set_permissions(a, view_channel=True)
		await tc1.set_permissions(a, read_messages=True)

	await tc1.send("Вам все еще необходимо зарегистрировать команду у Филиппа Руховича")

	await Channel.send('Необходимые голосовые и текстовые чаты команды "' + name + '" созданы, можете начинать игру!')
@team.error 
async def on_command_error(ctx, error):
	await ctx.send("Найди побольше участников и не забудь указать название команды")
	await ctx.send("Хорошо, остался один шаг! Инициатор должен оставить реакцию под командой /team", delete_after = 20)
bot.run(TOKEN)