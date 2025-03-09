def get_num_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def get_num_letters(file_contents):
    letter_dict = {


    }
    lowercase = file_contents.lower()
    for val in lowercase:
        if val.isalpha():
            if val not in letter_dict:
                letter_dict[val] = 1
            else:
                letter_dict[val] += 1
    return letter_dict

def sort_on(letter_dict):
    return letter_dict["count"]

def sorted_dict(letters):
    #converts the letters dictionary to a list of dictionaries
    letter_list =  [{"character": char, "count": count} for char, count in letters.items()]

    # Sort the list of dictionaries
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list