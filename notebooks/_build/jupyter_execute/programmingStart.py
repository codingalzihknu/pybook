#!/usr/bin/env python
# coding: utf-8

# # 프로그래밍 시작하기

# 간단한 예제를 이용하여 파이썬 프로그래밍을 맛보기 해본다.

# ## 파이썬 시작하기

# 다음 명령을 실행하면 `Hello, world` 문구가 화면에 출력된다.

# In[1]:


print("Hello, world!")


# 계속해서 아래 명령문도 실행해보자. 

# In[2]:


a = 3
b = 2 * a
type(b)


# :::{admonition} 코드 셀 실행
# :class: tip
# 
# 주피터 노트북의 코드 셀<font size="2">code cell</font>은
# IPython 콘솔처럼 명령문을 실행할 수 있으며 
# 이어지는 코드 셀은 이전에 실행된 코드 셀의
# 내용을 이어 받는다.
# 하지만 코드 셀은 콘솔과는 달리 여러 줄의 파이썬 명령문을 
# 마치 편집기로 작성된 하나의 코드 파일을 실행하는 것처럼
# 전체 명령문을 차례대로 실행할 수 있다.
# :::

# In[3]:


print(b)


# In[4]:


a * b 


# In[5]:


b = "hello"
type(b)


# In[6]:


b + b


# In[7]:


2 * b


# In[8]:


b * 2


# 변수를 선언할 때 변수의 자료형<font size="2">data type</font>을 
# 지정하지 않는다.
# 변수의 자료형을 지정하지 않기 때문에
# 변수가 가리키는 값을 다른 자료형의 값으로 변경할 수 있다.
# 예를 들어 변수 `b` 가 처음에는 정수 `6` 을 
# 가리켰다가 이후엔 문자열 `'hello'` 를 가리킨다.

# :::{admonition} 변수의 자료형
# :class: tip
# 
# C, C++, C#, 자바 등 다른 프로그래밍 언어와의 차이점 중에 하나다.
# 예를 들어, C 언어에서 변수 선언은 아래와 같이 변수의 자료형을 지정한다.
# 
# ```c
# int b = 6;
# ```
# 
# 따라서 파이썬과는 달리 아래와 같이 문자열 등 다른 자료형의 값을 가리키도
# 하는 것을 허용하지 않는다.
# 
# ```c
# b = "hello";
# ```
# :::

# 곱셈 기호 `*` 는 인자의 자료형에 따라 다른 연산자로 작동한다. 
# `3 * 6` 은 두 정수의 곱셈이지만
# `2 * 'hello'` 와 `2 * 'hello'` 는 문자열 `'hello'` 를 두 번 
# 이어붙인다.
# 덧셈 기호 `+` 도 사용되는 인자에 따라 다르게 작동한다.

# ## 파이썬의 기본 자료형

# 정수, 부동소수점, 부울값 등 세 종류의 **스칼라**<font size="2">scalar</font> 
# 자료형을 기본으로 제공한다.

# ### 정수

# -2, -1, 0, 1, 2 등의 정수는 `int` 유형<font size="2">type</font>의 값이다.
# 정수는 사칙연산, 변수 할당 등에 사용된다.

# In[9]:


1 + 2


# In[10]:


a = 4
type(a)


# In[11]:


a * 2


# ### 부동소수점

# **부동소수점**은 유리수, 실수 등을 가리키며 `float` 유형의 값이다.
# 정수와 마찬가지로 사칙연산, 변수 할당 등에 사용된다.

# In[12]:


2.1 + 3.3


# In[13]:


c = 2.1
type(c)


# 정수와의 연산도 가능한데, 이때 정수를 부동소수점으로 취급한다. 
# 예를 들어 3은 3.0으로 처리된다.

# In[14]:


2.3 + 3


# In[15]:


2.3 + 3.0


# ### 부울값

# 참과 거짓을 의미하는 `True`와 `False`를 
# **부울값**<font size="2">boolean</font>
# 또는 **진리값**이라 한다.
# 부울값은 `bool` 유형을 갖는 **유일한 두 개의 값**이다.

# In[16]:


type(True)


# In[17]:


d = False
type(d)


# 등식, 부등식 등이 부울값을 가리키는 
# **표현식**<font size="2">expression</font>이다.

# In[18]:


3 > 4


# In[19]:


test = (1.0 == 1)


# In[20]:


test


# In[21]:


type(test)


# ## 계산기

# 파이썬을 계산기로 활용할 수 있다.

# In[22]:


7 * 3


# 정수에 점(`.`)을 찍으면 부동소수점으로 처리된다.

# In[23]:


7 * 3.


# 지수승은 `**` 를 사용한다.

# In[24]:


2 ** 10


# 정수 나눗셈의 몫(`//`)과 나머지(`%`) 연산도 지원된다.

# In[25]:


8 // 3


# In[26]:


8 % 3


# 몫 계산과 나눗셈 연산은 다르다.
# 몫은 정수 계산이며, 나눗셈은 부동소수점 연산이다.

# In[27]:


8 / 3


# 나눗셈의 몫이 정수인 경우엔 차이를 두지 않는다.

# In[28]:


(4 / 2) == (4 // 2)


# :::{admonition} 형변환 함수
# :class: info
# 
# `2.3 + 3`을 실행하면 파이썬 해석기<font size="2">interpreter</font>는
# 내부적으로 정수를 부동소수점으로 형변환하는 함수 `float()`를 이용하여
# 정수 `3`을 부동소수점 `3.0`으로 유형을 변환한 후에
# 덧셈을 처리한다. 
# 이렇게 값의 유형을 적절하게 자동 변환하는 기능을 
# **형변환**<font size="2">type casting</font>이라 부른다.
# 
# ```python
# >>> float(3)
# 3.0
# ```
# 
# `float()` 함수 이외에 `int()`, `str()`, `list()` 등 다양한 형변환 함수를 앞으로 
# 만나게 될 것이다.
# :::

# :::{admonition} 함수 이름 표기법
# :class: tip
# 
# `float`는 부동소수점 자료형을 가리키기도 하고 
# 형변환 함수를 가리키기도 한다. 
# 여기서는 자료형과 함수 이름을 구분하기 위해 
# 함수는 `int()`, `float()`, `str()`, `list()` 등처럼
# 함수 이름과 괄호를 함께 사용하는 표기법 관행을 따른다.
# :::

# ## 문자열

# **문자열**은 문자와 기호들의 나열을 의미하며 작은따옴표 또는 큰따옴표로 감싸인다.
# `print()` 함수는 지정된 문자열을 화면에 출력할 때 문자열을 감싸는 따옴표를 제고하고 
# 동시에 문자열에 포함된 특별한 기능을 수행하는 문자를 적절하게 변환해서 보여준다.

# In[29]:


'spam eggs'


# In[30]:


print('spam eggs')


# 작은따옴표로 감싸인 문자열이 작은따옴표를 포함하도록 하려면
# 백슬래시 `\`기호를 작은따옴표 기호 바로 앞에 추가한다.

# In[31]:


'doesn\'t'


# In[32]:


print('doesn\'t')


# 큰따옴표로 감싸인 문자열에 작은따옴표를 임의로 포함시킬 수 있다.
# 이는 문자열의 시작과 끝이 작은따옴표에도 불구하고 명확하기 때문이다.

# In[33]:


"doesn't"


# In[34]:


print("doesn't")


# 동일한 이유로 작은따옴표로 감싸인 문자열이 큰따옴표를 포함해도 된다.

# In[35]:


'"Yes," they said.'


# In[36]:


print('"Yes," they said.')


# 하지만 큰따옴표로 감싸인 문자열이 큰따옴표를 포함하려면
# 여기서도 백슬래시 기호를 추가해야 한다.

# In[37]:


"\"Yes,\" they said."


# In[38]:


print("\"Yes,\" they said.")


# 문자열에 큰따옴표와 작은따옴표가 동시에 포함되면
# 감싸는 따옴표와 동일한 종류의 따옴표는 백슬래시가 추가되어야 한다.

# In[39]:


'"Isn\'t," they said.'


# `print()` 함수는 백슬래시의 모든 특수 기능을 적절히 반영해서 화면에 출력한다.

# In[40]:


print('"Isn\'t," they said.')


# `\n`은 줄바꿈을 의미하는 문자다.

# In[41]:


s = 'First line.\nSecond line.'


# 변수 `s` 가 가리키는 문자열은 다음과 같다.

# In[42]:


s


# `print()` 함수를 이용하면 실제 의도한 대로 두 줄로 표현된다.

# In[43]:


print(s)


# ### 날 문자열

# 앞서의 경우처럼 작은따옴표, 큰따옴표, 특수 문자에 대해 백슬래시를 사용하냐,
# 그렇지 않냐를 걱정하는 것 대신에
# **날 문자열**<font size="2">raw string</font>을 사용하면 보다 편리하다.
# 날 문자열은 문자열 앞에 `r`을 추가해서 얻어지며
# 그러면 문자열 안에 포함된 모든 특수 문자들의 기능이 제거된다.

# In[44]:


print('C:\some\name')  # 일반 문자열 사용. 줄바꿈 적용됨.


# In[45]:


print(r'C:\some\name')  # 날 문자열 사용. 줄바꿈 없음.


# ### 여러줄 문자열

# 여러 줄로 작성된 문자열은 항상 세개의 작은따옴표 또는 세 개의 큰따옴표로 감싸져야 한다.

# In[46]:


print("""첫째줄(위에 여백 없음!)
둘째줄
셋째줄
""")


# 하지만 다음과 같이 첫째줄에 비어 있는채로 출력된다.

# In[47]:


print("""
첫째줄(위에 여백 있음)
둘째줄
셋째줄
""")


# 이를 방지하려면 백슬래시 기호를 추가한다.

# In[48]:


print("""첫째줄(위에 여백 없음)
둘째줄
셋째줄
""")


# ### 문자열 연산

# 문자열의 `+` 와 `*` 두 기호를 이용한 연산을 지원한다.
# 
# `+` 연산자는 두 문자열을 이어붙인다.

# In[49]:


'hello' + 'python'


# In[50]:


'hello, ' + 'python'


# `*` 연산자는 정수와 문자열을 인자로 받아 정수 만큼 복제해서 이어붙인다.

# In[51]:


3 * 'hello'


# In[52]:


2 * 'hello, ' + "python"


# ### 문자열 길이

# 문자열에 포함된 문자의 개수를 문자열의 길이로 지정한다.
# `len()` 함수가 문자열의 길이를 계산한다.

# In[53]:


s = 2 * 'hello, ' + "python"


# In[54]:


len(s)


# ### 문자열 인덱싱

# 문자열은 문자 여러 개의 나열이며 문자들 사이의 순서가 중요하다.
# 이때 문자열 왼편에 위치한 문자부터 차례대로 0, 1, 2, 3 등의
# **인덱스**<font size="2">index</font>를 부여받는다.
# **인덱싱**<font size="2">indexing</font>은 
# 인덱스를 이용하여 문자열의 항목을 확인하는 기능이다.

# In[55]:


word = 'I love Python!'


# In[56]:


word[0]  # 0번 인덱스 문자. 즉, 왼쪽에서 첫번째 문자.


# In[57]:


word[5]   # 5번 인덱스 문자. 즉, 왼쪽에서 여섯번째 문자.


# 인덱스를 문자열 오른쪽에서부터 차례대로 -1, -2, -3 등 음수로 지정할 수도 있다.

# In[58]:


word[-1]  # 맨 오른쪽 문자. 즉 마지막 문자.


# In[59]:


word[-2]  # 끝에서 두번째 문자.


# In[60]:


word[-6]  # 끝에서 여섯번째 문자.


# ### 문자열 슬라이싱

# **슬라이싱**<font size="2">slicing</font>은 지정된 인덱스의 구간에 해당하는
# 문자들을 추출하여 새로운 문자열을 생성하는 기능이다.

# In[61]:


word[0:2]  # 0번 인덱스부터 2번 인덱스 이전까지 추출


# In[62]:


word[2:5]  # 2번 인덱스부터 5번 인덱스 이전까지 추출


# 구간의 처음과 끝을 생략할 수 있다.
# 그러면 구간의 시작은 0, 구간의 끝은 문자열의 길이에 1을 더한 값으로 자동 지정된다.

# In[63]:


word[:2]   # 처음부터 1번 인덱스까지


# In[64]:


word[4:]   # 4번 인덱스부터 끝까지


# In[65]:


word[-2:]  # 끝에서 두번째 인덱스부터 끝까지


# In[66]:


word[:3] + word[3:]


# **보폭**<font size="2">stride</font>을 사용하여 인덱스를 
# 지정된 보폭만큼 건너 뛰면서 문자를 추출할 수 있다.
# 보폭이 1인 경우는 앞서 본 것처럼 보폭 표기를 아예 생략하면 된다.

# In[67]:


word[2:10:2]  # 2번 인덱스부터 9번 인덱스까지 두 개씩 건너뛰며 추출


# -1을 보폭으로 지정하면 오른쪽에서 왼쪽으로 역순으로 추출한다.

# In[68]:


word[::-1]  # 문자열 뒤집기


# In[69]:


word[-2:-8:-2]  # 끝에서 두번째 인덱스부터 끝에서 일곱번째 인덱스까지 두 개씩 건너뛰며 추출


# 문자열의 길이에 해당하는 범주를 벗어나는 인덱스를 사용하면 오류가 발생한다.
# 
# ```python
# >>> word[42]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# ```

# 반면에 슬라이싱에서는 자동으로 문자열의 처음과 끝을 한계로 사용한다.

# In[70]:


word[4:42]


# In[71]:


word[42:]


# ### 문자열 수정 가능성

# 한 번 생성된 문자열은 수정이 불가능<font size="2">immutable</font>하다.
# 예를 들어 다음과 같이 인덱싱 또는 슬라이싱을 이용하여
# 문자열을 수정하고자 하면 오류가 발생한다.
# 
# ```python
# >>> word[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# 
# >>> word[2:] = 'py'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# ```

# 문자열을 수정하는 대신 인덱싱, 슬라이싱, 문자열 연산을 활용하여 
# 필요한 문자열을 생성해야 한다.

# In[72]:


'You' + word[1:]


# ## 리스트

# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
# 
# ```python
# >>> squares = [1, 4, 9, 16, 25]
# >>> squares
# [1, 4, 9, 16, 25]
# ```

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
# 
# ```python
# >>> squares[0]  # indexing returns the item
# 1
# >>> squares[-1]
# 25
# >>> squares[-3:]  # slicing returns a new list
# [9, 16, 25]
# ```

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
# 
# ```python
# >>> squares[:]
# [1, 4, 9, 16, 25]
# ```

# Lists also support operations like concatenation:
# 
# ```python
# >>> squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ```

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
# 
# ```python
# >>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
# >>> 4 ** 3  # the cube of 4 is 64, not 65!
# 64
# >>> cubes[3] = 64  # replace the wrong value
# >>> cubes
# [1, 8, 27, 64, 125]
# ```

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
# 
# ```python
# >>> cubes.append(216)  # add the cube of 6
# >>> cubes.append(7 ** 3)  # and the cube of 7
# >>> cubes
# [1, 8, 27, 64, 125, 216, 343]
# ```

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
# 
# ```python
# >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> # replace some values
# >>> letters[2:5] = ['C', 'D', 'E']
# >>> letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# >>> # now remove them
# >>> letters[2:5] = []
# >>> letters
# ['a', 'b', 'f', 'g']
# >>> # clear the list by replacing all the elements with an empty list
# >>> letters[:] = []
# >>> letters
# []
# ```

# The built-in function len() also applies to lists:
# 
# ```python
# >>> letters = ['a', 'b', 'c', 'd']
# >>> len(letters)
# 4
# ```

# It is possible to nest lists (create lists containing other lists), for example:
# 
# ```python
# >>> a = ['a', 'b', 'c']
# >>> n = [1, 2, 3]
# >>> x = [a, n]
# >>> x
# [['a', 'b', 'c'], [1, 2, 3]]
# >>> x[0]
# ['a', 'b', 'c']
# >>> x[0][1]
# 'b'
# ```

# ## 3.2. First Steps Towards Programming

# Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the Fibonacci series as follows:
# 
# ```python
# >>> # Fibonacci series:
# ... # the sum of two elements defines the next
# ... a, b = 0, 1
# >>> while a < 10:
# ...     print(a)
# ...     a, b = b, a+b
# ...
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# ```

# This example introduces several new features.
# 
# - The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.
# 
# - The while loop executes as long as the condition (here: a < 10) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple comparison. The standard comparison operators are written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).
# 
# - The body of the loop is indented: indentation is Python’s way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot guess when you have typed the last line). Note that each line within a basic block must be indented by the same amount.
# 
# - The `print()` function writes the value of the argument(s) it is given. It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:

# ```python
# >>> i = 256*256
# >>> print('The value of i is', i)
# The value of i is 65536
# ```

# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
# 
# ```python
# >>> a, b = 0, 1
# >>> while a < 1000:
# ...     print(a, end=',')
# ...     a, b = b, a+b
# ...
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
# ```
