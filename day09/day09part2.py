with open('input.txt') as f:
    data = list(map(int, list(f.read().strip())))

    position_i = 0
    file_i = 0
    is_current_file = True
    files = []
    freespace = []
    for d in data:
        if is_current_file:
            if d > 0:
                files.append((d, position_i, file_i))
                file_i += 1
            is_current_file = False
        else:
            if d > 0:
                freespace.append((d, position_i))
            is_current_file = True
        position_i += d
        
    print(files)
    print(freespace)

    # merge freespace
    print('Merging freespace')
    freespace_ = [freespace.pop(0)]
    while len(freespace) > 0:
        space = freespace.pop(0)
        if freespace_[-1][1] + freespace_[-1][0] == space[1]:
            freespace_[-1] = (freespace_[-1][0] + space[0], freespace_[-1][1])
        else:
            freespace_.append(space)
    freespace = freespace_
    print(freespace)

    print('Do stuff')
    result = []
    while len(files) > 0:
        file = files.pop()
        for i in range(len(freespace)):
            space = freespace[i]
            if space[1] > file[1]:
                break
            if space[0] >= file[0]:
                result.append((file[0], space[1], file[2]))
                freespace[i] = (space[0] - file[0], space[1] + file[0])
                file = None
                break
        if file is not None:
            result.append(file)        

    result.sort(key=lambda x: x[1])
    print(result)

    checksum = 0
    for r in result:
        for i in range(r[0]):
            checksum += (r[1] + i) * r[2]
    print(checksum)
