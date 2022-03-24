#!/usr/bin/env python
# coding: utf-8

# (ch:functions)=
# # 함수

# 프로그램은 명령문의 합성으로 구현된다. 
# 그런데 특정 기능을 수행하는 명령문의 일부가 너무 길거나,
# 반복적으로 사용되어 보다 편하게 사용하고 싶거나
# 프로그램을 보다 체계적으로 구현하도록 하고 싶을 때가 있다.
# 그럴 때 특정 기능을 수행하는 명령문에 이름을 주고
# 필요에 따라 해당 이름을 대신 활용할 수 있다.
# 
# 예를 들어, `print('함수란 ...')`는 실행되면 
# `print()` 함수에 내재된
# 명령문이 작동하여 모니터 화면에 
# 문자열 `함수란 ...`을 출력한다.
# 그런데 `print()` 함수에 내재된 어떤 명령문이 정확히 무슨 일을 하는지
# 사용자는 쉽게 알지 못하고 또 굳이 알 필요도 없다. 
# 화면에 문자열을 출력하고 싶을 때 `print()` 함수를 
# 사용할 수 있다는 사실만 기억하고 있으면 된다.
# 
# 이렇게 함수는 함수의 이름에 가려진 명령문을 대행하며
# 해당 명령문을 실행하려면 지정된 함수를 
# **호출**<font size="2">call</font>하면 된다.

# ## 함수 호출

# **함수 호출**<font size="2">function call</font>은
# 함수 이름과 연관된 명령문을 실행하도록 하는 일종의 명령문이다.
# 함수 호출의 일반적인 형식은 다음과 같다. 
# 
# ```python
# 함수이름(인자1, 인자2, ..., 인자n)
# ```

# `print()` 함수를 호출하는 방식은 다음과 같다.

# In[1]:


print('함수란 ...')


# `int()` 함수는 소수점 이하를 버리는 명령문을 실행한다.

# In[2]:


int(3.14)


# `type()` 함수는 인자의 자료형을 확인하는 명령문을 실행한다.

# In[3]:


type(2.37)


# :::{admonition} 인자를 받지 않는 함수의 호출
# :class: info
# 
# 인자를 사용하지 않는 함수라 하더라도
# 함수 호출은 열고닫기 괄호를 반드시 사용해야 한다.
# 예를 들어 `dir()` 함수는 인자를 사용하지 않고 호출하면
# 현재 사용가능한 함수 또는 변수의 목록을 반환한다.
# 
# ```python
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
# ```
# 
# 반면에 괄호를 사용하지 않으면 함수 자체에 대한 정보를 확인해준다.
# 예를 들어 다음과 같이 `dir` 가 내장 함수임을 확인해준다.
# 
# ```python
# >>> dir
# <built-in function dir>
# ```
# 
# **내장 함수**<font size="2">built-in function</font>란 파이썬에서 기본으로 제공하는 함수라는 의미이다. 

# ### 함수의 인자

# 모든 함수는 호출될 때 적절한 개수의 인자를 사용해야 한다.
# 그렇지 않은 경우 오류가 발생한다. 
# 예를 들어, `type()` 함수는 1개 또는 3개의 인자와 함께 
# 호출되어야 하며, 그렇지 않은 경우 아래와 같은 
# 오류가 발생한다.
# 
# ```python
# >>> type()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: type() takes 1 or 3 arguments
# ```

# :::{admonition} 세 개의 인자를 사용하는 `type()` 함수
# :class: info
# 
# `type(2.37)`처럼 하나의 인자를 사용하면 인자의 자료형을 확인해준다.
# 반면에 세 개의 인자를 사용하는 경우는 특정 클래스의 객체를 
# 생성할 때 사용하며, 여기서는 자세히 다루지 않는다.
# :::

# ### 함수의 반환값과 `return` 키워드

# 함수를 호출하면 함수에 의해 지정된 명령문을 실행한 후에
# 최종적으로 어떤 값을 
# 반환<font size="2">return</font>하기도 한다.
# 반환값은 `return 반환값` 형식의 명령문으로 지정된다.
# 
# 예를 들어 `int(3.14)`는 정수 `3`을, 
# `type(2.37)`은 부동소수점의 자료형인 `float`를
# 함수 실행의 결괏값으로 반환하며,
# 반환된 값은 다른 연산에 재활용될 수 있다.

# In[4]:


y = int(3.14)
y + 1


# :::{admonition} 자료형과 값
# :class: info
# 
# `int`, `float` 등과 같은 자료형도 하나의 값으로 취급한다. 
# 앞으로 보겠지만, 파이썬에서 다루는 모든 **객체**<font size="2">object</font>는
# 값으로 사용될 수 있다.
# :::

# ### `print()` 함수의 반환값 `None`

# 파이썬은 모든 함수가 반환값을 갖도록 강제한다.
# `print()` 함수처럼 반환값이 없는 것처럼 보이는 함수도
# 공식적으로는 아무런 의미가 없는 값을 의미하는 `None`을
# 반환값으로 사용한다.
# 즉, 아래 명령문이 항상 마지막에 실행된다.
# 
# ```python
# return None
# ```
# 
# `None`도 하나의 값이라서 변수 할당에 사용되어 저장될 수 있다.
# 하지만 연산 등에 사용하면 오류가 발생한다.
# 즉, 아무런 기능을 수행하지 못한다. 
# 
# ```python
# >>> x = None
# >>> x + 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# ```

# 반면에 `print()` 함수에 의해 
# 화면에 출력되는 문자열은 반환값이 아니다.
# 다만 화면에 지정된 값을 출력하는 명령문의 실행 결과에 불과하다.
# 
# 함수의 반환값은 변수에 할당해서 활용할 수 있지만 
# 화면에 출력된 문자열은 그럴 수 없다는 데서 그 차이를 알 수 있다.
# 예를 들어 아래 할당 명령문을 실행할 때 화면에 보여지는 `3.14`는 
# 변수 `x`가 가리키는 값이 아니다.

# In[5]:


x = print(3.14)


# 변수 `x`는 `None`을 가리킨다.

# In[6]:


print(x)


# ## 형변환 함수

# 부동소수점 또는 정수 모양의 문자열을 정수로 변환하는 `int()` 함수는
# 하나의 자료형을 다른 자료형으로 변환된 값을 반환한다.
# 이처럼 자료형을 변환하는 것을 **형변환**<font size="2">type casting 또는 type conversion</font>라 하며
# 파이썬은 다양한 형변환 함수를 제공한다.
# `int()` 이외에 대표적으로 정수 또는 부동소수점 모양의 문자열을 부동소수점으로
# 변환하는 `float()` 함수,
# 모든 값을 문자열로 변환하는 `str()` 함수가 있다. 

# In[7]:


int(3.14)


# In[8]:


int('3')


# In[9]:


float(27)


# In[10]:


float('27.25')


# In[11]:


str(3.15)


# In[12]:


str(22)


# ## 수학 함수

# $\sin x$, $\cos x$, $\sqrt{x}$, $\log x$, $e^x$ 등
# 수학에서 많이 사용되는 함수를 파이썬에서 기본으로 제공한다. 

# ### `math` 모듈

# 파이썬에서 기본으로 제공하는 다양한 수학 함수를 사용하려면 먼저
# `math` 라는 모듈<font size="2">module</font>을 
# 불러와야<font size="2">import</font> 한다.
# 모듈은 {numref}`%s 장 <ch:module>`에서 자세히 살펴볼 것이며, 
# 여기서는 모듈이 다양한 함수를 모아 놓은 파이썬 코드 파일이라는 
# 사실 정도만 기억하면 된다.
# `math` 모듈을 불러오는 방식은 다음과 같다.

# In[13]:


import math


# :::{admonition} 자료형과 값
# :class: info
# 
# 앞서 언급했듯이 파이썬에 다루는 모든 객체는 특정 
# 자료형에 속하는 하나의 값이다.
# `math` 모듈 조차도 하나의 값이며
# `module` 자료형에 속한다.
# 
# ```python
# >>> type(math)
# <class 'module'>
# ```
# :::

# 모듈에 포함된 함수를 호출하려면 모듈과 함수를 구두점으로 구분해서 명시해야 한다.
# 예를 들어 정수 10을 밑으로 하는 상용로그 함수 $\log_{10}$에 해당하는 
# `log10()` 함수를 사용하는 방법은 다음과 같다.

# In[14]:


math.log10(10)


# In[15]:


10 ** math.log10(100)


# `math.log()`는 자연로그 함수($\ln = \log_e$)를 가리킨다.

# In[16]:


math.log(10)


# In[17]:


math.log(2.718281828459045)


# `math.sqrt()`는 제곱근 함수 $\sqrt{x}$를 가리킨다.

# In[18]:


math.sqrt(2)


# `math.exp()`는 지수 함수 $e^x$를 가리킨다.

# In[19]:


math.exp(1)


# ::::{prf:example}
# :label: degree2radian
# 
# 일반각의 각도<font size="2">degree</font>를 
# 호도법의 라디안<font size="2">radian</font>으로 
# 변환하는 공식은 다음과 같다.
# 
# $$
# \text{라디안} = \frac{\text{각도}}{180} \, \pi
# $$
# 
# 일반각 90도를 라디안으로 변환한 후에 
# 사인<font size="2">sine</font>값을 계산하는 과정은 다음과 같다.
# `math.pi`는 원주율을 가리킨다.
# 
# ```python
# >>> degree = 90
# >>> radian = degree / 180.0 * math.pi
# >>> math.sin(radian)
# 1.0
# ```

# ### NumPy 패키지

# [넘파이<font size="2">NumPy</font>](https://numpy.org)는 
# 행렬, 다차원 배열 등을 효율적으로 빠르게 
# 처리하는 많은 수학 함수를 지원하는 파이썬 라이브러리 패키지이며
# 데이터분석, 계산과학 등 컴퓨터를 이용한 계산이 필요한 영역에서 많이 활용된다.
# 파이썬의 기본 패키지에는 포함되지 않지만
# 계산과학 툴킷인 
# [아나콘다 파이썬 배포판<font size="2">Anaconda Python distribution</font>](https://www.anaconda.com)은
# 함께 지원한다.

# :::{admonition} 모듈과 패키지
# :class: info
# 
# 패키지<font size="2">package</font>는 일종의 모듈 모음집이다.
# 즉, 많이 활용되는 함수 등을 기능과 분야별로 여러 개의 모듈로 분류해서 모아놓은 것을 가리킨다.
# 패키지와 모듈은 하나의 폴더 안에 내용에 따라 여러 개의 파일로 정리하는 개념과 유사하다.
# 파일이 많아지면 폴더를 여러 개의 하위 폴더로 분류해서 파일을 분류하는 것처럼
# 패키지를 여러 개의 하위 패키지로 구분하기도 한다.
# 하위 패키지에 포함된 모듈의 활용법도 기본적으로 모듈의 함수를 사용하는 방법과 동일하다.
# 나중에 그래프를 그릴 때 필요한 패키지와 모듈을 사용해야 할 때 활용 예제를 보게 될 것이다.
# :::

# 넘파이 패키지는 앞서 언급한 `math` 모듈에서 지원하는 함수들을 포함해서 보다 많은 함수와 기능을 지원한다.
# 앞으로 필요할 때마다 하나씩 넘파이가 제공하는 기능을 활용할 것이다. 
# 넘파이를 사용하려면 먼저 `numpy` 모듈을 불러오면 된다.
# 그런데 `numpy`를 보통 `np`라는 약칭으로 아래처럼 불러온다.

# In[20]:


import numpy as np


# 모듈에 포함된 함수를 사용하는 방식은 `math.sqrt()` 처럼 구두점을 사용한다.
# 다만 약칭이 지정된 모듈은 반드시 이용해서 사용해야 한다.
# 
# `math` 모듈에 포함된 함수의 이름이 `numpy` 모듈에서 거의 동일하게 사용되었다.

# In[21]:


np.log10(10)


# In[22]:


np.log(2.72)


# In[23]:


np.sqrt(2)


# In[24]:


np.exp(1)


# In[25]:


degree = 90
radian = degree / 180.0 * np.pi
np.sin(radian)


# :::{admonition} 함수 중복 정의
# :class: info
# 
# `math`, `numpy` 두 모듈에 포함된 많은 함수가 동일한 이름을 사용한다.
# 하지만 다른 모듈의 동일한 이름의 두 함수는 서로 다른 함수이다.
# 일반 구문상 `math.exp()`와 `np.exp()` 처럼 모듈의 이름으로 구분된다.
# 
# 동일한 기능을 수해하는 함수라 하더라도 
# 각 함수의 본문에 사용된 명령문은 기본적으로 다르다.
# 실제로 `numpy` 모듈이 제공하는 수학 함수가 `math` 모듈이
# 제공하는 동일 이름의 수학 함수보다 실행속도가 빠른 경우가 많다. 
# 
# 하나의 모듈에서 동일한 이름의 두 함수를 지원하는 기능을 
# **함수 중복 정의** 또는 **함수 오버로딩**<font size="2">function overloading</font>이라 한다.
# 파이썬과 C 언어는 이 기능을 지원하지 않는 반면에 Java, C++, C# 등은 지원한다.
# :::

# ## 함수 정의하기

# 파이썬에서 사용자가 임의로 함수를 정의해서 사용할 수 있다.
# 함수를 정의하는 방식은 다음과 같다.
# 
# ```python
# def 함수이름(매개변수1, 매개변수2, ..., 매개변수n):
#     명령문
# ```
# 
# 키워드 `def` 로 시작하는 첫쨋줄은 함수의 기본 정보를 담은 **헤더**<font size="2">header</font>이고
# 나머지는 함수의 **본문**<font size="2">body</font>이다.
# 함수의 본문은 함수가 호출되었을 때 실행해야 하는 명령문을 담는다.
# 
# 문법적으로 다음 두 가지 사항에 주의해야 한다.
# 
# - 함수 이름 짓기는 변수 이름 짓기와 동일한 조건을 따라야 한다.
# - 함수 본문에 사용되는 명령문은 들여쓰며, 보통 한 번의 탭<font size="2">tab</font> 키 누르기에 
#     해당한다.

# ### 함수의 반환값

# 함수의 반환값은 본문에 사용된 명령문을 실행하다가
# 어느 순간 아래 모양의 기본 명령문을 실행하는 순간 결정된다.
# 
# 
# ```python
# return 표현식
# ```
# 
# 위 `return` 명령문이 실행되는 순간
# 지정된 `표현식`이 가리키는 값이 반환되면서 함수의 실행이 멈춘다.

# ### 매개 변수와 인자

# **매개 변수**<font size="2">parameter</font>는
# 함수 호출에 사용되는 **인자**<font size="2">argument</font>를
# 함수 본문 명령문에 전달하는 역할을 수행한다.
# 전달방식은 각 매개 변수가 지정된 인자를 가리키도록 하는 변수 할당을 통해 이루어진다.
# 
# 함수 호출이 다음과 같이 진행되었다고 가정하자.
# 
# ```python
# 함수이름(인자1, 인자2, ..., 인자n)
# ```
# 
# 그러면 함수의 본문에 포함된 명령문이 실행되기 이전에 다음 할당 명령문이 먼저 실행된다.
# 
# ```python
# 매개변수1 = 인자1
# 매개변수2 = 인자2
# ...
# 매개변수n = 인자n
# ```

# :::{prf:example}
# :label: myAdd
# 
# 두 숫자의 합을 계산하는 함수 `myAdd`를 아래와 같이 직접 정의할 수 있다.
# 더해야 할 두 개의 값을 입력받아야 하기에 두 개의 매개 변수가 필요하다.
# 
# ```python
# def myAdd(left, right):
#     sum = left + right
#     return sum
# ```
# 
# 이제 `myAdd(-2, 5)`를 실행하면 아래 명령문이 실행된다.
# 
# ```python
# left = -2
# right = 5
# sum = left + right
# ```
# 
# 결국 `sum`은 정수 `3`을 가리키게 되어 함수의 실행은 3을 
# 반환하면서 종료한다.
# 
# 함수의 반환값은 아래 코드에서처럼 다른 변수의 할당 또는 다른 함수의 인자로 사용될 수 있다.
# 
# ```python
# >>> m2p5 = myAdd(-2, 5)
# >>> print("-2와 5의 합은", m2p5, "입니다.")
# -2와 5의 합은 3 입니다.
# ```
# :::

# :::{prf:example} 인자 없는 함수
# :label: no-parameters
# 
# 아래 코드에서 정의된 `grid2()` 함수는 인자를 받지 않으며, 반환값도 없다.
# 
# ```python
# pm = "+ - - "
# ps = "|     "
# plus = "+"
# bar = "|"
# 
# def print_pm(s):
#     print(s)
# 
# def print_ps(s):
#     print(s)
#     
# def grid2():
#     for num1 in [1, 2]:
#         print_pm(pm * 2 + plus)
#         for num2 in [1, 2]:
#             print_ps(ps * 2 + bar)
# 
#     print_pm(pm*2 + plus)
# ```
# 
# `grid()` 함수를 호출하면 아래 모양의 격자가 그려진다.
# 
# ```python
# >>> grid()
# + - - + - - +
# |     |     |
# |     |     |
# + - - + - - +
# |     |     |
# |     |     |
# + - - + - - +
# ```
# :::

# ### 제1종 객체 

# 프로그래밍 언어에서 
# **제1종 객체**<font size="2">first-class object</font>는 
# 변수 할당, 함수의 인자, 함수의 반환값 등으로 사용될 수 있는
# 객체<font size="2">object</font>를 가리킨다.
# 반면에 그렇지 않은 객체는 
# **제2종 객체**<font size="2">second-class object</font>라고 
# 한다.

# :::{admonition} 제1종 객체 대 일급 객체 
# :class: tip
# 
# first-class object를 주로 ''일급 객체''로 번역되지만
# "제1종 객체"가 개념상 보다 적절하다.
# first-class와 second-class는 사용법상 구분을 나타내는 반면에
# 일급, 이급 표현은 질적 차이를 내포한다.
# :::

# 프로그래밍 언어에 따라 제1종 객체의 기준이 다르다.
# 대표적으로 C 언어의 경우 함수는 제1종 객체가 아니다.
# 즉, 함수를 다른 함수의 인자 또는 반환값으로 사용할 수 없다.
# 반면에 파이썬은 다룰 수 있는 모든 것이 제1종 객체이다. 
# 
# 함수가 하나의 값이기에 예를 들어 다음과 같이 
# `myPrint()` 함수를 변수 할당에 사용할 수 있다.
# 단, 함수를 하나의 값으로 취급할 때는 괄호를 전혀 
# 사용하지 않는다.
# 
# ```python
# >>> a_function = myPrint
# >>> a_function
# <function myPrint at 0x7f1c890a2af0>
# >>> 
# ```
# 
# 괄호을 사용하면 함수 호출을 의미하깅 아래 코드는 `myPrint()` 함수가
# 호출된 후에 반환한 `None`이 변수 할당에 사용된다.
# 
# ```python
# >>> a_return_value = myPrint()
# 인자 없어요!
# >>> a_return_value
# >>> 
# ```

# :::{admonition} C 언어의 포인터 활용
# :class: info
# 
# C 언어는 제1종 객체의 범위가 매우 제한적이다. 
# 반면에 파이썬, 
# C++, C#, 
# 자바<font size="2">Java</font>, 
# 자바스크립트<font size="2">Javascript</font>, 
# 스위프트<font size="2">Swift</font> 등
# 보다 현대적인 프로그래밍 언어는
# 이미 또는 거의 모든 객체를 제1종 객체로 지원한다.
# 
# C 언어는 포인터<font size="2">pointer</font>를 이용하여 
# 함수, 구조체 등 제1종 객체가 아닌 대상을 다루며, 
# 포인터가 C 언어에서 핵심적인 역할을 수행하는 이유가 바로 여기에 있다.
# :::

# ::::{prf:example} 함수를 인자로 받는 함수
# :label: exp:first-class-function_1
# 
# 아래 조건을 만족하도록 `do_twice()` 함수를 정의해보자.
# 
# * 두 개의 인자를 받는다.
# * 첫째 인자는 하나의 인자를 받는 함수가 사용된다.
# * 둘째 인자는 첫째 인자로 사용된 함수의 인자로 사용될 값이다. 
# * 둘째 인자로 들어온 값에 대해 두 번 연속 적용한 값을 반환한다.
# 
# 함수 `f`를 인자 `x`에 두 번 연속 적용한다는 의미는`f(f(x))`를 의미한다.
# 따라서 `do_twice()` 함수를 다음과 같이 정의할 수 있다.
# 
# ```python
# def do_twice(func, arg):
#     x = func(arg)
#     return func(x)
# ```
# 
# `three_times()` 함수는 인자의 세 배를 반환한다.
# 
# ```python
# def three_times(num):
#     return num * 3
# ```
# 
# `three_times()` 함수를 정수 `2`에 대해 연속으로 적용한 값은 18이다.
# 실제로 2의 세 배는 6, 6의 세 배는 18이다.
# 다음과 같이 확인할 수 있다.
# 
# ```python
# >>> do_twice(three_times, 2)
# 18
# ```
# 
# 위 계산은 다음과 동일하다.
# 
# ```python
# >>> three_times(three_times(2))
# 18
# ```
# 
# ::::

# ::::{prf:example} 함수를 반환하는 함수
# :label: exp:first-class-function_2
# 
# `adding_n_func(n)`를 호출하면
# `n`을 더하는 함수 `myAdd_n()`을 반환한다.
# 
# ```python
# def adding_n_func(n):
# 
#     def myAdd_n(m):
#         return n + m
#     
#     return myAdd_n
# ```
# 
# 그려면 `adding_n_func(10)`은 입력값에 10을 더한 값을 반환하는 함수를
# 반환한다.
# 
# ```python
# >>> myAdd10 = adding_n_func(10)
# >>> myAdd10(3)
# 13
# ```
# ::::

# :::{admonition} C 언어의 포인터 활용
# :class: info
# 
# C 언어는 제1종 객체의 범위가 매우 제한적이다. 
# 반면에 파이썬, 
# C++, C#, 
# 자바<font size="2">Java</font>, 
# 자바스크립트<font size="2">Javascript</font>, 
# 스위프트<font size="2">Swift</font> 등
# 보다 현대적인 프로그래밍 언어는
# 이미 또는 점점 더 거의 모든 객체를 제1종 객체로 지원한다.
# 
# C 언어는 함수, 구조체 등 제1종 객체가 아닌 객체를
# 포인터를 이용하여 다룬다. 
# 포인터가 C 언어에서 핵심적인 역할을 수행하는 이유가 여기에 있다.
# :::

# (sec:keyword-arguments)=
# ### 키워드 인자

# `print()` 함수는 여러 개의 인자를 받을 수 있다.
# 그러면 각 인자를 공백<font size="2">space</font>으로 구분하여
# 함께 한 줄에 출력한다.

# In[26]:


print('Hello,', 'Python', '!')


# 그런데 각각의 인자를 서로 다른 줄에 출력하려면 아래와 같이 해야 한다.

# In[27]:


print('Hello,', 'Python', '!', sep='\n')


# `sep='\n'`의 `sep`은 `print()` 함수의 숨겨진 매개 변수이며
# 인자를 굳이 지정하지 않으면 **키워드 인자**<font size="2">keyword argument</font>로 
# 지정된 값을 사용한다.
# 매개 변수 `sep`의 원래 키워드 인자는 한 칸 띄어쓰기를 의미하는 문자열(`' '`)이며,
# 사용된 인자들을 한 칸씩 띄어서 한 줄에 보여주도록 한다.
# 
# `print()`함수에는
# `sep` 이외에 `end`, `file`, `flush`가
# 키워드 인자를 갖는 매개 변수이다.
# 실제로 `print()` 함수의 헤더는 다음과 같다.
# 
# ```python
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# ```
# 
# - 둘째 매개 변수 자리에 위치한 말줄임표(`...`)는 
#     여러 개의 값이 인자로 사용될 수 있음을 의미한다.
# - `end='\n'` 매개 변수는 지정된 인자들을 출력한 후에 
#     기본적으로 줄바꿈을 실행하는 것을 의미한다.
#     `end=''`로 설정하면 줄바꿈을 하지 않게 된다. 
#     아래 두 경우를 비교하면 차이점을 확인할 수 있다.
# 
#     먼저 `end='\n'` 기본값을 그대로 사용하는 경우엔 굳이 언급하지 않는다.
# 
#     ```python
#     >>> print('Hello,', 'Python', '!', sep='\n')
#     Hello,
#     Python
#     !
#     >>>
#     ```
# 
#     다음은 줄바꿈을 나타내는 문자열 `'\n'` 대신 
#     아무런 문자도 포함하지 않는 빈 문자열 `''`를 `end` 매개 변수의 인자로 사용한다.
# 
#     ```python
#     >>> print('Hello,', 'Python', '!', sep='\n', end='')
#     Hello,
#     Python
#     !>>>
#     ```

# :::{admonition} `file`과 `flush` 매개 변수
# :class: info
# 
# `print()` 함수의 `file`과 `flush` 두 매개 변수는 특별한 경우에 활용되며
# 간단한 예제는 [이곳](https://velog.io/@janeljs/python-print-sep-end-file-flush)에서 확인할 수 있다.
# :::

# ::::{prf:example}
# :label: keyword_argument
# 
# 아래 코드는 `myAdd10()` 함수를 키워드 인자를 이용하여
# 정의하는 방식을 보여준다. 
# 
# ```python
# def myAdd10(left, right=10):
#     add10 = left + right
#     return add10
# ```
# 
# 둘째 인자가 생략되면 자동으로 10이 대신 사용된다.
# 
# ```python
# >>> myAdd10(5) # right=10
# 15
# ```
# 
# 둘째 인자를 별도로 지정하면 지정된 값이 사용된다.
# 
# ```python
# >>> myAdd10(5, right=20)
# 25
# ```
# ::::

# ### 함수 합성과 함수 호출 표현식

# 수학에서 $f$, $g$ 두 개의 함수를 합성해서 새로운 함수 $f\circ g$ 를 
# 다음과 같이 정의한다.
# 
# $$
# (f\circ g) (x) := f(g(x))
# $$
# 
# 동일한 방식으로 파이썬 함수를 합성하여 새로운 표현식을 정의할 수 있다.
# 다음은 곱셈, 나눗셈, 사인 함수의 합성을 활용한 표현식이다.
# 
# ```python
# math.sin(degree / 360.0 * 2 * math.pi)
# ```
# 
# `f(x1, ..., xn)` 등의 함수 호출 표현식이 가리키는 값은
# 함수 본문에 지정된 명령문이 
# 실행되는 도중에 만나는 `return 표현식` 명령문의 `표현식`이 가리키는 값이다.
# 예를 들어 아래 코드에서 변수 `x` 가 가리키는 값은 지수승 함수 `np.exp()`가
# `np.log(2)`를 인자로 사용해서 계산된 반환값을 가리킨다.

# In[28]:


x = np.exp(np.log(2))


# ### 프로그램 실행과 함수 호출

# 파이썬 프로그램의 실행은 기본적으로 
# "위에서 아래로"와 "왼쪽에서 오른쪽으로"의 두 기준으로
# 더 이상 실행할 명령문이 없을 때까지 진행된다.
# 
# 그런데 프로그램 실행 도중에 
# 함수 호출이 발생하면 함수의 실행이 종료될 때까지 이후 명령문은 대기한다. 
# 함수 호출은 프로그램 실행 도중에 발생하는 일종의 "나들이"이다. 
# 즉, 프로그램 실행 도중 잠시 일을 멈추고 다른 일을 먼저 완료하는 기능이며
# 나들이 도중에 얻어진 결과물을 이어서 활용할 수 있다.
# 
# 물론 함수 본문에서 다른 함수를 호출할 수도 있기 때문에 
# 프로그램의 실행은 무한정 복잡해질 수 있다.
# 다행히도 파이썬 해석기가 프로그램의 실행 과정을 철저하게 
# 추적하고 관리한다. 

# ## 지역 변수와 전역 변수

# 함수를 선언할 때 사용되는 매개 변수와 함수 본문에서 선언되는 변수는 
# 함수가 실행되는 동안에만 의미를 가지며, 
# 이런 의미에서 **지역 변수**<font size="2">local variable</font>라 한다.
# 반면에 함수 밖에서도 의미를 갖는 변수는 **전역 변수**<font size="2">global variable</font>이다. 
# 
# 아래 코드에서 `hour_to_min()` 함수는 시간을 분으로 변환한 값을 반환한다. 
# 매개 변수 `hour`와 함수 본문에서 선언된 `minutes` 변수는 모두 지역 변수이다.
# 반면에 `two_hour` `hour_to_min(2)`의 실행 결괏값을 가리키는 전역 변수이다. 

# In[29]:


def hour2min(hour):
    minutes = hour * 60
    return minutes

two_hour = hour2min(2)


# 위 코드의 실행 결과 `two_hour` 변수는 120을 가리킨다.

# In[30]:


print("2 시간은", two_hour, "분입니다.")


# 반면에 `minutes`와 `hour` 두 지역변수는 더 이상 존재하지 않으며
# 두 변수가 가리키는 값을 확인하려 시도하면 이름이 존재하지 않음을 의미하는
# `NameError` 오류가 발생한다. 

# ```python
# >>> print(minutes)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'minutes' is not defined
# ```

# ```python
# >>> print(hour)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'hour' is not defined
# ```

# :::{admonition} 파이썬 튜터 활용: 지역 변수의 생존 주기
# :class: info
# 
# [PythonTutor:지역 변수 전역 변수](http://pythontutor.com/visualize.html#code=def%20hour_to_min%28hour%29%3A%0A%20%20%20%20minutes%20%3D%20hour%20*%2060%0A%20%20%20%20return%20minutes%0A%0Atwo_hour%20%3D%20hour_to_min%282%29%0Aprint%28minutes%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# `hour`와 `minutes`의 생존주기, 즉, 언제 생성되고 언제 사라지는지를 시각적으로 확인할 수 있다.
# :::

# ## 콜 스택: 프레임의 생성과 사멸

# 함수가 실행되는 동안 발생하는 모든 정보는 컴퓨터 메모리 상에서
# **프레임**<font size="2">frame</font> 형식으로 관리된다.
# 프레임은 하나의 함수가 실행되는 동안 발생하는 지역 변수의 생성 및 값 할당, 
# 할당된 값 업데이트 등을 관리한다.
# 함수의 실행과 함께 생성된 프레임은 함수의 실행이 종료되면 스택에서 사라진다.
# 하지만 함수의 반환값은 지정된 변수에 할당되거나 다른 함수의 인자로 전달된다.
# 
# 다음 코드를 이용하여 함수 호출과 프레임 생성 및 사멸의 관계를 알아보자.

# In[31]:


def hour2min(hour):
    min = hour * 60
    return min

def hour2sec(hour):
    min = hour2min(hour)
    sec = 60 * min
    return sec

print("2 시간은", hour2sec(2), "초입니다.")


# 아래 그림은 `hour2sec(2)`가 실행되면 이어서 바로 `hour2min(2)`가 호출되어
# `hour`와 `min` 두 지역 변수로 구성된 프레임이 포함된 콜 스택의 상태를 보여준다.
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/stack-diagram.jpg" style="width:275px;"></div>
# 
# - 맨 위 프레임: Global frame은 전역적<font size="2">global</font>으로 
#     사용 가능한 함수 이름과 전역 변수를 관리한다.
# - 가운데 프레임: hour2sec 프레임은 `hour2sec()` 함수가 호출되면서 
#     생성된 프레임이며, 매개 변수 `hour`가 
#     지역 변수로 포함되어 있다.
# - 맨 아래 프레임: hour2min 프레임은 
#     변수 할당문 `min = hour2min(hour)`를 실행하면 먼저 
#     `hour2min()` 함수가 호출되기에 새로 생성된 프레임이다.
#     매개 변수 `hour`와 지역 변수 `min`이 포함된다.
# - hour2sec 프레임의 지역 변수 `sec`은 `hour2min(hour)` 의 반환값이 정해지면 그때 포함된다.
# 
# 위 코드의 전체 실행 과정을 
# [PythonTutor: 프레임의 생성과 사멸](https://pythontutor.com/visualize.html#code=def%20hour2min%28hour%29%3A%0A%20%20%20%20min%20%3D%20hour%20*%2060%0A%20%20%20%20return%20min%0A%0Adef%20hour2sec%28hour%29%3A%0A%20%20%20%20min%20%3D%20hour2min%28hour%29%0A%20%20%20%20sec%20%3D%2060%20*%20min%0A%20%20%20%20return%20sec%0A%0Aprint%28%222%20%EC%8B%9C%EA%B0%84%EC%9D%80%22,%20hour2sec%282%29,%20%22%EC%B4%88%EC%9E%85%EB%8B%88%EB%8B%A4.%22%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# 확인해 보면 함수 호출이 발생할 때마다 프레임이 생성되고 또 함수의 실행이 완료될 때마다
# 해당 함수의 프레임이 사멸하는 것을 확인할 수 있다.

# 프레임은 생성된 순서 역순으로 사멸한다.
# 즉, 가장 나중에 생성된 프레임이 가장 먼저,
# 가장 먼저 생성된 프레임이 가장 나중에 사멸한다. 
# 이렇게 작동하는 구조가 **스택**<font size="2">stack</font> 이기에
# 함수의 프레임으로 구성된 스택을 **콜 스택**<font size="2">call stack</font>이라 부른다.
# **스택 다이어그램**(stack diagram)은 콜 스택의 변화를 다이어그램으로 표현한다.
# 위 프로그램의 실행 과정에서의 
# 스택 다이어그램의 변화는 다음과 같다.
# 
# - 프레임 생성 순서
# 
# ```
# Global frame => hour2sec 프레임 => hour2min 프레임
# ```
# 
# - 프레임 사멸 순서
# 
# ```
# hour2min 프레임 => hour2sec 프레임 => Global frame
# ```

# ## 연습문제 

# 참고: [(실습) 함수](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-functions.ipynb)
