#!/usr/bin/env python
# coding: utf-8

# (ch:inheritance)=
# # 상속

# **참고:** 아래 내용은 [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds3/index.html)의 1.13 절을 
# 일부 내용을 활용합니다.

# __상속__(inheritance)은 객체 지향 프로그래밍의 또 다른 주요 요소이다. 
# 클래스를 선언할 때 다른 클래스의 상태(state)와 메서드를 상속 받아 활용할 수 있다.
# 상속을 받는 클래스를 __자식 클래스__ 또는 __하위 클래스__, 
# 상속을 해주는 클래스를 __부모 클래스__ 또는 __상위 클래스__라고 부른다. 

# <그림 8>이 파이썬 모음 자료형의 상속 체계를 보여준다. 
# 예를 들어, `list` 클래스는 `Sequence` 클래스를 상속하며,
# `Sequence`는 `Collection` 클래를 상속한다. 
# 이를 'is-a' 관계를 표현하면 "리스트는 시퀀스 모음 자료형이다" 등으로 말한다.
# 이와 달리 항목들의 순서를 고려하지 않는 `dict`와 `set` 은 
# `Sequence` 클래스와 'is-a' 관계를 갖지 않는다. 

# <figure>
# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/inheritance1.png" width="70%">
#     <figcaption>그림 8: 파이썬 모음 자료형의 상속 체계</figcaption>
# </figure>

# `list`, `tuple`, `str` 클래스 모두 `Sequence` 클래스를 상속하기에
# 자신들의 객체를 다루는 공통된 방식을 갖는다.
# 반면에 서로 구별되는 각 자료형 고유의 속성과 메서드를 갖는다. 
# 이렇듯 자식 클래스는 서로 공통된 요소와 각 자식 클래스 고유의 요소를 함께 갖는다.

# 클래스 상속을 활용할 때의 주요 장점은 다음과 같다. 
# - 기존에 작성된 코드를 필요에 따라 수정, 재활용 가능.
# - 데이터(객체) 사이의 관계를 보다 잘 이해할 수 있음.

# ## 컨테이너 클래스 선언

# 모음 자료형을 추상 자료형 클래스를 이용하여 정의하려면
# 경우에 따라 아래 사항을 추가적으로 고려해야 한다.
# 
# - `len()` 함수 지원
# - `for` 반복문 지원
# - 대괄호 (`[]`) 인덱싱 지원

# 모음 자료형 객체가 속하는 클래스를 일명 __컨테이너 클래스__라 하며,
# 앞으로 스택, 큐, 그래프, 트리 등을 다룰 때 중요한 역할을 수행한다.
# 여기서는 앞서 언급한 요소들이 필요한 경우에
# 사용되는 매직 메서드들을 알아본다.

# __예제: 1차원 넘파이 어레이 구현__
# 
# 아래 코드는 1차원 넘파이 어레이에 해당하는 자료형을 리스트를 이용하여 직접 구현한다. 
# 일반 리스트의 경우와는 달리 1차원 어레이에 대한 덧셈 연산이 항목별로 이루어진다.

# In[1]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 
               정수 또는 부동소수점들의 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# 덧셈 연산이 항목별로 이루어진다. 

# In[2]:


oneD1 + oneD2


# ### `len()` 함수 지원

# 그런데 포함된 항목의 개수를 쉽게 확인할 수 없다.

# ```python
# len(oneD1)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-29-7d7804051de9> in <module>
# ----> 1 len(oneD1)
# 
# TypeError: object of type 'OneDArray' has no len()
# ```

# `len()` 함수가 사용되려면 `__len()__` 메서드가 적절하게 선언되어야 한다.

# In[3]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)

    def __len__(self):
        return len(self.items)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# In[4]:


len(oneD1)


# **`mean()` 메서드 지원**

# `len()` 함수를 이용하여 넘파이 어레이 객체가 제공하는 다양한 메서드를 구현할 수 있다.
# 예를 들어 아래 코드는 항목들의 평균값을 계산하는 메서드를 제공한다.

# In[5]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 
               정수 또는 부동소수점들의 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)

    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# 이제 평균값을 계산할 수 있다.

# In[6]:


oneD1.mean()


# In[7]:


oneD2.mean()


# ### `for` 반복문 지원

# 포함된 항목들을 대상으로 반복문을 실행할 수 없다.

# ```python
# for x in oneD1:
#     print(x)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-35-ae2d40dfb17d> in <module>
# ----> 1 for x in oneD1:
#       2     print(x)
# 
# TypeError: 'OneDArray' object is not iterable
# ```

# 아래에서 처럼 `__iter__()`와 `__next__()` 메서드가 적절하게 선언되어야 한다.
# 
# - `__iter__()` 메서드: 반복적으로 항목을 생성할 수 있는 객체인 이터레이터(iterator) 생성
# - `__next__()` 메서드: 이터레이터에 포함되는 메서드이며 지정된 순서에 따라 항목을 반환함.
#     - 함수 본체에서 사용되는 `count`, `max_repeats` 인스턴스 변수는 생성자에서 선언됨.

# In[8]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        self.count = 0                  # 항목 카운트
        self.max_repeats = len(items)   # 항목 카운트 최댓값
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
            raise StopIteration("더 이상 항목이 없어요!")
            
        next_item = self.items[self.count]
        self.count += 1                       # 항목 반환할 때마다 카운트 키우기
        return next_item
    
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])        


# 이제 `for` 반복문이 지원된다.

# In[9]:


oneD3 = oneD1 + oneD2


# In[10]:


for x in oneD3:
    print(x)


# 그런데 `for` 반복문을 한 번만 사용할 수 있다.

# In[11]:


for x in oneD3:
    print(x)


# 이유는 `count=3` 이 되어 `__next_()` 메서드가 `StopIteration` 오류를 발생시키가 때문이다.

# In[12]:


oneD3.count


# ```python
# oneD3.__next__()
# 
# StopIteration                             Traceback (most recent call last)
# <ipython-input-41-61e9b06a5a78> in <module>
# ----> 1 oneD3.__next__()
# 
# <ipython-input-36-e3b35e606009> in __next__(self)
#      43     def __next__(self):
#      44         if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
# ---> 45             raise StopIteration("더 이상 항목이 없어요!")
#      46 
#      47         next_item = self.items[self.count]
# 
# StopIteration: 더 이상 항목이 없어요!
# ```

# `for` 문을 다시 사용하려면 객체를 새로 생성해야 한다.

# In[13]:


oneD3 = oneD1 + oneD2

for x in oneD3:
    print(x)


# ### 인덱싱 지원

# 순차 자료형이 되려면 항목들의 순서를 이용한 인덱싱이 가능해야 한다.
# 그런데 항목들의 순서를 고려해서 항목을 확인하고 수정하고자 하면 오류가 발생한다. 

# ```python
# oneD2[0]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-46-8369793c9173> in <module>
# ----> 1 oneD2[0]
# 
# TypeError: 'OneDArray' object is not subscriptable
# ```

# ```python
# oneD2[0] = 100
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-47-8bc71738b965> in <module>
# ----> 1 oneD2[0] = 100
# 
# TypeError: 'OneDArray' object does not support item assignment
# ```

# 아래 두 메서드를 구현해야 한다.
# 
# - `__getitem__()` 메서드: 대괄호 인덱싱 지원
# - `__setitem__()` 메서드: 특정 인덱스 항목 업데이트

# 이제 드디어 순차 자료형으로 선언할 수 있다.
# 
# - `Sequence` 클래스 상속
# 
# **참고:** https://docs.python.org/3/library/collections.abc.html

# In[14]:


from collections.abc import Sequence, Iterable


# In[15]:


class OneDArray(Sequence):
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
# 다음은 굳이 필요 없음: __getitem__() 과 __len__() 만 있으면 됨.
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
#             raise StopIteration("더 이상 항목이 없어요!")
            
#         next_item = self.items[self.count]
#         self.count += 1                       # 항목 반환할 때마다 카운트 키우기
#         return next_item

    def __getitem__(self, idx):
        return self.items[idx]
    
    def __setitem__(self, idx, item):
        self.items[idx] = item
        
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# `Sequence`와 `Iterable` 클래스를 상속함을 다음과 같이 확인할 수 있다.

# In[16]:


issubclass(OneDArray, Sequence)


# In[17]:


issubclass(OneDArray, Iterable)


# In[18]:


oneD2[0]


# In[19]:


oneD2[0] = 100


# In[20]:


oneD2


# __슬라이싱__(slicing)도 지원한다.

# In[21]:


oneD2[1:3]


# In[22]:


oneD2[0:3]


# In[23]:


oneD2[0:3:2]


# ### 이터러블 자료형과 `__getitem__()` 메서드

# `__getitem_()` 메서드를 지원하는 클래스는 자동으로 이터레이터가 된다. 
# 아래에서 확인할 수 있듯이 `__iter__()` 와 `__next__()` 메서드가 없어도
# `for` 반복문이 작동한다.

# In[24]:


class OneDArray:
    def __init__(self, items):
        """
        items: 1차원 어레이 항목으로 사용될 값들. 리스트, 튜플 등 모음 자료형 사용.
        저장: 리스트 활용
        """ 
        self.items = list(items)
        
    def __repr__(self):
        return f"myArray({self.items})"
    
    def __add__(self, other):
        """항목별 덧셈 연산"""

        # 어레이 길이가 동일하지 않으면 오류 발생시킴
        # raise와 RuntimeError 활용
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")

        # 항목별 덧셈 실행
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]

        return OneDArray(main_object)
    
    def __len__(self):
        return len(self.items)

    def mean(self):
        """항목들의 평균"""
        sum = 0
        for item in self.items:
            sum += item
            
        return sum/len(self)
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count >= self.max_repeats:    # 항목 개수만큼만 반복 허용
#             raise StopIteration("더 이상 항목이 없어요!")
            
#         next_item = self.items[self.count]
#         self.count += 1                       # 항목 반환할 때마다 카운트 키우기
#         return next_item

    def __getitem__(self, idx):
        return self.items[idx]
    
    def __setitem__(self, idx, item):
        self.items[idx] = item
        
oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])


# In[25]:


oneD3 = oneD1 + oneD2


# In[26]:


for x in oneD3:
    print(x)


# 이와 더불어 객체를 새로 생성할 필요없이 반복문을 계속해서 활용할 수도 있다.

# In[27]:


for x in oneD3:
    print(x)


# ## 이터레이터와 제너레이터

# __참고__: 아래 내용은 Vicent Driessen의 
# [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)
# 블로그 내용을 참조합니다.

# ### 이터러블 자료형과 이터레이터

# __이터러블__(iterable) 자료형은 `__iter__()` 메서드를 지원하는 자료형이다.
# `__iter__()` 메서드는 이터러블 객체의 항목들을 지정된 순서대로
# 반환할 수 있는 능력을 갖춘 `__next__()` 메서드를 지원하는 __이터레이터__(iterator)를 
# 필요할 때 내부적으로 생성해서 반복문에 활용한다(아래 그림 참조).

# <div align="center"><img src="https://nvie.com/img/iterable-vs-iterator.png" style="width:600px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# ### 제너레이터

# __제너레이터__(generator)는 간단한 방식으로 구현할 수 있는 이터레이터이며,
# 크게 두 가지 방식으로 생성된다.
# 
# - 제너레이터 함수 활용
# - 제너레이터 표현식 활용
# 
# 이터러블, 이터레이터, 제너레이터 사이의 관계는 다음과 같다.

# <div align="center"><img src="https://nvie.com/img/relationships.png" style="width:700px;"></div>
# 
# 그림 출처: [Iterables vs. Iterators vs. Generators](https://nvie.com/posts/iterators-vs-generators/)

# ### 제너레이터 함수

# 아래 코드는 피보나찌 수열을 무한정 생성하는 제너레이터를 정의한다.
# 
# - `yield`: `return` 키워드 역할 수행. 하지만 실행을 멈추게 하지는 않음.
# - 한 번 실행될 때마다 지정된 순서로 특정 값을 생성함. 
#     미리 모든 값을 생성하는 것이 아니기에 무한 리스트 등을 정의할 때 사용됨.

# In[28]:


def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


# 제너레이터의 항목을 구하려면 `next()` 함수를 이용한다. 
# 내부적으로는 `__next__()` 메서드가 사용된다.
# 이런 의미에서 제너레이터를 하나의 객체로 선언하는 방식으로 사용한다.

# In[29]:


f = fib()


# In[30]:


for _ in range(10):
    print(next(f))


# `__next__()` 가 필요할 때 계속 작동함에 주의해야 한다.

# In[31]:


for _ in range(10):
    print(next(f))


# **__islice()__ 함수**

# 제너레이터 자체는 인덱싱과 슬라이싱을 지원하지 않는다.
# 하지만 __itertools__ 모듈의 __islice()__ 함수를 이용하면 인덱싱과 슬라이싱을 이용할 수 있다.
# 여기서도 `__next__()` 가 필요할 때 계속 작동함에 주의해야 한다.

# In[32]:


from itertools import islice

for x in islice(f, 0, 10):
    print(x)


# 처음부터 다시 생성하려면 다시 호출해야 한다.

# In[33]:


f = fib()

for x in islice(f, 0, 10):
    print(x)


# `fib()` 제너레이터를 이터레이터 클래스로 선언하면 다음과 같다.

# In[34]:


class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


# In[35]:


f = fib()


# In[36]:


for _ in range(10):
    print(next(f))


# ### 제너레이터 표현식

# 조건제시법을 이용하여 리스트를 아래와 같이 생성할 수 있다.

# In[37]:


numbers = [x for x in range(10)]

numbers


# 리스트에 사용되는 대괄호(`[]`) 대신에 튜플에 사용되는 소괄호(`()`)를 사용하면 다르게 작동한다.

# In[38]:


lazy_squares = (x * x for x in numbers)

lazy_squares


# 이유는 리스트 조건제시법은 이터레이터인 리스트를 생성하는 반면에
# 소괄호를 사용하면 제너레이터를 생성한다.
# 제너레이터는 리스트와는 달리 항목을 모두 미리 생성하지는 않고 필요할 때 
# 하나씩 `__next__()` 메서드를 활용하여 생성한다.
# 
# __참고__: `range` 객체 또한 제너레이터이다. 
# 반면에 리스트는 항상 모든 항목을 미리 생성해 놓으며, 따라서 제너레이터가 아니다.

# In[39]:


next(lazy_squares)


# In[40]:


list(lazy_squares)


# ## 연습문제

# 참고: [(실습) 상속](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-inheritance.ipynb)
