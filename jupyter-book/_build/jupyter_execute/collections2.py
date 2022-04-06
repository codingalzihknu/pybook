#!/usr/bin/env python
# coding: utf-8

# (ch:collections2)=
# # 모음 자료형 2부

# 집합과 사전 두 개의 비순차 자료형을 살펴본다.

# ## 집합

# 집합 자료형은 수학에서 다루는 집합과 비슷한 자료형으로 형식은 아래와 같다.  
# 
# `{항목1, 항목2, 항목3, ..., 항목n}`
# 
# 집합은 항목의 중복을 허용하지 않고, 항목들 사이의 순서는 무시된다. 
# 따라서 인덱싱이나 슬라이싱을 지원하지 않는다.

# In[1]:


a_set = {4, 9.2, "apple", True, 4}
a_set


# :::{admonition} 참고  
# :class: info  
# 집합의 원소는 모두 불변 자료형이어야 한다. 예를 들어 리스트는 집합의 원소가 될 수 없다. 
# 
# ```python
# >>> {[1, 3], 4}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/2739416386.py in <module>
# ----> 1 {[1, 3], 4}
# 
# TypeError: unhashable type: 'list'
# ```
# :::

# **공집합**
# 
# 공집합<font size = "2">empty set</font>은 아무것도 포함하지 않는 집합을 의미한다. 
# 공공집합를 만드는 방법은 아래와 같다. 

# In[2]:


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

# ### 집합 연산

# **`in` 연산자**
# 
# 집합의 항목(원소)으로 등장하는지 여부를 알려주는 논리 연산자다.

# In[3]:


1 in {1, 2, 3, 9, 4}


# In[4]:


'a' not in {1, 'b', True, 9}


# **집합 연산(수학)**
# 
# 합집합, 교집합, 차집합 계산과 부분집합 여부 등을 확인하는 연산은 
# 수학에서 사용되는 개념과 동일하게 작동한다.
# 반면에 덧셈과 곱셈 연산자는 지원되지 않는다.

# |연산자|설명|예시|실행결과|
# |:----------:|:----------:|:----------:|:----------:|
# |`\|`|합집합|`{1, 2} \| {2, 4}`|`{1, 2, 4}`|
# |`&`|교집합|`{1, 2} & {2, 4}`|`{2}`|
# |`-`|차집합|`{1, 2} - {2, 4}`|`{1}`|
# |`<=`|부분집합 여부|`{1, 2} <= {2, 4}`|`False`|

# In[5]:


{1, 2, 3, 4, 5} | {2, 4, 6}


# In[6]:


{1, 2, 3, 4, 5} & {2, 4, 6}


# In[7]:


{1, 2, 3, 4, 5} - {2, 4, 6}


# In[8]:


{1, 2, 3, 4, 5} <= {2, 4, 6}


# In[9]:


{1, 2} <= {1, 2, 3, 4, 5}


# **`len()` 함수**
# 
# 집합에 포함된 항목의 개수를 반환한다.

# In[10]:


len({1, 3, 5, 7, 9})


# **`min()`/`max()` 함수**
# 
# 항목 중에서 최솟값/최댓값을 확인한다.
# 단, 기본적으로 모든 값의 자료형이 갖고 크기 비교가 가능해야 한다. 

# In[11]:


max({1, 3, 5, 7, 9})


# In[12]:


min({1, 3, 5, 7, 9})


# ### 집합 메서드  

# 집합 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|
# |:----------|:----------|
# |`set.union()`|합집합 반환|
# |`set.intersection()`|교집합 반환|
# |`set.difference()`|차집합 반환|
# |`set.issubset()`|부분 집합 여부를 판단하여 반환|
# |`set.add()`|항목추가. 반환값은 `None`|
# |`set.remove()`|특정 항목 삭제. 반환값은 `None`|
# |`set.pop()`|임의의 항목 삭제. 반환값은 삭제하는 항목. 공집합에 사용하면 오류 발생|
# |`set.clear()`|모든 항목을 삭제. 반환값은 `None`|
# |`set.update()`|여러 개의 항목 한번에 추가. 반환값은 `None`|

# **`union()` 메서드**

# In[13]:


{1, 2}.union({3, 4})


# **`intersection()` 메서드**

# In[14]:


{1, 2, 3}.intersection({3, 4})


# **`difference()` 메서드**

# In[15]:


{1, 2, 3}.difference({3, 4})


# **`issubset()` 메서드**

# In[16]:


{1, 2, 3}.issubset({3, 4})


# **`add()` 메서드**

# In[17]:


a_set = {1, 2, 3, 4}
a_set.add(8)
print(a_set)


# **`remove()` 메서드**

# In[18]:


a_set.remove(1)
print(a_set)


# **`pop()` 메서드**

# In[19]:


print(a_set.pop())
print(a_set)


# **`clear()` 메서드**

# In[20]:


a_set.clear()
print(a_set)


# **`update()` 메서드**

# In[21]:


a_set.update({5, 10, 15})
print(a_set)


# ## 사전 

# 사전 자료형은 **키**<font size = "2">key</font>와 **값**<font size = "2">value</font>의
# 쌍으로 이루어진 항목들의 집합이며, **딕셔너리**<font size = "2">dictionary</font> 라고도 불린다.
# 사전의 형식은 아래와 같다.   
# 예를 들어, `'Hello'` 와 `'World'` 를 키로, `'안녕'`, `'세계'` 를 각 키에 대한 값으로
# 갖는 사전은 다음과 같다.
# 
# ```python
# {'Hello' : '안녕', 'World' : '세계'}
# ```

# 정수, 부동소수점, 문자열, 튜플 등 불변 자료형만 사전의 키로 사용될 수 있다.  
# 단, 튜플의 경우 리스트 등 가변 자료형을 포함할 수 없다.
# 이는 키로 사용되는 값은 변하지 않아야 하기 때문이다.

# **빈 사전**

# 빈 사전은 아무것도 포함하지 않는 사전을 의미한다. 빈 사전를 만드는 방법은 아래와 같다. 

# In[22]:


empty_dict = {}
empty_dict = dict()
empty_dict


# ### 사전 연산

# **`in` 연산자**
# 
# 사전의 키로 사용되었는 여부를 알려주는 논리 연산자다.

# In[23]:


'city' in {"name": "강현", "age": "3"} 


# In[24]:


'city' not in {"name": "강현", "age": "3"} 


# **`len()` 함수**
# 
# 사전에 포함된 항목 개수를 반환한다.

# In[25]:


len({"name": "강현", "age": "3"}) 


# **`min()`/`max()` 함수**
# 
# 키로 사용된 값들 중에서 최솟값/최댓값을 확인한다.
# 단, 키들의 기본적으로 자료형이 같고 크기 비교가 가능해야 한다.

# In[26]:


max({1 : 'one', 2 : 'two', 3 : 'three'})


# In[27]:


min({1 : 'one', 2 : 'two', 3 : 'three'})


# ### 사전 인덱싱 

# 사전에 사용된 키를 이용한 인덱싱이 지원된다. 
# 예를 들어, 아래 딕셔너리 `dic`에서 `'Hello'`에 대응하는 값을 확인하고자 하면  
# 다음과 같이 대괄호를 사용하는 인덱싱을 이용한다. 

# In[28]:


dic = {'Hello' : '안녕', 'World' : '세계'}
dic['Hello']


# 존재하지 않는 키로 값을 추출하려고 하면, 오류가 발생한다. 
# 
# ```python
# >>> dic['Python']
# KeyError                                  Traceback (most recent call last)
# /tmp/ipykernel_1817/1517958361.py in <module>
# ----> 1 dic['Python']
# 
# KeyError: 'Python'
# ```

# ### 항목의 추가와 삭제 

# 아래와 같은 형식으로 사전에 항목을 추가한다.  
# 
# ```python
# 사전[key] = value
# ```   
# 
# 예를 들어, `dic`에 `Python : 파이썬` 항목을 다음과 같이 추가할 수 있다.

# In[29]:


dic['Python'] = '파이썬'

print(dic)


# 단, 이미 사용된 키를 이용하면 값이 업데이트 된다.

# In[30]:


dic['World'] = '세상'
print(dic)


# 사전의 항목은 `del` 명령어를 사용하여 삭제한다.

# In[31]:


del dic['World']
print(dic)


# ### 사전 메서드 

# 사전 자료형이 제공하는 주요 메서드는 아래와 같다.

# In[32]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# |메서드|설명|
# |:----------|:----------|
# |`dict.keys()`|사전에 사용된 key들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 반환|
# |`dict.values()`|사전에 사용된 value들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 반환
# |`dict.items()`|사전에 사용된 item들을 모두 모아서 리스트와 비슷한 자료형으로 만들어서 반환|
# |`dict.get()`|key에 대응되는 value를 반환. 존재하지 않는 key를 사용하면 `None`을 반환
# |`dict.update()`|다른 사전과 합함. 반환값은 `None`|
# |`dict.pop()`|key에 해당하는 항목을 삭제. 반환값은 key에 대응하는 value. key가 존재하지 않으면 오류 발생.|
# |`dict.clear()`|사전 안의 모든 항목들을 삭제. 반환값은 `None`|

# **`keys()` 메서드**

# In[33]:


dic.keys()


# **`values()` 메서드**

# In[34]:


dic.values()


# **`items()` 메서드**

# In[35]:


dic.items()


# **`get()` 메서드**

# In[36]:


dic.get('Hello')


# 존재하지 않는 키를 사용하면 기본값으로 `None`이 사용된다.

# In[37]:


dic.get('hello')


# 키가 사용되지 않았을 때 기본값을 바꾸려면 둘째 인자를 지정한다.

# In[38]:


dic.get('hello', "해당 키가 없어요.")


# **`update()` 메서드**

# In[39]:


print(dic.update({'Python' : '파이썬', 'Programming' : '프로그래밍'}))
print(dic)


# **`pop()` 메서드**

# In[40]:


print(dic.pop('Python'))
print(dic)


# **`clear()` 메서드**

# In[41]:


print(dic.clear())
print(dic)


# ## 형변환 함수

# **`list()` 함수**

# `list()` : 리스트형으로 변환.

# In[42]:


list('abc')  #문자열의 각 문자를 항목으로 갖는 리스트 반환


# In[43]:


list((1, 2, 3))


# In[44]:


list({1, 2, 5})


# In[45]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(list(dic))
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))


# **`tuple()` 함수**

# `tuple()` : 튜플형으로 변환.

# In[46]:


tuple('abc')


# In[47]:


tuple([1, 2, 3])


# In[48]:


tuple({1, 2, 5})


# In[49]:


dic = {'Hello' : '안녕', 'World' : '세계'}
print(tuple(dic))
print(tuple(dic.keys()))
print(tuple(dic.values()))
print(tuple(dic.items()))


# **`set()` 함수**

# `set()` : 집합형으로 변환.

# In[50]:


set('abc')


# In[51]:


set([1, 1, 2, 5])


# In[52]:


set((1, 3, 3, 9, 1))


# In[53]:


dic = {'Hello' : '안녕', 'World' : '세계', 'Hi' : '안녕'}
print(set(dic))
print(set(dic.keys()))
print(set(dic.values()))
print(set(dic.items()))


# **`dict()` 함수**

# `dict()` : 사전형으로 변환.  
# 
# 사전의 각 항목은 키와 값으로 이루어졌기 때문에 적절하게 짝지어진 데이터를 사용해야 사전을 만들 수 있다.

# In[54]:


data = [('Hello', '안녕'), ('World', '세계'), ('Programming', '프로그래밍')]
dict(data)


# In[55]:


data = zip('abcde', [1, 2, 3, 4, 5])
dict(data)


# In[56]:


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

# In[57]:


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

# In[58]:


words = 'Python is a general purpose language'.split()
print(words)
words_len = [len(x) for x in words] # 리스트 조건제시법
print(words_len)
unique_len = {len(x) for x in words} # 집합 조건제시법
print(unique_len)


# ### 사전 조건제시법  

# 조건제시법을 이용하여 사전을 생성하는 과정도 유사하다. 

# In[59]:


words = 'Python is a general purpose language'.split()
print(words)
len_dict = {k : len(k) for k in words}
print(len_dict)


# ## 연습문제

# 참고: [(실습) 모음 자료형](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-collections.ipynb)
