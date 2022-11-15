from typing import List

def exe(ins):
    ip = 0
    executed = set()
    acc = 0
    while ip not in executed and ip < len(ins):
        executed.add(ip)
        i, v = ins[ip]
        if i == 'acc':
            acc += v
            ip += 1
        elif i == 'jmp':
            ip += v
        elif i == 'nop':
            ip += 1
    return (acc, ip == len(ins))

def run(inp: List[str]):
    ins = [(i.split(' ')[0], int(i.split(' ')[1])) for i in inp]
    print(exe(ins)[0])

    finished = False
    jmpsnops = [i for i, x in enumerate(ins) if x[0] == 'jmp' or x == 'nop']
    for rep in jmpsnops:
        cpy = ins.copy()
        cpy[rep] = ('nop' if cpy[rep][0] == 'jmp' else 'jmp', cpy[rep][1])
        a, finished = exe(cpy)
        if finished:
            print(a)
            break
