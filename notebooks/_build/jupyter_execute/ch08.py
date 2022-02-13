#!/usr/bin/env python
# coding: utf-8

# # 조건문

# 특정 조건의 성립여부에 따라 다른 일을 실행하게 만드는 명령문이 
# **조건문**<font size="2">conditional statement</font>이다.
# 조건문의 가장 간단한 형식은 다음과 같다.
# 
# ```python
# if x < 0:
#     print('x는 음수')
# ```
# 
# 위 조건문이 실행되는 순간 변수 `x`가 가리키는 값이 0보다 작으면 `'x는 음수'` 
# 라는 문장을 출력하고,
# 그렇지 않으면 다음 명령문으로 넘어간다. 
# 
# 키워드 `if` 다음에 나온 `x < 0`이 **조건**<font size="2">condition</font>이며
# 참 또는 거짓을 가리키는 부울 표현식<font size="2">boolean expression</font>이 사용된다.
# 조건이 참일 때만 들여쓰기와 함께 작성된 명령문, 
# 즉 조건문의 본문이 실행된다.
# 
# 조건문의 본문은 임의의 명령문이 사용될 수 있으며 비어둘 수 없다.
# 조건문의 본문을 비워 둔 다음에 나중에 다시 살펴보고자 하는 경우
# 아무 것도 하지 말고 지나가라는 의미의 `pass` 명령문을 사용하곤 한다.
# 
# ```python
# if x < 0:
#     pass          # 음수인 경우 할 일을 나중에 추가할 것!
# ```

# ## 부울 표현식

# **부울 표현식**<font size="2">boolean expression</font>은
# `True` 또는 `False`를 가리키는 표현식이다.
# 예를 들어, 두 값을 동치성 여부를 판단하는 연산자 `==`를
# 이용한 부울 표현식은 다음과 같다.

# In[1]:


5 == 4 + 1


# In[2]:


3 + 2 ==  3 * 2


# :::{admonition} `==` 대 `=`
# :class: warning
# 
# 등호 기호가 하나인 경우와 두 개인 경우가 완전히 다름에 주의해야 한다.
# 등호 기호 두 개는 동치 여부를 판단하는 비교 연산자임 반면에
# 하나의 등호 기호는 변수 할당에 사용된다.
# :::

# `True`와 `False`는 `bool` 자료형에 속하는 유일한 두 개의 값이다.

# In[3]:


type(True)


# In[4]:


type(False)


# ### 비교 연산자

# `==`는 두 값의 동치여부를 판단하는 비교 연산자이다.
# 이외에 다음 비교 연산자가 참, 거짓을 가리키는 부울 표현식에 많이 사용된다.
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
# 그렇지 않으면 `x`의 두 배한 값을 출력하도록 해보자.
# 
# `x`가 짝수인지 여부는 2로 나눈 나머지가 0인지 1인지 여부로 판단할 수 있다.
# `%`가 나머지 연산자이다. 
# 
# ```python
# >>> 21 % 6
# 3
# >>> 21 % 4
# 1
# ```
# 
# 따라서 나머지 연산자를 이용한 다음 조건식이 바로 짝수 여부를 판단한다.
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
# 이제 정리하면 짝수일 때와 홀수일 때 지정된 일을 하도록 하는 명령문은 다음과 같다.
# 
# ```python
# if x % 2 == 0:
#     print(x // 2)
# else:
#     print(x * 2)
# ```
# ::::

# ## 논리 연산자

# There are three **logical operators**: `and`, `or`, and `not`.
# The semantics (meaning) of these operators is
# similar to their meaning in English.  For example,
# `x > 0 and x < 10` is true only if `x` is greater than 0
# and less than 10.
# 
# `n%2 == 0 or n%3 == 0` is true if *either or both* of the
# conditions is true, that is, if the number is divisible by 2 or 3.
# 
# Finally, the `not` operator negates a boolean
# expression, so `not (x > y)` is true if `x > y` is false,
# that is, if `x` is less than or equal to `y`.
# 
# Strictly speaking, the operands of the logical operators should be
# boolean expressions, but Python is not very strict.
# Any nonzero number is interpreted as `True`:

# ```python
# >>> 42 and True
# True
# ```

# This flexibility can be useful, but there are some subtleties to
# it that might be confusing.  You might want to avoid it (unless
# you know what you are doing).

# ## `if ... else ...` 조건문

# 변수 `x`가 가리키는 값이 음수가 아닐 때에는 음수가 아니다 라는 내용을 출력하려면
# 다음과 같이 조건문을 작성한다.
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

# ## Chained conditionals

# Sometimes there are more than two possibilities and we need more than
# two branches.  One way to express a computation like that is a 
# **chained conditional**:

# ```python
# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x and y are equal')
# ```

# `elif` is an abbreviation of ''else if''.  Again, exactly one
# branch will run.  There is no limit on the number of `elif` statements.
# If there is an `else` clause, it has to be
# at the end, but there doesn't have to be one.

# ```python
# if choice == 'a':
#     draw_a()
# elif choice == 'b':
#     draw_b()
# elif choice == 'c':
#     draw_c()
# ```

# Each condition is checked in order.  If the first is false,
# the next is checked, and so on.  If one of them is
# true, the corresponding branch runs and the statement
# ends.  Even if more than one condition is true, only the
# first true branch runs.  

# ## Nested conditionals

# One conditional can also be nested within another.  We could have
# written the example in the previous section like this:

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
