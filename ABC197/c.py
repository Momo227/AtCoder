import math

def main():

   n, x, y = list(map(int, input().split()))

   D = math.sqrt(x*x + y*y)

   if(n == D):
       print("1")
   elif(D <= 2*n):
       print("2")
   else:
       print(math.ceil(D/n))



if __name__ == '__main__':
    main()