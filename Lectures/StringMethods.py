course_Name = "Communications Engineering"
print(course_Name.upper()) # converts to upper case
print(course_Name.lower()) # converts to lower case
print(course_Name.title()) # converts it to a title
print(course_Name.strip()) # removes white spaces at the start and end

print(course_Name.find("Eng")) # gets the position of substr (Case Sensitive) -1 is returned if not found or incorrect
print(course_Name.replace("C","-")) # replaces the given string
print("programming" in course_Name) # returns false after check
print("programming" not in course_Name) # returns true after check
