import sys

curr_word = None
curr_count = 0

for line in sys.stdin:
    words = line.strip().split(' ')

    word = words[0]
    count = int(words[1])

    if curr_word != word and curr_word != None:
        print curr_word, curr_count
        curr_count = count
        curr_word = word
    else:
        curr_count += count
        curr_word = word

print curr_word, curr_count