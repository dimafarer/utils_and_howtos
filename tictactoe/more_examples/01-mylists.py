# ============================================
# PYTHON LISTS - WEEK 3 TUTORIAL
# ============================================
# This file teaches: indexing, negative indexing, slicing, append, pop, and looping
# We progress from EASY to HARDER concepts

# ============================================
# SECTION 1: CREATING OUR SAMPLE LISTS
# ============================================
# First, let's create 5 different lists to work with

# 1. Shopping cart - e-commerce application
shopping_cart = ["milk", "bread", "eggs", "apples", "cheese", "yogurt"]

# 2. Daily temperatures - weather tracking system
temperatures = [72, 68, 75, 80, 77, 73, 69, 71]

# 3. User permissions - access control system
user_roles = ["admin", "editor", "viewer", "guest", "moderator"]

# 4. Task priorities - project management app
task_list = ["Fix login bug", "Update homepage", "Write documentation", "Test payment system", "Deploy to production"]

# 5. Stock prices - financial application
stock_prices = [150.25, 148.90, 152.10, 149.75, 151.30, 153.45]

print("Lists created successfully!")
print()

# ============================================
# SECTION 2: POSITIVE INDEXING (EASY)
# ============================================
# Indexing means accessing ONE specific item in a list
# Python lists start counting at 0 (not 1!)
# Index 0 = first item, Index 1 = second item, etc.

print("=" * 50)
print("SECTION 2: POSITIVE INDEXING")
print("=" * 50)
print()

# Example 1: Get the FIRST item (index 0)
print("Example 1: Getting the first item")
first_item = shopping_cart[0]  # Index 0 is the FIRST position
print(f"First item in shopping cart: {first_item}")  # Output: milk
print()

# Example 2: Get the SECOND item (index 1)
print("Example 2: Getting the second item")
second_temp = temperatures[1]  # Index 1 is the SECOND position
print(f"Second temperature: {second_temp}")  # Output: 68
print()

# Example 3: Get the THIRD item (index 2)
print("Example 3: Getting the third item")
third_role = user_roles[2]  # Index 2 is the THIRD position
print(f"Third user role: {third_role}")  # Output: viewer
print()

# Example 4: Get the LAST item using len() function
print("Example 4: Getting the last item using length")
# len() tells us how many items are in the list
# If there are 6 items, the last index is 5 (because we start at 0)
last_index = len(shopping_cart) - 1  # We subtract 1 because indexing starts at 0
last_item = shopping_cart[last_index]
print(f"Shopping cart has {len(shopping_cart)} items")
print(f"Last item in shopping cart: {last_item}")  # Output: yogurt
print()

# ============================================
# SECTION 3: NEGATIVE INDEXING (EASY-MEDIUM)
# ============================================
# Negative indexing lets us count BACKWARDS from the end
# Index -1 = last item, Index -2 = second to last, etc.
# This is EASIER than using len() - 1!

print("=" * 50)
print("SECTION 3: NEGATIVE INDEXING")
print("=" * 50)
print()

# Example 1: Get the LAST item (index -1)
print("Example 1: Getting the last item with negative index")
last_task = task_list[-1]  # -1 always means the LAST item
print(f"Last task: {last_task}")  # Output: Deploy to production
print()

# Example 2: Get the SECOND TO LAST item (index -2)
print("Example 2: Getting the second to last item")
second_last_price = stock_prices[-2]  # -2 means second from the end
print(f"Second to last stock price: {second_last_price}")  # Output: 151.30
print()

# Example 3: Comparing positive vs negative indexing
print("Example 3: Positive vs Negative - they access the SAME items!")
print(f"temperatures[0] = {temperatures[0]}")  # First item using positive
print(f"temperatures[-8] = {temperatures[-8]}")  # First item using negative
print(f"temperatures[7] = {temperatures[7]}")  # Last item using positive
print(f"temperatures[-1] = {temperatures[-1]}")  # Last item using negative
print()

# ============================================
# SECTION 4: SLICING (MEDIUM)
# ============================================
# Slicing means getting MULTIPLE items from a list
# Syntax: list[start:stop]
# - start: where to begin (INCLUDED)
# - stop: where to end (NOT INCLUDED)
# Remember: stop index is NOT included in the result!

print("=" * 50)
print("SECTION 4: SLICING")
print("=" * 50)
print()

# Example 1: Get first 3 items
print("Example 1: Get first 3 items [0:3]")
first_three = shopping_cart[0:3]  # Start at 0, stop BEFORE 3
print(f"First 3 items: {first_three}")  # Output: ['milk', 'bread', 'eggs']
print("Note: Index 3 ('apples') is NOT included!")
print()

# Example 2: Get items from middle
print("Example 2: Get middle items [2:5]")
middle_temps = temperatures[2:5]  # Start at index 2, stop BEFORE 5
print(f"Temperatures from index 2 to 4: {middle_temps}")  # Output: [75, 80, 77]
print()

# Example 3: Slice from beginning (omit start)
print("Example 3: Slice from beginning [:3]")
# If you leave out the start, Python assumes 0
first_roles = user_roles[:3]  # Same as user_roles[0:3]
print(f"First 3 roles: {first_roles}")  # Output: ['admin', 'editor', 'viewer']
print()

# Example 4: Slice to the end (omit stop)
print("Example 4: Slice to the end [2:]")
# If you leave out the stop, Python goes to the end
last_tasks = task_list[2:]  # Start at index 2, go to the end
print(f"Tasks from index 2 onwards: {last_tasks}")
print()

# Example 5: Slice with negative indices
print("Example 5: Slice with negative indices [-3:]")
last_three_prices = stock_prices[-3:]  # Last 3 items
print(f"Last 3 stock prices: {last_three_prices}")
print()

# Example 6: Get every other item (step)
print("Example 6: Slice with step [::2]")
# Syntax: list[start:stop:step]
# step = how many items to skip
every_other = temperatures[::2]  # Get every 2nd item (skip 1 each time)
print(f"Every other temperature: {every_other}")
print()

# ============================================
# SECTION 5: APPEND (ADDING ITEMS) (EASY-MEDIUM)
# ============================================
# append() adds ONE item to the END of a list
# This is like "push" in other programming languages
# The list gets modified directly (no need to reassign)

print("=" * 50)
print("SECTION 5: APPEND (Adding Items)")
print("=" * 50)
print()

# Example 1: Add one item to shopping cart
print("Example 1: Adding 'butter' to shopping cart")
print(f"Before: {shopping_cart}")
shopping_cart.append("butter")  # Add butter to the end
print(f"After:  {shopping_cart}")
print()

# Example 2: Add multiple items one at a time
print("Example 2: Adding multiple temperatures")
print(f"Before: {temperatures}")
temperatures.append(74)  # Add first new temperature
temperatures.append(76)  # Add second new temperature
print(f"After:  {temperatures}")
print()

# Example 3: Add item and immediately access it
print("Example 3: Add item and access it with negative index")
user_roles.append("superadmin")  # Add new role
print(f"Newest role added: {user_roles[-1]}")  # -1 gets the item we just added
print(f"Full list: {user_roles}")
print()

# ============================================
# SECTION 6: POP (REMOVING ITEMS) (MEDIUM)
# ============================================
# pop() removes an item from the list AND returns it
# pop() with no argument removes the LAST item
# pop(index) removes the item at that specific index

print("=" * 50)
print("SECTION 6: POP (Removing Items)")
print("=" * 50)
print()

# Example 1: Remove the last item
print("Example 1: Remove last item from shopping cart")
print(f"Before: {shopping_cart}")
removed_item = shopping_cart.pop()  # Remove and return last item
print(f"Removed: {removed_item}")
print(f"After:  {shopping_cart}")
print()

# Example 2: Remove item at specific index
print("Example 2: Remove item at index 0 (first item)")
print(f"Before: {task_list}")
first_task = task_list.pop(0)  # Remove and return first item
print(f"Removed first task: {first_task}")
print(f"After:  {task_list}")
print()

# Example 3: Remove from middle
print("Example 3: Remove item from middle (index 2)")
print(f"Before: {user_roles}")
middle_role = user_roles.pop(2)  # Remove item at index 2
print(f"Removed: {middle_role}")
print(f"After:  {user_roles}")
print()

# Example 4: Pop in a workflow (process tasks)
print("Example 4: Processing tasks one by one")
print(f"Tasks remaining: {len(task_list)}")
current_task = task_list.pop(0)  # Get first task and remove it
print(f"Working on: {current_task}")
print(f"Tasks remaining: {len(task_list)}")
print()

# ============================================
# SECTION 7: LOOPING THROUGH LISTS (MEDIUM)
# ============================================
# Looping means going through each item in a list one by one
# We use a "for loop" to do this
# Syntax: for variable_name in list_name:

print("=" * 50)
print("SECTION 7: LOOPING THROUGH LISTS")
print("=" * 50)
print()

# Example 1: Simple loop - print each item
print("Example 1: Print each item in shopping cart")
for item in shopping_cart:
    # The variable 'item' holds one item from the list each time through the loop
    print(f"  - {item}")
print()

# Example 2: Loop with counter
print("Example 2: Print temperatures with day numbers")
day = 1  # Start counting at day 1
for temp in temperatures:
    print(f"  Day {day}: {temp}°F")
    day = day + 1  # Increment the counter
print()

# Example 3: Loop with conditional (if statement inside loop)
print("Example 3: Find hot days (temperature > 75)")
for temp in temperatures:
    # Check if this temperature is hot
    if temp > 75:
        print(f"  Hot day! Temperature: {temp}°F")
print()

# Example 4: Loop and build a new list
print("Example 4: Convert temperatures to Celsius")
celsius_temps = []  # Create empty list to store results
for fahrenheit in temperatures:
    # Formula to convert F to C: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9
    celsius_temps.append(celsius)  # Add converted temp to new list
print(f"Fahrenheit: {temperatures}")
print(f"Celsius: {celsius_temps}")
print()

# ============================================
# SECTION 8: ENUMERATE (MEDIUM-HARD)
# ============================================
# enumerate() gives us BOTH the index AND the item
# This is useful when you need to know the position
# Syntax: for index, item in enumerate(list_name):

print("=" * 50)
print("SECTION 8: ENUMERATE (Index + Item)")
print("=" * 50)
print()

# Example 1: Print items with their index numbers
print("Example 1: Show user roles with index numbers")
for index, role in enumerate(user_roles):
    # enumerate gives us TWO variables: index (position) and role (the item)
    print(f"  Index {index}: {role}")
print()

# Example 2: Start counting at 1 instead of 0
print("Example 2: Task list numbered starting at 1")
for number, task in enumerate(task_list, start=1):
    # start=1 makes enumerate count from 1 instead of 0
    print(f"  Task #{number}: {task}")
print()

# Example 3: Find position of specific item
print("Example 3: Find which day had temperature of 80°F")
for index, temp in enumerate(temperatures):
    if temp == 80:
        print(f"  Temperature 80°F was on day {index + 1} (index {index})")
print()

# ============================================
# SECTION 9: COMBINING CONCEPTS (HARD)
# ============================================
# Now let's combine multiple concepts we learned

print("=" * 50)
print("SECTION 9: COMBINING CONCEPTS")
print("=" * 50)
print()

# Example 1: Loop + Slice + Conditional
print("Example 1: Analyze first 5 stock prices")
first_five_prices = stock_prices[:5]  # Slice: get first 5
for index, price in enumerate(first_five_prices, start=1):  # Enumerate: get index and price
    if price > 150:  # Conditional: check if price is high
        print(f"  Day {index}: ${price} - HIGH PRICE")
    else:
        print(f"  Day {index}: ${price} - normal")
print()

# Example 2: Loop + Append + Pop (Queue simulation)
print("Example 2: Task queue - add and process tasks")
queue = []  # Start with empty task queue
print("Adding tasks to queue...")
queue.append("Send email")
queue.append("Update database")
queue.append("Generate report")
print(f"Queue: {queue}")
print()
print("Processing tasks...")
while len(queue) > 0:  # While loop: continue until queue is empty
    current = queue.pop(0)  # Pop: remove first item
    print(f"  Processing: {current}")
    print(f"  Remaining: {queue}")
print("All tasks completed!")
print()

# Example 3: Nested loop (loop inside a loop)
print("Example 3: Compare all temperatures to find biggest change")
biggest_change = 0
day1 = 0
day2 = 0
# Outer loop: go through each temperature
for i in range(len(temperatures) - 1):  # Stop before last item
    # Inner loop: compare current temp to next temp
    current_temp = temperatures[i]
    next_temp = temperatures[i + 1]
    change = abs(next_temp - current_temp)  # abs() makes it positive
    if change > biggest_change:
        biggest_change = change
        day1 = i + 1
        day2 = i + 2
print(f"  Biggest temperature change: {biggest_change}°F")
print(f"  Between day {day1} and day {day2}")
print()

# Example 4: List comprehension (advanced shortcut)
print("Example 4: List comprehension - create list in one line")
# This is an ADVANCED technique that combines loop + append
# Normal way (what we learned):
squares_normal = []
for price in stock_prices:
    squares_normal.append(price * 2)
# Advanced way (list comprehension):
squares_advanced = [price * 2 for price in stock_prices]
print(f"  Doubled prices (normal loop): {squares_normal}")
print(f"  Doubled prices (comprehension): {squares_advanced}")
print("  Both methods give the same result!")
print()

# ============================================
# SECTION 10: SUMMARY
# ============================================
print("=" * 50)
print("SUMMARY - WHAT WE LEARNED")
print("=" * 50)
print()
print("1. POSITIVE INDEXING: list[0] = first item, list[1] = second item")
print("2. NEGATIVE INDEXING: list[-1] = last item, list[-2] = second to last")
print("3. SLICING: list[start:stop] = get multiple items")
print("4. APPEND: list.append(item) = add item to end")
print("5. POP: list.pop() = remove and return last item")
print("6. LOOPING: for item in list: = go through each item")
print("7. ENUMERATE: for index, item in enumerate(list): = get position and item")
print("8. COMBINING: Use multiple concepts together for complex tasks")
print()
print("Great job! You now know the fundamentals of Python lists!")
