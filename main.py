def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_letter_count(text)
    print(f"{num_words} words found in the document")
    print(num_letters)


def get_letter_count(text):
    lowering_case = text.lower()
    lower_text_sorted = sorted(lowering_case)
    letter_count = {}
    for letters in lower_text_sorted:
        if letters not in letter_count:
            letter_count[letters] = 1
        else:
            letter_count[letters] += 1
    return letter_count



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()