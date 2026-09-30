user_name=input("Enter name: ")
print("(H)ello\n""(G)oodbye\n""(Q)uit")
choice=input(">>> ").upper()
while choice != "Q":
   if choice == "H":
       print(f"hello {user_name}")
   elif choice == "G":
       print(f"goodbye {user_name}")
   else:
        print("Invalid message")
   print("(H)ello\n""(G)oodbye\n""(Q)uit")
   choice=input(">>> ").upper()
print("Finished.")