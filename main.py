
def word_count(text):
    return len(text.split())


def char_counts(text):
    counts = {}
    for c in text.lower():
        if c.isalpha():
            counts[c] = counts.get(c, 0) + 1
    return counts


def print_report(file_path, word_count, char_counts):    
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    char_count_list = [{"char": c, "count": count} for c, count in char_counts.items()]
    char_count_list.sort(reverse=True, key=lambda item: item['count'])
    for item in char_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    print_report(path, word_count(file_contents), char_counts(file_contents))


if __name__ == "__main__":
    main()
