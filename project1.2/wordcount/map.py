import sys

for line in sys.stdin:
    words = line.strip().split(' ')
    for word in words:
        string = word + ' 1'
        print string