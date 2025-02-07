from src.Controllers.LangLoader import LangLoader
from src.View.CourseSelectorView import CourseSelectorView
from src.models.CourseSelectorModel import CourseSelectorModel
from src.models.WordGetter import WordGetter

loader = LangLoader(lang_path='../../LangFlashCards/data/')
csm = CourseSelectorModel(loader)
csv = CourseSelectorView( csm )
csv.launch_form()
#print(csm.chosen_language + str(csm.chosen_card_count))
words = WordGetter( loader, csm.chosen_card_count, csm.chosen_language ).get_lesson_words()
print( words )

