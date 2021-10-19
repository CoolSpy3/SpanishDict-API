import spanishdictapi.conjugations
from html.parser import HTMLParser
import json
import re
import urllib.parse
import urllib.request

__cacheEnabled = True
__cache = {}

class __JsonFinder(HTMLParser):
    def __init__(self, jsonArr):
        HTMLParser.__init__(self)
        self.__jsonArr = jsonArr

    def handle_data(self, data):
        data = re.sub('[\n ]', '', data)
        if data.startswith('window.SD_COMPONENT_DATA={'):
            self.__jsonArr.append(data[25:-1])

def get_json_for_word(word: str) -> str:
    if __cacheEnabled and word in __cache:
        return __cache[word]
    with urllib.request.urlopen(f'https://spanishdict.com/conjugate/{urllib.parse.quote(word)}') as htmlfp:
        js = []
        __JsonFinder(js).feed(htmlfp.read().decode('utf-8'))
        if __cacheEnabled:
            __cache[word] = js[0]
        return js[0]

def set_cache_enabled(enabled: bool) -> None:
    __cacheEnabled = enabled
    if not enabled:
        __cache.clear()

def __get_json_path(js, *path):
    for pathElement in path:
        if isinstance(pathElement, str):
            pathParts = pathElement.split('/')
            for part in pathParts:
                js = js[part]
        else:
            js = js[pathElement]
    return js

def translate_word(word: str) -> str:
    js = json.loads(get_json_for_word(word))
    return __get_json_path(js, 'resultCardHeaderProps/headwordAndQuickdefsProps/quickdef1/displayText')

def conjugate_word(word: str) -> str:
    js = json.loads(get_json_for_word(word))
    if 'verb' not in js:
        return None
    js = js['verb']
    conjs = {}
    conjs[conjugations.INFINITIVE] = js['infinitive']
    conjs[conjugations.PAST_PARTICIPLE] = __get_json_path(js, 'pastParticiple/word')
    conjs[conjugations.PRESENT_PARTICIPLE] = __get_json_path(js, 'gerund/word')
    js = js['paradigms']
    for mode in conjugations.VALID_CONJUGATIONS:
        for tense in conjugations.VALID_CONJUGATIONS[mode]:
            for subject in conjugations.SUBJECTS:
                if mode not in conjs:
                    conjs[mode] = {}
                if tense not in conjs[mode]:
                    conjs[mode][tense] = {}
                conjs[mode][tense][subject] = __get_json_path(js, conjugations.get_json_path_for_conjugation(mode, tense), conjugations.get_position_for_subject(subject), 'word')
    return conjs
