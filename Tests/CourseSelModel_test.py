import pytest
from Tests.MoqLangLoader import MoqLangLoader
from src.models.CourseSelectorModel import CourseSelectorModel


def test_course_sel_model_defaults_set_correctly():
    """Checks to se if the the models defaults get set up correctly"""
    moq_load = MoqLangLoader()
    model = CourseSelectorModel(moq_load)
    assert model.chosen_card_count == 10
    assert model.chosen_language == moq_load.get_language_list()[0]


@pytest.mark.parametrize("invalid_langs", ["", "Canadian"])
def test_model_throws_with_invalid_langauge(invalid_langs):
    """should raise and exception if the language is unknown"""
    moq_load = MoqLangLoader()
    model = CourseSelectorModel(moq_load)
    with pytest.raises(Exception) as exc_info:
        model.set_langauge(invalid_langs)
    assert str(exc_info.value) == "unexpected langauge encountered"


@pytest.mark.parametrize("invalid_card", [-1, 0, 500])
def test_model_throws_with_invalid_card(invalid_card):
    """Should raise an exception if the card value isn't valid."""
    moq_load = MoqLangLoader()
    model = CourseSelectorModel(moq_load)
    with pytest.raises(Exception) as exc_info:
        model.set_card_count(invalid_card)
    assert str(exc_info.value) == "unexpected card count value encountered"


def test_model_can_take_any_valid_lang():
    moq_load = MoqLangLoader()
    model = CourseSelectorModel(moq_load)
    try:
        for lang in moq_load.get_language_list():
            model.set_langauge(lang)
    except Exception as ex:
        assert False, f"no exception should have been raised. {ex}"
