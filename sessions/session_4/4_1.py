with open(r'data/unsorted_names.txt', 'r') as rf:
    with open(r'data/sorted_names.txt', 'w') as wf:
        wf.write(''.join(sorted(rf.readlines())))
