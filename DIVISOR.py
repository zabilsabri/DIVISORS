__foundby__ = "zabilsabri"


number = int(input("ENTER YOUR NUMBER: "))
answer = []

for i in range(1, number + 1):
    x = number % i
    if x == 0:
        answer.append(i)

print(answer)
