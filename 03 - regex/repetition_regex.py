import re


# * matches 0 or more repetitions
assert re.search(r'Py[a-z]*n', 'Pygmalion')[0] == 'Pygmalion'
assert re.search(r'Py[a-z]*n', 'Pyn')[0] == 'Pyn'

# + matches 1 or more repetitions
assert re.search(r'o+l+', 'wooly')[0] == "ool"

# ? matches 0 or 1 repetitions
assert re.search(r'p?each', 'To each their own')[0] == 'each'
assert re.search(r'p?each', 'I like peaches')[0] == 'peach'

# {n} matches 'n' number of repetitions
assert re.search(r'o{2}g', "Kungfu Panda's Oogway", re.IGNORECASE) == 'Oog'
