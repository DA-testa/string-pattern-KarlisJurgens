# python3

def read_input():
    choice = input().rstrip()

    if choice == "F":
        with open('tests/06.txt', 'r') as file:
            l1 = file.readline().rstrip()
            l2 = file.readline().rstrip()
            F_return = (l1, l2)
            return F_return
    if choice == "I":
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    #test
    p = 31
    m = len(pattern)
    n = len(text)
    p_hash = 0
    t_hash = 0
    power = 1
    occurrences = []

    for i in range(m):
        p_hash += ord(pattern[i]) * power
        t_hash += ord(text[i]) * power
        if i < m-1:
            power = power * p

    for i in range(n-m+1):
        if p_hash == t_hash and pattern == text[i:i+m]:
            occurrences.append(i)
        if i < n-m:
            t_hash = t_hash - ord(text[i]) * power
            t_hash = t_hash * p + ord(text[i+m])

    return [0] if not occurrences else occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


