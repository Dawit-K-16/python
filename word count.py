paragraph = input("Enter your paragraph: ")
words = paragraph.split()
print("Total words:", len(words))

word_count = {}
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(word, ":", count)

most_frequent = max(word_count, key=word_count.get)
print("Most frequent word:", most_frequent)