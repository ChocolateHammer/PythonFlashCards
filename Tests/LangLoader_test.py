import pytest
from src.Controllers.LangLoader import LangLoader


def test_loader_generata_file_name():
    """kind of a dumb test but the point of this project is ot learn pytest.
    in a real project I'd probably still add it though."""
    lang_path = ".//foobar//data//"
    language = "Dutch"
    lloader = LangLoader(lang_path)
    filename = lloader.generata_file_name(language)

    assert filename == lang_path+language+lloader.STANDARD_CVS_NAME_ENDING


def test_loader_gets_correct_default_path():
    """make sure that the loader generates a valid default lang  path if none is passed in"""
    lloader = LangLoader()
    assert lloader.lang_path == lloader.DEFAULT_LANG_PATH


def test_path_gets_terminator_if_missing():
    loader = LangLoader('../test')
    assert loader.lang_path == '../test/'


def test_assert_thrown_on_null_or_empty_path():
    with pytest.raises(Exception) as exc_info:
        LangLoader("")
    assert str(exc_info.value) == 'Invalid path passed into ILangLoader'
