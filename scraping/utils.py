cyrillic_letters = {
    u'�': u'a',
    u'�': u'b',
    u'�': u'v',
    u'�': u'g',
    u'�': u'd',
    u'�': u'e',
    u'�': u'e',
    u'�': u'zh',
    u'�': u'z',
    u'�': u'i',
    u'�': u'y',
    u'�': u'k',
    u'�': u'l',
    u'�': u'm',
    u'�': u'n',
    u'�': u'o',
    u'�': u'p',
    u'�': u'r',
    u'�': u's',
    u'�': u't',
    u'�': u'u',
    u'�': u'f',
    u'�': u'h',
    u'�': u'ts',
    u'�': u'ch',
    u'�': u'sh',
    u'�': u'sch',
    u'�': u'',
    u'�': u'y',
    u'�': u'',
    u'�': u'e',
    u'�': u'yu',
    u'�': u'ya'
}


def from_cyrillic_to_eng(text: str):
    text = text.replace(' ', '_').lower()
    tmp = ''
    for ch in text:
        tmp += cyrillic_letters.get(ch, ch)
    return tmp