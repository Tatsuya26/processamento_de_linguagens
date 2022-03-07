import re
import sys

inteiro = r'(\+|-)?(\d+)'

#?: significa que o ponto não deve ser capturado, parte decimal entre paratenses para poder ser capturada
real    = r'(\+|-)?(\d+)(?:\.(\d+))?'
pint    = re.compile(inteiro)
preal   = re.compile(real)
#'\b -> operador de contexto -> Fronteira de uma palavra
#\1
palavraDobrada = r'\b(\w+)\s+\1\b'



'''
for linha in sys.stdin:
    m = pint.search(linha)
    print(m.groups())
    print(m.group(1,2,1))
'''

'''
for linha in sys.stdin:
    m = re.search(palavraDobrada,linha)
    if m:
        print(m.groups())
        print(m.group())
    else :
        print("No match")
'''


#Named groups -> Sintax do python (?P) - comportamento alterado

palavra = r'(?P<pal>\b\w+\b)'

for linha in sys.stdin:
    m = re.search(palavra,linha)
    if m:
        dic = m.groupdict()
        print(dic)
        #print(m.group(1))
        #print(m.group('pal'))
    else :
        print("No match")