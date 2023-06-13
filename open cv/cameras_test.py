from my_class import MyClass
from my_classTwo import MyClassTwo

choice = input("Enter 1 for MyClass or 2 for MyClassTwo: ")

if choice == "1":
    cam = MyClass()
elif choice == "2":
    cam = MyClassTwo()
else:
    print("Invalid choice")
    exit()

cam.show()
