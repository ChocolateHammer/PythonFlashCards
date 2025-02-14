import pytest
from Tests.MoqLangLoader import MoqLangLoader
from src.models.WordGetter import WordGetter


def setup(number_cards):
    """Going to do the same setup a bunch of times so this will return a setup word getter"""
    moq_load = MoqLangLoader()
    return WordGetter(moq_load, number_cards, 'German')


def test_word_first_line_skipped():
    """the sub set we get the test cards from shouldn't have the first line ('german','english')"""
    number_cards = 10
    word_getter = setup(number_cards)
    words = word_getter.get_domain_words()
    assert MoqLangLoader.FIRST_LINE not in words


card_count_test_data = [
    (1, 2, 1),
    (5, 10, 5),
    (15, 30, 15),
    (16, 30, 16),  #there are only 31[included the dropped (german,english) row] so 16 is an edge case
    (40, 30, 30) ] #if there are more cards than words in the dictionary should take the whole dictionary
@pytest.mark.parametrize("card_count, expected_domain_count, expected_count",
    card_count_test_data)
def test_domain_count(card_count, expected_domain_count, expected_count):
    word_getter = setup(card_count)
    assert len(word_getter.get_domain_words()) == expected_domain_count


@pytest.mark.parametrize("card_count, expected_domain_count, expected_count",
    card_count_test_data)
def test_correct_card_count(card_count, expected_domain_count, expected_count):
    word_getter = setup(card_count)
    words = word_getter.get_lesson_words()
    assert len(words) == expected_count


@pytest.mark.parametrize("card_count, included_word, excluded_word",
    [(1, ('die', 'the'), ('Es', 'It')),
     (5, ('Du', 'You'),  ('mich', 'me'))])
def test_correct_words_in_domain(card_count, included_word, excluded_word):
    word_getter = setup(card_count)
    domain = word_getter.get_domain_words()
    assert included_word in domain
    assert excluded_word not in domain
