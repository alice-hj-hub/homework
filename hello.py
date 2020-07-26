fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

def cot(name_fruit):
    count = 0

    for fruit in fruits:
        if fruit == name_fruit:
            count += 1

    return count

print(cot('수박'))




