import random
def jokes():
    l1=["shahrukh Khan ","virat Kohli","Sachin Tendulkar","Rohit Sharma","MS Dhoni"]
    l2=["launches",f"dance with {random.choice(l1)}", "cancels","eats","declaress war on"]
    l3=["at red fort","in a mumbai local","a plate of samosas","inside paraliament","at a ganga ghat"]
    l4=["and the crowd goes wild","and the crowd goes silent","and the crowd laughs","and the crowd cheers","and the crowd boos"]

    print(random.choice(l1),random.choice(l2),random.choice(l3),random.choice(l4),sep=" ")
    print()
# This code generates a random joke by selecting random elements from predefined lists.

if __name__ == "__main__":

    while True:
        if input("Do you want to see a joke? (yes/no): ").strip().lower() != "yes":
            print("Goodbye!")
            break
        jokes()
