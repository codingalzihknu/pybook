#!/usr/bin/env python
# coding: utf-8

# # 변수, 값, 표현식, 명령문

# **변수**(variables)는 (컴퓨터 메모리에) 저장된 하나의 값을 가리키는 이름이며,
# 파이썬 프로그래밍 언어의 핵심 기능 중의 하나가 바로 변수가 가리키는 값을 
# 조작하는 것이다.
# 여기서는 다양한 방식으로 **값**(values)을 표현하는 **표현식**(expressions)과, 
# 값을 조작하도록 하는 **명령문**(statements)의 
# 기본 개념을 소개한다.

# ## 변수와 변수 할당

# 변수를 선언하려면 해당 변수가 하나의 값을 가리키도록 하는
# **변수 할당**(variable assignment)을 명령해야 한다.
# 변수 할당 명령문의 형식은 다음과 같다.
# 
# ```python
# 변수 = 값
# ```
# 
# 예를 들어, 아래 세 개의 할당 명령문은 서로 다른 종류의 값을 가리키는 세 개의 변수를
# 선언한다.

# In[1]:


greetings = '안녕하세요!'
num = 17
pi = 3.1415926535897932


# - `greetings` 변수가 가리키는 값은 `'안녕하세요!'` 라는 문장이다.
#     단, 변수 이름과는 달리 값으로 사용되는 문장 또는 단어는 
#     항상 인용부호로 감싸져야 하며, **문자열**(string)이라 불린다.
# - `num` 변수가 가리키는 값은 정수 `17`이다.
# - `pi` 변수가 가리키는 값은 유리수 `3.1415926535897932`이다.
#     유리수는 공식적으로 **부동소수점**(floating points)이라 불린다.
# 
# 선언된 변수는 할당된 값과 동일하게 취급된다.

# In[2]:


greetings


# In[3]:


num + 2


# In[4]:


2 * pi


# 그런데 변수가 가리키는 값을 변경할 수 있다.
# 예를 들어, 변수 `num`에 `18`을 새롭게 할당하면
# 이제는 `17`이 아닌 `18`을 가리킨다.

# In[5]:


num = 18


# In[6]:


num + 2


# ```{admonition} 참고: 파이썬 튜터와 프레임
# 
# 변수 할당은 **컴퓨터 메모리** 상에서 이루어지며,
# 변수와 변수에 할당된 값 사이의 관계는 **프레임**(frames)을 통해 관리된다.
# 컴퓨터 메모리 상에서 일어나는 변화를 직접 눈으로 볼 수는 없다. 
# 하지만 **파이썬 튜터**([https://pythontutor.com/](https://pythontutor.com/))를 
# 이용하면 프레임의 변화를 시각적으로 추적할 수 있다.
# 
# 앞서 변수 세 개의 할당을 실행하면 프레임이 어떻게 변하는지
# [파이썬 튜터: 변수 할당](https://pythontutor.com/visualize.html#code=greetings%20%3D%20'%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94!'%0An%20%3D%2017%0Api%20%3D%203.1415926535897932%0A%0Aprint%28n%20%2B%202%29%0A%0An%20%3D%2018%0A%0Aprint%28n%20%2B%202%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에 
# 접속해서 확인할 수 있다.
# 파이썬튜터 사용법은 다음과 같다.
# 
# * 해당 사이트에 접속해서 코드 확인 및 수정 후 <kbd>Visualize Execution</kbd> 버튼을 누른다.
# * 이후 화면에서 <kbd>Next></kbd> 버튼을 반복해서 누르면서
#     각각의 명령문이 차례대로 실행되는 과정에서 발생하는 프레임의 변화를 확인한다.
#     **Global frame**은 **전역 변수**를 담당하는 **전역 프레임**을 가리킨다.
#     전역 변수에 대한 정의는 나중에 소개한다.
# ```

# **변수의 이름**

# 할당되는 값과 연관된 변수 이름 사용을 권장한다.
# 이름의 길이는 기본적으로 제한이 없지만 아래 제한 사항을 지켜야 한다.
# 
# * 알파벳, 숫자, 밑줄(_, underscore) 등을 조합해서 사용한다.
# * 숫자로 시작할 수 없다.
# * 공백을 사용할 수 없다.
# * 골뱅이 기호 (@), 물결 기호(~)는 사용할 수 없다.
# * 파이썬에서 특별한 역할을 수행하는 **키워드**(keyword)는 사용할 수 없다.

# 허용되지 않는 사례 몇 가지를 살펴보자.

# * 숫자로 시작
# 
#     ```python
#     >>> 3dogs = '강아지 세 마리'
# 
#       File "/tmp/ipykernel_605/3068493907.py", line 1
#         3dogs = '강아지 세 마리'
#          ^
#     SyntaxError: invalid syntax
#     ```

# * 공백 사용
# 
#     ```python
#     >>> big number = 1000000
# 
#       File "/tmp/ipykernel_882/2232769824.py", line 1
#         big number = 1000000
#             ^
#     SyntaxError: invalid syntax
#     ```

# * 키워드 사용: 예를 들어, `False`는 거짓을 나타내는 부울값(Boolean value)이기에 
#     다른 의미로 사용될 수 없다.
# 
#     ```python
#     >>> False = 0
# 
#       File "/tmp/ipykernel_1149/4180392404.py", line 1
#         False = 0
#         ^
#     SyntaxError: cannot assign to False
#     ```

# **파이썬 키워드**

# 파이썬 프로그래밍 언어의 키워드는 다음과 같다.
# 각 키워드의 역할은 차차 하나씩 설명될 것이다. 
# 
# ```python
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise
# ```

# **소문자와 대문자**

# 영어 알파벳의 소문자와 대문자는 엄연히 구분된다.
# 예를 들어, `'hello'`와 `'Hello'`는 서로 다른 단어, 즉 서로 다른 문자열이다.
# 아래 식에서 사용되는 `==` 기호는 양편에 위치한 두 값의 동치(equality) 여부를 판단한다.

# In[7]:


'hello' == 'Hello'


# 또한 변수 이름은 규정은 아니지만 관습적으로 소문자로 시작한다.
# 파이썬의 경우 대문자로 시작하는 이름은 주로 나중에 설명할 **클래스**를 선언할 때 사용한다.

# **한글 사용**

# 한글 단어, 심지어 자음과 모음도 독립적으로 사용할 수 있다.

# In[8]:


헬로 = 'hello'


# 아래 식에서 덧셈 기호(`+`)는 두 문자열과 함께 사용될 때
# 두 문자열을 차례대로 연결하여
# 새로운 문자열을 생성하는 **연결**(concatenation) 연산자로
# 작동한다.

# In[9]:


헬로 + '!'


# In[10]:


ㅎㅔㄹㄹㅗ = '헬로'


# In[11]:


ㅎㅔㄹㄹㅗ + '!'


# ```{admonition} 주의
# :class: caution
# 
# 프로그램을 작성할 때 한글을 변수, 함수 등의 이름으로 사용하는 일은 
# 아직 거의 없으며,
# 전통적으로 영어 등 라틴어 계열의 단어를 사용한다.
# 하지만 변수가 가리키는 값으로는 한글 등 다양한 언어가 기본적으로 활용된다.
# ```

# ## 값과 표현식

# `'안녕하세요!'`, `18`, `3.1415926535897932` 등은 변수에 할당하거나 
# 다른 연산에 사용할 수 있는 값들이다. 
# 반면에 `num`이 하나의 값을 가리키면 `num + 2`도 하나의 값을 가리킨다.
# 또한 `'hello' + ' python'`는 `'hello python'`이라는 문자열을 가리킨다. 

# ### 연산자

# 일반적으로 **연산**은 사칙연산 등 숫자들을 대상으로 계산을 실행하는 
# 기능을 의미한다.
# 하지만 연산은 수 이외에도 문자열 등 다른 종류의 값도 대상으로 삼는다.
# 이렇게 특정 값들을 대상으로 연산을 수행하는 기호를 
# **연산자**(operators)라 하며
# 가장 많이 사용되는 연산자는 다음과 같다.
# 
# * 사칙 연산자: 덧셈(`+`), 뺄셈(`-`), 곱셈(`*`), 나눗셈(`/`)
# * 비교 연산자: 작다(`<`), 크다(`>`), 작거나 같다(`<=`), 크거나 같다(`>=`)
# 
# 위 연산자들이 수 연산에 사용되는 경우 수학에서 배운
# 연산 개념과 동일하다.
# 하지만 수가 아닌 다른 종류의 값들을 대상으로하면 기능이 달라질 수 있다.
# 예를 들어 문자열을 대상으로 하면 덧셈 연산자는 두 개의 문자열을 연결하여
# 새로운 문자열을 생성하는 연결 연산자이다.

# In[12]:


first = '파이썬, '
second = '안녕!'


# In[13]:


first + second


# 그리고 문자열을 정수와 곱하면 해당 문자열을 정수만큼 복제하여 모두 연결한다.
# 반면에 문자열끼리의 곱셈과, 뺄셈 기호(`-`)와 나눗셈 기호(`/`)는 
# 문자열 연산자로 사용되지 않는다.

# In[14]:


'I love python! ' * 4


# **연산자 우선순위**

# 표현식이 나타내는 값은 파이썬 해석기에 의해 계산되며,
# 계산 과정에서 연산자 별로 지정된 우선순위를 따른다. 
# 사칙연산 등 많이 사용되는 수학 함수들의 우선순위는 일반적으로 알려진 것과 동일하다.
# 
# * 괄호 안에 있는 표현식을 가장 먼저 계산한다. 
#     * `2*(3-1) = 2*2 = 4`
#     * `(1+1)**(5-2) = 2**(5-2) = 2**3 = 8`
# * 거듭제곱의 우선순위가 사칙연산보다 높다.
#     * `3**2*2 = (3**2)*2 = 9*2 = 18`
#     * `3*2**2 = 3*(2**2) = 3*4 = 12`
# * 곱셈과 나눗셈을 덧셈과 뺄셈보다 먼저 계산한다. 
#     * `2*3-1 = (2*3)-1 = 6-1 = 5`
#     * `6+4/2 = 6+(4/2) = 6+2 = 8`
# * 곱셈과 나눗셈은 서로 우선순위가 같다.
# * 덧셈과 뺄쎔도 서로 우선순위가 같다.
# * 같은 우선순위를 갖는 연산자가 연속해서 나오면 (거듭제곱을 제외하고) 왼쪽에서 오른쪽으로 계산됩니다. 
#     * `60/2*3 = (60/2)*3 = 30*3 = 90`
# * 거듭제곱이 연속해서 나오면 오른쪽에서 왼쪽으로 계산된다. 
#     * `2**3**2 = 2**(3**2) = 2**9 = 512`

# ### 함수와 표현식

# 함수는 기본적으로 수학에서 다루는 아래와 같은 함수를 가리킨다.

# - $f(x) = ax + b$, 
# - $g(x, y) = a x^2 + b y^2$, 
# - $h(x) = \sin x$,
# - $k(x) = \log x$,
# - $pow(x, y) = x ^ y$

# ```{admonition} 다른 종류의 함수
# :class: tip
# 
# `print()` 함수의 경우처럼 일반 수학 함수와는 다른 종류의 함수도
# 프로그래밍에서 사용된다.
# 파이썬에서 함수를 어떻게 정의하고 활용하는가는 나중에 자세히 다룬다.
# 다만, 여기서는 앞서 설명한 연산자들 또한 함수로 볼 수 있다는 점과
# 각 함수는 사용하는 인자의 종류와 개수가 다르다는 점만을 강조한다. 
# ```

# 변수, 정수, 유리수, 문자열 등을 연산자 또는 함수와 함께 조합하여
# 하나의 값(value)을 표현하도록 작성된 식을 **표현식**이라 부른다.
# 예를 들어 `max()`가 주어진 두 수의 최댓값을 계산하는 함수이고
# `num`이 정수 `5`를 가리키면
# `max(17, num) + 3 / (num + 1)` 는 유리수 `17.5`를 가리키는 표현식이 된다.

# ::::{admonition} 주의
# :class: caution
# 
# 모든 표현식이 하나의 값을 가리키는 것은 아니다. 
# 예를 들어, 곱셈 연산자는 두 개의 인자를 받는데, 
# 문자열을 대상으로 하는 경우 인자 하나는 문자열을, 다른 인자는
# 정수를 사용해야 한다.
# 그렇지 않으면 실행중에 오류가 발생한다.
# 
# ```python
# >>> 'hello' * 'python'
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_355/2897560022.py in <module>
# ----> 1 'hello' * 'python'
# 
# TypeError: can't multiply sequence by non-int of type 'str'
# ```
# ::::

# ## 자료형

# 모든 값들은 각각 고유의 **자료형**에 속한다.
# 예를 들어,
# 
# * `-2`, `-1`, `0,` `1`, `2`, ... 등은 **정수** 자료형(`int`)에 속하고,
# * `3.141592`, `2.71`, `-0.23` 등의 유리수는 **부동소수점** 자료형(`float`)에 속하고,
# * `'강아지'`, `'Hello, World!'`, `'파이썬은 재밌어요!'` 등의 단어 또는 문장은
#     **문자열**(`str`) 자료형에 속한다. 
# 
# 만약 값이 어떤 자료형에 속하는지 모르겠다면 아래와 같이 `type()` 함수를 이용할 수 있다.

# In[15]:


type(-7)


# In[16]:


type(3.141592)


# In[17]:


type('Hello, World!')


# **수 표기 주의사항**

# 수(numbers)를 표기할 때 다음 세 가지 사항들에 주의해야 한다.
# 
# 첫째, `'17'`, `'3.2'` 등은 작은 따옴표(인용부호)로 둘러싸여 있어서
# 수가 아닌 숫자 기호들로 이루어진 문자열이며,
# 연산이 다르게 작동한다. 

# In[18]:


type('17')


# In[19]:


'1.7' + '3.2'


# 둘째, 수를 표기할 때 쉼표(콤마)를 사용하면 다른 의미로 해석된다.
# 예를 들어 `1,000,000` 이라고 입력하면 백만이 아니라 1, 0, 0 세 개의 수를 항목으로 갖는 
# 길이가 3인 튜플 자료형으로 인식된다.
# **튜플**(tuple)은 여러 개의 값을 하나로 묶어서 사용하는 값들의 자료형이며
# 나중에 자세히 다룬다.

# In[20]:


i_am_a_tuple = 1,000,000

print(i_am_a_tuple)


# In[21]:


type(i_am_a_tuple)


# 셋째, 0으로 시작하면 안된다.
# 예를 들어 서울 지역의 우편번호는 0으로 시작하는데
# 우편번호를 정수 자료형으로 지정하면 문제가 발생한다.
# 
# ```python
# # 청와대 우편번호
# >>> zipcode = 03048
# 
#   File "/tmp/ipykernel_1081/521329660.py", line 2
#     zipcode = 03048
#                   ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# ```    
# 
# 사실 우편번호는 구역 식별용으로 사용되기에,
# 고유명사처럼 문자열로 처리하는 게 맞다.

# In[22]:


# 청와대 우편번호
zipcode = '03048'


# ### 변수의 자료형

# 변수의 자료형은 가리키는 값의 자료형으로 지정된다.
# 따라서, 변수에 할당된 값의 자료형이 달라지면 변수의 자료형도 함께 달라진다.

# In[23]:


num = 18
type(num)


# In[24]:


num = 3.14
type(num)


# ## 명령문

# 컴퓨터에 의해 실행될 수 있는 문장을 **명령문**이라 부른다.
# 프로그래밍 언어에 따라 명령문 작성 규칙이 정해져 있다.
# 명령문들을 규칙에 맞게 적절히 구상하여 원하는 프로그램을 구현한다.
# 
# 명령문은 기본 명령문들을 조합해서 생성된다.
# 지금까지 살펴본 기본 명령문들은 다음과 같다.
# 
# * 변수 할당
# * `print`
# * 조건 제어문
# * `while` 반복문
# 
# 위 명령문들만을 이용하여 숫자맞히기 게임을 구현하였다.
# 
# ```python
# print("숫자맞추기 게임에 환영합니다.")
# 
# secret = 9
# guess = -1
# 
# while guess != secret:
#     guess = int(input("0부터 20 사이의 숫자 하나를 입력하세요: "))
#     if guess == secret:
#         print("맞았습니다!")
#     elif guess > secret:
#         print("너무 커요!")
#     else:
#         print("너무 작아요!")
# 
# print("게임 종료!")
# ```

# 예를 들어, 만약에 변수 `x`에 할당된 값이 정수 `3`이라고 가정한다.
# 아래 표는 표현식과 해당 표현식이 표현하는 값, 그리고 값의 자료형 사이의 관계를 보여준다.
# 
# | 표현식 | 값 | 자료형 |
# |---|---|---|
# | `17`  | `17`  | `int` |
# | `"abc"`  | `"abc"`  | `str` |
# | `x`  | `3`  | `int` |
# | `x/2`  | `1.5`  | `float` |
# | `(x/2 - 1) < 0` | `False` | `bool` |
# | `(1, x/2-1, x+x+1)`  | `(1, 0.5, 7)`  | `tuple` |
# | `[x, x*3/2, x**3+1]`  | `[3, 4.5, 28]`  | `list` |
# | `print(x)`  | `None`   | `NoneType` |
# | `int('17')`  | `17` | `int` |
# | `input`  | `input` | `method` |
# 
# * `None`의 자료형은 `NoneType`이다.
# * 마지막 줄에 있는 `input` 함수는 자체로 하나의 값이다. 
#      `input` 함수의 자료형은 `method`라고 한다. 

# ## 주석

# 프로그램 중간중간에 사용된 명령문과 관련된 설명을 적어 놓으면 프로그램을 보다 쉽게 이해할 수 있게 된다.
# 이와 같이 프로그램의 실행과 무관한 설명 문장을 **주석**(comment)이라 부르며,
# 프로그램이 실행될 때 파이썬 해석기에 의해 무시된다.
# 
# * 한 줄 주석: 우물 정 또는 영어로 샵(sharp)이라 불리는 기호(`#`, 샵)로 시작하며
#     `#` 이후의 문장은 실행과정에서 무시된다.

# In[25]:


# speed는 시속을 가리키는 변수이다.

speed = 90 # 속도 단위는 km이다.


# * 여러 줄 주석: 작은 따옴표 세 개(`'''`)로 감싼다.

# In[26]:


print(0)
'''
여러 줄 주석은
이렇게 사용합니다.
'''
print(1)


# ## 프로그램 오류와 디버깅

# 변수 이름으로 `class` 등의 지정어를 사용하거나, `odd~job` 나 `US$`처럼 
# 허용되지 않은 문자나 기호를 포함하는 경우에 파이썬 해석기는 오류를 발생시키며 프로그램의 실행을 멈춘다.
# 예를 들어, 아래와 같이 변수 이름에 공백을 사용하여 실행한 결과를 확인해 보자.

# ```python
#  bad name = 5
# 
# ---------------------------------------------------------------------------
#   File "/tmp/ipykernel_868/870302018.py", line 1
#     bad name = 5
#         ^
# SyntaxError: invalid syntax
# ```    

# 이와 같이 오류가 발생하면 오류의 원인을 찾아 해결해야 한다.
# 이렇게 프로그램의 오류를 찾아 해결하는 과정을 **디버깅**(debugging)이라 부른다.
# 
# 프로그램의 오류는 크게 세 가지 유형이 있다.

# ### 구문 오류

# 변수 이름을 잘못 지정하는 경우 위와 같이 구문 오류(`SyntaxError: invalid syntax`)가 발생한다.
# 구문 오류는 해석기가 프로그램을 실행하기 전에 일종의 문법 검사를 통해 찾아낸다.

# ### 런타임 오류
# 
# 런타임 오류는 구문 오류를 포함하지 않는 프로그램이 실행되는 과정에서 발생하는 오류이다.
# 런타임 오류는 다양한 경우에 발생한다.
# 여기서는 두 가지 경우를 살펴본다.

# #### ZeroDivisionError
# 
# 런타임 에러의 또다는 대표적인 예는 **0으로 나누기 오류**이다.

# ```python
# num = 0
# print(3/num)
# 
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_868/2927743795.py in <module>
#       1 num = 0
# ----> 2 print(3/num)
# 
# ZeroDivisionError: division by zero
# ```

# `ZeroDivisionError` 라고 표시되는데,
# 이는 0으로 나눗셈을 시도하는 경우 발생한다. 
# `num` 변수가 가리키는 값과 3 모두 정수이고,
# 나눗셈 연산자는 정수들을 대상으로 작동하도록 정의되었기 때문에
# `0/num`은 문법적으로 전혀 문제가 없다.
# 하지만 실제로 실행을 하다보면 `num`에 할당된 값이 0이라는 것으로 확인되어
# 오류를 발생시키는 것이다.

# #### NameError
# 
# 예를 들어 아래 코드에는 문법적인 오류가 없다.
# 하지만 실행을 하면 'a_number' 라는 이름이 선언되어 있지 없기 때문에 문제가 발생한다.

# ```python
# a_Number = 327.68
# b = a_number * 3
# 
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_868/830051863.py in <module>
#       1 a_Number = 327.68
# ----> 2 b = a_number * 3
# 
# NameError: name 'a_number' is not defined
# ```

# 자세히 살펴보면 'a_number'와 'a_Number' 둘 중에 하나는 오타임을 알 수 있다.

# ### 의미 오류
# 
# 프로그램이 실행은 되지만 원하는 기능을 지원하지 못한다면 프로그램을 제대로 구현하지 못한 것이다.
# 프로그램은 작동하기 때문에 구문 오류나 런타임 오류와는 달리 원인을 바로 확인하기 어려울 수 있다.
# 이와같은 오류를 **의미 오류**(semantic error)라 부르며,
# 발생원인은 매우 다양하다.
# 
# 수학 문제를 풀다가 계산실수를 하거나, 기호를 다르게 적거나, 문제를 잘못 이해했거나 해서
# 풀 수 있었던 문제를 틀렸던 경험이 있을 것이다.
# 프로그래밍 과정에서도 유사한 실수를 수업이 하게 된다.
# 
# 예를 들어, 아래 프로그램은 두 배 계산 대신에 제곱 계산을 하는 실수를 보여준다.

# In[27]:


num = 3
doubleNum = num**2
print("입력한 값", num, "의 두 배는", doubleNum, "입니다.")


# 두 배하려면 `num*2`를 사용했어야 하는데 실수로 `num**2`를 사용하여서
# 결과적으로 입력한 값의 제곱을 계산하게 된다.
# 수천, 수만 줄로 이루어진 프로그램에서 이런 형식의 오류의 원인을 찾는 일은
# 경우에 따라 잔디밭에서 바늘찾기처럼 어렵거나 불가능할 수 있다.

# ## 연습문제

# 1. 아래 명령문들을 실행하였을 때 무슨 일이 발생하는지를 확인하라.
# 
#     ```python
#     print("Hello World"
#     print("Hello World)
#     print('Hello World")
#     print(+2)
#     print(2++2)
#     print(023)
#     print(21 8)
#     ```
# 
# 1. 변수 선언과 할당 관련 주의해야할 점들을 다룬다.
#     아래 명령문들을 실행하였을 때 무슨 일이 발생하는지를 확인하라.
# 
#     ```python
#     23 = n
#     x = y = 1
#     x = 2;
#     y = x + 1.
#     z = x y
#     ```
# 
# 1. 아래와 같이 변수들이 선언 및 할당되었다고 가정하자.
# 
#     ```python
#     width = 17
#     height = 12.0
#     delimiter = '.'
#     ```
# 
#     다음에 오는 각각의 표현식들에 대해, 표현식의 값과 (표현식의 값이 갖는) 자료형을 확인하라.
# 
#     ```python
#     width//2
#     width/2
#     width/2.0
#     height/3
#     1+2*5
#     delimiter*5
#     ```
# 
# 1. 파이썬을 계산기처럼 사용할 수 있다.
#     1. 반지름이 r인 구의 부피는 $\frac{4}{3} \pi r^3$ 이다. 반지름이 5인 구의 부피는 얼마인가? 
#         (**힌트:** 392.7은 답이 아니다.)
#         
#     1. 책의 정가는 권당 $24,950$원이지만, 각 권당 $10\%$ 의 할인을 받는다고 가정하자.
#         첫 한 권의 운송료는 $2,000$원 이고, 두 권째 부터는 권당 500원을 추가로 내야 한다.
#         60권을 사서 배송을 받고자 하면 얼마를 지불해야 하는가?
#         
#     1. 오전 6:52 에 집을 떠나서, 가볍게 (km당 8분 15초 소요) 1km을 뛰고, 
#         이어서 좀 빠르게 (km당 7분 12초 소요) 3km를 뛴 후, 다시 가볍게 1km를 마저 달린다면, 
#         아침 식사를 위해 집에 돌아오는 시간은 언제인가?
#         
#     1. 만약 10 킬로미터를 43분 30초 만에 달렸다면, 마일당 소요 시간은 얼마인가? 
#         시간당 마일로 계산한 평균 속도는 얼마인가? 
#         (**힌트:** 1마일은 1.61 킬로미터로 계산한다.)
# 
# 1. `print` 함수의 성질을 조사한다. 
#     즉, `print` 함수가 받아들일 수 있는 인자와 리턴값에 대해 알아본다.
#     설명을 예를 들면서 하면 더욱 좋다.
#     (힌트: `help(print)` 명령문을 실행하면 `print` 함수에 대한 기초정보를 확인할 수 있다.)
