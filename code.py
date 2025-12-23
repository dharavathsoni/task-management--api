from pathlib import Path


path = Path("main")
for file in path.glob('*.py'):
    print(file.name)

