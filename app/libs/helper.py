def is_isbn_or_key(word):
    """
    判断搜索关键字还是isbn
    :param word: 搜索变量
    :return:
    """
    # isbn 13个数字
    # isbn 10 含有‘-’
    # isbn_or_key
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    shot_word = word.replace("-", "")
    if '-' in word and len(shot_word) == 10 and shot_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
