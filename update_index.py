with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80')", "url('./Photo/fullSchool.jpg')")
content = content.replace('src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80"', 'src="./Photo/s5.jpg"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html unsplash links.")
