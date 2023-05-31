# python3

def read_input():
    choice = input().rstrip()

    if choice == "F":
        with open('tests/06.txt', 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
            return (pattern, text)
    if choice == "I":
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 11 
    m= len(pattern)
    n = len(text)
    
    p_pow = [1] * (n - m + 1)

    for i in range(1, n - m + 1):

        p_pow[i] = p_pow[i - 1] * p
        
    p_hash = sum(ord(pattern[i]) * p_pow[m - i - 1] for i in range(m))
    t_hash = sum(ord(text[i]) * p_pow[m - i - 1] for i in range(m))
    occ = []
    
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+m]:

                occ.append(i)
                
        if i < n - m:
            t_hash = (t_hash - ord(text[i]) * p_pow[m - 1]) * p + ord(text[i + m])
            
    return occ


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

