from sys import modules
from tkinter import Tk, Label, messagebox
from tkinter.ttk import Button
from src.models.FlashCardModel import FlashCardModel


class FlashCardView:
    """The lesson view that displays flash cards and lets the user flip them
    [doesn't check to see if they actually know the answer]  The simple case."""

    def __init__(self, model: FlashCardModel):
        self.model = model

        # define window
        self.window = Tk()
        self.window.title(f"{model.language} lesson {len(model.card_words)} cards")
        self.window.config(pady=25, padx=25)

        # language selector setup
        lang_l = Label(self.window, text="Click the card when you think you know the answer then click the check if you got and the x if you missed it.:")
        lang_l.grid(row=0, column=0, padx=8, pady=8)

        # card button
        self.card_button = Button( self.window, command= self.card_button_pressed)
        self.update_card()
        self.card_button.grid( row=1, column=0)

        #correct button
        self.correct_button = Button(self.window, command= self.correct_button_pressed)
        self.correct_button.grid(row=2, column=0)

        #incorrect button
        self.incorrect_button = Button(self.window, command= self.incorrect_button_pressed)
        self.incorrect_button.grid(row=2, column=1)


    def update_card(self):
        """updates the card to show the front side or back side"""
        if self.model.showing_front:
            self.card_button.config( text=f"{self.model.language} : {self.model.front()}" )
        else:
            self.card_button.config(text=f"English : {self.model.back()}")

    def card_button_pressed(self):
        """handles the pressing of the flip button"""
        self.model.flip_card()
        self.update_card()

#todo :  figure out how to hook both buttons up the the same command.
    def correct_button_pressed(self):
        """"Handles the clicking of the correct button"""
        self.model.check_answer( self.model.back() )
        self.check_for_end_of_lesson()
        self.update_card()

    def incorrect_button_pressed(self):
        """"Handles the clicking of the correct button"""
        self.model.check_answer("incorrect answer")
        self.check_for_end_of_lesson()
        self.update_card()


    def check_for_end_of_lesson(self):
        """commonized logic to deal with the last button press."""
        if self.model.done():
            self.window.withdraw() #hide the main window
            messagebox.showinfo( f"The lesson is concluded you got {self.model.calc_percent()}% correct!")
            self.window.destroy()

    def launch_form(self):
        self.window.mainloop()

