import re


group = r'[a-z]way'
text = 'This is a highway'
assert re.search(group, text)[0] == 'hway'


exclude = r'[^a-zA-Z ]'
text_2 = 'This sentence contains the number 1.'
assert re.search(exclude, text_2)[0] == '1'


either = r'(cat|dog)s?'
text_3 = 'I dislike cats.'
assert re.search(either, text_3)[0] == 'cats'
text_4 = 'I also dislike dogs.'
assert re.search(either, text_4)[0] == 'dogs'
