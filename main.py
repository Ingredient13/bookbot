def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict_text = count_chars(text)
    format_text_print(dict_text, count_words(text), book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c not in char_count and (c.isalpha() == True):
            char_count[c] = 1
        elif c in char_count and (c.isalpha() == True):
            char_count[c] += 1
    return char_count

def format_text_print(text, word_count, book):
    text_list = []
    for c in text:
        c_dict = {"name": c, "num":text[c]}
        text_list.append(c_dict)

    print(f"--- Begin report of {book} ---")
    
    def sort_on(dict):
        return dict["num"]

    text_list.sort(reverse=True, key=sort_on)

    print(f"{word_count} words found in the document")
    for i in text_list:
        print (f" The '{i['name']}' character was found {i['num']} times")

    print("--- End report ---")

main()