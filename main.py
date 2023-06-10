def main():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_enum(text)
    char_list = chars_dict_to_sorted_list(char_dict)

    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_book_text(path):
    with open (path) as f:
        return f.read()

def get_num_words(text):
     words = text.split()
     return len(words)
def get_char_enum(text):
    chars = {}
    text = text.lower()
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
def chars_dict_to_sorted_list(char_dict):
    sorted_list =  []
    char_analysis= ""
    for c in char_dict:
        sorted_list.append({"char": c, "num": char_dict[c]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list
def sort_on(d):
    return d["num"]

main()



