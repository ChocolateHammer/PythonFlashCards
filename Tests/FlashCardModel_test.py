import pytest

from Tests.MoqLangLoader import MoqLangLoader
from src.models.FlashCardModel import FlashCardModel
from src.models.WordGetter import WordGetter


def setup(count):
    """Going to do the same setup a bunch of times so this will return a setup word getter"""
    word_getter = WordGetter(MoqLangLoader(), count, 'German')
    words = word_getter.get_lesson_words()
    return FlashCardModel('German', words)


def setup_with_given_words(words):
    return FlashCardModel('German', words)


def test_model_init():
    count = 10
    model = setup(count)
    assert model.language == "German"
    assert model.cards_processed == 0
    assert model.score == 0
    assert len(model.card_words) == count


def test_model_done():
    model = setup(2)
    assert not model.done()
    model.next()
    assert not model.done()
    model.next()
    assert model.done()


def test_next_stops_at_done():
    """checks to make sure you can't next beyond the end of the cards array"""
    model = setup(3)
    for i in range(0, 4):
        model.next()
    assert model.cards_processed == 3


def test_model_front_back():
    model = setup_with_given_words([('dir', 'the')])
    assert model.front() == 'dir'
    assert model.back() == 'the'


@pytest.mark.parametrize("words, test_word, expected_result",
    [([('die', 'the')], 'The', True),
     ([('die', 'the')], 'the', True),
     ([('die', 'the')], '', False),
     ([('die', 'the')], 'money', False)])
def test_model_check_answer(words, test_word, expected_result):
    model = setup_with_given_words(words)
    assert model.check_answer(test_word) == expected_result


def test_model_goes_to_front_after_next():
    model = setup(3)
    model.flip_card()
    assert not model.showing_front
    model.next()
    assert model.showing_front


def test_model_score():
    """This one is kind of an integration test"""
    model = setup_with_given_words([('Hier', 'Here'), ('es', 'it'), ('ist', 'is'), ('mein', 'my'), ('freude', 'friend')])
    assert model.score == 0
    model.check_answer('here')
    assert model.score == 1
    model.check_answer('it')
    assert model.score == 2
    model.check_answer("isn't")
    assert model.score == 2
    # lets simulate a skip
    model.next()
    assert model.score == 2
    model.check_answer('Friend')
    assert model.score == 3
    assert model.calc_percent() == 3.0/5.0


def test_model_flip():
    model = setup(3)
    assert model.showing_front
    model.flip_card()
    assert not model.showing_front
    model.flip_card()
    assert model.showing_front
