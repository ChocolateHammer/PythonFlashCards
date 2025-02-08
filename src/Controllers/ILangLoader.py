

class ILangLoader:
    """A simple 'interface' so tests can be written with a mock around the load stuff"""

    def __init__(self, lang_path: str):
        """Python doesn't really allow for interfaces but this kind of
        does the same thing.   Except for the init, which sets the lang path"""
        if not lang_path or lang_path == '' :  #if not null or empty
            raise Exception("Invalid path passed into ILangLoader")
        #could do some regular expression checking here but this is just a play project so this is sufficient
        lang_path = lang_path.strip()
        if not lang_path.endswith('/'):
            lang_path = lang_path + '/'
        self.lang_path = lang_path

    def get_language_list(self):
        """Gets a list of languages by looking for comma-delimited files at the landDir location"""
        pass

    def get_known_words(self,
                        language: str):
        """Gets the string tuples for all known words in the selected library """
        pass
