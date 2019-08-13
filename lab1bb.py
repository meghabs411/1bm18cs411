def fibonacci(n):
    a=0
    b=1
    for i in range(n):
            print(a)
            nxt=a+b
            a=b
            b=nxt

def main():
    
       n=int(input("eneter the size"))
       fibonacci(n)
main()
        

