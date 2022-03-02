#!/usr/bin/env python
# coding: utf-8

# # 프로그래밍 시작하기

# 간단한 예제를 이용하여 파이썬 프로그래밍을 맛보기 해본다.

# ## 계산기

# 파이썬을 계산기로 활용할 수 있다.

# ### 수 연산

# 임의의 연산식을 작성하고 실행하면 연산 결과가 계산되어 보여진다. 
# 일반적으로 알려진 사칙연산 규칙이 동일하게 적용된다.

# In[1]:


-5 + 2


# In[2]:


50 - 5 * 6


# In[3]:


(50 - 5 * 6) / 4


# In[4]:


17 / 3


# `-3`, `5`, `17` 등의 정수는 `int` 라는 정수 자료형에 속하고, 
# `5.0`, `1.6` 등의 소수는 `float`
# **부동소수점** 자료형에 속한다.
# 나눗셈의 결과는 항상 `float`에 속한다. 
# 
# 대다수의 프로그래밍 언어에서 `5` 와 `5.0` 은 서로 다른 
# **자료형**<font size="2">data type</font>에 속하는 것으로 취급한다.
# 하지만 그럼에도 불구하고 `5` 와 `5.0` 을 동일한 수로 간주하기도 한다. 
# 이는 정수와 소수는 원래 다르지만 정수 집합을 소수 집합의 부분집합으로 취급한다는
# 수학 상식과도 일치한다.
# 따라서 정수와 부동소수점이 함께 연산에 사용되는 정수는 모두 부동소수점으로 처리되어
# 계산된다.

# In[5]:


4 * 3.75 - 1


# 몫과 나머지는 정수로 계산된다.

# In[6]:


17 // 3   # 몫 계산


# In[7]:


17 % 3    # 나머지 계산


# 지수승 연산은 `**` 연산자를 이용한다.
# 샵 기호는 이후의 문장을 주석<font size="2">comment</font> 로 처리하도록 한다.
# 즉, 파이썬 해석기에 의해 무시되어 코드 실행과 무관해진다.

# In[8]:


5 ** 2    # 5의 제곱


# In[9]:


2 ** 7    # 2의 7승


# :::{admonition} 주의
# :class: warning
# 
# 지수승 연산이 뺄셈 연산 보다 우선된다.
# 예를 들어 `-3**2`는 `-3`의 제곱인 9가 아닌 `-(3**2)`, 즉 `-9`로 계산된다.
# 혼란을 피하기 위해 괄호 사용을 권장한다.
# :::

# ### 변수 할당

# **변수 할당**<font size="2">variable assignment</font>은 
# 변수가 특정 값을 가리키도록 명령하는 것이다.
# 이를 위해 등호 기호 `=` 를 사용한다.

# In[10]:


width = 20
height = 5 * 9


# 변수가 가리키는 값을 대신하여 해당 변수를 연산에 사용할 수 있다.

# In[11]:


width * height


# 변수 할당이 지정되지 않는 변수,
# 즉 정의되지 않은 변수는 사용할 수 없다.
# 
# ```python
# >>> n
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined
# ```

# ## 문자열

# **문자열**은 문자와 기호들의 나열을 의미하며 작은따옴표 또는 끈따옴표로 감싸인다.
# `print()` 함수는 지정된 문자열을 화면에 출력한다.
# 이때 문자열을 감싸는 따옴표를 제고하고 동시에 문자열에 포함된 특별한 기능을 수행하는 문자를
# 적절하게 변환해서 보여준다.

# In[12]:


'spam eggs'


# In[13]:


print('spam eggs')


# 작은따옴표로 감싸인 문자열이 작은따옴표를 포함하도록 하려면
# 백슬래시 `\`기호를 작은따옴표 기호 바로 앞에 추가한다.

# In[14]:


'doesn\'t'


# In[15]:


print('doesn\'t')


# 큰따옴표로 감싸인 문자열에 작은따옴표를 임의로 포함시킬 수 있다.
# 이는 문자열의 시작과 끝이 작은따옴표에도 불구하고 명확하기 때문이다.

# In[16]:


"doesn't"


# In[17]:


print("doesn't")


# 동일한 이유로 작은따옴표로 감싸인 문자열이 큰따옴표를 포함해도 된다.

# In[18]:


'"Yes," they said.'


# In[19]:


print('"Yes," they said.')


# 하지만 큰따옴표로 감싸인 문자열이 큰따옴표를 포함하려면
# 여기서도 백슬래시 기호를 추가해야 한다.

# In[20]:


"\"Yes,\" they said."


# In[21]:


print("\"Yes,\" they said.")


# 문자열에 큰따옴표와 작은따옴표가 동시에 포함되면
# 감싸는 따옴표와 동일한 종류의 따옴표는 백슬래시가 추가되어야 한다.

# In[22]:


'"Isn\'t," they said.'


# `print()` 함수는 백슬래시의 모든 특수 기능을 적절히 반영해서 화면에 출력한다.

# In[23]:


print('"Isn\'t," they said.')


# `\n`은 줄바꿈을 의미하는 문자다.

# In[24]:


s = 'First line.\nSecond line.'


# 변수 `s` 가 가리키는 문자열은 다음과 같다.

# In[25]:


s


# `print()` 함수를 이용하면 실제 의도한 대로 두 줄로 표현된다.

# In[26]:


print(s)


# ### 날 문자열

# 앞서의 경우처럼 작은따옴표, 큰따옴표, 특수 문자에 대해 백슬래시를 사용하냐,
# 그렇지 않냐를 걱정하는 것 대신에
# **날 문자열**<font size="2">raw string</font>을 사용하면 보다 편리하다.
# 날 문자열은 문자열 앞에 `r`을 추가해서 얻어지며
# 그러면 문자열 안에 포함된 모든 특수 문자들의 기능이 제거된다.

# In[27]:


print('C:\some\name')  # 일반 문자열 사용. 줄바꿈 적용됨.


# In[28]:


print(r'C:\some\name')  # 날 문자열 사용. 줄바꿈 없음.


# ### 여러줄 문자열

# 여러 줄로 작성된 문자열은 항상 세개의 작은따옴표 또는 세 개의 큰따옴표로 감싸져야 한다.

# In[29]:


print("""첫째줄(위에 여백 없음!)
둘째줄
셋째줄
""")


# 하지만 다음과 같이 첫째줄에 비어 있는채로 출력된다.

# In[30]:


print("""
첫째줄(위에 여백 있음)
둘째줄
셋째줄
""")


# 이를 방지하려면 백슬래시 기호를 추가한다.

# In[31]:


print("""첫째줄(위에 여백 없음)
둘째줄
셋째줄
""")


# ### 문자열 연산

# 문자열의 `+` 와 `*` 두 기호를 이용한 연산을 지원한다.
# 
# `+` 연산자는 두 문자열을 이어붙인다.

# In[32]:


'hello' + 'python'


# In[33]:


'hello, ' + 'python'


# `*` 연산자는 정수와 문자열을 인자로 받아 정수 만큼 복제해서 이어붙인다.

# In[34]:


3 * 'hello'


# In[35]:


2 * 'hello, ' + "python"


# ### 문자열 인덱싱

# 문자열은 문자 여러 개의 나열이며 문자들 사이의 순서가 중요하다.
# 이때 문자열 왼편에 위치한 문자부터 차례대로 0, 1, 2, ... 

# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
# 
# ```python
# >>> word = 'Python'
# >>> word[0]  # character in position 0
# 'P'
# >>> word[5]  # character in position 5
# 'n'
# ```

# Indices may also be negative numbers, to start counting from the right:
# 
# ```python
# >>> word[-1]  # last character
# 'n'
# >>> word[-2]  # second-last character
# 'o'
# >>> word[-6]
# 'P'
# ```

# Note that since -0 is the same as 0, negative indices start from -1.
# 
# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
# 
# ```python
# >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
# 'Py'
# >>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
# 'tho'
# ```

# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
# 
# ```python
# >>> word[:2]   # character from the beginning to position 2 (excluded)
# 'Py'
# >>> word[4:]   # characters from position 4 (included) to the end
# 'on'
# >>> word[-2:]  # characters from the second-last (included) to the end
# 'on'
# ```

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
# 
# ```python
# >>> word[:2] + word[2:]
# 'Python'
# >>> word[:4] + word[4:]
# 'Python'
# ```

# One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
# 
#      +---+---+---+---+---+---+
#      | P | y | t | h | o | n |
#      +---+---+---+---+---+---+
#      0   1   2   3   4   5   6
#     -6  -5  -4  -3  -2  -1

# The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.
# 
# For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

# Attempting to use an index that is too large will result in an error:
# 
# ```python
# >>> word[42]  # the word only has 6 characters
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# ```

# However, out of range slice indexes are handled gracefully when used for slicing:
# 
# ```python
# >>> word[4:42]
# 'on'
# >>> word[42:]
# ''
# ```

# Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
# 
# ```python
# >>> word[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> word[2:] = 'py'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# ```

# If you need a different string, you should create a new one:
# 
# ```python
# >>> 'J' + word[1:]
# 'Jython'
# >>> word[:2] + 'py'
# 'Pypy'
# ```

# The built-in function len() returns the length of a string:
# 
# ```python
# >>> s = 'supercalifragilisticexpialidocious'
# >>> len(s)
# 34
# ```

# ### 3.1.3. Lists

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
