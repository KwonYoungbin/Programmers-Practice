def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if not i.isalnum() and i != '-' and i != '_' and i != '.':
            new_id = new_id.replace(i, '')

    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5
    if not new_id:
        new_id += 'a'

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id