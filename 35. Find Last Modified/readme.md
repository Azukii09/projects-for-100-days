# Find Last Modified

## Instruction

Implement a Python function which takes a string path as a parameter and return the last modified file or folder in the given path.


### Example Input 
```
directory = pathlib.Path.cwd()
find_last_modified(directory)
```
### Example Output 

```
Date modified: 2025-02-04 14:55:39.720376, Filename: find_main.py
```


# Hint

- Use pathlib module.
- Use datetime.fromtimestamp for converting to the date
