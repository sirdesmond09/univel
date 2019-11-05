# def greet(*people):

#     print(people)

# greet("desmond", "attah", "bimi")

# def solve(x = 3,y = 4,z = 2):
#     solution = x*y-z
#     print(solution)


# solve(12)  

# def you(**people):
#     print(people)

# you(name = 'attah', age = 20, state = 'lagos')

# def stupid(depth = 10):
#     if depth < 1:
#         return
#     print("I am recursing inward")
#     stupid(depth-1)
#     print("I am recursing backward")


# stupid()

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# n_fact = factorial(6)
# print(n_fact) 

# x= [20, 70, 100, 120, 160, 165, 171]

# num = 0
# for i in range(len(x)):
#     if i == len(x)-1:
#         break
    
#     first =x[num]
#     ammount_saved =x[i+1] - first
#     num+=1
#     print(ammount_saved)


# def get_savings(d):
#     if len(d) < 2:
#         return
#     else:
#         print(d[1] - d.pop(0))
#         return get_savings(d)

# get_savings(x)


def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    if n == 1: 
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod) 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 

TowerOfHanoi(6, 'A', 'B', 'C')
