
import re

mas = []
for i in range(5):
    mas.append(input())

for i in mas:
    print(re.sub(r'([А-Я]{1})[а-я]*-?\1?[а-я]*\s\1\.\1\.\sP0000', '', i))
