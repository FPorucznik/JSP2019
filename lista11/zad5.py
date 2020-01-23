import re
text="PythonExcercises testtestTest"
spacje=re.sub(r"(\w)([A-Z])", r"\1 \2",text)
print(spacje)