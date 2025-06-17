import os

def create_solution(name):
    path = f"solutions/{name}.py"
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(f"# Solution: {name}\n\ndef {name}():\n    pass\n")
        print(f"{name}.py created successfully.")
    else:
        print(f"{name}.py already exists.")

if __name__ == "__main__":
    name = input("Enter new solution file name: ")
    create_solution(name)
