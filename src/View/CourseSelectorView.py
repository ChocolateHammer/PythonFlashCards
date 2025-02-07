from tkinter.ttk import Combobox

from src.models.CourseSelectorModel import CourseSelectorModel
from tkinter import *


class CourseSelectorView:
    """This is the view to allow selection of language and course complexity"""
    FONT_NAME = "Courier"

    def __init__(self, model : CourseSelectorModel):
        self.model = model

        #define window
        self.window = Tk()
        self.window.title("Course Selector")
        self.window.config(pady=25, padx=25)


        #language selector setup
        lang_l = Label(self.window, text="What Language would you like to study today:")
        lang_l.grid(row=0, column=0, padx=8, pady=8)

        self.select_lang = StringVar()
        lang_cb = Combobox(self.window, textvariable= self.select_lang )
        lang_cb['values'] = model.languages
        lang_cb['state'] = 'readonly' #don't allow them to type unsupported or invalid options
        lang_cb.grid( row=0, column=1, padx=8, pady=8)
        self.select_lang.set( self.model.chosen_language)

        #set up the card number
        cards_l = Label(self.window, text="How many cards would you like to try:")
        cards_l.grid(row=2, column=0, padx=8, pady=8)

        self.sel_card_count= IntVar()
        count_cb = Combobox(self.window, textvariable=self.sel_card_count)
        count_cb['values'] = model.possible_card_counts()
        count_cb['state'] = 'readonly'  # don't allow them to type unsupported or invalid options
        count_cb.grid(row=2, column=1, padx=8, pady=8)
        self.sel_card_count.set(self.model.chosen_card_count)

        okay_btn = Button(text="Start Lesson", command=self.start_button_pressed)
        okay_btn.grid( row = 4, column = 0, padx=8, pady=8)

    def start_button_pressed(self):
        """applies choices to the model and closes the window"""
        self.model.set_langauge( self.select_lang.get() )
        self.model.set_card_count( self.sel_card_count.get())
        self.window.quit()
        self.window.destroy()

    def launch_form(self):
        self.window.mainloop()


