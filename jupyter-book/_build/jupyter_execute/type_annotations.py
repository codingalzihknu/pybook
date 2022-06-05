#!/usr/bin/env python
# coding: utf-8

# (ch-type-annotation)=
# # (부록) 자료형 힌트

# ## 동적 타이핑 vs  정적 타이핑

# 파이썬은 **동적 타이핑**<font size='2'>dynamic typing</font>을 지원하는 언어이다.
# 즉, 함수나 변수를 선언할 때 변수들의 자료형을 명시적으로 제한하지 않는다.
# 동적 타이핑 언어의 경우 프로그램 실행 과정에서 문제가 발생하지 않도록 
# 프로그램을 작성해야 한다.

# 예를 들어 아래 `add` 함수를 보자.

# In[1]:


def add(a, b):
    result = a + b
    return result


# `add` 함수의 인자로 정수, 실수, 리스트, 문자열이 사용될 수 있다.

# In[2]:


add(10, 5)


# In[3]:


add([1, 2], [3])


# In[4]:


add("저 ", "잠깐만요!")


# 하지만 두 인자가 동일한 자료형을 가져야 한다.
# 예를 들어, 숫자와 문자열의 덧셈은 작동하지 않는다.
# 이유는 숫자와 문자열의 덧셈이 정의되어 있지 않기 때문이다.

# In[5]:


try:
    add(10, "five")
except TypeError:
    print("정수와 문자열은 서로 더할 수 없어요!")


# 반면에 C, Java 등 많은 프로그래밍 언어는 동적 타이핑 대신
# **정적 타이핑**<font size='2'>static typing</font>을 지원한다.
# 즉, 함수나 변수를 선언할 때 사용되는 변수들의 자료형과 인자 및 반환값의 자료형을 
# 항상 명시해야 하며 지정된 자료형이 사용되지 않을 경우 오류를 발생시킨다.
# 아래 코드는 C 언로 작성한 `add()` 함수이다.
# 
# ```c
# int add(int a, int b) {
#     int result = a + b;
#     return result;
#     }
# ```

# 파이썬은 3.6 버전부터 정적 타이핑 형식을 옵션으로 지원한다. 
# 다만 C, Java의 자료형과 관련된 엄격함은 전혀 존재하지 않으며, 
# 그냥 정적 타이핑의 형식만 빌려왔다.
# 즉, **자료형 힌트**<font size='2'>type annotations</font>를 지원할 뿐이며, 
# 실제로는 동적 타이핑 방식을 사용한다.
# 예를 들어, `add` 함수를 아래와 같이 선언할 수 있다.
# 화살표 `->` 오른쪽에 위치한 `int` 함수 반환값의 자료형을 명시함에 주의하라.

# In[6]:


def add(a: int, b: int) -> int:
    return a + b


# ## 파이썬과 자료형 힌트

# 파이썬이 자료형 힌트를 지원하기 시작했지만 겉모습에만 한정된다.
# 예를 들어 `add()` 함수가 자료형 힌트를 사용했다 하더라도 
# 여전히 문자열이나 리스트를 인자로 사용할 수 있다.

# In[7]:


print(add(10, 5))
print(add([1, 2], [3]))
print(add("저 ", "잠깐만요!"))


# ### 자료형 힌트의 장점

# 하지만 자료형 힌트가 형적적임에도 불구하고 여러 장점을 갖는다.

# 첫째, 코드에 사용된 객체들의 자료형에 대한 정보를 제공한다.
# 
# 예를 위해, 먼저 벡터 자료형 `Vector` 를 실수들의 리스트 자료형으로 정의해보자.
# 이를 위해 `typing` 모듈의 `List` 클래스를 불러온다.

# In[8]:


from typing import List

Vector = List[float]


# 이제 아래 두 개의 정의를 비교하면 둘째 정의가 보다 많은 정보를 제공함을 알 수 있다.
# 
# - 정의 1: 전통적 방식

# In[9]:


def dot_product(x, y): 
    ...


# - 정의 2: 자료형 힌트

# In[10]:


def dot_product(x: Vector, y: Vector) -> float: 
    ...


# :::{admonition} 말줄임표(`...`)
# :class: info
# 
# 함수 본문에 사용되는 말줄임표 기호 `...` 는 "앞으로 채워질 것이다" 정도의 의미로 이해하면 되며
# `pass` 명령문과 비슷하게 작동한다. 
# 단, `pass` 명령문은 "아무 것도 하지 않고 그냥 넘어간다" 를 가리키는 명령문이기에 원래의 의미는 다르다.
# :::

# 둘째, `mypy` 와 같은 패키지를 이용하면
# 파이썬 코드를 실행하기 전에 작성된 코드에 사용된 함수와 변수들이 모두 
# 적절한 자료형을 사용했는지 여부, 
# 즉 유형 검사를 실행할 수 있다.
# 
# 하지만 여기서는 mypy 패키지를 사용하지 않으며,
# 관심이 있다면 [mypy 공식 문서](https://mypy.readthedocs.io/en/stable/)를 참조하기를 추천한다.

# :::{admonition} `mypy` 패키지 설치 및 활용
# :class: info
# 
# 터미널에서 아래 명령문으로 `mypy` 패키지를 설치할 수 있다.
# 
# ```shell
# $ pip install mypy-ipython
# ```
# 
# 주피터 노트북 또는 ipython 에서 `mypy` 명령문을 사용하려면 아래 매직 명령문으로 `mypy`를 불러온다.
# 
# ```python
# %load_ext mypy_ipython
# ```
# 
# 그런 다음 파이썬 코드를 작성하고 실행한 후에 아래 명령문을 실행하면 지금까지 작성한 코드를 대상으로 
# **유형 검사**<font size='2'>type checking</font>를 진행한다.
# 
# ```python
# %mypy
# ```
# 
# 예를 들어 아래 결과를 얻을 수 있다.
# 
# ```python
# >>> a : int = 3.4
# >>> %mypy
#     a : int = 3.4
# error: Incompatible types in assignment (expression has type "float", variable has type "int")
# Found 1 error in 1 file (checked 1 source file)
# Type checking failed
# ```
# :::

# 셋째, 편집기의 자동완성 기능을 보다 적절하게 활용하게 해준다.
# 
# 예를 들어, 구글 코랩, Visual Studio Code 등에서 아래 코드를 작성하다 보면 
# 매개변수 `xs`가 정수들의 리스트를 입력받을 것으로 기대하며,
# 리스트의 메소드의 목록을 보여주며 코드 작성을 도와준다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/type_annotation.png" width="90%"></div>

# ### 자료형 힌트 사용법

# `int`, `bool`, `float`, `str` 등의 기본 자료형은 그대로 사용한다.

# In[11]:


a : int = 3


# In[12]:


b : bool = True


# In[13]:


c : float = 3.14


# In[14]:


s : str = "python"


# 반면에 `list` 라고 단순히 언급하는 것은 별 도움 않된다.
# 이유는 리스트 항목의 자료형을 알 수 없기 때문이다.

# In[15]:


def total(xs: list) -> float:
    return sum(xs)


# 대신에 어떤 자료형의 값으로 구성된 리스트인지 명시하면 보다 많은 정보를 전달한다.

# In[16]:


def total(xs : List[float]) -> float:
    return sum(xs)


# 경우에 따라 변수의 자료형이 명확하지 않을 수 있다.
# 예를 들어, 아래 두 변수는 어떤 종류의 리스트인지 명확하지 않다.

# In[17]:


values = []


# 하지만 자료형을 명시하면, 
# 현재는 비어 있는 리스트이지만 앞으로 정수가 추가될 것임을 암시한다.

# In[18]:


values : List[int]= []


# In[19]:


values.append(3)
values.append(5)
values


# 아래의 경우는 애매함이 더욱 심하다.

# In[20]:


best_so_far = None


# `None`은 '아무 값도 아니다'를 가리키는 '값'이다.
# 하지만 이런 경우는 나중에 다른 값을 가리키는 변수를 미리 선언해 놓기 위해 
# 사용되곤 한다. 
# 따라서 앞으로 지정될 값의 자료형을 미리 암시해줄 필요가 있다.
# 이를 위해 `Optional` 을 `List` 와 유사한 방식으로 사용한다.
# 예를 들어 아래 코드는 앞으로 부동소수점을 할당할 것이라고 암시한다.

# In[21]:


from typing import Optional

best_so_far: Optional[float] = None


# ## `typing` 모듈

# `typing` 모듈은 `List`, `Optional` 이외에도 타이핑 힌트에 사용될 수 있는 다른 많은 자료형을 포함한다.
# 여기서는 그중에 일부만 다룰 예정이다.
# 
# 다음은 사전, 이터러블, 튜플의 자료형 힌트를 불러온다.

# In[22]:


from typing import Dict, Iterable, Tuple


# - `counts` 변수는 문자열을 키(key)로, 정수를 키값으로 사용하는 사전 자료형을 가리킨다.

# In[23]:


counts: Dict[str, int] = {'data': 1, 'science': 2}


# In[24]:


counts['data']


# - `evens` 변수는 0부터 9사이의 짝수들의 리스트에 해당하는 이터레이터를 가리킨다.

# In[25]:


evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)


# In[26]:


next(evens)


# In[27]:


next(evens)


# - `triple` 변수는 정수, 실수, 정수 세 개의 값을 갖는 튜플을 가리킨다.

# In[28]:


triple: Tuple[int, float, int] = (10, 2.3, 5)


# In[29]:


triple[1]


# ### 함수의 자료형: `Callable`

# 파이썬에서 함수는 1종 객체이다. 
# 즉, 함수의 인자 또는 반환값으로 함수를 입력할 수 있다.
# 따라서 함수의 자료형도 명시할 수 있어야 하며,
# 이를 위해 호출가능한 이라는 의미의 `Callable` 자료형을 사용한다.

# In[30]:


from typing import Callable

def twice(repeater: Callable[[str, int], str], s : str, n : int) -> str:
    return repeater(s, n)


# `twice()` 함수에 사용된 세 개의 매개변수가 기대하는 입력값의 자료형은 다음과 같다.
# 
# * `repeater`: 문자열(`str`) 과 정수(`int`) 두 개의 인자를 받으며, 반환값은 문자열`str` 인 함수를 인자로 받음.
# * `s`: 문자열을 인자로 받음.
# * `n`: 정수를 인자로 받음.

# 예를 들어, 아래 `comma_repeater()` 함수를 `twice` 함수의 인자로 사용해보자.

# In[31]:


def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)


# `comma_repeater()` 함수는 주어진 정수 만큼 주어진 문자열을 복제하여 이어붙인다.
# 단, 복제된 문자열은 쉼표로 분리한다.

# In[32]:


comma_repeater("type hints", 3)


# `twice(comma_repeater, "type hints", 3)`는 
# `comma_repeater("type hints", 3)`의 반환값을 반환한다.

# In[33]:


twice(comma_repeater, "type hints", 3)


# ### 자료형 객체

# 자료형 힌트에 사용된 자료형들 자체도 1종 객체이며,
# 따라서 변수에 할당될 수 있다.
# 예를 들어, 복잡한 자료형에 단순한 이름을 지정할 수 있다.
# 
# 아래 코드는 정수들의 리스트에 해당하는 자료형을 `Numbers` 라고 보다 단순한 이름으로 지정한다.

# In[34]:


Numbers = List[int]


# 그러면 정수 리스트에 포함된 항목들의 합을 반환하는 함수를 다음과 같이
# 단순한 자료형 힌트를 이용하여 정의할 수 있다.

# In[35]:


def my_sum(xs: Numbers) -> int:
    return sum(xs)


# In[36]:


my_sum([1, 2, 3, 4, 5])

