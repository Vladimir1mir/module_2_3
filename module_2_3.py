mu_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index<len(mu_list):
    if mu_list[index]<0:
        break
    if mu_list[index]>0:
        print(mu_list[index])

    index+=1

