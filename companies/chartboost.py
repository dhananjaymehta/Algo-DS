# Number times each word appears in a given sentence.
# For example "the fox jumps over the fox moon" would output:
import collections

def word_count(string):
    string=string.strip().split(" ")
    count={}
    for word in string:
        count[word]=count.get(word,0)+1
    print(count)

#string = "the fox jumps over the fox moon"
#word_count(string)

# Python program to del the node in which only a single pointer
# is known pointing to that node
# http://www.geeksforgeeks.org/in-a-linked-list-given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/


