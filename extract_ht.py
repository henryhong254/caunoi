with open('d:/LP20-caunoi/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s1 = content.find('Bản Đồ Hành Trình')
if s1 == -1:
    s1 = content.find('Hành Trình')
start = content.rfind('<section', 0, s1)
end = content.find('</section>', s1) + 10
with open('d:/LP20-caunoi/temp_ht.txt', 'w', encoding='utf-8') as out:
    out.write(content[start:end])
