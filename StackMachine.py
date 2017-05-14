'''def StackMachine
		public class StackMachine:
		
    def __init__(self, code):
        self.data_stack = Stack()
        self.return_addr_stack = Stack()
        self.instruction_pointer = 0
        self.code = code
        self.dispatch_map = {...}
        
        def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()
        
    def over(self):
        b = self.pop()
        a = self.pop()
        self.push(a)
        self.push(b)
        self.push(a)

    def read(self):
        self.push(raw_input())
        
#endif //Stack_H call header
'''
'MyLUAEXAMPLE'

'''-- function to search for a item in a list
function Set (list)
    local set = {}
    for key,value in ipairs(list) do
      set[value] = true
    end
    return set
end

-- function get table lenth
function table.getn(table)
    local count = 0
    for k,v in pairs(table) do
        -- print(k)
        count = k
    end
  return count
end

-- function that is called from C++ main
function InfixToPostfix(str)

   -- print(str)

    -- operand vars
    local OperatorMultiply = '*'
    local OperatorDivide = '/'
    local OperatorAdd = '+'
    local OperatorSubtract = '-'
    
    -- list of operators to search
    local Operators = Set {
        OperatorMultiply,
        OperatorDivide,
        OperatorAdd,
        OperatorSubtract,    
    }

    local LeftAssociative = {
        OperatorMultiply,
        OperatorDivide,
        OperatorAdd,
        OperatorSubtract,
        OperatorLParen,
        OperatorRParen,
    }

    -- list to set precedence
    local Precedence = {
        ['*'] = 7,
        ['/'] = 7,
        ['+'] = 5,
        ['-'] = 5,
        ['('] = 1,
        [')'] = 1,
    }

    -- Split string
    local StringSplit = {}
    for i in str:gmatch("[\\s0-9+-/*]+") do
        StringSplit[#StringSplit+1] = i
    end

    local stack = {}
    local output = {}

    -- main loop
    
    
    OPERATORS = "+-*/()"
PRIORITY = {'(' : -1, '+' : 0, '-' : 0, '*' : 1, '/' : 1}
def infixToPostfix(infixExp):
    s = Stack()
    postfixExp = ""
    for ch in infixExp:
        if ch >= 'a' and ch <= 'z':
            postfixExp += ch
        elif ch in OPERATORS:
            if s.empty():
                s.push(ch)
            else:
                if ch == ')':
                    while (not s.empty()) and (s.top() != '('):
                        postfixExp += s.pop()
                    s.pop()
                elif ch == '(':
                    s.push(ch)
                else:
                    while not s.empty() and PRIORITY[s.top()] >= PRIORITY[ch]:
                        postfixExp += s.pop()
                    s.push(ch)
    while not s.empty():
        postfixExp += s.pop()
    return postfixExp

def calculate(postfixExp, varDic):
    s = Stack()
    for ch in postfixExp:
        if ch >= 'a' and ch <= 'z':
            s.push(int(varDic[ch]))
        else:
            r = s.pop()
            l = s.pop()
            res = 0
            if   ch == '+':
                res = l + r
            elif ch == '-':
                res = l - r
            elif ch == '*':
                res = l * r
            elif ch == '/':
                res = l / r
            s.push(res)
    return s.pop()

infixExp = raw_input("Enter a infix experssion:")
if len(infixExp) == 0: infixExp = "a + b * c + (d * e + f) * g"
postfixExp = infixToPostfix(infixExp)
print postfixExp

valStr = raw_input("Enter the values of the variables:")
if len(valStr) == 0:
    valStr = "a=1,b=2,c=3,d=4,e=5,f=6,g=7"
valDic = eval("dict(%s)" % valStr)
print calculate(postfixExp, valDic)
    
    
    end -- end main for loop

      if stack and stack[table.getn(stack)] == OperatorLParen and OperatorRParen then
        print("Parenthesis do NOT match.")
      end

    -- clean the stack
    while table.getn(stack) ~= 0 do
        q = table.remove(stack)
        output[#output+1] = q
    end

    local StringOutPut = table.concat( output, " " )

   return StringOutPut
end -- InFixToPostFix
'''

import sys

class StackMachine:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     '''def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)'''

operator.add(a, b)
operator.__add__(a, b)
Return a + b, for a and b numbers.

operator.sub(a, b)
operator.__sub__(a, b)
Return a - b.

operator.mul(a, b)
operator.__mul__(a, b)
Return a * b, for a and b numbers.

operator.div(a, b)
operator.__div__(a, b)
Return a / b when __future__.division is not in effect.

operator.mod(a, b)
operator.__mod__(a, b)
Return a % b.

operator.truth(obj)
Return True if obj is true, and False otherwise.