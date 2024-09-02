import os
f = __file++
print(f)

dir_name = os.path.dirname(f)
os.path.json(dir_name, "model.pkl")
