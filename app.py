
import os

username = os.getenv('USERNAME')

print(f"Hola {username}")

for i in [1,2,3]:
    print(f'{username}' * i)