import pytest
from src.Controllers.LangLoader import LangLoader


def test_loader_generata_file_name():
    """kind of a dumb test but the point of this project is ot learn pytest.
    in a real project I'd probably still add it though."""
    lang_path = ".//foobar//data//"
    language = "Dutch"
    l = LangLoader(lang_path)
    filename = l.generata_file_name(language)
    assert filename == lang_path+language+l.STANDARD_CVS_NAME_ENDING


def test_loader_gets_correct_default_path():
    """make sure that the loader generates a valid default lang  path if none is passed in"""
    l = LangLoader()
    assert l.lang_path == l.DEFAULT_LANG_PATH


def test_path_gets_terminator_if_missing():
    l = LangLoader('../test')
    assert l.lang_path == '../test/'


def test_assert_thrown_on_null_or_empty_path():
    with pytest.raises(Exception) as exc_info:
        LangLoader("")
    assert str(exc_info.value) == 'Invalid path passed into ILangLoader'
