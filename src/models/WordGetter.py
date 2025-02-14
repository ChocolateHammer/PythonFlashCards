from src.Controllers.ILangLoader import ILangLoader
import random


class WordGetter:
    """This class gathers the words to be used with this learning session
    Note: probably should just be a function rather than a class, but it's a
    play project, so I'm leaving it this way in case I want to come back later
    and complicate it in some significant ways."""

    def __init__(self,
                 loader: ILangLoader,
                 card_count: int,
                 lang: str):
        self.card_count = card_count
        self.language = lang
        self.loader = loader

    def get_domain_words(self):
        """uses the loader to get all the words in the dictionary
        then gets a 2x card count subset of them for the test
        excluding the first row which is just (language, 'english')"""
        all_words = self.loader.get_known_words(self.language)
        end_index = min( len(all_words), (self.card_count*2)+1 )
        return all_words[1:end_index]

    def get_lesson_words(self):
        """uses the loader to get all the words in the dictionary then gets a subset of them for the test"""
        sub_list = self.get_domain_words()
        random.shuffle(sub_list)
        return sub_list[:self.card_count]
