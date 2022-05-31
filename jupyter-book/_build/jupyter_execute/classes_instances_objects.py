#!/usr/bin/env python
# coding: utf-8

# (ch:classes_instances_objects)=
# # 클래스, 인스턴스, 객체

# **참고** 
# 
# 아래 내용은 [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds3/index.html)의 1.13 절 내용을 
# 일부 활용한다. 

# **주요 내용**
# 
# 파이썬은 객체 지향 프로그래밍 언어이다.
# 객체 지향 프로그래밍 언어의 가장 큰 장점 중의 하나로,
# 사용자가 직접 필요한 자료형을 클래스로 정의하고 객체를 생성하여 활용할 수 있다.
# 
# 여기서는 `fractions` 모듈에 포함된 `Fraction` 클래스를
# 직접 정의하는 과정을 다루면서 클래스, 인스턴, 객체 개념을 소개한다. 
# `Fraction` 클래스는 `1/2`, `2/7` 처럼 기약분수들의 자료형 역할을 수행하고
# 분수들의 덧셈, 크기 비교 등을 지원하도록 할 것이다. 

# ## 클래스 선언과 생성자

# ### 클래스 선언

# 분수들의 클래스를 정의해보자.
# 클래스 정의는 다음 형식으로 이루어진다.

# In[1]:


class Fraction:
    ...
    # 속성 지정 및 메서드 선언


# `Fraction` 클래스의 속성으로 "임의의 정수인 분자와 0이 아닌 임의의 정수인 분모"에 
# 대한 정보가 저장된다.
# `Fraction` 클래스가 제공해야 하는 메서드로
# 예를 들어 분수의 사칙연산, 크기 비교 등이 포함된다.

# ### 생성자

# 모든 파이썬 클래스는 인스턴스<font size='2'>instance</font>를 생성하는 **생성자**인 
# `__init__()` 메서드를 포함해야 한다. 
# 생성자는 생성되는 인스턴스의 속성<font size='2'>attributes</font>으로 저장될 정보와 관련된 값을 
# 인자로 받는다.
# `Fraction` 클래스의 생성자는 분자와 분모에 해당하는 값을 받아 저장하는 기능을 수행한다.

# In[2]:


class Fraction:
    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """

        self.top = top
        self.bottom = bottom


# :::{admonition} 인스턴스 초기 설정
# :class: info
# 
# 엄밀히 말하면 `__init__()` 메서드는 객체를 생성하는 게 아니라
# 생성되는 객체의 초기 설정을 담당하지만
# 생성자라는 표현이 일반적으로 사용된다.
# :::

# ## 인스턴스와 객체

# ### 인스턴스 생성

# `Fraction` 클래스의 **인스턴스**<font size='2'>instance</font>, 
# 즉 하나의 분수에 해당하는 **객체**<font size='2'>object</font>를 생성하는 방식은 다음과 같다.
# 
# ```python
# >>> Fraction(3, 5)
# ```
# 
# 그러면 생성자 함수 `__init__()` 가 분자에 해당하는 3, 분모에 해당하는 5를 인자로 사용하여
# 호출된다.
# 아래 코드는 `3/5` 에 해당하는 객체, 즉 `Fraction` 클래스의 인스턴스를 가리키는 
# `f35` 변수를 선언한다.

# In[3]:


f35 = Fraction(3, 5)


# 메모리 상에서 `f35` 변수가 가리키는 분수 객체는 아래와 같이 구성된다.

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/fraction1.png" width="80%"></div>

# :::{admonition} `self`의 역할
# :class: info
# 
# `f35 = Fraction(3, 5)` 방식으로 변수 할당이 실행되면
# 파이썬 해석기는 다음을 싱행한다.
# 
# ```python
# >>> __init__(f35, 3, 5)
# ```
# 
# 즉, `self` 매개변수는 현재 생성되는 객체를 인자로 사용한다.
# :::

# ### 인스턴스 변수와 속성

# **인스턴스 변수**<font size='2'>instance variable</font>는
# 클래스 내부에서 `self`와 함께 선언된 변수를 가리킨다.
# `Fraction` 클래스의 인스턴스 변수는 `self.top` 과 `self.bottom` 두 개다.
# 인스턴스 변수는 해당 클래스의 영역<font size='2'>scope</font> 내에서만 의미를 갖는다.
# 인스턴스 변수는 일반적으로 생성자가 실행되는 동안 선언되지만
# 클래스 내부 어딘가에서 일반 전역 변수처럼 선언될 수도 있다.
# 
# 클래스의 인스턴스는 인스턴스 변수가 가리키는 값을 속성을 갖게 되며,
# 이런 의미에서 인스턴스 변수가 가리키는 값을 
# **인스턴스 속성**<font size="2">instance attribute</font>이라 부른다.
# 인스턴스 속성은 따라서 클래스의 인스턴스가 생성되어야만 의미를 갖는다.
# 
# 인스턴스 변수 이외에 `self` 를 사용하지 않는 
# **클래스 변수**<font size='2'>class variable</font> 가 선언될 수도 있지만
# 이에 대해서는 나중에 자세히 소개한다.
# 
# `f35` 가 가리키는 객체의 인스턴스 변수와 인스턴스 속성을 각각 키와 값으로 갖는 
# 항목들의 사전을 `__dict__` 의 속성으로 확인한다.
# `__dict__` 는 모든 객체에 기본으로 포함되는 속성 중에 하나다.

# In[4]:


f35.__dict__


# 모든 객체에 기본으로 포함된 속성 중에 해당 객체의 클래스 정보를 가리키는 `__class__` 속성도 
# 종종 사용된다.

# In[5]:


f35.__class__


# `__main__` 은 현재 실행되는 코드가 저장된 모듈을 가리킨다.
# 따라서 `__main__.Fraction` 는 현재 파일에서 정의된 `Fraction` 클래스의 객체라는
# 사실을 확인해준다.

# ## 인스턴스 메서드

# 클래스 내부에 선언된 함수를 메서드라 부른다. 
# 이중에 첫째 매개변수로 `self` 를 사용하는 함수가 인스턴스 메서드다.
# 인스턴스 메서드는 클래스의 인스턴스가 생성되어야만 활용될 수 있다.
# 인스턴스 메서드 이외에 클래스 메서드, 정적 메서드 등이 있지만 여기서는 다루지 않는다.

# ### 매직 메서드

# 매직 메서드<font size='2'>magic method</font>는 클래스에 기본적으로 포함되는 메서드다.
# 매직 메서드의 이름은 밑줄 두 개로 감싸지며, 
# 클래스가 기본적으로 갖춰야 하는 기능을 제공한다.
# 
# 클래스에 기본으로 포함된 매직 메서드를 `dir()` 함수를 이용하여 확인할 수 있다.
# 그러면 `__class__`, `__dict__` 등과 같은 기본 속성과 함께 다른 다양한 기본 속성과
# 매직 메서드의 리스트를 확인할 수 있다.

# In[6]:


dir(f35)


# 이중에 중요한 매직 메서드 몇 개를 살펴본다.

# **`__str__()` 메서드**
# 
# `f35` 는 '3/5'에 해당하는 분수를 가리킨다.
# 그런데 `print()` 함수를 이용하여 이 사실을 확인하려면 
# 이상한 결과만 확인한다.

# In[7]:


print(f35)


# 이유는 `Fraction` 클래스가 자신의 인스턴스를 소개하는 기능을 제공하지 않았기 때문이다. 
# 이런 상황에서 `f35` 입장에서는 자신이 어떤 클래스의 인스턴스이며 
# 자신이 저장된 메모리 주소만을 알려주게 된다.
# 
# 클래스의 인스턴스가 제대로 자신을 소개하도록 하려면 `__str__()` 메서드를
# 사용하가 직접 정의해야 한다. 
# 즉, `__str__()` 메서드는 해당 클래스의 인스턴스를 `print()` 함수를 통해
# 어떻게 보여줄 것인가를 문자열로 지정하는 함수로 활용된다.

# `Fraction` 클래스를 선언할 때 `__str__()` 메서드를 아래처럼 재정의(overriding) 해보자.

# In[8]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"  # 3/5, 1/2 형식으로 출력


# 클래스를 재정의 했으면 객체로 새로 생성해야 한다.

# In[9]:


f35 = Fraction(3, 5)


# 이제 `print()` 함수를 실행하면
# 3/5, 1/2 등의 형식으로 출력한다.

# In[10]:


print(f35)


# In[11]:


print(f"피자의 {f35}를 먹었다.")


# `__str__()` 메서드를 직접 호출해도 동일한 결과를 얻는다. 

# In[12]:


f35.__str__()


# `str()` 함수는 인자로 사용된 객체가 제공하는 `__str__()` 메서드를 내부에서 호출한다.

# In[13]:


str(f35) # f35.__str__()


# **`__repr__()` 메서드**
# 
# `print()` 함수는 잘 작동한다.
# 하지만 그냥 `f35` 를 확인하려하면 여전히 제대로 보여지지 않는다.

# In[14]:


f35


# 이를 해결하려면 `__repr__()` 메서드를 `__str__()` 메서드처럼 추가해야 한다.

# In[15]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"  # 3/5, 1/2 형식으로 출력
    
    def __repr__(self):
        return f"{self.top}/{self.bottom}"  # 3/5, 1/2 형식으로 출력


# In[16]:


f35 = Fraction(3, 5)


# In[17]:


f35


# `__repr__()` 를 `__str__()` 와 다르게 정의해도 된다.

# In[18]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"  # 3/5, 1/2 형식으로 출력
    
    def __repr__(self):
        return f"{self.bottom}분의 {self.top}"  # 5분의 3 형식으로 출력


# In[19]:


f35 = Fraction(3, 5)


# In[20]:


f35


# In[21]:


print(f35)


# `__repr__()` 메서드를 `__str__()` 대신 사용할 수 있다.

# In[22]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

#     def __str__(self):
#         return f"{self.top}/{self.bottom}"  # 3/5, 1/2 형식으로 출력
    
    def __repr__(self):
        return f"{self.bottom}분의 {self.top}"  # 5분의 3 형식으로 출력


# In[23]:


f35 = Fraction(3, 5)


# In[24]:


f35


# In[25]:


print(f35)


# 따라서 `__repr__()` 와 `__str__()` 를 동일하게 작동하게 하려면
# `__repr__()` 메서드 하나만 구현하면 된다.

# In[26]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

    def __repr__(self):
        return f"{self.top}/{self.bottom}"  # 3/5, 1/2 형식으로 출력


# **`__add__()` 메서드**
# 
# 아래 두 개의 이용하여 분수의 덧셈이 가능한지 확인해보자.

# In[27]:


f14 = Fraction(1, 4)
f12 = Fraction(1, 2)


# 그런데 분수의 덧셈을 시도하면 오류가 발생한다.

# ```>>> f1 + f2
# TypeError                                 Traceback (most recent call last)
# <ipython-input-13-ad0256b81ae0> in <module>
# ----> 1 f1 + f2
# 
# TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
# ```

# 이유는 덧셈 연산자 `+`가 `Fraction` 클래스의 인스턴스에 대해 지원되지 않기 때문이다. 
# 
# 덧셈, 뺄셈 등 사칙연산에 대해 일반적으로 사용되는 기호를 사용하려면
# 각각의 기호에 해당하는 매직 메서드를 선언해야 한다. 
# 예를 들어 분수의 덧셈을 위해 `+` 연산자를 사용하려면 
# `Fraction` 클래스에 `__add__()` 메서드가 적절하게 정의되어 있어야 한다.

# :::{admonition} 분수의 덧셈
# :class: info
# 
# 분수의 덧셈은 아래와 같이 정의된다.
# 
# $$\frac {a}{b} + \frac {c}{d} = \frac {ad}{bd} + \frac {cb}{bd} = \frac{ad+cb}{bd}$$
# :::
# 
# 분수의 덧셈을 지원하는 `__add__()` 메서드를 `Fraction` 클래스에 추가하자.

# In[28]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other_fraction):
        new_top = self.top * other_fraction.bottom + self.bottom * other_fraction.top
        new_bottom = self.bottom * other_fraction.bottom

        return Fraction(new_top, new_bottom)


# In[29]:


f14 = Fraction(1, 4)
f12 = Fraction(1, 2)
print(f14 + f12)


# 덧셈이 잘 작동하지만 결과값이 기약분수의 형태가 아니다. 
# 기약분수를 계산하려면 최대공약수(gcd)를 계산하는 알고리즘이 필요하다.

# :::{prf:example} 유클리드 호젯법
# :label: euclid_gcd
# 
# 두 개의 정수 $m$과 $n$의 최대공약수를 가장 빠르고 효율적으로 계산하는 기법은 유클리드 호젯법이다.
# 
# - $m$을 $n$으로 나눌 수 있으면 $n$이 최대공약수이다.
# - 그렇지 않으면 $n$과 $m\,\%\, n$의 최대공약수가 원하는 최대공약수이다.
# :::

# 위 기법을 구현하면 다음과 같다.

# In[30]:


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


# In[31]:


print(gcd(20, 10))
print(gcd(20, 30))


# `gcd()` 함수를 `__add__()` 함수의 정의에 활용하자. 

# In[32]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other_fraction):
        new_num = self.top * other_fraction.den +                      self.bottom * other_fraction.num
        new_den = self.bottom * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)


# 이제 `Fraction`의 인스턴스는 생성자를 제외하고 두 개의 메서드를 더 갖는다.

# <figure>
# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/fraction2.png" width="50%">
# </figure>

# 이제 8/6이 아니라 3/4를 반환한다.

# In[33]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)


# **`__eq__()` 메서드: 객체의 동등성과 동일성**
# 
# 두 객체의 __동일성__(identity) 여부는 비교되는 두 객체가 동일한 메모리 주소에 저장되었는가에 따라 결정된다.
# 반면에 메모리의 주소가 아니라 객체가 표현하는 값의 동일성 여부에 따라
# 두 값을 비교 판정하는 것은 __동등성__(equality) 여부이다. 
# 
# 예를 들어, 아래 두 객체 모두 분수 1/2를 객체를 가리키지만 서로 독립적으로 생성되었기에
# 서로 다른 메모리에 저장되며, 따라서 두 변수 `x`와 `y`는 서로 다른 객체를 참조한다.
# 따라서 두 변수가 참조하는 값은 동등하지 않다고 판정된다.
# 이와같이 두 값의 동등성을 판단하는 것을 __얕은 동등성__(shallow equality)이라 부른다.

# x = Fraction(1, 2)
# y = Fraction(1, 2)
# x == y

# 물론 두 객체가 동일하지 않다고 판단된다.

# x is y

# __참고__: [PythonTutor-얕은 동등성](https://pythontutor.com/visualize.html#code=class%20Fraction%3A%0A%20%20%20%20%22%22%22Fraction%20%ED%81%B4%EB%9E%98%EC%8A%A4%22%22%22%0A%0A%20%20%20%20def%20__init__%28self,%20top,%20bottom%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%EC%83%9D%EC%84%B1%EC%9E%90%20%EB%A9%94%EC%84%9C%EB%93%9C%0A%20%20%20%20%20%20%20%20top%3A%20%EB%B6%84%EC%9E%90%0A%20%20%20%20%20%20%20%20bottom%3A%20%EB%B6%84%EB%AA%A8%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20self.top%20%3D%20top%0A%20%20%20%20%20%20%20%20self.bottom%20%3D%20bottom%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.top%7D/%7Bself.bottom%7D%22%0A%0A%20%20%20%20def%20__add__%28self,%20other_fraction%29%3A%0A%20%20%20%20%20%20%20%20new_num%20%3D%20self.top%20*%20other_fraction.den%20%2B%20%5C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.bottom%20*%20other_fraction.num%0A%20%20%20%20%20%20%20%20new_den%20%3D%20self.bottom%20*%20other_fraction.den%0A%20%20%20%20%20%20%20%20common%20%3D%20gcd%28new_num,%20new_den%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20Fraction%28new_num%20//%20common,%20new_den%20//%20common%29%0A%0Ax%20%3D%20Fraction%281,%202%29%0Ay%20%3D%20Fraction%281,%202%29%0Aprint%28x%20%3D%3D%20y%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# 반면에 아래처럼 두 변수가 참조하는 객체를 동일(identical)하게 하면 당연히 다른 결과가 나온다.

# x = Fraction(1, 2)
# y = x
# print(x == y)
# print(x is y)

# <figure>
# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/fraction3.png" width="80%">
# </figure>

# 반면에 __깊은 동등성__(deep equality)은 두 객체가 (의도된) 동일한 값을
# 가리키는가 여부를 결정하며, 이를 위해 
# `__eq__` 매직 메서드를 이용한다.
# 두 분수의 동등성은 아래와 같이 정의된다.
# 
# $$\frac {a}{b} = \frac {c}{d} \Longleftrightarrow ad = bc$$
# 
# 이를 구현하는 `__eq__()` 메서드를 `Fraction` 클래스에 추가하자.

# class Fraction:
#     """Fraction 클래스"""
# 
#     def __init__(self, top, bottom):
#         """생성자 메서드
#         top: 분자
#         bottom: 분모
#         """
#         self.top = top
#         self.bottom = bottom
# 
#     def __str__(self):
#         return f"{self.top}/{self.bottom}"
# 
#     def __add__(self, other_fraction):
#         new_num = self.top * other_fraction.den + \
#                      self.bottom * other_fraction.num
#         new_den = self.bottom * other_fraction.den
#         common = gcd(new_num, new_den)
#         
#         return Fraction(new_num // common, new_den // common)
# 
#     def __eq__(self, other_fraction):
#         first_num = self.top * other_fraction.den
#         second_num = other_fraction.num * self.bottom
# 
#         return first_num == second_num

# 이제 동등성이 의도한대로 작동한다.

# x = Fraction(1, 2)
# y = Fraction(1, 2)
# print(x == y)

# 동일성은 동등성과 상관없이 전혀 변하지 않는다.

# x = Fraction(1, 2)
# y = Fraction(2, 3)
# print(x == y)

# **`__dir__()` 메서드**
# 
# 객체의 모든 속성과 메서드를 확인하기 위해 아래와 같이 실행한다. 

# x.__dir__()

# 예를 들어, `__class__` 변수는 객체가 속하는 클래스 이름을 속성값으로 갖는다.

# x.__class__

# ### 기타 메서드

# - 분수를 부동소수점으로 변환 메서드 등등

# ## 연습문제

# 참고: [(실습) 클래스, 인스턴스, 객체](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-classes_instances_objects.ipynb)
