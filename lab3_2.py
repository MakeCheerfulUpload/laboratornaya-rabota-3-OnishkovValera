import re
ms = [
'0000N0000U000L',
' рпоалвдNgjj&U*7%L  N**ULL ',
' нрраррNоаоорврвUосNимтнUлмоL hghfjNbvn5U87kL ',
' nNnNnNnNnnhhUuuuLLvlvL рпаалл:NимипUу?5L',
' 0000N0000U000L рпоалвдNgjj&U*7%L N**ULL нрраррNоаоорврвUосNимтнUлмоL hghfjNbvn5U87k nNnNnNnNnnhhUuuuLLvlvLрпаалл:NимипUу?5L ']

for i in ms:
    n = re.findall(r'\s\S*N[^\sU]{4}U[^\sL]{3}L\S*\s', re.sub(r'\s','  ',i))
    print(n)

