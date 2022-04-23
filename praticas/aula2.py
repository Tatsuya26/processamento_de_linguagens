import re
'''
l = "Hello 123 world 3123 123"
ls = re.sub(r'\d+','NUM',l)
print(ls)
'''


def swapconcat_names(filename):  
    f = open(filename, 'r')
    for line in f:
        sub_line = re.sub(r'(\w)\w* +(\w+)', r'\2, \1.', line.strip())
        print(sub_line)
    f.close()


def swap_names(filename):  
    f = open(filename, 'r')
    for line in f:
        sub_line = re.sub(r'(\w+) +(\w+)', r'\2 \1', line.strip())
        print(sub_line)
    f.close()


swap_names('pessoas.txt')