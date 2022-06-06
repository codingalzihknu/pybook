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
# 파이썬 실행기<font size='2'>interpreter</font>는 다음을 싱행한다.
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
# 인스턴스 변수는 해당 클래스의 영역<font size='2'>scope</font>에서만 의미를 가지며,
# 일반적으로 생성자가 실행되는 동안 선언되지만
# 클래스 내부 어디에서도 일반 전역 변수처럼 선언될 수도 있다.
# 
# 클래스의 인스턴스는 인스턴스 변수가 가리키는 값을 속성을 갖게 되며,
# 이런 의미에서 인스턴스 변수가 가리키는 값을 
# **인스턴스 속성**<font size="2">instance attribute</font>이라 부른다.
# 인스턴스 속성은 따라서 클래스의 인스턴스가 생성되어야만 의미를 갖는다.
# 
# 인스턴스 변수 이외에 `self` 를 사용하지 않는 
# **클래스 변수**<font size='2'>class variable</font> 가 선언될 수도 있지만
# 여기서는 다루지 않는다.
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

# ```python
# >>> f1 + f2
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

    def __repr__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom

        return Fraction(new_top, new_bottom)


# 이제 `Fraction`의 인스턴스는 생성자 이외에 `__repr__()` 와 `__add__()` 두 개의 메서드를 더 갖는다.

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/fraction2.png" width="80%"></div>

# 덧셈도 잘 작동한다.

# In[29]:


f14 = Fraction(1, 4)
f12 = Fraction(1, 2)

f14 + f12


# 실제로는 `__add__()` 메서드가 다음처럼 호출된다.

# In[30]:


f14.__add__(f12)


# :::{admonition} `self` 와 `other`
# 
# `f14.__add__(f12)` 이  실행되면 실제로는 `__add__()` 메서드가 다음과 같이 호출된다.
# 
# ```python
# __add__(f14, f12)
# ```
# 
# 즉, `self=f14`, `other=f12` 가 인자로 사용되며,
# 이는 `f14` 를 중심(self)으로 해서 다른 값(other)과의 연산을 실행한다는 의미이다. 
# :::

# 그런데 덧셈의 결과가 기약분수의 형태가 아니다. 
# 기약분수를 계산하려면 최대공약수(gcd)를 계산하는 알고리즘이 필요하다.

# :::{admonition} 유클리드 호젯법
# :class: info
# 
# 두 개의 정수 $m$과 $n$의 최대공약수를 가장 빠르고 효율적으로 계산하는 기법은 유클리드 호젯법이다.
# 
# - $m$을 $n$으로 나눌 수 있으면 $n$이 최대공약수이다.
# - 그렇지 않으면 $n$과 $m\,\%\, n$의 최대공약수가 원하는 최대공약수이다.
# :::

# 아래 `gcd()` 함수는 유클리드 호젯섭을 구현한다.

# In[31]:


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


# In[32]:


print(gcd(6, 14))
print(gcd(8, 20))


# `gcd()` 함수를 `__add__()` 함수의 정의에 활용하자. 

# In[33]:


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
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        new_top = self.top * other.bottom +                      self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        common = gcd(new_top, new_bottom)
        
        return Fraction(new_top // common, new_bottom // common)


# 이제 8/6 이 아니라 3/4 을 반환한다.

# In[34]:


f14 = Fraction(1, 4)
f12 = Fraction(1, 2)

f14 + f12


# **`__eq__()` 메서드**
# 
# 두 객체의 **동일성**<font size='2'>identity</font>은 두 객체가 
# 동일한 메모리 주소에 저장되었는가에 따라 결정된다.
# 반면에 메모리의 주소가 아니라 객체가 표현하는 값의 동일성 여부에 따라
# 두 값을 비교 판정하는 것은 **동등성**<font size='2'>equality</font>과 관련된다.
# 
# 예를 들어, 아래 두 객체 모두 분수 1/2 를 객체를 가리키지만 서로 독립적으로 생성되었기에
# 서로 다른 메모리에 저장되며, 따라서 두 변수 `f1`와 `f2`는 서로 다른 객체를 참조한다.
# 따라서 두 변수가 가리키는 값은 서로 동일하지 않다고 판정된다.

# In[35]:


f1 = Fraction(1, 2)
f2 = Fraction(1, 2)

print(f1 == f2)
print(f1 is f2)


# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/fraction3.png" width="80%"></div>

# 반면에 아래처럼 두 변수가 참조하는 객체를 동일(identical)하게 하면 당연히 다른 결과가 나온다.

# In[36]:


f1 = Fraction(1, 2)
f2 = f1

print(f1 == f2)
print(f1 is f2)


# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/fraction4.png" width="80%"></div>

# 반면에 **깊은 동등성**은 두 객체가 (의도된) 동일한 값을 가리키는가 여부를 결정하며, 
# 이를 위해 `__eq__` 매직 메서드를 이용한다.

# :::{admonition} 분수의 동등성
# 
# 두 분수의 동등성은 아래와 같이 정의된다.
# 
# $$\frac {a}{b} = \frac {c}{d} \Longleftrightarrow ad = bc$$
# :::

# 분수의 동등성을 구현한 `__eq__()` 메서드를 `Fraction` 클래스에 추가하자.

# In[37]:


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
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        new_top = self.top * other.bottom +                      self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        common = gcd(new_top, new_bottom)
        
        return Fraction(new_top // common, new_bottom // common)

    def __eq__(self, other):
        first_top = self.top * other.bottom
        second_top = other.top * self.bottom

        return first_top == second_top


# 이제 동등성이 의도한대로 작동한다.

# In[38]:


f1 = Fraction(1, 2)
f2 = Fraction(1, 2)

print(f1 == f2)
print(f1 is f2)


# `f1 == f2` 는 `__eq__()` 메서드를 다음과 같이 호출한다.

# In[39]:


f1.__eq__(f2)


# 보다 다양한 매직 메서드에 대해서는 연습문제를 참고한다.

# :::{admonition} `self` 와 `other`
# 
# `f14.__add__(f12)` 이  실행되면 실제로는 `__add__()` 메서드가 다음과 같이 호출된다.
# 
# ```python
# __add__(f14, f12)
# ```
# 
# 즉, `self=f14`, `other=f12` 가 인자로 사용된다.
# 하지만 `f14` 를 기준(self)으로 해서 다른 값(other)과의 연산을 실행한다는 의미를
# 강조하기 위해 관행적으로 `self` 와 `other` 를 매개변수로 사용한다.
# 
# 이런 관행은 덧셈과 동등성 비교 등 모든 이항 연산자를 정의할 때 활용된다.
# 예를 들어 `f1 == f2`, 
# 즉 `f1.__eq__(f2)`는 파이썬 실행기의 내부에서 `__eq__(f1, f2)` 로 처리된다.
# :::

# ### 일반 인스턴스 메서드

# 매직 메서드 이외에 클래스에게 다른 기능을 제공할 수 있다. 
# 인스턴스 메서드를 정의하는 방식은 매직 메서드의 경우와 동일하다.

# **분모와 분자 추출**

# `Fraction` 클래스의 객체인 분수로부터 분자와 분모를 반환하는 `numerator()` 메서드와
# `denominator()` 메서드를 구현하자.

# In[40]:


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
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        new_top = self.top * other.bottom +                      self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        common = gcd(new_top, new_bottom)
        
        return Fraction(new_top // common, new_bottom // common)

    def __eq__(self, other):
        first_top = self.top * other.bottom
        second_top = other.top * self.bottom

        return first_top == second_top
    
    def numerator(self):
        return self.top

    def denominator(self):
        return self.bottom


# In[41]:


f3 = Fraction(2, 3)


# 2/3의 분자는 2.

# In[42]:


f3.numerator()


# 2/3의 분모는 3.

# In[43]:


f3.denominator()


# **부동소수점으로의 변환**

# 분수를 부동소수점으로 변환하는 `to_float()` 메서드를 구현해보자.

# In[44]:


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
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        new_top = self.top * other.bottom +                      self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        common = gcd(new_top, new_bottom)
        
        return Fraction(new_top // common, new_bottom // common)

    def __eq__(self, other):
        first_top = self.top * other.bottom
        second_top = other.top * self.bottom

        return first_top == second_top
    
    def numerator(self):
        return self.top

    def denominator(self):
        return self.bottom
    
    def to_float(self):
        return self.numerator() / self.denominator()


# In[45]:


f3 = Fraction(2, 3)


# In[46]:


f3.to_float()


# :::{prf:example} 라이프니츠 공식
# 
# 원주율을 아래 라이프니츠 공식으로 구할 수 있다.
# 
# $$
# \begin{align*}
# \pi & = 4 \left( \frac 1 1 - \frac 1 3 + \frac 1 5 - \frac 1 7 + \frac 1 9 - \frac{1}{11} + \frac{1}{13} - \frac{1}{15} + \frac{1}{17} - \frac{1}{19} + \cdots \right) \\
# & = 4 \sum_{k=0}^{\infty} \left( \frac{1}{4k + 1} - \frac{1}{4k + 3} \right) \\
# & = \sum_{k=0}^{\infty}  \frac{8}{(4k + 1)(4k + 3)} \\
# \end{align*}
# $$
# :::

# 라이프니츠 공식을 이용하여 원주율을 임의로 정밀한 수준까지 원주율을 계산할 수 있다.

# In[47]:


def leibniz(n):
    pi_sum = Fraction(0, 1)
    for k in range(n):
        kth_item = Fraction(8, (4*k + 1) * (4*k + 3))
        pi_sum += kth_item
        
    return pi_sum.to_float()


# In[48]:


leibniz(10)


# In[49]:


leibniz(100)


# In[50]:


leibniz(1000)


# 하지만 더 이상의 계산은 매우 어렵다. 
# 예를 들어 `leibniz(10000)` 은 언제 끝날지 모른다.
# 이유는 이런 분수 형식의 계산이
# 너무 오래 걸리기 때문이다. 
# 실제로 분수 덧셈의 통분에 사용되는 시간과 메모리 사용량이 
# 매우 크다.
# 
# 반면에 지난 수 십년동안 부동소수점 연산의 정확도와 속도를 최적하는 노력의 결과로
# 부동소수점을 사용하는 연산은 매우 빠르고 보다 많은 반복무의 실행을 지원한다.

# In[51]:


def leibniz_float(n):
    pi_sum = 0
    for k in range(n):
        kth_item = 8/((4*k + 1) * (4*k + 3))
        pi_sum += kth_item
        
    return pi_sum


# In[52]:


leibniz_float(10000)


# In[53]:


leibniz_float(1000000)


# ## 연습문제

# 참고: [(실습) 클래스, 인스턴스, 객체](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-classes_instances_objects.ipynb)
