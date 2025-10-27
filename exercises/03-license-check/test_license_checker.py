from license_checker import has_license_header
import os

def write_tmp(content, filename="tmp_test.py"):
    with open(filename, "w", encoding="utf-8") as fh:
        fh.write(content)
    return filename

def test_detect_license():
    fname = write_tmp("# Copyright 2025 Example\nprint('hi')\n")
    assert has_license_header(fname) is True
    os.remove(fname)

def test_no_license():
    fname = write_tmp("print('no header here')\n")
    assert has_license_header(fname) is False
    os.remove(fname)
