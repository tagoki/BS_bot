import telebot
from telebot import types
import sys
from battles.one_s.all_balltles_one_s import ALL_BATTLES
from links.links_for_projects.links_projects import BSB_LINK, BST_LINK, BSN_LINK
import os
from colorama import Fore
from art import tprint
from banner_choice import banner
sys.path.append('/home/haku/BS')

lbs = tprint('launcher   Brilliant   segments')

print(banner)

choice_operations = int(input('Введите номер операци:\n'))

if choice_operations == 1:
    TOKIN = input('Пожалуйста, введи свой API токен от BotdFather:\n')
elif choice_operations == 2:
    print('https://t.me/+qYRwfhNobn8xOTI6')
    exit()
else:
    print(Fore.RED +'Что то пошло не так! Перезапустите программу в введите валидный номер!')


try:
   bot = telebot.TeleBot(TOKIN)
except Exception:
    print(Fore.RED + "Токин неверный или произошла ошибка! Перезапустите программу и введите токен снова.")
    exit()


@bot.message_handler(commands=['start'])              
def start_bot(message):
    bot.send_message(message.chat.id, f'''🌟 Приветствуем вас, {message.from_user.first_name} ! 🌟\nЭтот бот принадлежит каналу Briliant segments и создан для того, чтобы предоставлять полезную информацию о наших участниках.\n💡 Что может сделать этот бот?\n -Выдавать актуальные данные о участниках\n -Выдавать ссылки на наши проекты\n -Делиться таблицой с результатами батлов''')

@bot.message_handler(commands=['all_projects'])
def projects(message):
    bot.send_message(message.chat.id, f'''У нас есть 3 основных проекта:\n\n<a href="{BSB_LINK}">BSB</a> - это платформа, где проходят увлекательные дебаты и дискуссии, а также различные батлы. Здесь участники могут обмениваться мнениями и участвовать в обсуждениях на самые актуальные темы.\n\n<a href="{BST_LINK}">BST</a> — это форум, где публикуются разнообразные посты на различные темы, начиная от математики и заканчивая криминалистикой. У нас вы найдете увлекательные обсуждения, полезные материалы и интересные мнения участников. Мы стремимся создать пространство для обмена знаниями и мнениями, где каждый может поделиться своим опытом и задать вопросы по интересующим его темам.\n\n<a href="{BSN_LINK}">BSN</a> — это основной новостной канал, на котором публикуются главные новости нашего комьюнити. Здесь вы найдете актуальную информацию о событиях, обновлениях и достижениях, связанных с нашим сообществом. Мы стремимся держать наших участников в курсе всех важных событий и делиться интересными новостями, которые могут быть полезны и увлекательны для всех.\n''', disable_web_page_preview=True, parse_mode='html')

@bot.message_handler(commands=['all_table'])
def print_question(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('1', callback_data='1'))
    bot.send_message(message.chat.id, 'Пожалуйста, выберите сезон:', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == '1')
def print_table_bat(callback):
    bot.send_message(callback.message.chat.id, f"Посмотреть результаты батлов за 1 сезон:\n\n{ALL_BATTLES}", parse_mode='Markdown', disable_web_page_preview=True)

@bot.message_handler(commands=['stat'])
def print_question_player_statistics(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('hiro', callback_data='hiro'))
    markup.add(types.InlineKeyboardButton('shako', callback_data='shako'))
    bot.send_message(message.chat.id,'Пожалуйста, выберите игрока:', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data in ['hiro', 'shako'])
def print_statistics_players(callback):
    if callback.data == 'hiro':
        bot.send_message(callback.message.chat.id, 'Статистика игрока hiro:\nw - 0\nl - 1')
    elif callback.data == 'shako':
        bot.send_message(callback.message.chat.id, 'Статистика игрока shako:\nw -1\nl-0')

@bot.message_handler(commands=['players'])
def print_playerss(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Dizzy', callback_data='dizzy'))
    bot.send_message(message.chat.id, 'Выберите игрока, чтобы просмотреть информацию о нём:', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'dizzy')
def print_dizzy(callback):
    bot.send_message(callback.message.chat.id, '◈━◈━◈━◈━◈◈━◈━◈━◈━◈◈━◈━◈\n\n୨⎯ player ⎯୧ \n╰┈➤ Dizzy\n\n୨⎯ strengths ⎯୧ \n╰┈➤Foresight\n\n୨⎯ quote ⎯୧\n\n◤──•~❉᯽❉~•──◥ \nЗлых людей не существует, \nсуществует тяжелый опыт и больные люди\n◣──•~❉᯽❉~•──◢  \n\n◈━◈━◈━◈━◈◈━◈━◈━◈━◈◈━◈━◈')


@bot.message_handler(commands=['info_events'])
def print_question_info_eventes(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Lie on Lie', callback_data='lol'))
    bot.send_message(message.chat.id, 'Выберите, пожалуйства, ивент, по которому хотите посмотреть информацию', reply_markup=markup)
@bot.callback_query_handler(func=lambda callback: callback.data == 'lol')
def print_info_events(callback):
    if callback.data == 'lol':
        bot.send_message(callback.message.chat.id, 'https://t.me/fit_lieonlie')






bot.polling(none_stop=True)


if __name__ == '__main__':
    main()