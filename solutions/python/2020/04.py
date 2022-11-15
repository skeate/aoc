import re
from typing import List

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


def check_passport(pp: str):
    return all([(f + ":") in pp for f in required_fields])


def check_passport2(pp: str):
    byr = re.search(r"byr:(\d{4})\b", pp)
    iyr = re.search(r"iyr:(\d{4})\b", pp)
    eyr = re.search(r"eyr:(\d{4})\b", pp)
    hgt = re.search(r"hgt:(\d+)(cm|in)\b", pp)
    hcl = re.search(r"hcl:#[0-9a-f]{6}\b", pp)
    ecl = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", pp)
    pid = re.search(r"pid:[0-9]{9}\b", pp)
    try:
        return (
            check_passport(pp)
            and (1920 <= int(byr.group(1)) <= 2002)
            and (2010 <= int(iyr.group(1)) <= 2020)
            and (2020 <= int(eyr.group(1)) <= 2030)
            and (
                (150 <= int(hgt.group(1)) <= 193)
                if hgt.group(2) == "cm"
                else (59 <= int(hgt.group(1)) <= 76)
            )
            and hcl is not None
            and ecl is not None
            and pid is not None
        )
    except:
        return False


def run(inp: List[str]):
    pps = []
    pp = ""
    for line in inp:
        if line.strip() == "":
            pps.append(pp.strip())
            pp = ""
        else:
            pp += " " + line.strip()
    pps.append(pp.strip())
    print(len([x for x in pps if check_passport(x)]))
    print(len([x for x in pps if check_passport2(x)]))
