#!/usr/bin/env python
# coding: utf-8

# (ch:collections3)=
# # 사례 연구: 이터러블, 이터레이터, 제너레이터

# 파이썬은 **덕 타이핑**<font size='2'>duck typing</font>을 지원한다.
# 덕 타이핑은 원래 '오리처럼 걷고 꽥꽥 울면 오리가 맞다" 라는 속담에서 유래한다.
# 하지만 파이썬에서는 주어진 클래스가 특정 이름의 메소드를 지원하는지 여부에만 관심을 둘 때 사용하는 관용적 표현이다.
# 
# 예를 들어, `__iter__()` 라는 메소드를 지원하는 클래스는 이터러블 자료형이라 불리며
# `for` 반복문을 작성할 때 사용될 수 있는 모음 자료형 역할을 수행한다.

# ## 이터러블

# **이터러블**<font size = "2">iterable</font> 자료형의 값은
# 필요한 경우 포함된 항목을 한 번에 하나씩 전달할 수 있는 기능을 제공하는 갖는 객체이다.
# 예를 들어 `for` 반복문과 함께 사용될 수 있는
# 모든 시퀀스 자료형(예, 리스트, 튜플, 문자열 등)과 사전 자료형이 이터러블 객체이다.

# In[1]:


for i in [1, 2, 3] :
    print(i)


# In[2]:


for k in {'a' : '에이', 'b' : '비'} :
    print(k)


# 이터러블 객체의 엄밀한 정의는 `__iter__()` 메서드를 갖는 클래스의 객체이다. 
# `dir()` 함수를 사용하여 `__iter__()` 메서드의 포함여부를 확인할 수 있다.

# In[3]:


a_list = [1, 2, 3]

'__iter__' in dir(a_list)


# :::{admonition} `dir()` 함수
# :class: info
# 
# `dir()` 함수는 인자로 사용된 객체의 속성과 메서드의 리스트를 반환한다.
# 
# ```python
# >>> dir(a_list)
# ['__add__',
#  ...
#  '__iter__',
#  ...
#  'append',
#  'clear',
#  'copy',
#  'count',
#  'extend',
#  'index',
#  'insert',
#  'pop',
#  'remove',
#  'reverse',
#  'sort']
# ```
# :::

# `a_list` 변수가 가리키는 값이 순차 자료형인 리스트이면서 동시에 이터러블 자료형의 객체인지 
# 여부를 판단하기 위해 `isinstance()` 함수를 활용할 수도 있다.
# 하지만 먼저 이터러블 자료형의 클래스인 `Iterable`과 순차 자료형의 클래스인 `Sequence` 을
# 불러와야 한다. 

# In[4]:


from collections.abc import Sequence, Iterable


# 아래 표현식은 리스트가 순차 자료형임을 확인해준다.

# In[5]:


isinstance(a_list, Sequence)


# 아래 표현식은 리스트가 이터러블 자료형임을 확인해준다.

# In[6]:


isinstance(a_list, Iterable)


# 반면에 사전은 이터러블이지만 순차 자료형은 아님을 확인할 수 있다.

# In[7]:


a_dict = {'a': 1, 'b': 2}


# In[8]:


isinstance(a_dict, Iterable)


# In[9]:


isinstance(a_dict, Sequence)


# (sec:iterators)=
# ## 이터레이터

# **이터레이터**<font size = "2">iterator</font>는 값을 하나씩 꺼낼 수 있는 객체로, 
# `__next__()` 메서드를 갖는다.
# 예를 들어, 모든 이터러블 객체를 `__iter__()` 메서드를 이용하여 이터레이터로 변환시킬 수 있다.

# <div align="center"><img src="https://nvie.com/img/iterable-vs-iterator.png" style="width:600px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# 리스트는 이터러블 객체이기에 `__iter__()` 메서드를 호출할 수 있다.
# 그러면 이터레이터 객체가 하나 생성된다.

# In[10]:


a_list = [1, 2, 3]
a_iter = a_list.__iter__()

type(a_iter)


# 다음 방식으로도 이터레이터임을 확인할 수 있다.

# In[11]:


from collections.abc import Iterator


# In[12]:


isinstance(a_iter, Iterator)


# 이터레시터는 `__next__()` 메서드를 갖는다.

# In[13]:


'__next__' in dir(a_iter)


# 반면에 리스트 자체는 이터레이터가 아니다.

# In[14]:


'__next__' in dir(a_list)


# In[15]:


isinstance(a_list, Iterator)


# 이터레이터는 값을 바로 보여주지 않는다. 이터레이터의 항목은 리스트로 형변환하면 쉽게 확인할 수 있다. 

# In[16]:


print(a_iter)


# 이터레이터의 항목을 확인하거나 이용하려면 
# `__next__()` 메서드를 호출해야 한다.
# 그런데 `__next__()` 메서드가 호출될 때마다 포함된 항목이 차례대로 반환된다.

# In[17]:


a_iter.__next__() 


# In[18]:


a_iter.__next__()


# In[19]:


a_iter.__next__()


# 모든 항목이 반환되면 더 이상 `__next__()` 메서드를 사용할 수 없다.
# 이유는 더 이상 반환해줄 항목이 없기에 실행하면 `StopIteration` 오류를 발생시키기 때문이다.
# 
# ```python
# >>> a_iter.__next__()
# StopIteration                             Traceback (most recent call last)
# /tmp/ipykernel_79/31460938.py in <module>
# ----> 1 a_iter.__next__()
# 
# StopIteration: 
# ```

# 항목을 다시 확인하려면 이터레이터를 다시 생성해야 하고,
# 그러면 다시 첫 항목부터 확인된다.

# In[20]:


a_iter = a_list.__iter__()

a_iter.__next__()


# **`for` 반복문과 이터러블 자료형**
# 
# 리스트 자체는 이터레이터 자료형이 아니지만 `for` 반복문과 여러 번 사용할 수 있다.

# In[21]:


for i in [1, 2, 3]:
    print(i)


# In[22]:


for i in [1, 2, 3]:
    print(i)


# 이유는 `for` 반복문이 실행될 때마다 이터러블의 `__iter__()`메서드가
# 먼저 호출되어 매번 새로 이터레이터 객체를 생성한다.
# 그런 다음에 `__next__()` 메서드가 실행되는 방식으로 `for` 반복문이 작동한다. 

# **`range` 객체는 이터러블**
# 
# `range()` 함수로 생성되는 `range` 객체도 리스트처럼 이터러블 자료형이지만 이터레이터는 아니다.

# In[23]:


a_range = range(5)


# In[24]:


isinstance(a_range, Iterable)


# In[25]:


isinstance(a_range, Iterator)


# 항목을 미리 만들어 놓지 않기에 미리 보여주지 않는다.

# In[26]:


print(a_range)


# 하지만 `range` 객체 또한 당연히 `for` 반복문과 함께 유용하게 사용된다.

# In[27]:


for item in a_range:
    print(f"{item}의 제곱은 {item**2}.")


# ## 제너레이터 

# **제너레이터**<font size = "2">generator</font>는 간단한 방식으로 구현할 수 있는 이터레이터이며,
# 크게 두 가지 방식으로 생성된다.
# 
# - 제너레이터 함수 활용
# - 제너레이터 표현식 활용
# 
# 이터러블, 이터레이터, 제너레이터 사이의 관계는 다음과 같다.

# <div align="center"><img src="https://nvie.com/img/relationships.png" style="width:700px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# **제너레이터 함수**
# 
# 제너레이터 함수는 일반 함수와 비슷한 방식으로 정의되는데, `return`키워드 대신 `yield` 키워드를 사용하여
# `__next__()` 메서드가 반환해야 하는 값을 어떻게 생성할지 지정한다.   
# 
# 예를 들어, 1부터 n의 제곱을 생성하는 제너레이터는 아래와 같이 정의한다. 

# In[28]:


def squares(n) :
    for i in range(1, n + 1) :
        yield i ** 2


# `squares()` 는 제너레이터만을 생성한다. 
# 예를 들어 `squares(5)` 가 제너레이터임을 다음과 같이 확인할 수 있다.

# In[29]:


from collections.abc import Generator

isinstance(squares(5), Generator)


# 앞서 보았듯이 제너레이터는 항목을 미리 모두 만들지 않고 필요할 때마나 하나씩 만들어 반환한다. 

# In[30]:


squares_5 = squares(5)
print(squares_5)


# In[31]:


squares_5.__next__()


# In[32]:


squares_5.__next__()


# `next()` 함수를 사용하면 인자로 사용된 객체의 `__next__()` 메서드가 호출된다.

# In[33]:


next(squares_5) # squares_5.__next__()


# :::{admonition} 주의   
# :class: caution  
# 
# `for` 반복문을 사용하더라도 
# 이미 `__next__()` 메서드가 반환된 값의 다음 항목부터 사용됨에 주의하라.
# 
# ```python
# >>> for x in squares_5:
# >>>     print(x, end = ' ')
# 16 25 
# ```
# :::

# **제너레이터 표현식**
# 
# 조건제시법 방식을 튜플에 적용하면 제너레이터 표현식이 된다.
# 예를 들어, 아래 코드는 튜플이 아닌 
# 앞서 정의한 `squares_5`와 동일하게 작동하는 제너레이터를 생성한다. 

# In[34]:


squares_5_new = (i ** 2 for i in range(1, 6))

isinstance(squares_5_new, Generator)


# In[35]:


for item in squares_5_new:
    print(item, end=' ')


# 제너레이터는 이터레이터이기에 두 번 연속 사용할 수 없다.

# In[36]:


for item in squares_5_new:
    print(item, end=' ')


# 다시 사용하려면 매번 다시 생성해야 한다.

# In[37]:


squares_5_new = (i ** 2 for i in range(1, 6))

for item in squares_5_new:
    print(item, end=' ')


# ## 이터러블 자료형에 유용한 함수

# **`enumerate()` 함수**
# 
# `enumerate(iterable, start = 0)` 함수는
# 카운트와 `iterable`의 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환한다. 

# In[38]:


seasons = ['봄', '여름', '가을', '겨울']


# In[39]:


list(enumerate(seasons))


# 카운트는 기본적으로 0부터 시작하고 다른 값부터 시작하고 싶다면 `start` 값을 변경해주면 된다. 

# In[40]:


class_name = ['강현', '나현', '다현']
class_name_enum = enumerate(class_name, 1)

for num, name in class_name_enum :
    print(f'{num}번 학생은 {name}입니다.')


# **`zip()` 함수**
# 
# 여러 개의 이터러블 값을 인자로 받아 각 항목을 튜플로 묶은 형태로 짝짓기된 항목을
# 생성하는 이터레이터를 만들어 반환한다. 

# In[41]:


data_zip = zip(['3월', '2월', '9월'], ['강현', '나현', '다현'])

for month, name in data_zip :
    print(f'{name}은 {month}달에 태어났다.')


# 두 이터러블의 길이가 다르면 짧은 길이에 맞춰서 작동한다.

# In[42]:


data_zip = zip(['3월', '2월', '9월'], ['강현', '나현', '다현', '상우']) # '상우'는 무시됨.

for month, name in data_zip :
    print(f'{name}은 {month}달에 태어났다.')


# 세 개 이상의 이터러블을 짝짓기 할 수도 있다.

# In[43]:


data_zip = zip(['3월', '2월', '9월'], ['강현', '나현', '다현', '상우'], ['7일', '23일'])

for month, name, date in data_zip :
    print(f'{name}은 {month} {date}에 태어났다.')


# **`all()` 함수**
# 
# 이터러블의 모든 항목이 참이면 `True`, 아니면 `False`를 반환한다. 

# In[44]:


all([1 != 1+0, True, True, True])


# In[45]:


all([True, 1<=2, 3==2+1, True])


# 0은 거짓, 나머지 수는 참으로 간주된다.

# In[46]:


all([1 < 2, 3, 0, 2, True])


# **`any()` 함수**
# 
# 이터러블의 항목 중 어느 하나라도 참이면 `True`, 아니면 `False`를 반환한다. 

# In[47]:


any((False, 1, False, False))


# In[48]:


any((False, 1 == 3, False, False))


# **`filter()` 함수**
# 
# `filter(function, iterable)` 함수는 `function`이 참을 반환하는 `iterable`의 항목들로 
# 이터레이터를 만들어 반환한다.

# In[49]:


def is_even(n) :
    if not n % 2 :
        return True
    else :
        return False

num = [2, 8, 9, 3, 10, 12]


# In[50]:


num_iter = filter(is_even, num)

for item in num_iter:
    print(item, end = ' ')


# 아래처럼 간단하게 확인할 수도 있다.

# In[51]:


list(filter(is_even, num))


# **`map()` 함수**
# 
# `map(function, iterable)` 함수는 `iterable`의 모든 항목에 
# `function`을 적용한 후 그 결과를 돌려주는 이터레이터를 반환한다.  

# In[52]:


def is_even(n) :
    if not n % 2 :
        return True
    else :
        return False

num = [2, 8, 9, 3, 10, 12]


# In[53]:


num_map = map(is_even, num)

for item in num_map :
    print(item, end = ' ')


# 리스트의 각 항목을 제곱하려면 다음과 같이 한다.

# In[54]:


def square(x):
    return x**2


# In[55]:


list(map(square, num))


# ## 적극적 계산과 소극적 계산

# `range` 객체처럼 모든 값을 미리 생성해서 준비해 놓는 대신에 필요할 때 필요한 항목을 생성하는 것을 
# **소극적**<font size='2'>lazy</font> 계산이라 부른다. 
# 반면에 호출 되자마자 바로 실행하는 것은 **적극적**<font size='2'>eager</font> 계산이다.
# 파이썬은 기본적으로 적극적 계산을 사용하지만 제너레이터 경우와 같이 부분적으로
# 소극적 계산을 지원한다.

# **무한 수열 생성**
# 
# 제너레이터를 이용하면 무한 수열을 다룰 수 있다. 
# 이유는 소극적 계산을 따르는 제너레이터는 항상 요구되는 만큼만 생성하기에
# 절대로 무한히 많은 값들을 한꺼번에 다루지 않기 때문이다.
# 
# 예를 들어, 아래 `natural_numbers` 함수는 모든 자연수를 생성할 준비가 된 제너레이터이다.

# In[56]:


def natural_numbers():
    """모든 자연수 생성 가능"""
    n = 1
    while True:
        yield n
        n += 1


# 물론 위와 같이 무한 수열을 생성할 수 있는 제너레이터는 매우 조심해서 사용해야 한다.
# 예를 들어 아래와 같이 사용하면 무한 반복(loop)이 발생한다.
# 
# ```python
# for i in natural_numbers():
#     print(i)
# ```

# 무한히 많은 값을 생성할 수 있는 제너레이터는 `break` 명령문 등을 적절히
# 섞어서 사용해야 한다.
# 예를 들어, 1부터 시작하는 자연수 5개를 항목으로 갖는 리스트는 다음과 생성한다. 

# In[57]:


list_5 = []

for i in natural_numbers():
    if i > 5:
        break
    list_5.append(i)
    
print(list_5)


# **무한 피보나찌 수열 생성**
# 
# 아래 코드는 피보나찌 수열을 무한정 생성하는 제너레이터를 정의한다.

# In[58]:


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


# 피보나찌 수열의 처음 10개 항목은 다음과 같다.

# In[59]:


count = 0

for item in fib():
    if count >= 10:
        break
        
    print(item, end=' ')
    count += 1


# 피보나찌 수열의 처음 n개의 항목을 출력하는 함수는 다음과 같다.

# In[60]:


def fibo(n):
    count = 0

    for item in fib():
        if count >= n:
            break

        print(item, end=' ')
        count += 1


# In[61]:


fibo(3)


# In[62]:


fibo(10)


# ## 연습문제

# 참고: [(실습) 사례 연구: 이터러블, 이터레이터, 제너레이터](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-casestudy_collections.ipynb)
