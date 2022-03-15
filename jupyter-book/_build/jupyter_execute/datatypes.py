#!/usr/bin/env python
# coding: utf-8

# # 기본자료형

# 일반적으로 **자료형**으로 불리는 
# **데이터 유형**<font size = "2">data type</font>은 사용되는 데이터와
# 관련된 많은 정보를 포함한다.
# 해석기<font size = "2">interpreter</font> 또는 
# 컴파일러<font size = "2">compiler</font>는 
# 자료형에 포함된 정보를 이용하여 해당 데이터의 사용법을 확인한다.
# 이번 장에서는 파이썬 프로그래밍 언어가 제공하는
# 기본 자료형 네 가지를 간단히 살펴본다.
# 
# * 정수
# * 부동소수점
# * 부울값
# * 문자열

# ## 정수

# 일반적으로 알고 있는 -2, -1, 0, 1, 2 등의 정수(자연수, 0, 음의 정수)는 `int` 자료형의 값이다.
# 정수형으로 나타내면 덧셈, 뺄셈, 곱셈, 나눗셈 등의 기본 연산이 가능하다. 
# 정수는 사칙연산, 변수 할당 등에 사용된다.

# In[1]:


1 + 2


# In[2]:


a = 4
a * 2


# `type()` 함수는 주어진 값의 자료형을 확인해준다.

# In[3]:


type(a)


# ## 부동소수점

# **부동소수점**은 유리수, 실수 등을 가리키며 `float` 유형의 값이다.
# 1.2, 0.333, -1.2, -3.7680, 4.0 등은 모두 부동소수점형(`float`)이다.
# 정수와 마찬가지로 사칙연산, 변수 할당 등에 사용된다.
# 
# 부동소수점은 원래 실수를 컴퓨터에서 다루기 위해 개발되었으나 실제로는 유한 소수만을 다룬다.
# 예를 들어 무리수인 원주율 $\pi$의 경우에도 
# 컴퓨터의 한계로 인해 소수점 이하 적당한 자리에서 끊어서 사용한다.

# In[4]:


2.1 + 3.3


# In[5]:


c = 2.1
type(c)


# 정수와의 연산도 가능한데, 이때 정수를 부동소수점으로 취급한다. 
# 예를 들어 3은 3.0으로 처리된다.

# In[6]:


2.3 + 3


# In[7]:


2.3 + 3.0


# ### 정수와 부동소수점 연산

# 파이썬의 기본 연산을 표로 정리하면 아래와 같다. 

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`+`|덧셈| `3 + 4` |`7`|
# |`-`|뺄셈| `7 - 2` | `5`|
# |`*`|곱셈| `2 * 6` | `12`|
# |`/`|나눗셈|`14 / 4`|`3.5`|
# |`**`|지수승|`2 ** 3`|`8`|
# |`//`|몫|`9 // 2`|`4`|
# |`%`|나머지|`3 % 2`|`1`|

# 나눗셈은 항상 부동소수점을 계산한다.

# In[8]:


7 / 3


# 나머지 연산은 부동소수점이 인자로 사용되면 부동소수점을,
# 그렇지 않으면 정수를 계산한다. 

# In[9]:


3.0 + 2


# In[10]:


2 ** 3


# In[11]:


9 ** 0.5


# 몫과 나머지 연산도 동일하다. 

# In[12]:


-7 // 3


# In[13]:


-7 % 3


# In[14]:


-7.0 // 3


# In[15]:


-7 % 3.0


# :::{admonition} 참고 
# :class: info
# 
# 몫과 나머지 연산은 초등학교에서 배운 것과 동일하다.
# 즉, `(a // b) * b + (a % b)` 를 계산하면 정확하게 `a` 가 된다.
# 
# ```python
# >>> -7 == (-7 // 3) * 3 + (-7 % 3)
# True
# :::

# ## 문자열

# **문자열**<font size="2">string</font>은 문자 기호로 이루어진 단어, 문구 등을 가리킨다.
# 키보드에 포함된 영문 알파벳, 한글 자음과 모음 등을 기본적으로 사용한다.
# 문자열은 세 가지 방식으로 작성될 수 있다.

# **작은따옴표 활용**

# In[16]:


s = '안녕하세요.'
print(s)


# **큰따옴표 활용**

# In[17]:


s = "안녕하세요."
print(s)


# **연속된 세 개의 작은 또는 큰따옴표 활용**
# 
# 여러 줄로 이루어진 문자열 작성에 사용된다.

# In[18]:


s = '''안녕.
잘 지내?'''

print(s)


# In[19]:


s = """안녕.
잘 지내?"""

print(s)


# 스페이스와 탭을 활용해서 생성된 여백<font size="2">white space</font>도 문자열로 처리된다.

# In[20]:


s = '''안녕.
    잘 지내?'''

print(s)


# In[21]:


s = """안녕.
    잘 지내?"""

print(s)


# :::{admonition} 유니코드 문자
# :class: info
# 
# 키보드 상에 존재하지 않는 다른 기호나 문자도 **유니코드**<font size="2">Unicode</font> 
# 형식으로 지원된다.
# 유니코드는 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 
# 표준화된 체계이다.
# 대표적으로 서유럽 언어에서 많이 사용되는 
# &#xE0;, &#xE2;, &#xE7;, &#xE8;,&#xFC; 등 특수 알파벳 등이
# 유니코드로 지원된다.
# 
# 또한 이모티콘도 지원된다. 
# 예를 들어 웃는 얼굴의 이모티콘을 나타내는 문자열은 다음과 같다. 
# 
# ```python
# >>> s = '\U0001f600'
# >>> s
# '😀'
# >>> s * 2
# '😀😀'
# ```
# 
# 유니코드로 지원되는 모든 이모티콘은 [Emoji Charts](https://unicode.org/emoji/charts/emoji-list.html)에서
# 확인할 수 있다. 단, `U+`로 시작하는 부분을 `U000` 으로 대체해서 사용해야 한다. 
# :::

# ### 백슬래시와 이스케이프 문자

# 문자열 자체에 따옴표가 포함되면 조심해야 한다.
# 예를 들어, 작은따옴표가 포함된 문자열을 다음과 같이 지정하면 오류가 발생한다.
# 
# ```python
# >>> s = 'Python's grammar'
#   File "<stdin>", line 1
#     s = 'Python's grammar'
#                 ^
# SyntaxError: invalid syntax
# ```
# 
# 이유는 작은따옴표로 문자열의 시작을 지정했기 때문에
# `Python's` 에 사용된 작은따옴표가 
# 문자열의 끝을 의미하게 되는데
# 이후에도 문자열이 이어지게 되어 결국 문자열의 끝이 불분명해져서
# 구문 오류를 뜻하는 `SyntaxError`가 발생한다.
# 
# 이런 종류의 오류를 방지하는 다양한 방식이 존재하지만,
# 여기서는 **백슬래시**<font size="2">backslash</font> 기호 (`\`)를 
# 따옴표 바로 앞에 추가하는 방식만 소개한다.

# In[22]:


s = 'Python\'s grammar'
print(s)


# :::{admonition} 슬래시 기호(&#x5C;)와 원화 기호(&#x20a9;)
# :class: info
# 
# 백슬래시 키는 키보드의 <kbd>Enter</kbd> 키 바로 위에 위치하는데
# 한글 키보드의 경우 원화 기호 키 <kbd>&#x20a9;</kbd> 가 대신 
# 자리잡고 있을 수 있다.
# 그리고 모니터 화면에도 사용하는 운영체제의 언어 설정에 따라
# 원화 기호(&#x20a9;)와 백슬래시 기호(&#x5C;) 둘 중에 하나로만 보인다.
# 하지만 단순한 언어 설정의 차이일 뿐 기능은 동일하다.
# :::

# 백슬래시는 이처럼 특정 문자와 함께 사용되면 특별한 기능을 갖는
# **이스케이프 문자**<font size="2">escape character</font>를 구성한다.
# 가장 많이 사용되는 이스케이프 문자의 목록은 다음과 같다.
# 
# | 이스케이프 문자 | 의미 |
# | :---: | :---:    |
# | `\'` | 작은따옴표 |
# | `\"` | 큰따옴표 |
# | `\\` | 백슬래시 기호 |
# | `\n` | 줄바꿈 |
# | `\t` | 탭 |

# :::{prf:example}
# :label: exp_backslash
# 
# 예를 들어 백슬래시 두 개를 포함한 문자열을 지정하려면 따라서 
# 네 개의 백슬래시를 사용한다.
# 즉, 백슬래시 문자를 하나의 문자로 표현하려면 항상 짝수 개의 백슬래시가 사용되어야 한다.
# 
# ```python
# >>> print("\\\\")
# \\
# ```
# :::

# ### 문자열 기본 연산

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`+`|이어붙이기| `'Hello ' + 'python'` |`'Hello python'`|
# |`*`|연속 복제| `3 * 'Hello '` | `Hello Hello Hello `|
# | | | `'Hello ' * 3` | `Hello Hello Hello `|

# 덧셈 기호는 두 문자열을 이어붙인다.

# In[23]:


name = "강현"
print("안녕, " + name)


# 문자열 하나와 양의 정수의 연산은 지정된 정수 만큼 문자열을 복제하여 이어붙인다.

# In[24]:


"Hello " * 3


# In[25]:


2 * "Hi "


# 양의 정수가 아니면 빈 문자열로 계산된다.

# In[26]:


"Hello " * 0


# In[27]:


"Hello " * -2


# :::{admonition} 주의
# :class: caution  
# 연산자는 사용되는 인자의 자료형에 민감하다.
# 예를 들어 `2 + 'hello'`는 오류를 발생시킨다. 
# 
# ```python
# >>> 2 + 'hello'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ```
# :::

# ### 화이트 스페이스

# **화이트 스페이스**<font size="2">whitespace</font>는 
# 화면상 보이지 않는 여백을 가리키는 문자를 의미한다.
# `string` 모듈의 `whitespace` 변수가 화이트 스페이스 문자를 모두 포함한다.

# In[28]:


import string

string.whitespace


# `' \t\n\r\x0b\x0c'` 의 맨 왼쪽에는 스페이스 바를 한 번 눌렀을 때
# 발생하는 여백 문자 `' '` 이 위치한다.
# 위 문자열에 포함된 각 화이트 스페이스 기호의 의미는 다음과 같다.

# | 기호 | 설명 |
# | :---: | :---: |
# | `' '`  | 스페이스<font size = "2">space</font>| 
# | `'\t'` | 탭<font size = "2">tab</font>| 
# | `'\n'` | 줄 변경<font size = "2">new line</font>|
# | `\r` | 캐리지 리턴<font size = "2">carriage return</font>|
# | `'\v'` 또는 `'\x0b'` | 수직탭<font size = "2">vertical tab</font>|
# | `'\f'` 또는 `'\x0c` | 폼피드<font size = "2">form feed</font>|

# 이중에 스페이스, 줄 변경, 탭이 가장 많이 사용되며,
# 다른 화이트 스페이스는 여기서는 다루지 않는다.

# In[29]:


print(' 1\n2\t3')


# :::{admonition} `''` 대 `' '`
# :class: info
# 
# 빈 문자열<font size = "2">empty string</font> 
# `''` 는 아무런 문자도 포함하지 않았기 때문에 문자열의 길이 즉, 문자열에 포함된 문자의 개수가 0이다.
# 반면 `' '` 는 눈에 보이지는 않지만 스페이스 여백 하나를 포함하는 문자열이며, 따라서 길이가 1이다. 
# 
# C, 자바 등의 언어에서는 길이가 1인 문자열을 **character** 자료형으로 별도 관리하며,
# 보통 `char` 로 표기한다. 
# 하지만 파이썬은 character 자료형을 제공하지 않는다.
# :::

# :::{prf:example}
# :label: exp_backslash_escape
# 
# 화이트 스페이스가 기능을 발휘하지 않고 그 자체로 문자열에 포함되도록 하려면
# 앞서 언급한 백슬래시 자체를 이스케이프 문자로 표현한다. 
# 
# ```python
# >>> print("Hello\\n World")
# Hello\n World
# 
# >>> print("Hello\\t World")
# Hello\5 World
# ```
# :::

# ### 날 문자열

# **날 문자열**<font size="2">raw string</font>은 
# '가공되지 않은'의 의미를 갖는 영어 단어 *raw* 의 첫 글자인 `'r'` 이
# 추가된 문자열이다. 
# 이스케이프 문자가 날 문자열에 포함되더라도 특별한 기능을
# 발휘하지 못한다.

# In[30]:


print(r"Hello\ World")


# In[31]:


print(r"Hello\n World")


# In[32]:


print(r"Hello\t World")


# ### 문자열 포매팅

# **문자열 포매팅**<font size="2">string formatting</font>은
# 문자열 안에 변수 또는 표현식을 사용하여 변하는 값을
# 반영하여 문자열을 생성하도록 한다.
# 여러 방식이 있지만 여기서는 가장 최신 방법인 
# **f-문자열**<font size="2">f-string</font>을 
# 활용하는 방법을 소개한다.
# f-문자열은 문자열 앞에 `f`를 붙이며, 
# 문자열 안에 임의의 표현식이 중괄호로 감싸여서 사용될 수 있다.

# In[33]:


name = '강현'
age = 3
s = f'{name}이는 {age}살이다.'
print(s)


# In[34]:


s1 = f'{name}이의 동생은 {age - 2}살이다'
print(s1)


# 출력되는 문자열의 길이를 지정하고 좌우로 정렬할 수 있다.

# In[35]:


s = 'hi'


# In[36]:


print(f'{s:<10}')
print(f'{s:>10}')
print(f'{s:^10}')


# 남은 자리를 지정된 문자로 채울 수 있다.

# In[37]:


print(f'{s:+<10}')
print(f'{s:0>10}')
print(f'{s:-^10}')


# 부동소수점의 소수점 이하 자릿수를 지정하려면 `{표현식:.1f}` 와 같은 형식을 사용한다.

# In[38]:


num = 17.123456789

print(f'{num:.1f}')
print(f'{num:.2f}')
print(f'{num:.3f}')


# 전체 자릿수를 지정하려면 `{표현식:3.2f}` 와 같은 형식을 사용한다.

# In[39]:


print(f'{num:15.2f}')


# 좌우 정렬도 가능하다.

# In[40]:


print(f'{num:<15.5f}')
print(f'{num:>15.5f}')
print(f'{num:0>15.5f}')


# ### 문자열과 `input()` 함수

# 사용자의 입력은 `input()` 함수를 사용하여 받을 수 있다.
# 아래와 같이 `input()`을 입력하고 코드를 실행하면, 그 아래에 값을 입력하라는 창이 나온다. 
# 예를 들어 `Hello, python!`을 입력하고 엔터 키 <kbd>Enter</kbd>를 누르면 
# 입력한 내용이 그대로 출력된다.
# 
# ```python
# >>> input()
# Hello, Python!
# 'Hello, Python!'
# ```

# `input()` 함수는 입력받은 내용을 문자열로 반환한다.
# 따라서 변수에 할당하여 사용할 수 있다.
# 
# ```python
# >>> s = input()
# '파이썬 좋아!'
# >>> print('진짜로 ' + name)
# 진짜로 '파이썬 좋아!'
# ```

# 사용자가 숫자를 입력하더라도 문자열로 처리된다.
# 
# ```python
# >>> num = input()
# 17
# >>> type(num)
# <class 'str'>
# ```
# 
# 따라서 입력받은 정수를 연산에 활용하려면 
# 먼저 `int()` 함수 또는 `float()` 함수를 이용하여 정수 또는 부동소수점으로 
# 자료형을 변환해야 한다. 
# 아래 {numref}`%s절 <sec:type_casting>`에서 두 함수를 자세히 소개한다.
# 
# ```python
# >>> int(num) / 3
# 5.666666666666667
# ```

# 문자열 인자를 이용하여 입력사항을 안내할 수 있다.
# 
# ```python
# >>> input_num = input("정수를 입력하세요 : ")
# 정수를 입력하세요 : 23
# >>> print("입력하신 정수는 " + input_num + "입니다.")
# 입력하신 정수는 23입니다.
# ```

# ## 부울값

# 참과 거짓을 의미하는 `True`와 `False`를 
# **부울값**<font size="2">boolean</font>
# 또는 **진리값**이라 한다.
# 부울값은 `bool` 유형을 갖는 **유일한 두 개의 값**이다.

# In[41]:


type(True)


# In[42]:


d = False
type(d)


# **논리식**<font size="2">boolearn expression</font>은
# `True` 또는 `False`를 가리키는 표현식이다. 
# 논리식은 기본적으로 등식, 부등식 등의 **비교 연산자**를 이용하여 표현하며,
# **논리 연산자**를 이용하여 보다 복잡한 논리식을 구성한다.

# ### 비교 연산자

# 비교 연산자는 수, 문자열 등의 크기를 비교할 수 이며
# 다음 연산자를 기본으로 지원한다.
# 
# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`<`|작다|`2 < 1`|`False`|
# |`<=`|작거나 같다|`1 <= 2`|`True`|
# |`>`|크다|`2 > 1`|`True`|
# |`>=`|크거나 같다|`1 >= 2`|`False`|
# |`==`|같다|`3 == 2 * 1`|`False`|
# |`!=`|같지 않다|`1 != '1'`|`True`|

# 두 값의 동치성 여부를 판단하는 `==` 연산자는 
# 자료형이 다르면 무조건 거짓으로 판정한다.
# 하지만 정수는 부동소수점으로 취급하기에 
# 예를 들어 1과 1.0은 동치라고 판정한다.

# In[43]:


1 == 1.0


# 문자열도 비교 연산자를 지원하며
# 사전식 순서 개념을 사용한다.

# In[44]:


'apple' < 'banana'


# 영어 알파벳의 경우 대문자가 소문자보다 작다고 판단한다.

# In[45]:


'apple' < 'Apple'


# ### 논리 연산자

# 영어의 *and*, *or*, *not* 의 개념과 거의(!) 유사하게 작동하는
# 세 개의 논리 연산자를 이용하여 보다 복잡한 논리식을 구현할 수 있다.

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`and`|그리고|`1==2 and 3==2+1`|`False`|
# |`or`|또는|`1==2 and 3==2+1`|`True`|
# |`not`|부정|`not 1==2`|`True`|

# 논리 연산자들 사이의 우선순위는 `not` 이 가장 높고 `and` 와 `or` 는 동등하다.
# 예를 들어
# 
# ```python
# not a > b and b > c
# ```
# 
# 는
# 
# ```python
# (not a > b) and b > c
# ```
# 
# 와는 서로 동치이지만
# 
# ```python
# not (a > b and b > c)
# ```
# 
# 와는 일반적으로 서로 다른 값을 가리킨다.

# :::{prf:example}
# :label: logical_op1
# 
# 세 개의 수 중에서 최댓값을 출력하는 코드는 다음과 같다.
# 
# ```python
# a = 3
# b = 7
# c = -1
# 
# if a > b and a > c:
#     print(a)
# elif a > b and not a > c:
#         print(c)
# elif not a > b and b > c:
#     print(b)
# else:
#     print(c)
# ```
# :::

# :::{prf:example}
# :label: logical_op2
# 
# 세 개의 수가 주어졌을 때 
# 양수가 최소 하나라도 있는 경우에만 `True`를 출력하도록 하는 코드는 다음과 같다.
# 
# ```python
# a = -23
# b = -7
# c = 1
# 
# if a > 0 or b > 0 or not c <= 0:
#     print(True)
# else:
#     print(False)
# ```
# :::

# :::{admonition} 참고 
# :class: info
# 
# `and` 와 `or` 가 자연어의 *and* 와 *or* 와는 조금 다르게 작동한다. 
# 예를 들어, 아래와 같이  `False and 3/0`를 실행하면 `False`로 계산되는데
# 좀 이상하다. 
# 왜냐하면 `3/0` 이 `ZeroDivisionError` 라는 오류를 발생시켜야 할 것으로
# 기대되기 때문이다.
# 
# ```python
# >>> False and 3/0
# False
# ```
# 
# 실제로 `3/0 and False` 를 실행하면 `3/0`을 먼저 확인하기에 오류가 발생한다. 
# 
# ```python
# >>> 3/0 and False
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# ```
# 
# `False and 3/0` 를 실행할 때 오류가 발생하지 않은 이유는 
# `x and y`는 `x`가 참일 때만 `y` 를 확인하기 때문이다.
# `x` 를 먼저 확인해서 거짓으로 판명되면 논리식 전체를 바로 거짓으로 계산한다.
# 반면에 `x or y`는 `x`가 거짓일 때만 `y`를 확인한다.
# 즉, `x`를 먼저 확인해서 참이되면 논리식 전체를 참으로 계산한다.
# 
# :::

# (sec:type_casting)=
# ## 형변환

# `2.3 + 3`을 실행하면 파이썬 해석기<font size="2">interpreter</font>는
# 내부적으로 정수를 부동소수점으로 형변환하는 함수 `float()`를 이용하여
# 정수 `3`을 부동소수점 `3.0`으로 유형을 변환한 후에
# 덧셈을 처리한다. 
# 이렇게 값의 유형을 적절하게 자동 변환하는 기능을 
# **형변환**<font size="2">type casting</font>이라 부른다.

# In[46]:


float(3)


# `float()` 함수 이외에 `int()`, `str()`, `bool()` 등 다양한 형변환 함수가 제공된다.

# :::{admonition} `float` 대 `float()`
# :class: tip
# 
# `float`는 부동소수점 자료형을 가리키기도 하고 
# 형변환 함수를 가리키기도 한다. 
# 여기서는 자료형과 함수 이름을 구분하기 위해 
# 함수는 `int()`, `float()`, `str()` 등처럼
# 함수 이름과 괄호를 함께 사용하는 표기법 관행을 따른다.
# :::

# **`int()` 함수**
# 
# 정수 모양의 문자열 또는 부동소수점을 정수로 변환한다.

# In[47]:


int('5')


# In[48]:


int(4.8)


# `True`와 `False`는 각각 1과 0으로 취급된다.

# In[49]:


int(True)


# In[50]:


int(False)


# **`float()` 함수**
# 
# 유한소수 모양의 문자열 또는 정수 등을 부동소수점으로 변환한다.

# In[51]:


float(7)


# In[52]:


float('7')


# In[53]:


float('7.9')


# :::{admonition} 주의 
# :class: caution  
# `int()`함수의 인자로 문자열을 사용할 때는 그 모양이 정수의 모양을 갖추어야 한다.
# 
# ```python
# >>> int('5.1')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '5.1'
# ```
# 
# `float()` 함수의 문자열 인자는 정수 또는 부동소수점 모양이어야 한다. 
# 
# ```python
# >>> float('5.2a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: could not convert string to float: '5.2a'
# ```
# :::

# **`str()` 함수**
# 
# 임의의 값을 문자열로 변환한다.

# In[54]:


str(6)


# In[55]:


str(7.6)


# In[56]:


str(False)


# **`bool()` 함수**
# 
# 임의의 값을 `True` 또는 `False` 로 변환한다.
# `0`, `0.0`, `''`(빈 문자열) 등처럼 0, 비어 있는 것, 의미 없는 것등은 `False` 로
# 그렇지 않으면 `True` 로 지정한다.

# In[57]:


bool(0)


# In[58]:


bool(2)


# In[59]:


bool(0.0)


# In[60]:


bool(0.01)


# In[61]:


bool('')


# In[62]:


bool('Hello')


# ## 기타 자료형

# 파이썬이 기본으로 제공하는 자료형은 지금까지 살펴 본 정수, 부동소수점, 문자열, 부울값 이외에
# {numref}`%s장 <ch:collections>`에서 자세히 다룰
# 리스트, 튜플, 사전, 집합 등의 
# 모음<font size="2">collection</font> 자료형이 있다.
# 그리고 사용자가 원하면 직접 새로운 자료형을 정의해서 사용할 수 있는 기능을 
# 파이썬이 제공한다.
# 
# 자료형을 직접 정의하는 방법은 나중에 
# {numref}`%s장 <ch:classes>`에서 
# 클래스를 다룰 때 자세히 살펴볼 것이다. 
# 여기서는 판다스<font size="2">Pandas</font> 라는 
# 파이썬 추가 패키지가 제공하는 자료형인 `Timestamp` 를 소개한다.

# ### 날짜와 시간

# 판다스의 `Timestamp` 자료형은 날짜와 시간에 특화된 문자열 자료형으로 생각할 수 있다.
# 하지만 문자열과는 달리 날짜와 시간과 관련된 연산을 지원한다.
# 예를 들어 다음과 같이 1999년 10월 4일과
# 오전 9시 30분을 문자열로 지정해보자.

# In[63]:


date_str = 'October 4, 1999'  # 문자열로 작성된 날짜
time_str = '9:30:00'          # 문자열로 작성된 시간


# :::{admonition} 참고 
# :class: info
# 
# 한글이 아닌 영어식 날짜를 사용하는 이유는 이어서 소개할 `Timestamp` 자료형이 
# 영어만 지원하기 때문이다.
# :::

# 이렇게 문자열로 지정된 날짜와 시간은 일상에서 사용되는 날짜와 시간의 연산에 활용될 수 있다.
# 예를 들어 1999년 10월 4일은 오늘 기준으로 며칠 전인지를 알고 싶거나,
# 오전 9시 30분에서 3시간 15분 뒤는 몇 시 몇 분인지 알고 싶을 때
# 문자열을 이용해서 바로 답을 구할 수 없다. 
# 하지만 판다스의 `Timestamp` 자료형으로 변환하면 일상적인 연산이 가능해진다.
# 
# 판다스 모듈은 관습적으로 `pd` 라는 이름으로 사용되며
# 아래와 같이 불러와야 한다.

# In[64]:


import pandas as pd


# 문자열로 작성된 날짜와 시간을 `Timestamp` 자료형으로 변환하려면
# 다음 방식으로 형변환한다.
# 
# 날짜만 지정되면 시간은 새벽 0시 0분 0초로 설정된다.

# In[65]:


pd.Timestamp(date_str)


# 시간만 지정되면 날짜는 코드가 실행된 날의 정보를 이용한다.

# In[66]:


pd.Timestamp(time_str)


# 날짜와 시간을 모두 지정할 수 있다.

# In[67]:


birthday = date_str + ' ' + time_str
birthday


# In[68]:


date_of_birth = pd.Timestamp(birthday)
date_of_birth


# `Timestamp` 값으로부터 년, 월, 일, 시, 분, 초 정보를 확인할 수 있다.

# In[69]:


date_of_birth.year, date_of_birth.month, date_of_birth.day


# In[70]:


date_of_birth.hour, date_of_birth.minute, date_of_birth.second


# 달과 요일을 영어 표현으로 확인할 수도 있다.
# 1999년 10월 4일은 월요일이었다.

# In[71]:


date_of_birth.day_name(), date_of_birth.month_name()


# 현재 시각을 알고자 하면 `Timestamp` 클래스의 `now()` 메서드를 호출한다.

# In[72]:


now = pd.Timestamp.now()
now


# :::{admonition} 메서드
# :class: info
# 
# **메서드**<font size="2">method</font>는 특정 자료형과
# 함께 사용되는 함수이다.
# {numref}`%s장에서 <ch:collections>`
# 모음 자료형을 설명할 때 다양한 메서드를 살펴볼 것이다.
# :::

# ### 날짜와 시간 연산

# `Timestamp` 자료형은 특정 연산을 지원한다. 
# 예를 들어 나이는 현재 시간과 생일 사이의 차이로 계산된다.

# In[73]:


age = now - date_of_birth
age


# 뺄셈 연산 결과는 `Timedelta` 자료형의 값으로 지정되며
# 일, 시, 분, 초, 마이크로초($10^{-6}$초) 단위로 계산된다. 

# :::{admonition} 델타
# :class: seealso
# 
# 델타<font size="2">delta</font>는 그리스어 알파벳($\Delta$)이지만 증가량 또는 차이를 나타내는 의미로 많이 사용된다.
# :::

# `components` 속성에 차이 내용을 별도로 저장된다.

# In[74]:


age.components


# 차이를 일 단위로 따로 확인할 수 있다.

# In[75]:


age.days


# `Timedelta` 에 저장되는 가장 큰 단위는 년(year)이 아니라 일(day)이다.
# 사실 일 년이 365일이기도 하고 366일 이기도 하기에 년 단위로 계산하면 부정확해진다.
# 실제로 지구의 공전 주기는 약 365.24일이다.

# In[76]:


a_year = 365.24


# 이 정보를 이용하여 나이를 계산하면 다음과 같다.

# In[77]:


age.days / a_year


# 나이를 말할 때 보통 소수점 이하는 버린다.
# 이를 위해 넘파이 모듈의 `floor()` 함수를 사용할 수 있다.

# In[78]:


import numpy as np

np.floor(age.days / 365.24)


# `ceil()` 함수를 이용하여 나이를 올림할 수도 있다.

# In[79]:


np.ceil(age.days / 365.24)


# :::{prf:example}
# :label: exp_timestamp_comparison
# 
# `Timestamp` 자료형의 값들을 서로 크기 비교가 가능하다.
# 예를 들어 생일이 지났는지 여부를 다음과 같이 확인할 수 있다.
# 
# ```python
# # 올해의 생일 날짜
# bday_this_year = pd.Timestamp(now.year,
#                               date_of_birth.month, 
#                               date_of_birth.day)
# bday_this_year
# ```
# 
# ```python
# Timestamp('2022-10-04 00:00:00')
# ```
# 
# 크기 비교 연산자 `>` 를 이용하여 `now` 가 가리키는 값과 비교하면 생일이 지났는지 여부를 
# 알 수 있다.
# 
# ```python
# now > bday_this_year
# ```
# 
# ```python
# False
# ```
# :::

# ## 연습문제

# 참고: [(실습) 기본자료형](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-datatypes.ipynb)
