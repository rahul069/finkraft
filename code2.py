def pair(n, tar):
    d = {}

    for i,e in enumerate(n):
        if tar-e in d:
            print("pair found",n[d.get(tar-e)],n[i])
            return
        d[e] = i
        print("pair not found")

print(pair([1,2,3],5))