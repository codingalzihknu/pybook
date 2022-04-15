#!/usr/bin/env python
# coding: utf-8

# # 객체 지향 프로그래밍

# **참고:** 아래 내용은 [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds3/index.html)의 1.13 절 내용을 
# 일부 활용한다. 

# 파이썬은 객체 지향 프로그래밍 언어이다.
# 객체 지향 프로그래밍 언어의 가장 큰 장점 중의 하나로,
# 사용자가 직접 필요한 자료형을 클래스로 정의하고 객체를 생성하여 활용할 수 있다.
# 
# 여기서는 분수 자료형인 `Fraction` 클래스를 정의하기 위해 다양하며 필요한 
# __상태__<font size='2'>state</font>와 __메서드__<font size='2'>method</font>를
# 추가하는 과정을 자세히 소개한다.

# ## 클래스 선언

# 분수들의 클래스를 자료형으로 정의해보자.
# `Fraction` 클래스의 상태는 아래 정보를 담는다.
# 
# - 임의의 정수인 분자와 0이 아닌 임의의 정수인 분모
# 
# `Fraction` 클래스는 기본적으로 분수들의 사칙연산 기능을 제공해야 한다.
# 또한 '3/5'와 같이 표현할 수 있어야 하며, 사칙연산의 계산결과는
# 모두 기약분수로 표현되도록 한다.
# 
# 파이썬을 이용한 클래스 정의 형식은 다음과 같다.
# 
# ```python
# class Fraction:
#     
#     # 상태 지정 및 메서드 선언
# ```

# ## 생성자

# 모든 파이썬 클래스는 인스턴스<font size='2'>instance</font>를 생성하는 **생성자**인 
# `__init__()` 메서드를 포함해야 한다. 
# 생성자는 생성되는 인스턴스의 상태<font size='2'>로 저장될 정보와 관련된 값을 
# 인자로 받는다.
# `Fraction` 클래스의 생성자는 분자와 분모에 해당하는 값을 받아 저장하는 기능을 수행한다.

# In[1]:


class Fraction:
    """Fraction 클래스"""
    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """

        self.num = top
        self.den = bottom


# ## 인스턴스

# `Fraction` 클래스의 **인스턴스**<font size='2'>instance</font>, 
# 즉 하나의 분수에 해당하는 **객체**<font size='2'>object</font>를 생성하는 방식은 다음과 같다.
# 
# ```python
# Fraction(3, 5)
# ```
# 
# 그러면 생성자 함수 `__init__()` 가 분자에 해당하는 3, 분모에 해당하는 5를 인자로 사용하여
# 호출된다.
# 아래 코드는 `3/5` 에 해당하는 객체, 즉 `Fraction` 클래스의 인스턴스를 가리키는 
# `my_fraction` 변수를 선언한다.

# In[2]:


my_fraction = Fraction(3, 5)


# <figure>
# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/fraction1.png" width="50%">
# </figure>

# :::{admonition} `self`의 역할
# :class: info
# 
# `my_fraction = Fraction(3, 5)` 방식으로 변수 할당이 실행되면
# 파이썬 해석기는 다음을 싱행한다.
# 
# ```python
# __init__(my_fraction, 3, 5)
# ```
# 
# 즉, `self` 매개변수는 현재 생성되는 객체를 인자로 사용한다.
# :::

# ## 인스턴스 변수와 속성

# 클래스에서 선언된 `self.num` 과 `self.den` 은 
# **인스턴스 변수**<font size='2'>instance variable</font>다.
# 인스턴스 변수는 해당 클래스의 영역 내에서만 의미를 가지며
# 기본적으로 생성자가 실행되는 과정, 즉
# 클래스의 인스턴스가 생성되는 과정에서 선언된다.
# 
# **인스턴스 속성**<font size="2">instance attribute</font>은 
# 인스턴스 변수에 할당된 값이며,
# 생성된 객체의 속성을 나타낸다.
# 
# 인스턴스 변수는 생성자 이외에도 클래스 내부에서 다른 방식으로 선언될 수 있다.
# 
# 

# :::{admonition} 클래스 변수
# :class: info
# 
# 클래스 내부에서 선언되는 변수는
# `self` 와 함께 선언되는 인스턴스 변수와
# `self` 없이 일반적인 변수처럼 선언되는 
# **클래스 변수**<font size='2'>class variable</font>로 구분된다.
# 여기서는 인스턴스 변수만 다루면 클래스 변수는 나중에 소개한다.
# :::

# ## 매직 메서드

# **`__str__()` 메서드**
# 
# `my_frantion`이 가리키는 분수는 '3/5'에 해당하는 분수이다. 
# 그런데 `print()` 함수를 이용하여 이 사실을 확인하려면 
# 이상한 결과만 확인한다.

# In[3]:


print(my_fraction)


# 이유는 `Fraction` 클래스가 자신의 인스턴스를 소개하는 기능을 제공하지 않았기 때문이다. 
# 결국 `my_fraction` 입장에서는 자신이 어떤 클래스의 인스턴스이며 
# 자신이 저장된 메모리 주소만을 알려준다. 

# 파이썬의 모든 클래스는 생성자와 함께 기본적으로 포함하는 메서드 목록이 있다. 
# 이유는 파이썬의 모든 클래스는 기본적으로 최상위 클래스인 `object` 클래스를 
# 상속한다.
# 따라서 `Fraction` 클래스의 엄밀한 정의는 다음과 같다. 

# In[4]:


class Fraction(object):
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom


# 상속을 통해 `__init__()` 등 기본으로 지정된 메서드를 여러 개 함께 상속한다.
# 이렇게 자동으로 상속받으며 두 개의 밑줄이 양쪽을 감싼느 메서드를 __매직 메서드__(magic method)라 부르며,
# 이중에 `__str__()` 메서드도 포함된다.
# 이 사실을  `dir()` 함수를 이용하여 확인할 수 있다.

# In[5]:


dir(Fraction)


# 언급된 매직메서드 각자는 고유의 역할을 수행하기에 준비되었지만 대부분 본체가 없는,
# 즉 제대로 정의되지 않은 채로 상속된다. 
# 이 중에 `__str__()` 메서드는 해당 클래스의 인스턴스를 `print()` 함수를 통해
# 어떻게 보여줄 것인가를 문자열로 지정하는 함수로 활용된다.

# `Fraction` 클래스를 선언할 때 `__str__()` 메서드를 아래처럼 재정의(overriding) 해보자.

# In[6]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"


# In[7]:


my_fraction = Fraction(3, 5)


# 이제 `print()` 함수가 원했던 대로 작동한다.

# In[8]:


print(my_fraction)


# `__str__()` 메서드를 직접 호출해도 동일한 결과를 얻는다. 

# In[9]:


my_fraction.__str__()


# In[10]:


print(f"피자의 {my_fraction}를 먹었다.")


# `str()` 함수는 인자로 사용된 객체가 제공하는 `__str__()` 메서드를 내부에서 호출한다.

# In[11]:


str(my_fraction)


# **`__add__()` 메서드**
# 
# 분수의 덧셈을 시도하면 오류가 발생한다.
# 
# ```python
# f1 = Fraction(1, 4)
# f2 = Fraction(1, 2)
# 
# f1 + f2
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-13-ad0256b81ae0> in <module>
# ----> 1 f1 + f2
# 
# TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'
# ```
# 
# 이유는 덧셈 연산자 `+`가 `Fraction` 클래스의 인스턴스에 대해 지원되지 않기 때문이다. 
# 
# 덧셈, 뺄셈 등 사칙연산에 대해 일반적으로 사용되는 기호를 사용하려면
# 각각의 기호에 해당하는 매직 메서드를 선언해야 한다. 
# 예를 들어 분수의 덧셈을 위해 `+` 연산자를 사용하려면 
# `Fraction` 클래스에 `__add__()` 메서드가 적절하게 정의되어 있어야 한다.
# 그러면 아래 표현식은 `f1 + f2`에 해당하는 값을 가리키게 된다.
# 
# ```python
# f1.__add__(f2)
# ```

# 분수의 덧셈은 아래와 같이 정의된다.
# 
# $$\frac {a}{b} + \frac {c}{d} = \frac {ad}{bd} + \frac {cb}{bd} = \frac{ad+cb}{bd}$$
# 
# 이를 구현하는 `__add__()` 메서드를 `Fraction` 클래스에 추가하자.

# In[12]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den +                     self.den * other_fraction.num
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)


# In[13]:


f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)


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

# In[14]:


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


# In[15]:


print(gcd(20, 10))
print(gcd(20, 30))


# `gcd()` 함수를 `__add__()` 함수의 정의에 활용하자. 

# In[16]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den +                      self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)


# 이제 `Fraction`의 인스턴스는 생성자를 제외하고 두 개의 메서드를 더 갖는다.

# <figure>
# <img src="https://raw.githubusercontent.com/codingalzi/problem_solving_with_algorithms/master/_sources/Introduction/Figures/fraction2.png" width="50%">
# </figure>

# 이제 8/6이 아니라 3/4를 반환한다.

# In[17]:


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

# In[18]:


x = Fraction(1, 2)
y = Fraction(1, 2)
x == y


# 물론 두 객체가 동일하지 않다고 판단된다.

# In[19]:


x is y


# __참고__: [PythonTutor-얕은 동등성](https://pythontutor.com/visualize.html#code=class%20Fraction%3A%0A%20%20%20%20%22%22%22Fraction%20%ED%81%B4%EB%9E%98%EC%8A%A4%22%22%22%0A%0A%20%20%20%20def%20__init__%28self,%20top,%20bottom%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22%EC%83%9D%EC%84%B1%EC%9E%90%20%EB%A9%94%EC%84%9C%EB%93%9C%0A%20%20%20%20%20%20%20%20top%3A%20%EB%B6%84%EC%9E%90%0A%20%20%20%20%20%20%20%20bottom%3A%20%EB%B6%84%EB%AA%A8%0A%20%20%20%20%20%20%20%20%22%22%22%0A%20%20%20%20%20%20%20%20self.num%20%3D%20top%0A%20%20%20%20%20%20%20%20self.den%20%3D%20bottom%0A%0A%20%20%20%20def%20__str__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.num%7D/%7Bself.den%7D%22%0A%0A%20%20%20%20def%20__add__%28self,%20other_fraction%29%3A%0A%20%20%20%20%20%20%20%20new_num%20%3D%20self.num%20*%20other_fraction.den%20%2B%20%5C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.den%20*%20other_fraction.num%0A%20%20%20%20%20%20%20%20new_den%20%3D%20self.den%20*%20other_fraction.den%0A%20%20%20%20%20%20%20%20common%20%3D%20gcd%28new_num,%20new_den%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20Fraction%28new_num%20//%20common,%20new_den%20//%20common%29%0A%0Ax%20%3D%20Fraction%281,%202%29%0Ay%20%3D%20Fraction%281,%202%29%0Aprint%28x%20%3D%3D%20y%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

# 반면에 아래처럼 두 변수가 참조하는 객체를 동일(identical)하게 하면 당연히 다른 결과가 나온다.

# In[20]:


x = Fraction(1, 2)
y = x
print(x == y)
print(x is y)


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

# In[21]:


class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den +                      self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num


# 이제 동등성이 의도한대로 작동한다.

# In[22]:


x = Fraction(1, 2)
y = Fraction(1, 2)
print(x == y)


# 동일성은 동등성과 상관없이 전혀 변하지 않는다.

# In[23]:


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x == y)


# **`__dir__()` 메서드**
# 
# 객체의 모든 속성과 메서드를 확인하기 위해 아래와 같이 실행한다. 

# In[24]:


x.__dir__()


# 예를 들어, `__class__` 변수는 객체가 속하는 클래스 이름을 속성값으로 갖는다.

# In[25]:


x.__class__


# 기타 다른 메서드들은 앞으로 필요할 때마다 설명된다.

# ## 연습문제

# 참고: [(실습) 객체 지향 프로그래밍](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-oop.ipynb)
