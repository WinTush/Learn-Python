import re


n = '\n\n'
group = r'[a-z]way'
text = 'This is a highway'
print(f'Group "{group}":')
print(text)
print(re.search(group, text), end=n)


exclude = r'[^a-zA-Z ]'
text_2 = 'This sentence contains the number 1.'
print(f'Exclude "{exclude}":')
print(text_2)
print(re.search(exclude, text_2), end=n)


either = r'(cat|dog).'
text_3 = 'I dislike cats.'
text_4 = 'I also dislike dogs.'
print(f'Either or "{either}":')
print(text_3)
print(re.search(either, text_3))
print(text_4)
print(re.search(either, text_4), end=n)
