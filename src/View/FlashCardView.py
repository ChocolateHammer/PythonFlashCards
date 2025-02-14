from tkinter import Tk, Label, messagebox, PhotoImage
from tkinter.ttk import Button
from src.models.FlashCardModel import FlashCardModel

class FlashCardView:
    """The lesson view that displays flash cards and lets the user flip them
    [doesn't check to see if they actually know the answer]  The simple case."""
    CORRECT_BUTTON = 1
    INCORRECT_BUTTON = 2
    BACKGROUND_COLOR = "#B1DDC6"

    def __init__(self, model: FlashCardModel, image_path):
        self.model = model

        # define window
        self.root = Tk()
        self.root.title(f"{model.language} lesson {len(model.card_words)} cards")
        self.root.resizable(False, False)
        self.root.config(pady=25, padx=25, background=self.BACKGROUND_COLOR)

        # language selector setup
        lang_l = Label(self.root,  background=self.BACKGROUND_COLOR, font=("Arial", 18),
                       text="Click the card when you think you know the answer."+
                            "\nThen click the check if you got and the x if you missed it.")
        lang_l.pack(pady=0)

# TODO: the render of the card is lacking will probably need to construct a canvas to make it work.
        # card button
        self.front_image = PhotoImage(file=image_path + "card_front.png")
        self.back_image = PhotoImage(file=image_path + "card_back.png")
        self.card_button = Button(self.root, image=self.front_image,
                                  compound="center",
                                  command= self.card_button_pressed)
        self.card_button.config()
        self.card_button.pack()
        self.update_card()
        # correct button
        self.correct_glyph = PhotoImage(file=image_path+"right.png")
        self.correct_button = Button(self.root, image=self.correct_glyph,
                                     command=lambda:self.button_pressed(self.CORRECT_BUTTON))
        self.correct_button.pack(side='left')
        # incorrect button
        self.incorrect_glyph = PhotoImage(file=image_path+"wrong.png")
        self.incorrect_button = Button(self.root, image=self.incorrect_glyph,
                                       command=lambda:self.button_pressed(self.INCORRECT_BUTTON))
        self.incorrect_button.pack(side='right')

    def update_card(self):
        """updates the card to show the front side or back side"""
        if self.model.showing_front:
            self.card_button.config(image=self.front_image, text=f"{self.model.language} : {self.model.front()}")
        else:
            self.card_button.config(image=self.back_image, text=f"English : {self.model.back()}")

    def card_button_pressed(self):
        """handles the pressing of the flip button"""
        self.model.flip_card()
        self.update_card()

    def button_pressed(self, button_id):
        """"Handles the clicking of the correct button"""
        if button_id == self.CORRECT_BUTTON:
            self.model.check_answer(self.model.back())
        else:
            self.model.check_answer("incorrect answer")
        if self.model.done():
            self.handle_end_of_lesson()
        else:
            self.update_card()

    def handle_end_of_lesson(self):
        """handles the end of lesson stuff"""
        self.root.withdraw()  # hide the main window
        messagebox.showinfo(title="Lesson Complete.",
                            message=f"The lesson is concluded you got {self.model.calc_percent()*100}% correct!")
        self.root.destroy()

    def launch_form(self):
        self.root.mainloop()
