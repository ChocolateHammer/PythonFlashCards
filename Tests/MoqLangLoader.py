from src.Controllers.ILangLoader import ILangLoader

class MoqLangLoader(ILangLoader):
    """just a simple test moq for the file IO part of the app"""
    FIRST_LINE = ('German', 'English')


    def __init__(self, _lang_dir: str = '../data/'):
        super().__init__(_lang_dir)


    def get_language_list(self) :
        """Gets a list of languages by looking for comma-delimited files at the landDir location"""
        return ['german', 'french', 'japanese']


    def get_known_words(self,
                        language: str) :
        """Gets the string tuples for all known words in the selected library """
        return [
            self.FIRST_LINE,
            ('hier', 'here'), ('die', 'the'), ('Es', 'It'), ('Ich', 'I'), ('Was', 'What'),
            ('hat', 'has'), ('auf', 'on'), ('sind', 'are'), ('einen', 'a'), ('Du', 'You'),
            ('mich', 'me'), ('in', 'in'), ('Wir', 'We'), ('dem', 'dem'), ('ihr', 'her'),
            ('an', 'to'), ('Das', 'The'), ('ein', 'a'), ('fÃ¼r', 'for'), ('dich', 'you'),
            ('zu', 'to'), ('mir', 'me'), ('wir', 'we'), ('wie', 'How'), ('mit', 'with'),
            ('so', 'so'), ('von', 'from'), ('Sie', 'She'), ('den', 'the'), ('es', 'it')]

