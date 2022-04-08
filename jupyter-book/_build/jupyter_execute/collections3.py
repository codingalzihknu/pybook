#!/usr/bin/env python
# coding: utf-8

# (ch:collections)=
# # 모음 자료형 3부: range, 조건제시법, 이터레이터, 제너레이터

# ## `range` 자료형

# `range` 자료형은 리스트, 튜플 등과 매우 유사하며, `range()` 함수를 이용하여 생성한다.
# 예를 들어, `range(3)`는 0부터 2까지의 정수를 포함하는 리스트 또는 튜플로 간주될 수 있다.
# 하지만, `range()` 함수의 반환값은 `range` 이며 항목을 바로 확인할 수 없다.

# In[1]:


print(range(3))


# `range` 자료형의 항목을 확인하려면 `for` 반복문을 사용하던가
# 리스트 또는 튜플로 형변환을 해야 한다.

# In[2]:


for item in range(3):
    print(item)


# In[3]:


list(range(3))


# In[4]:


tuple(range(3))


# `range()` 함수는 최대 세 개의 인자를 받으며 각 인자의 기능은 리스트 또는 튜플의 슬라이싱에서의
# 기능과 동일하다.

# In[5]:


list(range(1, 9, 2))


# In[6]:


tuple(range(0, 9, 3))


# In[7]:


list(range(9, 0, -2))


# 하나의 인자만 하용하면 구간의 끝을 의미하며, 구간의 시작은 0이 된다.
# 셋째 인자는 생략되면 1이 기본값으로 사용된다.

# In[8]:


range(3) == range(0, 3)


# In[9]:


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

# In[10]:


zero2ten_odd = []

for x in range(11):
    if x%2 == 1:
        zero2ten_odd.append(x**2)

zero2ten_odd


# 조건제시법을 이용하여 보다 간단하게 리스트를 생성할 수 있다.

# In[11]:


zero2ten_odd = [ x**2 for x in range(11) if x%2 == 1 ]
zero2ten_odd


# 위 두 코드를 비교하면 조건제시법의 작동원리를 이해할 수 있을 것이다. 

# **집합 조건제시법**

# 조건제시법을 이용한 집합 정의도 유사하다.

# In[12]:


words = 'Python is a general purpose language'.split()
words


# In[13]:


unique_len = {len(x) for x in words}
unique_len


# **사전 조건제시법**

# 조건제시법을 이용하여 사전을 생성하는 과정도 유사하다. 

# In[14]:


words = 'Python is a general purpose language'.split()
words


# In[15]:


len_dict = {k : len(k) for k in words}
len_dict


# ## 이터러블과 이터레이터

# ### 이터러블

# 이터러블<font size = "2">iterable</font> 또는 이터러블 객체는 값을 한 번에 하나씩 돌려줄 수 있는 반복 가능한 객체로, `for` 반복문과 함께 사용될 수 있다.   
# 예를 들어, 모든 시퀀스 자료형(예, 리스트, 튜플, 문자열 등)은 이터러블하고, 시퀀스 자료형은 아니지만 사전 자료형도 이터러블하다.  

# In[16]:


for i in [1, 2, 3] :
    print(i)


# In[17]:


for k in {'a' : '에이', 'b' : '비'} :
    print(k)


# 이터러블 객체는 `__iter__()` 메서드를 가지고 있다.

# In[18]:


a_list = [1, 2, 3]
print(dir(a_list)) #dir() 함수를 사용하여 a_list가 어떤 메서드를 가지고 있는지 확인할 수 있다. 


# ### 이터레이터

# 이터레이터<font size = "2">iterator</font>는 값을 하나씩 꺼낼 수 있는 객체로, 이터러블의 `__iter__()` 메서드나 내장함수 `iter()`를 사용하여 이터레이터를 만들 수 있다. 

# In[19]:


a_list = [1, 2, 3]
a_iter = iter(a_list)
type(a_iter)


# 이터레이터의 `__next__()` 메서드나 내장함수 `next()`를 반복적으로 호출하면 값을 차례대로 돌려준다.    

# In[20]:


a_iter.__next__() 


# In[21]:


a_iter.__next__()


# In[22]:


a_iter.__next__()


# :::{admonition} 주의  
# :class: caution  
# 차례대로 이터레이터의 항목을 모두 꺼낸 다음에 `__next__()` 메서드를 실행하면 `StopIteration` 오류가 발생한다. 
# 
# ```python
# >>> a_iter.__next__()
# StopIteration                             Traceback (most recent call last)
# /tmp/ipykernel_79/31460938.py in <module>
# ----> 1 a_iter.__next__()
# 
# StopIteration: 
# ```
# :::
# 

# 이터레이터는 값을 바로 보여주지 않는다. 이터레이터의 항목은 리스트로 형변환하면 쉽게 확인할 수 있다. 

# In[23]:


a_list = [1, 2, 3]
a_iter = iter(a_list)
print(a_iter)
print(list(a_iter))


# :::{admonition} 참고  
# :class: info  
# `for`반복문을 사용할때마다 이터러블의 `__iter__()`메서드는 새로운 이터레이터 객체를 자동으로 만들어주기 때문에 사용자가 직접 이터레이터를 만들 필요는 없다.  
# 예를 들어, 아래와 같이 리스트를 이용하여 `for` 반복문을 실행하면 리스트의 `__iter__()` 메서드가 호출된다. 
# ```python
# >>> a_list = [1, 2, 3]
# >>> for item in a_list :
#         print(item)
# 1
# 2
# 3
# ```
# :::
# 

# ### 제너레이터 

# 제너레이터<font size = "2">generator</font>는 특별한 이터레이터로, `__iter__()`와 `__next__()` 메서드를 구체적으로 구현할 필요없이 간단하게 이터레이터를 정의할 수 있다. 제너레이터는 함수와 비슷한 방식으로 정의하지만 함수 안에 `return`키워드 대신 `yield` 키워드를 사용하여 생성해야 하는 값들을 지정한다는 점이 다르다.     

# 예를 들어, 1부터 n의 제곱을 생성하는 제너레이터는 아래와 같이 정의한다. 

# In[24]:


def squares(n) :
    for i in range(1, n + 1) :
        yield i ** 2


# In[25]:


gen = squares(5)
type(gen)


# 제너레이터는 지정된 값들을 바로 생성하지 않으며, 생성할 준비만 해두고 필요할 때 값을 생성하여 메모리를 보다 효율적으로 사용할 수 있다.   
# `__next__()` 메서드나 `next()` 함수를 사용하여 항목을 차례대로 가져올 수 있다.  

# In[26]:


gen.__next__()


# In[27]:


gen.__next__()


# In[28]:


next(gen)


# `for` 반복문에 사용하면 그때 필요한 항목을 하나씩 생성한다.  
# 앞에서 `1, 4, 9` 항목을 가져왔기 때문에 `16`과 `25`만 출력된 것을 볼 수 있다. 

# In[29]:


for x in gen :
    print(x, end = ' ')


# :::{admonition} 주의   
# :class: caution  
# 제너레이터도 `__next__()` 메서드가 모든 항목을 순회하면 더 이상 가리키는 값이 없다. 따라서 한 번 더 `for` 반복문을 사용했을 때, 아무 것도 출력하지 않는다. 
# 
# ```python
# >>> for x in gen :
#         print(x, end = ' ')
# ```
# 
# 동일한 제너레이터를 다시 사용하려면 제너레이터를 다시 생성해야 한다. 
# ```python
# >>> gen = squares(5)
# >>> for x in gen :
#         print(x, end = ' ')
# 1 4 9 16 25 
# ```
# :::
# 

# **제너레이터 표현식**  
# 제너레이터는 제너레이터 표현식을 사용하여 만들 수도 있다. 조건제시법과 유사하지만 소괄호(`( )`)로 감싸서 만든다. 

# In[30]:


squares = (i ** 2 for i in range(1, 6))
type(squares)


# :::{admonition} 주의  
# :class: caution  
# 소괄호로 감싸서 만들지만 튜플 자료형이 아니라 제너레이터이다. 
# :::
# 

# In[31]:


print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


# In[32]:


x = (x**2 for x in range(3))


# In[33]:


y = [z for z in x]
y


# ### 이터러블에 유용한 내장함수

# #### `enumerate()` 함수  
# `enumerate(iterable, start = 0)` : 카운트와 `iterable`의 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환한다. 카운트는 기본적으로 0부터 시작하고 다른 값부터 시작하고 싶다면 `start` 값을 변경해주면 된다. 

# In[34]:


seasons = ['봄', '여름', '가을', '겨울']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start = 10)))


# In[35]:


class_name = ['강현', '나현', '다현']
class_name_enum = enumerate(class_name, 1)

for num, name in class_name_enum :
    print(f'{num}번 학생은 {name}입니다.')


# #### `zip()` 함수

# 여러 개의 이터러블을 인자로 받아 각 항목을 튜플로 묶은 형태로 이터레이터를 만들어 반환한다. 

# In[36]:


data_zip = zip(['3월', '2월', '9월'], ['강현', '나현', '다현'])

for month, name in data_zip :
    print(f'{name}은 {month}달에 태어났다.')


# #### `all()` 함수    
# 
# 이터러블의 모든 항목이 참이거나 비어있으면 `True`, 아니면 `False`를 반환한다. 

# In[37]:


print(all([1, 3, 0, 2, 15])) # 0 == False를 실행하면 True다. 0이 아닌 수는 True이다. 
print(all([1, 3, 2, 15]))


# #### `any()` 함수  
# 
# 이터러블의 항목 중 어느 하나라도 참이면 `True`, 아니면 `False`를 반환한다. 

# In[38]:


print(any((False, 1, False, False)))
print(any((False, 1 == 3, False, False)))


# #### `filter()` 함수  
# `filter(function, iterable)`은 `function`이 참을 반환하는 `iterable`의 요소들로 이터레이터를 만들어 반환한다.   

# In[39]:


def is_even(n) :
    if not n % 2 :
        return True
    else :
        return False

print(is_even(5))
print(is_even(10))


# In[40]:


num = [2, 8, 9, 3, 10, 12]
num_iter = filter(is_even, num)


# In[41]:


for item in num_iter :
    print(item, end = ' ')


# In[42]:


num_iter = filter(is_even, num)
list(num_iter)


# #### `map()` 함수  
# `map(function, iterable)` : `iterable`의 모든 항목에 `function`을 적용한 후 그 결과를 돌려주는 이터레이터를 반환한다.  

# In[43]:


def is_even(n) :
    if not n % 2 :
        return True
    else :
        return False


# In[44]:


num = [2, 8, 9, 3, 10, 12]
num_map = map(is_even, num)


# In[45]:


for item in num_map :
    print(item, end = ' ')


# ## 연습문제

# 참고: [(실습) 모음 자료형](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-collections.ipynb)
