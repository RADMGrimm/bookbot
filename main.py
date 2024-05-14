def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_letter_count(text)
    sorted_by_use = sort_usage(num_letters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    #print(f"The letter {} was found {} times")
    for item in sorted_by_use:
        print(f"The {item["char"]} was found {item["num"]} times")
    print("---End report---")
    


def sort_on(d):
    return d["num"]

def sort_usage(num_letters):
    sorted_list = []
    for chars in num_letters:
        sorted_list.append({"char":chars, "num": num_letters[chars]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letter_count(text):
    lowering_case = text.lower()
    lower_text_sorted = sorted(lowering_case)
    letter_count = {}
    for letters in lower_text_sorted:
        if letters not in letter_count and letters.isalpha():
            letter_count[letters] = 1
        elif letters in letter_count:
            letter_count[letters] += 1
    return letter_count



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()