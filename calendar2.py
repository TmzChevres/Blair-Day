file1 = open("C:/Users/agupta-22/Magic-Mirror/calendar2.txt", "w")
with open('calendar1.txt', 'r') as f:
    cnt = 1
    for line in f:
        if cnt <= 17:
            print(line, end='', file=open("calendar2.txt", "a"))
            cnt += 1
        else:
            break
file1.close()