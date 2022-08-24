score = 0
win = 0
for i in range(0,30):
    emtiaz = int(input())
    score += emtiaz
    i += 1
    if emtiaz == 3:
        win += 1
print(score, win)