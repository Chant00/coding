#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create date : 2024/8/7
@Author     : Chant

《大话数据结构》 https://github.com/anliux/Play-With-Data-Structure?tab=readme-ov-file
《大话数据结构》4.9节---栈的应用---四则运算表达式求值
    1. 中缀表达式转后缀表达式（也称逆波兰表达式）
    需要一个stack存运算符，一个output的list存后缀表达式
    cur_char 为数字，则存入后缀表达式
    cur_char 为左括号，则入栈
    cur_char 为右括号，直接出栈，并将出栈字符存入后缀表达式，直到栈顶符号位左括号（左括号也出栈，但不存如后缀表达式）
    cur_char 为操作符，
        若栈空，则入栈
        如栈非空，则判断栈顶字符的优先级，栈顶字符优先级低于该操作符，该操作符入栈。
        否则一直出栈，并将出栈字符存入后缀表达式，直到栈顶操作符的优先级低于该操作符，再将该操作符入栈
        注：中缀表达式遍历完成，栈中可能还有字符未输出，故需要判断栈空。
    https://huaweicloud.csdn.net/63a56f6cb878a54545946fd6.html?dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NjMyNTkwNSwiZXhwIjoxNzIzNTUzMzQ5LCJpYXQiOjE3MjI5NDg1NDksInVzZXJuYW1lIjoid2VpeGluXzM4MzgzODM4In0.Xtqq6k4NheVK4byligycb05JTD90cniKb4b0JHFvFzM


        1、从左到右遍历中缀表达式的每个数字和符号
        2、是数字就输出，是符号则判断与栈顶符号的优先级，
        3、当前符号优先级<=栈顶符号或者当前符号是右括号，栈顶元素依次出栈，将当前符号进栈
        4、遇到右括号才弹出左括号
        原文链接：https://blog.csdn.net/sinat_29158831/article/details/117477691

    2. 计算后缀表达式
    cur_char 为数字，直接入栈
    cur_char 为操作符，连续出栈两次，使用出栈字符与该操作符计算，并将计算结果入栈
    遍历完后缀表达式后，最后栈中数据就是计算结果
"""

sign_priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,  # 左括号优先级最低，只在遇到右括号时弹出
}

sign_priority2 = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    ')': 0,  # 右括号也定义优先级
    '(': -1,  # 左括号优先级最低，只在遇到右括号时弹出
}


def parse_to_postfix_expression(s):
    """
        cur_char 为数字，则存入后缀表达式
        cur_char 为左括号，则入栈
        cur_char 为右括号，直接出栈，并将出栈字符存入后缀表达式，直到栈顶符号为左括号（左括号也出栈，但不存入后缀表达式）
        cur_char 为操作符，
            若栈空，则入栈
            如栈非空，则判断栈顶字符的优先级
                栈顶字符优先级低于该操作符，该操作符入栈。
                否则一直出栈，并将出栈字符存入后缀表达式，直到栈顶操作符的优先级低于该操作符，再将该操作符入栈
        注：中缀表达式遍历完成，栈中可能还有字符未输出，故需要判断栈空。
    """
    sign_stack = []
    postfix = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            sign_stack.append(s[i])
        elif s[i] in '+-*/':
            # 栈为空，或者栈顶优先级低于当前操作符优先级，直接入栈。
            # 否则一直出栈，直到栈顶优先级低于当前操作符的优先级，然后当前操作符入栈。
            # 也可以理解为，当前符号为+-时，如果栈中没有左括号，则弹出所有，否则弹出到左括号为止。优先级的实现方式使得这里的代码更简洁
            while sign_stack and sign_priority[sign_stack[-1]] >= sign_priority[s[i]]:
                postfix.append(sign_stack.pop())
            sign_stack.append(s[i])
        elif s[i] == ')':
            # 右括号，一直出栈直到遇到左括号，并弹出左括号
            while sign_stack[-1] != '(':
                # while sign_stack and sign_stack[-1] != '(':
                postfix.append(sign_stack.pop())
            sign_stack.pop()  # 注意这里多pop一下，将左括号pop丢弃
            # 否则就这样写
            # top = sign_stack.pop()
            # while top != '(':
            #     postfix.append(top)
            #     top = sign_stack.pop()
        else:
            # 解析数字，注意i-=1, 否则就将i+=1挪到每个if里
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            postfix.append(num)
            i -= 1

        i += 1
    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while sign_stack:
        postfix.append(sign_stack.pop())
    return postfix


def parse_to_postfix_expression2(s):
    """
    不使用内部while去解析数字，每次迭代中，在非数字时append数字，
    以及循环结束后，末尾不是符号的话（通过num是否为None来判断），需要再append一次末尾的数字
    """
    sign_stack = []
    postfix = []
    i = 0
    num = None
    while i < len(s):
        if s[i].isdigit():
            if num is None:
                num = 0
            num = num * 10 + ord(s[i]) - ord('0')
        else:
            if num is not None:
                postfix.append(num)
                num = None
            if s[i] == '(':
                sign_stack.append(s[i])
            elif s[i] in '+-*/':
                # 栈为空，或者栈顶优先级低于当前操作符优先级，直接入栈。
                # 否则一直出栈，直到栈顶优先级低于当前操作符的优先级，然后当前操作符入栈。
                # 也可以理解为，当前符号为+-时，如果栈中没有左括号，则弹出所有，否则弹出到左括号为止。优先级的实现方式使得这里的代码更简洁
                while sign_stack and sign_priority[sign_stack[-1]] >= sign_priority[s[i]]:
                    postfix.append(sign_stack.pop())
                sign_stack.append(s[i])
            elif s[i] == ')':
                # 右括号，一直出栈直到遇到左括号，并弹出左括号
                while sign_stack and sign_stack[-1] != '(':
                    postfix.append(sign_stack.pop())
                sign_stack.pop()  # 注意这里多pop一下，将左括号pop丢弃
        i += 1
    if num is not None:
        postfix.append(num)
    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while sign_stack:
        postfix.append(sign_stack.pop())
    return postfix


def parse_to_postfix_expression3(s):
    """定义完整的优先级，仅根据优先级决定是否出栈"""
    sign_stack = []
    postfix = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            sign_stack.append(s[i])
        elif s[i] in '+-*/)':
            # 栈不为空，且栈顶优先级>=当前操作符，一直出栈，直到栈顶优先级<当前操作符
            while sign_stack and sign_priority2[sign_stack[-1]] >= sign_priority2[s[i]]:
                postfix.append(sign_stack.pop())
            if s[i] == ')':  # 右括号时，不入栈，且需要多pop一下，弹出左括号
                sign_stack.pop()
            else:
                sign_stack.append(s[i])
        else:
            # 解析数字，注意i-=1, 否则就将i+=1挪到每个if里
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            postfix.append(num)
            i -= 1

        i += 1
    # 注意：表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while sign_stack:
        postfix.append(sign_stack.pop())
    return postfix


def calculate(s):
    """
    1. 中缀表达式 转 后缀表达式
    2. 计算后缀表达式
    cur_char 为数字，直接入栈
    cur_char 为操作符，连续出栈两次，使用出栈字符与该操作符计算，并将计算结果入栈
    遍历完后缀表达式后，最后栈中数据就是计算结果
    """
    postfix_exp = parse_to_postfix_expression(s)
    stack = []
    for i in postfix_exp:
        if i in {'+', '-', '*', '/'}:
            # -和/有先后顺序，所以先pop出来，num2在前面
            num1 = stack.pop()
            num2 = stack.pop()
            if i == '+':
                stack.append(num2 + num1)
            elif i == '-':
                stack.append(num2 - num1)
            elif i == '*':
                stack.append(num2 * num1)
            elif i == '/':
                stack.append(num2 / num1)
        else:
            stack.append(i)
    return stack[0]


def cal_post_exp(postfix_exp):
    """计算后缀表达式"""
    stack = []
    for i in postfix_exp:
        if i in {'+', '-', '*', '/'}:
            # -和/有先后顺序，所以先pop出来，num2在前面
            num1 = stack.pop()
            num2 = stack.pop()
            if i == '+':
                stack.append(num2 + num1)
            elif i == '-':
                stack.append(num2 - num1)
            elif i == '*':
                stack.append(num2 * num1)
            elif i == '/':
                stack.append(num2 / num1)
        else:
            stack.append(i)
    return stack[0]


s = '(1+(14-1+4/2*2+5*21)-3)+(6+8)'
s = '(1+(14-2*17+1+4/2*2+5*21)-3)+(6/3*2+8-2)'
s = ('14+5*21')
# calculate(s)
print(parse_to_postfix_expression(s))
print(parse_to_postfix_expression2(s))
print(parse_to_postfix_expression3(s))

cal_post_exp(parse_to_postfix_expression(s))
cal_post_exp(parse_to_postfix_expression2(s))
cal_post_exp(parse_to_postfix_expression3(s))

# calculate("10*(8+2)")
# parse_post_exp("10*(8+2)")
# parse_to_postfix_expression("10*(8+2)")
