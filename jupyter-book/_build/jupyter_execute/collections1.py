#!/usr/bin/env python
# coding: utf-8

# (ch:collections)=
# # 모음 자료형 1부: 문자열, 리스트, 튜플

# 모음 자료형<font size = "2">collection data types</font>은
# 여러 개의 값을 항목으로 포함하는 값들의 자료형이다.
# 많은 값을 담고 있다는 의미에서
# **컨테이너**<font size="2">container</font>라고도 불린다.
# 파이썬은 아래 다섯 가지 모음 자료형을 기본으로 제공한다.
# 
# ```
# 문자열, 리스트, 튜플, 집합, 사전
# ```

# :::{admonition} 스칼라 자료형
# :class: info
# 
# 정수, 부동소수점, 불리언 등은 하나의 값으로만 구성되었다는 의미에서
# **스칼라**<font size='2'>scalar</font> 자료형이라 부른다.
# :::

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

# 먼저 순차 자료형을 다룬다.

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

# ### 문자열 연산

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

# **`count()` 메서드**

# In[29]:


words = " My life is so cool, my life is so cool "


# In[30]:


words.count('so')


# **`find()` 메서드**

# In[31]:


words.find('life')


# **`index()` 메서드**

# In[32]:


words.index('My')


# **`lower()` 메서드**

# In[33]:


words.lower()


# **`upper()` 메서드**

# In[34]:


words.upper()


# **`replace()` 메서드**

# In[35]:


words.replace('so ', 'that')


# **`lstrip()` 메서드**

# In[36]:


words.lstrip()


# **`rstrip()` 메서드**

# In[37]:


words.rstrip()


# **`strip()` 메서드**

# In[38]:


words.strip()


# **`split()` 메서드**

# In[39]:


words.split()


# **`join()` 메서드**

# In[40]:


'--'.join('Hello')


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


# ### 리스트 연산

# **`in` 연산자**
# 
# 리스트의 항목으로 등장하는지 여부를 알려주는 논리 연산자이다.

# In[47]:


3 in [1, 2, 3, 4, 5]


# In[48]:


'a' in [1, 2, 3, 4, 5]


# In[49]:


'a' not in [1, 2, 3, 4, 5]


# **이어붙이기/복제**
# 
# 문자열의 경우처럼 리스트도 이어붙이기와 복제 연산을 사용한다.

# In[50]:


['a', 'b'] + ['b', 'c', 'd']


# In[51]:


['a', 'b'] * 2


# In[52]:


2 * ['a', 'b']


# **`min()`/`max()` 함수**
# 
# 항목 중에서 최솟값 또는 최댓값을 확인한다.
# 단, 기본적으로 모든 값의 자료형이 갖고 크기 비교가 가능해야 한다. 

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
# |`list.pop()`|지정된 인덱스의 항목 삭제 후 삭제된 값 반환. 인덱스를 지정하지 않으면 마지막 항목 삭제 후 삭제된 값 반환|
# |`list.remove()`|지정된 항목이 처음으로 사용된 위치에서 삭제. 반환값은 `None`|
# |`list.sort()`|리스트의 항목을 크기 순으로 정렬. 반환값은 `None`|
# |`list.reverse()`|리스트의 항목들 순서 뒤집기. 반환값은 `None`|
# |`list.index()`|지정된 항목이 처음 위치한 인덱스 반환|
# |`list.count()`|지정된 항목이 등장한 횟수 반환|
# 
# 

# In[67]:


food = ['banana', 'apple', 'coconut', 'apple']


# **`append()` 메서드**

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

# **`extend()` 메서드**

# In[72]:


food.extend(['eggplant', 'fig'])
food


# :::{admonition} 참고   
# :class: info   
# 
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

# **`insert()` 메서드**

# In[73]:


food.insert(1, 'blueberry')
food


# **`pop()` 메서드**

# In[74]:


food.pop(0)


# In[75]:


food


# In[76]:


food.pop()


# In[77]:


food


# **`remove()` 메서드**

# In[78]:


food.remove('apple')
food


# **`sort()` 메서드**

# In[79]:


food.sort()
food


# `reverse=True` 옵션 인자를 사용하면 역순으로 정렬한다.

# In[80]:


food.sort(reverse=True)
food


# **`reverse()` 메서드**

# In[81]:


food = ['banana', 'apple1', 'coconut', 'apple2']


# In[82]:


food.reverse()
food


# `sort()`와 `reverse()` 메서드를 연속으로 적용하면 역순으로 정렬하게 된다.

# In[83]:


food = ['banana', 'apple1', 'coconut', 'apple2']
food.sort()
food.reverse()
food


# `sort()` 메서드를 `reverse=True` 옵션 인자와 함께 사용하는 것과 동일한 결과를 생성한다.

# In[84]:


food = ['banana', 'apple1', 'coconut', 'apple2']
food.sort(reverse=True)
food


# **`index()` 메서드**

# In[85]:


food.index('coconut')


# **`count()` 메서드**

# In[86]:


food.count('apple2')


# (sec:tuple)=
# ## 튜플

# 튜플은 리스트와 거의 비슷하지만, 변경 불가능<font size = "2">immutable</font>하다는 점이 다르다.
# 따라서 튜플을 활용하는 메서드가 많이 제공되지 않는다.
# 소괄호 `()`를 사용하고, 각 항목은 콤마(`,`)로 구분한다. 

# In[87]:


(1, 2, 3, 4, 5)


# In[88]:


('a','b', 'c', 'd')


# 소괄호를 사용하지 않아도 튜플로 처리된다.

# In[89]:


a_tuple = 'a','b', 'c', 'd'
a_tuple


# 길이가 1인 튜플인 경우 항목 뒤에 반드시 쉽표를 붙혀야 한다.

# In[90]:


tup1 = (3, )
type(tup1)


# 그렇지 않으면 튜플로 간주되지 않는다.

# In[91]:


tup1 = (3)
type(tup1)


# 튜플 또한 여러 종류의 값을 포함할 수 있다.

# In[92]:


mixed_tuple = (1, 2.3, 'abc', False, ['ab', 'c'], (2, 4))
mixed_tuple


# **빈 튜플**
# 
# 빈 튜플은 아무것도 포함하지 않는 튜플을 의미한다. 빈 튜플를 만드는 방법은 아래와 같다. 
# 
# ```python
# empty_tuple = ()
# empty_tuple = tuple()
# ```

# ### 튜플 연산

# **`in` 연산자**
# 
# 튜플의 항목으로 등장하는지 여부를 알려주는 논리 연산자이다.

# In[93]:


'1' in ('a', 'bc', 'd', 'e')


# In[94]:


'd' in ('a', 'bc', 'd', 'e')


# In[95]:


'f' not in ('a', 'bc', 'd', 'e')


# **이어붙이기/복제**
# 
# 리스트의 경우처럼 튜플도 이어붙이기와 복제 연산을 사용한다.

# In[96]:


('a', 'b') + ('b', 'c', 'd')


# In[97]:


('a', 'b') * 2


# **`len()`함수**
# 
# 튜플의 길이, 즉 튜플에 포함된 항목의 개수를 반환한다.

# In[98]:


len(('a', 'b', 'c', 'd'))


# **`min()`/`max()` 함수**
# 
# 항목 중에서 최솟값 또는 최댓값을 확인한다.
# 단, 기본적으로 모든 값의 자료형이 갖고 크기 비교가 가능해야 한다. 

# In[99]:


max((2, 9, 11, 20, 3))


# In[100]:


min((2, 9, 11, 20, 3))


# ### 튜플 인덱싱/슬라이싱

# 튜플도 문자열과 리스트처럼 인덱싱과 슬라이싱이 가능하다. 

# In[101]:


a_tuple = (3, 15, 9, 12, 7, 14, 10)


# In[102]:


a_tuple[0]


# In[103]:


a_tuple[-1]


# In[104]:


a_tuple[2:6:2]


# 튜플은 불변 자료형이라 값을 수정할 수 없다. 
# 예를 들어, 아래와 같이 인덱싱을 사용하여 튜플의 항목을 변경하려고 하면 오류가 발생한다.   
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

# 튜플이 변경 불가능한 자료형이라고 해서 튜플의 모든 항목이 모두 변경 불가능해야 하는 것은 아니다. 
# 예를 들어, 아래 `tup` 이 가리키는 튜플의 첫번째 항목은 `[1, 2]`이고, 리스트는 변경가능한 자료형이다.

# In[105]:


tup = ([1, 2], 10, 100)


# 변수 `tup` 과 튜플 사이의 관계는 아래 그림에서 보여준다.

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/ch04/tuple01.png" style="width:275px;">
# </div>

# 따라서 아래와 같이 첫번째 항목 자체는 변경이 가능하다. 

# In[106]:


tup[0].append(3)


# 실제로 `tup` 의 첫째 항목이 변경되었음을 확인할 수 있다.

# In[107]:


tup


# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/hj617kim/ch04/tuple02.png" style="width:300px;">
# </div>

# ### 튜플 메서드

# 튜플 자료형의 메서드는 많지 않다. 많이 사용되는 두 개의 메소드를 살펴보자.   
# 
# |메서드|설명|
# |:----------|:----------|
# |`tuple.count()`|지정된 항목이 등장한 횟수 반환|
# |`tuple.index()`|지정된 항목이 처음 위치한 인덱스 반환|

# In[108]:


num_tuple = (1, 2, 3, 1, 3, 5, 5, 10, 15)


# **`count()` 메서드**

# In[109]:


num_tuple.count(1)


# **`index()` 메서드**

# In[110]:


num_tuple.index(5)


# ## 시퀀스 짝짓기와 해체

# 시퀀스를 짝짓는 것과 항목별로 해체하는 것을 살펴본다.

# ### `zip()` 함수

# 문자열, 리스트, 튜플 등 순차 자료형 여러 개를 묶어 하나의 값으로 만든다.
# 이때, 각 순차 자료형의 값에 사용된 순서를 반영한다.
# 단, `zip()` 함수의 반환값은 구체적으로 명시되지 않는다. 

# In[111]:


zip("abc", [1, 2, 3])


# `for` 반복문을 이용하여 항목을 확인할 수는 있다.

# In[112]:


for item in zip("abc", [1, 2, 3]):
    print(item)


# 아니면 `list()`함수를 이용하여 튜플 리스트로 변환할 수도 있다.

# In[113]:


list(zip("abc", [1, 2, 3]))


# 여러 개의 모음 자료형을 짝짓는 것도 가능하다.
# 단. 길이가 다르면 가장 짧은 길이에 맞춰서 짝을 짓고, 나머지는 버린다.

# In[114]:


list(zip("abcdefgh",(1, 2, 3, 4, 5), [5, 10, 15]))


# ### 시퀀스 해체

# 순자 자료형의 항목 각각에 대해 변수 할당을 진행할 수 있다.
# 단, 사용되는 변수의 수는 항목의 수와 일치해야 한다.
# 예를 들어, 세 개의 항목을 갖는 시퀀스를 해체하려면 세 개의 변수가 필요하다. 

# In[115]:


a, b = "12"


# In[116]:


print(a, type(a)) # 타입은 문자열이다.
print(b)


# In[117]:


c, d, e = [3, 4, 5]


# In[118]:


print(c) 
print(d) 
print(e) 


# In[119]:


f, g = (6, 7)


# In[120]:


print(f) 
print(g) 


# **밑줄 기호 `_` 활용**
# 
# 변수의 이름이 굳이 필요 없다면 밑줄<font size = "2">underscore</font>(`_`) 기호를
# 대신 사용할 수 있다.
# 예를 들어, 둘째 값에 대한 변수가 필요없다면 아래와 같이 해체할 수 있다. 

# In[121]:


c, _, e = [3, 4, 5]
print(c + e)


# :::{admonition} 주의   
# :class: caution  
# 항목의 개수와 변수의 개수가 일치하지 않으면 오류가 발생한다.
# 오류를 피하려면 위해 밑줄 등을 반드시 활용해야 한다.
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

# **별표 기호 `*` 활용**
# 
# 앞에 몇 개의 값에만 변수 할당에 사용하고 나머지는 하나의 리스트로 묶어서 퉁쳐버릴 수도 있다.
# 이를 위해 별표 기호<font size = "2">asterisk</font>(`*`)를 하나의 변수명과 함께 사용한다. 

# In[122]:


values = (1, 2, 3, 4, 5)
a, b, *rest = values


# In[123]:


print(a)
print(b)
print(rest)


# 나머지 항목들을 무시하고 싶다면, 별표와 밑줄을 함께 사용한다. 

# In[124]:


a, b, *_ = values


# In[125]:


print(a)
print(b)


# ### unzip

# unzip(언짚) 은 `zip()` 함수의 역함수의 기능에 해당한다.
# 즉, 튜플의 리스트에서 여러 개의 리스트를 생성하는 기능이다.
# 
# 그런데 이 기능은 함수의 인자를 해체하는 `*` 연산자와 `zip()` 함수 자체를 이용하여 
# 구현할 수 있다.

# In[126]:


pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

numbers, letters = zip(*pairs)


# In[127]:


numbers


# In[128]:


letters


# `zip(*pairs)` 이 호출되었을 때 다음 과정이 실행된다.
# 
# ```
# zip(*[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
#     => zip((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))
#     => [(1, 2, 3, 4), ('a', 'b', 'c', 'd')]
# ```

# ### 동시 반복

# `zip()` 을 이용하면 여러 개의 리스트, 튜플을 대상으로 동시에 반복문을 돌릴 수 있다.

# In[129]:


letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'문자: {l}')
    print(f'숫자: {n}')


# In[130]:


letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'문자:   {l}')
    print(f'숫자:   {n}')
    print(f'연산자: {o}')


# ## 연습문제

# 참고: [(실습) 모음 자료형 1부: 문자열, 리스트, 튜플](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-collections1.ipynb)
