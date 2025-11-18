import sys

def greet(name):
    print("Hello, World!")
    print(f"Hello, {name}! Welcome to Jenkins and Docker.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Guest"  # default name if none provided
    greet(name)
