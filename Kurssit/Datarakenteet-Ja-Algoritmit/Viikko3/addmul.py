import re

r = {
    'add': lambda o1, o2: str(int(o1)+int(o2)),
    'mul': lambda o1, o2: str(int(o1)*int(o2))
}

def evaluate(data):
    for match in set(re.findall(r'(?:mul|add)\([1-9]\d*,[1-9]\d*\)', data)):
        o1, o2 = match[4:-1].split(',')
        data = data.replace(match, r[match[:3]](o1, o2))
    return data
