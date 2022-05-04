def find_most_frequency(s):
    if not s or len(s) == 0:
        return None 

    s = s.lower()
    s_dict = {}
    for c in s:
        if c not in s_dict.keys():
            s_dict[c] = 1
        else:
            s_dict[c] += 1
    
    return sorted(s_dict, key = s_dict.get, reverse = True)[0]

if __name__ == '__main__':
    print(find_most_frequency(''))