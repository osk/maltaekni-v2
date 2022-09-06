"""Some methods for stat analysis of text
"""

from reynir import Greynir
import spacy

nlp = spacy.load("en_core_web_sm")

# From Greynir Tokenizer
# https://github.com/mideind/Tokenizer#the-kind-property
WORD = 6
WORD_GROUP_NOUNS = ['hk', 'kvk', 'kk']

# very naïve
LOCALES = ['is', 'en']

TRANS_DICT = {
    '-': '',
    '–': ' ',
    '—': ' ',
    '!': '',
    '"': '',
    '#': '',
    '$': '',
    '&': '',
    '(': '',
    ')': '',
    '*': '',
    '+': '',
    ',': '',
    '.': '',
    '/': '',
    ':': '',
    ';': '',
    '’': '\'',
    '“': '',
    '”': '',
    # etc for """;<=>?@[\]^_`{|}~"""
}

CONSONANTS = {'is': 'bdðfghjklmnprstvxþ','en': 'bdfghjklmnprstvx'}

def split_str(input_str: str):
    """Split a string just the way we like it"""
    transtable = str.maketrans(TRANS_DICT)

    str_without_punctuation = input_str.translate(transtable)
    return str_without_punctuation.split()

def order_list_of_words_by_occurrence(input_list):
    """
    Order list of words by occurrence
    TODO super slow
    """

    all_words = []
    for word in input_list:
        found = False
        for _, item in enumerate(all_words):
            if item['word'] == word:
                item['count'] = item['count'] + 1
                found = True
        if not found:
            all_words.append({ 'word': word, 'count': 1 })
    all_words_sorted = sorted(all_words, key=lambda d: d['count'], reverse=True)

    return all_words_sorted

def count_words(input_str: str):
    """Count words in input_str"""
    return len(split_str(input_str))

def count_word_forms(input_str_list: list):
    """Count different word forms in input_str"""
    count = 0
    seen = set()
    for word in input_str_list:
        word = word.lower()
        if word not in seen:
            count = count + 1
        seen.add(word)
    return count

def order_words_by_occurrence(input_str: str):
    """Order words in input_str by occurrence, returns list of dicts"""

    # Should this use tuples instead of dicts?
    split = split_str(input_str)
    return order_list_of_words_by_occurrence(split)

def unique_word_ratio(input_str_list: list):
    """Return ratio of each unique word in input_str"""
    all_words_sorted = order_list_of_words_by_occurrence(input_str_list)
    total_words = len(input_str_list)

    for word in all_words_sorted:
        word['ratio'] = word['count'] / total_words

    return all_words_sorted

def unique_words_ratio(input_str_list: list):
    """Return the ratio of unique words to total words in input_str_list"""
    return count_word_forms(input_str_list) / len(input_str_list)

def word_length_ratio(input_str_list: str, min_length: int):
    """Return the ratio of words in input_str_list that are longer than min_length"""
    if min_length <= 0:
        return 0

    count = len([item for item in input_str_list if len(item) > min_length])

    return count / len(input_str_list)

def is_sorted_nouns(input_str: str):
    """Return icelandic nouns in input_str sorted by occurrence"""
    greynir = Greynir()
    tokens = greynir.tokenize(input_str)
    nouns = []
    for token in tokens:
        if token.kind == WORD:
            try:
                ordfl = token.val[0].ordfl
                if ordfl in WORD_GROUP_NOUNS:
                    nouns.append(token.txt)
            except: # pylint: disable=bare-except
                pass
    return order_list_of_words_by_occurrence(nouns)

def en_sorted_nouns(input_str: str):
    """Return english nouns in input_str sorted by occurrence"""
    tokens = nlp(input_str)
    print(len(tokens))
    nouns = []
    for token in tokens:
        if token.tag_ == 'NN':
            nouns.append(token.text)
    return order_list_of_words_by_occurrence(nouns)

def sorted_nouns(input_str: str, locale: str):
    """Find all nouns in input_str sorted by occurrence"""

    if locale == 'is':
        return is_sorted_nouns(input_str)
    if locale == 'en':
        return en_sorted_nouns(input_str)
    return []

def longest_consonant_cluster(input_str_list: list, locale: str):
    """
    Return the longest consonant cluster in input_str in given locale
    TODO should raise if illegal locale
    TODO this is too messy, refactor
    """

    consonants = CONSONANTS[locale]
    longest = 0
    longest_words = []
    for word in input_str_list:
        longest_cluster_in_word = 0
        current_cluster = 0

        for letter in list(word):
            if letter in consonants:
                current_cluster = current_cluster + 1
            else:
                if current_cluster > longest_cluster_in_word:
                    longest_cluster_in_word = current_cluster
                current_cluster = 0

        if longest_cluster_in_word >= longest:
            if longest_cluster_in_word > longest:
                longest_words = []
                longest = longest_cluster_in_word
            seen = next((item for item in longest_words if item['word'] == word), None)
            if not seen:
                longest_words.append(
                  { 'word': word, 'length': longest_cluster_in_word }
                )
    return longest_words

with open("./data/stopwords/is.txt", "rb") as input_file:
    is_stop_words = input_file.read().decode('utf8').split()

with open("./data/stopwords/en.txt", "rb") as input_file:
    en_stop_words = input_file.read().decode('utf8').split()

def is_remove_stop_words(input_str: str):
    """Remove icelandic stop words"""
    split = split_str(input_str)
    return [word for word in split if word.lower() not in is_stop_words]

def en_remove_stop_words(input_str: str):
    """Remove english stop words"""
    split = split_str(input_str)
    return [word for word in split if word.lower() not in en_stop_words]

def remove_stop_words(input_str: str, locale: str):
    """Remove stop words if we know how and return list of words"""
    if locale == 'is':
        return is_remove_stop_words(input_str)
    if locale == 'en':
        return en_remove_stop_words(input_str)
    return split_str(input_str)
