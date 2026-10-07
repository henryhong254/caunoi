with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_t = 'Từ người xem đến khách trả phí là một hành trình dài.<br>Khách cần bạn dẫn dắt họ đi qua từng chặng để đến đích dễ dàng hơn.'
new_t = 'Từ người xem đến khách trả phí là một hành trình dài.<br>Khách cần bạn dẫn dắt họ đi qua từng trạm để đến đích dễ dàng hơn.'

if old_t in content:
    content = content.replace(old_t, new_t)
else:
    # Maybe whitespace is different
    import re
    pattern = r'Từ người xem đến khách trả phí là một hành trình dài\..*?Khách cần bạn dẫn dắt họ đi qua từng chặng để đến đích dễ dàng hơn\.'
    replacement = r'Từ người xem đến khách trả phí là một hành trình dài.<br>Khách cần bạn dẫn dắt họ đi qua từng trạm để đến đích dễ dàng hơn.'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
