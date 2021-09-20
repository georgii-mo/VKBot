#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import vk_api
#from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import json
import requests
import time
import datetime

#тексты матки
mes1 = 'Обучающиеся из числа детей-сирот и детей, оставшихся без попечения родителей.\n\nНеобходимые документы:\n1. Копия свидетельства о рождении;\n\n2. Документы, подтверждающие отсутствие родителей:\n• Копии свидетельств о смерти;\n• Копии постановлений суда о лишении родительских прав или решение суда об установлении опеки;\n• Отобрании ребенка;\n• Признание родителей безвестно отсутствующими;\n• Объявлении умершими;\n• Признании недееспособными;\n• Копии приговора суда об осуждении родителей;\n• Медицинский документ о длительной болезни родителей, препятствующей выполнению ими своих обязанностей;\n• Документ, подтверждающий то, что ребенок был подкинут;\n• Материалы о розыске родителей и др.'
mes2 = '2'
mes3 = '3'
mes4 = '4'
mes5 = '5'
mes6 = '6'
mes7 = '7'
mes8 = '8'
mes9 = '9'
mes10 = '10'
mes11 = '11'
mes12 = '12'
mes13 = '13'

mes = [mes1, mes2, mes3, mes4, mes5, mes6, mes7, mes8, mes9, mes10, mes11, mes12, mes13]

#текст кричалок
krich = ['Когда ИММиТ - всегда ИММиТ!','Если в трусиках кипит, знают все - идет ИММиТ','Кроха не души','Кит-убийца','Аоаоаоаоаоа'] #,'Машьянов - лох'

#анонсы
anons = '15.03.21 - в 15.00 какая то дичь\n23.07.21 - тоже хуета'

#приветственный текст
priv = 'Привет!\nЯ - интерактивный помощник группы Профбюро ИММиТ и я с радостью готов вам помочь!'

#фото из альбома
photo = list(range(457239017, 457239034))  #оооочень топорно, просто номера фото в альбоме

#массив из кнопок матки
MAT_BUTTON = {'1','2','3','4','5','6','7','8','9','10','11','12','13'}

now = datetime.datetime.now()

#отправка нового поста
def send(user_id, attachment):
    random_id = random.randint(-2147483648, +2147483648)
    vk.messages.send(
        peer_ids=user_id, #несколько id
        random_id=random_id,
        message="Новый пост в группе!",
        attachment=attachment
        )
#отправка сообщения
def write_message(sender, message, keyboard = None):
    post = {'chat_id': sender, 'message': message, "random_id": random.randint(-2147483648, +2147483648)}
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post
    vk_session_group.method('messages.send', post)

token = 'f2ab0f6184bd9e5e7a62a0d439897d43c0dfb3cb90404ed1914f5b62b0b177975d1aabb929def8c18d917'

vk_session_group = vk_api.VkApi(token = token) # Токен группы (изменяем настройки в Long)
vk = vk_session_group.get_api()
longpoll_group = VkBotLongPoll(vk_session_group, 192243844)  # ID группы смотрим через запись)

#списки бесед
user_id = list(range(2000000001, 2000000100)) #очень топорно делаю, по хорошему последнее число надо заменить на функцию определения количества бесед +1


#добавляем кнопки и их значения
keyboard = VkKeyboard(inline=True) # заменить, если хочу клавой  one_time=True
keyboard.add_callback_button(label='Сюрприз', color=VkKeyboardColor.SECONDARY, payload={"type": "show_snackbar", "text": None}) #сплывающее сообщение NEGATIVE
#keyboard.add_callback_button(label='Фото', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_200500_type_edit"}) #рандомные фото из альбома POSITIVE
keyboard.add_callback_button(label='Анонсы', color=VkKeyboardColor.SECONDARY, payload={"type": "my_own_100500_type_edit"}) #переключение на анонсы
keyboard.add_line()
keyboard.add_callback_button(label='Задать вопрос', color=VkKeyboardColor.PRIMARY, payload={"type": "open_link", "link": "https://vk.me/botforpractice"}) #ссылка на сообщения группы
keyboard.add_line()
keyboard.add_callback_button(label='Материальная помощь', color=VkKeyboardColor.NEGATIVE, payload={"type": "type_for_mat_edit"}) #переключение на второе меню

#кнопки анонса
keyboard_2 = VkKeyboard(inline=True)
keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"}) #переключение на основное меню

#кнопки 1 страницы меню матки
keyboard_3 = VkKeyboard(inline=True)
keyboard_3.add_callback_button(label='Без попечения родителей', color=VkKeyboardColor.SECONDARY, payload={"type": "1"})
keyboard_3.add_line()
keyboard_3.add_callback_button(label='Потеря родителя', color=VkKeyboardColor.SECONDARY, payload={"type": "2"})
keyboard_3.add_line()
keyboard_3.add_callback_button(label='Инвалиды', color=VkKeyboardColor.SECONDARY, payload={"type": "3"})
keyboard_3.add_line()
keyboard_3.add_callback_button(label='Участники военных действий', color=VkKeyboardColor.SECONDARY, payload={"type": "4"})
keyboard_3.add_line()
keyboard_3.add_callback_button(label='Радиационные катастрофы', color=VkKeyboardColor.SECONDARY, payload={"type": "5"})
keyboard_3.add_line()
keyboard_3.add_callback_button(label='-2-', color=VkKeyboardColor.SECONDARY, payload={"type": "type_for_mat_edit_2"}) #переключение на 2 страницу матки
keyboard_3.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "type_for_mat_edit"}) #переключение на основное меню
keyboard_3.add_callback_button(label='-3-', color=VkKeyboardColor.SECONDARY, payload={"type": "type_for_mat_edit_3"}) #переключение на 3 страницу матки

#кнопки 2 страницы матки
keyboard_4 = VkKeyboard(inline=True)
keyboard_4.add_callback_button(label='Тяжелое мат. положение', color=VkKeyboardColor.SECONDARY, payload={"type": "6"})
keyboard_4.add_line()
keyboard_4.add_callback_button(label='Многодетные семьи', color=VkKeyboardColor.SECONDARY, payload={"type": "7"})
keyboard_4.add_line()
keyboard_4.add_callback_button(label='Проезд', color=VkKeyboardColor.SECONDARY, payload={"type": "8"})
keyboard_4.add_line()
keyboard_4.add_callback_button(label='Ухудшение здоровья', color=VkKeyboardColor.SECONDARY, payload={"type": "9"})
keyboard_4.add_line()
keyboard_4.add_callback_button(label='Чрезвычайные ситуации', color=VkKeyboardColor.SECONDARY, payload={"type": "10"})
keyboard_4.add_line()
keyboard_4.add_callback_button(label='-1-', color=VkKeyboardColor.SECONDARY, payload={"type": "type_for_mat_edit_2"}) #переключение на 1 страницу матки
keyboard_4.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "type_for_mat_edit"}) #переключение на основное меню
keyboard_4.add_callback_button(label='-3-', color=VkKeyboardColor.SECONDARY, payload={"type": "type_for_mat_edit_4"}) #переключение на 3 страницу матки


#кнопки 3 страницы матки
keyboard_5 = VkKeyboard(inline=True)
keyboard_5.add_callback_button(label='Рождение ребенка', color=VkKeyboardColor.SECONDARY, payload={"type": "11"})
keyboard_5.add_line()
keyboard_5.add_callback_button(label='Уход за ребенком', color=VkKeyboardColor.SECONDARY, payload={"type": "12"})
keyboard_5.add_line()
keyboard_5.add_callback_button(label='Доноры', color=VkKeyboardColor.SECONDARY, payload={"type": "13"})
keyboard_5.add_line()
keyboard_5.add_callback_button(label='-1-', color=VkKeyboardColor.SECONDARY, payload={"type": "type_for_mat_edit_3"}) #переключение на 1 страницу матки
keyboard_5.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "type_for_mat_edit"}) #переключение на основное меню
keyboard_5.add_callback_button(label='-2-', color=VkKeyboardColor.SECONDARY, payload={"type": "type_for_mat_edit_4"}) #переключение на 2 страницу матки

#кнопка выхода из категории
keyboard_6 = VkKeyboard(inline=True)
keyboard_6.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "type_for_mat_edit"}) #переключение на основное меню

while True:
    try:
        f_toggle: bool = False
        f_toggle_2: bool = False
        f_toggle_3: bool = False
        f_toggle_4: bool = False
        f_toggle_5: bool = False
        f_toggle_6: bool = False
        for event in longpoll_group.listen():

            #если вышла новая запись в группе
            if event.type == VkBotEventType.WALL_POST_NEW and event.object['text']:
                #var = ['#Важное'] #добавляем слова в запись, на которые будет реагировать бот
                if '#Важное_ИММиТ' in event.object['text']:
                    id_ = event.object['id'] #ID поста
                    owner_id_ = event.group_id #ID группы
                    wall_id = f'wall-{owner_id_}_{id_}'
                    #print('Новый пост! - ', wall_id)
                    attachment = wall_id
                    send(user_id, attachment)

            #если бота отметили, работает, версия API на 5.131
            elif event.type == VkBotEventType.MESSAGE_NEW:
                print('обратились к боту в '+str(event.chat_id)+' чате')
                message=priv
                write_message(event.chat_id, message, keyboard)

            #взаимодействие с кнопками
            elif event.type == VkBotEventType.MESSAGE_EVENT:
                if event.object.payload.get('type') == 'open_link':
                    print('сообщения с группой')
                    r = vk.messages.sendMessageEventAnswer(
                              event_id=event.object.event_id,
                              user_id=event.object.user_id,
                              peer_id=event.object.peer_id,
                              event_data=json.dumps(event.object.payload))

            	#для фото
                elif event.object.payload.get('type') == "my_own_200500_type_edit":
                    photo_id = random.choice(photo)   #ID альбома?
                    attachment=f'photo-192243844_{photo_id}' #в ссылке ID группы и ID фото
                    last_id = vk.messages.edit(
                              peer_id=event.obj.peer_id,
                              message=(priv if f_toggle else None),
                              attachment=(None if f_toggle else attachment),
                              conversation_message_id=event.obj.conversation_message_id,
                              keyboard=(keyboard if f_toggle else keyboard_2).get_keyboard())
                    f_toggle = not f_toggle

            	#для кричалки
                elif event.object.payload.get('type') == 'show_snackbar':
                     print('кричалка')
                     r = vk.messages.sendMessageEventAnswer(
                              event_id=event.object.event_id,
                              user_id=event.object.user_id,
                              peer_id=event.object.peer_id,
                              event_data=json.dumps({"type": "show_snackbar", "text": random.choice(krich)}))

            	#для анонса
                elif event.object.payload.get('type') == 'my_own_100500_type_edit':
                    print('анонс')
                    last_id = vk.messages.edit(
                              peer_id=event.obj.peer_id,
                              message=(priv if f_toggle else anons),
                              conversation_message_id=event.obj.conversation_message_id,
                              keyboard=(keyboard if f_toggle else keyboard_2).get_keyboard())
                    f_toggle = not f_toggle

                #для переключенния на меню матки
                elif event.object.payload.get('type') == 'type_for_mat_edit':
                    print('матка')
                    last_id = vk.messages.edit(
                              peer_id=event.obj.peer_id,
                              message=(priv if f_toggle_2 else 'ᅠᅠᅠᅠᅠКАТЕГОРИИ'),
                              conversation_message_id=event.obj.conversation_message_id,
                              keyboard=(keyboard if f_toggle_2 else keyboard_3).get_keyboard())
                    f_toggle_2 = not f_toggle_2


                #РАБОТАЕМ С КНОПКАМИ В МАТКЕ
                elif event.type == VkBotEventType.MESSAGE_EVENT:
                    #для переключенния на второе меню матки из первого
                    if event.object.payload.get('type') == 'type_for_mat_edit_2':
                        print('матка 2 стр')
                        last_id = vk.messages.edit(
                          peer_id=event.obj.peer_id,
                          message='ᅠᅠᅠᅠᅠКАТЕГОРИИ',
                          conversation_message_id=event.obj.conversation_message_id,
                          keyboard=(keyboard_3 if f_toggle_3 else keyboard_4).get_keyboard())
                        f_toggle_3 = not f_toggle_3


                    #для переключенния на первое меню матки из третьего
                    elif event.object.payload.get('type') == 'type_for_mat_edit_3':
                        print('матка 1 стр')
                        last_id = vk.messages.edit(
                          peer_id=event.obj.peer_id,
                          message='ᅠᅠᅠᅠᅠКАТЕГОРИИ',
                          conversation_message_id=event.obj.conversation_message_id,
                          keyboard=(keyboard_3 if f_toggle_4 else keyboard_5).get_keyboard())
                        f_toggle_4 = not f_toggle_4



                    #для переключенния на третье меню матки из второго
                    elif event.object.payload.get('type') == 'type_for_mat_edit_4':
                        print('матка 3 стр')
                        last_id = vk.messages.edit(
                                    peer_id=event.obj.peer_id,
                                    message='ᅠᅠᅠᅠᅠКАТЕГОРИИ',
                                    conversation_message_id=event.obj.conversation_message_id,
                                    keyboard=(keyboard_4 if f_toggle_5 else keyboard_5).get_keyboard())
                        f_toggle_5 = not f_toggle_5




                    elif event.object.payload.get('type') in MAT_BUTTON:
                        n = int(event.object.payload.get('type'))-1
                        print('кнопка № '+str(n+1))
                        if n in range(0,5):
                            last_id = vk.messages.edit(
                              peer_id=event.obj.peer_id,
                              message=mes[n],
                              conversation_message_id=event.obj.conversation_message_id,
                              keyboard=(keyboard_3 if f_toggle_6 else keyboard_6).get_keyboard())
                        elif n in range(5,10):
                            last_id = vk.messages.edit(
                              peer_id=event.obj.peer_id,
                              message=mes[n],
                              conversation_message_id=event.obj.conversation_message_id,
                              keyboard=(keyboard_4 if f_toggle_6 else keyboard_6).get_keyboard())
                        elif n in range(10,13):
                            last_id = vk.messages.edit(
                              peer_id=event.obj.peer_id,
                              message=mes[n],
                              conversation_message_id=event.obj.conversation_message_id,
                              keyboard=(keyboard_5 if f_toggle_6 else keyboard_6).get_keyboard())
                        f_toggle_6 = False #, f_toggle_5, f_toggle_4, f_toggle_3







    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК"+" "+str(now)+"\n")
        time.sleep(3)


if __name__ == '__main__':
            print()

