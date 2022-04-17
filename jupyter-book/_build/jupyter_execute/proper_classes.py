#!/usr/bin/env python
# coding: utf-8

# (ch:classes)=
# # 클래스의 기본 요소

# **참고:** 아래 내용은 [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds3/index.html)의 2장 내용을 
# 일부 활용한다. 

# ## 기본 클래스

# 클래스를 선언할 때 아래 사항들을 기본적으로 지원하도록 해야 한다. 
# 
# * 문서화: __독스트링__(docstring) 기능을 이용하여 해당 클래스의 기능과 사용법을 설명한다.
#     세 개의 큰 따옴표(`"""`)로 감싸인 문장으로 작성된다.
# 
# * 출력
#     * `__str__()` 메서드: `print()`함수를 이용하여 해당 인스턴스를 출력할 때 활용된다.
#     * `__repr__()` 메서드: `print()` 함수의 영향이 미치지 못하는 곳에서 객체를 보여줄 때 활용된다.
# 
# 다면체 주사위 클래스를 선언하는 과정을 살펴보면서 클래스 선언에 기본적으로 필요한 요소를 살펴본다.

# **예제: 주사위 클래스 `MSDie`**

# 다면체 주사위 객체를 인스턴스로 갖는 `MSDie` 클래스를 선언한 후에 한 단계씩 
# 업데이트 하는 과정을 살펴본다. 
# 생성되는 주사위는 지정된 개수의 면을 갖는다. 
# 즉, 4면체, 6면체, 7면체 등 다면체 주사위 객체를 생성할 수 있도록 생성자를 정의한다.
# 또한 주사위 객체를 생성할 때 주사위가 가리키는 값을 하나 무작위로 지정하도록 한 다음에
# 필요에 따라 주사위 굴리기를 실행하고 그 결과를 저장하도록 한다.

# In[1]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value


# 6면체 주사위 객체를 하나 생성하여 5번 굴린 결과를 확인한다.

# In[2]:


my_die = MSDie(6)

for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()    # 주사위 새로 굴리기


# In[3]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# `print(my_die)`가 `num_sides`와 `current_value`를 활용하여 적절한 출력을
# 만들어 내도록 하려면 `__str__()` 메서드가 적절한 문자열을 출력하도록 해야 한다.
# 또한 리스트의 항목으로 사용된 경우처럼 `print()` 함수가 영향을 미치지 못하는 곳에서
# 객체를 적절하게 출력하도록 하려면 `__repr__()` 메서드의 반환값을
# 적절한 문자열로 지정해야 한다.
# 이유는 
# 리스트를 `print()` 함수의 인자로 사용하면
# 리스트의 항목을 출력하기 위해 `__repr__()` 메서드가 사용된다.

# In[4]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f"MSDie({self.num_sides}): {self.current_value}"


# In[5]:


my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()


# In[6]:


d_list = [MSDie(6), MSDie(20)]
print(d_list)


# ## 비교 가능 클래스

# 두 개의 주사위 객체의 동등성(equality) 여부를 어떻게 판단할까? 
# 두 주사위가 가리키는 값이 같을 때? 주사위 면의 수가 다르면?
# 두 주사위의 크기 비교는 어떻게?
# 
# 아래 질문들에 답하려면 객체 비교와 관련된 아래 메서드 일부 또는 전체를 구현해야 한다.
# 
# * `__lt__`: 작다 연산자(`<`) 지원
# * `__gt__`: 크다 연산자(`>`) 지원
# * `__eq__`: 동등성 연산자(`==`) 지원
# * `__le__`: 작거나 같다 연산자(`<=`) 지원
# * `__ge__`: 크거나 같다 연산자(`>=`) 지원
# * `__ne__`: 비동등성(`!=`) 지원
# 
# 여기서는 두 주사의 크기 비교를 주사위가 가리키는 값(`current_value`)을 이용하여 지정한다.

# In[7]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()   # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

    def __eq__(self,other):
        return self.current_value == other.current_value

    def __lt__(self,other):
        return self.current_value < other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value    


# 비교 연산자들의 활용법은 모두 아래 형식을 따른다.
# 
# ```python
# __eq__(self, other)
# ```
# 
# - `self`: 비교 중심 객체
# - `other`: 비교 대상 객체

# In[8]:


x = MSDie(6)
y = MSDie(7)

x.current_value = 6
y.current_value = 5

print(x == y)
print(x < y)
print(x<=y)


# **최소로 필요한 비교 연산자**
# 
# 앞서 `__gt__()`, `__ge__()`, `__ne__()` 메서드를 정의하지 않았지만
# 자동으로 지원된다. 

# In[9]:


print(x > y)
print(x>=y)
print(x != y)


# **동등성 대 동일성**

# In[10]:


x.current_value = 6
y.current_value = 6

print(x == y)    # 동등성
print(x is y)    # 동일성


# ## 공개 여부

# 자바<font size='2'>Java</font> 프로그래밍 언어의 클래스 선언에 사용되는 
# private, default, protected, public 등과 같은
# 접근 제어자는 파이썬에서 지원되지 않는다.
# 
# 파이썬 클래스의 모든 것은 원칙적으로 공개(public)되며 접근 및 수정될 수 있다.
# 하지만 일부 변수와 메서드는 특별한 방식으로 이름을 지어 외부 노출을 최대한 줄인다. 
# 
# * 두 개의 밑줄("`__`")로 시작하기: 숨기고자 하는 속성 변수와 메서드 이름
# * 한 개의 밑줄("`_`")로 시작하기: 굳이 사용자가 알 필요 없는 속성 변수와 메서드 이름
# 
# 아래 코드는 MSDie 클래스의 생성자를 조금 수정하였다.
# 수정된 내용은 주사위를 굴렸을 때 나온 값에 `__hidden1`을 곱한 후에 `_hidden2`로 
# 나눈 결과를 `current_value`로 가리키도록 하였다.

# In[11]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.__hidden1 = 3                  # 숨긴 변수: 네임 맹글링
        self._hidden2 = 7                   # 숨긴 변수
        
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        randNum = random.randrange(1, self.num_sides+1)
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value


# In[12]:


x = MSDie(6)


# In[13]:


x.current_value


# 그런데 두 밑줄로 시작하는 `__hidden1` 속성은 인스턴스 변수로 확인되지 않는다.

# ```python
# >>> x.__hidden1
# AttributeError                            Traceback (most recent call last)
# <ipython-input-14-5b793c2c1cb0> in <module>
# ----> 1 x.__hidden1
# 
# AttributeError: 'MSDie' object has no attribute '__hidden1'
# ```

# 반면에 하나의 밑줄로 시작하는 `_hidden2` 속성은 인스턴스 변수로 값이 확인된다.

# In[14]:


x._hidden2


# **`__dict__` 변수**

# 객체 `x`가 갖는 인스턴스 속성을 확인하면 다음과 같이 
# 속성 변수와 해당 속성값으로 이루어진 사전을 얻는다.

# In[15]:


x.__dict__


# 그런데 `__hidden1` 변수 대신에 `_MSDie__hidden1` 이 확인된다.
# 이처럼 두 개의 밑줄로 시작하는 변수의 이름이 내부적으로 클래스 이름이 붙는 방식으로 변경된다.
# 이를 __네임 맹글링__(name mangling)이라 한다. 
# 변경된 이름을 이용하면 속성이 확인된다.

# In[16]:


x._MSDie__hidden1


# ## 게터와 세터

# 반면에 하나의 밑줄을 사용하는 `_hidden2`는 숨길 것 까지는 아니지만 클래스 내부에서만
# 사용되는 것을 반영한 이름이다. 
# 이런 변수와 메서드는 사용자가 직접 값을 수정하기 보다는 
# **세터**<font size='2'>setter</font>와 
# **게터**<font size='2'>getter</font> 메서드를 이용하여
# 외부와 내부를 중개하는 역할을 수행하도록 하는 것이 좋다. 
# 이유는 사용자 입장에서 최소한의 정보를 이용하여 객체 속성 정보를 확인하고 이용하도록 만들기 위해서이다. 
# 
# 아래 코드는 `current_value`를 지정하고 확인하는 게터,
# 그리고 `_hidden2`를 확인하고 지정하는 게터와 세터를 선언한다.

# In[17]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.__hidden1 = 3
        self._hidden2 = 7
        
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        randNum = random.randrange(1, self.num_sides+1)
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value
        
    # 게터
    def get_value(self):
        return self.current_value
    
    # 게터
    def get_hidden2(self):
        return self._hidden2

    # 세터
    def set_hidden2(self, num):
        self._hidden2 = num


# In[18]:


x = MSDie(6)


# `current_value` 값을 직접 확인해보자.

# In[19]:


x.current_value


# 게터 메서드를 이용할 수도 있다.

# In[20]:


x.get_value()


# 현재의 `_hidden2` 속성 또한 게터 메서드로 확인해보자.

# In[21]:


x.get_hidden2()


# `x._hidden2` 가 가리키는 값을 세터 메서드를 이용하여 11로 변경해보자.

# In[22]:


x.set_hidden2(11)
print(x.get_hidden2())


# ## 데코레이터

# 게터 메서드와 세터 메서드는 인스턴스 속성을 확인하고 변경한다.
# 따라서 마치 하나의 인스턴스 변수처럼 다룰 수 있으면 보다 편할 것이다.
# 여기서는 파이썬의 데코레이터를 이용하면 이것이 가능하게 만드는 것을 보인다.
# 
# **데코레이터**<font size='2'>decorator</font>는 선언되는 함수에 다른 
# 기능을 추가하는 도구이다.
# 파이썬은 다양한 종류의 데코레이터를 제공한다.
# 하지만 여기서는 게터와 세터를 지정하는 데코레이터만 소개한다.
# 
# 예를 들어, 게터 메서드 바로 이전에 `property` 데코레이터를 지정하면
# 해당 게터 메서드는 인스턴스 변수처럼 사용될 수 있다.
# 또한 세터 메서드 앞에 `게터메서드.setter` 형식의 데코레이터를 지정하면
# 해당 세터 메서드를 인스턴스 변수를 업데이트 하듯이 값을 재할당할 수 있다.

# In[23]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.__hidden1 = 3
        self._hidden2 = 7
        
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        randNum = random.randrange(1, self.num_sides+1)
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value

    # 게터
    @property
    def value_get(self):
        return self.current_value
        
    # 게터
    @property
    def hidden2_get(self):
        return self._hidden2

    # 세터
    @hidden2_get.setter
    def hidden2_set(self, num):
        self._hidden2 = num


# In[24]:


x = MSDie(6)


# In[25]:


x.current_value


# In[26]:


x.value_get


# `x._hidden2` 가 가리키는 값을 11로 변경해보자.
# 그에 맞게 다른 속성도 변한다.

# In[27]:


x.hidden2_set = 11  # x.hidden2_set(11) 에 해당


# In[28]:


x.hidden2_get       # x.hidden2 에 해당


# 데코레이터를 사용하면 심지어 게터와 세터를 동일한 이름으로 지정할 수 있다.

# In[29]:


import random

class MSDie:
    """
    다면체 주사위
    
    인스턴스 변수: 
        num_sides: 면 개수
        current_value: 주사위를 굴린 결과
    """

    def __init__(self, num_sides):
        self.__hidden1 = 3                  # 네임 맹글링
        self._hidden2 = 7
        self.num_sides = num_sides
        self.current_value = self.roll()    # 주사위 굴리기 먼저 실행

    def roll(self):   # 주사위 굴리기
        randNum = random.randrange(1, self.num_sides+1)
        self.current_value = (self.__hidden1 * randNum) % self._hidden2 
        return self.current_value

    @property
    def value_get(self):
        return self.current_value

    # _hidden2의 게터
    @property
    def hidden2(self):
        return self._hidden2

    # _hidden2의 세터
    @hidden2.setter
    def hidden2(self, num):
        self._hidden2 = num


# In[30]:


x = MSDie(6)


# `x._hidden2` 의 값을 11로 바꾼다.

# In[31]:


x.hidden2 = 11


# 11로 변경된 것을 확인한다.

# In[32]:


x.hidden2


# :::{admonition} 주의 사항
# :class: warning
# 
# 게터와 세터의 이름을 동일하게 적용하는 경우
# 세터 메서드를 직접 호출하면 오류가 발생할 수 있다.
# 
# ```python
# >>> x.hidden2(11)
# TypeError                                 Traceback (most recent call last)
# /tmp/ipykernel_8430/3341417680.py in <module>
# ----> 1 x.hidden2(11)
# 
# TypeError: 'int' object is not callable
# ```
# 
# 이유는 `hidden2` 가 인스턴스 변수처럼 작동하기 때문이며, 
# 위의 경우 정수 11을 가리키며, 
# `hidden2(11)` 은 따라서 `11(11)` 이라는 실행이 불가능한 함수 호출로 처리되기 때문이다.
# :::

# ## 클래스 변수 대 인스턴스 변수

# In[ ]:





# In[ ]:





# ## 인스턴스 메서드, 클래스 메서드, 스태틱 메서드

# In[ ]:





# In[ ]:





# ## 연습문제

# 참고: [(실습) 클래스의 기본 요소](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-proper_classes.ipynb)
