def all_variants(str_):
    for count1 in range(len(str_)):
        for count2 in range(count1,len(str_)):
            yield str_[count1:count2+1]


s = all_variants(input())
for i in s:
    print(i)
