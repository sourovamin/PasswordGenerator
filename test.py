from pwgtor import PwGtor

pw = PwGtor()

# Single password generate default
print(pw.single())

# Single password generate with parameters
# Parameters: limit, lowerCase, upperCase, digits, punctuation
print(pw.single([8, 12], True, False, True, False))

# Bulk password generate default
print(pw.bulk())

# Single password generate with parameters
# Parameters: number, limit, lowerCase, upperCase, digits, punctuation
print(pw.bulk(10, [10, 16], True, False, True, True))

# Generate file with passwords default
pw.file()

# Generate txt file with passwords with parameters
# Parameters: number, filePath, separator, limit, lowerCase, upperCase, digits, punctuation
pw.file(50, "list.txt", "   ", [10, 16], True, False, True, True)

# Generate CSV file
pw.file(50, "password.csv", ",")
