import threading

#this is the method perform one operation (Ex.: process one dataframe)
def method_1(num):
    #Logic
    print("Print input : " + str(num))
    for i in range(0,10):
        print("\nPrinting from method_1 : " + str(i))

#this is the method perform second operation (Ex.: process another dataframe)
def method_2(num):
    #Logic
    print("Print input : " + str(num))
    for i in range(0,10):
        print("\nPrinting from method_2 : " + str(i))

#this is the method perform third operation (Ex.: process one dataframe)
def method_3():
    #Logic
    for i in range(0,10):
        print("\nPrinting from method_3 : " + str(i))


if __name__ == "__main__":
    #this is how you split the work into different threads.
    #Here I want to do 2 operations simultaneously, so i have created 2 threads
    #target = will have the method name alone.
    #args = will have the arguments that you need to pass to this method.
    t1 = threading.Thread(target=method_1, args=(2,)) 
    t2 = threading.Thread(target=method_2, args=(5,))

    #if the method is not expecting arguments then args can be skipped as follows
    t3 = threading.Thread(target=method_3)
  
    # Start method on each thread will start its execution.
    t1.start()
    t2.start()
    t3.start()
  
    #Following is needed to check if the execution of those threads is complete or not before we proceed further.
    #If this is not added then the parent thread will not get info about the completion of child thread's execution and it keeps waiting.
    t1.join()
    t2.join()
    t3.join()
