import re

log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR: Performing package upgrade'
regex = r'\[(\d+)\]'
assert re.search(regex, log)[1] == '12345'


def check_aei(text):
    return re.search(r"a.e.i", text) is not None


assert check_aei("academia") is True
assert check_aei("aerial") is False
assert check_aei("paramedic") is True

assert re.search(r'p.ng', 'penguin')[0] == 'peng'
assert re.search(r'p.ng', 'clapping')[0] == 'ping'
assert re.search(r'p.ng', 'sponge')[0] == 'pong'
assert re.search(r'p.ng', 'Pangaea', re.IGNORECASE)[0] == 'Pang'
