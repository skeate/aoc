from typing import List
from hashlib import md5

def run(inp: List[str]):
    v = ''.join(inp).strip()
    x = 1
    h = ''
    while h[:5] != '00000':
        h = md5(f'{v}{x}'.encode('utf-8')).hexdigest()
        x += 1

    print(x-1)

    while h[:6] != '000000':
        h = md5(f'{v}{x}'.encode('utf-8')).hexdigest()
        x += 1

    print(x-1)
