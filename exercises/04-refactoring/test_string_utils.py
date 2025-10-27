from string_utils import shout, whisper

def test_shout():
    assert shout(" hi ") == "HI!"
    assert shout("") == ""
    assert shout(None) == ""

def test_whisper():
    assert whisper("Yo") == "yo..."
    assert whisper("  ") == ""
    assert whisper(None) == ""
