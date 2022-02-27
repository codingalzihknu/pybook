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

# **문자열**<font size="2">string</font>은 문자 기호로 이루어진 단어, 문장 등을 가리킨다.
# 키보드에 포함된 영문 알파벳, 한글 자음과 모음 등을 기본적으로 사용한다.
# 문자열은 세 가지 방식으로 작성될 수 있다.

# **작은 따옴표 활용**

# In[16]:


s = '안녕하세요.'
print(s)


# **큰 따옴표 활용**

# In[17]:


s = "안녕하세요."
print(s)


# **연속된 세 개의 작은 또는 큰 따옴표 활용**
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


# :::{admonition} 유니코드
# :class: info
# 
# 키보드 상에 존재하지 않는 다른 기호나 문자도 **유니코드**<font size="2">unicode</font> 
# 형식으로 지원된다.
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
# 예를 들어, 작은 따옴표가 포함된 문자열을 다음과 같이 지정하면 오류가 발생한다.
# 
# ```python
# >>> s = 'Python's grammar'
#   File "<stdin>", line 1
#     s = 'Python's grammar'
#                 ^
# SyntaxError: invalid syntax
# ```
# 
# 이유는 작은 따옴표로 문자열의 시작을 지정했기 때문에
# `Python's` 문장에 사용된 작은 따옴표가 
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
# | `\'` | 작은 따옴표 |
# | `\"` | 큰 따옴표 |
# | `\\` | 백슬래시 기호 |
# | `\n` | 줄바꿈 |
# | `\t` | 탭 |

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

# ### whitespace

# whitespace는 화면상으로 아무것도 표시되지 않는 공백 문자를 말한다.  
# 
# `string.whitespace`는 공백으로 간주하는 문자를 포함하는 문자열로, 여기에는 스페이스<font size = "2">space</font>, 탭<font size = "2">tab</font>, 줄변경<font size = "2">line feed or new line</font>, 캐리지 리턴<font size = "2">carriage return</font>, 수직탭<font size = "2">vertical tab</font>, 폼피드<font size = "2">form feed</font> 문자가 포함된다.

# In[28]:


import string
string.whitespace


# |기호|설명|
# |:----------:|:----------:|
# |` `|공백 <font size = "2">space</font>| 
# |`\t`|탭 <font size = "2">tab</font>| 
# |`\n`|줄변경 <font size = "2">line feed or new line</font>|
# |`\r`|캐리지 리턴 <font size = "2">carriage return</font>|
# |`\v` 또는 `\x0b`|수직탭 <font size = "2">vertical tab</font>|
# |`\f` 또는 `\x0c`|폼피드<font size = "2">form feed</font>|

# In[29]:


print('1\n2\t3')


# In[30]:


print('123\b4')


# * 캐리지 리턴(`\r`)은 그 줄의 맨앞으로 이동시키는 특수 문자이다.

# In[31]:


print('1234\r56')


# * `\v` 또는 `\x0b`는 수직탭이고,  `\f` 또는 `\x0c`는 다음 페이지로 이동하는 것을 의미한다. 

# :::{admonition} 문자열 `''`과 문자의 `' '` 차이첨 
# :class: info
# 
# 빈 문자열<font size = "2">empty string</font> `''`는 아무런 문자도 포함하지 않았기 때문에 문자열의 길이 즉, 문자열에 포함된 문자의 개수가 0이다.   
# 반면 `' '`는 눈에 보이지는 않지만 공백 문제 하나를 포함하는 문자열이며 길이가 1이다. 
# :::

# ### 문자열에 특수 문자 활용하기

# 백슬래시(￦), 줄바꾸기(￦n), 탭(￦t) 등은 문자열에 사용될 경우 특수한 기능을 갖는다. 그리고 백슬래시(`\`)기호를 붙여서 특수 기능을 해제<font size= "2">escape</font>할 수 있다.

# In[32]:


print("Hello\\n World")


# In[33]:


print("Hello\\t World")


# In[34]:


print("Good\\night")


# 연속된 백슬래시 두 개를 출력하려면 아래와 같이 해야 한다.

# In[35]:


print("\\\\")


# :::{admonition} 주의
# :class: caution
# 
# 아래와 같이 코드를 작성하면 오류가 발생하므로 주의해야 한다.
# ```python
# >>> print("\\\")
#   File "/tmp/ipykernel_76/2337434698.py", line 1
#     print("\\\")
#                 ^
# SyntaxError: EOL while scanning string literal
# ```

# :::{admonition} 참고 
# :class: info  
# **순수 문자열**
# '가공되지 않은'의 의미를 갖는 'raw' 단어의 첫 글자인 'r'을 문자열 앞에 두면 특수 기능이 사라진다.
# :::

# In[36]:


print(r"Hello\n World")


# In[37]:


print(r"Hello\t World")


# In[38]:


print(r"Hello\ World")


# ### 문자열과 `input()` 함수

# 사용자의 입력은 `input()` 함수를 사용하여 받을 수 있다. 아래와 같이 `input()`을 입력하고 코드를 실행하면, 그 아래에 값을 입력하라는 창이 나온다. 그곳에 `Hello, python!`을 입력하고 엔터<font size ="2">enter</font>를 누르면 입력한 문자열이 그대로 출력된다.

# In[39]:


input()


# `input()` 함수로 입력받은 값은 변수에 할당하여 사용할 수도 있다.

# In[76]:


name = input()
print("Hello, " + name)


# 이때 `input()` 함수로 입력받은 값은 문자열`str`이다.

# In[77]:


type(name)


# 사용자가 숫자를 입력하더라도 입력받은 값은 문자열`str`이다.

# In[80]:


num = input()
type(num)


# 사용자에게 무엇을 입력할지 알려주고 싶다면, 그 내용의 문자열을 `input()`의 인자로 사용하면 된다.

# In[83]:


input_num = input("정수를 입력하세요 : ")
print("입력하신 정수는 " + input_num + "입니다.")


# ### 문자열과 `print()` 함수

# 그 동안 출력을 위해 `print()` 함수를 사용하였다. 예를 들어, `Hello, python`을 출력하고 싶다면, 아래와 같이 코드를 작성하면 된다. 

# In[84]:


print('Hello, python')


# 이제 `print()` 함수에 대해서 조금 더 살펴보자. 

# * 큰 따옴표(또는 작은 따옴표)로 둘러싸인 문자열을 연속해서 사용하면 문자열에서 +연산을 한 것과 동일한 결과를 출력해준다.

# In[86]:


print("Hello ""World")
print('Hello ''World')
print('Hello '"World")
print("Hello " + "World")


# * 문자열 사이에 콤마(`,`)를 사용하면 띄어쓰기를 할 수 있다.

# In[87]:


print("Hello", "World")


# * 인자들 사이에 구분자를 넣고 싶다면, `sep`을 변경하면 된다. `sep`의 기본값은 공백이다.

# In[88]:


print("010", "1234", "5678", sep = "-")
print("Hello", "World", sep = ", ")


# * 마지막에 출력할 문자를 변경하고 싶다면, `end`를 변경하면 된다. `end`의 기본값은 줄변경(`\n`)이다.

# In[89]:


print("a")
print("b", end = "")
print("c", end = "\t")
print("d")


# ### 문자열 포매팅 <font size = "2">String formatting</font>

# #### `str.format()`

# `format()`메서드를 사용하면, 문자열의 중괄호(`{}`)가 `format()`의 인자로 변경된다. 예제와 함께 살펴보자. 

# In[113]:


'{}님, 안녕하세요.'.format('강현')


# In[114]:


name = '강현'
'{}님, 안녕하세요.'.format(name)


# In[117]:


age = 3
'강현이는 {}살이다.'.format(age)


# 여러 개의 값을 변경할 때는 콤마(`,`)로 구분해서 적어준다. 

# In[118]:


name = '강현'
age = 3
'{}이는 {}살이다.'.format(name, age)


# 인덱스 항목을 사용하여 넣어줄 위치를 지정할 수도 있다.

# In[121]:


name1 = '강현'
name2 = '나영'
print('{}이와 {}이는 친구다.'.format(name1, name2))
print('{0}이와 {1}이는 친구다.'.format(name1, name2))
print('{1}이와 {0}이는 친구다.'.format(name1, name2))


# **소수점 표현**  
# 
# 콜론(`:`) 뒤에 소수점아래 몇 번째 자리까지 출력할지를 적어주면, 그 만큼을 보여준다.  
# 예제와 함께 살펴보자. 
# * `.`은 소수점을 의미하고, 소수점 뒤의 숫자는 소수점 뒤에 나올 숫자의 개수다.  

# In[101]:


num = 0.123456789
print('{0:.1f}'.format(num))
print('{0:.2f}'.format(num))
print('{0:.3f}'.format(num))
print('{0:.5f}'.format(num)) # 소수점 아래 여섯 번째 자리에서 반올림


# #### f-string

# 문자열 앞에 `f` 를 붙이면, 문자열 포매팅 기능을 사용할 수 있다.  
# 예제와 함께 살펴보자. 

# In[122]:


name = '강현'
f'{name}님, 안녕하세요.'


# In[123]:


age = 3
f'강현이는 {age}살이다.'


# In[124]:


name = '강현'
age = 3
f'{name}이는 {age}살이다.'


# `{}`안에 변수와 수식(`+`, `-`, `*`, `/` 등)을 함께 사용하는 것도 가능하다. 

# In[126]:


name = '강현'
age = 3
f'{name}이의 동생은 {age - 2}살이다'


# In[109]:


num = 0.123456789
print(f'{num:.1f}')
print(f'{num:.2f}')
print(f'{num:.3f}')


# ## 부울값

# 참(`True`)과 거짓(`False`)를 나타내는 자료형이다. 
# 파이썬에서 부울 자료형은 `int` 형의 자식형<font size = "2"> subtype</font>이고, 대부분의 상황에서 `True`와 `False`는 각각 `1`과 `0`처럼 동작한다. 

# ### 논리 연산자

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`and`|그리고|`True and False`|`False`|
# |`or`|또는|`True or False`|`True`|
# |`not`|부정|`not False`|`True`|

# :::{admonition} 참고 
# :class: info
# 
# `x and y`는 `x`가 참일 때만 `y`를 확인한다.  
# `x or y`는 `x`가 거짓일 때만 `y`를 확인한다.
# 
# 예를 들어, 아래와 같이  `False and 3/0`를 실행하면 `False`가 나온다. 
# ```python
# >>> False and 3/0
# ```
# 
# 하지만 반대로 `3/0 and False`를 실행하면 오류가 발생한다. 
# ```python
# >>> False and 3/0
# ZeroDivisionError                         Traceback (most recent call last)
# /tmp/ipykernel_422/2156724109.py in <module>
# ----> 1 True and 3/0
# 
# ZeroDivisionError: division by zero
# ```
# :::

# ### 비교 연산자

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`<`|작다|`2 < 1`|`False`|
# |`<=`|작거나 같다|`1 <= 2`|`True`|
# |`>`|크다|`2 > 1`|`True`|
# |`>=`|크거나 같다|`1 >= 2`|`False`|
# |`==`|같다|`1 == '1'`|`False`|
# |`!=`|같지 않다|`1 != '1'`|`True`|

# 서로 다른 숫자형을 제외하고는 서로 다른 형은 같다고 비교되지 않는다. 

# 예를 들어, 정수 `1`와 부동소수점 `1.0`이 같은지 여부를 확인해보자.

# In[17]:


1 == 1.0


# 반면, 정수 `1`과 문자열 `'1'`은 형<font size = "2">type</font>이 달라서 같은지 여부를 확인해보면, `False`가 나온다.

# In[18]:


1 == '1'


# In[8]:


1 == 1.0


# 문자열도 비교연산자를 사용할 수 있다.   
# 크기 비교 연산자들은 영어 사전식의 알파벳 순서를 사용한다. 

# In[28]:


'apple' == 'pineapple'


# In[26]:


'apple' < 'banana'


# :::{admonition} 참고 
# :class: info
# 영어 알파벳의 경우 대문자가 소문자보다 작다고 판단한다.
# :::

# ## 형변환

# `2.3 + 3`을 실행하면 파이썬 해석기<font size="2">interpreter</font>는
# 내부적으로 정수를 부동소수점으로 형변환하는 함수 `float()`를 이용하여
# 정수 `3`을 부동소수점 `3.0`으로 유형을 변환한 후에
# 덧셈을 처리한다. 
# 이렇게 값의 유형을 적절하게 자동 변환하는 기능을 
# **형변환**<font size="2">type casting</font>이라 부른다.

# In[9]:


float(3)


# `float()` 함수 이외에 `int()`, `str()`, `bool()` 등 다양한 형변환 함수가 제공된다.

# **`int()` 함수**
# 
# 정수 모양의 문자열 또는 부동소수점을 정수로 변환한다.

# In[11]:


int('5')


# In[12]:


int(4.8)


# `True`와 `False`는 각각 1과 0으로 취급된다.

# In[13]:


int(True)


# **`float()` 함수**
# 
# 유한소수 모양의 문자열 또는 정수 등을 부동소수점으로 변환한다.

# In[14]:


float('7.9')


# **`str()` 함수**
# 
# 임의의 값을 문자열로 변환한다.

# In[74]:


str(6)


# In[15]:


str(7.6)


# In[16]:


str(False)


# **`bool()` 함수**
# 
# 임의의 값을 `True` 또는 `False` 로 변환한다.
# `0`, `0.0`, `''`(빈 문자열) 등처럼 0, 비어 있는 것, 의미 없는 것등은 `False` 로
# 그렇지 않으면 `True` 로 지정한다.

# In[24]:


bool(0)


# In[25]:


bool(2)


# In[26]:


bool(0.0)


# In[27]:


bool(0.01)


# In[28]:


bool('')


# In[29]:


bool('Hello')


# :::{admonition} 주의 
# :class: caution  
# `int()`함수의 인자로 문자열을 사용할 때는 그 모양이 정수모양이어야 하고, `float()` 함수의 인자로 문자열을 사용할 때는 그 모양이 정수 또는 부동소수점 모양이어야 한다. 
# 
# ```python
# >>> int('5.0')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_279/3485297474.py in <module>
# ----> 1 int('5.0')
# 
# ValueError: invalid literal for int() with base 10: '5.0'
# ```
# ```python
# >>> float('5GB')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_279/814975516.py in <module>
# ----> 1 float('5GB')
# 
# ValueError: could not convert string to float: '5GB'
# ```
# :::
