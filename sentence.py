sentence="fOnt proCESSOR and ParsER"
split_sen=sentence.split()

lists=[split_sen[0].lower()]
my_word=""
print(split_sen)
for s in range(1, len(split_sen)):
    my_word=split_sen[s].capitalize()
    lists.append(my_word)
    print("" .join(lists))