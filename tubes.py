import random
import time

global pw
pw = 3542

def bruteForce():
    start_time = time.perf_counter_ns()

    #test = str(pw)
    count = 0
    answer = []

    test = [3, 5, 4, 2]
    count = 0
    answer = []

    for i in range(len(test)):
        while count <= 9:
            #print("Angka ke",i, ": ", count)
            if count == test[i]:
                #print("----------------------------")
                #print("Angka ke",i, "ketemu, yaitu", count)
                #print("----------------------------")
                answer.append(count)
                break
            count += 1
        count = 0

    for j in answer:
        print(j, end="")
    #print(answer)
    
    end_time = time.perf_counter_ns()
    global time_lapsed
    time_lapsed = end_time - start_time
    print()
   

dnc_answer = []
split_amount = 0

def divide_conquer(x):
    global dnc_answer
    global split_amount

    if (len(x) == 1):
        x = int(x[0])
        guess = 0
        while (guess != x):
            guess = guess + 1
        dnc_answer.append(guess)
    else:
        length = len(x)
        indexMid = length // 2
        split_amount = split_amount + 1
        bag1 = x[:indexMid]
        bag2 = x[indexMid:]
        divide_conquer(bag1)
        divide_conquer(bag2)


#Brute Force
print("PROGRAM BRUTE FORCE")
bruteForce()
print("time taken =", time_lapsed)
print()

#Divide and conquer
print("PROGRAM DIVIDE & CONQUER")

start_time = time.perf_counter_ns()
pw_list = [int(x) for x in str(pw)]
divide_conquer(pw_list)
end_time = time.perf_counter_ns()

time_dnc = end_time - start_time

print("Amount divided:", split_amount)
print("Divide and Conquer answer:", dnc_answer)
print("Divide and Conquer time taken:", time_dnc)