import os

print(os.environ["PATH"])
print(os.environ.__dict__)
user = os.environ["USERNAME"]
# editor = os.environ["EDITOR"]

print(user)

os.environ["FOO"] = "bar"

print(os.environ['FOO'])