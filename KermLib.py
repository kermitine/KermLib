# personal library that features word/sentence processing, and more


alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]



class KermLib():
    def __init__(self, version):
        self.version = version

    def text_extraction(self, complex_string): # removes special characters and converts sentence to simple text
        complex_string_list = complex_string.split()
        for word in complex_string_list:
            word_list = [char for char in word if char in alphabet]



KermLib = KermLib('2024.11.28.1835.alpha')

print(KermLib.text_extraction('-what() |does| /the\ @fox? !say!'))