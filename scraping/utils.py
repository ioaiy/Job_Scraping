cyrillic_letters = {
    u'à': u'a',
    u'á': u'b',
    u'â': u'v',
    u'ã': u'g',
    u'ä': u'd',
    u'å': u'e',
    u'¸': u'e',
    u'æ': u'zh',
    u'ç': u'z',
    u'è': u'i',
    u'é': u'y',
    u'ê': u'k',
    u'ë': u'l',
    u'ì': u'm',
    u'í': u'n',
    u'î': u'o',
    u'ï': u'p',
    u'ð': u'r',
    u'ñ': u's',
    u'ò': u't',
    u'ó': u'u',
    u'ô': u'f',
    u'õ': u'h',
    u'ö': u'ts',
    u'÷': u'ch',
    u'ø': u'sh',
    u'ù': u'sch',
    u'ú': u'',
    u'û': u'y',
    u'ü': u'',
    u'ý': u'e',
    u'þ': u'yu',
    u'ÿ': u'ya'
}


def from_cyrillic_to_eng(text: str):
    text = text.replace(' ', '_').lower()
    tmp = ''
    for ch in text:
        tmp += cyrillic_letters.get(ch, ch)
    return tmp