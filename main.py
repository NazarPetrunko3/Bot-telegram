import telebot
from telebot import types

bot = telebot.TeleBot('6657763261:AAHpM5xDYw7wOUPS16tr8QAiKuHQCp-NpWM')


@bot.message_handler(commands=['start'])
def buttons(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                       row_width=2)
    history = types.KeyboardButton(text='Історія')
    characteristic = types.KeyboardButton(text='Характеристики')

    button.add(history, characteristic)

    text = bot.send_message(message.chat.id, text='Привіт!',
                            reply_markup=button)
    bot.register_next_step_handler(text, next_func)


def next_func(message):
    if message.text == 'Історія':
        history_car(message)
    elif message.text == 'Характеристики':
        characteristics(message)


def history_car(message):
    text = bot.send_message(message.chat.id, text='Перший автомобіль, який реально використовувався,\n'
                                                  ' з бензиновим двигуном був сконструйований одночасно \n'
                                                  ' декількома незалежними німецькими винахідниками: \n'
                                                  ' Карл Бенц побудував свій перший автомобіль у 1885 в Мангаймі.')
    return text


def characteristics(message):
    text = bot.send_message(message.chat.id, text='Характеристики: \n'
                                                  'Двигун: 954см²\n'
                                                  'Кінські сили: 0.9\n'
                                                  'Коробка передач: 2х ступенева\n'
                                                  'Рік випуску: 1885')
    return text


if __name__ == '__main__':
    bot.polling(non_stop=True)
