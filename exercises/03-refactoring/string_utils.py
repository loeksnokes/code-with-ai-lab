# string_utils.py — intentionally verbose / duplicated
def shout(s):
    if s is None:
        return ""
    s2 = s.strip()
    if len(s2) == 0:
        return ""
    return s2.upper() + "!"


def whisper(s):
    if s is None:
        return ""
    s2 = s.strip()
    if len(s2) == 0:
        return ""
    return s2.lower() + "..."
