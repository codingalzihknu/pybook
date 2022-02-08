#!/usr/bin/env python
# coding: utf-8

# # 함수

# 프로그램은 명령문의 합성으로 구현된다. 
# 그런데 특정 기능을 수행하는 명령문의 일부가 너무 길거나,
# 반복적으로 사용되어 보다 편하게 사용하고 싶거나
# 프로그램을 보다 체계적으로 구현하도록 하고 싶을 때가 있다.
# 그럴 때 특정 기능을 수행하는 명령문에 이름을 주고
# 필요에 따라 해당 이름을 대신 활용할 수 있다.
# 
# 예를 들어 `print('함수란 ...')`는 실행되면 
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

# ### `print()` 함수와 `None` 값

# 파이썬은 모든 함수가 반환값을 갖도록 강제한다.
# `print()` 함수처럼 반환값이 없는 것처럼 보이는 함수도
# 공식적으로는 아무런 의미가 없는 값을 의미하는 `None`을
# 반환값으로 사용한다.
# 
# `None`은 `NoneType` 자료형에 속하는 하나의 값이다.
# 따라서 변수 할당에 사용되어 저장될 수 있다.
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

# `print()` 함수에 의해 
# 화면에 출력되는 문자열은 반환값이 아니고
# 화면에 지정된 값을 출력하는 명령문의 실행 결과에 불과하다.
# 함수의 반환값은 변수에 할당해서 활용할 수 있지만 
# 화면에 출력된 문자열은 그럴 수 없다는 데서 `print()` 함수의 반환값이
# 없다는 것을 확인할 수 있다.
# 
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
# 이처럼 자료형을 변환하는 것을 **형변환**<font size="2">type casting</font>라 하며
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
# 파이썬의 기본 패키지에는 없지만
# [아나콘다<font size="2">Anaconda</font>](https://www.anaconda.com)에는
# 포함되어 있다.

# :::{admonition} 모듈과 패키지
# :class: info
# 
# 패키지<font size="2">package</font>는 일종의 모듈 모음집이다.
# 즉, 많이 활용되는 함수 등을 기능과 분야별로 여러 개의 모듈로 분류해서 모아놓은 것을 가리킨다.
# 모듈과 패키지를 파일과 폴더에 비유할 수 있다. 
# 하나의 폴더 안에 내용에 따라 여러 개의 파일로 정리하는 것과 유사하다.
# 파일이 많아지면 폴더를 여러 개의 하위 폴더로 분류해서 파일을 분류하는 것처럼
# 패키지를 여러 개의 하위 패키지로 구분하기도 한다.
# 하위 패키지에 포함된 모듈의 활용법도 기본적으로 모듈의 함수를 사용하는 방법과 동일하다.
# 나중에 그래프를 그릴 때 필요한 패키지와 모듈을 사용해야 할 때 활용 예제를 보게 될 것이다.
# :::

# 넘파이 패키지는 앞서 언급한 `math` 모듈에서 지원하는 함수들을 포함해서 보다 많은 함수와 기능을 지원한다.
# 앞으로 필요할 때마다 하나씩 넘파이 모듈의 기능을 활용할 것이다. 
# 넘파이를 사용하려면 먼저 `numpy` 모듈을 불러오면 된다.
# 그런데 `numpy`를 보통 `np`라는 약칭으로 
# 아래처럼 불러온다.

# In[20]:


import numpy as np


# 모듈에 포함된 함수를 사용하는 방식은 `math.sqrt()` 처럼 구두점을 사용한다.
# 다만 모듈 이름대신 지정한 약칭을 사용해야 한다.
# `numpy` 모듈에 포함된 수학 함수의 이름은 `math` 모듈의 경우와 기본적으로 동일하다.

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


# :::{admonition} 동일 이름의 두 함수
# :class: warning
# 
# `math`, `numpy` 두 모듈에 포함된 많은 함수가 동일한 이름을 사용한다.
# 하지만 함수의 이름이 갖다고 해서 동일한 함수는 아니다.
# 서로 다른 모듈에 속하는 동일 이름의 함수는
# 비록 반환값이 같을 수는 있어도 반환값 계산에 사용된 명령문은
# 기본적으로 다르다. 
# 실제로 `numpy` 모듈이 제공하는 수학 함수가 `math` 모듈이
# 제공하는 동일 이름의 수학 함수보다 실행속도가 빠른 경우가 많다. 
# :::

# ## 함수 합성과 표현식

# 수학에서 $f, g$ 두 개의 함수를 합성해서 새로운 함수 $f\circ g$를 정의해서 사용한다.
# 
# $$
# (f\circ g) (x) := f(g(x))
# $$
# 
# 동일한 방식을 파이썬에서 지원한다.
# 아래 코드는 곱셈, 나눗셈, 사인 함수의 합성을 활용한다.

# In[26]:


x = math.sin(degree / 360.0 * 2 * math.pi)
print(x)


# 표현식은 함수와 변수, 정수, 유리수, 문자열 등을 조합하여
# 하나의 값(value)을 표현하도록 작성된 식이라고 
# {numref}`%s 절 <sec:representation>`에서 언급했다.
# 표현식 `f(x1, ..., xn)`은 또한 함수 호출을 의미하며 지정된 명령문을 실행한다.
# 실행 도중 `return 표현식`이 실행되면
# `표현식`이 가리키는 값을 계산하여 반환한다. 
# 
# 아래 코드에서 변수 `x`가 가리키는 값은 지수승 함수 `np.exp()`가
# `np.log(2)`를 인자로 사용했을 때의 반환값을 가리킨다.

# In[27]:


x = np.exp(np.log(x+1))
print(x)


# ## 함수 정의하기

# 파이썬에서 함수를 임의로 정의해서 사용할 수 있다.
# 함수를 정의하는 방식은 기본적으로 다음과 같다.
# 
# ```python
# def 함수이름(매개변수1, 매개변수2, ..., 매개변수n):
#     명령문
# ```
# 
# `def` 키워드로 시작하는 첫쨋줄은 함수의 기본 정보를 담은 **헤더**<font size="2">header</font>이고
# 나머지는 함수의 본문<font size="2">body</font>이다.
# 함수의 본문은 함수가 호출되었을 때 실행해야 하는 명령문을 담는다.
# 
# 문법적으로 다음 두 가지 사항에 주의해야 한다.
# 
# - 함수의 이름은 변수의 이름을 짓는 경우와 동일한 조건을 따라야 한다.
# - 함수 본체에 사용되는 명령문은 들여쓰며, 보통 탭<font size="2">tab</font> 키 한 번 누르는 것에 
#     해당한다.

# ### 함수의 반환값

# 함수의 반환값은 본문에 사용된 명령문을 실행하다가
# 어느 순간 `return 표현식` 모양의 기본 명령문을 실행하는 순간 결정된다.
# 함수는 그순간 지정된 `표현식`이 가리키는 값을 반환하면서 실행을 멈춘다.
# 
# `return 표현식`이 실행되지 않은 채 함수의 실행이 멈추면 
# 그 함수의 반환값은 `print()` 함수의 경우처럼 `None`으로 자동 지정된다.
# 단, 오류로 인해 실행이 멈추는 경우엔 반환값이 전혀 지정되지 않는다.

# ### 매개변수와 인자

# **매개변수**<font size="2">parameter</font>는
# 함수 호출에 사용되는 **인자**<font size="2">argument</font>를
# 함수 본체 명령문에 전달하는 역할을 수행한다.
# 전달방식은 각 매개변수가 지정된 인자를 가리키도록 하는 변수 할당을 통해 이루어진다.
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

# ::::{prf:example} 인자를 받지 않는 함수
# :label: no_parameter
# 
# 매개변수를 사용하지 않는 함수라 하더라도
# 함수호출은 괄호를 반드시 사용해야 한다.
# 
# 예를 들어 아래 함수는 인자 없이 호출해야 한다.
# 
# ```python
# >>> def myPrint():
# ...     print("인자 없어요!")
# ...
# >>> myPrint()
# 인자 없어요!
# ```

# ::::{prf:example}
# :label: myAdd
# 
# 두 숫자의 합을 계산하는 함수 `myAdd`를 아래와 같이 직접 정의할 수 있다.
# 더해야 할 두 개의 값을 입력받아야 하기에 두 개의 매개변수가 필요하다.
# 
# ```python
# def myAdd(left, right):
#     z = left + right
#     return z
# ```
# 
# 이제 `myAdd(-2, 5)`를 실행하면 아래 명령문이 실행된다.
# 
# ```python
# left = -2
# right = 5
# z = left + right
# ```
# 
# 결국 `z`는 정수 `3`을 가리키게 되어 함수의 실행은 3을 반환<font size="2">return</font>하면서 종료한다.
# ::::

# ### 키워드 인자

# `print` 함수를 이용하여 화면에 출력할 때 여러 개의 인자를 사용하면
# 각 인자를 공백<font size="2">space</font>로 구분하여 함께 한 줄에 출력한다.

# In[28]:


print('Hello,', 'Python', '!')


# 그런데 각각의 인자를 서로 다른 줄에 출력하려면 아래와 같이 해야 한다.

# In[29]:


print('Hello,', 'Python', '!', sep='\n')


# 위에서 사용된 `sep`은 `print()` 함수의 숨겨진 매개변수이며
# 인자를 굳이 지정하지 않으면 **키워드 인자**<font size="2">keyword argument</font>로 
# 지정된 값을 사용한다.
# `sep`의 키워드 인자는 한 칸 띄어쓰기를 의미하는 문자열 `' '`이며,
# 사용된 인자들을 한 칸씩 띄어서 한 줄에 보여준다.
# 그런데 `sep`에 대한 인자를 줄바꿈을 의미하는 문자열 `'\n'`를 사용하여
# 하나의 인자를 출력할 때마다 줄바꿈을 실행하도록 하였다.

# 이렇듯 경우에 따라 키워드 인자를 사용하는 매개변수를 
# 함수 정의에 사용할 수 있다.
# `print()`함수는
# `sep` 이외에 `end`, `file`, `flush` 가
# 키워드 인자를 갖는 매개변수이다.
# 실제로 `print()` 함수의 헤더는 다음과 같다.
# 
# ```python
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# ```
# 
# - 둘째 매개변수 자리에 위치한 `...`은 화면에 출력할 여러 개의 값이 사용될 수 있음을 의미한다.
# - `end='\n'` 매개변수는 지정된 인자들을 출력한 후에 기본적으로 줄바꿈을 실행하는 것을 의미한다.
# - `file`과 `flush`는 거의 사용할 일이 없다.

# ::::{prf:example}
# :label: keyword_argument
# 
# 아래 함수는 `myAdd()` 처럼 두 개의 숫자를 입력받아 합을 구한다.
# 다만 둘째 매개변수가 10을 키워드 인자로 사용한다.
# 
# ```python
# def myAdd10(left, right=10):
#     add10 = left + right
#     return add10
# ```
# 
# 따라서 둘째 인자를 반드시 입력하지 않아도 되며,
# 그럴 경우 둘째 인자는 10으로 지정된다.
# 
# ```python
# >>> myAdd10(5)
# 15
# ```
# 
# 그리고 둘째 인자를 따로 지정하면 지정된 값이 사용된다.
# 
# ```python
# >>> myAdd10(5, right=20)
# 25
# ```
# ::::

# ## 함수호출

# ### 함수호출 실행과정

# 함수호출 과정을 좀 더 자세히 살펴보자.
# 예를 들어, 아래 함수 표현식이 가리키는 값이 어떤 순서대로 계산되는가를 확인하고 한다.
# 
# ```python
# mul(add(2, mul(0x4, 0x6)), add(0x3, 0o5))
# ```
# 
# * `add` 함수와 `mul` 함수는 각각 두 숫자의 합과 곱을 계산하는 함수이며, 
#     `operator` 모듈에 포함되어 있다.
# * `0x`로 시작하는 숫자는 16진법을 의미한다.
# * `0o`로 시작하는 숫자는 8진법을 의미한다.

# In[30]:


from operator import add, mul

mul(add(2, mul(0x4, 0x6)), add(0x3, 0o5))


# 최종적으로 208이 계산되는 과정을 그림으로 나타내면 다음과 같다.
# 아래 그림에서 &#9312; ~ &#9319;번 사이의 번호가 배정된 네모상자로 둘러싸인 부분이 
# 현재 실행중인 함수호출 또는 함수호출의 결과값을 나타낸다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/fun_call.png" style="width:600px;"></div>

# ### 예제

# [PythonTutor: 함수호출 실행과정](http://pythontutor.com/visualize.html#code=def%20myAdd%28left,%20right%29%3A%0A%20%20%20%20return%20left%2Bright%0A%20%20%20%20%0Adef%20myMul%28left,%20right%29%3A%0A%20%20%20%20return%20left*right%0A%0AmyMul%28myAdd%282,%20myMul%280x4,%200x6%29%29,%20myAdd%280x3,%200o5%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# 앞서 사용한 표현식과 동일하게 작동하는 표현식이 계산되는 과정을 살펴볼 수 있다.
# 
# **주의:** `add`, `mul`과 같이 파이썬에서 이미 정의된 내장함수들의 계산과정은 시각화해서 보여지지 않는다.
# 그래서 동일하게 작동하는 `myAdd`와 `myMul`을 새로 정의하였다.
# 함수의 이름만 다를 뿐 동일한 표현식이다.

# ## 지역변수와 전역변수

# 함수를 선언할 때 사용되는 매개변수와 함수 본체에서 선언되는 변수는 함수가 실행되는 동안에만 의미를 갖는 변수들이며,
# 이런 변수들을 **지역변수**라 부른다. 
# 지역변수 가인 변수들은 **전역변수**라 부른다.
# 
# 예를 들어, `hour_to_min` 함수를 정의할 때 사용된 
# `hour`와 본체에서 선언된 `minutes` 변수는 모두 지역함수이며,
# `two_hour` 는 함수 밖에서 선언된 전역변수이다.

# In[31]:


def hour_to_min(hour):
    minutes = hour * 60
    return minutes


# 지역변수들은 함수 밖에서는 어떤 의미도 갖지 않는다. 예를 들어, 아래 코드를 실행하면 오류가 발생한다.

# In[32]:


two_hour = hour_to_min(2)
print(minutes)


# 물론 아래의 경우도 오류가 발생한다.

# In[32]:


two_hour = hour_to_min(2)
print(hour)


# 위에서 오류가 발생하는 이유는 `hour_to_min` 함수가 인자 2와 함께 실행되어 종료가 되면 
# 실행도중에 선언되어 사용된 `hour`와 `minutes` 변수의 의미도 완전히 사라지기 때문이다.
# 
# **참고:**
# [PythonTutor:지역변수 전역변수](http://pythontutor.com/visualize.html#code=def%20hour_to_min%28hour%29%3A%0A%20%20%20%20minutes%20%3D%20hour%20*%2060%0A%20%20%20%20return%20minutes%0A%0Atwo_hour%20%3D%20hour_to_min%282%29%0Aprint%28minutes%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# `hour`와 `minutes`의 생존주기, 즉, 언제 생성되고 언제 사라지는지를 확인할 수 있다.

# ## 재귀함수

# 봉 감독의 영화(Movies by Bong, moBong)를 담고 있는 리스트가 아래와 같이 있다.

# In[33]:


moBong = ["기생충", 2019, ["설국열차", 2013, ["살인의 추억", 2003]]]


# 위 리스트는 3중이다. 리스트 안에 리스트, 또 리스트 안에 리스트.
# 이제 아래와 같이 모든 항목을 나열하고자 한다.
# 
# ```
# 기생충
# 2019
# 설국열차
# 2013
# 살인의 추억
# 2003
# ```
# 
# 먼저, 위 리스트의 항목들을 하나씩 확인하려면 아래와 같이 `for` 반복문을 활용해보자.

# In[34]:


for item in moBong:
    print(item)


# 그런데 위와 같이 하면 중첩으로 되어 있는 영화들을 제대로 풀어헤칠 수 없다.
# 2중 `for` 반복문을 활용해보자.
# 
# **주의:** 아래 코드에서 `isinstance(item, list)`는 `item` 변수가 가리키는 항목이 
# 리스트 자료형 여부를 확인한다.

# In[35]:


for item in moBong:
    if isinstance(item, list):
        for itemN in item:
            print(itemN)
    else:
        print(item)


# 여전히 삼중 리스트의 모든 항목을 나열하진 못한다. 
# 3중 `for` 반복문을 활용해보자.

# In[36]:


for item in moBong:
    if isinstance(item, list):
        for itemN in item:
            if isinstance(itemN, list):
                for itemNN in itemN:
                    print(itemNN)
            else:
                print(itemN)
    else:
        print(item)


# 그런데 프로그램을 이렇게 구현하면 안된다.
# 만약에 영화목록이 4중, 5중으로 구성된 리스트로 작성되었다면
# 위 프로그램은 4중, 5중 `for` 반복문으로 수정해야 하고,
# 그러면서 프로그램의 길이와 복잡도가 기하급수적으로 증가하기 때문이다.
# 
# 처리해야 하는 데이터에 따라 프로그램이 수정되거나 복잡도가 증가하지 않는 
# 프로그램을 구현해야 한다. 
# 
# 다시 한 번 위 세 개의 프로그램을 살펴보자. 
# 세 개의 프로그램은 사실상 아래 명령문을 반복해서 사용한다. 
# 
# ```python
# for 항목 in 리스트:
#     if isinstance(항목, list):
#         명령문
#     else:
#         print(항목)
# ```
# 
# 위 명령문은 리스트의 항목이 또 다른 리스트이면 그 리스트의 항목들을 
# 대상으로 동일한 확인작업을 수행하며,
# 더 이상 리스트가 다른 리스트의 항목으로 포함되지 않을 때 까지 반복된다.
# 즉, 모든 중첩 리스트가 해체될 까지 리스트 여부를 반복하며, 
# 리스트가 아니면 해당 항목을 화면에 출력한다.
# 
# 이런 반복작업을 **재귀**(recursion)라 부르며,
# 반복되는 작업에 이름을 주면, 위 세 개의 코드를 하나의 함수로 정의할 수 있다.
# 예를 들어, 아래와 같이 앞서 언급된 명령문에 `printItems`이란 이름을 주어 함수로 정의해보자.

# In[37]:


def printItems(aList):
    for item in aList:
        if isinstance(item, list):
            printItems(item)
        else:
            print(item)


# `printItems` 함수는 좀 이상하다. 
# 정의가 끝나지 않았는데 자신을 자신 본체에서 사용한다. 
# (4번 줄 참조)
# 
# 실제로 `printItems` 함수를 호출하면 실행과정 중에
# 자신을 또다시 호출한다. 
# 단, 사용되는 인자가 다르며, 애초에 사용된 리스트의 항목이면서
# 또다른 리스트가 인자로 사용된다.
# 이런 함수를 자기 자신을 호출한다는 의미로 **재귀함수**(recursive function)라 부른다. 
# 
# 사실 임의로 중첩된 리스트를 인자로 받아도 중첩을 모두 풀어버린다.

# In[38]:


printItems(moBong)


# ### 예제: 콜라츠 추측

# 독일 수학자인 콜라츠(Collatz, L.)가 1937년에 아래 알고리즘을
# 얼마나 많이 반복하면 최종적으로 숫자 1에 다다를 것인가를 질문했다.
# 
# * 주어진 숫자가 짝수면 2로 나눈다.
# * 주어진 숫자가 홀수면 3배한 후 1을 더한다.
# 
# 실제로 숫자 7부터 시작해서 위 과정을 16번 반복하면 1에 다다른다. 
# 
#     7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
#     
# 반면에 숫자 128부터 시작하면 7번만 반복하면 된다.
# 
#     128, 64, 32, 16, 8, 4, 2, 1
#     
# 즉, 처음 시작하는 값이 작다고 해서 반드시 먼저 끝나는 것이 아니다.
# 또한 무지 오랫동안 반복해야 하는 경우도 있다.
# 예를 들어, 129로 시작하면 무려 122번 반복해야 한다.
# 
# 아래 그림은 10,000까지의 숫자들과 관련된 반복회수를 보여준다.
# 그림에서 알 수 있듯이 반복회수와 관련된 수학적 특징을 확인하기 어렵다.
# 실제로 콜라츠의 질문에 대한 답이 여전히 알려지지 않았다.
# 반면에 무한 반복되는 경우도 알려지지 않았다.
# 
# 콜라츠는 어떤 숫자로 시작하든지 반복잡업이 언젠가는 끝난다고 추측하였지만,
# 언제 끝나는가는 수학적으로 알아내지 못했으며, 여전히 미해결 문제로 남아 있다.

# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Collatz-stopping-time.svg/440px-Collatz-stopping-time.svg.png" style="width:400px;"></div>
# 
# <그림출처: [위키백과](https://en.wikipedia.org/wiki/Collatz_conjecture)>

# 콜라츠의 질문에 답하는 함수를 아래와 같이 `while` 반복문을 이용하여 구현할 수 있다.

# In[39]:


def collatzWhile(num):
    count = 0
    while (num != 1):
        if num%2 == 0:
            num = num//2
        else:
            num = num*3+1
        count = count+1
    return count


# In[40]:


collatzWhile(7)


# In[41]:


collatzWhile(128)


# In[42]:


collatzWhile(129)


# 반면에 재귀를 이용할 경우 아래와 같이 구현한다.

# In[43]:


def collatz_(num):
    if num == 1:
        return 0
    elif num%2 == 0:
        return collatz_(num//2) + 1
    else:
        return collatz_(num*3 + 1) + 1


# In[44]:


collatz_(7)


# In[45]:


collatz_(128)


# In[46]:


collatz_(129)


# 반복되는 과정을 보고 싶으면 반복될 때마다 숫자를 출력하면 된다.

# In[47]:


def collatzWhile_(num):
    count = 0
    while (num != 1):
        if num%2 == 0:
            print(num, end=', ')
            num = num//2
        else:
            print(num, end=', ')
            num = num*3+1
        count = count+1
    return count


# In[48]:


collatzWhile_(7)


# In[49]:


collatzWhile_(128)


# In[50]:


collatzWhile_(129)


# In[51]:


def collatz(num):
    if num == 1:
        print(num)
        return 0
    elif num%2 == 0:
        print(num, end=', ')
        return collatz(num//2) + 1
    else:
        print(num, end=', ')
        return collatz(num*3 + 1) + 1


# In[52]:


collatz(7)


# In[53]:


collatz(128)


# In[54]:


collatz(129)


# ## 함수호출과 스택 다이어그램

# 함수를 호출하여 실행을 하면 컴퓨터 메모리의 스택(stack) 영역에 함수의 호출과 실행과정, 
# 그리고 실행 결과값과 관련된 정보의 변화가 일어난다. 
# 이런 정보의 변화를 **프레임**(frame)으로 다루며, 
# 프레임은 모든 함수와 변수의 생성, 호출, 삭제 과정을 기록한다.
# 
# 또한 하나의 함수가 호출될 때마다 하나의 프레임이 임시로 생성되었다가 함수의 실행이 종료되면 해당 함수의
# 반환값을 다른 프레임에 넘겨 준 후에 사라지는 과정이 반복된다. 이렇게 특정 함수호출과 관련된 프레임을 **지역 프레임**이라 
# 부른다.
# 반면에 프로그램이 실생되는 전 과정동안 살아 있는 프레임을 **전역 프레임**이라 부른다. 
# 
# 예를 들어, 앞서 지역변수와 전역변수를 설명하면서 사용한 코드를 
# [PythonTutor:지역변수 전역변수](http://pythontutor.com/visualize.html#code=def%20hour_to_min%28hour%29%3A%0A%20%20%20%20minutes%20%3D%20hour%20*%2060%0A%20%20%20%20return%20minutes%0A%0Atwo_hour%20%3D%20hour_to_min%282%29%0Aprint%28minutes%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서 
# 실행하면서 프레임의 변화를 살펴볼 수 있다. 
# 
# 위 프로그램을 한 단계씩 실행할 때 아래 사항들에 생각하면서 메모리 상태의 변화를 살펴보아야 한다. 
# 
# * 전역변수와 함수들은 전역 프레임(global frame)에서 다룬다.
# * 지역변수들은 함수가 호출되면 생성되어 지역변수들의 정보를 다루다가, 함수의 실행이 종료되면 
#     모든 정보와 함께 사라진다. 
#     예를 들어, 마지막 그림에서 `minutes` 값을 확인하고자 할 때 오류가 발생하는 이유가 
#     `hour_to_min` 함수가 호출될 때 생성된 지역 프레임이 함수의 실행이 종료되면 사라지기 때문이라는 
#     점을 눈으로 확인할 수 있다.
# 
# 반면에 재귀함수의 실행과정 동안 많은 프레임의 생성과 소멸이 발생한다.
# 그리고 이런 프레임들의 변화가 스택(stack) 형식으로 이루어지는데,
# 따라서 그와 같은 프레임들의 변화를 **스택 다이어그램**(stack diagram)이라 부른다.
# 
# 에를 들어,
# [PythonTutor: 콜라츠 추측](http://pythontutor.com/visualize.html#code=def%20collatz%28num%29%3A%0A%20%20%20%20if%20num%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20print%28num%29%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20elif%20num%252%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28num,%20end%3D',%20'%29%0A%20%20%20%20%20%20%20%20return%20collatz%28num//2%29%20%2B%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28num,%20end%3D',%20'%29%0A%20%20%20%20%20%20%20%20return%20collatz%28num*3%20%2B%201%29%20%2B%201%0A%20%20%20%20%20%20%20%20%0Acollatz%287%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# 재귀함수 호출 과정 동안 메모리에서 벌어지는 프레임의 생성과 소멸 과정,
# 즉, 스택 다이어그램의 변화를 살펴볼 수 있다.

# ## 동적 타이핑 vs. 정적 타이핑

# 함수는 임의의 값을 인자로 받는다. 
# 하지만 함수마다 다룰 수 있는 값들의 자료형이 존재하며,
# 다룰 수 없는 자료형의 값이 인자로 사용되면 오류가 발생한다.
# 
# 예를 들어, `type` 함수는 모든 자료형의 값을 다룰 수 있지만,
# `abs` 함수는 정수와 실수는 다루지만, 문자열을 
# 인자로 사용하면 오류가 발생한다. 

# In[55]:


abs('-3.3')


# 이렇듯, 파이썬 함수는 임의의 값에 적용될 수 있지만,
# 인자의 자료형을 파이썬 해석기가 파악해서 적용가능 여부를 판단한다.
# 이런 기능을 **동적 타이핑**이라 부른다.
# 즉, 처음부터 인자의 자료형을 지정하거나 확인하는 게 아니라
# 프로그램을 실행하는 도중에 사용되는 함수 인자들의 자료형을 확인한다는 의미이다.
# 이는 함수가 다루는 모든 값에 대해 동일하다. 

# ### 파이썬과 정적 타이핑

# C, Java 등 많은 프로그래밍 언어는 동적 타이핑 대신에 **정적 타이핑**(static typing)을 지원한다.
# 즉, 함수나 변수를 선언할 때 사용되는 변수들의 자료형과 인자 및 반환값의 자료형을 
# 애초부터 명시해야 하며 지정된 자료형이 사용되지 않을 경우 오류를 발생시킨다.
# 
# 파이썬은 3.6 버전부터 정적 타이핑 형식을 지원한다. 
# 다만 C, Java의 자료형과 관련된 엄격함은 전혀 존재하지 않으며, 
# 그냥 정적 타이핑의 형식만 빌려왔다.
# 
# 즉, **자료형 명시**(type annotations)를 지원할 뿐이며, 
# 실제로는 동적 타이핑 형식으로 문법과 실행 과정을 확인하고 제어한다.
# 
# 예를 들어, `myAdd` 함수를 아래와 같이 선언할 수 있다.

# In[56]:


def myAdd(a: float, b: float) -> float:
    return a + b


# `myAdd` 함수는 부동소수점의 합을 계산함수라는 의도를 
# 명확히 하기 위해 `float`라는 자료형을 입력값와 반환값에 대해 명시하였다.
# 
# 그래서 위 함수는 마치 부동소수점에 대해서만 작동하는 것처럼 보인다.
# 하지만 이는 `myAdd` 함수는 여전히 다른 자료형의 값들을 
# 인자로 사용할 수 있다.

# In[57]:


print(myAdd(10, 5))
print(myAdd([1, 2], [3]))
print(myAdd("저 ", "잠깐만요!"))


# 즉, 자료형의 명시는 함수 정의의 의도를 전달하는 역할만 수행하며,
# 파이썬이 정적타이피을 지원한다는 의미는 아님에 주의해야 한다.

# ### 고계 함수와 제1종 객체

# 파이썬에서는 함수도 하나의 값으로 간주된다.
# 이렇게 하나의 값으로 간주되는 객체를
# **제1종 객체**(first-class object)라고 부른다.
# 제1종 객체로 간주되는 값은 변수에 할당되거나, 함수의 인자 또는 반환값으로 사용될 수 있다.
# 
# 함수를 인자로 받거나 내주는 값으로 사용하는 함수를 **고계 함수**(higher-order function)라 부른다.

# ## 연습문제 

# 1. 다음 조건을 만족시키는 `right_justify`라는 함수를 정의하라.
#     * 인자는 하나만 받으며, 매개변수는 `s`라 부른다.
#     * 문자열 하나를 인자로 받아 실행하면 해당 문자열의 끝이 70번째 칸에 위치하도록 
#         입력받은 문자열 앞에 충분한 공백이 위치하도록 출력(print)한다. 
# ```python
# >>> right_justify('monty')
#                                                                 monty
# ```                                                                 
#     힌트: 문자열 결합 및 반복, 그리고 문자열의 길이를 되돌려주는 내장함수 `len` 활용 가능.
# <br><br>
# 1. 파이썬은 정의된 함수도 하나의 값으로 취급한다. 
#     따라서 함수를 다른 함수의 인자로 사용하거나 변수에 할당되는 값으로 사용될 수 있다. 
#     예를 들어, 아래에 정의된 `do_twice` 함수는 함수 `f`를 인자로 입력받으면
#     그 함수를 두 번 호출하여 실행하도록 하는 함수이다. 
# ```python
# def do_twice(f):
#     f()
#     f()
# ```
#     그리고 `print_spam` 이라는 함수를 두 번 호출하도록 `do_twice`를 활용하고자 하면 
#     아래와 같이 프로그램을 작성하면 된다.
#     ```python
#     def print_spam():
#         print('spam')
# 
#     do_twice(print_spam)
#     ```
#     1. 이 프로그램을 직접 입력해서 실행해 보라.
#     1. 아래 조건을 만족하도록 `do_twice` 함수를 수정하라. 
#         * 두 개의 인자를 사용한다.
#         * 첫째 매개변수는 하나의 인자를 받는 함수를 인자로 입력받는다.
#         * 둘째 매개변수는 첫째 인자에 사용된 함수의 인자로 사용될 수 있는 값을 인자로 입력받는다.
#         * 첫째 인자로 사용된 함수를 둘째 인자로 사용된 값을 이용하여 두 번 연속 호출한다. 
#     1. 아래 조건을 만족하도록 `do_four` 함수를 수정하라. 
#         * 두 개의 인자를 사용한다.
#         * 첫째 매개변수는 하나의 인자를 받는 함수를 인자로 입력받는다.
#         * 둘째 매개변수는 첫째 인자에 사용된 함수의 인자로 사용될 수 있는 값을 인자로 입력받는다.
#         * 첫째 인자로 사용된 함수를 둘째 인자로 사용된 값을 이용하여 네 번 연속 호출한다. 
#         * 앞서 정의된 `do_twice` 함수를 반드시 활용한다.
# <br><br>
# 답: http://greenteapress.com/thinkpython2/code/do_four.py
# <br><br>
# 1. 이번 문제는 지금까지 배운 내용을로 풀 수 있다. 
#     1. 다음과 같은 격자를 그리는 함수를 작성하라.
#         ```
#         + - - - - + - - - - +
#         |         |         |
#         |         |         |
#         |         |         |
#         |         |         |
#         + - - - - + - - - - +
#         |         |         |
#         |         |         |
#         |         |         |
#         |         |         |
#         + - - - - + - - - - +
#         ```
#         힌트: 한 줄에 하나 이상의 값을 출력하려면 `print` 함수에 여러 인자를 사용하면 된다.
#         ```python
#         print('+', '-')
#         ```
#         `print` 함수는 기본적으로 줄바꿈을 실행한다.
#         줄바꿈을 하지 않기 위해서는 에를 들어 아래와 같이 실행하면 된다.
#         ```
#         print('+', end=' ')
#         print('-')
#         ```
#         위 프로그램을 실행하면 `+ -` 형식으로 출력된다. 
#         <br><br>
#     1. 4개의 행과 4개의 열을 갖는 격자를 그리는 함수를 작성하라.
# 
#     답: http://greenteapress.com/thinkpython2/code/grid.py
#     <br><br>
#     이 연습문제는 아래 책의 Oualline에 포함된 연습문제를 응용하였다. 
#     
#             Practical C Programming, Third Edition, O’Reilly Media, 1997.
# 
#     1. 위 함수를 일반화 하라. 즉, 입력값 n이 주어지면
#         n개의 행과 n개의 열을 갖는 격자를 그리는 함수를 작성하라.
#         <br><br>
# 
# 1. `printItems` 수정하여 `moBong`에 포함된 항목들을 아래와 같이 
#     출력하도록 하는 `printItems2` 함수를 구현하라.
# 
#         기생충
#         2019
#             설국열차
#             2013
#                 살인의 추억
#                 2003
# 
#     **힌트**
#     * `printItems` 함수의 인자를 두 개로 수정한다. 
#         하나는 리스트의 인자를 다루며, 다른 하나는 들어쓰기 정도를 다루는 
#         인자를 하나 받는다.
#         
#         ```python
#         def printItems2(aList, level):
#         명령문
#         ```
# 
#     * 위에서 `level` 매개변수의 인자는 탭키를 사용하는 횟수를 나타내도록 한다. 
#         그러면 `printItems2(moBong, 0)`을 실행하면 원하는 결과가 나와야 한다.
#     * 탭 출력은 `print('\t')`를 이용하면 된다.
#     <br><br>
# 1. 위 과제에서 구현한 `printItems2` 함수를 아래와 같이 수정하라.
#     * 인자수를 세 개로 늘린다.
# 
#         ```python
#         def printItems3(aList, level, indent=False):
#             명령문
#         ```
# 
#     * `indent` 매개변수의 키워드인자 값이 `True`이면 연습4에서 처럼 들여쓰기를 하고, 
#         `False`이면 들여쓰기를 하지 않아야 한다.
#     <br><br>
# 1. `printItems` 함수를 재귀가 아닌 `while` 함수를 이용하여 구현하라.
# 
#     **힌트:** `while` 반복문에 사용되는 조건식을 선택하는 게 핵심이다.
#     재귀로 구현된 함수로부터 이에대한 힌트를 얻을 수 있다.
