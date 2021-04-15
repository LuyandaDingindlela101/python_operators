#   TASK 2
#   Write a program to get the largest number from a list.
max_number = 0
my_numbers = [5,1,3,2,4]

#   WE USE THE FOR LOOP TO RUN THROUGH EACH ITEM(NUMBER) IN THE LIST AND COMPARE IT TO THE max
for current_number in my_numbers:
    #   CHECK IF THE current_number IS LESS THAN THE max
    if current_number > max_number:
        #   IF IT IS, THEN THAT MUST BE THE LOWEST NUMBER SO FAR...UP UNTIL THERE ARE NO MORE NUMBERS
        max_number = current_number

#   PRINT THE max
print("The lowest number in the list is: " + str(max_number))

#   2. Given a list of numbers with duplicates, how would you remove the duplicates so that the list become unique.
new_list = []
my_list = [10,2,45,3,5,7,2,10,45,8,10]

#   FIRST, WE LOOP THROUGH my_list
for current_number in my_list:
    #   HERE, WE CHECK IF THE current_number IS IN THE new_list OR NOT
    #   IF IT IS...THAT WILL MEAN THAT IT IS A DUPLICATE
    if current_number in new_list:
        #   THE break STATEMENT LETS ME BREAK OUT OF THE CURRENT ITERATION OF THE LOOP
        pass
    #   IF IT ISN'T, ADD IT TO THE new_list
    else:
        new_list.append(current_number)

print(my_list)
print(new_list)