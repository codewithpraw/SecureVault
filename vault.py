import os
import json

VAULT_FILE = "passwords.json"

def load_vault():
    """Loads passwords from the JSON file. If the file doesn't exist, returns an empty dictionary."""
    if not os.path.exists(VAULT_FILE):
        return{"accounts":[]}
    with open (VAULT_FILE,"r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"accounts":[]}

def save_vault(data):
    """Save the Python Dictionary back into the JSON File."""
    with open(VAULT_FILE,"w") as file:
        json.dump(data, file, indent=4)

def add_password():
    site = input("\nEnter your Site:")
    username = input("\nEnter your Username:")
    password = input("\nEnter your Password:")

    vault_data = load_vault()
    
    new_entry = {
        "site" : site,
        "username" : username,
        "password" : password
    }
    vault_data["accounts"].append(new_entry)
    save_vault(vault_data)
    print(f"\nSuccess!Your Password for the {site} has been saved successfully!")

def view_password():
    #It shows all the saved accounts and passwords.
    vault_data = load_vault()
    accounts = vault_data.get("accounts",[])

    if not accounts:
        print("\nYour vault is empty.")
        return
    print("\n---Your Saved Passwords---")
    for index, accounts in enumerate(accounts, start=1):
        print(f"{index}.Website:{accounts['site']}")
        print(f"Username:{accounts['username']}")
        print(f"Password:{accounts['password']}")
        print("-" * 28)

def main():
    while True:
        print("\n===Sacret Vault Menu===")
        print("1.Add a Password")
        print("2.View a Password")
        print("3.Exit")

        choice = input("\nChoose an option(1-3):").strip()
        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            print("\nClosing Secret Vault, Thank You!!!<3")
            break
        else:
            print("Please, choose an correct option.")

if __name__ == '__main__':
    main()