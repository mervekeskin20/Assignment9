# Assignment 9
# Merve Keskin

#!/usr/bin/env python3

import yaml
import os

class Sentence:
    def __init__(self, sentence_string, document, line_number): # init function defines the object self
        self.sentence_string = sentence_string 
        self.document = document
        self.line_number = line_number
        self.character_length = None 
        self.word_length = None
    
    def __repr__(self):
        # print everything 
        sentence_string_to_print = 'Sentence(arg1=' + self.sentence_string +\
                          ', arg2='        + self.document +\
                          ', arg3='        + str(self.line_number) +\
                          ', arg4='        + str(self.character_length) +\
                          ', arg5='        + str(self.word_length) +\
                          ')'
        print(sentence_string_to_print)

    def count_characters(self):
        self.character_length = len(self.sentence_string)

    def count_words(self):
        string_to_read = self.sentence_string.strip()
        self.word_length = len(string_to_read.split())
    
    def read(self):
        print(self.sentence_string)
        self.__repr__()

    def write(self, file):
        with open(file, "a") as f:
            f.write("--- ")
            yaml.dump(self, f)

def main():
    file_name = ['995.txtCleaned', '996.txtCleaned', '997.txtCleaned', '998.txtCleaned', '999.txtCleaned']
    for f_name in file_name:
        line_num = 1
        address = "cleaned_input/" + f_name
        with open(address, "r") as f:
            while True:
	            
	            line = f.readline().strip()
	            if not line.strip():
	            	break
	            s = Sentence(line, f_name, line_num)
	            s.count_characters()
	            s.count_words()
	            s.read()
	            s.write('output.yaml')
	            line_num = line_num + 1


main()    



