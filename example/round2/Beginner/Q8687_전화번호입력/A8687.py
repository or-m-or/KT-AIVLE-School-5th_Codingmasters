'''
Type : 
'''
import sys
import re

readline = sys.stdin.readline
write = sys.stdout.write

if __name__ == "__main__":
    phone = readline().strip()

    pattern = re.compile("010-\d{4}-\d{4}")
    if pattern.fullmatch(phone):
        write('valid')
    else:
        write('invalid')
