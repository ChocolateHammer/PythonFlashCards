from src.Controllers.LangLoader import LangLoader
from src.View.CourseSelectorView import CourseSelectorView
from src.models.CourseSelectorModel import CourseSelectorModel

loader = LangLoader(lang_path='../../LangFlashCards/data/')
csm = CourseSelectorModel(loader)
csv = CourseSelectorView(csm)
csv.launch_form()


