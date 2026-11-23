openlist = ["(", "[", "{"]
closelist = [")", "]", "}"]

def CheckBalance(mystring):
    stack = []
    for i in mystring:
        if i in openlist:
            stack.append(i)
        elif i in closelist:
            pos = closelist.index(i)
            if (len(stack) > 0 and openlist[pos] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

# Main
string = "{ []{}}"
print(string, '-', CheckBalance(string))

string = "{ []((}"
print(string, '-', CheckBalance(string))

string = "{ []()}"
print(string, '-', CheckBalance(string))

# Graph for Asymptotic Notation
import matplotlib.pyplot as p

p.title('Bracket Matching using Stack - Graph for Asymptotic Notation')
p.xlabel('Inputs Size')
p.ylabel('Steps')

x = list(range(1, 100))
y1 = [1 for y in x]
y2 = [y for y in x]

p.plot(x, y1, 'r', label='O(1)- Space Complexity')
p.plot(x, y2, 'g', label='O(n)- Time Complexity')

p.legend()
p.show()