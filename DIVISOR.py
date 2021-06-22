__foundby__ = "zabilsabri"


number = int(input("ENTER YOUR NUMBER: "))
answer = []

for i in range(1, number + 1):
    if number % i == 0:
        answer.append(i)
        
print(answer)
