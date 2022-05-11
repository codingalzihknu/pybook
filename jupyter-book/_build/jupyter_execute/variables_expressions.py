#!/usr/bin/env python
# coding: utf-8

# # 변수, 값, 표현식, 명령문

# **변수**<font size="2">variable</font>는
# (컴퓨터 메모리에) 저장된 하나의 값을 가리키는 이름이며,
# 파이썬과 같은 명령형 프로그래밍 언어의 핵심 기능 중의 하나가 
# 바로 변수가 가리키는 값을 조작하는 일이다.
# 여기서는 다양한 방식으로 **값**<font size="2">value</font>을 
# 표현하는 **표현식**<font size="2">expression</font>과, 
# 값을 조작하도록 하는 **명령문**<font size="2">statement</font>의 
# 기본 개념을 소개한다.

# ## 변수와 변수 할당

# 변수를 선언하려면 해당 변수가 하나의 값을 가리키도록 하는
# **변수 할당**<font size="2">variable assignment</font>을 명령해야 한다.
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
#     단, 변수 이름과는 달리 값으로 사용되는 단어와 문장은 
#     항상 짝은따옴표 또는 큰따옴표로 감싸져야 하는 
#     **문자열**<font size="2">string</font>이다.
# - `num` 변수가 가리키는 값은 정수<font size="2">integer</font> `17`이다.
# - `pi` 변수가 가리키는 값은 유리수 `3.1415926535897932`이다.
#     유리수는 공식적으로 
#     **부동소수점**<font size="2">floating point</font>이라 불린다.
# 
# 선언된 변수는 할당된 값과 동일하게 취급된다.

# In[2]:


greetings


# In[3]:


num + 2


# In[4]:


2 * pi


# 그런데 변수가 가리키는 값은 변경될 수 있다.
# 예를 들어, 변수 `num`에 `18`을 새롭게 할당하면
# 이제는 `17`이 아닌 `18`을 가리킨다.

# In[5]:


num = 18


# In[6]:


num + 2


# 업데이트된 변수의 값을 동일한 변수 이름을 이용하여 가리키도록 할 수 있다.
# 아래 코드는 변수 `num`이
# 원래 가리키던 값 18의 두 배인 36일 가리키도록 한다.
# 이런 의미에서 변수 할당에 사용되는 기호 `=`는 
# 값이 동일하다<font size="2">equal</font>라는 
# 의미와 전혀 상관이 없음을 기억해야 한다.
# 두 표현식이 동일한 값을 가리키는지 여부를 다루는 기호는 나중에 소개한다.

# In[7]:


num = num * 2
print(num)


# :::{admonition} 파이썬 튜터와 프레임
# :class: info
# 
# 변수 할당은 **컴퓨터 메모리** 상에서 이루어지며,
# 변수와 변수에 할당된 값 사이의 관계는 
# **프레임**<font size="2">frame</font>을 통해 관리된다.
# 
# 컴퓨터 메모리 상에서 일어나는 변화를 직접 눈으로 볼 수는 없다. 
# 하지만 **파이썬 튜터**([https://pythontutor.com/](https://pythontutor.com/))를 
# 이용하면 프레임의 변화를 시각적으로 추적할 수 있다.
# 앞서 변수 세 개의 할당을 실행하면 프레임이 어떻게 변하는지
# [파이썬 튜터: 변수 할당](https://pythontutor.com/visualize.html#code=greetings%20%3D%20'%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94!'%0Anum%20%3D%2017%0Api%20%3D%203.1415926535897932%0A%0Aprint%28num%29%0A%0Anum%20%3D%2018%0Aprint%28num%29%0A%0Anum%20%3D%20num%20%2B%202%0Aprint%28num%29%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에 
# 접속해서 확인할 수 있다.
# 파이썬튜터의 사용법은 다음과 같다.
# 
# * 해당 사이트에 접속해서 코드 확인 및 수정 후 <kbd>Visualize Execution</kbd> 버튼을 누른다.
# * 이후 화면에서 <kbd>Next></kbd> 버튼을 반복해서 누르면
#     각각의 명령문이 차례대로 실행되는 과정에서 발생하는 프레임의 변화를 확인할 수 있다.
# * **Global frame**은 **전역 변수**<font size="2">global variable</font>를 
#     담당하는 **전역 프레임**을 가리킨다.
#     전역 변수에 대한 정의는 나중에 소개한다.
# :::

# **변수의 이름**

# 변수의 이름은 임의로 정할 수 있지만 할당되는 값과 연관된 이름을 사용할 것을 권장한다.
# 또한 아래 제한 사항을 지켜야 한다.
# 
# * 알파벳, 숫자, 밑줄(_, underscore) 등을 조합해서 임의로 조합해서 사용한다.
# * 마침표(.), 연산 기호(+, -, *, /, !, %), 골뱅이 기호(@), 물결 기호(~), 
#     공백<font size="2">space</font> 은 사용할 수 없다.
# * 숫자로 시작할 수 없다.
# * 파이썬에서 특별한 역할을 수행하는 
#     **키워드**<font size="2">keyword</font>는 사용할 수 없다.
# 
#     파이썬 프로그래밍 언어의 키워드는 파이썬 최신 버전 기준으로 총 35개이다.
#     각 키워드의 역할은 필요할 때마다 설명될 것이다. 
# 
#     ```python
#     False      await      else       import     pass
#     None       break      except     in         raise
#     True       class      finally    is         return
#     and        continue   for        lambda     try
#     as         def        from       nonlocal   while
#     assert     del        global     not        with
#     async      elif       if         or         yield
#     ```

# 허용되지 않는 사례 몇 가지를 살펴보자.

# * 숫자로 시작
# 
#     ```python
#     >>> 3dogs = '강아지 세 마리'
#       File "<stdin>", line 1
#         3dogs = '강아지 세 마리'
#          ^
#     SyntaxError: invalid syntax
#     ```

# * 공백 사용
# 
#     ```python
#     >>> big number = 1000000
#       File "<stdin>", line 1
#         big number = 1000000
#             ^
#     SyntaxError: invalid syntax
#     ```

# * 키워드 사용: 예를 들어, `False`는 거짓을 나타내는 
#     부울값<font size="2">Boolean value</font>이기에 
#     다른 의미로 사용될 수 없다.
# 
#     ```python
#     >>> False = 0
#       File "<stdin>", line 1
#         False = 0
#         ^
#     SyntaxError: cannot assign to False
#     ```

# **소문자와 대문자**

# 영어 알파벳의 소문자와 대문자는 엄연히 구분된다.
# 예를 들어, `'hello'`와 `'Hello'`는 서로 다른 단어, 즉 서로 다른 문자열이다.
# 아래 식에서 사용되는 `==` 기호는 양편에 위치한 두 값의 
# 동치<font size="2">equality</font> 여부를 판단한다.

# In[8]:


'hello' == 'Hello'


# 또한 규정은 아니지만 변수 이름은 관습적으로 소문자로 시작한다.
# 파이썬의 경우 대문자로 시작하는 이름은 주로 
# **클래스**<font size="2">class</font>를 선언할 때 사용한다.
# 클래스는 나중에 자세히 다룬다.

# **한글 사용**

# 한글 단어, 심지어 자음과 모음도 독립적으로 사용할 수 있다.

# In[9]:


헬로 = 'hello'


# 아래 식에서 덧셈 기호(`+`)는 두 문자열과 함께 사용될 때
# 두 문자열을 차례대로 연결하여
# 새로운 문자열을 생성하는 
# **연결**<font size="2">concatenation</font> 연산자이다.

# In[10]:


헬로 + '!'


# In[11]:


ㅎㄹ = '헬로'


# In[12]:


ㅎㄹ + '!'


# :::{admonition} 주의
# :class: caution
# 
# 프로그램을 작성할 때 변수, 함수 등의 이름으로 한글을 사용하는 일은 
# 아직 일반적이지 않다.
# 하지만 변수가 가리키는 값으로는 한글 등 다양한 언어가 활용된다.
# :::

# ## 함수와 표현식

# `'안녕하세요!'`, `18`, `3.1415926535897932` 등은 변수에 할당하거나 
# 연산 등에 사용할 수 있는 **값**<font size="2">value</font>이다. 
# 반면에 `num`이 하나의 값을 가리키면 `num + 2`도 하나의 값을 가리키며,
# `'hello' + ' python'`는 `'hello python'`이라는 문자열을 가리킨다.
# 이처럼 값들의 연산, 값과 변수들의 연산 등을 이용하여 새로운 값을 
# 가리키는 식을 **표현식**<font size="2">expression</font>이라 한다.

# ### 연산자

# 일반적으로 **연산**<font size="2">operation</font>은 사칙연산 등 
# 숫자들을 대상으로 하는 **계산 실행**을 의미한다.
# 하지만 연산은 수 이외에도 문자열의 연결 등 다른 종류의 값을 대상으로 실행될 수도 있다.
# 이렇게 특정 종류의 값을 대상으로 계산 실행을 수행하는 기능을 갖춘 기호를
# **연산자**<font size="2">operator</font>라 부르며,
# 가장 많이 사용되는 연산자는 다음과 같다.
# 
# * 사칙 연산자: 덧셈(`+`), 뺄셈(`-`), 곱셈(`*`), 나눗셈(`/`)
# * 비교 연산자: 작다(`<`), 크다(`>`), 작거나 같다(`<=`), 크거나 같다(`>=`)
# 
# 위 연산자들이 수 연산에 사용되는 경우 수학에서 배운
# 연산 개념과 동일하다.
# 하지만 앞서 살펴보았듯이 수가 아닌 다른 종류의 값들을 대상으로하면 기능이 달라질 수 있다.

# In[13]:


first = '파이썬, '
second = '안녕!'


# In[14]:


first + second


# In[15]:


'I love python! ' * 4


# **연산자 우선순위**

# 표현식이 나타내는 값은 파이썬 실행기가 
# 표현식에 사용된 연산자와 연관된 연산을 실행하는 방식으로 계산되며,
# 계산 과정에서 연산자 별로 지정된 우선순위를 고려한다. 
# 사칙연산 등 많이 사용되는 수학 함수들의 우선순위는 일반적으로 알려진 것과 동일하다.
# 
# * 괄호 안에 있는 표현식을 가장 먼저 계산한다. 
#     
#     ```python
#     2*(3-1) => 2*2 => 4
#     (1+1)**(5-2) => 2**(5-2) => 2**3 => 8
#     ```
#     
# * 거듭제곱의 우선순위가 사칙연산보다 높다.
# 
#     ```python
#     3**2*2 => (3**2)*2 => 9*2 => 18
#     3*2**2 => 3*(2**2) => 3*4 => 12
#     ```
#     
# * 곱셈과 나눗셈을 덧셈과 뺄셈보다 먼저 계산한다. 
# 
#     ```python
#     2*3-1 => (2*3)-1 => 6-1 => 5
#     6+4/2 => 6+(4/2) => 6+2 => 8
#     ```
#     
# * 곱셈과 나눗셈은 서로 우선순위가 같다.
# * 덧셈과 뺄쎔도 서로 우선순위가 같다.
# * 같은 우선순위를 갖는 연산자가 연속해서 나오면 (거듭제곱을 제외하고) 왼쪽에서 오른쪽으로 계산됩니다. 
# 
#     ```python
#     60/2*3 => (60/2)*3 => 30*3 => 90
#     ```
#     
# * 거듭제곱이 연속해서 나오면 오른쪽에서 왼쪽으로 계산된다. 
# 
#     ```python
#     2**3**2 => 2**(3**2) => 2**9 => 512
#     ```

# ### 함수

# 함수는 기본적으로 아래와 같이 수학에서 다루는 함수를 가리킨다.
# 
# - $f(x) = ax + b$, 
# - $g(x, y) = a x^2 + b y^2$, 
# - $h(x) = \sin x$,
# - $k(x) = \log x$,
# - $pow(x, y) = x ^ y$

# 언급된 함수 중에서 $\sin$ 와 $\log$, 그리고 제곱근 함수 $\sqrt{\,\,\,}$ 등은 
# `math` 모듈에 포함되어 있다.
# 아나콘다 패키지를 설치한 경우 `numpy` 모듈도 많은 함수를 제공한다.
# 
# 언급된 함수들을 사용하려면 먼저 해당 모듈을 불러와야 한다. 
# 예를 들어 `math` 모듈을 사용하려면 다음과 같이 한다.

# In[16]:


import math


# 그러면 `sin()`, `log()`, `sqrt()` 함수 등을 이용할 수 있다.
# 단, 불러온 모듈 이름과 함께 사용한다.
# 
# - $\sin(\pi/2)$

# In[17]:


# 원주율 
pi = math.pi

math.sin(pi/2)


# - $\sqrt{2}$

# In[18]:


math.sqrt(2)


# - $\log_2(10)$

# In[19]:


math.log(10)


# - $\log_{10}(10)$

# In[20]:


math.log10(10)


# :::{admonition} 다른 종류의 함수
# :class: tip
# 
# `print()` 함수의 경우처럼 일반 수학 함수와는 다른 종류의 함수도
# 프로그래밍에서 사용된다.
# 파이썬 함수의 정의와 활용법은 
# {numref}`%s장 <ch:functions>`에서 자세히 다룬다.
# 여기서는 대신 앞서 설명한 연산자들 또한 함수로 간주된다는 점과
# 함수 인자의 종류와 개수가 함수마다 다르다는 점만을 강조한다. 
# :::

# (sec:representation)=
# ### 표현식

# 앞서 표현식을 연산자와 값을 조합한 식으로 설명하였다.
# 하지만 일반적으로는 연산자 뿐만 아니라 임의의 함수와
# 변수, 정수, 유리수, 문자열 등을 조합하여
# 하나의 값(value)을 표현하도록 작성된 식을 
# **표현식**<font size="2">expression</font>이라 부른다.
# 
# 예를 들어 `max`가 주어진 두 수의 최댓값을 계산하는 함수이고
# `num`이 정수 `5`를 가리키면
# `max(17, num) + 3 / (num + 1)` 는 유리수 `17.5`를 가리키는 표현식이 된다.

# ::::{admonition} 주의
# :class: caution
# 
# 모든 표현식이 하나의 값을 가리키는 것은 아니다. 
# 예를 들어, 곱셈 연산자는 두 개의 인자를 받는데, 
# 문자열을 대상으로 하는 경우 인자 하나는 문자열을, 다른 인자는
# 정수를 사용해야 한다.
# 그렇지 않으면 실행중에 오류가 발생하며
# 이런 이유로 적절한 표현식으로 허용되지 않는다.
# 
# ```python
# >>> 'hello' * 'python'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'str'
# ```
# 
# 동일한 이유로 아래 표현식들도 허용되지 않는다. 
# 
# ```python
# 'Korean' - 'pop'
# 'apple' / 'pie'
# ```
# ::::

# ## 자료형

# 모든 값들은 각각 고유의 **자료형**<font size="2">data type</font>에 속한다.
# 예를 들어,
# 
# * `-2`, `-1`, `0,` `1`, `2`, ... 등은 **정수** 자료형 `int`에 속하고,
# * `3.141592`, `2.71`, `-0.23` 등의 유리수는 **부동소수점** 자료형 `float`에 속하고,
# * `'강아지'`, `'Hello, World!'`, `'파이썬은 재밌어요!'` 등의 단어 또는 문장은
#     **문자열** 자료형 `str`에 속한다. 

# ### `type()` 함수

# `type()` 함수는 인자의 자료형을 확인해준다.

# In[21]:


type(-7)


# In[22]:


type(3.141592)


# In[23]:


type('Hello, World!')


# **숫자 표기 주의사항**

# 수<font size="2">number</font>를 표기할 때 다음 세 가지 사항들에 주의해야 한다.
# 
# 첫째, `'17'`, `'3.2'` 등은 작은따옴표로 둘러싸여 있어서
# 수가 아닌 숫자 기호들로 이루어진 문자열이며,
# 연산이 다르게 작동한다. 

# In[24]:


type('17')


# In[25]:


'1.7' + '3.2'


# 둘째, 수를 표기할 때 쉼표(콤마)를 사용하면 다른 의미로 해석된다.
# 예를 들어 `1,000,000` 이라고 입력하면 백만이 아니라 1, 0, 0 세 개의 수를 항목으로 갖는 
# 길이가 3인 튜플 자료형으로 인식된다.
# **튜플**<font size="2">tuple</font>은 여러 개의 값을 
# 하나로 묶어서 사용하는 값을 가리키며
# 나중에 자세히 다룬다.

# In[26]:


저는튜플입니다 = 1,000,000


# In[27]:


type(저는튜플입니다)


# In[28]:


print(저는튜플입니다)


# 셋째, 0으로 시작하면 안된다.
# 예를 들어 서울 지역의 우편번호는 0으로 시작하는데
# 이런 우편번호를 정수처럼 작성하면 문제가 발생한다.
# 
# ```python
# # 청와대 우편번호
# >>> zipcode = 03048
#   File "<stdin>", line 1
#     zipcode = 03048
#                   ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# ```    
# 
# 우편번호는 사실 구역 식별용이기에 
# 고유명사처럼 문자열로 처리하는 게 맞다.

# In[29]:


# 청와대 우편번호
zipcode = '03048'


# ### 변수의 자료형

# 변수의 자료형은 변수가 현재 가리키는 값의 자료형으로 지정된다.
# 따라서 변수에 할당된 값의 자료형이 달라지면 변수의 자료형도 함께 달라진다.

# In[30]:


num = 18
type(num)


# In[31]:


num = 3.14
type(num)


# In[32]:


num = '3.14'
type(num)


# ````{prf:example}
# :label: exp-type
# 
# 아래 표는 표현식과 해당 표현식이 표현하는 값, 그리고 값의 자료형 사이의 관계를 보여준다.
# 단, `x` 는 정수 3을 가리킨다고 가정한다.
# 
# | 표현식 | 값 | 자료형 |
# | ---   |--- | ---   |
# | `x`  | `3`  | `int` |
# | `x/2`  | `1.5`  | `float` |
# | `(x/2 - 1) < 0` | `False` | `bool` |
# | `(1, x/2-1, x+x+1)`  | `(1, 0.5, 7)`  | `tuple` |
# | `[x, x*3/2, x**3+1]`  | `[3, 4.5, 28]`  | `list` |
# ````

# ### 문자열과 `input()` 함수

# `input()` 함수를 이용하여 사용자로부터 값을 입력받을 수 있다.
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

# 문자열을 인자로 이용하여 입력할 사항에 대한 안내를 할 수 있다.
# 
# ```python
# >>> input_num = input("정수를 입력하세요 : ")
# 정수를 입력하세요 : 23
# >>> print("입력하신 정수는 " + input_num + "입니다.")
# 입력하신 정수는 23입니다.
# ```

# ## 명령문

# 컴퓨터에 명령을 내리려면
# **명령문**<font size="2">statement</font>을 작성해야 하며,
# 이를 위해 하나의 프로그래밍 언어를 선택해야 한다. 
# 모든 프로그래밍 언어는 고유의 명령문 작성 규칙을 제공하며,
# 언어의 특성에 따라 명령문 작성법과 작성된 명령문의 모양이 많이 다를 수 있다.

# ### 기본 명령문 

# 파이썬 명령문은 **기본 명령문**을 
# 지정된 규칙에 따라 합성해서 생성한다.
# 지금까지 간략하게나마 살펴본 기본 명령문은 다음과 같다.
# 
# * 변수 할당
# * `if` 조건문
# * `for` 반복문
# * `while` 반복문
# 
# 또한 명령문을 재귀적으로 합성하여 새로운 명령문을 만들 수 있다.
# **프로그램**<font size="2">program</font>은 바로 
# 특정 명령을 의도한대로 수행하는 명령문을 가리키는
# 일상 언어 표현이다.

# [파이썬 명령문의 엄밀한 정의](https://docs.python.org/3/reference/compound_stmts.html)는 
# 꽤 복잡하다.
# 웬만해서는 알 필요 없으며,
# 원하는 기능을 옳바르게 수행하는 프로그램을 구현하는 훈련과
# 작업을 통해 자연스럽게 명령문에 친숙해지는 것이 일반적이다.
# 하지만 실행기<font size='2'>interpreter</font>, 
# 번역기<font size='2'>compiler</font> 등을 직접 구현해야 하는 
# 일을 하려면 반드시 알아야 한다. 

# ### 함수 호출과 명령문 

# 예를 들어, `print("맞았습니다!)` 를 실행하면 문자열 인자를 화면에 출력한다.
# 이처럼 함수를 지정된 인자와 함께 실행하도록 하는 것이
# **함수 호출**<font size="2">function call</font>이다.
# 함수 호출이 이뤄지면 
# 함수 이름이 가리키는 명령문이 실행되기에 
# 함수 호출도 하나의 명령문 역할을 수행한다.
# 하지만 함수 자체는 명령문이 아니다.

# ## 주석

# 프로그램에 사용된 명령문에 설명을 추가하면 
# 작성된 프로그램의 작동 원리를 보다 쉽게 이해할 수 있다.
# 이와 같이 프로그램의 실행과는 무관하지만 명령문, 함수 등의 
# 기능, 아이디어 등을 설명하는 문장이
# **주석**<font size="2">comment</font>이다.
# 주석은 일반 자연어를 사용하며,
# 프로그램이 실행될 때 파이썬 실행기에 의해 무시된다.
# 
# 주석은 한 줄 또는 여러 줄로 작성될 수 있다.
# 한 줄 주석은 우물 정(영어로 샵<font size="2">sharp</font>) 기호(`#`)로 시작한다.

# In[33]:


# speed는 시속을 가리키는 변수이다.

speed = 90 # 속도 단위는 km이다.


# 여러 줄 주석은 작은따옴표 세 개(`'''`)로 감싼다.

# In[34]:


print(0)
'''
여러 줄 주석은
이렇게 사용합니다.
'''
print(1)


# ## 프로그램 오류와 디버깅

# 변수 이름으로 `class` 등의 지정어를 사용하거나, `odd~job` 또는 `US$`처럼 
# 허용되지 않은 기호를 포함하는 경우에 파이썬 실행기는 
# **오류**<font size="2">error</font>를 발생시키며 곧바로 프로그램의 실행을 멈춘다.
# 예를 들어, 아래와 같이 변수 이름에 공백을 사용하여 실행한 결과를 확인해 보자.
# 
# ```python
# >>> bad name = 5
#   File "<stdin>", line 1
#     bad name = 5
#         ^
# SyntaxError: invalid syntax
# ```    
# 
# 오류가 발생하면 오류의 원인을 찾아 해결해야 한다.
# 이렇게 프로그램의 오류를 찾아 해결하는 과정을 **디버깅**(debugging)이라 부른다.
# 
# 프로그램의 오류는 크게 세 가지 유형으로 나뉜다.

# ### 구문 오류

# 변수의 이름을 잘못 지정하면 `SyntaxError: invalid syntax`와 
# 같은 **구문 오류**<font size="2">syntax error</font>가 발생한다.
# 구문 오류는 실행기가 프로그램을 실행하기 전에 일종의 문법 검사를 통해 찾아낸다.

# ### 런타임 오류
# 
# **런타임 오류**<font size="2">runtime error</font>는 
# 프로그램이 실행되는 중간에 발생하는 오류이다.
# 프로그램 실행 중간에 예외 상황을 발생시키는 오류라는 의미에서 런타임 오류를 
# **예외**<font size="2">exception</font>라고 부르기도 한다.
# 런타임 오류는 다양한 경우에 발생한다.
# 여기서는 두 가지 경우를 살펴본다.

# ::::{prf:example} ZeroDivisionError
# :label: zerodivision
# 
# 런타임 에러의 대표적인 예는 **0으로 나누기 오류**이다.
# 
# ```python
# >>> num = 0
# >>> print(3/num)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# ```
# 
# `ZeroDivisionError` 라고 표시되는데,
# 이는 0으로 나눗셈을 시도하는 경우 발생한다. 
# `3/num`은 문법적으로 전혀 문제가 없지만 실제 계산 중에 `num`에 할당된 값이 0이라는 것으로 확인되어
# 오류가 발생한다.
# ::::

# ::::{prf:example} NameError
# :label: nameerror
# 
# 아래 코드를 실행하면 'a_number' 라는 이름이 선언되어 있지 않기 때문에 문제가 발생한다.
# 
# ```python
# >>> a_Number = 327.68
# >>> b = a_number * 3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a_number' is not defined
# ```
# 
# 자세히 살펴보면 'a_number'와 'a_Number' 둘 중에 하나는 오타임을 알 수 있다.
# ::::

# ### 의미 오류

# 프로그램 실행은 잘 되지만 원하는 결과를 가져오지 못한다면 프로그램
# 어딘가에 논리적 오류가 존재한다는 의미이다.
# 이와같은 오류를 
# **의미 오류**<font size="2">semantic error</font>라 부르며,
# 발생원인은 다양하며,
# 프로그램이 정상적으로 작동하기 때문에 구문 오류나 런타임 오류와는 다르게
# 오류의 원인을 바로 확인하기 어려울 수 있다.
# 
# 수학 문제를 풀다가 계산실수를 하거나, 기호를 다르게 적거나, 
# 문제를 잘못 이해했거나 해서
# 풀 수 있었던 문제를 틀렸던 경험이 있을 것이다.
# 프로그래밍 과정에서도 유사한 실수를 수없이 하게 된다.
# 예를 들어, 아래 프로그램은 두 배 계산 대신에 제곱 계산을 하는 실수를 보여준다.

# In[35]:


num = 3
doubleNum = num ** 2

print("입력한 값", num, "의 두 배는", doubleNum, "입니다.")


# 두 배하려면 `num * 2`를 사용했어야 하는데 실수로 `num ** 2`를 사용하여서
# 결과적으로 입력한 값의 제곱을 계산하게 된다.
# 수천, 수만 줄로 이루어진 프로그램에서 이런 형식의 오류의 원인을 찾는 일은
# 경우에 따라 모래사장에서 바늘찾기처럼 매우 어렵거나 불가능할 수 있다.

# :::{admonition} `print()` 함수의 인자
# :class: info
# 
# `print()` 함수가 여러 개의 인자를 받으면
# 모든 인자를 한 줄에 차례대로 출력한다.
# 인자들 사이는 스페이스 여백으로 구분한다.
# `print()` 에 대해서는 {numref}`%s절 <sec:keyword-arguments>`에서
# 보다 자세히 설명한다.
# :::

# ## 연습문제

# 참고: [(실습) 변수, 값, 표현식, 명령문](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-variables_expressions.ipynb)
