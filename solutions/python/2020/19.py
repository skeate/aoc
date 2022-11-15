from typing import List
import re
import lark


def parse_rule(l):
    c = l.index(":")
    n = int(l[:c])
    r = re.findall(r'[|:] (?:"(\w)"|((?:\d+ )*\d+))', l[c:])
    if len(r) == 1 and r[0][0] != "":
        return n, r[0][0]
    return n, [[*map(int, ns.split(" "))] for a, ns in r]


def parse(s: str, r, ri: int, indent=""):
    # print(f"{indent}matching {s} against rule {ri}")
    if s == "":
        return (False, 0)
    if type(r[ri]) == str:
        if s[0] == r[ri]:
            return (True, 1)
    else:
        for rule in r[ri]:
            parsed = True
            total_consumed = 0
            rule_index = 0
            while parsed and rule_index < len(rule):
                parsed, consumed = parse(
                    s[total_consumed:], r, rule[rule_index], f"{indent}|   "
                )
                total_consumed += consumed
                rule_index += 1
            if parsed:
                # print(f"{indent}-> {s[total_consumed:]}")
                return (True, total_consumed)
    # print(f"{indent}xxxx")
    return (False, 0)


def try_parse(parser, message):
    try:
        parser.parse(message)
    except:
        return False
    return True


def larkify(rules):
    larky_rules = "\n".join(
        str(r)
        + ": "
        + (
            f'"{rs}"'
            if type(rs) == str
            else "|".join(" ".join(map(str, rss)) for rss in rs)
        )
        for r, rs in rules.items()
    )
    larky_rules = (
        larky_rules.replace("0", "zero")
        .replace("1", "one")
        .replace("2", "two")
        .replace("3", "three")
        .replace("4", "four")
        .replace("5", "five")
        .replace("6", "six")
        .replace("7", "seven")
        .replace("8", "eight")
        .replace("9", "nine")
    )
    return lark.Lark(larky_rules, start="zero")


def run(inp: List[str]):
    rules = {}
    messages = []
    put_in_rules = True
    for l in inp:
        if l.strip() == "":
            put_in_rules = False
        elif put_in_rules:
            r, n = parse_rule(l)
            rules[r] = n
        else:
            messages.append(l.strip())

    p = larkify(rules)
    print(len([m for m in messages if try_parse(p, m)]))

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    p = larkify(rules)
    print(len([m for m in messages if try_parse(p, m)]))
