import math
import os
import random
import re
import sys



#
# Complete the 'generateAndPrintConcordance' function below.
#
# The function accepts STRING_ARRAY inputLines as parameter.
#
import collections
import re
import string
def generateAndPrintConcordance(inputLines):
    # Write your code here
    #print(len(inputLines))
    concordance = {}
    concordance_line = {} 
    sen_number = 1
    paragraph = ""
    abbreviation = {}
    #construct sentences from input lines
    for line in inputLines:
        if paragraph:
            paragraph += " " + line
        else:
            paragraph += line
    #find the abbreviations        
    abbrev = re.findall(r'\b(?:[a-zA-Z]\.){2,}',paragraph)
    #split into sentences
    paragraph = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', paragraph)
    #print(inputLines)
    #print(abbrev)
    #print(paragraph)
    for word in abbrev:
        shortened_word = word.replace(".","")
        if shortened_word not in abbreviation:
            abbreviation[shortened_word] = word
    for sen in paragraph:
        #remove whitesplace and make lowercase
        sen = sen.strip().lower()
        #removes all puncutaion marks
        sen = sen.translate(sen.maketrans("", "", string.punctuation)) 
        individual_words = sen.split(" ")
        
        for word in individual_words:
            if word in abbreviation:
                word = abbreviation[word]
            if word in concordance:
                concordance[word] += 1
            else:
                concordance[word] = 1
            if word in concordance_line:
                concordance_line[word] += ","+str(sen_number)
            else:
                concordance_line[word] = str(sen_number)              
        sen_number += 1
            
    #ordered the dict
    ordered_con = collections.OrderedDict(sorted(concordance.items())) 
    for key, values in ordered_con.items():
        print(f"{key}: {{{values}:{concordance_line[key]}}}")    
if __name__ == '__main__':
    inputLines_count = int(input().strip())

    inputLines = []

    for _ in range(inputLines_count):
        inputLines_item = input()
        inputLines.append(inputLines_item)

    generateAndPrintConcordance(inputLines)