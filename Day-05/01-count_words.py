from collections import Counter

text = (
    'this is sample with several words '
    'this is more sample text with some different words '
    'that is also another text with other different words'
)
cnt = Counter(text.split())
print(cnt)

for key, value in sorted(cnt.items(), key=lambda item: item[1]):
    print(f'{key:<12}:{value}')

print(len(cnt.items()))
