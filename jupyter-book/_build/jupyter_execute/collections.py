#!/usr/bin/env python
# coding: utf-8

# (ch:collections)=
# # 모음 자료형

# 모음 자료형<font size = "2">Collection Data Types</font>은
# 여러 개의 값을 항목으로 포함하는 값들의 자료형이다.
# 파이썬은 아래 다섯 가지 모음 자료형을 기본으로 제공한다.
# 
# ```
# 문자열, 리스트, 튜플, 집합, 사전
# ```
# 
# 모음 자료형을 구분하는 여러가지 기준이 있다.
# 
# 첫째, 리스트처럼 항목들 사이의 순서를 중요하게 고려하고 항목의 중복 사용을 허용하는 
# 순차<font size="2">sequential</font> 자료형과 
# 집합처럼 그렇지 않은 비순차 자료형으로 나뉜다.
# 
# - 순차 자료형: 문자열, 리스트, 튜플
# - 비순차 자료형: 집합, 사전

# 둘째, 항목 변경의 허용여부에 따라 불변<font size = "2">immutable</font> 자료형과 
# 가변<font size = "2">mutable</font> 자료형으로 나뉜다.
# 
# - 가변 자료형: 리스트, 집합, 사전
# - 불변 자료형: 문자열, 튜플

# (sec:string)=
# ## 문자열

# 문자들을 나열한 값들을 일컫는 자료형으로 작은 따옴표(`'`) 또는 큰 따옴표(`"`)를 사용한다. 
# 
# ```python
# 'Hello, Python!'
# ```
# 
# ```python
# "Hello, Python!"
# ```

# 문자열은 순차 자료형이며, 따라서 항목의 순서 또는 개수가 다르면 서로 다른 문자열로 처리된다.

# In[1]:


'ab' == 'ba'


# In[2]:


'aa' == 'aaa'


# **빈 문자열**
# 
# 빈 문자열은 아무것도 포함하지 않는 문자열이다.
# 빈 문자열을 만드는 방법은 다음 세 가지 방법이 있다.
# 
# ```python
# empty_str = ''
# empty_str = ""
# empty_str = str()
# ```

# **`in` 연산자** 
# 
# 문자열의 일부로 포함된 부분 문자열인지 여부를 판단하는 논리 연산자이다. 

# In[3]:


'app' in 'apple'


# In[4]:


'h' in 'banana' 


# In[5]:


'ca' not in 'coconut'


# **크기 비교 연산**

# 문자열은 사전식의 순서를 사용하며 공백문자, 소문자, 대문자 순으로 크기가 정해진다.

# In[6]:


'a' >= 'A'


# In[7]:


'apple' < 'Hello, World!'


# In[8]:


'Hello, World!' < ' hello'


# **`min()`/`max()` 함수**

# 문자열에 사용된 가장 작은 또는 가장 큰 값의 기호를 반환한다.

# In[9]:


max('apple')


# In[10]:


max('Hello, World!')


# In[11]:


min('banana')


# In[12]:


min('Hello, World!')


# **`len()` 함수**
# 
# 문자열의 길이, 즉 문자열에 포함된 기호의 개수를 반환한다.

# In[13]:


len('apple')


# In[14]:


len('hello, world!')


# 화이트 스페이스는 모두 하나의 기호로 간주된다.

# In[15]:


len('hello,\t\nworld!')


# ### 문자열 인덱싱

# 문자열에 포함된 모든 문자는 인덱스<font size = "2">index</font>라는 고유한 번호를 갖는다.
# 인덱스는 0부터 시작하며, 오른쪽으로 한 문자씩 이동할 때마다 증가한다.
# **인덱싱**<font size = "2">indexing</font>은 인덱스를 활용하여 문자열에 포함된 특정 문자를 확인한다.

# In[16]:


colors = 'red, blue, yellow'


# In[17]:


colors[0] #0번 인덱스 값


# In[18]:


colors[5] #3번 인덱스 값


# 문자열의 길이와 같거나 큰 인덱스를 사용하면 오류가 발생한다. 
# 
# ```python
# >>> len(colors)
# 17
# >>> colors[50]
# IndexError                                Traceback (most recent call last)
# /tmp/ipykernel_1817/3232567937.py in <module>
# ----> 1 colors[50]
# 
# IndexError: string index out of range
# ```

# 인덱스 값으로 음의 정수를 사용할 수 있다. 
# -1을 마지막 문자의 인덱스로 사용하고, 왼쪽으로 한 문자씩 이동할 때마다 감소한다.  

# In[19]:


colors[-1] # 오른쪽 끝에 위치한 문자


# In[20]:


colors[-2] # 오른쪽 끝에서 두 번째 문자


# ### 문자열 슬라이싱

# 인덱스의 특정 구간에 해당하는 부분 문자열을 확인하려 할 때는 
# **슬라이싱**<font size = "2">slicing</font>을 사용한다.
# 슬라이싱은 다음과 같이 실행한다.  
# 
# * 시작 인덱스 : 해당 인덱스부터 문자 확인
# * 끝 인덱스 : 해당 인덱스 이전까지의 문자 확인
# * 계단: 시작 인덱스부터 몇 계단씩 건너뛰며 문자를 추출할지 결정. 
#     계단의 크기가 1이면 생략 가능.

# In[21]:


colors = 'red, blue, yellow'


# `colors`에서 `red`를 추출하고 싶다면 다음과 같이 하면 된다. 

# In[22]:


colors[0 : 3 : 1]


# `colors`에서 `b`부터 끝까지 하나씩 건너서 추출하려면 다음과 같이 하면 된다. 

# In[23]:


colors[5 : len(colors) : 2]


# 양의 정수와 음의 정수를 섞어서 인덱스로 사용할 수 있다.

# In[24]:


colors[5 : -1 : 2]


# 시작인덱스, 끝인덱스, 계단 각각의 인자는 경우에 따라 생략될 수도 있다. 
# 그럴 때는 각각의 위치에 대해 설정된 기본값이 사용된다.
# 
# * `시작 인덱스`의 기본값 : `0`  
# * `끝 인덱스`의 기본값 : 문자열의 길이  
# * `계단`의 기본값 : `1`

# In[25]:


colors[ : 3 : ]


# In[26]:


colors[ : 3] #계단을 생략할 떄는 콜론(:)도 함께 생략가능


# In[27]:


colors[5 : : 2]


# **역순 슬라이싱**
# 
# 슬라이싱은 기본적으로 작은 인덱스에서 큰 인덱스 방향으로 확인한다. 
# 하지만 역순으로 확인하고자 한다면 계단에 음의 정수를 사용하면 된다.
# 계단이 `-1`이고, 시작 인덱스와 끝 인덱스를 생략하면 문자열 전체를 역순으로 확인한다.

# In[28]:


colors[ : : -1]


# :::{admonition} 주의
# :class: caution  
# 
# 문자열은 불변 자료형이라 인덱싱 또는 슬라이싱을 사용하여 값의 일부를 변경할 수 없다.
# 
# ```python
# >>> a_word = 'hello'
# >>> a_word[0] = 'H'
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/217255829.py in <module>
#       1 a_word = 'hello'
# ----> 2 a_word[0] = 'H'
# 
# TypeError: 'str' object does not support item assignment
# ```
# :::

# ### 문자열 메서드 

# 문자열 자료형에만 사용하는 함수들이 있다. 이와같이 특정 자료형에만 사용하는 함수들을 메서드<font size = "2">method</font>라 부른다.
# 메서드는 일반적인 함수들과는 달리, 특정 자료형의 값을 먼저 언급하고 바로 이어서 점(`.`)을 찍은 다음 호출한다.

# 문자열 자료형이 제공하는 주요 메서드는 아래 표와 같다. 

# |메서드|설명|
# |:---|:---|
# |`count()`|지정된 문자열이 등장한 횟수 반환|
# |`find()`|지정된 문자열이 처음 등장한 위치 반환. 지정된 문자열이 없다면 -1반환|
# |`index()`|지정된 문자열이 처음 등장한 위치 반환. 지정된 문자열이 없다면 오류발생|
# |`lower()`|문자열에 사용된 문자를 모두 소문자로 변환한 문자열 반환|`words.lower()`|
# |`upper()`|문자열에 사용된 문자를 모두 대문자로 변환한 문자열 반환|`words.upper()`|
# |`replace()`|하나의 문자열을 다른 문자열로 대체한 문자열 반환|`words.replace('so ', '')`|
# |`lstrip()`|문자열 왼쪽에서 지정된 부분 문자열을 삭제한 문자열 반환. 지정된 부분 문자열이 없는 경우 왼쪽 공백들을 삭제한 문자열 반환|
# |`rstrip()`|문자열 오른쪽에서 지정된 부분 문자열을 삭제한 문자열 반환. 지정된 부분 문자열이 없는 경우 오른쪽 공백들을 삭제한 문자열 반환|
# |`strip()`|문자열 양쪽에서 지정된 부분 문자열을 삭제한 문자열 반환. 지정된 문자열이 없는 경우 양쪽 공백들을 삭제한 문자열 반환|
# |`split()`|문자열을 지정된 기준으로 쪼개서 생성된 문자열들로 구성된 리스트 반환. 지정된 문자열이 없는 경우 공백을 기준 사용|
# |`join()`|지정된 문자열에 포함된 모든 문자들 사이에 지정된 문자열이 삽입된 문자열 반환|

# - `count()` 메서드

# In[29]:


words = " My life is so cool, my life is so cool "


# In[30]:


words.count('so')


# * `find()` 메서드

# In[31]:


words.find('life')


# * `index()` 메서드

# In[32]:


words.index('My')


# * `lower()` 메서드

# In[33]:


words.lower()


# * `upper()` 메서드

# In[34]:


words.upper()


# * `replace()` 메서드

# In[35]:


words.replace('so ', 'that')


# * `lstrip()` 메서드

# In[36]:


words.lstrip()


# * `rstrip()` 메서드

# In[37]:


words.rstrip()


# * `strip()` 메서드

# In[38]:


words.strip()


# * `split()` 메서드

# In[39]:


words.split()


# * `join()` 메서드

# In[40]:


'-'.join('Hello')


# (sec:list)=
# ## 리스트

# 리스트는 유한개의 값들을 모아서 하나의 값으로 취급하는 자료형이다.
# 대괄호(`[]`)를 사용하고, 각 항목은 콤마(`,`)로 구분한다. 

# In[41]:


[1, 2, 3, 4, 5]


# In[42]:


['a', 'b', 'c']


# 리스트는 아래와 같이 서로 다른 자료형의 항목들을 포함할 수 있다.

# In[43]:


mixed_list = [1, 2.3, 'abc', True, [1, 2], ('a', 'b')]


# 리스트는 순차 자료형이며, 따라서 항목의 순서 또는 개수가 다르면 서로 다른 리스트로 처리된다.

# In[44]:


[1, 2] == [2, 1]


# In[45]:


[1] == [1, 1]


# **빈 리스트**
# 
# 빈 리스트<font size = "2">empty list</font>는 아무것도 포함하지 않는 리스트를 의미한다.
# 빈 리스트를 만드는 방법은 아래와 같다. 
# 
# ```python
# empty_list = []
# empty_list = list()
# ```

# 아래 `a_singleton`은 빈 리스트가 아니라 빈 리스트를 포함하는 리스트를 가리킨다.

# In[46]:


a_singleton = [[]]
print(a_singleton)


# **`in` 연산자**
# 
# 리스트의 항목으로 등장하는지 여부를 알려주는 논리 연산자이다.

# In[47]:


3 in [1, 2, 3, 4, 5]


# In[48]:


'a' in [1, 2, 3, 4, 5]


# In[49]:


'a' not in [1, 2, 3, 4, 5]


# **리스트 연산**
# 
# 문자열의 경우처럼 리스트도 이어붙이기와 복제 연산자를 사용한다.

# In[50]:


['a', 'b'] + ['b', 'c', 'd']


# In[51]:


['a', 'b'] * 2


# In[52]:


2 * ['a', 'b']


# **`min()`/`max()` 함수**
# 
# 항목 중에서 최솟값 또는 최댓값을 확인한다.

# In[53]:


a_list = [3, 15, 9, 12]


# In[54]:


max(a_list)


# In[55]:


min(a_list)


# **`len()`함수** 
# 
# 리스트의 길이, 즉 리스트에 포함된 항목의 개수를 반환한다.

# In[56]:


len(a_list)


# ### 리스트 인덱싱/슬라이싱

# 리스트도 문자열처럼 인덱싱과 슬라이싱을 지원하며
# 사용방식도 거의 동일하다.

# In[57]:


a_list = [3, 15, 9, 12, 7, 14, 10]


# In[58]:


a_list[0]


# In[59]:


a_list[-1]


# In[60]:


a_list[2 : 5]


# In[61]:


a_list[2 : 6 : 2]


# In[62]:


a_list[:: -1]


# 리스트는 가변 자료형이라 값을 변경할 수 있다.
# 예를 들어, 인덱싱을 사용하여 `a_list[3]`을 `12`에서 `100`으로 변경할 수 있다. 

# In[63]:


a_list[3] = 100

print(a_list)


# 이번에는 슬라이싱을 사용하여 2번 인덱스 값부터 5번 인덱스 값 전까지를 1과 11로 변경해보자. 

# In[64]:


a_list[2 : 5] = [1, 11]

print(a_list)


# **`del` 명령어**

# `del` 명령어를 사용하여 리스트의 일부 또는 전체를 삭제할 수 있다. 

# In[65]:


print(a_list)


# In[66]:


del a_list[0]
print(a_list)


# :::{admonition} 주의
# :class: caution  
# 
# `del` 명령어로 리스트를 메모리에서 삭제할 수 있다. 
# 이런 경우 리스트를 사용하려 하면 오류가 발생한다.
# 
# ```python
# >>> del a_list
# >>> print(a_list)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_647/65709556.py in <module>
# ----> 1 print(a_list)
# 
# NameError: name 'a_list' is not defined
# ```
# :::

# ### 리스트 메서드 

# 리스트 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|
# |:----------|:----------|
# |`list.append()`|리스트 끝에 항목 추가. 반환값은 `None`|
# |`list.extend()`|리스트를 연결하여 확장. 반환값은 `None`|
# |`list.insert()`|지정된 인덱스에 항목 추가. 반환값은 `None`|
# |`list.pop()`|지정된 인덱스의 항목 삭제 후 삭제된 값 반환. 지정된 인덱스가 없다면 마지막 항목 삭제 후 삭제된 값 반환|
# |`list.remove()`|지정된 항목이 처음으로 사용된 위치에서 삭제. 반환값은 `None`|
# |`list.sort()`|리스트의 항목을 크기 순으로 정렬. 반환값은 `None`|
# |`list.reverse()`|리스트의 항목들 순서 뒤집기. 반환값은 `None`|
# |`list.index()`|지정된 항목이 처음 위치한 인덱스 반환|
# |`list.count()`|지정된 항목이 등장한 횟수 반환|
# 
# 

# In[67]:


food = ['banana', 'apple', 'coconut', 'apple']


# * `append()`  : 리스트 끝에 항목 추가. 반환값은 `None`   

# In[68]:


print(food.append('durian'))


# In[69]:


food


# 리스트 끝에 `eggplant`와 `fig`를 아래와 같이 추가해보자. 

# In[70]:


food.append(['eggplant', 'fig'])

food


# 그러면 `food` 리스트 끝에 두 개의 항목이 추가되는 것이 아니라 `['eggplant', 'fig']`리스트가 추가된 것을 볼 수 있다.  
# 지금은 `del`을 사용하여 추가된 마지막 항목을 삭제한다. 

# In[71]:


del food[-1]


# 두 개의 항목을 리스트에 추가하고자 한다면 `append()` 메서드를 두 번 적용하거나 `extend()` 메서드를 사용하면 된다.  

# * `extend()` : 리스트를 연결하여 확장. 반환값은 `None`

# In[72]:


food.extend(['eggplant', 'fig'])
food


# :::{admonition} 참고   
# :class: info   
# 두 개의 리스트를 덧셈 기호를 이용하여 확장할 수도 있지만, 원래의 리스트를 변경하는 것이 아니라 새로운 리스트를 생성한다.
# 
# ```python
# >>> food = ['banana', 'apple', 'coconut', 'apple']
# >>> food + ['eggplant', 'fig']
# ['banana', 'apple', 'coconut', 'apple', 'eggplant', 'fig']
# >>> food
# ['banana', 'apple', 'coconut', 'apple']
# ```
# :::

# * `insert()` : 지정된 인덱스에 항목 추가. 반환값은 `None`

# In[73]:


food.insert(1, 'blueberry')
food


# * `pop()` : 지정된 인덱스의 항목 삭제 후 삭제된 값 반환. 지정된 인덱스가 없다면 마지막 항목 삭제 후 삭제된 값 반환.

# In[74]:


food.pop()


# In[75]:


food


# In[76]:


food.pop(0)


# In[77]:


food


# * `remove()` : 지정된 항목이 처음으로 사용된 위치에서 삭제. 반환값은 `None`

# In[78]:


food.remove('apple')
food


# * `sort()` : 리스트의 항목을 크기 순으로 정렬. 반환값은 None  
#     * 숫자의 경우, 크기 순서대로
#     * 문자의 경우, 사전식으로

# In[79]:


food.sort()


# In[80]:


food


# * `reverse()` : 리스트의 항목들 순서 뒤집기. 반환값은 None

# In[81]:


food.reverse()


# In[82]:


food


# * `index()` : 지정된 항목이 처음 위치한 인덱스 반환.

# In[83]:


food.index('coconut')


# * `count()` : 지정된 항목이 등장한 횟수 반환

# In[84]:


food.count('apple')


# (sec:tuple)=
# ## 튜플

# 튜플은 리스트와 거의 비슷하지만, 수정 불가능<font size = "2">immutable</font>하다는 점이 다르다. 튜플의 형식은 아래와 같다. 

# `(항목1, 항목2, 항목3, ..., 항목n)`

# 소괄호(`()`)를 사용하고, 각 항목은 콤마(`,`)로 구분한다. 

# In[85]:


(1, 2, 3, 4, 5)


# In[86]:


('a','b', 'c', 'd')


# :::{admonition} 주의     
# :class: caution  
# 
# 항목이 하나인 튜플을 만들 때는 항목 뒤에 콤마(`,`)를 꼭 붙여줘야 한다. 
# 
# ```python
# >>> tup1 = (3)
# >>> print(type(tup1))
# <class 'int'>
# >>> tup2 = (3, )
# >>> print(type(tup2))
# <class 'tuple'>
# ```
# :::

# 튜플은 아래와 같은 방식으로 타입 힌트를 추가한다.  

# In[87]:


from typing import Tuple 
a_tuple : Tuple[int, int, str] = (2022, 12345, '강현')
a_tuple


# 튜플은 아래와 같이 서로 다른 자료형의 항목들을 포함할 수 있지만, 일반적으로 항목들이 모두 같은 자료형인 경우를 많이 사용한다. 

# In[88]:


mixed_tuple = (1, 2.3, 'abc', False, ['ab', 'c'], (2, 4))
mixed_tuple


# **빈 튜플**
# 
# 빈 튜플<font size = "2">empty tuple</font>은 아무것도 포함하지 않는 튜플을 의미한다. 빈 튜플를 만드는 방법은 아래와 같다. 

# In[89]:


empty_tuple = ()
empty_tuple = tuple()
empty_tuple


# **항목 포함 여부 연산자**
# 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 튜플의 항목으로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 튜플의 항목으로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[90]:


'1' in ('a', 'bc', 'd', 'e')


# In[91]:


'd' in ('a', 'bc', 'd', 'e')


# In[92]:


'f' not in ('a', 'bc', 'd', 'e')


# ### 튜플 연산  

# 튜플은 사칙연산 중 덧셈과 곱셈 연산자를 사용할 수 있다. 

# In[93]:


('a', 'b') + ('b', 'c', 'd')


# In[94]:


('a', 'b') * 2


# **`len()`함수**
# 
# len()함수 : 튜플의 길이 확인

# In[95]:


len(('a', 'b', 'c', 'd'))


# **최대, 최소 함수**
# 
# * `max()` 함수 : 최댓값 확인

# In[96]:


max((2, 9, 11, 20, 3))


# * `min()` 함수 : 최솟값 확인

# In[97]:


min((2, 9, 11, 20, 3))


# ### 튜를 인덱싱과 슬라이싱

# 튜플도 문자열과 리스트처럼 인덱싱과 슬라이싱이 가능하다. 

# In[98]:


a_tuple = (3, 15, 9, 12, 7, 14, 10)
print(a_tuple[0])
print(a_tuple[-1])
print(a_tuple[2:6:2])


# :::{admonition} 주의   
# :class: caution  
# 튜플은 불변 자료형이라 값을 수정할 수 없다. 예를 들어, 아래와 같이 인덱싱을 사용하여 튜플의 항목을 변경하려고 하면 오류가 발생한다.   
# 
# ```python
# >>> a_tuple = (3, 15, 9, 12, 7, 14, 10)
# >>> a_tuple[0] = 100
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/347940049.py in <module>
#       1 a_tuple = (3, 15, 9, 12, 7, 14, 10)
# ----> 2 a_tuple[0] = 100
# 
# TypeError: 'tuple' object does not support item assignment
# ```
# :::

# :::{admonition} 참고   
# :class: info  
# 
# 튜플이 변경 불가능한 자료형이라고 해서 튜플의 모든 항목이 모두 변경 불가능해야 하는 것은 아니다. 예를 들어, `tup`의 첫번째 항목은 `[1, 2]`이고, 리스트는 변경가능한 자료형이다. 따라서 아래와 같이 첫번째 항목 자체는 변경이 가능하다. 
# ```python
# >>> tup = ([1, 2], 10, 100)
# >>> tup[0].append(3)
# >>> print(tup)
# ([1, 2, 3], 10, 100)
# ```
# 
# 이러한 성질이 가능한 이유는 아래와 같다.  
# `tup`은 `([1, 2], 10, 100)`을 참조한다. 그리고 첫번째 항목인 `[1, 2]` 또한 참조 형태로 다른 메모리에 저장된다. 즉, `tup`의 첫번째 항목은 `[1, 2]`가 저장된 위치의 주소이다. 그런데 `[1, 2]`가 변경되어도 주소 자체는 변하지 않는다. 따라서 `tup` 입장에서는 변한 것이 하나도 없다. 
# 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch04/tuple01.png" style="width:400px;">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch04/tuple02.png" style="width:400px;">
# </div>
# 
# 
# :::

# ### 튜플 메서드

# 튜플은 불변 자료형이라 메서드가 별로 없다. 많이 사용되는 두 개의 메소드를 살펴보자.   
# 
# |메서드|설명|
# |:----------:|:----------:|
# |`tuple.count()`|지정된 항목이 등장한 횟수 반환|
# |`tuple.index()`|지정된 항목이 처음 위치한 인덱스 반환|

# In[99]:


num_tuple = (1, 2, 3, 1, 3, 5, 5, 10, 15)
print(num_tuple.count(1))
print(num_tuple.index(5))


# ## `zip()` 함수

# 시퀀스(예, 문자열, 리스트, 튜플) 여러 개의 항목을 순서대로 짝지어 튜플의 리스트 형식의 객체를 생성한다. 자료형이 달라도 된다. 단, `zip()` 함수의 반환값은 구체적으로 명시되지 않는다. 

# In[100]:


zip("abc", [1, 2, 3])


# `list()`함수를 이용하여 리스트로 변환하면, 쉽게 내용을 확인할 수 있다. 

# In[101]:


list(zip("abc", [1, 2, 3]))


# 여러 개를 짝짓는 것도 가능하며, 각 자료형의 길이가 다르면 짧은 길이에 맞춰서 짝을 짓는다. 

# In[102]:


list(zip("abcdefgh",(1, 2, 3, 4, 5), [5, 10, 15]))


# ### 해체 방법

# 시퀀스 항목 각각을 변수에 지정하고자 할 때는 해체하는 방법을 사용한다. 단, 사용되는 변수의 수는 항목의 수와 일치해야 한다.   
# 예를 들어, 세 개의 항목을 갖는 시퀀스를 해체하려면 세 개의 변수가 필요하다. 

# In[103]:


a, b = "12"
c, d, e = [3, 4, 5]
f, g = (6, 7)
print(a) 
print(type(a)) # 타입은 문자열이다.
print(b) #타입 - str
print(c) #타입 - int
print(d) #타입 - int
print(e) #타입 - int
print(f) #타입 - int
print(g) #타입 - int


# 굳이 이름을 주지 않아도 되는 항목이 있다면 변수 대신에 밑줄<font size = "2">underscore</font>(`_`) 기호를 사용한다.   
# 예를 들어, 변수 `d`가 필요없다면 아래와 같이 해체할 수 있다. 

# In[104]:


c, _, e = [3, 4, 5]
print(c + e)


# :::{admonition} 주의   
# :class: caution  
# 시퀀스 항목 각각을 변수에 지정하고자 할 때는 사용되는 변수의 수와 항목의 수는 일치해야 한다.
# 
# ```python
# >>> c, e = [3, 4, 5]
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_1817/4065688922.py in <module>
# ----> 1 c, e = [3, 4, 5]
#       2 print(c + e)
# 
# ValueError: too many values to unpack (expected 2)
# ```
# :::

# 반면에 앞에 몇 개만 변수에 할당하고 나머지는 하나의 리스트로 묶을 수도 있다. 이를 위해 별표 기호<font size = "2">asterisk</font>(`*`)를 하나의 변수명과 함께 사용한다. 

# In[105]:


values = (1, 2, 3, 4, 5)
a, b, *rest = values
print(a)
print(b)
print(rest)


# 나머지 항목들을 무시하고 싶다면, 별표와 밑줄을 함께 사용한다. 

# In[106]:


a, b, *_ = values
print(a)
print(b)


# ## 집합

# 집합<font size = "2">set</font>형은 수학에서 다루는 집합과 비슷한 자료형으로 형식은 아래와 같다.  

# `{항목1, 항목2, 항목3, ..., 항목n}`

# 중괄호(`{}`)를 사용하고, 각 항목은 콤마(`,`)로 구분한다.

# 집합은 항목의 중복을 허용하지 않고, 항목들 사이의 순서는 무시된다. 

# In[107]:


a_set = {4, 9.2, "apple", True, 4}
a_set


# :::{admonition} 참고  
# :class: info  
# 집합의 원소는 모두 해시 가능이어야 한다. 즉, 리스트는 집합의 원소가 될 수 없다. 
# ```python
# >>> {[1, 3], 4}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/2739416386.py in <module>
# ----> 1 {[1, 3], 4}
# 
# TypeError: unhashable type: 'list'
# ```
# :::

# :::{admonition} 해시 가능 <font size = "2">hashable</font>  
# :class: info  
# 
# 어떤 객체가 변하지 않는 해시값을 갖고, 다른 객체와 비교될 수 있으면 해시 가능이라고 한다.  
# 파이썬의 모든 불변 내장 객체들은 해시 가능하다. 반면 리스트나 딕셔너리와 같은 가변 객체들은 해시 불가능이다.  
# 집합의 원소나 딕셔너리의 키는 해시 가능한 것만 사용할 수 있다. 
# 
# 
# `hash()` 함수를 사용하여 해시 가능 여부를 확인할 수 있다.   
# `hash()` 함수는 해시 가능일 때는 특정 정수를 반환하고, 불가능일 때는 오류가 발생한다.  
# ```python
# >>> hash(1)
# 1
# >>> hash([1, 2])
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/3864786969.py in <module>
# ----> 1 hash([1, 2])
# 
# TypeError: unhashable type: 'list'
# ```
# 
# :::

# :::{admonition} 주의  
# :class: caution  
# 집합은 순서가 없는 자료형이라 인덱싱이나 슬라이싱을 지원하지 않는다.   
# ```python
# >>> a_set[0]
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/3483571857.py in <module>
# ----> 1 a_set[0]
# 
# TypeError: 'set' object is not subscriptable
# ```
# :::

# 집합은 아래와 같은 방식으로 타입 힌트를 추가한다.  

# In[108]:


from typing import Set 
a_set : Set[int] = {1, 5, 9, 7}
a_set


# **빈 집합**

# 빈 집합<font size = "2">empty set</font>은 아무것도 포함하지 않는 집합을 의미한다. 빈 집합를 만드는 방법은 아래와 같다. 

# In[109]:


empty_set = set()
empty_set


# :::{admonition} 주의  
# :class: caution  
# 
# 빈 집합을 만들 때는 `set()`을 사용해야 한다. `{}`은 빈 딕셔너리이다. 
# ```python
# >>> a = {}
# >>> type(a)
# dict
# ```
# :::

# **항목 포함 여부 연산자**
# 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 집합의 항목으로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 집합의 항목으로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[110]:


1 in {1, 2, 3, 9, 4}


# In[111]:


'a' not in {1, 'b', True, 9}


# ### 집합 연산

# 집합에서 사용할 수 있는 연산자는 아래와 같다. 

# |연산자|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`\|`|합집합|`{1, 2} \| {2, 4}`|`{1, 2, 4}`|
# |`&`|교집합|`{1, 2} & {2, 4}`|`{2}`|
# |`-`|차집합|`{1, 2} - {2, 4}`|`{1}`|
# |`<=`|부분집합 여부|`{1, 2} <= {2, 4}`|`False`|

# In[112]:


{1, 2, 3, 4, 5} | {2, 4, 6}


# In[113]:


{1, 2, 3, 4, 5} & {2, 4, 6}


# In[114]:


{1, 2, 3, 4, 5} - {2, 4, 6}


# In[115]:


{1, 2, 3, 4, 5} <= {2, 4, 6}


# In[116]:


{1, 2} <= {1, 2, 3, 4, 5}


# :::{admonition} 주의  
# :class: caution  
# 
# 집합은 덧셈과 곱셈 연산자를 사용할 수 없다. 
# 
# ```python 
# >>> {1, 2} + {3, 4, 5}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/437379440.py in <module>
# ----> 1 {1, 2} + {3, 4, 5}
# 
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# 
# >>> {1, 2} * 2
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/650599529.py in <module>
# ----> 1 {1, 2} * 2
# 
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
# ```
# :::

# **`len()` 함수**
# 
# len()함수 : 집합의 길이 확인

# In[117]:


len({1, 3, 5, 7, 9})


# **최대, 최소 함수**
# 
# * `max()` 함수 : 최댓값 확인

# In[118]:


max({1, 3, 5, 7, 9})


# * `min()` 함수 : 최솟값 확인

# In[119]:


min({1, 3, 5, 7, 9})


# ### 집합 메서드  

# 집합 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`set.union()`|합집합 반환|`{1, 2}.union({3, 4})`|`{1, 2, 3, 4}`|
# |`set.intersection()`|교집합 반환|`{1, 2, 3}.intersection({3, 4})`|`{3}`|
# |`set.difference()`|차집합 반환|`{1, 2, 3}.difference({3, 4})`|`{1, 2}`|
# |`set.issubset()`|부분 집합 여부를 판단하여 반환|`{1, 2, 3}.issubset({3, 4})`|`False`|
# |`set.add()`|항목추가. 반환값은 `None`|||
# |`set.remove()`|특정 항목 삭제. 반환값은 `None`|||
# |`set.pop()`|임의의 항목 삭제. 반환값은 삭제하는 항목. 빈 집합에 사용하면 오류 발생|||
# |`set.clear()`|모든 항목을 삭제. 반환값은 `None`|||
# |`set.update()`|여러 개의 항목 한번에 추가. 반환값은 `None`|||

# In[120]:


a_set = {1, 2, 3}
a_set.add(8)
print(a_set)


# In[121]:


a_set.remove(1)
print(a_set)


# In[122]:


print(a_set.pop())
print(a_set)


# In[123]:


a_set.clear()
print(a_set)


# In[124]:


a_set.update({5, 10, 15})
print(a_set)


# ## 사전 

# 사전형 또는 딕셔너리<font size = "2">dictionary</font> 자료형은 키<font size = "2">keys</font>와 값<font size = "2">values</font>으로 이루어진 항목<font size = "2">items</font>들의 집합으로, 사전에서 단어의 뜻을 확인하는 방식과 유사하게 활용할 수 있는 자료구조를 가지고 있다. 예를 들어, 영어 사전에서 `world`란 단어의 뜻을 물으면 `세계`라는 뜻을 알려주는 데, 이때 `world`는 키<font size = "2">key</font>에 해당하고, `세계`는 값<font size = "2">value</font>에 해당한다.   
# 
# 딕셔너리의 형식은 아래와 같다.   
# 
# `{key1 : value1, key2 : value2, key3 : value3, ...}`  
# 
# `key : value` 형태로 이루어진 여러 개의 항목들이 중괄호(`{}`)로 묶여있고, 각 항목들은 콤마(`,`)로 구분한다.  
# 
# 예를 들어, key가 `'Hello'`, `'World'`이고, 각각의 key에 대응하는 value가 `'안녕'`, `'세계'`인 딕셔너리 `dic`를 만드는 코드를 아래와 같다. 

# In[125]:


dic = {'Hello' : '안녕', 'World' : '세계'}
dic


# :::{admonition} 참고  
# :class: info  
# 해시 가능한 것만 딕셔너리의 키로 사용될 수 있다. 예를 들어, 정수, 부동소수점, 문자열, 튜플 등이다.  
#  
# ```python
# >>> dic = {1 : 5, 2.5 : [3, 4], 'a' : (2, 7, 4), (1, 2) : 'd'}
# >>> print(dic)
# {1: 5, 2.5: [3, 4], 'a': (2, 7, 4), (1, 2): 'd'}
# ```
# 
# 단, 키로 사용되는 튜플의 항목에 리스트 등 변경 가능한 값이 사용되지 않아야 한다. 
# ```python
# >>> {([1, 2], 3): 1}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/230770617.py in <module>
# ----> 1 {([1, 2], 3): 1}
# 
# TypeError: unhashable type: 'list'
# ```
# :::

# 사전은 아래와 같은 형식으로 타입 힌트를 추가한다. 

# In[126]:


from typing import Dict
a_dict : Dict[str, str] = {"name": "강현", "age": "3"}


# **빈 사전**

# 빈 사전 또는 빈 딕셔너리<font size = "2">empty dictionary</font>는 아무것도 포함하지 않는 사전을 의미한다. 빈 사전를 만드는 방법은 아래와 같다. 

# In[127]:


empty_dict = {}
empty_dict = dict()
empty_dict


# **항목 포함 여부 연산자**
# 
# * `in` :  연산자 왼쪽에 있는 값이 오른쪽에 있는 사전의 키로 등장하는지 여부를 알려주는 논리 연산자
# * `not in` : 연산자 왼쪽에 있는 값이 오른쪽에 있는 사전의 키로 등장하지 않는지 여부를 알려주는 논리 연산자

# In[128]:


'city' in {"name": "강현", "age": "3"} 


# In[129]:


'city' not in {"name": "강현", "age": "3"} 


# **`len()` 함수**
# 
# len()함수 : 사전에서 항목의 길이 확인

# In[130]:


len({"name": "강현", "age": "3"}) 


# **최대, 최소 함수**
# 
# * `max()` 함수 : 사전의 키의 최댓값 확인

# In[131]:


max({1 : 'one', 2 : 'two', 3 : 'three'})


# * `min()` 함수 : 사전의 키의 최솟값 확인

# In[132]:


min({1 : 'one', 2 : 'two', 3 : 'three'})


# ### 사전 인덱싱 

# 딕셔너리에서 항목의 순서는 중요하지 않다. 그보다 어떤 키<font size = "2">key</font>가 사용되었는지가 중요하다.  
# 딕셔너리에서 인덱싱은 키를 이용한다. 예를 들어, 아래 딕셔너리 `dic`에서 `'Hello'`에 대응하는 값을 확인하고자 하면  
# 다음과 같이 대괄호를 사용하는 인덱싱을 이용한다. 

# In[133]:


dic = {'Hello' : '안녕', 'World' : '세계'}
dic['Hello']


# :::{admonition} 주의  
# :class: caution  
# 
# 존재하지 않는 키로 값을 추출하려고 하면, 오류가 발생한다. 
# ```python
# >>> dic = {'Hello' : '안녕', 'World' : '세계'}
# >>> dic['Python']
# KeyError                                  Traceback (most recent call last)
# /tmp/ipykernel_1817/1517958361.py in <module>
# ----> 1 dic['Python']
# 
# KeyError: 'Python'
# ```
# :::

# ### 항목의 추가와 삭제 

# * 아래와 같은 형식으로 사전에 항목을 추가한다.  
# `사전변수명[key] = value`   
# 
# 예를 들어, `dic`에 key와 value가 각각 `Python`과 `파이썬`인 항목을 추가하는 코드는 아래와 같다.   

# In[134]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(dic)
dic['Python'] = '파이썬'
print(dic)


# :::{admonition} 주의  
# :class: caution  
# 이미 사용하고 있는 키를 가진 항목을 추가하려고 하면, 그 키로 저장된 이전 값은 사라진다.  
# ```python
# >>> dic = {'Hello' : '안녕', 'World' : '세계'}
# >>> print(dic)
# {'Hello': '안녕', 'World': '세계'}
# >>> dic['World'] = '세상'
# >>> print(dic)
# {'Hello': '안녕', 'World': '세상'}
# ```
# :::

# * 사전의 항목은 `del` 명령어를 사용하여 삭제할 수 있다. 

# In[135]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(dic)
del dic['World']
print(dic)


# ### 사전 메서드 

# 사전 자료형이 제공하는 주요 메서드는 아래와 같다.

# In[136]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# |메서드|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`dict.keys()`|사전에 사용된 key들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 반환|`dic.keys()`|`dict_keys(['Hello', 'World'])`|
# |`dict.values()`|사전에 사용된 value들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 반환|`dic.values()`|`dict_values(['안녕', '세계'])`|
# |`dict.items()`|사전에 사용된 item들을 모두 모아서 리스트와 비슷한 자료형으로 만들어서 반환|`dic.items()`|`dict_items([('Hello', '안녕'), ('World', '세계')])`|
# |`dict.get()`|key에 대응되는 value를 반환. 존재하지 않는 key를 사용하면 `None`을 반환|`dic.get('Hello')`|`'안녕'`|
# |`dict.update()`|다른 사전과 합함. 반환값은 `None`|`dic.update({'Python' : '파이썬', 'Programming' : '프로그래밍'})`|`None`|
# |`dict.pop()`|key에 해당하는 항목을 삭제. 반환값은 key에 대응하는 value. key가 존재하지 않으면 오류 발생.|`dic.pop('Python')`|`'파이썬'`|
# |`dict.clear()`|사전 안의 모든 항목들을 삭제. 반환값은 `None`|`dic.clear()`|`None`|

# In[137]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(dic)
print(dic.update({'Python' : '파이썬', 'Programming' : '프로그래밍'}))
print(dic)


# In[138]:


print(dic)
print(dic.pop('Python'))
print(dic)


# In[139]:


print(dic)
print(dic.clear())
print(dic)


# ## 형변환함수

# **`list()` 함수**

# `list()` : 리스트형으로 변환.

# In[140]:


list('abc')  #문자열의 각 문자를 항목으로 갖는 리스트 반환


# In[141]:


list((1, 2, 3))


# In[142]:


list({1, 2, 5})


# In[143]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(list(dic))
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))


# **`tuple()` 함수**

# `tuple()` : 튜플형으로 변환.

# In[144]:


tuple('abc')


# In[145]:


tuple([1, 2, 3])


# In[146]:


tuple({1, 2, 5})


# In[147]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(tuple(dic))
print(tuple(dic.keys()))
print(tuple(dic.values()))
print(tuple(dic.items()))


# **`set()` 함수**

# `set()` : 집합형으로 변환.

# In[148]:


set('abc')


# In[149]:


set([1, 1, 2, 5])


# In[150]:


set((1, 3, 3, 9, 1))


# In[151]:


dic = {'Hello' : '안녕', 'World' : '세계', 'Hi' : '안녕'}
print(set(dic))
print(set(dic.keys()))
print(set(dic.values()))
print(set(dic.items()))


# **`dict()` 함수**

# `dict()` : 사전형으로 변환.  
# 
# 사전의 각 항목은 키와 값으로 이루어졌기 때문에 적절하게 짝지어진 데이터를 사용해야 사전을 만들 수 있다.

# In[152]:


data = [('Hello', '안녕'), ('World', '세계'), ('Programming', '프로그래밍')]
dict(data)


# In[153]:


data = zip('abcde', [1, 2, 3, 4, 5])
dict(data)


# In[154]:


dict(Hello = '안녕', World = '세계', Programming = '프로그래밍')


# ## 조건제시법

# 리스트, 집합, 사전은 조건제시법<font size = "2">comprehension</font>을 이용하여 정의할 수 있다.

# ### 리스트 조건제시법

# 리스트 조건제시법은 수학에서 집합을 정의할 때 사용하는 조건제시법과 매우 유사한다.   
# 
# * 0과 10사이에 있는 홀수들의 제곱을 원소로 갖는 집합을 조건제시법으로 표현한다.  
# { x^2 | 0 <= x <= 10, 단 x는 홀수 }
# 
# * 집합 기호를 리스트 기호로 대체한다.   
# [ x^2 | 0 <= x <= 10, 단 x는 홀수 ]  
# 
# * 집합의 짝대기(|) 기호는 `for`로 대체한다.   
# [ x^2 for 0 <= x <= 10, 단 x는 홀수 ]  
# 
# * 짝대기 기호 왼편에 위치한 x^2를 파이썬 수식으로 변경한다. 즉, x ** 2로 변경한다.   
# [ x ** 2 for 0 <= x <= 10, 단 x는 홀수 ]  
# 
# * 짝대기 기호 오른편에 위치하고, 변수 x가 어느 범위에서 움직이는지를 설명하는 부등식인 0 <= x <= 10 부분을 파이썬 수식으로 변경한다. 주로, 기존에 정의된 리스트를 사용하거나 `range()` 함수를 사용하여 범위를 x in ... 형식으로 지정한다.   
# [ x ** 2 for x in range(11), 단 x는 홀수 ]  

# :::{admonition} `range()` 함수  
# :class: info  
# `range()` 함수는 규칙성을 가진 정수들의 모음<font size = "2">collection</font>을 반환한다. 반환된 값은 range객체이며, 리스트와 유사하게 작동한다.  
# 
# `range()` 함수는 인자를 최대 세 개까지 받을 수 있다. 각 인자들의 역할은 슬라이싱에 사용되는 세 개의 인자들의 역할과 동일하다. 
# * `range([start, ] stop [, step])`
# * `start`의 경우 주어지지 않으면 `0`을 기본값으로 갖는다.
# * `step`의 경우 주어지지 않으면 `1`을 기본값으로 갖는다.
# 
# 예를 들어, 0부터 10까지의 정수들로 이루어진 `range`객체는 다음과 같이 생성한다.  
# 리스트로 형변환하면 `range(11)` 안에 포함된 항목을 확인할 수 있다. 
# ```python
# >>> print(range(11))
# range(0, 11)
# >>> print(list(range(11)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ```
# range형은 불변 시퀀스이다. 
# :::
# 

# * 마지막으로 변수 `x`에 대한 제한조건인 `단 x는 홀수` 부분을 파이썬의 `if` 문장으로 변경한다. 예를 들어, `x는 홀수`는 파이썬의 `x % 2 == 1`로 나타낼 수 있다.  
# `[x**2 for x in range(11) if x % 2 == 1]`

# In[155]:


a_list = [x**2 for x in range(11) if x % 2 == 1]
a_list


# :::{admonition} 참고   
# :class: info  
# 
# 위의 조건제시법은 다음 장에서 소개하는 `for` 반복문을 활용한 코드와 동일하다.
# 
# ```python
# >>> a_list = []
# >>> for x in range(0, 10) :
#         if x % 2 == 1 :
#             a_list.append(x ** 2)
# >>> print(a_list)
# [1, 9, 25, 49, 81]
# ```
# :::
# 

# :::{admonition} 참고  
# :class: info  
# 아래와 같이 리스트를 초기화할 때, 리스트 조건제시법을 사용하면 좋다. 
# ```python
# >>> a = [[0] * 5 for x in range(5)]
# >>> print(a)
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]
# ```
# 
# 리스트 `a`는 리스트`b`와 동일하지 않다. 
# ```python
# >>> b = [[0] * 5] * 5
# >>> print(b)
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]
# ```
# 
# 아래 그림처럼 리스트 `a`의 각 항목은 서로 다른 리스트를 참조한다. 반면 리스트 `b`의 각 항목은 하나의 리스트를 참조한다. 
# <div align="center">
#     <img src="https://raw.githubusercontent.com/hj617kim/core_pybook/master/images/ch04/list_comp01.png" style="width:400px;">
# </div>
# 
# 이러한 성질로 아래와 같은 일이 발생한다. 예를 들어, `a[2][3] = 1` 코드를 사용하여 리스트 `a`의 3행 4열의 값을 1로 변경하고자 하면, 해당 값이 1로 변경된 것을 볼 수 있다. 반면 `b[2][3] = 1` 코드를 사용한 다음, `b`를 확인해보면 4열의 값이 모두 1로 변경된 것을 볼 수 있다. 즉, 리스트 `b`는 원하는 대로 동작하지 않는다. 
# 
# ```python
# >>> a = [[0] * 5 for x in range(5)]
# >>> a[2][3] = 1
# [[0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]
# >>> b[2][3] = 1
# >>> print(b)
# [[0, 0, 0, 1, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 1, 0]]
# ```
# :::
# 

# ### 집합 조건제시법 

# 조건제시법을 이용하여 집합을 생성하는 과정은 리스트 조건제시법과 비슷하다. 

# In[156]:


words = 'Python is a general purpose language'.split()
print(words)
words_len = [len(x) for x in words] # 리스트 조건제시법
print(words_len)
unique_len = {len(x) for x in words} # 집합 조건제시법
print(unique_len)


# ### 사전 조건제시법  

# 조건제시법을 이용하여 사전을 생성하는 과정도 유사하다. 

# In[157]:


words = 'Python is a general purpose language'.split()
print(words)
len_dict = {k : len(k) for k in words}
print(len_dict)


# ## 연습문제

# 참고: [(실습) 모음 자료형](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-collections.ipynb)
