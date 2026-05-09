# A few of my favorite movies

movie_list = ["Matyrs", "Blue Velvet","Gummo", "Twin Peaks: Fire Walk With Me", "Emily the Criminal","Buffalo 66", "Eyes Wide Shut" ]

                           
#                                         ~~PRINT STATEMENT~~

print(f"The movie list contains {len(movie_list)} strange and exciting movies") # Returns 7 Movies

yes_or_no = input("Would you like to see the list? (Yes/No) ").lower().strip()
if yes_or_no == ("yes"):
    print(f"Here are my recommendations! {movie_list}")
else:
    print("You wouldn't know good cinema if it smacked you in the face...")

#                                            ~~SORTED LISTS~~
    
print("\n SORTED LISTS")
print("\n ~~~~~~~~~~~~~")

# Sorted List
print(f"[SORTED LIST]: {sorted(movie_list)}")
print(f"[UNSORTED LIST]: {movie_list}")

# The sorted list is in alphabetical order, while the unsorted list is in the original order.
#                                               ~~CONT.~~
movie_list.sort()
print(f"[Alternative sorting for list]: {movie_list}")

#                                            ~~APPENDED LIST~~

movie_list.append("Idiocracy")
print(f"[Appended list]: {movie_list}")