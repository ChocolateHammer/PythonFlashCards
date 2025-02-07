
from src.Controllers.ILangLoader import ILangLoader


class CourseSelectorModel :
    """This class is just a simple little class that gets the
    settings for this flash card session"""

    def __init__(self, loader:ILangLoader):
        """Set up the class"""
        self.languages = loader.get_language_list()
        self.chosen_language = self.languages[0]
        self.chosen_card_count = self.possible_card_counts()[1]

    @staticmethod
    def possible_card_counts():
        return [5,10,20,30]

    def set_langauge( self, language : str ):
        if language not in self.languages :
            raise Exception("unexpected langauge encountered")
        else:
            self.chosen_language = language

    def set_card_count(self, card_count:int):
        if card_count not in self.possible_card_counts():
            raise Exception("unexpected card count value encountered")
        self.chosen_card_count = card_count

