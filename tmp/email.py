# Recuperação de emails
from crypt import METHOD_SHA256
import re
import sys

email = r'\b\w(\w+[\-.]?)*\w@\w(\w|-)*\.(\w|-){2,}\b'
pe1 = re.compile(email)

email2 = r'^[\w\-.]+@[\w\-.]+\.[\w\-]{2,}$'
pe2 = re.compile(email2)
nlinha = 1
for linha in sys.stdin:
    m1 = pe1.search(linha)
    if m1:
        print(nlinha, ' :: ',"e1: VÁLIDO", '::', m1.group())
    else:
        print(nlinha, ' :: ',"e1: INVÁLIDO")
    m2 = pe2.search(linha)
    if m2:
        print(nlinha, ' :: ',"e2: VÁLIDO", '::', m2.group())
    else:
        print(nlinha, ' :: ',"e2: INVÁLIDO")
    nlinha = nlinha + 1