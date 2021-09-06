import re

log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR: Performing package upgrade'
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])
print()


def check_aei(text):
    return re.search(r"a.e.i", text) is not None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True
print()

print(re.search(r'p.ng', 'penguin'))
print(re.search(r'p.ng', 'clapping'))
print(re.search(r'p.ng', 'sponge'))
print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))
