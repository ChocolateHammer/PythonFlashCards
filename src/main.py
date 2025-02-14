from src.Controllers.LangLoader import LangLoader
from src.View.CourseSelectorView import CourseSelectorView
from src.View.FlashCardView import FlashCardView
from src.models.CourseSelectorModel import CourseSelectorModel
from src.models.FlashCardModel import FlashCardModel
from src.models.WordGetter import WordGetter

def create_course_viewmodel(loader ):
    course_model = CourseSelectorModel(loader)
    # the model will have defaults right now lets throw up a ui and let the
    # user customize the lesson
    csv = CourseSelectorView(course_model)
    csv.launch_form()
    return course_model

def create_flash_card_model(loader, course_model: CourseSelectorModel):
    getter = WordGetter(loader, course_model.chosen_card_count, course_model.chosen_language)
    cards_model = FlashCardModel(course_model.chosen_language, getter.get_lesson_words())
    return cards_model

the_loader = LangLoader(lang_path='../../LangFlashCards/data/')
the_course_model = create_course_viewmodel(the_loader)
card_model = create_flash_card_model(the_loader, the_course_model )
card_view = FlashCardView(card_model, "../images/")
card_view.launch_form()
