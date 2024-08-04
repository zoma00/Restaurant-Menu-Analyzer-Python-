def read_menu(file_path):
    menu_items = []
    with open(file_path, 'r') as file:
        for line in file:
            # Extracting item name, price, and description
            item_name, rest = line.split(' - ($')
            price, description = rest.split(') - ')
            price = float(price.strip())
            item_name = item_name.strip()
            description = description.strip()

            menu_items.append({
                'name': item_name,
                'price': price,
                'description': description
            })
    return menu_items

def calculate_average_price(menu_items):
    total_price = sum(item['price'] for item in menu_items)
    average_price = total_price / len(menu_items) if menu_items else 0
    return average_price

def find_most_expensive_item(menu_items):
    if not menu_items:
        return None
    return max(menu_items, key=lambda item: item['price'])



def filter_by_keywords(menu_items, keywords):
    return [
    item for item in menu_items if any
    (keyword.lower() in item['description'].lower() or
    keyword.lower() in item['name'].lower()
    for keyword in keywords
     )]

 
def display_menu(menu_items):
    print(f"{'Item Name':<30} {'Price':<10} {'Description'}")
    print("-" * 70)
    for item in menu_items:
        print(f"{item['name']:<30} ${item['price']:<10} {item['description']}")

# Example usage
if __name__ == "__main__":
    menu_file = 'menu.txt'  # Ensure this file is in the same directory
    menu_items = read_menu(menu_file)
    
    # Display all menu items
    print("Full Menu:")
    display_menu(menu_items)
    
    print(f"\nAverage Price: ${calculate_average_price(menu_items):.2f}")
    
    most_expensive = find_most_expensive_item(menu_items)
    if most_expensive:
        print(f"Most Expensive Item: {most_expensive['name']} at ${most_expensive['price']:.2f}")

    keywords_to_filter = ['Chocolate', 'Vegetarian']  # Change as needed
    filtered_items = filter_by_keywords(menu_items, keywords_to_filter)
    print(f"\nItems matching keywords '{', '.join(keywords_to_filter)}':")
    display_menu(filtered_items)
 