from telebot import types

class Subjects():
    def __init__(self, bot):
        self.bot = bot
        self.subjectUserList = []
        self.removesubjectUserList = []
        self.c_callbackPrefixRemovesubject = 'removesubject_'

        self.subjList = ["предмет 1", "предмет 2", "предмет 3"]

    def subjectCommand(self, message):
        self.bot.send_message(message.chat.id, 'Введите название нового предмета')
        self.subjectUserList.append(message.from_user.id)

    def removesubjectCommand(self, message):
        buttons = []
        for subject in self.subjList:
            buttons.append(
                [types.InlineKeyboardButton(subject, callback_data=self.c_callbackPrefixRemovesubject + subject)])
        markup = types.InlineKeyboardMarkup(buttons)
        self.bot.send_message(message.chat.id, 'Удалить предмет', reply_markup=markup)
        self.removesubjectUserList.append(message.from_user.id)

    def subjectTextHandler(self, message):
        if message.from_user.id in self.subjectUserList:
            self.bot.send_message(message.chat.id, 'Предмет ' + message.text + ' добавлен')
            self.subjList.append(message.text)
            self.subjectUserList.remove(message.from_user.id)

    def removesubjectCallback(self, callback):
        subject = callback.data.removeprefix(self.c_callbackPrefixRemovesubject)
        self.bot.send_message(callback.message.chat.id, 'Предмет ' + subject + ' удален')
        self.subjList.remove(subject)
        self.removesubjectUserList.remove(callback.from_user.id)

    def getSubj(self):
        return self.subjList
