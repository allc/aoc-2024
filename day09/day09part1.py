with open('input.txt') as f:
    data = list(map(int, list(f.read().strip())))
    # data = list(map(int, list(input().strip())))
    files = data[::2]
    freespace = data[1::2]

    i = 0
    files_ = []
    for file in files:
        files_.append((file, i))
        if file > 0:
            i += 1
    files = files_
        

    compact = []
    is_current_file = True
    while len(files) > 0:
        if is_current_file:
            compact.append(files.pop(0))
            is_current_file = False
        else:
            space = freespace.pop(0)
            file = files.pop()
            compact.append((min(space, file[0]), file[1]))
            if space > file[0]:
                freespace.insert(0, space - file[0])
            elif space < file[0]:
                files.append((file[0] - space, file[1]))
                is_current_file = True
            else:
                is_current_file = True

    print(compact)

    checksum = 0
    i = 0
    while len(compact) > 0:
        file = compact.pop(0)
        for j in range(file[0]):
            checksum += (i + j) * file[1]
        i += file[0]

    print(checksum)

