def Variance(a):
    #res = a/1392
    res = a/92721
    res = round(res, 2)
    res = res * 100
    res = str(res)
    res = res + "%"
    return (res)


file = open("proj.snp", "r")

file_str = file.read()
file.close()

file_str = file_str.split("\n")

count = 0

for element in file_str:
    count += 1

print(f"Количество изменений в гене: {count}")

print(f"Примерный коэффициент вариативности равен {Variance(count)}")