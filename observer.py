# -*- coding: utf8 -*-
import discord, asyncio, requests, json, os
import datetime as dt
from discord.ext import commands
from dbclassmembers import *
from config import *

intents = discord.Intents.all()
intents.members = True
observer = commands.Bot (command_prefix = 'Q', intents=intents)
guild = discord.Guild

@observer.event #Console ready display
async def on_ready():
    db.connect()
    Members.drop_table()
    print('Успешно: {0.user}'.format(observer))
    Members.create_table()
    params = {'limit': 100}
    r = requests.get('https://discord.com/api/v9/guilds/606561480170668101/members', params = params, headers = headers)
    rjson = json.loads(r.text)
    amount = len(rjson)
    for i in range(0, amount):
        memberid = rjson[i]['user']['id']
        username = rjson[i]['user']['username']
        discriminator = rjson[i]['user']['discriminator']
        add = Members(memberid = memberid, username = username, discriminator = discriminator)
        add.save()
    db.close()
    birthupd = observer.get_channel(768480484618534914)
    await birthupd.purge(limit=4)
    print('Channel purged')
    ec0 = discord.Embed(color = 0xffffff)
    ec0img = discord.File('bdayseng.png')
    ec0.set_image(url='attachment://bdayseng.png')
    await birthupd.send(embed = ec0, file = ec0img)
    ec0bd = discord.Embed(title = ':closed_book: Information about users on the server :closed_book:', description = '`Nickname | Name | Date of birth | Age | City`', color = 0xffffff)
    ec0bd.add_field(
        name = ':snowman: Winter :snowflake:', 
        value = '<@334301539860742145> | Misha | january 15 | 23 y.o. | Krasnodar\n<@595328091962867717>  | Alleksh  | january 29 | 17 y.o. | Lviv\n<@289430056261124097> | Igaryasha | january 31 | 20 y.o. | Ekaterinburg\n<@372007261876256768>  | Daniel | february 6 | 16 y.o. | Petropavl\n<@276780906654728202> | Max | february 20 | 18 y.o. | Kyiv\n<@564581176631885834> | Nikolay | february 22 | 15 y.o. | Simferopol\nᅠ',
        inline = False) 
    ec0bd.add_field(
        name = ':partly_sunny: Spring :wilted_rose:',
        value = '<@345085964500074497> | Julia | march 18 | 20 y.o. | Ekaterinburg\nᅠ',
        inline = False)
    ec0bd.add_field(
        name = ':sun_with_face: Summer :island:',
        value = '<@529232630420340736> | Artem | june 16 | 21 y.o. | Penza\n<@272388934166773763> | Dmitry | june 18 | 17 y.o. | Kyiv\n<@339776970609131521> | Alexey | july 5 | 16 y.o. | Penza\n<@423184105929310209> | Lina | july 26 | 19 y.o. | Nizhny Novgorod\n<@327402918481231873> | Nikita | august 6 | 18 y.o. | Ivatsevichi/Baranovichi\n<@893120179012247553> | Denis | august 16 | 19 y.o. | Nizhny Novgorod\n <@412298602925391873> | Kristina | August 25 | 17 y.o. | Oryol\nᅠ',
        inline = False)
    ec0bd.add_field(
        name = ':umbrella: Autumn :fallen_leaf:',
        value = '<@858102341555585055> | Semen | today | 38 y.o. | Ukraine\n<@381768919301750791> | Dmitry | september 4 | 21 y.o. | Mykolaiv\n<@619831709839523840> | Artem | september 5 | 19 y.o. | Kyiv\n<@402044993054703618> | Ilya | september 10 | 18 y.o. | Donetsk\n<@677258830111047690> | Ksyusha | september 12 | 16 y.o. | Chelyabinsk\n<@650028253750493185> | Anastasia | september 22 | 16 y.o. | Odesa\n<@460031382723362827> | Artem | september 23 | 18 y.o. | Kyiv\n<@409750693851824130> | Egor | october 5 | 14 y.o. | Simferopol\n<@414051284094812160> | Alexander | october 12 | 18 y.o. | Kyiv\n<@385542550729130006> | Vitaly | november 12 | 23 y.o. | Kyiv\n <@444946884805787648> | Artem | november 15 | 16 y.o. | Klaipeda\n<@570311375633514496> | Danya | november 19 | 17 y.o. | Cheboksary\n<@733063317764964352> | Daria | november 20 | 18 y.o. | Krasnodar\n<@421930169713033228> | Vladimir | november 26 | 19 y.o. | Cherkasy\n<@390836335000420352> | Artem | november 30 | 20 y.o. | Ekaterinburg\nᅠ',
        inline = False)
    await birthupd.send(embed = ec0bd)
    ec1 = discord.Embed(color = 0xffffff)
    ec1img = discord.File('bdaysrus.png')
    ec1.set_image(url='attachment://bdaysrus.png')
    await birthupd.send(embed = ec1, file = ec1img)
    ec1bd = discord.Embed(title = ':closed_book: Информация о пользователях на сервере :closed_book:', description = '`Никнейм | Имя | День рождения | Возраст | Город`', color = 0xffffff)
    ec1bd.add_field(
        name = ':snowman: Зима :snowflake:', 
        value = '<@334301539860742145> | Миша | 15 января | 23 года | Краснодар\n<@595328091962867717>  | Аллекш  | 29 января | 17 лет | Львов\n<@289430056261124097> | Игаряша | 31 января | 20 лет | Екатеринбург\n<@372007261876256768> | Даниил | 6 февраля | 16 лет | Петропавловск\n<@276780906654728202> | Макс | 20 февраля | 18 лет | Киев\n<@564581176631885834> | Николай | 22 февраля | 15 лет | Симферополь\nᅠ',
        inline = False) 
    ec1bd.add_field(
        name = ':partly_sunny: Весна :wilted_rose:',
        value = '<@345085964500074497> | Юлия | 18 марта | 20 лет | Екатеринбург\n',
        inline = False)
    ec1bd.add_field(
        name = ':sun_with_face: Лето :island:',
        value = '<@529232630420340736> | Артём | 16 июня | 21 год | Пенза\n<@272388934166773763> | Дмитрий | 18 июня | 17 лет | Киев\n<@339776970609131521> | Лёша | 5 июля | 16 лет | Пенза\n<@423184105929310209> | Лина | 26 июля | 19 лет | Нижний Новгород\n<@327402918481231873> | Никита | 6 августа | 18 лет | Ивацевичи/Барановичи\n<@893120179012247553> | Денис | 16 августа | 19 лет | Нижний Новгород\n <@412298602925391873> | Кристина | 25 августа | 17 лет | Орёл\nᅠ',
        inline = False)
    ec1bd.add_field(
        name = ':umbrella: Осень :fallen_leaf:',
        value = '<@858102341555585055> | Семён | сегодня | 38 лет | Украина\n<@381768919301750791> | Дмитрий | 4 сентября | 21 год | Николаев\n<@619831709839523840> | Артём | 5 сентября | 19 лет | Киев\n<@402044993054703618> | Илья | 10 сентября | 18 лет | Донецк\n<@677258830111047690> | Ксюша | 12 сентября | 16 лет | Челябинск\n<@650028253750493185> | Анастасия | 22 сентября | 16 лет | Одесса\n<@460031382723362827> | Артём | 23 сентября | 18 лет | Киев\n<@409750693851824130> | Егор | 5 октября | 14 лет | Симферополь\n<@414051284094812160> | Александр | 12 октября | 18 лет | Киев\n<@385542550729130006> | Виталик | 12 ноября | 23 года | Киев\n <@444946884805787648> | Артём | 15 ноября | 16 лет | Клайпеда\n<@570311375633514496> | Даня | 19 ноября | 17 лет | Чебоксары\n<@733063317764964352> | Дашуля | 20 ноября | 18 лет | Краснодар\n<@421930169713033228> | Владимир | 26 ноября | 19 лет | Черкассы\n<@390836335000420352> | Артём | 30 ноября | 20 лет | Екатеринбургᅠ',
        inline = False)
    await birthupd.send(embed = ec1bd)

@observer.event
async def on_member_join(member):
    joinleave = observer.get_channel(917054710740037643)
    e = discord.Embed(title = 'Пользователь вошёл на сервер', description = f'{member.mention}', color = 0x00ff00, timestamp=dt.datetime.utcnow())
    e.set_author(name = f'ID - {member.id}', icon_url = member.avatar_url)
    await joinleave.send(embed=e)

@observer.event
async def on_member_remove(member):
    joinleave = observer.get_channel(917054710740037643)
    e = discord.Embed(title = 'Пользователь покинул сервер', description = f'{member.mention}', color = 0xff0000, timestamp=dt.datetime.utcnow())
    e.set_author(name = f'ID - {member.id}', icon_url = member.avatar_url)
    await joinleave.send(embed=e)

@observer.command()
async def ukr(ctx):
    await ctx.channel.purge(limit=1)
    print(ctx.channel.id)
    print(ctx.channel)
    channel = ctx.channel(id='768516870998720524')
    await channel.send('<a:UkrFan:880863748703784980>')

@observer.command(pass_context = True)
async def mainpicture(ctx):
    await ctx.channel.purge(limit=1)

@observer.command(pass_context = True)
async def birth(ctx):
    await ctx.channel.purge(limit=5)
    ec0 = discord.Embed(color = 0xffffff)
    ec0img = discord.File('bdayseng.png')
    ec0.set_image(url='attachment://bdayseng.png')
    await ctx.channel.send(embed = ec0, file = ec0img)
    ec0bd = discord.Embed(title = ':closed_book: Information about users on the server :closed_book:', description = '`Nickname | Name | Date of birth | Age | City`', color = 0xffffff)
    ec0bd.add_field(
        name = ':snowman: Winter :snowflake:', 
        value = '<@334301539860742145> | Misha | january 15 | 23 y.o. | Krasnodar\n<@595328091962867717>  | Alleksh  | january 29 | 17 y.o. | Lviv\n<@289430056261124097> | Igaryasha | january 31 | 20 y.o. | Ekaterinburg\n<@372007261876256768>  | Daniel | february 6 | 16 y.o. | Petropavl\n<@276780906654728202> | Max | february 20 | 18 y.o. | Kyiv\n<@564581176631885834> | Nikolay | february 22 | 15 y.o. | Simferopol\nᅠ',
        inline = False) 
    ec0bd.add_field(
        name = ':partly_sunny: Spring :wilted_rose:',
        value = '<@345085964500074497> | Julia | march 18 | 20 y.o. | Ekaterinburg\nᅠ',
        inline = False)
    ec0bd.add_field(
        name = ':sun_with_face: Summer :island:',
        value = '<@529232630420340736> | Artem | june 16 | 21 y.o. | Penza\n<@272388934166773763> | Dmitry | june 18 | 17 y.o. | Kyiv\n<@339776970609131521> | Alexey | july 5 | 16 y.o. | Penza\n<@423184105929310209> | Lina | july 26 | 19 y.o. | Nizhny Novgorod\n<@327402918481231873> | Nikita | august 6 | 18 y.o. | Ivatsevichi/Baranovichi\n<@297658029304971265> | Denis | august 16 | 19 y.o. | Nizhny Novgorod\n <@412298602925391873> | Kristina | August 25 | 17 y.o. | Oryol\nᅠ',
        inline = False)
    ec0bd.add_field(
        name = ':umbrella: Autumn :fallen_leaf:',
        value = '<@858102341555585055> | Semen | today | 37 y.o. | Kryzhopil\n<@381768919301750791> | Dmitry | september 4 | 21 y.o. | Mykolaiv\n<@619831709839523840> | Artem | september 5 | 19 y.o. | Kyiv\n<@402044993054703618> | Ilya | september 10 | 18 y.o. | Donetsk\n<@677258830111047690> | Ksyusha | september 12 | 16 y.o. | Chelyabinsk\n<@650028253750493185> | Anastasia | september 22 | 16 y.o. | Odesa\n<@460031382723362827> | Artem | september 23 | 18 y.o. | Kyiv\n<@409750693851824130> | Egor | october 5 | 14 y.o. | Simferopol\n<@414051284094812160> | Alexander | october 12 | 18 y.o. | Kyiv\n<@385542550729130006> | Vitaly | november 12 | 23 y.o. | Kyiv\n <@444946884805787648> | Artem | november 15 | 16 y.o. | Klaipeda\n<@570311375633514496> | Danya | november 19 | 17 y.o. | Cheboksary\n<@733063317764964352> | Daria | november 20 | 18 y.o. | Krasnodar\n<@421930169713033228> | Vladimir | november 26 | 18 y.o. | Cherkasy\n<@390836335000420352> | Artem | november 30 | 19 y.o. | Ekaterinburg\nᅠ',
        inline = False)
    await ctx.channel.send(embed = ec0bd)
    ec1 = discord.Embed(color = 0xffffff)
    ec1img = discord.File('bdaysrus.png')
    ec1.set_image(url='attachment://bdaysrus.png')
    await ctx.channel.send(embed = ec1, file = ec1img)
    ec1bd = discord.Embed(title = ':closed_book: Информация о пользователях на сервере :closed_book:', description = '`Никнейм | Имя | День рождения | Возраст | Город`', color = 0xffffff)
    ec1bd.add_field(
        name = ':snowman: Зима :snowflake:', 
        value = '<@334301539860742145> | Миша | 15 января | 23 года | Краснодар\n<@595328091962867717>  | Аллекш  | 29 января | 17 лет | Львов\n<@289430056261124097> | Игаряша | 31 января | 20 лет | Екатеринбург\n<@372007261876256768> | Даниил | 6 февраля | 16 лет | Петропавловск\n<@276780906654728202> | Макс | 20 февраля | 18 лет | Киев\n<@564581176631885834> | Николай | 22 февраля | 15 лет | Симферополь\nᅠ',
        inline = False) 
    ec1bd.add_field(
        name = ':partly_sunny: Весна :wilted_rose:',
        value = '<@345085964500074497> | Юлия | 18 марта | 20 лет | Екатеринбург\nᅠ',
        inline = False)
    ec1bd.add_field(
        name = ':sun_with_face: Лето :island:',
        value = '<@529232630420340736> | Артём | 16 июня | 21 год | Пенза\n<@272388934166773763> | Дмитрий | 18 июня | 17 лет | Киев\n<@339776970609131521> | Лёша | 5 июля | 16 лет | Пенза\n<@423184105929310209> | Лина | 26 июля | 19 лет | Нижний Новгород\n<@327402918481231873> | Никита | 6 августа | 18 лет | Ивацевичи/Барановичи\n<@297658029304971265> | Денис | 16 августа | 19 лет | Нижний Новгород\n <@412298602925391873> | Кристина | 25 августа | 17 лет | Орёл\nᅠ',
        inline = False)
    ec1bd.add_field(
        name = ':umbrella: Осень :fallen_leaf:',
        value = '<@858102341555585055> | Семён | сегодня | 37 лет | Крыжополь\n<@381768919301750791> | Дмитрий | 4 сентября | 21 год | Николаев\n<@619831709839523840> | Артём | 5 сентября | 19 лет | Киев\n<@402044993054703618> | Илья | 10 сентября | 18 лет | Донецк\n<@677258830111047690> | Ксюша | 12 сентября | 16 лет | Челябинск\n<@650028253750493185> | Анастасия | 22 сентября | 16 лет | Одесса\n<@460031382723362827> | Артём | 23 сентября | 18 лет | Киев\n<@409750693851824130> | Егор | 5 октября | 14 лет | Симферополь\n<@414051284094812160> | Александр | 12 октября | 18 лет | Киев\n<@385542550729130006> | Виталик | 12 ноября | 23 года | Киев\n <@444946884805787648> | Артём | 15 ноября | 16 лет | Клайпеда\n<@570311375633514496> | Даня | 19 ноября | 17 лет | Чебоксары\n<@733063317764964352> | Дашуля | 20 ноября | 18 лет | Краснодар\n<@421930169713033228> | Владимир | 26 ноября | 18 лет | Черкассы\n<@390836335000420352> | Артём | 30 ноября | 19 лет | Екатеринбургᅠ',
        inline = False)
    await ctx.channel.send(embed = ec1bd)

@observer.command()
async def eng(ctx):
    await ctx.channel.purge(limit=1)
    ec0 = discord.Embed(color = 0xffffff)
    ec0img = discord.File('mp.png')
    ec0.set_image(url='attachment://mp.png')
    await ctx.channel.send(embed = ec0, file = ec0img)
    ec1 = discord.Embed(color = 0xffffff)
    ec1img = discord.File('greng.png')
    ec1.set_image(url='attachment://greng.png')
    await ctx.channel.send(embed = ec1, file = ec1img)
    ec2 = discord.Embed(title = 'The server "Adequate Inadequacy" was created on 2 Aug, 2019.', description = 'In this server we have only cool users with own local humour, interests and so on.\nWe think that everyone must be polite with anyone, respect any opinion and do not split the team onto parts!\nBe adequate and try to do nothing terrible.', color = 0xffffff)
    await ctx.channel.send(embed = ec2)
    e = discord.Embed(title = ':octagonal_sign: ADMINISTRATION OF THE SERVER :octagonal_sign:', color = 0xffffff)
    e.add_field(
        name = ':black_joker: HeadAdministrator  :black_joker:',
        value = 'Role: <@&774384435772260373>\n Member: <@402044993054703618>',
        inline = False)
    e.add_field(
        name = ':diamond_shape_with_a_dot_inside: Pre-head Administrator :diamond_shape_with_a_dot_inside:',
        value = 'Role: <@&678985540112220160>\n Members: <@595328091962867717> | <@858102341555585055>',
        inline = False)
    e.add_field(
        name = ':large_orange_diamond: St. Administrator :large_orange_diamond:',
        value = 'Role: <@&680061400969773119>\n Members: <@444946884805787648> | <@460031382723362827> | <@289430056261124097>',
        inline = False)
    e.add_field(
        name = ':large_blue_diamond: Common Administrator :large_blue_diamond:',
        value = 'Role: <@&678985864680046592>\n Members: <@421930169713033228> | <@619831709839523840> | <@327402918481231873> | <@733063317764964352> ',
        inline = False)
    await ctx.channel.send(embed = e)
    e = discord.Embed(title = ':octagonal_sign: TEAMS IN THE SERVER :octagonal_sign:', color = 0xffffff)
    e.add_field(
        name = ':purple_square: GAMES :purple_square:',
        value = '**Minecraft lovers**\nRole: <@&772175163843674122>\n\n**Dota lovers**\nRole: <@&795655650041528370>\n\n**Terraria lovers**\nRole: <@&808390166984917007>',
        inline = True)
    e.add_field(
        name = ':green_square: LIFE :green_square:', 
        value = '**Reader Team**\nRole: <@&804823346394824735>\n\n**Sport Team**\nRole: <@&791998561763328010>',
        inline = True)
    e.add_field(
        name = ':yellow_square: OTHERS :yellow_square:',
        value = '**The team of development**\nRole: <@&808324715924029471>\n\n**Music lovers**\nRole: <@&780778939848982579>\n\n**Horny-club**\nRole: <@&816941141801959445>',
        inline = True)
    await ctx.channel.send(embed = e)
    e = discord.Embed(title = ':robot: BOTS :robot:', color = 0xffffff)
    e.add_field(
        name = 'Name | Prefix | Owner (if has)',
        value = '<@235148962103951360> | !\n<@155149108183695360> | ?\n<@310848622642069504> | !\n<@900676952774570025> | // | <@402044993054703618>\n<@812729764477534229> | / | <@444946884805787648>',
        inline = False)
    await ctx.channel.send(embed = e)
    e = discord.Embed(title = 'Server invite', description = 'https://discord.gg/QN52MhW - Server invitation, endless and has infinite number of uses.', color = 0xffffff)
    await ctx.channel.send(embed = e)

@observer.command(pass_context = True)
async def rus(ctx):
    await ctx.channel.purge(limit=1)
    ec1 = discord.Embed(color = 0xffffff)
    ec1img = discord.File('grrus.png')
    ec1.set_image(url='attachment://grrus.png')
    await ctx.channel.send(embed = ec1, file = ec1img)
    ec2 = discord.Embed(title = 'Сервер "Adequate Inadequacy" был создан 2 августа, 2019 года.', description = 'На этом сервере только самые крутые пользователи со своим местным юмором, интересами и так далее.\n Мы считаем, что каждый должен быть вежлив с кем угодно, уважать любое мнение и не разделять сообщество на части!\n Будьте адекватны и старайтесь не делать ничего ужасного.', color = 0xffffff)
    await ctx.channel.send(embed = ec2)
    e = discord.Embed(title = ':octagonal_sign: АДМИНИСТРАЦИЯ СЕРВЕРА :octagonal_sign:', color = 0xffffff)
    e.add_field(
        name = ':black_joker: Администратор-управляющий  :black_joker:',
        value = 'Роль: <@&774384435772260373>\n Участник: <@402044993054703618>',
        inline = False)
    e.add_field(
        name = ':diamond_shape_with_a_dot_inside: Заместитель Администратора-управляющего :diamond_shape_with_a_dot_inside:',
        value = 'Роль: <@&678985540112220160>\n Участники: <@595328091962867717> | <@858102341555585055>',
        inline = False)
    e.add_field(
        name = ':large_orange_diamond: Старший Администратор :large_orange_diamond:',
        value = 'Роль: <@&680061400969773119>\n Участники: <@444946884805787648> | <@460031382723362827> | <@289430056261124097>',
        inline = False)
    e.add_field(
        name = ':large_blue_diamond: Администратор :large_blue_diamond:',
        value = 'Роль: <@&678985864680046592>\n Участники: <@421930169713033228> | <@619831709839523840> | <@327402918481231873> | <@733063317764964352> ',
        inline = False)
    await ctx.channel.send(embed = e)
    e = discord.Embed(title = ':octagonal_sign: КОМАНДЫ ПО ИНТЕРЕСАМ НА СЕРВЕРЕ :octagonal_sign:', color = 0xffffff)
    e.add_field(
        name = ':purple_square: ИГРЫ :purple_square:',
        value = '**Майнкрафтеры**\nРоль: <@&772175163843674122>\n\n**Дотеры**\nРоль: <@&795655650041528370>\n\n**Терраристы**\nРоль: <@&808390166984917007>',
        inline = True)
    e.add_field(
        name = ':green_square: ЖИЗНЬ :green_square:', 
        value = '**Чтецы**\nРоль: <@&804823346394824735>\n\n**Спортивная команда**\nРоль: <@&791998561763328010>',
        inline = True)
    e.add_field(
        name = ':yellow_square: ДРУГОЕ :yellow_square:',
        value = '**Команда разработчиков**\nРоль: <@&808324715924029471>\n\n**Любители музыки**\nРоль: <@&780778939848982579>\n\n**Horny-club**\nРоль: <@&816941141801959445>',
        inline = True)
    await ctx.channel.send(embed = e)
    e = discord.Embed(title = ':robot: БОТЫ :robot:', color = 0xffffff)
    e.add_field(
        name = 'Имя | Префикс | Владелец (если имеется)',
        value = '<@235148962103951360> | !\n<@155149108183695360> | ?\n<@310848622642069504> | !\n<@900676952774570025> | // | <@402044993054703618>\n<@812729764477534229> | / | <@444946884805787648>',
        inline = False)
    await ctx.channel.send(embed = e)
    e = discord.Embed(title = 'Серверное приглашение', description = 'https://discord.gg/QN52MhW - Приглашение на сервер, бессрочное и имеет неограниченное количество применений.', color = 0xffffff)
    await ctx.channel.send(embed = e)

@observer.command(pass_context = True)
async def q(ctx):
    await ctx.channel.purge(limit=1)
    ec = discord.Embed(title = '**Завершение сеанса**', description = f'Вызвано пользователем {ctx.author.mention}', color = 0x6450fa)
    ec.set_author(name = f'{ctx.author.name} использовал {ctx.message.content}', icon_url = ctx.author.avatar_url)
    ec.set_thumbnail(url = ctx.author.avatar_url)
    await ctx.channel.send(embed = ec, delete_after = 3)
    await asyncio.sleep(4)
    await observer.close()

@observer.command()
async def clear(ctx, x=0):
	if x == 0:
		await ctx.send('Eblo')
	else:
	    await ctx.channel.purge(limit=x+1)

observer.run(token)