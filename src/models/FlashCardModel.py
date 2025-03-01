
class FlashCardModel:
    """Super simple class that presents the cards to the student"""
    def __init__(self, language: str, card_words):
        """Just sets the learning session view model up"""
        self.language = language
        self.card_words = card_words
        self.cards_processed = 0
        self.score = 0
        self.showing_front = True

    def done(self):
        """checks to see if the position is at the end of the list"""
        return self.cards_processed == len(self.card_words)

    def next(self):
        """moves the pointer to the next word in the list"""
        if not self.done():
            self.cards_processed += 1
        self.showing_front = True

    def front(self):
        """returns the currently active foreign language word for the front of the card"""
        return self.card_words[self.cards_processed][0].strip()

    def back(self):
        """returns the english word on the back of the card"""
        return self.card_words[self.cards_processed][1].strip()

    # I was going to derive a second model off this one to handle the other test. But I found that
    # it's actually pretty useful to just use in the simple model and the code is cleaner this woy!
    def check_answer(self, test_word: str):
        """checks to see if the entered word matches the english side of the card"""
        return_value = self.back().casefold() == test_word.strip().casefold()
        if return_value:
            self.score += 1
        self.next()
        return return_value

    def calc_percent(self):
        return float(self.score)/len(self.card_words)

    def flip_card(self):
        self.showing_front = not self.showing_front
