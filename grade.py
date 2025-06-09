name = input("Enter your name: ")

score = list(map(int, input("Enter numbers separated by space: ").split()))
print("You scores are:", score)
length = len(score)

print(name, " your grades are as follows")

for i in range(length):
    if score[i] >= 90:
        print(score[i], " Grade: A")
    elif score[i] >= 80:
        print(score[i], " Grade: B")
    elif score[i] >= 70:
        print(score[i], " Grade: C")
    elif score[i] >= 60:
        print(score[i], " Grade: D")
    else:
        print("Grade: F")
