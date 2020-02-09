
def oddNum(n):
    for i in range(1,n):
        if(i%2 == 1):
            print(i)

if __name__ == "__main__":
    n = int(input())    
    oddNum(n)
