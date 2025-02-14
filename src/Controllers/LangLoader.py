from pathlib import Path
from src.Controllers.ILangLoader import ILangLoader
import csv


class LangLoader(ILangLoader):
    """A simple class to handle the file IO."""
    STANDARD_CVS_NAME_ENDING = "_words.csv"
    DEFAULT_LANG_PATH = '../../../LangFlashCards/data/'

    def __init__(self, lang_path: str = DEFAULT_LANG_PATH):
        super().__init__(lang_path)

    def get_language_list(self):
        """Gets a list of languages by looking for comma-delimited files
         at the landDir location.  Note: It's lazy but this is just a practice
         implementation so the files need to take a naming convention of *_words.csv"""
        dict_path = Path(self.lang_path)
        results = [file.name for
                   file in dict_path.iterdir()
                   if file.name.endswith(self.STANDARD_CVS_NAME_ENDING)]
        #truncate the standard cvs ending
        results = [l[:-len(self.STANDARD_CVS_NAME_ENDING)] for l in results]
        return results

    def get_known_words(self, language: str):
        """Gets the string tuples for all known words in the selected library """
        with open(self.generata_file_name(language), encoding="utf8") as f:
            reader = csv.reader(f)
            lst = list(tuple(line) for line in reader)
        return lst

    def generata_file_name(self, language: str):
        return self.lang_path+language+self.STANDARD_CVS_NAME_ENDING
