#!/usr/bin/env python
# coding: utf-8

# (ch:recursion)=
# # 재귀 함수

# 하나의 함수가 실행되는 동안 다른 함수를 호출할 수 있으며 
# 심지어 실행되는 함수 자신을 다시 호출할 수 있다. 
# 예를 들어 아래 `countdown()` 함수의 본문에 현재 정의되고 있는 자신에 대한 호출이 포함되어 있다.

# In[1]:


def countdown(n):
    if n <= 0:
        print('발사!')
    else:
        print(n)
        countdown(n-1)


# `countdown()` 함수의 작동 방식은 다음과 같다.
# 
# - `n` 이 0 이하인 경우: `'발사!'` 출력
# - `n` 이 양의 정수인 경우: `n`을 출력한 다음 바로 `countdown(n-1)` 호출.
#     
# `n` 이 양수인 경우 동일한 함수가 호출되지만 인자가 1적어 지고 결국 `n`이 되어
# 더 이상의 함수 호출이 없어 실행이 멈춘다.
# 예를 들어 `countdown(3)`을 호출하면 다음처럼 실행된다.

# In[2]:


countdown(3)


# 함수 본문에 자신을 호출하는 함수를 기능을 **재귀**<font size="2">recursion</font>라 하며,
# **재귀 함수**<font size="2">recursive function</font>는 재귀를 활용하는 함수이다.

# ## 재귀 함수의 콜 스택

# 재귀 함수의 실행과정 동안 많은 프레임의 생성과 소멸이 발생하여
# 콜 스택의 변화가 경우에 따라 매우 복잡해지기도 한다.
# 아래 그림은 `countdown(3)`을 호출했을 때의 콜 스택의 상태를 스택 다이어그램으로 보여준다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/count_down.jpg" style="width:300px;"></div>

# 예를 들어,
# [PythonTutor: 콜라츠 추측](http://pythontutor.com/visualize.html#code=def%20collatz%28num%29%3A%0A%20%20%20%20if%20num%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20print%28num%29%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20elif%20num%252%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28num,%20end%3D',%20'%29%0A%20%20%20%20%20%20%20%20return%20collatz%28num//2%29%20%2B%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28num,%20end%3D',%20'%29%0A%20%20%20%20%20%20%20%20return%20collatz%28num*3%20%2B%201%29%20%2B%201%0A%20%20%20%20%20%20%20%20%0Acollatz%287%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# 재귀 함수 호출 과정 동안 메모리에서 벌어지는 프레임의 생성과 소멸 과정,
# 즉, 콜 스택의 변화를 살펴볼 수 있다.

# ## 기저 조건과 무한 재귀

# 재귀 함수의 실행이 멈추려면 재귀 호출 과정에서 언젠가는 더 이상 자신을 호출하지 않아야 한다.
# `countdown()` 함수는 `0`과 함께 호출될 때 더 이상 재귀 호출을 하지 않는다. 
# 이렇게 더 이상 재귀 호출이 발생하지 않도록 하는 경우를 
# **기저 조건**<font size="2">base case</font>이라 한다.
# 즉, `countdown()` 함수의 기저 조건은 `n = 0`이다.
# 
# 반면에 아래 함수는 기저 조건을 갖지 않는다. 
# 
# ```python
# def count_infinitely(n):
#     print(n)
#     count_finitely(n+1)
# ```
# 
# `count_infinitely()` 함수를 호출하면 재귀 호출이 무한정 반복됨을 쉽게 알 수 있다.
# 하지만 파이썬을 포함해서 대부분의 프로그래밍 언어는 재귀 호출의 무한 반복을 허용하지 않고
# 언젠가 아래와 같은 오류를 발생시키면서 실행을 중지시킨다. 
# 
# ```python
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in count_infinitely
#   File "<stdin>", line 3, in count_infinitely
#   File "<stdin>", line 3, in count_infinitely
#   [Previous line repeated 992 more times]
#   File "<stdin>", line 2, in count_infinitely
# RecursionError: maximum recursion depth exceeded while calling a Python object
# ```

# :::{admonition} 최대 재귀 한도
# :class: info
# 
# 파이썬은 **최대 재귀 한도**<font size="2">Maximum recursion depth</font>를 정해
# 허용되는 재귀 호출의 최대 반복 횟수를 지정한다. 
# 한도는 파이썬 버전과 운영체제 등에 따라 다를 수 있으며
# 필요에 따라 조정하는 것도 가능하다.
# 
# 사용하는 파이썬의 최대 재귀 한도는 다음 명령문으로 확인할 수 있다.
# ```python
# >>> import sys
# >>> print(sys.getrecursionlimit())
# ```
# :::

# 재귀 함수를 실행해서 무한 반복에 빠지거나 최대 재귀 한도를 벗어났다는
# 오류 메시지가 발생하면 다음 두 가지 사항을 확인해야 한다.
# 
# - 기저 조건이 주어졌는가?
# - 어떠한 경우에도 기저 조건에 다달하는가?
# 
# 하나라도 충족되지 않거나 확인할 수 없다면 해당 재귀 함수의 활용에 매우 
# 주의를 기울여야 한다.

# ## 함수 실행 종료와 `return` 명령문

# 함수의 본문에 함수의 반환값을 지정하는 `return 표현식`이 여러 번
# 사용될 수 있다.
# 예를 들어 짝수이면 0, 홀수이면 1을 반환하는 함수는 다음과 같이 정의한다.

# In[3]:


def even_odd(n):
    if n % 2 == 0:
        return 0
    else:
        return 1


# In[4]:


even_odd(8)


# In[5]:


even_odd(3)


# 파이썬 프로그램은 함수 실행 중에 `return 표현식` 명령문을 만나면
# `표현식`의 값을 반환하면서 동시에 함수의 실행을 멈춘다.
# 따라서 함수 본문에 `return` 명령문이 여러 번 사용되었다 하더라도
# 한 번만 실행되며, 결국 하나의 반환값만 지정된다.
# 
# 재귀 함수에 대해서도 동일하게 적용된다.
# 다음 `countdown_num()` 함수는 카운트 다운 횟수를 반환한다.
# 인자로 0을 사용하면 바로 0을 반환값으로 지정하고
# 이후 명령문을 더 이상 실행하지 않고 바로 종료한다.

# In[6]:


def countdown_num(n):
    if n <= 0:
        return 0
    else:
        print(n, '이(가) 양수인 경우!')
        result = countdown_num(n-1) + 1
        return result


# In[7]:


print('반환값:', countdown_num(0))


# 하지만 `n`이 `0`보다 크면 `countdown_num(n-1)` 이 
# 재귀적으로 호출되어 실행이 종료할 때까지 기다렸다가
# 반환값을 받아 `result`가 가리키는 값을 지정한다.
# 
# `n = 1`이면 재귀 호출이 한 번 발생하며
# 재귀 호출된 `countdown_num(0)`은 `0`을 반환하며 종료된다.
# 따라서 `result = 0 + 1`이 실행되어 최종적으로 `1`을 반환한다.

# In[8]:


print('반환값:', countdown_num(1))


# 일반적으로 `n = k`이면 재귀 호출이 `k-1` 번 발생하며
# 재귀적으로 호출된 역순으로 계산된 값을 반환하며 실행을 종료한다.

# In[9]:


print('반환값:', countdown_num(2))


# In[10]:


print('반환값:', countdown_num(3))


# ## 예제: 계승

# 음이 아닌 정수 $n$이 주어졌을 때 1부터 $n$ 까지의 곱을 $n$의 계승 또는 
# 팩토리얼<font size="2">factorial</font>이라 하고 $n!$로 표시한다. 
# 
# $$
# \begin{align*}
# 0! & = 1 \\
# n! & = n \, (n-1)!\quad\text{단, $n>0$.}
# \end{align*}
# $$
# 
# 계승을 계산하는 함수 `factorial()` 을 재귀로 구현할 수 있다.
# 
# - 기저 조건은 `n == 0`이고, 1을 반환한다. 
# - `n`이 0보다 크면 `(n-1)`의 계승과 `n`을 곱합 값을 반환한다.

# In[11]:


def factorial(n):
    if n == 0:                            # 기저 조건
        return 1
    else:
        recursion_step = factorial(n-1)   # (n-1)의 계승
        result = n * recursion_step
        return result


# ## 예제: 피보나치 수열

# **피보나치 수열**<font size="2">Fibonacci sequence</font>은 
# 처음엔 1과 1로 시작한 후에 이후의 항목은 이전 두 개의 항목의 합으로 생성된다.
# 
#     1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 
# 피보나치 수열의 두 항목의 관계 점화식은 다음과 같다.
# 
# $$
# \begin{align*}
# f_0 & = 1 \\
# f_1 & = 1 \\
# f_n & = f_{n-1} + f_{n-2} \quad \text{단, $n \ge 2$.}
# \end{align*}
# $$

# 점화식이 알려진 수열의 $n$ 번째 항목을 생성하는 
# 함수는 기본적으로 재귀로 쉽게 구현할 수 있다.
# 피보나치 수열의 `n` 번째 값을 구하는 함수는 다음과 같다.

# In[12]:


def fibonacci(n):
    if n == 0:
        return 1
    elif  n == 1:
        return 1
    else:                                        # n >= 2 인 경우
        return fibonacci(n-1) + fibonacci(n-2)


# 피보나치 수열의 처음 10개 항목은 다음과 같다.

# In[13]:


for n in range(10):
    print(fibonacci(n), end=', ')

print('...')


# :::{admonition} 인덱스의 시작
# :class: info
# 
# 프로그래밍에서는 관습적으로 순서를 1번부터가 아닌 0번부터 시작한다. 
# 따라서 피보나치 수열의 0번과 1번 값이 1, 2번 값은 2, 3번 값은 3 등이 된다.
# :::

# ## 예제: 콜라츠 추측

# 독일 수학자 콜라츠(Collatz -> L.)가 1937년에 아래 알고리즘을
# 얼마나 많이 반복하면 최종적으로 숫자 1에 다다를 것인가를 질문했다.
# 
# * 주어진 숫자가 짝수면 2로 나눈다.
# * 주어진 숫자가 홀수면 3배한 후 1을 더한다.
# 
# 실제로 숫자 7부터 시작해서 위 과정을 16번 반복하면 1에 다다른다. 
# 
#     7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#     
# 반면에 숫자 128부터 시작하면 7번만 반복하면 된다.
# 
#     128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1    

# 콜라츠 알고리즘을 재귀 함수로 구현할 수 있다.
# 
# - 기저 조건: `num == 1`
# - `num % 2 == 0`: 짝수인 경우. 2로 나누기
# - 기타<font size="2">else</font>: 홀수 인 경우. 3배 더하기 1.

# In[14]:


def collatz(num):
    if num == 1:                        # 기저 조건
        print(num)
    elif num % 2 == 0:                  # 짝수인 경우
        print(num, end=' -> ')
        collatz(num//2)
    else:                               # 홀수인 경우
        print(num, end=' -> ')
        collatz(num*3 + 1)


# In[15]:


collatz(7)


# In[16]:


collatz(128)


# In[17]:


collatz(129)


# 재귀 호출 횟수를 반환값으로 지정할 수 있다.
# 
# - `n == 1`: 재귀 호출 없음. 0 반환.
# - 짝수인 경우: 2로 나눈 값에 대한 재귀 호출 횟수 더하기 1
# - 홀수인 경우: 세 배 더하기 1에 대한 재귀 호출 횟수 더하기 1

# In[18]:


def collatz_count(num):
    if num == 1:                        # 기저 조건
        return 0
    elif num % 2 == 0:                  # 짝수인 경우
        return collatz_count(num//2) + 1
    else:                               # 홀수인 경우
        return collatz_count(num*3 + 1) + 1


# In[19]:


print(collatz_count(7), "회")


# In[20]:


print(collatz_count(128), "회")


# In[21]:


print(collatz_count(129), "회")


# 앞서 보았듯이 처음 시작하는 값이 작다고 해서 반드시 먼저 끝나는 것이 아니다.
# 이처럼 시작 값이 정해졌을 때 언제 위 1에 다다르며 종료하는지 알려지지 않았다.
# 반면에 지금까지 테스트한 모든 자연수에 대해 콜라츠 알고리즘은 
# 언젠가는 1에 다다르며 종료하였다.
# 즉, 콜라츠 알고리즘이 모든 수에 대해 언젠가는 1에 다다르며 정지한다라는 주장이
# 아직 증명도 부정도 되지 않고 있다.
# 이렇게 증명도 부정되 되지 않은 콜라츠의 주장을 
# **콜라츠 추측**<font size="2">Collatz conjecture</font>
# 이라 부른다.

# ## 영화 감독 봉준호

# 봉준호 영화 감독의 영화를 담고 있는 리스트가 아래와 같이 있다.

# In[22]:


movie_Bong = ["기생충", 2019, ["설국열차", 2013, ["살인의 추억", 2003]]]


# 위 리스트는 3중이다. 리스트 안에 리스트, 또 리스트 안에 리스트.
# 이제 아래와 같이 모든 항목을 나열하고자 한다.
# 
# ```
# 기생충
# 2019
# 설국열차
# 2013
# 살인의 추억
# 2003
# ```

# In[23]:


for item in movie_Bong:
    print(item)


# 그런데 위와 같이 하면 중첩으로 되어 있는 영화들을 제대로 풀어헤칠 수 없다.
# 2중 `for` 반복문을 활용해보자.
# 
# **주의:** 아래 코드에서 `isinstance(item, list)`는 `item` 변수가 가리키는 항목이 
# 리스트 자료형 여부를 확인한다.

# In[24]:


for item in movie_Bong:
    if isinstance(item, list):
        for itemN in item:
            print(itemN)
    else:
        print(item)


# 여전히 삼중 리스트의 모든 항목을 나열하진 못한다. 
# 3중 `for` 반복문을 활용해보자.

# In[25]:


for item in movie_Bong:
    if isinstance(item, list):
        for itemN in item:
            if isinstance(itemN, list):
                for itemNN in itemN:
                    print(itemNN)
            else:
                print(itemN)
    else:
        print(item)


# 그런데 프로그램을 이렇게 구현하면 안된다.
# 만약에 영화목록이 4중, 5중으로 구성된 리스트로 작성되었다면
# 위 프로그램은 4중, 5중 `for` 반복문으로 수정해야 하고,
# 그러면서 프로그램의 길이와 복잡도가 기하급수적으로 증가하기 때문이다.
# 
# 처리해야 하는 데이터에 따라 프로그램이 수정되거나 복잡도가 증가하지 않는 
# 프로그램을 구현해야 한다. 
# 
# 다시 한 번 위 세 개의 프로그램을 살펴보자. 
# 세 개의 프로그램은 사실상 아래 명령문을 반복해서 사용한다. 
# 
# ```python
# for 항목 in 리스트:
#     if isinstance(항목, list):
#         명령문
#     else:
#         print(항목)
# ```
# 
# 위 명령문은 리스트의 항목이 또 다른 리스트이면 그 리스트의 항목들을 
# 대상으로 동일한 확인작업을 수행하며,
# 더 이상 리스트가 다른 리스트의 항목으로 포함되지 않을 때 까지 반복된다.
# 즉, 모든 중첩 리스트가 해체될 까지 리스트 여부를 반복하며, 
# 리스트가 아니면 해당 항목을 화면에 출력한다.
# 
# 이런 반복작업을 **재귀**(recursion)라 부르며,
# 반복되는 작업에 이름을 주면, 위 세 개의 코드를 하나의 함수로 정의할 수 있다.
# 예를 들어, 아래와 같이 앞서 언급된 명령문에 `printItems`이란 이름을 주어 함수로 정의해보자.

# In[26]:


def printItems(aList):
    for item in aList:
        if isinstance(item, list):
            printItems(item)
        else:
            print(item)


# `printItems` 함수는 좀 이상하다. 
# 정의가 끝나지 않았는데 자신을 자신 본체에서 사용한다. 
# (4번 줄 참조)
# 
# 실제로 `printItems` 함수를 호출하면 실행과정 중에
# 자신을 또다시 호출한다. 
# 단, 사용되는 인자가 다르며, 애초에 사용된 리스트의 항목이면서
# 또다른 리스트가 인자로 사용된다.
# 이런 함수를 자기 자신을 호출한다는 의미로 **재귀함수**(recursive function)라 부른다. 
# 
# 사실 임의로 중첩된 리스트를 인자로 받아도 중첩을 모두 풀어버린다.

# In[27]:


printItems(movie_Bong)


# ## 연습문제 

# 1. `printItems` 수정하여 `movie_Bong`에 포함된 항목들을 아래와 같이 
#     출력하도록 하는 `printItems2` 함수를 구현하라.
# 
#         기생충
#         2019
#             설국열차
#             2013
#                 살인의 추억
#                 2003
# 
#     **힌트**
#     * `printItems` 함수의 인자를 두 개로 수정한다. 
#         하나는 리스트의 인자를 다루며, 다른 하나는 들어쓰기 정도를 다루는 
#         인자를 하나 받는다.
#         
#         ```python
#         def printItems2(aList, level):
#         명령문
#         ```
# 
#     * 위에서 `level` 매개변수의 인자는 탭키를 사용하는 횟수를 나타내도록 한다. 
#         그러면 `printItems2(movie_Bong, 0)`을 실행하면 원하는 결과가 나와야 한다.
#     * 탭 출력은 `print('\t')`를 이용하면 된다.
#     <br><br>
# 1. 위 과제에서 구현한 `printItems2` 함수를 아래와 같이 수정하라.
#     * 인자수를 세 개로 늘린다.
# 
#         ```python
#         def printItems3(aList, level, indent=False):
#             명령문
#         ```
# 
#     * `indent` 매개변수의 키워드인자 값이 `True`이면 연습4에서 처럼 들여쓰기를 하고, 
#         `False`이면 들여쓰기를 하지 않아야 한다.
#     <br><br>
# 1. `printItems` 함수를 재귀가 아닌 `while` 함수를 이용하여 구현하라.
# 
#     **힌트:** `while` 반복문에 사용되는 조건식을 선택하는 게 핵심이다.
#     재귀로 구현된 함수로부터 이에대한 힌트를 얻을 수 있다.
