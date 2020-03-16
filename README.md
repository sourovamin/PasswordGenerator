# PasswordGenerator
A simple python script/class to generate password strings (single, bulk or in file) with full characters customization.

Features

    Passwords generaton with full characters control.
    Bulk passwords generation
    Generation of file (csv, txt, etc) with passwords
  
Initialization
```
from pwgtor import PwGtor
pw = PwGtor()
```

Single password (default).
```
pw.single()
```

Single password (with parameters).
Parameters: limit, lowerCase, upperCase, digits, punctuation
```
pw.single([8, 12], True, False, True, False)
```

Bulk password (default).
```
pw.bulk()
```

Bulk passwords (with parameters).
Parameters: number, limit, lowerCase, upperCase, digits, punctuation
```
pw.bulk(10, [10, 16], True, False, True, True)
```

Generate file (default)
```
pw.file()
```

Generate file (with parameters). Parameters: number, filePath, separator, limit, lowerCase, upperCase, digits, punctuation
```
pw.file(50, "list.txt", "\n", [10, 16], True, False, True, True)
```

Generate CSV file
```
pw.file(50, "password.csv", ",")
```
