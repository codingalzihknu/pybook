#!/usr/bin/env python
# coding: utf-8

# (ch:inheritance)=
# # 상속

# **상속**<font size='2'>inheritance</font>은 객체 지향 프로그래밍의 또 다른 주요 요소이다. 
# 클래스를 선언할 때 다른 클래스의 속성과 메서드를 상속 받아 활용할 수 있다.
# 상속을 받는 클래스를 **자식 클래스** 또는 **하위 클래스**, 
# 상속을 하는 클래스를 **부모 클래스** 또는 **상위 클래스**라고 부른다. 

# ## 모음 자료형의 상속 체계

# 아래 그림은 파이썬 모음 자료형의 상속 체계를 보여준다. 
# 예를 들어, `list` 클래스는 `Sequence` 클래스를 상속하며,
# `Sequence`는 `Collection` 클래를 상속한다. 
# 이렁 이유로 "리스트는 순차<font size='2'>Sequence</font> 자료형이다" 등으로 말한다.
# 이와 달리 항목들의 순서를 고려하지 않는 `dict`와 `set` 은 순차 자료형이 아니다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/inheritance1.png" width="70%"></div>
# 
# <그림 출처: [Problem Solving with Algorithms and Data Structures using Python의 1.13 절](https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html)>

# `list`, `tuple`, `str` 클래스 모두 `Sequence` 클래스를 상속하기에
# 인덱싱, 슬라이싱 등 자신들의 항목을 다루는 공통된 방식을 갖는다.
# 반면에 각 자료형마다 서로 다른 메서드를 제공한다.
# 이렇듯 한 클래스의 여러 자식 클래스는 서로 공통된 요소와 함께 
# 각 자식 클래스 고유의 요소를 갖는다.

# 클래스를 상속할 때의 가장 큰 장점은 
# 첫째, 기존에 작성된 코드를 필요에 따라 수정하고 재활용 할 수 있다는 것과
# 둘째, 자식 클래스의 인스턴스들 사이의 관계를 보다 잘 이해할 수 있다는 것이다. 

# 두 가지 예제를 이용하여 상속을 설명한다. 

# ## 벡터의 내적

# 벡터는 정수 또는 부동소수점의 리스트를 의미하며
# 길이가 같은 두 벡터의 내적은 각 항목끼리의 곱셈의 합이다. 
# 예를 들어 `[2, 3, 4]` 와 `[5, 6, 9]` 두 벡터의 내적은 다음과 같다.
# 
# ```python
# 2 * 5 + 3 * 6 + 4 * 9
# ```

# 리스트 클래스 `list` 는 벡터의 내적 연산자를 지원하지 않는다.
# 따라서 내적 연산을 지원하도록 `list` 클래스의 기능을 확장해야 한다. 

# ### Vector 클래스

# 아래 코드는 `list` 클래스를 상속하면서 내적 연산자를 지원하는 `Vector` 클래스를
# 정의한다.
# 
# - `super().__init__()`: 부모 클래스의 생성자 호출.
#     자식 클래스의 생성자를 호출할 때 호출되면
#     부모 클래스의 속성과 메서드를 모두 상속받음.
# - `dot()` 메서드: 추가되는 메서드. 내적 반환.
# - `len` 속성: 추가되는 인스턴스 속성. 벡터의 길이.

# In[1]:


# list 클래스 상속

class Vector(list):
    # Vector 클래스 생성자 재정의
    def __init__(self, items):
        """
        - list 클래스 상속
        - items: 벡터로 사용될 리스트
        """
        
        # 부모 클래스 생성자 호출
        super().__init__(items)
        
        # 속성 추가
        self.len = self.__len__()
            
    # 내적 메서드
    def dot(self, other):
        """
        벡터 내적
        """

        # 벡터의 길이가 다르면 실행 오류 발생
        if self.len != other.len:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        # 내적 계산: 각 항목들의 곱의 합
        # 리스트를 상속하기에 인덱싱 사용 가능
        sum = 0
        for i in range(self.len):
            sum += self[i] * other[i]

        return sum


# 두 개의 벡터를 생성하자.

# In[2]:


x = Vector([2, 3, 4])
y = Vector([5, 6, 9])


# `__str__()` 등 리스트의 모든 매직 메서드와
# `append()` 등의 다른 모든 메서드,
# 그리고 인덱싱, 슬라이싱 등 
# 리스트의 모든 기능을 활용할 수 있다.

# - `__str__()` 메서드

# In[3]:


print(x)


# * `append()` 메서드

# In[4]:


x.append(5)
x


# * `pop()` 메서드

# In[5]:


x.pop()
x


# * 인덱싱

# In[6]:


x[0]


# * 슬라이싱

# In[7]:


x[::2]


# 리스트 클래스에 없던 속성과 메서드도 당연히 지원된다.

# * `len` 속성

# In[8]:


x.len


# * 내적

# In[9]:


x.dot(y)


# In[10]:


x.dot(y) == 2 * 5 + 3 * 6 + 4 * 9


# 벡터의 내적을 자주 활용한다면 함수로 지정하는 게 좋다.
# 아래 `dot()` 함수는 벡터 인자에 대해서만 작동하도록 구현되었다.

# In[11]:


def dot(x, y):
    assert isinstance(x, Vector) and isinstance(y, Vector)
    
    return x.dot(y)


# In[12]:


dot(x, y) == x.dot(y)


# ### 메서드 재정의

# 상속 받은 메서드를 재정의할 수 있다.
# 사실 `Vector` 클래스의 생성자 메서드는
# 부모 클래스인 `list` 클래스의 생성자를 재정의 하였다.
# 생성자 이외의 상속 받은 다른 메서드도 필요에 따라 재정의할 수 있다.

# **벡터 합**

# 예를 들어, `+` 연산자는 두 개의 리스트를 이어붙인다. 
# 반면에 벡터의 덧셈은 동일한 위치의 항목들의 합으로 이루어진 벡터를 계산한다.
# 이런 벡터 연산을 지원하며려 `__add__()` 메서드를 재정의하면 된다.

# In[13]:


# list 클래스 상속

class Vector(list):
    # Vector 클래스 생성자 재정의
    def __init__(self, items):
        """
        - list 클래스 상속
        - items: 벡터로 사용될 리스트
        """
        
        # 부모 클래스 생성자 호출
        super().__init__(items)
        
        # 속성 추가
        self.len = self.__len__()
            
    # 내적 메서드
    def dot(self, other):
        """
        벡터 내적
        """

        # 벡터의 길이가 다르면 실행 오류 발생
        if self.len != other.len:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        # 내적 계산: 각 항목들의 곱의 합
        # 리스트를 상속하기에 인덱싱 사용 가능
        sum = 0
        for i in range(self.len):
            sum += self[i] * other[i]

        return sum
    
    # 벡터 합 메서드
    def __add__(self, other):
        """
        벡터 합
        """

        # 벡터의 길이가 다르면 실행 오류 발생
        if self.len != other.len:
            raise RuntimeError("두 벡터의 길이가 달라요!")

        # 벡터 합 계산: 각 항목들의 합으로 이루어진 벡터
        new_list = []
        
        for i in range(self.len):
            item = self[i] + other[i]
            new_list.append(item)

        return Vector(new_list)
    
# dot 함수도 새로 정의해야 함.
def dot(x, y):
    assert isinstance(x, Vector) and isinstance(y, Vector)
    
    return x.dot(y)


# 클래스를 수정하면 인스턴스를 새로 생성해야
# 변경된 내용이 반영된다.

# In[14]:


x = Vector([2, 3, 4])
y = Vector([5, 6, 9])


# 벡터 내적은 동일하게 작동한다.

# In[15]:


x.dot(y)


# In[16]:


dot(x, y)


# 벡터의 합이 이제 지원된다.

# In[17]:


x + y


# ## 연습문제

# 참고: [(실습) 상속](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-inheritance.ipynb)
