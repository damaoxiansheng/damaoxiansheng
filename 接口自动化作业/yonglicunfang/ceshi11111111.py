a = "abcdefabcdefabcd"
b = list(a)
b[b.index("f", 6, 12)] = "fly"
print(b)

import requests