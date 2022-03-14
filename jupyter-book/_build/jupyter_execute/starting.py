#!/usr/bin/env python
# coding: utf-8

# # 프로그래밍 시작하기

# 간단한 예제를 이용하여 파이썬 프로그래밍을 맛보기 해본다.

# ## 파이썬 시작하기

# 다음 명령을 실행하면 `Hello, world` 문구가 화면에 출력된다.

# In[1]:


print("Hello, world!")


# ### 변수 할당

# 계속해서 아래 명령문도 실행해보자. 

# In[2]:


a = 3
b = 2 * a


# 이제 `a` 와 `b`를 변수로 활용할 수 있고
# 원하는 모든 연산을 수행할 수 있다.

# In[3]:


a * b 


# 이처럼 변수와 값을 연결시키는 것을 **변수 할당**<font size="2">variable assignment</font>
# 명령문이라 한다.
# 변수가 가리키는 값을 확인하려면 보통 다음과 같이 `print()` 함수를 이용한다.

# In[4]:


print(a)


# In[5]:


print(b)


# 프린트 함수는 두 개 이상의 값을 동시체 출력할 수 있다.
# 지정된 두 인자는 공백(스페이스)로 구분된다.

# In[6]:


print(a, b)


# :::{admonition} 코드 셀 실행
# :class: tip
# 
# 주피터 노트북의 코드 셀<font size="2">code cell</font>은
# IPython 콘솔처럼 명령문을 실행할 수 있으며 
# 이어지는 코드 셀은 이전에 실행된 코드 셀의
# 내용을 이어 받는다.
# 하지만 코드 셀은 콘솔과는 달리 여러 줄의 파이썬 명령문을 
# 마치 편집기로 작성된 하나의 코드 파일을 실행하는 것처럼
# 전체 명령문을 차례대로 실행할 수 있다.
# :::

# ### 값과 변수의 자료형

# 파이썬에 사용되는 값과 선언된 변수는 모두 자료형를 갖는다.
# 정수의 자료형은 `int`이며, 
# `type()` 함수를 이용하여 확인할 수 있다.

# In[7]:


type(6)


# 선언된 변수의 자료형은 할당된 값의 자료형으로 지정된다.

# In[8]:


type(b)


# 앞서 보았듯이 파이썬의 변수 할당 명령문은 변수에 할당되는 값의 자료형을 지정하지 않으며,
# 이는 C, C++, C#, 자바 등 다른 프로그래밍 언어와의 차이점 중에 하나다.
# 
# 예를 들어, C 언어에서 변수 선언은 아래와 같이 변수의 자료형을 지정한다.
# 
# ```c
# int b = 6;
# ```
# 
# 따라서 문자열 등 다른 자료형의 값을 가리키도록 하는 것을 허용하지 않는다.
# 
# ```c
# b = "hello";  // 허용되지 않음
# ```
# 
# 하지만 파이썬에서는 변수의 자료형을 지정하지 않았기에 임의의 자료형의 값으로 
# 변경할 수 있다.

# In[9]:


b = "hello"


# 변수의 자료형은 변경된 값의 자료형으로 함께 바뀐다.
# 문자열의 자료형은 `str` 이다.

# In[10]:


type(b)


# ## 파이썬의 기본 자료형

# 정수, 부동소수점, 부울값 등 세 종류의 **스칼라**<font size="2">scalar</font> 
# 자료형을 기본으로 제공한다.

# ### 정수

# -2, -1, 0, 1, 2 등의 정수는 `int` 유형<font size="2">type</font>의 값이다.
# 정수는 사칙연산, 변수 할당 등에 사용된다.

# In[11]:


1 + 2


# In[12]:


a = 4
type(a)


# In[13]:


a * 2


# ### 부동소수점

# **부동소수점**은 유리수, 실수 등을 가리키며 `float` 유형의 값이다.
# 정수와 마찬가지로 사칙연산, 변수 할당 등에 사용된다.

# In[14]:


2.1 + 3.3


# In[15]:


c = 2.1
type(c)


# 정수와의 연산도 가능한데, 이때 정수를 부동소수점으로 취급한다. 
# 예를 들어 3은 3.0으로 처리된다.

# In[16]:


2.3 + 3


# In[17]:


2.3 + 3.0


# ### 부울값

# 참과 거짓을 의미하는 `True`와 `False`를 
# **부울값**<font size="2">boolean</font>
# 또는 **진리값**이라 한다.
# 부울값은 `bool` 유형을 갖는 **유일한 두 개의 값**이다.

# In[18]:


type(True)


# In[19]:


d = False
type(d)


# 등식, 부등식 등이 부울값을 가리키는 대표적인
# **표현식**<font size="2">expression</font>이며,
# 이렇게 부울값을 가리키는 표현식을
# **논리식**<font size="2">logical expression</font>라 한다.

# In[20]:


3 > 4


# In[21]:


test = (1.0 == 1)


# In[22]:


test


# In[23]:


type(test)


# ## 계산기

# 파이썬을 계산기로 활용할 수 있다.

# In[24]:


7 * 3


# 정수에 점(`.`)을 찍으면 부동소수점으로 처리된다.

# In[25]:


7 * 3.


# 지수승은 `**` 를 사용한다.

# In[26]:


2 ** 10


# 정수 나눗셈의 몫(`//`)과 나머지(`%`) 연산도 지원된다.

# In[27]:


8 // 3


# In[28]:


8 % 3


# 몫 계산과 나눗셈 연산은 다르다.
# 몫은 정수 계산이며, 나눗셈은 부동소수점 연산이다.

# In[29]:


8 / 3


# 나눗셈의 몫이 정수인 경우엔 차이를 두지 않는다.

# In[30]:


(4 / 2) == (4 // 2)


# :::{admonition} 형변환 함수
# :class: info
# 
# `2.3 + 3`을 실행하면 파이썬 해석기<font size="2">interpreter</font>는
# 내부적으로 정수를 부동소수점으로 형변환하는 함수 `float()`를 이용하여
# 정수 `3`을 부동소수점 `3.0`으로 유형을 변환한 후에
# 덧셈을 처리한다. 
# 이렇게 값의 유형을 적절하게 자동 변환하는 기능을 
# **형변환**<font size="2">type casting</font>이라 부른다.
# 
# ```python
# >>> float(3)
# 3.0
# ```
# 
# `float()` 함수 이외에 `int()`, `str()`, `list()` 등 다양한 형변환 함수를 앞으로 
# 만나게 될 것이다.
# :::

# :::{admonition} 함수 이름 표기법
# :class: tip
# 
# `float`는 부동소수점 자료형을 가리키기도 하고 
# 형변환 함수를 가리키기도 한다. 
# 여기서는 자료형과 함수 이름을 구분하기 위해 
# 함수는 `int()`, `float()`, `str()`, `list()` 등처럼
# 함수 이름과 괄호를 함께 사용하는 표기법 관행을 따른다.
# :::

# ## 문자열

# **문자열**은 문자와 기호들의 나열을 의미하며 작은따옴표 또는 큰따옴표로 감싸인다.
# `print()` 함수는 지정된 문자열을 화면에 출력할 때 문자열을 감싸는 따옴표를 제고하고 
# 동시에 문자열에 포함된 특별한 기능을 수행하는 문자를 적절하게 변환해서 보여준다.

# In[31]:


'spam eggs'


# In[32]:


print('spam eggs')


# 작은따옴표로 감싸인 문자열이 작은따옴표를 포함하도록 하려면
# 백슬래시 `\`기호를 작은따옴표 기호 바로 앞에 추가한다.

# In[33]:


'doesn\'t'


# In[34]:


print('doesn\'t')


# :::{admonition} 슬래시 기호(&#x5C;)와 원화 기호(&#x20a9;)
# :class: info
# 
# 백슬래시 키는 키보드의 <kbd>Enter</kbd> 키 바로 위에 위치하는데
# 한글 키보드의 경우 원화 기호 키 <kbd>&#x20a9;</kbd> 가 대신 
# 자리잡고 있을 수 있다.
# 그리고 모니터 화면에도 사용하는 운영체제의 언어 설정에 따라
# 원화 기호(&#x20a9;)와 백슬래시 기호(&#x5C;) 둘 중에 하나로만 보인다.
# 하지만 단순한 언어 설정의 차이일 뿐 기능은 동일하다.
# :::

# 큰따옴표로 감싸인 문자열에 작은따옴표를 임의로 포함시킬 수 있다.
# 이는 문자열의 시작과 끝이 작은따옴표에도 불구하고 명확하기 때문이다.

# In[35]:


"doesn't"


# In[36]:


print("doesn't")


# 동일한 이유로 작은따옴표로 감싸인 문자열이 큰따옴표를 포함해도 된다.

# In[37]:


'"Yes," they said.'


# In[38]:


print('"Yes," they said.')


# 하지만 큰따옴표로 감싸인 문자열이 큰따옴표를 포함하려면
# 여기서도 백슬래시 기호를 추가해야 한다.

# In[39]:


"\"Yes,\" they said."


# In[40]:


print("\"Yes,\" they said.")


# 문자열에 큰따옴표와 작은따옴표가 동시에 포함되면
# 감싸는 따옴표와 동일한 종류의 따옴표는 백슬래시가 추가되어야 한다.

# In[41]:


'"Isn\'t," they said.'


# `print()` 함수는 백슬래시의 모든 특수 기능을 적절히 반영해서 화면에 출력한다.

# In[42]:


print('"Isn\'t," they said.')


# `\n`은 줄바꿈을 의미하는 문자다.

# In[43]:


s = 'First line.\nSecond line.'


# 변수 `s` 가 가리키는 문자열은 다음과 같다.

# In[44]:


s


# `print()` 함수를 이용하면 실제 의도한 대로 두 줄로 표현된다.

# In[45]:


print(s)


# ### 날 문자열

# 앞서의 경우처럼 작은따옴표, 큰따옴표, 특수 문자에 대해 백슬래시를 사용하냐,
# 그렇지 않냐를 걱정하는 것 대신에
# **날 문자열**<font size="2">raw string</font>을 사용하면 보다 편리하다.
# 날 문자열은 문자열 앞에 `r`을 추가해서 얻어지며
# 그러면 문자열 안에 포함된 모든 특수 문자들의 기능이 제거된다.

# In[46]:


print('C:\some\name')  # 일반 문자열 사용. 줄바꿈 적용됨.


# In[47]:


print(r'C:\some\name')  # 날 문자열 사용. 줄바꿈 없음.


# ### 여러줄 문자열

# 여러 줄로 작성된 문자열은 항상 세개의 작은따옴표 또는 세 개의 큰따옴표로 감싸져야 한다.

# In[48]:


print("""첫째줄(위에 여백 없음!)
둘째줄
셋째줄
""")


# 하지만 다음과 같이 첫째줄에 비어 있는채로 출력된다.

# In[49]:


print("""
첫째줄(위에 여백 있음)
둘째줄
셋째줄
""")


# 이를 방지하려면 백슬래시 기호를 추가한다.

# In[50]:


print("""첫째줄(위에 여백 없음)
둘째줄
셋째줄
""")


# ### 문자열 연산

# 문자열의 `+` 와 `*` 두 기호를 이용한 연산을 지원한다.
# 
# `+` 연산자는 두 문자열을 이어붙인다.

# In[51]:


'hello' + 'python'


# In[52]:


'hello, ' + 'python'


# `*` 연산자는 정수와 문자열을 인자로 받아 정수 만큼 복제해서 이어붙인다.

# In[53]:


3 * 'hello'


# In[54]:


2 * 'hello, ' + "python"


# ### 문자열 길이

# 문자열에 포함된 문자의 개수를 문자열의 길이로 지정한다.
# `len()` 함수가 문자열의 길이를 계산한다.

# In[55]:


s = 2 * 'hello, ' + "python"


# In[56]:


len(s)


# ### 문자열 인덱싱

# 문자열은 문자 여러 개의 나열이며 문자들 사이의 순서가 중요하다.
# 이때 문자열 왼편에 위치한 문자부터 차례대로 0, 1, 2, 3 등의
# **인덱스**<font size="2">index</font>를 부여받는다.
# **인덱싱**<font size="2">indexing</font>은 
# 인덱스를 이용하여 문자열의 항목을 확인하는 기능이다.

# In[57]:


word = 'I love Python!'


# In[58]:


word[0]  # 0번 인덱스 문자. 즉, 왼쪽에서 첫번째 문자.


# In[59]:


word[5]   # 5번 인덱스 문자. 즉, 왼쪽에서 여섯번째 문자.


# 인덱스를 문자열 오른쪽에서부터 차례대로 -1, -2, -3 등 음수로 지정할 수도 있다.

# In[60]:


word[-1]  # 맨 오른쪽 문자. 즉 마지막 문자.


# In[61]:


word[-2]  # 끝에서 두번째 문자.


# In[62]:


word[-6]  # 끝에서 여섯번째 문자.


# ### 문자열 슬라이싱

# **슬라이싱**<font size="2">slicing</font>은 지정된 인덱스의 구간에 해당하는
# 문자들을 추출하여 새로운 문자열을 생성하는 기능이다.

# In[63]:


word[0:2]  # 0번 인덱스부터 2번 인덱스 이전까지 추출


# In[64]:


word[2:5]  # 2번 인덱스부터 5번 인덱스 이전까지 추출


# 구간의 처음과 끝을 생략할 수 있다.
# 그러면 구간의 시작은 0, 구간의 끝은 문자열의 길이에 1을 더한 값으로 자동 지정된다.

# In[65]:


word[:2]   # 처음부터 1번 인덱스까지


# In[66]:


word[4:]   # 4번 인덱스부터 끝까지


# In[67]:


word[-2:]  # 끝에서 두번째 인덱스부터 끝까지


# In[68]:


word[:3] + word[3:]


# **보폭**<font size="2">stride</font>을 사용하여 인덱스를 
# 지정된 보폭만큼 건너 뛰면서 문자를 추출할 수 있다.
# 보폭이 1인 경우는 앞서 본 것처럼 보폭 표기를 아예 생략하면 된다.

# In[69]:


word[2:10:2]  # 2번 인덱스부터 9번 인덱스까지 두 개씩 건너뛰며 추출


# -1을 보폭으로 지정하면 오른쪽에서 왼쪽으로 역순으로 추출한다.

# In[70]:


word[::-1]  # 문자열 뒤집기


# In[71]:


word[-2:-8:-2]  # 끝에서 두번째 인덱스부터 끝에서 일곱번째 인덱스까지 두 개씩 건너뛰며 추출


# 문자열의 길이에 해당하는 범주를 벗어나는 인덱스를 사용하면 오류가 발생한다.
# 
# ```python
# >>> word[42]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# ```

# 반면에 슬라이싱에서는 자동으로 문자열의 처음과 끝을 한계로 사용한다.

# In[72]:


word[4:42]


# In[73]:


word[42:]


# ### 문자열 수정 가능성

# 한 번 생성된 문자열은 수정이 불가능<font size="2">immutable</font>하다.
# 예를 들어 다음과 같이 인덱싱 또는 슬라이싱을 이용하여
# 문자열을 수정하고자 하면 오류가 발생한다.
# 
# ```python
# >>> word[0] = 'J'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# 
# >>> word[2:] = 'py'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# ```

# 문자열을 수정하는 대신 인덱싱, 슬라이싱, 문자열 연산을 활용하여 
# 필요한 문자열을 생성해야 한다.

# In[74]:


'You' + word[1:]


# ## 리스트

# 파이썬은 여러 개의 값을 하나로 묶어 다룰 수 있는 자료형을 지원한다.
# 여기서는 **리스트**<font size="2">list</font>를 간단히 소개한다.
# 리스트는 임의의 값을 **항목**<font size="2">item</font>으로 여러 개 포함할 수 있다. 
# 서로 다른 자료형의 항목을 포함할 수도 있다.

# In[75]:


name_age = ["홍길동", 22]


# 하지만 동일한 자료형의 값들로 이루어지는 것이 일반적이다.

# In[76]:


squares = [1, 4, 9, 16, 25]
squares


# ### 리스트 인덱싱과 슬라이싱

# 문자열 자료형처럼 리스트 자료형도 인덱싱과 슬라이싱 기능을 지원하며
# 사용법은 사실상 동일하다.
# 다만 왼편에 위치한 항목부터 0, 1, 2, 3 등으로 인덱스를 지정할 뿐이다.

# In[77]:


squares[0]


# In[78]:


squares[-1]


# In[79]:


squares[-3:]


# In[80]:


squares[:]


# ### 리스트 연산

# `+` 연산자는 두 개의 리스트를 이어붙인다.

# In[81]:


squares + [36, 49, 64, 81, 100]


# ### 리스트 길이

# 리스트의 길이는 포함된 항목의 개수이며, 문자열의 경우처럼 `len()` 함수로 계산된다.

# In[82]:


len(squares)


# ### 리스트 수정 가능성

# 리스트는 항목 변경, 항목 추가 등 수정이 가능<font size="2">mutable</font>하다.

# **항목 수정**
# 
# 예를 들어 1부터 5까지 자연수의 세제곱으로 이루어진 리스트를 다음과 같이 정의하자.

# In[83]:


cubes = [1, 8, 27, 65, 125]


# 그런데 4의 세제곱은 65가 아니라 64이다.

# In[84]:


4 ** 3


# 그래서 3번 인덱스 항목을 64로 수정해야 한다.

# In[85]:


cubes[3] = 64


# 3번 인덱스 값이 수정되었다.

# In[86]:


cubes


# **항목 추가**
# 
# 예를 들어 6의 세제곱을 `cubes` 리스트의 오른쪽 끝에 새로운 항목으로 다음과 같이 추가할 수 있다.

# In[87]:


cubes.append(6 ** 3)


# 7의 세제곱도 추가하자.

# In[88]:


cubes.append(7 ** 3)


# 리스트가 확장되었다.

# In[89]:


cubes


# **슬라이싱 대체**
# 
# 슬라이싱으로 리스트의 특정 구간을 다른 리스트로 대체할 수 있다.

# In[90]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters


# 소문자 'c', 'd', 'e' 를 대문자 'C', 'D', 'E' 로 변경하려면
# 2번 인덱스부터 4번 인덱스까지를 대상으로 슬라이싱 대체를 적용한다.

# In[91]:


letters[2:5] = ['C', 'D', 'E']
letters


# 슬라이싱 구간에 포함된 항목의 개수와 대체되는 리스트의 길이가 다를 수 있다.
# 예를 들어 2번 인덱스부터 4번 인덱스까지의 항목을 삭제하려면
# 다음과 같이 빈 리스트로 대체하면 된다.

# In[92]:


letters[2:5] = []
letters


# 물론 항목 적체를 삭체할 수도 있다.

# In[93]:


letters[:] = []
letters


# ### 중첩 리스트

# 리스트의 항목으로 임의의 값이 사용될 수 있으며
# 따라서 다른 리스트로 가능하다.

# In[94]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]


# In[95]:


x


# In[96]:


x[0]


# In[97]:


x[0][1]


# ## 파이썬 프로그래밍 맛보기

# 지금까지 살펴본 것은 파이썬 프로그래밍의 가장 간단한 기능들이다.
# 앞으로 본격적으로 파이썬 프로그래밍의 진수를 배우기 전에
# 보다 복잡한 문제를 해결하는 프로그램을 몇 개 살펴본다.

# ### `if` 조건문

# 특정 조건의 성립여부에 따라 다른 일을 실행하게 만드는 명령문을 **조건문**이라 부른다. 
# 예를 들어 `guess` 와 `secret` 두 변수가 가리키는 값의 동치 여부에 따라
# 다른 문장을 출력하도록 하려면 아래와 같이 한다.
# 
# ```python
# if guess == secret:
#     print("맞았습니다!")
# else:
#     print("틀렸습니다!")
# ```

# ### `for` 반복문

# `for` 반복문은 문자열과 리스트에 포함된 전체 항목을 대상으로
# 동일한 작업을 실행하고자 할 때 활용되며
# 아래 구문 형식을 사용한다.
# 
# ```python
# for 변수이름 in 문자열또는리스트:
#     본문명령문
# ```
# 
# - '변수이름 in 문자열또는리스트': '변수이름'은 문자열 또는 리스트에 포함된 항목을
#     왼쪽에서부터 차례대로 가리킨다.
# - '변수이름'이 현재 가리키고 있는 항목을 대상으로 지정된 '본문명령문'을 실행한다.
# 
# - '본문명령문' 실행이 완료되면 '변수이름'은 다음 항목을 가리키게 된다.
# - '변수이름'이 더 이상 가리킬 항목이 없을 때까지 위 과정을 반복한다.

# :::{prf:example}
# :label: for-loop_str-indexting
# 
# 문자자열에 포함된 문자 각각을 출력하는 코드는 다음과 같다.
# 
# ```python
# s = "안녕하세요"
# 
# for item in s:
#     print(item)
# ```
# 
# ```python
# 안
# 녕
# 하
# 세
# 요
# ```
# 
# `for` 반복문이 실행되는 동안 `item` 변수가 차례대로 `'안'`, `'녕'`, `'하'`, `'세'`, `'요'` 를 가리킬 때마다 출력된다. 
# :::

# :::{prf:example}
# :label: for-loop_list-indexing
# 
# 정수 리스트에 포함된 모든 항목의 합을 계산하는 코드는 다음과 같다.
# 
# ```python
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# sum = 0                # 항목을 차례대로 더한 값. 시작은 0부터.
# 
# for item in num_list:
#     sum += item        # 현재 가리키는 값을 합에 추가
#     
# print("1부터 10까지의 합:", sum)
# ```
# 
# ```python
# 1부터 10까지의 합: 55
# ```
# 
# `for` 반복문이 실행되는 동안 `item` 변수가 1부터 10까지의 수를 
# 차례대로 가리키며 `sum`은 그만큼씩 증가한다.
# :::

# :::{prf:example}
# :label: for-loop_even-sum
# 
# 정수 리스트에 포함된 항목 중에서 짝수들만의 합을 계산하는 코드는 다음과 같다.
# 
# ```python
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# sum = 0                # 항목을 차례대로 더한 값. 시작은 0부터.
# 
# for item in num_list:
#     if item % 2 == 0:
#         sum += item        # 짝수인 경우 합에 추가
#     
# print("짝수 항목의 합:", sum)
# ```
# 
# ```python
# 짝수 항목의 합: 30
# ```
# 
# `item` 변수가 가리키는 값이 짝수일 때만 `sum`에 추가된다.
# :::

# ### `while` 반복문 

# `while` 반복문은 특정 조건이 만족되는 동안 동일한 작업을 반복 수행하도록 할 때
# 사용하는 명령문이며 다음 구문 형식으로 사용된다.
# 
# ```python
# while 조건논리식:
#     본문명령문
# ```
# 
# - '조건논리식'이 `while` 반복문이 실행된느 조건을 가리키며,
#     반드시 콜론으로 끝나야 한다.
# - `while` 반복문의 '**본문**'<font size="2">body</font> 명령문은
#     반드시 탭 들여쓰기를 사용해야 한다.
#     
#     '본문명령문'의 실행이 완료되면 `while` 반복문의 처음으로 돌아가 
#     '조건논리식'을 다시 확인하여 참이면
#     다시 '본문명령문'을 실행하는 과정을 반복한다.
#     '조건논리식'이 거짓이 되는 순간 `while` 반복문 전체의 실행이 멈추고
#     다음 명령문이 실행된다.

# :::{prf:example} 피보나치 수열
# :label: while-fibonacci
# 
# **피보나치 수열**<font size="2">Fibonacci sequence</font>의
# 항목을 생성하는 코드를 구현해보자.
# 피보나치 수열의 항목을 생성하는 알고리즘은 다음과 같다.
# 
# - 첫째, 둘째 항목은 0과 1
# - 가장 최근에 생성된 두 개의 값을 더해 새로운 항목을 생성하는 과정 반복
# 
# 위 알고리즘을 이용하여 피보나치 수열의 처음 10개 항목을 생성하려면
# 먼저 첫째, 둘째 항목을 변수로 지정한 다음에 최근에 생성된
# 두 개의 값을 더하는 과정을 8번 정도 반복한다.
# 
# ```python
# a, b = 0, 1
# 
# # 첫째, 둘째 항목 출력
# 
# print(a)
# print(b)
# 
# # 셋째 항목부터는 이전 두 항목의 합으로 지정한다.
# 
# count = 2  # 반복횟수 저장
# while count < 10:
#     a, b = b, a+b
#     print(b)        # 새로 생성된 항목
#     count += 1      # count = count + 1, 생성된 항목 수 1 증가
# ```
# 
# ```python
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# ```
# 
# 위 코드에 사용된 주요 명령문의 실행과정은 다음과 같다.
# 
# 1. `a, b = 0, 1`: 변수 `a` 에는 `0`을, 변수 `b` 에는 `1`을 할당한다.
# 1. `count = 2`: 생성된 항목 수를 가리킨다. 이미 두 개가 생성되었다.
# 1. `while count < 10:` 변수 `count` 가 가리키는 값이 `10` 보다 작은 동안 `while` 반복문의 본문 코드를 반복 실행하라. 즉, 항목 10개를 만들 때까지  본문을 반복한다.
# 1. `while` 반복문 본문
#     - `a, b = b, a+b`
#         - 변수 `a` 가 가리키는 값을 변수 `b` 가 이전에 가리키던 값으로 변경하라.
#         - 변수 `b` 가 가리키는 값을 변수 `a` 와 변수 `b` 가 이전에 
#             가리키던 값의 합으로 변경하라.
#     - `print(a)`: 변수 `a` 가 현재 가리키는 값을 출력하라.
#     - `count += 1`: 생성된 항목 수를 1 증가시킨다.
# 1. 단계 3 으로 돌아가서 `count < 10` 조건이 참인지 여부를 확인하고,
#     참이면 단계 4 를 실행하고 거짓이면 실행을 종료한다.
# :::

# ## 연습문제

# 참고: [(실습) 프로그래밍 시작하기](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-starting.ipynb)
