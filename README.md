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
 
