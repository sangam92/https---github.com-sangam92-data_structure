"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""
dial = {
"2":["a","b","c"],
"3":["d","e","f"],
"4":["g","h","i"],
"5":["j","k","l"],
"6":["m","n","o"],
"7":["p","q","r"],
"8":["s","t","u"],
"9":["w","x","z"]
}

ip =str(input())
print(len(ip))
output =[]
if ip ==1 or len(ip)==0 or len(ip)>3:
    print("Invalid input")
else:
    for i in ip:

        for j in dial.get(i):
            k =dial.get(i) + j
            output.append(k)

print(output)
