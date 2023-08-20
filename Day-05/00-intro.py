# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             print(i, 'equals', j, '*', i // j)
#             break
#     else:
#         print(i, 'is a prime number')

text = (
    'this is sample with several words '
    'this is more sample text with some different words '
    'that is also another text with other different words'
)
# print(text)
# print(len(text.split()))
word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# print(word_count)
# for key, value in sorted(word_count.items()):
#     print(f'{key:<12}:{value}')

print(word_count)
for key, value in sorted(word_count.items(), key=lambda item: item[1]):
    print(f'{key:<12}:{value}')
