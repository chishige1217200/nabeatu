def nabeatu(num: int):
    if num <= 0:
        return False
    if num % 3 == 0:
        return True

    s = str(num)

    return False


# main
for num in range(0, 401):
    if nabeatu(num):
        print(str(num))
