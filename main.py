def main():
    file_contents = get_file_contents("books/frankenstein.txt")

    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for c in sorted_char_count(char_count):
        print(f"The '{c["name"]}' character was found {c["num"]} times")
    print ("--- End report ---")

    
def sort_on(dict):
    return dict["num"]

def sorted_char_count(raw_dict):
    list_of_dict = [{"name": k, "num": v} for k, v in raw_dict.items() if k.isalpha()]
    list_of_dict.sort(reverse = True, key = sort_on)
    return list_of_dict

def get_file_contents(path):
    with open ("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(input):
    return len(input.split())

def get_char_count(input):
    char_dict = {}
    for i in input.lower():
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict


main()