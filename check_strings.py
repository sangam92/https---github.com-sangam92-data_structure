"""
1662. Check If Two String Arrays are Equivalent

"""

def arraystringsequal(word1,word2):
    s1=''
    s2=''
    s1=s1.join(word1)
    s2=s2.join(word2)

    if s1==s2:
        return True
    else:
        return False

if __name__ == '__main__':
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    output = arraystringsequal(word1,word2)

    print(output)
