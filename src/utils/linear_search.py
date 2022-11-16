

def linear_search(data: list, value: any) -> int:
    for i, v in data:
        if v == value:
            return i
    return -1

