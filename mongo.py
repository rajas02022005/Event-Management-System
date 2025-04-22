from pymongo import MongoClient
import sys

def choice_input():
    print("\n1. Insert data into database")
    print("2. Update database documents")
    print("3. Delete database documents")
    print("4. Show database collections")
    print("5. Exit")

def main():
    # Initialize MongoDB connection
    client = MongoClient("localhost", 27017)
    db = client.myDb
    collection = db.dummyColl
    
    while True:
        choice_input()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:  # Insert data
            document = {}
            while True:
                key = input("Enter key: ")
                value = input("Enter value: ")
                document[key] = value
                ch = input("Do you want to enter more (y/n)? ")
                if ch.lower() == 'n':
                    break
            collection.insert_one(document)
        
        elif choice == 2:  # Update data
            search_key = input("Enter searched key: ")
            search_value = input("Enter searched value: ")
            new_key = input("Enter new key: ")
            new_value = input("Enter new value: ")
            search_obj = {search_key: search_value}
            new_obj = {"$set": {new_key: new_value}}
            collection.update_one(search_obj, new_obj)
        
        elif choice == 3:  # Delete data
            removable_key = input("Enter removable key: ")
            removable_value = input("Enter removable value: ")
            removable_obj = {removable_key: removable_value}
            collection.delete_one(removable_obj)
        
        elif choice == 4:  # Show data
            cursor = collection.find()
            for document in cursor:
                print(document)
        
        elif choice == 5:  # Exit
            client.close()
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
