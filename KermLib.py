# personal library that features word/sentence processing, and more


alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]



class KermLib():
    def __init__(self, version):
        self.version = version

    def text_extraction(self, complex_string):  # removes special characters and converts sentence to simple lowercase text
        new_string_list = []
        new_string_list_words_joined = []
        complex_string = complex_string.lower()
        complex_string_list = complex_string.split()
        for word in complex_string_list:    # creates a list of sub-lists, each sub-list contains each char for each word
            new_string = [char for char in word if char in alphabet]
            new_string_list.append(new_string)
        for sub_list in new_string_list:    # joins each sub-list
            joined_sub_list = ''.join(sub_list)
            new_string_list_words_joined.append(joined_sub_list)
        simplified_string = ' '.join(new_string_list_words_joined)  # joins each list back into a string
        return simplified_string


KermLib = KermLib('2024.11.28.1915.alpha')

print(KermLib.version)