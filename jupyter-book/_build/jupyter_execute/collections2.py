#!/usr/bin/env python
# coding: utf-8

# (ch:collections2)=
# # 모음 자료형 2부: 집합, 사전, `range`, 조건제시법

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


# 집합의 원소는 모두 **해시 가능**<font size="2">hashable</font>이어야 한다. 
# 예를 들어 가변 자료형인 리스트는 해시 가능이지 않으며 따라서 집합의 원소가 될 수 없다. 
# 
# ```python
# >>> {[1, 3], 4}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/2739416386.py in <module>
# ----> 1 {[1, 3], 4}
# 
# TypeError: unhashable type: 'list'
# ```

# :::{admonition} 해시 가능성
# :class: info   
# 
# `hash()` 함수에 의해 특정 정수로 변환될 수 있는 값을 **해시 가능**이다라고 말한다.]
# 해시 함수는 모든 객체에 대해 유일한 값을 계산한다.
# 따라서 두 객체의 동일성을 확인하는 데에 사용된다.
# 반면에 리스트와 같은 가변 자료형은 항목이 변할 수 있기에 해시 가능이 아니다. 
# 더 이상의 해시 함수에 대한 자세한 설명은 생략한다.
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
# 빈 집합을 만들 때는 `set()`을 사용해야 한다. `{}`은 이어서 소개할 
# 빈 사전<font size="2">empty dictionary</font>이다. 
# 
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


# **합집합, 교집합, 차집합, 부분집합**
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

# 정수, 부동소수점, 문자열, 튜플 등 해시 가능인 자료형만 사전의 키로 사용될 수 있다.  
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
# 
# 임의의 모음 자료형을 리스트로 변환한다.

# In[42]:


list('abc')


# In[43]:


list((1, 2, 3))


# In[44]:


list({1, 2, 5})


# 사전은 여러 방식으로 변환된다.

# In[45]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# * 키 리스트

# In[46]:


list(dic)


# In[47]:


list(dic.keys())


# * 값 리스트

# In[48]:


list(dic.values())


# * (키, 값) 리스트

# In[49]:


list(dic.items())


# **`tuple()` 함수**
# 
# 임의의 모음 자료형을 튜플로 변환한다.

# In[50]:


tuple('abc')


# In[51]:


tuple([1, 2, 3])


# In[52]:


tuple({1, 2, 5})


# 사전에 대해서는 `list()` 함수와 동일한 방식으로 작동한다.

# In[53]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# In[54]:


tuple(dic)


# In[55]:


tuple(dic.keys())


# In[56]:


tuple(dic.values())


# In[57]:


tuple(dic.items())


# **`set()` 함수**
# 
# 임의의 모음 자료형을 집합으로 변환한다.
# 이 과정에서 순서와 중복이 무시된다.

# In[58]:


set('abc')


# In[59]:


set([1, 1, 2, 5])


# In[60]:


set((1, 3, 3, 9, 1))


# In[61]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# In[62]:


set(dic)


# In[63]:


set(dic.keys())


# In[64]:


set(dic.values())


# In[65]:


set(dic.items())


# **`dict()` 함수**
# 
# 키-값의 튜플 형식의 항목을 갖는 모음 자료형을 사전으로 변환한다. 
# 단, 키로 사용되는 값은 해시 가능이어야 한다.

# In[66]:


data = [('Hello', '안녕'), ('World', '세계'), ('Programming', '프로그래밍')]
dict(data)


# In[67]:


data = zip('abcde', [1, 2, 3, 4, 5])
dict(data)


# In[68]:


dict(Hello = '안녕', World = '세계', Programming = '프로그래밍')


# ## `range` 자료형

# `range` 자료형은 리스트, 튜플 등과 매우 유사하며, `range()` 함수를 이용하여 생성한다.
# 예를 들어, `range(3)`는 0부터 2까지의 정수를 포함하는 리스트 또는 튜플로 간주될 수 있다.
# 하지만, `range()` 함수의 반환값은 `range` 이며 항목을 바로 확인할 수 없다.

# In[69]:


print(range(3))


# `range` 자료형의 항목을 확인하려면 `for` 반복문을 사용하던가
# 리스트 또는 튜플로 형변환을 해야 한다.

# In[70]:


for item in range(3):
    print(item)


# In[71]:


list(range(3))


# In[72]:


tuple(range(3))


# `range()` 함수는 최대 세 개의 인자를 받으며 각 인자의 기능은 리스트 또는 튜플의 슬라이싱에서의
# 기능과 동일하다.

# In[73]:


list(range(1, 9, 2))


# In[74]:


tuple(range(0, 9, 3))


# In[75]:


list(range(9, 0, -2))


# 하나의 인자만 하용하면 구간의 끝을 의미하며, 구간의 시작은 0이 된다.
# 셋째 인자는 생략되면 1이 기본값으로 사용된다.

# In[76]:


range(3) == range(0, 3)


# In[77]:


range(3) == range(0, 3, 1)


# ## 조건제시법

# 조건제시법<font size = "2">comprehension</font>을 이용하여 
# 리스트, 집합, 사전을 정의할 수 있다.

# **리스트 조건제시법**

# 수학에서 0과 10사이에 있는 홀수들의 제곱을 원소로 갖는 집합을 조건제시법으로 표현하면
# 다음과 같다.
# 
# $$\{ x^2 \mid 0 \le x \le 10, \text{ 단 $x$는 홀수} \}$$

# 0과 10 사이에 있는 홀수들의 제곱을 항목으로 갖는 리스트를 `for` 반복문으로 구현해 보자.

# In[78]:


zero2ten_odd = []

for x in range(11):
    if x%2 == 1:
        zero2ten_odd.append(x**2)

zero2ten_odd


# 조건제시법을 이용하여 보다 간단하게 리스트를 생성할 수 있다.

# In[79]:


zero2ten_odd = [ x**2 for x in range(11) if x%2 == 1 ]
zero2ten_odd


# 위 두 코드를 비교하면 조건제시법의 작동원리를 이해할 수 있을 것이다. 

# **집합 조건제시법**

# 조건제시법을 이용한 집합 정의도 유사하다.

# In[80]:


words = 'Python is a general purpose language'.split()
words


# In[81]:


unique_len = {len(x) for x in words}
unique_len


# **사전 조건제시법**

# 조건제시법을 이용하여 사전을 생성하는 과정도 유사하다. 

# In[82]:


words = 'Python is a general purpose language'.split()
words


# In[83]:


len_dict = {k : len(k) for k in words}
len_dict


# ## 연습문제

# 참고: [(실습) 모음 자료형 2부: 집합, 사전, `range`, 조건제시법](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-collections2.ipynb)
