import suggest_ref_db

def display_menu():
    print("Paper info:")
    print("-----------")
    print()
    print("1 - Provide MSCcode")
    print("2 - Provide partial MSCcode")    

def main():
    display_menu()
    try:
        choice=int(input("Choice: "))
        if (choice==1):
            code=input("Please provide an MSCcode:")
            print("Potential referees:")
            print("-------------------")
            auth=suggest_ref_db.by_msc(code)
            for a in auth:
                print(a["name"],a["email"])
        if (choice==2):
            partial_code=input("Please provide a partial MSCcode:")
            print("Potential referees:")
            print("-------------------")
            auth=suggest_ref_db.by_partial_msc(partial_code)
            for a in auth:
                print(a["name"],a["email"])
    except:
        print("That is not a valid selection.")

if __name__ == "__main__":
    main()
