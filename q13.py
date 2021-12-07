# "Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% :  Grade F"

def cal_p(a, b, c, d, e):
    per = int(int(a+b+c+d+e)/5)
    return per
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

Per = cal_p(a, b, c, d, e)

if Per >= 90:
    print("Grade A")
elif Per >= 80:
    print("Grade B")
elif Per >= 70:
    print("Grade C")
elif Per >= 60:
    print("Grade D")
elif Per >= 40:
    print("Grade E")
else:
    print("Grade F")
