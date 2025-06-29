from printer import print_status, print_all_contact

def add_contact(contacts: list[dict]):
    first_name = input("first name: ")
    last_name = input("last name: ")
    phone = input("phone: ")
    group = input("group (family, friend, work, other): ")

    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })

    print_status('success')

def show_all_contact(contacts: list[dict]):
    if contacts:
        print_all_contact(contacts)
    else:
        print_status('error')

def search_contact(contacts: list[dict]):
    query = input("Search by first or last name: ").lower()
    results = [c for c in contacts if query in c['first_name'].lower() or query in c['last_name'].lower()]

    if results:
        print_all_contact(results)
    else:
        print_status('not found')

def delete_contact(contacts: list[dict]):
    phone = input("Enter phone number of contact to delete: ")
    for i, c in enumerate(contacts):
        if c['phone'] == phone:
            del contacts[i]
            print_status('deleted')
            return
    print_status('not found')

def update_contact(contacts: list[dict]):
    phone = input("Enter phone number of contact to update: ")
    for c in contacts:
        if c['phone'] == phone:
            c['first_name'] = input(f"New first name (current: {c['first_name']}): ") or c['first_name']
            c['last_name'] = input(f"New last name (current: {c['last_name']}): ") or c['last_name']
            c['group'] = input(f"New group (current: {c['group']}): ") or c['group']
            print_status('updated')
            return
    print_status('not found')
