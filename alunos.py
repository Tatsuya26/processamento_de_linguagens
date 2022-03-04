import re
import sys

aluno  = r'(?:\"(?P<id>.+)\",)(?:\"(?P<nome>.+)\",)(?:\"(?P<curso>.+)\",)(?:(?P<tpc1>\d+),)(?:(?P<tpc2>\d+),)(?:(?P<tpc3>\d+),)(?P<tpc4>\d+)'
paluno = re.compile(aluno)

for linha in sys.stdin:
    maluno = paluno.search(linha)
    if maluno:
        print(maluno.groups())
        dic = maluno.groupdict()
        print(dic)
    else :
        print("error")