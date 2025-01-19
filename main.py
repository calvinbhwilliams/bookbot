def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = count_characters(text)

    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char, count in sort_on(char_counts):
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(char_counts):
    return sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

main()
