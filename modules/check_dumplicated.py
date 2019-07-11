text_list = []
duplicated_examples = []
for example in ['a', 'b', 'c', 'd', 'e', 'f', 'c', 'w', 'g', 'c', 'w', 's', 'j', 'a', 'l']:
    flag = True
    text = ''.join(example)
    for old_text in text_list:
        if text == old_text:
              flag = False
    if flag:
         duplicated_examples.append(example)
         text_list.append(''.join(example))
