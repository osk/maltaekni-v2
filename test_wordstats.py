# pylint: disable=missing-class-docstring, missing-function-docstring

""" Tests for wordstats
"""
import unittest

from wordstats import (
    split_str,
    count_words,
    count_word_forms,
    order_words_by_occurrence,
    unique_word_ratio,
    word_length_ratio,
    longest_consonant_cluster,
    sorted_nouns,
    remove_stop_words
)

class TestCountWords(unittest.TestCase):
    def test_count_words_basic(self):
        self.assertEqual(count_words("foo bar foo"), 3, "Should count words with spaces")
    def test_count_words_newline(self):
        self.assertEqual(count_words("""foo
        bar
        foo"""), 3, "Should count words with newlines and spaces")
    def test_count_words_punctuation(self):
        self.assertEqual(count_words("foo—bar–foo)"), 3, "Should count with en and em dashes")

class TestCountWordForms(unittest.TestCase):
    def test_count_word_forms(self):
        self.assertEqual(
            count_word_forms(split_str("Api sá APA vera að apa eftir öðrum apa")),
            7,
            "Should count word forms"
        )

class TestOrderWordsByoccurrence(unittest.TestCase):
    def test_order_words_by_occurrence(self):
        self.assertEqual(
            order_words_by_occurrence("baz foo bar foo bar foo"),
            [{'word': 'foo', 'count': 3}, {'word': 'bar', 'count': 2}, {'word': 'baz', 'count': 1}],
            "Should order words by occurrence"
        )

class TestUniqueWordRatio(unittest.TestCase):
    def test_unique_word_ratio(self):
        self.assertEqual(
            unique_word_ratio(split_str("baz foo bar foo bar foo")),
            [
                {'word': 'foo', 'count': 3, 'ratio': 3/6},
                {'word': 'bar', 'count': 2, 'ratio': 1/3},
                {'word': 'baz', 'count': 1, 'ratio': 1/6}
            ],
            "Should return unique word ratio"
        )

class TestWordLengthRatio(unittest.TestCase):
    def test_word_length_ratio(self):
        self.assertEqual(
            word_length_ratio(split_str("foobarbaz foo bar foo bar foofoofoo"), 8),
            1/3,
            "Should return the ratio of words longer than 8"
        )
    def test_word_length_ratio_none(self):
        self.assertEqual(
            word_length_ratio("foo", 9),
            0,
            "Should return the ratio of words if no matches"
        )
    def test_word_length_ratio_negative(self):
        self.assertEqual(
            word_length_ratio("foo", -1),
            0,
            "Should return the ratio of words if min_length is negative"
        )

class TestSortedNouns(unittest.TestCase):
    def test_sorted_nouns_is(self):
        self.assertEqual(
            sorted_nouns("ferskvatn ferskvatn kona sá maður bíll", "is"),
            [
                {'word': 'ferskvatn', 'count': 2},
                {'word': 'kona', 'count': 1},
                {'word': 'maður', 'count': 1},
                {'word': 'bíll', 'count': 1},
            ],
            "Should identify icelandic nouns"
        )
    def test_sorted_nouns_en(self):
        self.assertEqual(
            sorted_nouns("water woman saw big car car", "en"),
            [
                {'word': 'car', 'count': 2},
                {'word': 'water', 'count': 1},
                {'word': 'woman', 'count': 1},
            ],
            "Should identify english nouns"
        )

class TestLongestConsonantCluster(unittest.TestCase):
    def test_longest_consonant_cluster(self):
        self.assertEqual(
            longest_consonant_cluster(split_str("ég drekk ferskvatn"), "is"),
            [{'word': 'ferskvatn', 'length': 4}],
            "Should find word with longest cluster"
        )

    def test_longest_consonant_cluster_two(self):
        self.assertEqual(
            longest_consonant_cluster(split_str("Ég drekk ferskvatn ffffoo"), "is"),
            [
                {'word': 'ferskvatn', 'length': 4},
                {'word': 'ffffoo', 'length': 4}
            ],
            "Should find two words with longest cluster"
        )

    def test_longest_consonant_cluster_dupe(self):
        self.assertEqual(
            longest_consonant_cluster(split_str("Ég drekk ferskvatn ferskvatn"), "is"),
            [
                {'word': 'ferskvatn', 'length': 4}
            ],
            "Should find single word with longest cluster if twice"
        )

class TestRemoveStopWords(unittest.TestCase):
    def test_remove_stop_words_is(self):
        self.assertEqual(
            remove_stop_words('vatn EÐA ferskja hver sér mun', 'is'),
            ['vatn', 'ferskja', 'mun'],
            "Should remove icelandic stop words"
        )

    def test_remove_stop_words_en(self):
        self.assertEqual(
            remove_stop_words('Don’t keep coughing so', 'en'),
            ['keep', 'coughing'],
            "Should remove english stop words"
        )
