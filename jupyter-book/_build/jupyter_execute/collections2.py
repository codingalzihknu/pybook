#!/usr/bin/env python
# coding: utf-8

# (ch:collections2)=
# # 모음 자료형 2부: 집합, 사전, `range`, 조건제시법

# **주요 내용**

# - 집합과 사전
# - 해시 가능성
# - 형 변환 함수
# - `range` 객체
# - 리스트/사전 조건제시법
# - 모음 자료형과 `for` 반복문

# **슬라이드**
# 
# 본문 내용을 요약한 [슬라이드](https://github.com/codingalzi/pybook/raw/master/slides/slides-collections2.pdf)를 
# 다운로드할 수 있다.

# ## 집합

# 집합 자료형은 수학에서 다루는 집합처럼 작동하도록 만든 비순차 모음 자료형이며
# 다음과 같이 중괄호를 사용하여 정의된다.
# 집합은 항목의 중복을 허용하지 않고, 항목들 사이의 순서는 무시된다. 
# 따라서 인덱싱이나 슬라이싱을 지원하지 않는다.
# 
# `{항목1, 항목2, 항목3, ..., 항목n}`

# In[1]:


a_set = {4, 4, 9.2, "apple", True, 4}
a_set


# **공집합**
# 
# 공집합<font size = "2">empty set</font>은 아무것도 포함하지 않는 집합을 의미한다. 
# 공집합를 만드는 방법은 아래와 같다. 

# In[2]:


empty_set = set()
empty_set


# :::{admonition} 주의  
# :class: caution  
# 
# 빈 집합을 만들 때는 `set()`을 사용해야 한다. `{}`은 이어서 소개할 
# 빈 사전<font size="2">empty dictionary</font>을 가리킨다.
# 
# ```python
# >>> a = {}
# >>> type(a)
# dict
# ```
# :::

# ### 해시 가능성

# 집합의 항목으로 리스트 등 가변 자료형은 사용할 수 없다.
# 
# ```python
# >>> {[1, 3], 4}
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_1817/2739416386.py in <module>
# ----> 1 {[1, 3], 4}
# 
# TypeError: unhashable type: 'list'
# ```
# 
# 이유는 가변 자료형이 해시 가능하지 않기 때문이다.

# 파이썬 객체의 해시 가능성은 `hash()` 함수의 인자로 사용될 수 있는가에 의해 결정된다.
# 즉 `hash()` 함수와 함께 호출됐을 때 오류가 발생하지 않아야 한다.
# 이렇게 `hash()` 함수의 인자로 사용될 수 있는 값을
# **해시 가능**<font size="2">hashable</font>하다고 부른다.
# 
# 해시 가능한 인자에 대해 `hash()` 함수의 반환값은 특정 정수이며
# 서로 다른 인자에 대해 서로 다른 정수를 반환한다.
# 즉, 조금이라도 다른 해시 가능한 객체가 인자로 지정되면 다른 값을 계산한다.

# In[3]:


hash('123')


# In[4]:


hash('123 ')


# In[5]:


hash((1, 3, 4))


# In[6]:


hash((1, 2, 4))


# 반면에 리스트 등 가변 자료형의 객체는 해시 가능하지 않다.

# ```python
# >>> hash([1, 3])
# TypeError                                 Traceback (most recent call last)
# ~\AppData\Local\Temp\ipykernel_20092\1655639645.py in <module>
# ----> 1 hash([1, 3])
# 
# TypeError: unhashable type: 'list'
# ```

# 리스트를 포함한 튜플도 해시 가능하지 않다.

# ```python
# >>> hash(([1, 2], 3))
# TypeError                                 Traceback (most recent call last)
# ~\AppData\Local\Temp\ipykernel_20092\587436505.py in <module>
# ----> 1 hash(([1, 2], 3))
# 
# TypeError: unhashable type: 'list'
# ```

# 집합에 해시 가능한 값만 포함될 수 있는 이유는 두 항목을 구별하기 위해 `hash()` 함수를 이용하기 때문이다.
# 반면에 리스트 등과 같은 가변 자료형의 값은 언제든 변할 수 있기에 정체를
# 제대로 파악할 수 없다.

# ### 집합 연산

# **`in` 연산자**
# 
# 집합의 항목(원소)으로 등장하는지 여부를 알려주는 논리 연산자다.

# In[7]:


1 in {1, 2, 3, 9, 4}


# In[8]:


'a' not in {1, 'b', True, 9}


# **`len()` 함수**
# 
# 집합에 포함된 항목의 개수를 반환한다.

# In[9]:


len({1, 3, 5, 7, 9})


# **`min()`/`max()` 함수**
# 
# 항목 중에서 최솟값/최댓값을 확인한다.
# 단, 기본적으로 모든 값의 자료형이 갖고 크기 비교가 가능해야 한다. 

# In[10]:


max({1, 3, 5, 7, 9})


# In[11]:


min({1, 3, 5, 7, 9})


# (sec:set-methods)=
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

# **`union()` 메서드: 합집합**

# In[12]:


{1, 2}.union({3, 4})


# **`intersection()` 메서드: 교집합**

# In[13]:


{1, 2, 3}.intersection({3, 4})


# **`difference()` 메서드: 집합 뺄셈**

# In[14]:


{1, 2, 3}.difference({3, 4})


# **`issubset()` 메서드: 부분집합 관계**

# In[15]:


{1, 2, 3}.issubset({3, 4})


# In[16]:


{1, 2, 3}.issubset({1, 2, 3, 4})


# **`add()` 메서드: 항목 추가**

# In[17]:


a_set = {1, 2, 3, 4}
a_set.add(8)
a_set


# **`remove()` 메서드: 지정된 항목 제거**

# In[18]:


a_set.remove(1)
a_set


# **`pop()` 메서드: 임의 항목 제거**

# In[19]:


a_set.pop()


# In[20]:


a_set


# **`clear()` 메서드: 모든 항목 제거**

# In[21]:


a_set.clear()
a_set


# **`update()` 메서드: 여러 항목 추가**

# In[22]:


a_set.update({5, 10, 15})
a_set


# ## 사전 

# 사전 자료형은 **키**<font size = "2">key</font>와 **값**<font size = "2">value</font>의
# 쌍으로 구성된 항목들의 집합이며, **딕셔너리**<font size = "2">dictionary</font> 라고도 불린다.
# 예를 들어, `'Hello'` 와 `'World'` 를 키로, `'안녕'`, `'세계'` 를 각 키에 대한 값으로
# 갖는 사전은 다음과 같다.
# 
# ```python
# {'Hello':'안녕', 'World':'세계'}
# ```

# :::{admonition} 사전의 키와 해시 가능성
# :class: info
# 
# 사전의 키는 앞서 집합과 관련해서 설명한 것과 동일한 이유로 
# 정수, 부동소수점, 문자열, 튜플 등 해시 가능한 객체만 가능하다.
# :::

# **빈 사전**

# 빈 사전은 아무것도 포함하지 않는 사전을 의미한다. 빈 사전를 만드는 방법은 아래와 같다. 

# In[23]:


empty_dict = {}
empty_dict


# 다음 방식도 가능하다.

# In[24]:


empty_dict = dict()
empty_dict


# ### 사전 연산

# **`in` 연산자**
# 
# 사전의 키로 사용되었는 여부를 알려주는 논리 연산자다.

# In[25]:


'city' in {"name": "강현", "age": "3"} 


# `in`의 부정은 `not in`을 사용한다. 즉
# 키로 사용되지 않았는지 여부를 뭍는다.

# In[26]:


'city' not in {"name": "강현", "age": "3"} 


# **`len()` 함수**
# 
# 사전에 포함된 항목의 개수를 반환한다.

# In[27]:


len({"name": "강현", "age": "3"}) 


# **`min()`/`max()` 함수**
# 
# 키로 사용된 값들 중에서 최솟값/최댓값을 확인한다.
# 단, 키들의 기본적으로 자료형이 같고 크기 비교가 가능해야 한다.

# In[28]:


max({1 : 'one', 2 : 'two', 3 : 'three'})


# In[29]:


min({1 : 'one', 2 : 'two', 3 : 'three'})


# ### 사전 인덱싱 

# 사전에 사용된 키를 이용한 인덱싱이 지원된다. 
# 예를 들어, 아래 딕셔너리 `dic`에서 `'Hello'`에 대응하는 값을 확인하고자 하면  
# 다음과 같이 대괄호를 사용하는 인덱싱을 이용한다. 

# In[30]:


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

# ### 항목의 추가와 업데이트

# 아래와 같은 형식으로 사전에 항목을 추가하거나 업데이트 한다.
# 
# ```python
# 사전[key] = value
# ```   
# 
# 예를 들어, `dic`에 `Python : 파이썬` 항목을 다음과 같이 추가할 수 있다.

# In[31]:


dic['Python'] = '파이썬'

dic


# 이미 사용된 키를 이용하면 키와 연결된 값이 업데이트 된다.

# In[32]:


dic['World'] = '세상'
dic


# ### 항목 삭제

# 사전의 항목은 `del` 명령어를 사용하여 키를 지정하여 삭제한다.

# In[33]:


del dic['World']
dic


# ### 사전 메서드 

# 사전 자료형이 제공하는 주요 메서드는 아래와 같다.

# |메서드|설명|
# |:----------|:----------|
# |`dict.keys()`|사전에 사용된 key들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 반환|
# |`dict.values()`|사전에 사용된 value들을 모두 모아서 리스트와 비슷한 자료형을 만들어서 반환
# |`dict.items()`|사전에 사용된 item들을 모두 모아서 리스트와 비슷한 자료형으로 만들어서 반환|
# |`dict.get()`|key에 대응되는 value를 반환. 존재하지 않는 key를 사용하면 `None`을 반환
# |`dict.update()`|다른 사전과 합함. 반환값은 `None`|
# |`dict.pop()`|key에 해당하는 항목을 삭제. 반환값은 key에 대응하는 value. key가 존재하지 않으면 오류 발생.|
# |`dict.clear()`|사전 안의 모든 항목들을 삭제. 반환값은 `None`|

# In[34]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# **`keys()` 메서드: 키로 이루어진 모음 자료형 반환**

# In[35]:


dic.keys()


# **`values()` 메서드: 값으로 이루어진 모음 자료형 반환**

# In[36]:


dic.values()


# **`items()` 메서드: (키, 값) 모양의 쌍으로 이루어진 모음 자료형 반환**

# In[37]:


dic.items()


# **`get()` 메서드: 지정된 키와 연관된 값 반환**

# In[38]:


dic.get('Hello')


# 존재하지 않는 키를 사용하면 기본값으로 `None`이 사용된다.

# In[39]:


dic.get('hello')


# 키가 사용되지 않았을 때 기본값을 바꾸려면 둘째 인자를 지정한다.

# In[40]:


dic.get('hello', "해당 키가 없어요.")


# **`update()` 메서드: 여러 항목 추가**

# In[41]:


dic.update({'Python' : '파이썬', 'Programming' : '프로그래밍'})


# In[42]:


dic


# **`pop()` 메서드: 지정된 키 항목 삭제. 반환값은 키와 연관된 값**

# In[43]:


dic.pop('Python')


# In[44]:


dic


# **`clear()` 메서드: 전체 항목 삭제**

# In[45]:


dic.clear()


# In[46]:


dic


# ## 형변환 함수

# **`list()` 함수**
# 
# 임의의 모음 자료형을 리스트로 변환한다.

# In[47]:


list('abc')


# In[48]:


list((1, 2, 3))


# In[49]:


list({1, 2, 5})


# 사전은 여러 방식으로 변환된다.

# In[50]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# * 키 리스트

# In[51]:


list(dic)


# In[52]:


list(dic.keys())


# * 값 리스트

# In[53]:


list(dic.values())


# * (키, 값) 리스트

# In[54]:


list(dic.items())


# **`tuple()` 함수**
# 
# 임의의 모음 자료형을 튜플로 변환한다.

# In[55]:


tuple('abc')


# In[56]:


tuple([1, 2, 3])


# In[57]:


tuple({1, 2, 5})


# 사전에 대해서는 `list()` 함수와 동일한 방식으로 작동한다.

# In[58]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# In[59]:


tuple(dic)


# In[60]:


tuple(dic.keys())


# In[61]:


tuple(dic.values())


# In[62]:


tuple(dic.items())


# **`set()` 함수**
# 
# 임의의 모음 자료형을 집합으로 변환한다.
# 이 과정에서 순서와 중복이 무시된다.

# In[63]:


set('abc')


# In[64]:


set([1, 1, 2, 5])


# In[65]:


set((1, 3, 3, 9, 1))


# In[66]:


dic = {'Hello' : '안녕', 'World' : '세계'}


# In[67]:


set(dic)


# In[68]:


set(dic.keys())


# In[69]:


set(dic.values())


# In[70]:


set(dic.items())


# **`dict()` 함수**
# 
# 키-값의 튜플 형식의 항목을 갖는 모음 자료형을 사전으로 변환한다. 
# 단, 키로 사용되는 값은 해시 가능해야 한다.

# In[71]:


data = [('Hello', '안녕'), ('World', '세계'), ('Programming', '프로그래밍')]
dict(data)


# `zip()` 함수를 활용하면 편리하다.

# In[72]:


data = zip('abcde', [1, 2, 3, 4, 5])
dict(data)


# ## `range` 객체

# `range` 객체는 리스트, 튜플 등과 매우 유사하며, `range()` 함수를 이용하여 생성한다.
# 예를 들어, `range(3)`는 0부터 2까지의 정수를 포함하는 리스트로 간주될 수 있다.
# 하지만, `range()` 함수의 반환값은 `range` 이며 항목을 바로 확인할 수는 없다.

# In[73]:


range(3)


# `range` 자료형의 항목을 확인하려면 `for` 반복문을 사용하던가
# 리스트 또는 튜플로 형변환을 해야 한다.

# In[74]:


for item in range(3):
    print(item)


# In[75]:


list(range(3))


# In[76]:


tuple(range(3))


# `range()` 함수는 최대 세 개의 인자를 받으며 각 인자의 기능은 리스트의 슬라이싱 기능과 동일하다.

# In[77]:


list(range(1, 9, 2))


# In[78]:


list(range(9, 0, -2))


# 하나의 인자만 사용하면 구간의 끝을 의미하며, 구간의 시작은 0이 된다.
# 셋째 인자는 생략되면 1이 기본값으로 사용된다.

# In[79]:


range(3) == range(0, 3)


# In[80]:


range(3) == range(0, 3, 1)


# (sec-comprehension)=
# ## 조건제시법

# 조건제시법<font size = "2">comprehension</font>을 이용하여 
# 리스트, 집합, 사전을 정의할 수 있다.

# **리스트 조건제시법**

# 수학에서 0과 10사이에 있는 홀수들의 제곱을 원소로 갖는 집합을 조건제시법으로 표현하면
# 다음과 같다.
# 
# $$\{ x^2 \mid 0 \le x \le 10, \text{ 단 $x$는 홀수} \}$$

# 0과 10 사이에 있는 홀수들의 제곱을 항목으로 갖는 리스트를 `for` 반복문으로 구현해 보자.

# In[81]:


zero2ten_odd = []

for x in range(11):
    if x%2 == 1:
        zero2ten_odd.append(x**2)

zero2ten_odd


# 조건제시법을 이용하여 보다 간단하게 리스트를 생성할 수 있다.

# In[82]:


zero2ten_odd = [x**2 for x in range(11) if x%2 == 1]
zero2ten_odd


# 위 두 코드를 비교하면 조건제시법의 작동원리를 이해할 수 있을 것이다. 

# **집합 조건제시법**

# 위 결과를 집합으로 구현하면 다음과 같다.

# In[83]:


zero2ten_odd_set = {x**2 for x in range(11) if x%2 == 1}
zero2ten_odd_set


# **사전 조건제시법**

# 조건제시법을 이용하여 사전을 생성하는 과정도 유사하다. 
# 아래 코드는 문장에 포함된 단어를 키로, 단어의 길이를 값으로 갖는 항목들로 구성된 사전을 생성한다.

# In[84]:


words = '파이썬은 범용 프로그래밍 언어입니다.'.split()
words


# `words` 에 포함된 단어와 단어의 길이로 짝을 이룬 항목으로 구성된 사전은 다음과 같다.

# In[85]:


len_dict = {k : len(k) for k in words}
len_dict


# 아래 코드는 0부터 10 사이의 홀수를 키로, 홀수의 제곱은 값으로 갖는 항목으로 구성된 사전을 생성한다.

# In[86]:


odd_squares = {x : x**2 for x in range(11) if x%2 == 1}
odd_squares


# ## 모음 자료형과 `for` 반복문

# 앞서 소개된 모든 모음 자료형은 `for` 반복문과 함께 사용될 수 있다.

# * 문자열과 반복문

# In[87]:


aString = "Python is lovely!"

for chr in aString:
    print(chr, end=' ')


# * 리스트와 반복문

# In[88]:


aList = list(aString)
print(aList)


# In[89]:


for item in aList:
    print(item, end=' ')


# * 튜플과 반복문

# In[90]:


aTuple = tuple(aString)
print(aTuple)


# In[91]:


for item in aTuple:
    print(item, end=' ')


# * 집합과 반복문

# In[92]:


aSet = set(aString)
print(aSet)


# 집합은 중복을 허용하지 않음에 주의하라.

# In[93]:


for item in aSet:
    print(item, end=' ')


# * 사전과 반복문

# In[94]:


words = 'Python is a general purpose language'.split()
len_dict = {k : len(k) for k in words}
len_dict


# 사전에 대한 반복문은 키<font size='2'>key</font>에 대해 실행된다.

# In[95]:


for item in len_dict:
    print(item, end=' ')


# 키와 값의 쌍에 대해 반복문을 실행하려면 `items()` 메서드를 이용한다. 
# 단, 키와 값 각각에 대해 변수를 지정하는 게 좋다.

# In[96]:


for key, value in len_dict.items():
    print(f"{key:>8} 키의 값: {value}")


# 항목을 쪼개서 사용할 수도 있다.

# In[97]:


for item in len_dict.items():
    key = item[0]
    value = item[1]
    print(f"{key:>8} 키의 값: {value}")


# 값에 대해 반복문을 실행하려면 `values()` 메서드를 이용한다. 

# In[98]:


for item in len_dict.values():
    print(item, end=' ')


# * `zip` 과 반복문

# In[99]:


aZip = zip("abcdefgh",(1, 2, 3, 4, 5), [5, 10, 15])

for item in aZip:
    print(item)


# 항목별로 변수를 지정하여 활용할 수도 있다.

# In[100]:


aZip = zip("abcdefgh",(1, 2, 3, 4, 5), [5, 10, 15])

for chr, tup, lst in aZip:
    print(f"({chr}, {tup}, {lst})")


# * `range` 와 반복문

# In[101]:


for item in range(1, 10, 2):
    print(f"{item}의 제곱: {item**2}")


# ## 연습문제

# 참고: [(실습) 모음 자료형 2부: 집합, 사전, `range`, 조건제시법](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-collections2.ipynb)
