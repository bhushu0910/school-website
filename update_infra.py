import re

images = [
    './Photo/SchoolSide.jpg',
    './Photo/s9.jpg',
    './Photo/s8.jpg',
    './Photo/a1.jpg',
    './Photo/s7.jpg',
    './Photo/s5.jpg',
    './Photo/s1.jpg',
    './Photo/s2.jpg',
    './Photo/s4.jpg',
    './Photo/s6.jpg'
]

with open('infrastructure.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'https://images\.unsplash\.com/[^"]+')
matches = pattern.findall(content)

for i, match in enumerate(matches):
    if i < len(images):
        content = content.replace(match, images[i], 1)

with open('infrastructure.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated infrastructure.html images.")
