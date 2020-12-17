"""
start
get the numbers of sheets
sheets divided by 5
round answer to next number
output result to user
end
"""


def calculate(sheet):
    answer = (sheet / 5)
    rounded = round(answer, 1)
    print("sheet is: ", sheet) 
    print("the answer is:", rounded)
    print("=====================================")
    return rounded

output = calculate(16)
print("the return statement is:", output)