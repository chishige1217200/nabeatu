def nabeatu(num: int):
    if num <= 0:
        return
    if num % 3 == 0:
        return True

    s = str(num)
    for di in s:
        if int(di) == 3:
            return True


# main
for num in range(0, 401):
    if nabeatu(num) == True:
        print(str(num))
