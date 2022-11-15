from typing import List

def mult_bags(n, bags):
    return (bags[0] * n, bags[1])

def find_bag_in(target, bags, container):
    return target in bags[container] or any(find_bag_in(target, bags, c) for c in bags[container])

def run(inp: List[str]):
    bags = {}
    for line in inp:
        bag = ' '.join(line.split(' ')[:2])
        bags[bag] = {}
        unparsed_contents = line.split(' ')[4:]
        for count, desc, color in zip(unparsed_contents[::4], unparsed_contents[1::4], unparsed_contents[2::4]):
            if count != "no":
                bags[bag][f'{desc} {color}'] = int(count)
    print(len([v for k,v in bags.items() if find_bag_in('shiny gold', bags, k)]))

    total_subbags = 0
    to_expand = list(bags['shiny gold'].items())
    while len(to_expand) > 0:
        next_expansion = []
        for b,c in to_expand:
            total_subbags += c
            next_expansion.extend((b2, c*c2) for b2,c2 in bags[b].items())
        to_expand = next_expansion
    print(total_subbags)


