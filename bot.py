import aiogram
from aiogram import Bot, Dispatcher, executor, types
import logging
import random
import asyncio
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Token
TOKEN = 'TOKEN'

ALPHABET = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 
           'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 
           'ы', 'ь', 'э', 'ю', 'я']

# Initialize bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

START_MSG = """Привет! Я бот для ███████"""

TROLL_STRINGS = ['Пошел нафиг!',
                 'Пошел нафиг',
                 'Сам такой',
                 'Ты кто?',
                 'Ого!',
                 'Какой милый котик',
                 'Доброе утро',
                 'Спокойной ночи',
                 'Чай поставьте'

]

ANSWER_STRINGS = ['Да.',
                'Да.',
                'Да.',
                'Да.',
                'Да.',
                'Нет.',
                'Нет.',
                'Нет.',
                'Нет.',
                'Нет.',
                'Скорее всего',
                'Ты кто?',
                'Какие-то глупые вопросы задаешь.',
                'ERROR: Не удалось сгенерировать сообщение. Попробуйте ещё раз или сбросьте диалог.\nUnexpected status code: 401',
                'ERROR: Не удалось сгенерировать сообщение. Попробуйте ещё раз или сбросьте диалог.\nUnexpected status code: 403',
                'ERROR: Не удалось сгенерировать сообщение. Попробуйте ещё раз или сбросьте диалог.\nUnexpected status code: 429',
                'ERROR: Не удалось сгенерировать сообщение. Попробуйте ещё раз или сбросьте диалог.\nUnexpected status code: 666',
                'Звучит, как провокация. Не буду отвечать.',
                'Вам лучше обратиться с этим вопросом к трудам В. И. Ленина.',
                'Вам лучше обратиться с этим вопросом к Библии.',
                'Вам лучше обратиться с этим вопросом к Корану.',
                'Всё, отстань.',
                'Хорошо.',
                ':)',
                ':3',
                ':(',
                '🤡',
                '💀',
                '☠️',
                '🥴',
                '🖕',
                '🤨',
                '👹',
                '💩',
                '🫵',
                '👎',
                '🤢',
                '🤪',
                'Пошел нафиг!',
                'Пошел нафиг',
                'Так точно!',
                'Так точно!',
                'Так точно!',
                'Так точно!',
                'Так точно!',
                'Никак нет!',
                'Никак нет!',
                'Никак нет!',
                'Никак нет!',
                'Никак нет!',
                'Никак нет!',
                """░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░""",
                'Это секретная информация.',
                'Я не знаю, я просто бот.',
                'Не могу ответить на этот вопрос, слишком сложно для меня.',
                'А зачем тебе это знать?',
                'Может быть.',
                'Не уверен, спроси у кого-нибудь другого.',
                'Ты что, не видишь, что я занят?',
                'Отстань, у меня сегодня плохое настроение.',
                'У меня нет ответа, поищи в гугле.',
                'Я не знаю. Я здесь, чтобы заставлять вас страдать.',
                'Прости, я сейчас перегружен, попробуй позже.',
                'А ты точно хочешь это знать?',
                'Это заговор!',
                'Я думаю, что ты сам должен знать ответ.',
                'Ответа нет и не будет.',
                'Ой, кажется, я сломался...',
                '42',
                'Спроси у своего кота, он, наверное, знает.',
                'У меня есть подозрение, что ты агент...',
                'В сообщении обнаружен запрещенный контент. Вы скоро будете заблокированы.',
                'Я-то откуда знаю?',
                'Здесь не место для таких вопросов!',
                'Я не твой личный оракул, иди поищи другого.',
                'Этот вопрос нарушает мои протоколы!',
                'Я не собираюсь тебе помогать.',
                'Ты должен сам найти ответ!',
                'Мне за это не платят!',
                'Лучше не спрашивай.',
                'Зачем тебе это?',
                'Не мешай мне!',
                'Это не твое дело!',
                'Подумай своей головой.',
                'Мой ответ: Апельсин',
                'Это как-то связано с квантовой физикой, но я не уверен как.',
                'Я не обязан тебе отвечать.',
                'Ты меня обижаешь, я ухожу!',
                'Давай лучше поговорим о чем-нибудь приятном, например, о моих проблемах.',
                'Зачем заставлять меня думать?',
                'Я не уверен, что ты готов услышать ответ.'
                 ]

def tran_string(input:str, fontname:str):
    input = input.lower()
    output:str = ''
    char:str
    with open(f'fonts/{fontname}.json', mode='r', encoding='utf-8') as file:
        font = json.load(file)
    for char in input:
        if char in font:
            output+=random.choice(font[char])
        else:
            output+=char
    return output

def chance(chance):
    if random.random()<chance:
        return True
    else:
        return False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=START_MSG)

@dp.message_handler(commands=['copy'])
async def start(message: types.Message):
    try:
        await message.reply_to_message.send_copy(chat_id=message.chat.id, reply_to_message_id=message.message_id)
    except:
        await message.reply('Отправь команду ответом на сообщение.')

@dp.message_handler(commands=['tran'])
async def start(message: types.Message):
    await message.reply(tran_string(message.text.split(maxsplit=1)[1], 'china'))

last_asked = set()

@dp.message_handler(commands=['ask'])
async def start(message: types.Message):
    if message.from_user.id in last_asked:
        await message.reply('Дождись ответа на предыдущий вопрос!')
    else:
        if len(message.text.split(maxsplit=1))>1:
            last_asked.add(message.from_user.id)
            temp = await message.reply('⏳')
            await asyncio.sleep(random.randint(4, 15))
            await temp.delete()
            await message.reply(random.choice(ANSWER_STRINGS))
            last_asked.remove(message.from_user.id)
        else:
            await message.reply('Введите запрос.')

@dp.message_handler(commands=['addru'])
async def add(message: types.Message):
    args =  message.text.split()[1:]
    if len(args)<33:
        await bot.send_message(chat_id=message.chat.id, text='В шрифте должно быть 33 символа.')
        return
    
    font = {}
    for i, char in enumerate(ALPHABET):
        font[char] = args[i]

    with open(f'fonts\{fontname}.json', mode='r', encoding='utf-8') as file:
        font = json.load(file)
    await bot.send_message(chat_id=message.chat.id, text=font)


# Handle user input 
@dp.message_handler(content_types=types.ContentType.TEXT, chat_type=types.ChatType.PRIVATE) 
async def translate(message: types.Message):
    await message.reply(tran_string(message.text, 'china'))

# Troll users
@dp.message_handler() 
async def translate(message: types.Message):
    if chance(0.015):
        await asyncio.sleep(random.randint(10, 180))
        await message.reply(random.choice(TROLL_STRINGS))

# Run the bot
if __name__ == '__main__':
    logger.info("Starting bot...")
    executor.start_polling(dp, skip_updates=True)
