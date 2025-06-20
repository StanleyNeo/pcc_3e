from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)

# .replace()
message = "I really like dogs."
message = message.replace('dog', 'cat')
print(message)