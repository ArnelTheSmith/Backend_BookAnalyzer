print("Here comes a text")
with open ("books/frankestein.txt") as file:
    contents = file.read()
    words = contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
