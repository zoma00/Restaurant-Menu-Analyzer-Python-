# Restaurant-Menu-Analyzer-Python

Here's a sample README file for your Restaurant Menu Analysis project:

---

# Restaurant Menu Analyzer

## Overview

The Restaurant Menu Analyzer is a Python project designed to read, analyze, and display data from a restaurant's menu. This tool extracts menu items from a text file, calculates average prices, identifies the most expensive items, and allows for filtering based on categories. It serves as a practical example of data manipulation and analysis in Python.

## Features

- **Read Menu Data**: Reads menu items from a text file and stores them in a structured format.
- **Average Price Calculation**: Calculates the average price of all menu items.
- **Most Expensive Item**: Identifies the menu item with the highest price.
- **Category Filtering**: Filters menu items based on specified category keywords (e.g., "Vegetarian", "Dessert").
- **User-Friendly Display**: Displays the menu items in a clear and organized format.

## Data Format

Each line in the text file should follow this format:

```
"Item Name" (Price) - Description
```

### Example Menu File

```
"Pizza Margherita" ($10.99) - Classic pizza with tomato sauce and mozzarella cheese.
"Beef Burger" ($12.50) - Served with french fries and a side salad.
"Chocolate Cake" ($5.99) - Rich and decadent chocolate cake.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-menu-analyzer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd restaurant-menu-analyzer
   ```

3. Ensure you have Python installed on your machine.

## Usage

1. Place your menu text file in the project directory.
2. Run the main Python script:
   ```bash
   python menu_analyzer.py
   ```

3. Follow the prompts to analyze the menu data.

## Functions

### `read_menu_data(file_path)`

Reads the menu data from the specified text file and stores it in a list of dictionaries.

### `calculate_average_price(menu_items)`

Calculates and returns the average price of all menu items.

### `find_most_expensive_item(menu_items)`

Identifies and returns the menu item with the highest price.

### `filter_by_category(menu_items, category)`

Filters and returns menu items that contain the specified category keyword in their description.

### `display_menu(menu_items)`

Displays the menu items in a user-friendly format.

## Bonus Challenge

Enhance the filtering functionality to identify and display all vegetarian options on the menu.

## Tips

- Use string manipulation techniques to extract item name, price, and description from each line.
- Utilize appropriate data structures (lists, dictionaries) to organize the menu data effectively.
- Explore formatting options for improved readability when displaying the menu.

## License

This project is licensed under the MIT License.




