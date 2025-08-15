f = open("Data.txt", "a")

#Write to the file
f.write("\nHello brother")

#Close the file
# f.close()

f = open("Data.txt", "r")

# Display file content
print(f.read())

# Close the file
f.close()