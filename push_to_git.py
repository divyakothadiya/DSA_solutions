import subprocess

def push_to_git():
    msg = input("Enter commit message: ")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", msg])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    push_to_git()
