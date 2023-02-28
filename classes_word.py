import tkinter

import classes_keybord
import utils


class ButtonWord:
    def __init__(self, frame_1, frame_2, list_box):
        self.frame = frame_1
        self.frame_2 = frame_2
        self.classes_key = None                                                 # какая кнопка нажата
        self.list_box = list_box
        self.word = []                                                          # получившееся слово
        self.slovar = []                                                        # весь словарь

        self.btn_1 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_2 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_3 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_4 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_5 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_6 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_7 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_8 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_9 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_10 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_11 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_12 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_13 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_14 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_15 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_16 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_17 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_18 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_19 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_20 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_21 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_22 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_23 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_24 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_25 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_26 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_27 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_28 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_29 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)
        self.btn_30 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4)

        # кнопка выбора цвета
        self.btn_31 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4, bg='yellow')
        self.btn_32 = tkinter.Button(frame_1, height=1, width=1, padx=10, pady=4, bg='green')

        # Кнопка загрузки слов
        self.btn_33 = tkinter.Button(frame_1, height=1, width=5, padx=10, pady=4, text='load')

        # Кнопка проверки слов
        self.btn_34 = tkinter.Button(frame_1, height=1, width=5, padx=10, pady=4, text='Check')

        self.__draw_field()
        self.__add_command_button()

    def __draw_field(self):
        """отрисовать поле для ввода"""
        self.btn_1.place(x=5, y=5)
        self.btn_2.place(x=40, y=5)
        self.btn_3.place(x=75, y=5)
        self.btn_4.place(x=110, y=5)
        self.btn_5.place(x=145, y=5)
        self.btn_6.place(x=5, y=37)
        self.btn_7.place(x=40, y=37)
        self.btn_8.place(x=75, y=37)
        self.btn_9.place(x=110, y=37)
        self.btn_10.place(x=145, y=37)
        self.btn_11.place(x=5, y=69)
        self.btn_12.place(x=40, y=69)
        self.btn_13.place(x=75, y=69)
        self.btn_14.place(x=110, y=69)
        self.btn_15.place(x=145, y=69)
        self.btn_16.place(x=5, y=101)
        self.btn_17.place(x=40, y=101)
        self.btn_18.place(x=75, y=101)
        self.btn_19.place(x=110, y=101)
        self.btn_20.place(x=145, y=101)
        self.btn_21.place(x=5, y=134)
        self.btn_22.place(x=40, y=134)
        self.btn_23.place(x=75, y=134)
        self.btn_24.place(x=110, y=134)
        self.btn_25.place(x=145, y=134)
        self.btn_26.place(x=5, y=167)
        self.btn_27.place(x=40, y=167)
        self.btn_28.place(x=75, y=167)
        self.btn_29.place(x=110, y=167)
        self.btn_30.place(x=145, y=167)
        self.btn_31.place(x=5, y=200)
        self.btn_32.place(x=40, y=200)
        self.btn_33.place(x=75, y=200)
        self.btn_34.place(x=200, y=200)

    def __add_command_button(self):
        """Назначить действие кнопке"""
        self.btn_1.config(command=lambda btn=self.btn_1: self.__choise_field(btn))
        self.btn_2.config(command=lambda btn=self.btn_2: self.__choise_field(btn))
        self.btn_3.config(command=lambda btn=self.btn_3: self.__choise_field(btn))
        self.btn_4.config(command=lambda btn=self.btn_4: self.__choise_field(btn))
        self.btn_5.config(command=lambda btn=self.btn_5: self.__choise_field(btn))
        self.btn_6.config(command=lambda btn=self.btn_6: self.__choise_field(btn))
        self.btn_7.config(command=lambda btn=self.btn_7: self.__choise_field(btn))
        self.btn_8.config(command=lambda btn=self.btn_8: self.__choise_field(btn))
        self.btn_9.config(command=lambda btn=self.btn_9: self.__choise_field(btn))
        self.btn_10.config(command=lambda btn=self.btn_10: self.__choise_field(btn))
        self.btn_11.config(command=lambda btn=self.btn_11: self.__choise_field(btn))
        self.btn_12.config(command=lambda btn=self.btn_12: self.__choise_field(btn))
        self.btn_13.config(command=lambda btn=self.btn_13: self.__choise_field(btn))
        self.btn_14.config(command=lambda btn=self.btn_14: self.__choise_field(btn))
        self.btn_15.config(command=lambda btn=self.btn_15: self.__choise_field(btn))
        self.btn_16.config(command=lambda btn=self.btn_16: self.__choise_field(btn))
        self.btn_17.config(command=lambda btn=self.btn_17: self.__choise_field(btn))
        self.btn_18.config(command=lambda btn=self.btn_18: self.__choise_field(btn))
        self.btn_19.config(command=lambda btn=self.btn_19: self.__choise_field(btn))
        self.btn_20.config(command=lambda btn=self.btn_20: self.__choise_field(btn))
        self.btn_21.config(command=lambda btn=self.btn_21: self.__choise_field(btn))
        self.btn_22.config(command=lambda btn=self.btn_22: self.__choise_field(btn))
        self.btn_23.config(command=lambda btn=self.btn_23: self.__choise_field(btn))
        self.btn_24.config(command=lambda btn=self.btn_24: self.__choise_field(btn))
        self.btn_25.config(command=lambda btn=self.btn_25: self.__choise_field(btn))
        self.btn_26.config(command=lambda btn=self.btn_26: self.__choise_field(btn))
        self.btn_27.config(command=lambda btn=self.btn_27: self.__choise_field(btn))
        self.btn_28.config(command=lambda btn=self.btn_28: self.__choise_field(btn))
        self.btn_29.config(command=lambda btn=self.btn_29: self.__choise_field(btn))
        self.btn_30.config(command=lambda btn=self.btn_30: self.__choise_field(btn))
        self.btn_31.config(command=lambda btn=self.btn_31: self.__change_color(btn))
        self.btn_32.config(command=lambda btn=self.btn_32: self.__change_color(btn))
 #       self.btn_33.config(command=lambda btn=self.btn_33: self.check_letter_in_slovar())
        self.btn_34.config(command=lambda btn=self.btn_34: self.__create_chech_word())

    def __choise_field(self, btn):
        """выбор поля для ввода"""
        self.classes_key = btn

    def __change_color(self, btn):
        """сменить цвет кнопки"""
        text_button = btn.cget('bg')
        self.classes_key.config(bg=text_button)

    def load_word(self):
        """Загрузить слова"""
        a = utils.get_text()
        self.slovar = a

    def __create_chech_word(self):
        """Составить слово из ячеек"""
        self.word = []
        self.list_box.delete(1.0, 'end')
        self.word.append(self.btn_1.cget('text'))
        self.word.append(self.btn_2.cget('text'))
        self.word.append(self.btn_3.cget('text'))
        self.word.append(self.btn_4.cget('text'))
        self.word.append(self.btn_5.cget('text'))
        self.__check_letter_in_slovar()

    def __check_letter_in_slovar(self):
        """Поиск слов в словаре"""
        self.load_word()
        slovar_green = ['', '', '', '', '']
        slovar_yellow = ['', '', '', '', '']
        set_list = []
        first = []
        second = []
        true = []
        four = []
        five = []

        if self.btn_1.cget('bg') == 'green':
            slovar_green[0] = (self.btn_1.cget('text'))
        elif self.btn_1.cget('bg') == 'yellow':
            slovar_yellow[0] = (self.btn_1.cget('text'))

        if self.btn_2.cget('bg') == 'green':
            slovar_green[1] = (self.btn_2.cget('text'))
        elif self.btn_2.cget('bg') == 'yellow':
            slovar_yellow[1] = (self.btn_2.cget('text'))

        if self.btn_3.cget('bg') == 'green':
            slovar_green[2] = (self.btn_3.cget('text'))
        elif self.btn_3.cget('bg') == 'yellow':
            slovar_yellow[2] = (self.btn_3.cget('text'))

        if self.btn_4.cget('bg') == 'green':
            slovar_green[3] = (self.btn_4.cget('text'))
        elif self.btn_4.cget('bg') == 'yellow':
            slovar_yellow[3] = (self.btn_4.cget('text'))

        if self.btn_5.cget('bg') == 'green':
            slovar_green[4] = (self.btn_5.cget('text'))
        elif self.btn_5.cget('bg') == 'yellow':
            slovar_yellow[4] = (self.btn_5.cget('text'))

        for i in self.slovar:
            if slovar_green[0] != '' and slovar_green[0] == i[0]:
                first.append(i)
            if slovar_green[1] != '' and slovar_green[1] == i[1]:
                second.append(i)
            if slovar_green[2] != '' and slovar_green[2] == i[2]:
                true.append(i)
            if slovar_green[3] != '' and slovar_green[3] == i[3]:
                four.append(i)
            if slovar_green[4] != '' and slovar_green[4] == i[4]:
                five.append(i)

        set_first = set(first)
        set_second = set(second)
        set_true = set(true)
        set_four = set(four)
        set_five = set(five)

        count = 0

        if len(set_first) > 0:
            set_list.append(set_first)
            count += 1
        if len(set_second) > 0:
            set_list.append(set_second)
            count += 1
        if len(set_true) > 0:
            set_list.append(set_true)
            count += 1
        if len(set_four) > 0:
            set_list.append(set_four)
            count += 1
        if len(set_five) > 0:
            set_list.append(set_five)
            count += 1

        if count == 1:
            result_list = set_first.union(*set_list)
            for i in result_list:
                self.list_box.insert(1.0, i)

        if count > 1:
            result_list = set_first.union(*set_list)
            result = result_list.intersection(*set_list)
            for i in result:
                self.list_box.insert(1.0, i)
