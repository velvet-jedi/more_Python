def merge_the_tools(string, k):
    # your code goes here
    
    l = len(string)
    lost = []
    for i in range(l):
        if i%k == 0:
            lost.append(string[i:i+k])
    
    
    for ar in lost:
        lol = []
        for x in ar:
            if x not in lol:
                lol.append(x)
                # print(x)
        print(''.join(lol))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
