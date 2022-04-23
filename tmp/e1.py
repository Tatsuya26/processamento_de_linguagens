import sys
import re

pal = r'[A-Za-z][A-Za-z\-]*'
ppal = re.compile(pal)

chars = 0
pals = 0
linhas = 0

for linha in sys.stdin:
    pals = pals + len(ppal.findall(linha))
    linhas = linhas + 1
    chars = chars + len(linha)

print(linhas, pals, chars)
