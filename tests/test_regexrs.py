import pytest
import regexrs as re


def test_simple():
    pattern = re.compile(r'(\w+) (\w+)')
    match = pattern.match('hello rust')
    assert match.groups() == ('hello', 'rust')
    assert match.pos == 0
    assert match.endpos == 10


def test_flag_i():
    pattern = re.compile(r'hello rust', re.I)
    match = pattern.match('Hello Rust')
    assert match is not None


def test_findall_compiled():
    pattern = re.compile(r'\w+')
    assert re.findall(pattern, 'hello rust') == ['hello', 'rust']


def test_findall_compiled_pattern_with_flag_errors():
    pattern = re.compile(r'\w+')
    with pytest.raises(TypeError):
        re.findall(pattern, 'hello rust', re.I)


def test_findall_string():
    pattern = r'\w+'
    assert re.findall(pattern, 'hello rust') == ['hello', 'rust']


def test_match_does_not_match():
    pattern = re.compile('foo(?P<name>bar)')
    assert pattern.match('123 foobar') is None


def test_match_at_position():
    pattern = re.compile('foo(?P<name>bar)')
    assert pattern.match('123 foobar', pos=4) is not None


def test_match_fn_does_not_match():
    assert re.match(r'foo(?P<name>bar)', '123 foobar') is None


def test_match_fn():
    assert re.match(r'foo(?P<name>bar)', 'foobar') is not None


def test_fullmatch_does_not_match():
    assert re.fullmatch(r'\w+', 'foo 123') is None


def test_fullmatch_fn():
    assert re.fullmatch(r'\w+', 'foo') is not None


def test_search_fn_finds_match():
    # search should find a match anywhere in the string
    match = re.search(r'world', 'hello world')
    assert match is not None
    assert match.group() == 'world'
    assert match.pos == 6
    assert match.endpos == 11


def test_search_fn_does_not_find_match():
    # search should return None when no match is found
    assert re.search(r'xyz', 'hello world') is None


def test_search_pattern_finds_match():
    # Pattern.search should find a match anywhere in the string
    pattern = re.compile(r'world')
    match = pattern.search('hello world')
    assert match is not None
    assert match.group() == 'world'


def test_search_pattern_with_pos():
    # Pattern.search with pos should start searching from that position
    pattern = re.compile(r'foo')
    match = pattern.search('foo bar foo', pos=4)
    assert match is not None
    assert match.pos == 8  # Second 'foo' starts at position 8


def test_search_vs_match_difference():
    # match only matches at the beginning, search finds anywhere
    pattern = re.compile(r'world')
    assert pattern.match('hello world') is None  # no match at start
    assert pattern.search('hello world') is not None  # finds match in middle


def test_search_with_groups():
    # search should work with capture groups
    match = re.search(r'(\w+) (\w+)', 'say hello world')
    assert match is not None
    assert match.group() == 'say hello'  # Matches the first two words
    assert match.groups() == ('say', 'hello')


def test_search_with_flags():
    # search should work with flags
    match = re.search(r'WORLD', 'hello world', re.I)
    assert match is not None
    assert match.group() == 'world'
