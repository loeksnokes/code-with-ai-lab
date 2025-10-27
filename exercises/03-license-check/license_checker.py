def has_license_header(path: str) -> bool:
    """
    Return True if the file at path contains a license header snippet.
    For this exercise, a simple heuristic: check first 10 lines for "Copyright"
    or "License".
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for i, line in enumerate(fh):
                if i >= 10:
                    break
                if "copyright" in line.lower() or "license" in line.lower():
                    return True
    except FileNotFoundError:
        return False
    return False
