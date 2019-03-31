def regressivo(n):
      for i in range(n,-1,-1):
            for j in range(i):
                  if j == i-1:
                        print(i)
                  else:
                        print(i, end='-')

num = int(input())
regressivo(num)