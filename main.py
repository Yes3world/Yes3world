import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Привет'):
        await message.channel.send("Хай")
    elif message.content.startswith('Пока'):
        await message.channel.send("Покеда")
    elif message.content.startswith('Что будет если пчелки вымрут'):
        await message.channel.send("Если все медоносные пчёлы вымрут то опыление растений не будет овощи,фрукты и растительное продовольствие будет повышена цена все подробности в этой ссылке https://dzen.ru/a/YV26_u66sTPGuewp")
    elif message.content.startswith('Виды пчел'):
        await message.channel.send("Медоносная пчела (Apis mellifera), китайская восковая пчела (Apis cerana), гигантская пчела (Apis dorsata), фиолетовый шмель-плотник (Xylocopa violacea), люцерновая пчела-листорез (Megachile rotundata)")
    elif message.content.startswith('Пчелы видео'):
        await message.channel.send("https://youtu.be/sh4DzXEe1Nw?si=FSvDzZ-5s8rWffg_")
    elif message.content.startswith('Пчелы добрые'):
        await message.channel.send("Если не беспокоить то добрые")
    elif message.content.startswith('Факты о пчел'):
        await message.channel.send("https://youtu.be/WkQ7eYF3FJM")
    elif message.content.startswith('Упоротые пчелы'):
        await message.channel.send(file = discord.File('./Bee/B.jpg'))
        await message.channel.send(file = discord.File('./Bee/B2.jpg'))
        await message.channel.send(file = discord.File('./Bee/B3.jpg'))
    elif message.content.startswith('Коты и Собаки после укуса'):
        await message.channel.send(file = discord.File('./D&C/C1.jpg'))
        await message.channel.send(file = discord.File('./D&C/Cs2.jpg'))
        await message.channel.send(file = discord.File('./D&C/D1.jpg'))
        await message.channel.send(file = discord.File('./D&C/Ds2.jpg'))
    elif message.content.startswith('Пчелы где обитают'):
        await message.channel.send("Излюбленная естественная среда обитания пчел — лесопосадки и лесные массивы.Главное условие — удаленность от дорог, промышленных центров и поселений человека. Идеальное место для семьи — дупло.Гнездо может строиться и между ветвей деревьев в густой кроне, в расщелинах стен или гор. Для заселения пригодны и вырытые в почве норы.Иногда удобное место для жилья находится вблизи человека. Подходит щель под крышей сарая или дома, пространство между рамами и т.д.Самое главное условие для семейного обустройства — наличие рядом постоянного источника воды")
    elif message.content.startswith('Помощь'):
        await message.channel.send("рабочие команды, Пчелы где обитают, Упоротые пчелы, Коты и Собаки после укуса, Факты о пчел, Пчелы добрые, Пчелы видео, Виды пчел, Что будет если пчелки вымрут, Пока и Привет")
    else:
        await message.channel.send(message.content)


client.run("TOKEN")
