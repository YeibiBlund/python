# Exercises:

# 1. Create a list of your favorite foods and assign it to a variable.

# Example:
favorite_foods = ["pizza", "ice cream", "cheeseburgers"]
# 2. Add a food to the beginning and end of the list.

# Example:
favorite_foods = ["pizza", "ice cream", "cheeseburgers"]
favorite_foods.insert(0, "pasta")
favorite_foods.append("sushi")

# 3. Print the list and make sure the new items were added.
print (favorite_foods)

# 4. Print the second item in the list.
print (favorite_foods[1])

# 5. Print the last item in the list.
print (favorite_foods[-1])

# 6. Change the second item in the list to something new.
favorite_foods[1] = "patatas"
print (favorite_foods)

# 7. Remove the last item from the list & print the new list.
favorite_foods.pop(-1)
print (favorite_foods)

# 8. Create a list of numbers from 1 to 10.
numList = list(range(1,11))

# 9. Print the numbers 1 to 5.
print(numList[:5])
# 10. Print the even numbers from the list.
print (numList [1::2])
# 11. Print the odd numbers from the list.
print("Números impares:")
print (numList [::2])
#12. Print the multiples of 5 from the list.
print (numList [4::5])
