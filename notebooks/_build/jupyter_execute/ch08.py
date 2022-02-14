#!/usr/bin/env python
# coding: utf-8

# # 조건문

# 특정 조건의 성립여부에 따라 다른 일을 하게 만드는 명령문이 
# **조건문**<font size="2">conditional statement</font>이다.
# 조건문의 가장 간단한 형식은 다음과 같다.
# 
# ```python
# if x < 0:
#     print('x는 음수')
# ```
# 
# 위 조건문이 실행되는 순간 변수 `x`가 가리키는 값이 0보다 작으면 `'x는 음수'` 
# 라는 문장을 출력하고, 그렇지 않으면 다음 명령문으로 넘어간다. 
# 
# 조건문의 헤더<font size="2">header</font>는 
# `if` 키워드와 **조건**<font size="2">condition</font>으로 구성된다.
# 조건은 참 또는 거짓을 가리키는 **부울식**<font size="2">boolean expression</font>으로
# 표현되며
# 조건이 참일 때 조건문의 본문이 실행된다.
# 
# 조건문의 본문에 사용된 명령문은 함수의 본문처럼 들여쓰며
# 비어둘 수 없다.
# 조건문의 본문을 비워 둔 다음에 나중에 다시 살펴보고자 하는 경우
# 아무 것도 하지 말고 지나가라는 의미의 `pass` 명령문을 사용하곤 한다.
# 
# ```python
# if x < 0:
#     pass          # 음수인 경우 할 일을 나중에 추가할 것!
# ```

# ## 부울식

# **부울식**<font size="2">boolean expression</font>은
# `True`와 `False` 두 개의 값중 하나를 가리키는 표현식이다.
# 예를 들어, 두 값을 동치성 여부를 판단하는 연산자 `==`를
# 이용한 부울식은 다음과 같다.

# In[1]:


5 == 4 + 1


# In[2]:


3 + 2 ==  3 * 2


# :::{admonition} `==` 대 `=`
# :class: warning
# 
# 등호 기호가 하나인 경우와 두 개인 경우는 완전히 다르다.
# 등호 기호 두 개 `==` 는 동치 여부를 판단하는 비교 연산자임 반면에
# 하나의 등호 기호 `=` 는 변수 할당에 사용되는 특별한 기호이다.
# :::

# `True`와 `False`는 `bool` 자료형에 속하는 유일한 두 개의 값이다.

# In[3]:


type(True)


# In[4]:


type(False)


# ### 비교 연산자

# `==`는 두 값의 동치여부를 판단하는 **비교 연산자**이다.
# 이외에 다음 비교 연산자가 참, 거짓을 가리키는 부울식에 많이 사용된다.
# 
# ```python
#     x != y       # x와 y가 서로 다른 값을 가리킬 때 참
#     x > y        # x가 y보다 클 때 참
#     x < y        # x가 y보다 작을 때 참
#     x >= y       # x가 y보다 크거나 같을 때 참
#     x <= y       # x가 y보다 작거나 같을 때 참
# ```

# ::::{prf:example}
# :label: exp_comparison
# 
# 변수 `x`가 가리키는 값이 짝수이면 2로 나눈 값을,
# 그렇지 않으면 두 배한 값을 출력하도록 해보자.
# 
# 정수의 짝수 여부는 2로 나눈 나머지가 0 또는 1인지 여부로 판단할 수 있다.
# 파이썬의 나머지 연산자는 `%` 이다.
# 
# ```python
# >>> 21 % 6
# 3
# >>> 21 % 4
# 1
# ```
# 
# 따라서 다음 부울식이 짝수 여부를 판단한다.
# 
# ```python
# x % 2 == 0
# ```
# 
# 반면에 몫을 계산하는 연산자는 `//` 이다.
# 
# ```python
# >>> 27 // 6
# 4
# >>> 27 // 4
# 6
# ```
# 
# 정리하면 짝수일 때와 홀수일 때 지정된 일을 하도록 하는 명령문은 다음과 같다.
# 
# ```python
# if x % 2 == 0:
#     print(x // 2)
# else:
#     print(x * 2)
# ```
# ::::

# ### 논리 연산자

# 논리 연산자를 이용하여 보다 복잡한 부울식을 생성할 수 있다.
# `and`, `or`, `not` 세 개의 논리 연산자가 기본으로 제공되며
# 기능과 사용법은 영어 단어의 일반적인 의미와 유사하다.
# 
# | 연산자 | 기능 | 예제 | 의미 |
# | :---:  | :---: | :---: | :--- |
# |`and` | 논리곱 연산자| `x > 0 and x < 10` | `x`가 0보다 크고 10보다 작음 | 
# | `or` | 논리합 연산자 |`n % 2 == 0 or n % 3 == 0` | `n`이 2의 배수 또는 3의 배수 |
# | `not` | 논리곱 연산자 | `not (x > y)` | x가 y보다 크가 않음 |
# 
# 파이썬이 제공하는 편리 기능 중에 하나로 
# 논리 연산자의 인자로 부울식이 아닌 값이 사용될 수 있다.
# 예를 들어, 0이 아닌 수는 참, 0은 거짓으로 처리된다.

# In[5]:


17 and True


# 이외에 `None`은 거짓, 빈 리스트는 거짓으로 그렇지 않은 리스트는 참으로 등등처럼
# 많은 값들에 대해 비어 있거나 또는 의미가 없는 값은 거짓으로
# 그렇지 않으면 참으로 처리한다.
# 하지만 이런 방식은 코드의 이해를 어렵게 만들 수 있기에 조심해서 사용해야 한다.

# ## `if ... else ...` 조건문

# 변수 `x`가 가리키는 값이 음수가 아닐 때에는 음수가 아니다 라는 내용도 출력하는
# 기능을 추가하려면 다음과 같이 조건문을 작성한다.
# 
# ```python
# if x < 0:
#     print('x는 음수')
# else:
#     print('x는 음수 아님!')
# ```
# 
# 이처럼 조건 제어문의 일반적인 형식은 다음과 같다.
# 
# ```python
# if 조건식:
#     명령문1
# else:
#     명령문2
# ```
# 
# - `명령문1`: 조건식이 참일 때 실행
# - `명령문2`: 조건식이 거짓일 때 실행

# ## `elif` 키워드

# 세 개 이상의 경우를 다루고자 할 경우
# 다음과 같은 형식을 사용한다.
# 
# ```python
# if x < y:
#     print('x가 y보다 작다')
# elif x > y:
#     print('x가 y보다 크다')
# else:
#     print('x와 y가 같다')
# ```

# `elif`는 영어의 ''else if''의 줄임말이며,
# 임의로 많이 사용될 수 있고,
# `else` 는 생략될 수 있지만 사용된다면 항상 마지막에 위치해야 한다.
# `if`와 `elif` 문에 사용된 조건은 위에서 차례대로 확인되어
# 참이되는 경우의 명령문이 실행되며 나머지 경우는 무조건 무시된다.

# 예를 들어 `y`를 5로 나눈 나머지에 따라 다른 명령문을 다음과 같이 지정할 수 있다.
# 
# ```python
# x = y % 5
# 
# if x == 0:
#     print('나머지가 0')
# elif x == 1:
#     print('나머지가 1')
# elif x == 2:
#     print('나머지가 2')
# elif x == 3:
#     print('나머지가 3')
# else
#     print('나머지가 4')
# ```

# `else`를 사용하지 않을 수도 있다.
# 
# ```python
# x = y % 5
# 
# if x == 0:
#     print('나머지가 0')
# elif x == 1:
#     print('나머지가 1')
# elif x == 2:
#     print('나머지가 2')
# elif x == 3:
#     print('나머지가 3')
# elif x == 4:
#     print('나머지가 4')
# ```

# ## 중첩 조건문

# `elif` 키워드는 사실 없어도 된다.
# 예를 들어 크거나, 작거나, 같은 세 가지 경우를 다음과 같이 다룰 수 있다.
# 
# ```python
# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')
# ```

# The outer conditional contains two branches.  The
# first branch contains a simple statement.  The second branch
# contains another `if` statement, which has two branches of its
# own.  Those two branches are both simple statements,
# although they could have been conditional statements as well.
# 
# Although the indentation of the statements makes the structure
# apparent, **nested conditionals** become difficult to read very
# quickly.  It is a good idea to avoid them when you can.
# 
# Logical operators often provide a way to simplify nested conditional
# statements.  For example, we can rewrite the following code using a
# single conditional:

# ```python
# if 0 < x:
#     if x < 10:
#         print('x is a positive single-digit number.')
# ```

# The `print` statement runs only if we make it past both
# conditionals, so we can get the same effect with the `and` operator:

# ```python
# if 0 < x and x < 10:
#     print('x is a positive single-digit number.')
# ```

# For this kind of condition, Python provides a more concise option:

# ```python
# if 0 < x < 10:
#     print('x is a positive single-digit number.')
# ```
