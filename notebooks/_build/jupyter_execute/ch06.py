#!/usr/bin/env python
# coding: utf-8

# # 함수와 모듈

# _[Think Python의 3장](http://greenteapress.com/thinkpython2/html/thinkpython2004.html)와 [Think Python 14장](http://greenteapress.com/thinkpython2/html/thinkpython2015.html#sec173)의
# 내용을 요약 및 수정한 내용입니다._

# **고계 함수와 제1종 객체**
# 
# 파이썬에서는 함수도 하나의 값으로 간주된다.
# 이렇게 하나의 값으로 간주되는 대상을 **제1종 객체**(first-class object)라고 부른다.
# 제1종 객체로 간주되는 값은 변수에 할당되거나, 함수의 인자 또는 리턴값으로 사용될 수 있다.
# 
# 함수를 인자로 받거나 내주는 값으로 사용하는 함수를 **고계 함수**(higher-order function)라 부른다.

# ## 함수 정의하기

# 파이썬에서 함수의 정의는 아래 형식을 이용해야 한다.
# 
# ```python
# def 함수이름(매개변수1, 매개변수2, ..., 매개변수n):
#     명령문
#     return 표현식
# ```
# 
# **주의:** 함수 본체에 사용되는 명령문은 들여쓴다.
# 
# 함수를 정의할 때 사용되는 **매개변수**는 인자로 들어오는 값들을
# 함수 본체 명령문에 전달하는 역할을 수행한다.

# ### 예제

# 절댓값을 계산하는 함수 `myAbs`와
# 두 숫자의 합을 계산하는 함수 `myAdd`를 아래와 같이 직접 정의할 수 있다.
# 
# `myAbs`는 한 개의 값을 입력받아야 하기에 한 개의 매개변수가 필요하고,
# 반면에 `myAdd`는 더해야 할 두 개의 값을 입력받아야 하기에 두 개의 매개변수가 필요하다.

# In[1]:


def myAbs(num):
    if num >= 0:
        z = num
    else:
        z = -num
    return z

def myAdd(left, right):
    z = left + right
    return z


# In[2]:


myAbs(-3)


# In[3]:


myAdd(-3, myAbs(-3))


# ## 매개변수와 인자

# `myAbs`와 `myAdd`의 정의헤서 사용된 
# `num`, `left`, `right` 등은 함수의 인자를 받아들이는데 사용되는 **매개변수**이다.
# 그리고 매개변수를 통해 함수에게 전달되는 값들을 **인자**라고 부른다. 
# 사용되는 인자의 개수는 매개변수의 개수와 일치해야 한다.
# 
# 함수와 매개변수들의 이름은 각각의 역할에 맞게 정하는 것을 권유한다.
# 그러면 함수와 매개변수들의 이름을 보고 함수와 각 매개변수들의 의미와 
# 역할을 파악하는 데에 보다 유리하다.

# ### 옵션 인자

# `print` 함수를 이용하여 화면에 출력할 때 사용되는 인자의 수는 여러 개일 수 있다.

# In[4]:


print('Hello,', 'Python', '!')


# 그런데 여러 개의 인자를 각각 다른 줄에 출력하려면 아래와 같이 하면 된다.

# In[5]:


print('Hello,', 'Python', '!', sep='\n')


# 위에서 사용된 `sep`은 `print` 함수의 옵션 인자이다.
# `sep`과 같은 옵션 인자는 인자를 지정하지 않으면 기본값을 사용한다.
# `sep`의 기본값은 한 칸 띄어쓰기를 의미하는 `' '`이다.
# 즉, `print` 함수의 인자들을 한 칸씩 띄어서 화면에 보여준다.
# 그리고 위에서는 `sep`에 대한 인자를 띄어쓰기 대신 줄바꿈(`'\n'`)을
# 사용하였다.
# 
# 이렇듯 특정 함수들은 옵션 인자를 사용할 수 있으며, 그런 함수는
# 매개변수에 기본값을 지정하는 식으로 정의된다.
# 
# 예를 들어, `print`함수에 사용되는 매개변수 중에
# `sep` 이외에 `end`, `file`, `flush` 등이 기본값을 갖는다.
# 실제로 `help(print)` 명령문을 실행하면
# 아래와 같이 확인된다.
# 
# ```python
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# ```
# 
# * `sep` 매개변수: 출력할 인자들 사이에 대한 기준 지정. 기본값은 띄어쓰기.
# * `end` 매개변수: 화면 출력 후 추가로 할 일에 대한 기준 지정. 기본값은 줄바꿈.
# * `file` 매개변수: 출력 장치 지정. 기본값은 터미널 화면.
# * `flush` 매개변수: 여러 개의 출력값들을 하나씩 차례대로 출력 장치에 보낼지 말지를 지정. 기본값은 하나씩 바로바로 보내기.
# 
# 위 옵션 매개변수 중에서 `sep`과 `end`는 여러 모로 유용하게 활용할 수 있다.

# In[6]:


help(print)


# ### 예제

# 옵션 인자를 사용하는 함수를 정의할 수 있다.
# 아래 함수는 두 개의 숫자를 입력받아 합을 구한다.

# In[7]:


def myAdd10(left, right=10):
    add10 = left + right
    return add10


# 그런데, 둘째 매개변수의 기본값이 10으로 지정되었다.
# 따라서 둘째 인자를 반드시 입력하지 않아도 되며,
# 그럴 경우 둘째 인자는 10으로 처리된다.

# In[8]:


myAdd10(5)


# 물론 둘째 인자를 지정할 수도 있다.

# In[9]:


myAdd10(5, 20)


# 옵션 매개변수의 값을 지정하고잘 할 경우 매개변수 이름을 언급하는 것이 좋다.

# In[10]:


myAdd10(5, right=20)


# ## 수학과 프로그래밍에서의 함수 이해

# ### 수학에서의 함수

# 함수라는 표현이 수학에서 많이 사용된다. 
# 수학에서 함수는 두 집합 사이의 관계이며,
# 첫째 집합의 원소를 둘째 집합의 원소와 대응시킨다. 
# 
# 아래 그림은 집합 $X$의 원수 $x$와 집합 $Y$의 원소 $f(x)$를 대응시키는 함수를 보여준다.
# 
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Codomain2.SVG/440px-Codomain2.SVG.png" style="width:300px;"></div>
# 
# <그림 출처: [함수, 위키백과](https://ko.wikipedia.org/wiki/함수)>

# 이때 $X$와 $Y$를 각각 함수 $f$의 **정의역**(domain)과 
# **공역**(codomain)이라 부른다.

# ### 프로그래밍에서의 함수

# 프로그래밍에서 함수가 하는 역할은 다음과 같다. 
# 
# > 어떤 값이 입력(input)되면 그 값을 이용하여 특정 수식에 따라 계산한 후 
#     특정 값을 내준다(output).
#   
# 아래 그림은 함수의 입력(input)과 내주기(output)의 관계를 보여준다.
# 
# <div align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/440px-Function_machine2.svg.png" style="width:300px;"></div>
# 
# <그림 출처: [함수, 위키백과](https://ko.wikipedia.org/wiki/함수)>
# 
# 함수의 입력값으로 사용될 수 있는 값들의 집합이 정의역에 해당하고,
# 내주는 값들의 집합이 공역에 해당한다.
# 함수가 내주는 값을 **리턴값**이라 부르기도 한다.
# 이유는 함수가 내주는 값을 보통 `return` 지정자로 지정하기 때문이다.

# ### 차이점

# 입력값을 특정 집합의 원소로 보고, 리턴값을 다른 집합의 원소로 보고,
# 그리고 
# 두 집합 사이의 대응관계를 "수식에 따라 계산한다"라 이해한다면 
# 수학과 프로그래밍에서의 함수 개념은 동일하다.
# 
# * 정의역: 함수의 입력값들로 구성된 집합
# * 공역: 함수의 리턴값들로 구성된 집합
# 
# 실제로, 수학 함수를 프로그래밍 함수로 다룰 수 있다. 
# 예를 들어, 절댓값 함수는 실수에서 실수로 가는 함수이며,
# 양수는 그대로 두고, 음수는 부호를 바꿔 양수로 만든다. 
# 
# 절댓값에 해당하는 프로그래밍 함수는 `abs`이며, 아래와 같이 작동한다.

# In[11]:


abs(-3.3)


# 위에서 사용된 표현식 `abs(-3.3)`과 그 결과인 `3.3`의 역할은 다음과 같다.
# 
# * `abs`: 절댓값 함수를 가리키는 이름
# * `-3.3`: 입력값
# * `3.3`: 리턴값

# ### 프로그래밍 함수의 정의역

# 앞서 프로그래밍 함수의 입력값들로 구성된 집합이 수학 함수의 정의역에 
# 해당한다고 설명하였다.
# 그런데 주의사항이 하나 있다.
# 
# 파이썬의 경우, 함수의 입력값에 어떤 제한도 없기 때문이다.
# 다만, 의도하지 않은 값이 사용될 경우, 함수의 실행 과정에서 오류가 발생한다.
# 예를 들어, `abs` 함수를 문자열과 함께 실행하면 
# `TypeError`, 즉, 인자의 자료형에 문제가 있다는 오류가 발생한다.
# 이유는 `abs` 함수가 숫자만 다룰 수 있기 때문이다.

# In[12]:


abs('python')


# 따라서 프로그래밍 함수의 정의역은 입력값들 중에서 오류가 발생하지 않는 값들의 집합으로
# 보는 게 보다 더 적절하다.
# 하지만, 이것을 프로그래밍 함수의 정의역으로 **정의**(define)하지는 않을 것이다.
# 프로그래밍 함수의 정의역을 엄밀하게 정의하는 일은 보다 복잡하기에,
# 자세히 다루지 않는다. 
# 다만, 개념적으로 프로그래밍 함수와 수학 함수가 유사한 면이 많다라는 정도만
# 기억해두면 좋다.

# ### 프로그래밍 함수 예제

# 프로그래밍에서는 다루는 함수 유형을 살펴본다.

# #### 수학 함수와 유사한 경우
# 
# * 수를 입력하면 계산결과를 돌려준다.

# In[13]:


def toto1(x):
    y = x**2+1
    return y
    
print(toto1(3))


# * 아래 함수는 변수이름 `y`를 지역변수와 전역변수로 동시에 사용했다.
#     하지만 서로 관계가 없기 때문에 일반 수학 함수처럼 작동한다.

# In[14]:


y = -1

def toto2(x):
    y = x**2+1
    return y

# 전역변수 y는 함수와 아무 상관 없음.
print(y, toto2(3))


# In[15]:


y = -1

def toto3(x):
    y = x**2+1
    return y

# 전역변수 y는 함수와 아무 상관 없음.
print(toto3(3), y)


# #### 수학 함수와 조금 다른 경우

# * 아래 함수는 함수 안에서 전역변수 `y`를 업데이트한다.
#     이렇게 하면 `y`가 가리키는 값은 `toto` 함수의 호출에
#     민감하게 반응한다.

# In[16]:


y = -1

def toto4(x):
    global y
    y = x**2+1
    return y

# toto 함수가 실행되면 y 가 업데이트 됨.
print(toto4(3), y)


# In[17]:


y = -1

def toto5(x):
    global y
    y = x**2+1
    return y

# y 값을 먼저 확인 한 후에 toto 함수가 실행
print(y, toto5(3))


# #### 수학 함수와 많이 다른 경우

# * 함수의 리턴값이 지정되지 않으면 `None`을 내줌.
# * `None`은 아무런 의미가 없는 값임.
# * 대신에 아래 함수를 실행하면 변수 `y`의 값을 업데이트 함.
# * 수학엔 이런 함수 없음.

# In[18]:


y = -1

def toto6(x):
    global y
    y = x**2+1
    
print(toto6(3), y)


# In[19]:


y = -1

def toto7(x):
    global y
    y = x**2+1
    
print(y, toto7(3))


# ## 함수의 리턴값<a id='funReturn'></a>

# 앞서 살펴 보았던 `toto1`~`toto5` 같은 함수의 경우 `return` 지정자 이후에 
# 위치한 값 `y`를 내주는(output) 값으로 지정한다.
# 즉, 숫자 `x`를 입력(input)값으로 사용하여 실행하면
# 종료하기 전에 
# `y`가 가리키는 값 `x**2+1`를 내준다.
# 이렇게 함수가 실행을 종료하면서 내주는 값을 **리턴값**이라 부른다.

# ### 리턴값이 명시되지 않은 함수

# `toto6`와 `toto7`은 `return` 지정자를 사용하지 않았다.
# 이런 경우 파이썬은 암묵적으로 `return None`을 지정한다.
# 즉, 리턴값이 항상 `None` 값인 것이다.
# 
# **주의:** `None`은 아무런 의미를 갖지 않는 값이다.
# 
# 파이선 내장함수(built-in functions)들 중에 
# `print` 함수가 리턴값이 명시되지 않은 대표적인 함수이다. 
# 예를 들어, 아래 코드는 `print` 함수의 리턴값을 확인할 수 있다.

# In[20]:


x = print(1)
print(x)


# **주의:** 위 코드를 실행한 결과의 첫째 줄에서 보이는 `1`은 `print` 함수의 리턴값이 아니라,
# `print(1)`을 실행하여 모니터에 숫자 1을 출력하는 `print` 함수의 
# **부수효과**(side effect)에 불과하다.
# 함수의 부수효과에 대해서는 아래에서 좀 더 자세히 다룬다.

# ### 함수의 리턴값은 단 하나

# 함수 본체 코드에 `return` 지정자가 여러 번 사용되더라도 
# 함수를 실행할 때 내주는 값은 무조건 하나이다.
# 
# 예를 들어, 아래 `login` 함수는
# `members` 리스트에 아이디가 포함되어 있는지 여부를 
# 판단한다.
# 
# `login` 함수 본체에 `return` 지정자가 두 번 사용되었다.
# 하지만, `members`에 포함된 항목별로 회원여부를 판단할 때
# 회원이 확인되면 '누구누구님 환영합니다'를 리턴하고
# 바로 함수의 실행을 종료한다. 
# 즉, 더이상 `for` 반복문을 돌리지 않는다.

# In[21]:


members = ['egoing', 'k8805', 'leezche']

def login(_id):
    for member in members:
        if member == _id:
            return f'{member}님 환영합니다.'
    return '회원이 아닙니다.'


# In[22]:


login('egoing')


# In[23]:


login('k8805')


# In[24]:


login('liga')


# ## 함수호출

# 앞서 살펴 보았듯이 함수의 리턴값을 저장하거나 다른 함수의 인자로 전달할 수 있다.
# 즉, 하나의 값으로 다룰 수 있으며,
# 이렇게 함수를 이용하여 표현된 값을 **함수 표현식**이라 부른다. 
# 
# 예를 들어, 절댓값을 생성하는 함수인 `abs`에 부동소수점 `-3.3`을 
# 인자로 사용하여 표현된 값은 아래와 같다.
# 
# ```python
# abs(-3.3)
# ```
# 
# 또한, 실수 `abs(-3.3)`를 -3.3과 더해주려면 아래와 표현식처럼
# 함수의 합성을 이용할 수 있다.
# 
# ```python
# myAdd(abs(-3.3), -3.3)
# ```

# 하지만 함수 표현식이 가리키는 값을 실제로 확인하려면 
# 함수를 해당 인자와 함께 실행해야 한다.
# 이렇게 함수 표현식을 실행하는 것을 **함수호출**이라 부른다.
# 
# 예를 들어, 앞서 언급한 두 표현식의 호출해서 결과를 확인하려면 아래와 같이 할 수 있다.

# In[25]:


print(abs(-3.3))


# In[26]:


sumZero = myAdd(abs(-3.3), -3.3)
print(sumZero)


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

# In[27]:


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

# ## 함수호출의 부수효과

# 프로그램에서 사용되는 함수를 구분하는 다양한 기준이 있다.
# 여기서는 부수기능의 존재여부에 따른 함수 분류 기준을 살펴본다.

# ### 부수효과가 없는 함수 (Pure functions)
# 
# 함수가 호출되어 실행되어 실행결과를 리턴값으로 내줄 때까지 
# 실행결과를 생성하기 위한 일 이외에 다른 어떤 일도 하지 않는다면 
# 그 함수를 부수효과가없는 함수라 부른다.
# 
# 예를 들어 절대값을 계산하는 `abs` 함수와 덧셈을 행하는 `add` 함수 등이 순수한 함수이다. 
# 아래 그림에서 보듯이 인자를 입력받은 후에 각각 절대값과 덧셈을 실행하여 결과값을 돌려주는 일 
# 이외에는 다른 일을 행하지 않는다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/fun_pure.png" style="width:400px;"></div>

# ### 부수효과가 있는 함수 (Impure functions)
# 
# 부수효과가 있는 함수는 부수효과가 없는 함수와는 달리 결과값을 돌려주는 것 이외에 부수적인 일을 한다.
# 대표적으로 파이썬 내장함수인 `print` 함수가 부수효과를 갖는 함수이다.
# 
# 그런데 `print`가 부수효과를 갖는 함수라는 것을 확인하려면 아래 두 가지를 알아야 한다.
# 
# * 리턴하는 값이 무엇인가?
# * 부수적으로 어떤 일을 하는가?
# 
# 먼저, `print`가 리턴하는 값은 `None`이다. 
# 기타 언어에서는 보통 널(null) 값이라 부른다.
# 
# 다음으로, `print` 함수가 부수적으로 하는 일은 예를 들어 터미널 창에 어떤 문자열을 출력하는 것이다.
# `print("Hello Python")` 방식으로 `print` 함수를 호출하면 아래와 같이 `'Hello Python'` 이란 문자열을 출력한다.

# In[28]:


print("Hello Python")


# 즉, `print("Hello Python")`을 실행하였을 때 보여주는 
# `'Hello Python'`은 리턴값이 아니라 `print` 함수가 부수적으로 하는 일이다.

# ### 예제: 부수효과를 갖는 함수의 호출과정

# 부수효과를 갖는 함수호출의 실행과정은 부수효과가 없는 함수의 호출과정과 기본적으로 동일하다.
# 하지만 중간중간에 부수적인 일도 함께 벌어진다.
# 
# 먼저 아래 코드의 실행결과가 어떻게 도출되었는가를 잘 생각해보자.

# In[29]:


print(print(1), print(2))


# 아래의 그림은 위 코드를 호출하는 과정을 설명한다.
# 아래 그림에서 &#9312; ~ &#9319;번 사이의 번호가 배정된 네모상자로 둘러싸인 부분이 
# 현재 실행중인 함수호출 또는 함수호출의 결과값 또는 부수효과(화면 출력)를 나타낸다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/fun_print.png" style="width:600px;"></div>

# [PythonTutor: 함수호출 부수효과](http://pythontutor.com/visualize.html#code=def%20myPrint%28*args,%20**kwargs%29%3A%0A%20%20%20%20print%28*args,%20**kwargs%29%0A%0AmyPrint%28myPrint%281%29,%20myPrint%282%29%29&cumulative=false&curInstr=11&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# 앞서 사용한 표현식과 동일하게 작동하는 표현식이 계산되는 과정을 살펴볼 수 있다.
# 
# **주의:** `print` 함수와 동일하게 작동하는 `myPrint` 함수를 사용했다.
# 함수의 이름만 다를 뿐 동일한 표현식이다.

# ## 지역변수와 전역변수

# 함수를 선언할 때 사용되는 매개변수와 함수 본체에서 선언되는 변수는 함수가 실행되는 동안에만 의미를 갖는 변수들이며,
# 이런 변수들을 **지역변수**라 부른다. 
# 지역변수 가인 변수들은 **전역변수**라 부른다.
# 
# 예를 들어, `hour_to_min` 함수를 정의할 때 사용된 
# `hour`와 본체에서 선언된 `minutes` 변수는 모두 지역함수이며,
# `two_hour` 는 함수 밖에서 선언된 전역변수이다.

# In[30]:


def hour_to_min(hour):
    minutes = hour * 60
    return minutes


# 지역변수들은 함수 밖에서는 어떤 의미도 갖지 않는다. 예를 들어, 아래 코드를 실행하면 오류가 발생한다.

# In[31]:


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
# 위 명령문은 리스트의 항목이 또 다른 리스트이면 그 리스트의 항목들을 대상으로 동일한 확인작업을 수행하며,
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
# 리턴값을 다른 프레임에 넘겨 준 후에 사라지는 과정이 반복된다. 이렇게 특정 함수호출과 관련된 프레임을 **지역 프레임**이라 
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
# 명확히 하기 위해 `float`라는 자료형을 입력값와 리턴값에 대해 명시하였다.
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

# # 모듈

# 안내: [Think Python 14장](http://greenteapress.com/thinkpython2/html/thinkpython2015.html#sec173)
# 내용의 일부를 번역 및 요약수정하여 정리한 내용입니다.

# ## 모듈이란?

# 한 번 구현한 함수, 상수, 변수, 클래스, 객체 등 여러 파일에서 공유하여 사용하면 프로그램을 보다 효율적으로 구현할 수 있다.
# 이를 위해 **모듈**을 활용한다.
# 
# 파이썬에서 모듈은 간단하게 말하면 하나의 파이썬 소스코드 파일이다. 
# 파일의 확장자가 `py`이다. 
# 모듈은 언제든지 불러와서(import) 모듈에 포함된 내용을 활용할 수 있다.

# ## 모듈 종류

# 모듈은 크게 세 종류로 나뉜다.
# 
# * 내장 모듈(built-in module): 파이썬에서 기본적으로 제공하는 모듈
#     * 파이썬을 설치할 때 기본으로 제공되는 모듈
#     * 예제: `math`, `urllib.request`, `random`, `turtle`, `os`, `sys` 등등
# * 제3자 라이브러리 모듈: 제3자에 의해 제공된 라이브러리에 포함된 모듈
#     * 제3자가 제공한 라이브러리를 설치할 때 제공되는 모듈
#     * 예제: `numpy.random`, `matplotlib.pyplot`, `pygame.mixer` 등등
# * 사용자 정의 모듈: 개인 프로젝트를 진행하면서 작성한 모듈
#     * 프로젝트 관리를 위해 사용되는 모듈
#     * 예제: 아래 예제에서 소개되는 `wc.py` 파일

# ## 내장 모듈

# 파일썬을 설치하면 다양한 모듈이 함께 설치되며, 그런 모듈을 내장 모듈(built-in modules)이라 부른다.
# 지금까지 사용한 모듈은 `random`, `math`, `os`, `sys` 등이며, `import 모듈명` 형식으로 모듈을 불러왔다.
# 단, `.py` 확장자는 생략한다.
# 
# 예를 들어, `math` 모듈을 불러오려면 다음과 같이 한다.

# In[ ]:


import math


# 그러면 `math` 모듈에서 정의된 많은 수학 관련 함수들을 사용할 수 있다.
# 예를 들어, 로그(`log`) 함수의 사용은 다음과 같다.

# In[ ]:


math.log(2)


# 무작위 수 생성 함수들을 모아놓은 `random` 모듈에 0과 1사이의 실수를 무작으로 
# 생성하는 함수 `random`을 아래와 같이 사용한다.

# In[ ]:


import random

random.random()


# `random` 함수는 실행할 때마다 새로운 수를 무작위로 생성한다.

# In[ ]:


random.random()


# ## 제3자 라이브러리 모듈

# 제3자에 의해  제공된 라이브러리에 포함된 모듈을 사용하려면 먼저 추가 패키지를 설치해야 한다.
# 예를 들어, 단순한 2차원 그래프를 그리는 도구가 필요하면 맷플롯립(`matplotlib`)을,
# 데이터분석을 위한 다양한 도구가 필요하면 넘파이(`numpy`)를 기본적으로 설치해야 한다.
# 제3자 제공 파이썬 패키지를 설치하는 방법은 해당 패키지의 홈페이지를 참고해야 한다.
# 보통은 파이썬을 설치할 때 함께 제공되는 파이썬 패키지 매니저인 pip 명령어를 활용한다.
# 
# 파이썬과 관련된 주요 패키지를 함께 제공하는 앱이나 웹서버 등이 있어서 
# 개인적으로 추가하고 관리하기 어려운 경우 사용할 수 있다.
# 예를 들어, 아나콘다 패키지는 `matplotlib`, `numpy` 등 파이썬 
# 데이터분석과 관련된 다수의 패키지를 함께 제공한다.
# 또한 Repl.it, 구글 코랩 등도 파이썬 기본 이외에 다양한 패키지를 함께 제공한다. 
# 
# 현재 이 노트북을 실행하는 서버 또한 `matplotlib`, `numpy` 등을 포함해서 
# 다양한 제3자 제공 라이브러리가 함께 설치되어 있다. 
# Repl.it 및 구글 코랩에서 문제없이 작동하는 코드만 여기에서 사용한다. 

# ### 제3자 라이브러리 모듈 불러오기

# 예를 들어, 고차원 어레이를 편하게 다룰 수 있도록 도와주는 많은 도구를 담고 있는 넘파이 패키지를 활용하려면
# 아래와 같이 `numpy` 패키지를 불러와야 한다. 그러면 관련된 많은 모듈과 도구들을 활용할 수 있다.

# #### 별칭 사용하기

# 모듈이나 패키지를 불러올 때 별칭을 지정하여 활용할 수 있다.
# 많이 사용되는 모듈이나 패키지는 많은 사람들이 관습적으로 사용하는 별칭이 있다.
# `numpy` 패키지의 경우 보통 `np`로 줄여 부른다.
# 별칭을 사용하는 방식은 다음과 같다.

# In[ ]:


import numpy as np


# 넘파이 패키지에 `random` 모듈이 포함되어 있다. 
# 파이썬에서 기본으로 제공하는 내장 모듈인 `random` 보다 많은 기능을 갖춘 도구들이
# 넘파이 `random` 모듈이 제공한다.
# 
# 앞서 언급했던 파이썬 내장 모듈 `random`에서 정의된 `random` 함수에 해당하는 함수가
# 넘파이 `random` 모듈에 동일한 이름으로 정의되어 있다. 
# 하지만 넘파이 `random` 모듈을 사용하려면 반드시 `np`를 아래와 같이 추가해야 한다.
# 그렇지 않으면 파이썬 내장 모듈과 이름이 혼동되어 문제가 발생할 수 있다.

# In[ ]:


np.random.random()


# In[ ]:


np.random.random()


# 패키지나 모듈을 불러올 때 별칭을 지정하면 반드시 별칭으로 사용해야 한다.
# 그렇지 않으면 오류가 발생한다.

# In[ ]:


numpy.random.random()


# 원래의 패키지 또는 모듈의 이름을 사용하려면 한 번 불러와야 한다.
# 그러면 원래 이름과 별칭 모두 사용할 수 있다.

# In[ ]:


import numpy


# In[ ]:


numpy.random.random()


# In[ ]:


np.random.random()


# ## 사용자 정의 모듈

# 먼저, 아래 코드를 담고 있는 `wc.py` 파일을 먼저 작성한다.
# `wc.py` 파일을 이용하여 사용자가 임의로 작성한 파이썬 코드 파일을 모듈로 활용하는 법을 설명한다.
# 
# **주의:**
# 설명을 위해 `wc.py` 파일이 현재 작업 디렉토리의 하위 디렉토리인 `codes` 디렉토리에 저장되어 있다고 가정한다.
# 
# 파일의 내용은 아래와 같다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/wc1.png" style="width:600px;"></div>

# ### `__init__.py` 파일 작성
# 
# 현재 작업 디렉토리가 아닌 다른 디렉토리에 포함된 모듈을 불러오려면 
# 해당 디렉토리에 `__init__.py` 파일이 생성되어 있어야 한다.
# 따라서 `codes` 라는 하위 디렉토리에 포함된 파일들의 리스를 확인하면 `wc.py` 와 `__init__.py` 
# 두 개의 파일이 포함되어 있어야 한다.
# 
# **주의:** `__init__.py` 파일은 아무 내용이 없는 빈 파일이어도 된다. 다른 용도는 여기서 다루지 않는다.

# #### 현재 작업 디렉토리 확인

# 파이썬 명령어를 이용하여 현재 작업 디렉토리(current working directory, 줄임말: cwd)를
# 확인하는 방법은 다음과 같다.

# In[ ]:


import os
cwd = os.getcwd()
print(cwd)


# 현재 작업 디렉토리에 `codes`라는 디렉토리 포함여부 확인은 다음과 같다.

# In[ ]:


'codes' in os.listdir(cwd)


# `codes` 디렉토리에 포함된 파일들의 리스트 확인하면 `wc.py`와 `__init__.py` 두 파일이
# 포함되어 있음을 볼 수 있다.

# In[ ]:


os.listdir("./codes")


# ### 사용자 정의 모듈 불러오기

# `wc.py` 모듈에 포함되어 있는 `linecount` 함수를 활용하기 위해서
# 먼저 `wc.py` 모듈을 불러와야 한다.

# #### 현재 작업 디렉토리 모듈 불러오기

# 만약 `wc.py` 모듈이 현재 디렉토리에 포함되어 있다면 아래와 같이 불러오면 된다.
# 
# ```
# import wc
# ```
# 
# 또한 `wc.py`에 작성된 코드 마지막 줄을 아래와 같이 작성해야 오류가 발생하지 않는다.
#     
# ```python
# print(linecount('wc.py'))
# ```

# #### 경로 설정 문제

# 그런데 `wc.py` 모듈이 현재 디렉토리의 하위 디렉토리인 `codes` 에 포함되어 있기 때문에 
# 불러오기 과정이 좀 더 복잡하다. 
# 단순히 `import wc` 명령어를 사용하면 모듈을 찾을 수 없다는 오류(`ModuleNotFoundError`)가 발생한다.

# In[ ]:


import wc


# 이와 같이 현재 작업디렉토리가 아닌 곳에 포함된 사용자 정의 모듈은 다른 방식으로 불러와야 한다.
# 다양한 방식이 있지만 여기서는 __라이브러리 경로(library path)__에 특정 디렉토리를 추가하는 방식을 사용한다.
# 
# **주의:** 여기서 라이브러리 경로에 특정 경로를 추가하는 방식은 임시적이다.
# 라이브러리 경로를 영구적으로 변경하려면 다른 방식을 따라야 한다.

# #### 파이썬 라이브러리 경로 확인하기

# 먼저 파이썬이 기본적으로 사용하는 라이브러리들의 경로를 확인해보자.
# `sys.path` 변수에 파이썬이 기본적으로 지원하는 라이브러리들의 경로가 리스트로 저장되어 있다.

# In[ ]:


import sys
sys.path


# #### 파이썬 라이브러리 경로에 임시 경로 추가하기

# `sys.path` 에 저장된 라이브러리들의 경로들의 리스트에 원하는 경로를 추가한다.
# 
# 여기서는 현재 작업디렉토리의 하위 폴더인 `codes`를 경로에 추가하며, 
# 리스트에 항목을 추가하는 `append` 메소드를 활용한다.

# In[ ]:


sys.path.append(cwd + "/codes")


# 이제 새로운 경로가 추가된 것을 확인할 수 있다.

# In[ ]:


sys.path


# #### 라이브러리 경로에 포함된 디렉토리의 모듈 불러오기

# 라이브러리 경로에 포함된 디렉토리의 모듈은 현재 디렉토리에 포함된 모듈을 불러오는 것처럼 하면 된다.

# In[ ]:


import wc


# 이제 `wc`가 누군지를 물으면 아래와 같이 답한다.

# In[ ]:


wc


# 즉, `wc`는 모듈이라는 정보와 `wc.py` 파일이 저장된 위치 정보를 보여준다.

# ### `__name__` 속성과 `__main__` 함수

# #### `__name__` 속성

# 파이썬에서 함수, 클래스, 모듈 등은 `__name__`이라는 특별한 속성을 가지며,
# 항상 자기 자신을 가리킨다.
# 
# 예를 들어, 아래 함수를 살펴보자.

# In[ ]:


def myName():
    pass


# 이제 `myName` 함수의 `__name__` 속성을 확인해보자.
# 속성 확인은 자료형의 메서드를 호출하는 방식과 비슷하다.
# 다만, 속성은 함수가 아니기에 괄호를 사용하지 않는다.

# In[ ]:


myName.__name__


# 모듈도 `__name__` 속성을 갖는다. `wc.py` 모듈의 `__name__` 속성을 확인해보자.

# In[ ]:


wc.__name__


# 앞으로 좀 더 구체적으로 배우게 될 클래스 역시 `__name__` 속성을 갖는다.
# 사실 지금까지 살펴본 모든 자료형 역시 클래스이다. 
# 예를 들어, 사전 자료형의 `__name__` 속성은 아래와 같다.

# In[ ]:


dict.__name__


# #### `__main__` 함수

# `wc.py` 모듈을 임포트할 때 앞서 `os`와 `sys` 모듈을 임포트할 때와는 달리 숫자 `7`을 출력한다.
# 이유는 모듈을 임포트할 때 모듈 안에 포함된 코드가 실행되기 때문인데, 
# `wc.py` 파일의 경우에는 마지막 줄에 있는 아래 명령어가 실행되기 때문이다.
# 
# ```python
# print(linecount('./codes/wc.py'))
# ```
# 
# `linecount` 함수는 인자로 지정된 파일에 포함된 내용의 줄 수(line number)를 계산해서 내준다.
# 따라서 위 명령문은 `wc.py` 파일에 포함된 내용이 몇 줄인가를 확인해준다.
# 
# 그런데 사실 `print(linecount('./codes/wc.py'))` 명령문은 `linecount` 함수가 
# 제대로 작동하는가를 확인하는 용도로 작성된 코드이며, 
# 모듈을 불러와서 활용하기 위해서는 굳이 실행할 필요가 없다.
# 이런 경우에 모듈의 `__name__` 속성을 이용하여 아래와 같이 작성하면 모듈을 임포트할 때 굳이 실행할 필요가 
# 없는 코드를 모듈에 포함시킬 수 있다.
# 
# ```python
# if __name__ == '__main__':
#     print(linecount('./codes/wc.py'))
# ```
# 
# 위와 같이 작성하면 `import wc`를 실행해도 `if __name__ == '__main__':`에 포함된 코드는 실행되지 않는다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/wc5.png" style="width:600px;"></div>

# 반면에 터미널을 이용해서 현재 작업 디렉토리에서  `python codes/wc.py` 형태로 `wc.py` 코드를 직접 실행하면 
# `if __name__ == '__main__'` 조건문의 본체가 실행된다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/wc4.png" style="width:600px;"></div>

# `__main__` 함수의 이런 기능은 C, Java 등에서 의무적으로 사용되는 `main` 함수와 유사한 기능을 수행한다. 
# `Repl.it` 사이트에서 main 모듈이 기본적으로 실행되는 이유가 이런 전통에서 유래한다.

# ### 모듈 다시 불러오기

# 한 번 불러온 모듈을 다시 불러오면 모듈 내용이 또 실행되지는 않는다.

# In[ ]:


import wc


# ### 불러온 모듈 활용하기

# 어떤 종류의 모듈이든 한 번 불러온 모듈을 활용하는 방법은 동일하다.
# 우리가 작성하고 불러온 `wc` 모듈에 포함된 `linecount` 함수를 활용하는 방법도 동일하다.
# 예를 들어, `wc.py` 파일에 포함된 코드의 줄의 수를 알고자 하면 아래와 같이 실행한다.

# In[ ]:


wc.linecount('./codes/wc.py')


# 반면에 `codes` 디렉토리에 포함된 `__init__.py` 파일은 비어있음을 아래와 같이 확인할 수 있다.

# In[ ]:


wc.linecount('./codes/__init__.py')


# ### 별칭 사용

# 패키지나 모듈 또한 종류에 상관없이 별칭을 사용할 수 있다.
# 예를 들어, `wc` 모듈을 `wordCount` 라고 별칭을 지정하면서 불러올 수 있다.

# In[ ]:


import wc as wordCount


# 이제는 `wc` 대신에 `wordCount`를 사용할 수 있다.

# In[ ]:


wordCount.linecount('./codes/wc.py')


# In[ ]:


wordCount.linecount('./codes/__init__.py')


# ## 연습문제 

# 1. `print()` 함수의 성질을 조사한다. 
#     즉, `print()` 함수가 받아들일 수 있는 인자와 리턴값에 대해 알아본다.
#     설명을 예를 들면서 하면 더욱 좋다.
#     `help(print)`를 실행하면 
#     `print()` 함수에 대한 기초적인 정보를 확인할 수 있다.
# 
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
#     * `indent` 매개변수의 옵션인자 값이 `True`이면 연습4에서 처럼 들여쓰기를 하고, 
#         `False`이면 들여쓰기를 하지 않아야 한다.
#     <br><br>
# 1. `printItems` 함수를 재귀가 아닌 `while` 함수를 이용하여 구현하라.
# 
#     **힌트:** `while` 반복문에 사용되는 조건식을 선택하는 게 핵심이다.
#     재귀로 구현된 함수로부터 이에대한 힌트를 얻을 수 있다.
