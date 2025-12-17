print("_"*10,"INVENTRY","_"*10)
cart=[]
fruits=["Apple", "Grapes", "Mango", "Banana"]

while True:
    for i in range(len(fruits)):
        print(fruits[i])

    print("\nChoode the below optins")
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

    user_option=int(input("Choose your option:"))
    if user_option==1:
        user_need=input("Enter fruit").split(" ")
        for fruit in user_need:
            if fruit not in fruits:
                print(fruit,"is not available in inventry!")
            else:
                if fruit not in cart:
                    cart.append(fruit)
                    print(fruit,"added to cart")
                else:
                    print(fruit,"Already available Cart")

    elif user_option == 2:
        user_remove=input("Enter the fruit: ")
        if user_remove in cart:
            cart.remove(user_remove)
            print(user_remove,"removed from cart")
        else:
            print(user_remove,"not in cart")

    elif user_option == 3:
        print("_"*20)
        for items in cart:
            print(items,end=" ")
        print()
        print("_"*20)

    elif user_option == 4:
        print("Exiting")
        break
    else:
        print("Choose Correct option")
