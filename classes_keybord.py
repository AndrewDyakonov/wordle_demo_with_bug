import tkinter


class ButtonKeybord():

    def __init__(self, frame_2, ex_word):
        self.frame = frame_2

        self.ex_word = ex_word
        self.text = ''

        self.btn_1 = tkinter.Button(frame_2, text='й', height=1, width=1, padx=5, pady=2)
        self.btn_2 = tkinter.Button(frame_2, text='ц', height=1, width=1, padx=5, pady=2)
        self.btn_3 = tkinter.Button(frame_2, text='у', height=1, width=1, padx=5, pady=2)
        self.btn_4 = tkinter.Button(frame_2, text='к', height=1, width=1, padx=5, pady=2)
        self.btn_5 = tkinter.Button(frame_2, text='е', height=1, width=1, padx=5, pady=2)
        self.btn_6 = tkinter.Button(frame_2, text='н', height=1, width=1, padx=5, pady=2)
        self.btn_7 = tkinter.Button(frame_2, text='г', height=1, width=1, padx=5, pady=2)
        self.btn_8 = tkinter.Button(frame_2, text='ш', height=1, width=1, padx=5, pady=2)
        self.btn_9 = tkinter.Button(frame_2, text='щ', height=1, width=1, padx=5, pady=2)
        self.btn_10 = tkinter.Button(frame_2, text='з', height=1, width=1, padx=5, pady=2)
        self.btn_11 = tkinter.Button(frame_2, text='х', height=1, width=1, padx=5, pady=2)
        self.btn_12 = tkinter.Button(frame_2, text='ъ', height=1, width=1, padx=5, pady=2)
        self.btn_13 = tkinter.Button(frame_2, text='ф', height=1, width=1, padx=5, pady=2)
        self.btn_14 = tkinter.Button(frame_2, text='ы', height=1, width=1, padx=5, pady=2)
        self.btn_15 = tkinter.Button(frame_2, text='в', height=1, width=1, padx=5, pady=2)
        self.btn_16 = tkinter.Button(frame_2, text='а', height=1, width=1, padx=5, pady=2)
        self.btn_17 = tkinter.Button(frame_2, text='п', height=1, width=1, padx=5, pady=2)
        self.btn_18 = tkinter.Button(frame_2, text='р', height=1, width=1, padx=5, pady=2)
        self.btn_19 = tkinter.Button(frame_2, text='о', height=1, width=1, padx=5, pady=2)
        self.btn_20 = tkinter.Button(frame_2, text='л', height=1, width=1, padx=5, pady=2)
        self.btn_21 = tkinter.Button(frame_2, text='д', height=1, width=1, padx=5, pady=2)
        self.btn_22 = tkinter.Button(frame_2, text='ж', height=1, width=1, padx=5, pady=2)
        self.btn_23 = tkinter.Button(frame_2, text='э', height=1, width=1, padx=5, pady=2)
        self.btn_24 = tkinter.Button(frame_2, text='я', height=1, width=1, padx=5, pady=2)
        self.btn_25 = tkinter.Button(frame_2, text='ч', height=1, width=1, padx=5, pady=2)
        self.btn_26 = tkinter.Button(frame_2, text='с', height=1, width=1, padx=5, pady=2)
        self.btn_27 = tkinter.Button(frame_2, text='м', height=1, width=1, padx=5, pady=2)
        self.btn_28 = tkinter.Button(frame_2, text='и', height=1, width=1, padx=5, pady=2)
        self.btn_29 = tkinter.Button(frame_2, text='т', height=1, width=1, padx=5, pady=2)
        self.btn_30 = tkinter.Button(frame_2, text='ь', height=1, width=1, padx=5, pady=2)
        self.btn_31 = tkinter.Button(frame_2, text='б', height=1, width=1, padx=5, pady=2)
        self.btn_32 = tkinter.Button(frame_2, text='ю', height=1, width=1, padx=5, pady=2)

        self.draw_keyboard()
        self.__add_command_click_button()

    def draw_keyboard(self):
        self.btn_1.place(x=0, y=0)
        self.btn_2.place(x=23, y=0)
        self.btn_3.place(x=46, y=0)
        self.btn_4.place(x=69, y=0)
        self.btn_5.place(x=92, y=0)
        self.btn_6.place(x=115, y=0)
        self.btn_7.place(x=138, y=0)
        self.btn_8.place(x=161, y=0)
        self.btn_9.place(x=184, y=0)
        self.btn_10.place(x=207, y=0)
        self.btn_11.place(x=230, y=0)
        self.btn_12.place(x=253, y=0)
        self.btn_13.place(x=12, y=26)
        self.btn_14.place(x=35, y=26)
        self.btn_15.place(x=58, y=26)
        self.btn_16.place(x=81, y=26)
        self.btn_17.place(x=104, y=26)
        self.btn_18.place(x=127, y=26)
        self.btn_19.place(x=150, y=26)
        self.btn_20.place(x=173, y=26)
        self.btn_21.place(x=196, y=26)
        self.btn_22.place(x=219, y=26)
        self.btn_23.place(x=242, y=26)
        self.btn_24.place(x=35, y=52)
        self.btn_25.place(x=58, y=52)
        self.btn_26.place(x=81, y=52)
        self.btn_27.place(x=104, y=52)
        self.btn_28.place(x=127, y=52)
        self.btn_29.place(x=150, y=52)
        self.btn_30.place(x=173, y=52)
        self.btn_31.place(x=196, y=52)
        self.btn_32.place(x=219, y=52)


    def return_text_button(self, btn):
        """Возвращает текст кнопки"""
        text_button = btn.cget('text')
        self.ex_word.classes_key.config(text=text_button)



    def __add_command_click_button(self):
        """Добавить действие при нажатии кнопки"""
        self.btn_1.config(command=lambda btn=self.btn_1: self.return_text_button(btn))
        self.btn_2.config(command=lambda btn=self.btn_2: self.return_text_button(btn))
        self.btn_3.config(command=lambda btn=self.btn_3: self.return_text_button(btn))
        self.btn_4.config(command=lambda btn=self.btn_4: self.return_text_button(btn))
        self.btn_5.config(command=lambda btn=self.btn_5: self.return_text_button(btn))
        self.btn_6.config(command=lambda btn=self.btn_6: self.return_text_button(btn))
        self.btn_7.config(command=lambda btn=self.btn_7: self.return_text_button(btn))
        self.btn_8.config(command=lambda btn=self.btn_8: self.return_text_button(btn))
        self.btn_9.config(command=lambda btn=self.btn_9: self.return_text_button(btn))
        self.btn_10.config(command=lambda btn=self.btn_10: self.return_text_button(btn))
        self.btn_11.config(command=lambda btn=self.btn_11: self.return_text_button(btn))
        self.btn_12.config(command=lambda btn=self.btn_12: self.return_text_button(btn))
        self.btn_13.config(command=lambda btn=self.btn_13: self.return_text_button(btn))
        self.btn_14.config(command=lambda btn=self.btn_14: self.return_text_button(btn))
        self.btn_15.config(command=lambda btn=self.btn_15: self.return_text_button(btn))
        self.btn_16.config(command=lambda btn=self.btn_16: self.return_text_button(btn))
        self.btn_17.config(command=lambda btn=self.btn_17: self.return_text_button(btn))
        self.btn_18.config(command=lambda btn=self.btn_18: self.return_text_button(btn))
        self.btn_19.config(command=lambda btn=self.btn_19: self.return_text_button(btn))
        self.btn_20.config(command=lambda btn=self.btn_20: self.return_text_button(btn))
        self.btn_21.config(command=lambda btn=self.btn_21: self.return_text_button(btn))
        self.btn_22.config(command=lambda btn=self.btn_22: self.return_text_button(btn))
        self.btn_23.config(command=lambda btn=self.btn_23: self.return_text_button(btn))
        self.btn_24.config(command=lambda btn=self.btn_24: self.return_text_button(btn))
        self.btn_25.config(command=lambda btn=self.btn_25: self.return_text_button(btn))
        self.btn_26.config(command=lambda btn=self.btn_26: self.return_text_button(btn))
        self.btn_27.config(command=lambda btn=self.btn_27: self.return_text_button(btn))
        self.btn_28.config(command=lambda btn=self.btn_28: self.return_text_button(btn))
        self.btn_29.config(command=lambda btn=self.btn_29: self.return_text_button(btn))
        self.btn_30.config(command=lambda btn=self.btn_30: self.return_text_button(btn))
        self.btn_31.config(command=lambda btn=self.btn_31: self.return_text_button(btn))
        self.btn_32.config(command=lambda btn=self.btn_32: self.return_text_button(btn))

