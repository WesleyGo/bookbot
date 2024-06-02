def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    word_count = get_character_count(text)
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n\n")
    sorted = convert_dictionary_to_dictionary_of_list(word_count)
    sorted.sort(reverse=True, key=sort_on)
    for char in sorted:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def convert_dictionary_to_dictionary_of_list(dict):
    dict_list = []
    for key in dict:
        dict_list.append({ "char": key, "num": dict[key]})
    return dict_list

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    word_count = {}
    for c in text.lower():
        if c.isalpha():
            if c not in word_count:
                word_count[c] = 1
            else:
                word_count[c] += 1
    return word_count


main()