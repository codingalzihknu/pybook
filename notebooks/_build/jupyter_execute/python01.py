#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기본 자료형 1부

# ## 주요 내용

# * 컴퓨터 프로그램이란?
# * 파이썬 언어 소개
# * 변수와 변수 선언
# * 연산
# * 스칼라 자료형 1편: 정수, 부동소수점, 부울 값, `None`

# ## 컴퓨터 프로그램이란?

# __컴퓨터 프로그램__(computer programs)은 컴퓨터가 해야 할 일을 
# 특정 __프로그래밍 언어__를 이용하여 작성한 __명령문__(commands)으로 이루어진 문장이라 할 수 있다.
# 각각의 명령문이 하는 일은 기본적으로 값을 조작하거나 새로운 값을 생성한다.
# 즉, 컴퓨터 프로그램은 주어진 값을 어떻게 조작하고 어떤 값을 생성할 것인가를 명시한 매뉴얼 문서이다. 
# 
# 언어를 배울 때 어휘와 문장 구성을 배워야 하듯이 컴퓨터 프로그래밍은
# 명령문의 구성 요소와 명령문 사용법을 학습하는 것으로 시작한다.

# ### 프로그램, 코드, 명령문

# 프로그램은 여기서는 컴퓨터 프로그램을 가리킨다. 그리고 경우에 따라 프로그램, 코드, 명령문 등의 표현을 
# 특별한 정의 없이 사용한다.
# 프로그램은 완성된 컴퓨터 프로그램, 코드는 프로그램의 일부, 명령문은 프로그램의 기본 구성요소로 
# 가장 짧은 코드 정도로 이해할 수 있다.
# 반면에 소스코드는 완성된 프로그램의 원본 코드 전체를 의미한다.

# ## 파이썬 언어 소개

# 파이썬은 __스크립트 언어__(script language)다. 즉, 명령문을 작성한 후에 한 줄씩 바로 실행시킬 수 있다.

# ### 명령문 기본 사용법

# 사용되는 파이썬 쉘(shell)에 따라 명령문을 입력하는 장치의 모양이 다르다.
# 보통 명령 프롬프트(prompt)라고 불리는 아래 두 기호 중의 하나가 사용된다.
# 
# * 파이썬 기본 쉘의 명령 프롬프트: `>>>`
# 
# * IPython 명령 프롬프트: `In [17]:`
# 
# 여기서는 IPython 명령 프롬프트를 사용하며, 대괄호 안의 숫자는 실행된 명령문들의 순서를 나타낸다.
# 숫자가 클 수록 나중에 실행되었다는 의미이다.

# #### 명령문 예제: 출력하기

# 아래 코드는 `"Hello Python!"` 이란 문자열을 화면에 출력하는 명령문이다. 

# In[1]:


print("Hello Python!")


# 위 코드는 하나의 명령문으로 구성되었으며 `print()` 함수를 이용한다. 
# 이와같이 함수를 특정 인자와 함께 실행하는 것을 __함수 호출__(function call)이라 한다.
# 
# __참고:__ 큰따옴표 또는 작은따옴표로 감싸인 문자들의 나열을 __문자열__이라 부른다.

# #### 함수(functions)

# __함수__(function)는 지정된 인자를 사용하여 특정 계산과 지정된 기능을 수행한다.
# 프로그래밍에서의 함수와 수학에서의 함수는 사용법과 모양에 있어서 서로 다르지만 
# 기본적으로 지정된 값을 이용하여 계산을 실행한다는 점에서 동일한 개념이다.
# 다만 `print()` 함수가 하는 일에서 보았듯이 수학의 함수와 사용법이 많이 다르기에
# 익숙해지는 데에 조금 시간이 걸릴 수 있다. 
# 
# `print()` 함수는 무언가를 계산하는 것 이외에 지정된 문자열을 화면에 출력하는 일도 수행한다.
# 이처럼 계산 이외에 다른 일을 하는 것을 __부수 효과__(side effect)라고 한다.
# 
# __참고:__ 엄밀히 따지면 이런 작업도 계산이라고 할 수 있지만, 수학자에게는 매우 생소하게 다가올 것이다.
# 부수 효과를 참고서에 따라 __부작용__이라 부르는 경우도 있다.

# #### 명령문 예제: 변수 선언

# __변수__가 특정한 값을 가리키도록 하는 것을 __변수 선언__이라 하며
# 아래 양식을 따른다.
# 
# ```python
# 변수 = 값
# ```
# 
# 예를 들어, 아래 명령문은 2를 변수 `a`가 가리키는 값으로 선언한다.

# In[2]:


a = 2


# 이제 `a`가 가리키는 값을 확인하련 변수를 입력하고 실행하면 된다.

# In[3]:


a


# 변수 선언에 사용되는 등호 기호(`=`) 때문에 `"변수와 값이 동일하다"` 로 이해하면 안된다.
# 여기서는 동일하다의 의미가 아니라 변수가 지정된 값을 가리킨다는 의미이며, 
# 변수라는 말의 의미에서 알 수 있듯이 변수가 가리키는 값은 언제든지 변경될 수 있다.
# 
# 아래 코드는 변수 `a`가 가리키는 값을 5로 변경한다.
# 
# __참고:__ 만약에 `a = 2`를 `a`와 2는 같다라고 해석한다면 절대로 불가능한 일을 하게되는 셈이다.

# In[4]:


a = 5


# 변수가 가리키는 변경된 값을 `print()` 함수를 이용하여 확인할 수도 있다.

# In[5]:


print(a)


# ### 값과 표현식

# 파이썬은 여러 종류의 값을 저장하고 계산할 수 있으며,
# 값을 표현하기 위한 다양한 방식을 지원한다.
# 파이썬은 몇 가지 종류의 값을 기본으로 제공하며, 함수를 이용하여 
# 무한히 많은 값을 표현하고 다룰 수 있는 기능을 제공한다.
# 
# 가장 단순한 값은 정수, 유리수이며, 사칙연산 등을 이용하여 다양한 방식으로 값을 표현할 수 있다.
# 값을 표현하는 식을 __표현식__(expressions)이라 하며,
# 표현식은 명령문이 실행되면 모두 특정 값으로 계산된다.

# #### 예제: 사칙연산 표현식

# 사칙연산을 표현하고 필요에 따라 계산한다.
# 또한 계산된 값을 이용하여 변수를 선언하고 언제든지 필요할 때 재활용할 수 있다.

# In[6]:


2 + 3


# In[7]:


a = 2 + 3
a + 1


# In[8]:


42 - 15.3


# 곱셈은 `*` 기호를 사용한다.

# In[9]:


100 * 11


# 곱셈은 `/` 기호를 사용하며, 실행 결과는 부동소수점이다.
# 
# __참고:__ 컴퓨터에서 구현된 유리수를 __부동소수점__이라 한다.

# In[10]:


7 / 5


# In[11]:


-7/5


# In[12]:


7.0 / 5


# 나눗셈의 몫을 계산하는 연산자는 `//` 이다.

# In[13]:


7//5


# In[14]:


7.0//5


# In[15]:


-7//5


# In[16]:


-7.0//5


# 나눗셈의 나머지를 계산하는 연산자는 `%` 이다.

# In[17]:


7%5


# In[18]:


-7%5


# In[19]:


-7.0%5


# 지수 계산은 `**` 연산자를 사용한다.

# In[20]:


2 ** 3


# In[21]:


9 ** 0.5


# 이제부터 파이썬 프로그램을 구성하는 명령문의 기본 요소를 하나씩 살펴보자.

# ## 변수와 변수 선언

# 값을 저장해 두고 필요할 때 재활용하려면 저장된 값을 특정 이름과 연결시켜주어야 한다.
# 그러면 아무리 크고 복잡한 값이라 하더라고 해당 값을 가리키는 이름으로 간단하게 다룰 수 있다.
# 이렇게 특정 값을 가리키는 이름이 __변수__(variables)이며, 
# 값과 변수를 연결시키는 작업이 __변수 선언__이다.

# ### 변수 이름

# 변수 이름은 아래 세 가지 규칙을 따라야 한다.
# 
# * 영어 알파벳(`a-z,A-Z`), 숫자(`0-9`), 밑줄 기호(`_`)의 임의의 조합
# * 숫자로 시작할 수 없음.
# * 예약어 사용 불가
#     * def
#     * import
#     * from
#     * pass
#     * break
#     * continue
#     * 등등
# * '-', '+', '*','/' 등의 연산자 기호 사용 불가
# * '@', '$', '?', 쉼표, 공백 등 사용 불가

# #### 대소문자 구분

# 변수 이름은 대소문자를 구분한다.
# 예를 들어, 'YOU', 'you', 'You', 'yOu'는 모두 다른 이름으로 처리된다. 

# ### 변수 선언

# __변수__가 특정한 값을 가리키도록 하는 것을 __변수 선언__이라 하며
# 아래 양식을 따른다.
# 
# ```python
# 변수 = 값
# ```
# 
# 예를 들어, 변수 `a_number`는 정수 2를,
# 변수 `a_word`는 `dog`라는 문자열을 가리키도록 하려면 아래와 같이 두 개의 명령문을 작성한다.
# 
# __참고:__ 여러 개의 명령문은 기본적으로 줄바꿈으로 구분된다. 
# 파이썬은 줄바꿈과 들여쓰기가 명령문 작성 문법의 일부이다. 

# In[22]:


a_number = 2
a_word = 'dog'


# 변수가 가리키는 값을 확인하려면 변수 이름을 입력하고 실행하면 된다.

# In[23]:


a_number


# In[24]:


a_word


# `print()` 함수를 이용할 수도 있다.

# In[25]:


print(a_number)


# In[26]:


print(a_word)


# 변수가 가리키는 값을 변경할 수 있다.  

# In[27]:


a_number = 5

a_number


# ### 변수의 자료형

# 파이썬에서 사용되는 모든 값은 특정 __자료형__(data type)에 속한다.
# 지금까지 다룬 값들의 자료형은 다음과 같다. 
# 파이썬에서 기본으로 제공하는 이외에 더 많이 있으며 앞으로 차차 만나게 될 것이다.
# 
# | 자료형 | 예제 |
# |---|---|
# | `int` | 2, 3 등의 정수 |
# | `float` | 1.2, 5.0 등의 유리수 |
# | `str` | `"dog"`, `"python"` 등의 문자열|

# 변수의 자료형은 변수가 가리키는 값의 자료형으로 지정된다.
# 변수의 자료형은 `type()` 함수를 이용하여 확인할 수 있다.

# In[28]:


type(a_number)


# In[29]:


type(a_word)


# 변수가 가리키는 값이 변경되면 변수의 자료형도 함께 변경된다.

# In[30]:


a_number = 5.0


# In[31]:


type(a_number)


# ### 변수 관련 주의사항

# 파이썬 코드를 작성하면 `float`, `int`, `print`, `type`와 같은 단어는 녹색으로 표기된다.
# 이는 그 단어들이 파이썬에서 특별한 역할을 수행하는 함수의 이름이기 때문이다. 
# 그런 함수 이름을 변수로 사용할 수 있지만, 그렇게 되면
# 기존 함수의 정의가 변경될 수 있기 때문에 특별한 이유가 없다면 
# 변수로 사용하지 말아야 한다.
# 
# 예를 들어, 아래 코드는 `print`를 정수 4를 가리키는 변수로 선언한다.
# 
# ```python
# print = 4
# ```
# 
# 그러면 `print()` 함수의 본래 기능이 사라져서 더 이상 사용할 수 없다.

# ## 연산

# 변수를 연산에 직접 사용할 수 있다.

# In[32]:


a_number + 7


# In[33]:


(a_number * 6.0) / 5


# 연산의 결과를 다른 변수에 지정할 수 있다.

# In[34]:


first_result = 8 / 3.5


# 새롭게 선언된 변수는 표현식의 연산 결과를 가리킨다.

# In[35]:


first_result


# ### 문자열 연산

# 두 개의 문자열을 이어붙이거나 지정된 횟수만큼 복제해서 이어붙일 수 있다.
# 사용되는 연산자는 덧셈 기호와 곱셈 기호이다.

# In[36]:


"Bull " + a_word


# In[37]:


a_word * 2


# 반면에 문자열과 숫자의 덧셈은 허용되지 않는다.
# 아래 코드를 실행하면 오류가 발생한다.
# 
# __참고:__ 오류가 발생하면 발생 오류의 정보가 함께 표기된다.
# 일단은 맨 밑줄 앞부분에 있는 `TypeError`가 연산에 사용되는 인자의 자료형이 잘못되었다는 
# 의미라는 정도만 기억하자.

# In[38]:


a_number + a_word


# ### 연산자 우선순위

# 일반적으로 알려진 연산자들 사이의 우선순위가 그대로 사용된다.
# 
# ```python
# 괄호 >> 지수승 >> 곱셈, 나눗셈, 몫, 나머지 >> 덧셈, 뺄셈
# ```

# In[ ]:


2 * 3 - 2


# In[ ]:


(2 * 3) - 2


# In[ ]:


2 * (3 - 2)


# In[ ]:


-2 + 2 * 3


# In[ ]:


-2 + (2 * 3)


# In[ ]:


(-2 + 2) * 3


# In[ ]:


-2 + 4 % 3


# In[ ]:


-2 + (4 % 3)


# In[ ]:


(-2 + 4) % 3


# In[ ]:


.3 + 5 // 2


# In[ ]:


.3 + (5 // 2)


# In[ ]:


(.3 + 5) // 2


# In[ ]:


2 ** 4 // 2


# In[ ]:


(2 ** 4) // 2


# In[ ]:


2 ** (4 // 2)


# 우선순위가 같은 연산자가 연속으로 사용되면 왼편에 위치한 연산자가 먼저 계산된다.

# In[ ]:


2 * 3 % 5


# In[ ]:


(2 * 3) % 5


# In[ ]:


2 * (3 % 5)


# ## 스칼라 자료형 1편

# 파이썬에서 기본으로 제공하는 자료형 중에서 가장 기본적으로 사용되는 자료형 세 개를 소개한다. 
# 
# * 정수(`int`)
# * 부동소수점(`float`)
# * 부울 값(`bool`)
# 
# 세 자료형 모두 단일한 값의 자료형이라는 의미에서 __스칼라__ 자료형이라 부른다.
# 스칼라 자료형 2편에서 문자열, 날짜와 시간 등과 같은 다른 스칼라 자료형을 좀 더 살펴본다.
# 
# __참고:__ 문자열은 언어에 따라 스칼라 자료형이 아닐 수도 있다.
# 예를 들어, C 언어는 문자열을 문자로 이루어진 어레이로 정의되기에
# 스칼라 자료형이라 말하기 어렵다.
# 스칼라 자료형이 아니면서 파이썬에서 기본으로 제공하는 모음 자료형(collections)은 나중에 소개한다.

# ### 정수: `int`

# 일반적으로 알고 있는 정수(자연수, 0, 음의 정수)들의 자료형이며,
# 앞서 살펴보았듯이 덧셈, 뺄셈, 곱셈, 나눗셈 등의 일반 연산이 가능하다.
# 정수 자료형은 `int`로 표기한다.

# In[ ]:


ival = 17239871

ival ** 6  # ival의 6승


# ### 부동소수점: `float`

# 부동소수점(floating-point)은 원래 실수를 컴퓨터에서 다루기 위해 개발되었으나 실제로는 유리수 일부만을 다룬다. 
# 예를 들어, 무리수인 원주율 $\pi$의 경우에도 유한한 값만 다룰 수 있는 
# 컴퓨터 자체의 한계로 인해 소수점 이하 적당한 자리에서 끊어서 사용한다. 

# In[ ]:


pi = 3.141592653589793
pi


# #### 과학 표기법

# 과학 표기법도 사용할 수 있다.

# In[ ]:


fval = 6.78e-5

fval


# #### 부동소수점 연산 주의사항

# 부동소수점 연산은 아래 예제에서 보듯이 매우 조심해야 한다.

# In[ ]:


0.1 + 0.2


# 위와 같은 현상은 파이썬의 한계가 아니라,
# 컴퓨터에서 부동소수점을 다루는 매우 복잡하면서 불완전한 방식 때문에 발생한다.
# 왜 이런 문제가 발생하는가를 이해하는 일은 쉽지 않다.
# 다만, 부동소수점 연산을 매우 조심스럽게 다루어야 한다는 점은 기억해 두어야 한다.
# 여기서는 부동소수점 연산을 거의 다루지 않는다.

# ### 부울 값: `bool`

# 부울 자료형에는 아래 두 개의 값만 포함된다.
# 
# * `True`
# * `False`
# 
# 이 두 개의 값만을 이용하여 복잡한 프로그램을 구현할 수 있다.

# #### 예제
# 
# 강아지를 한 마리만 갖고 있다고 가정하자. 
# 이것을 표현하기 위해 puppy(강아지 한마리)라는 변수에 True를 할당하고, 여러 마리의 강아지를 뜻하는 puppies 변수에는 False를 할당한다.

# In[ ]:


puppy = True

puppy


# In[ ]:


type(puppy)


# In[ ]:


puppies = False


# 두 개의 변수 선언을 아래와 같이 동시에 할 수 있다. 등호기호 왼편과 오른편에 사용되는 변수와 값의 개수가 동일해야 함에 주의한다.

# In[ ]:


puppy, puppies = True, False


# In[ ]:


print("강아지가 있나요?", puppy)
print("여러 마리 강아지인가요?", puppies)


# __주의사항:__ 위에서 사용된 `print()` 함수의 사용법을 기억해둔다. 
# `print()` 함수는 인자를 여러 개 받을 수 있으며 그 값들을 동시에 한 줄에 출력한다. 
# 각각의 값은 공백 문자(space)로 구분된다.

# #### 숫자 비교
# 
# 일반적으로 사용하는 숫자들의 비교를 나타내는 연산자들은 다음과 같다. 결과는 모두 부울 자료형이다.
# 
# * `!=`: 다른지 여부를 판단
# * `==`: 같은지 여부를 판단
# * `<=`: 작거나 같은지 여부를 판단
# * `>=`: 크거나 같은지 여부를 판단
# * `<`: 작은지 여부를 판단
# * `>`: 큰지 여부를 판단

# In[ ]:


4 == 4


# In[ ]:


4 == 5


# In[ ]:


4 != 2


# In[ ]:


4 != 4


# In[ ]:


4 > 2


# In[ ]:


4 > 4


# In[ ]:


4 >= 4


# #### 부울 연산자와 부울 표현식

# `and`, `not`, `or` 세 개의 __부울 연산자__(Boolean operators)를 이용하여 부울 연산을 할 수 있다.
# 각 연산자의 의미는 일반적으로 알려진 것과 동일하다.

# In[ ]:


True and True


# In[ ]:


True and False


# 부울 자료형의 변수와 부울 연산자를 이용하여 다양한 표현식을 정의할 수 있다.
# __부울 표현식__(Boolean expressions)은 부울 값으로 계산되는 표현식을 가리킨다.

# In[ ]:


puppy and puppies


# In[ ]:


not puppies


# In[ ]:


not puppy


# #### 부울 연산자 우선순위

# `not` 연산자의 우선순위가 가장 높고, `and`와 `or`은 동일한 우선순위를 갖는다.
# 따라서 기본적으로 왼편에 위치한 연산자부터 차례대로 계산한다.

# In[ ]:


puppy and not puppies


# In[ ]:


puppy and (not puppies)


# In[ ]:


not puppy and puppies


# In[ ]:


not (puppy and puppies)


# In[ ]:


cat = False


# In[ ]:


cat and puppies or puppy


# In[ ]:


(cat and puppies) or puppy


# In[ ]:


cat and (puppies or puppy)


# #### 부울 값과 `if` 조건문

# 부울 값의 참/거짓 여부에 따라 다른 명령문을 실행하도록 하려면 `if` 조건문을 이용한다.
# 기본 형식은 다음과 같다.
# 
# ```python
# if 부울표현식:
#     명령문1
# else:
#     명령문2
# ``` 
# 
# * 부울표현식이 `True`로 계산될 때: 명령문1 실행
# * 부울표현식이 `False`로 계산될 때: 명령문2 실행

# __주의사항:__ 콜론 기호와 들여쓰기는 의무적으로 지켜야 하며 그렇지 않을 경우
# 오류가 발생하거나 의도와 다른 결과를 얻을 수 있다.

# #### 예제
# 
# 자연수 `n`이 짝수면 `True`를, 홀수면 `False`를 계산하는 코드는 다음과 같다.
# `n`의 값을 변경했을 때 어떤 결과가 나오는지 확인하라.

# In[ ]:


n = 100

if n%2 == 0:
    print(True)
else:
    print(False)


# #### 예제
# 
# 두 숫자 `a`와 `b`의 사이의 거리를 계산하는 코드는 다음과 같다.

# In[ ]:


a = 3
b = 17

if a < b:
    print(b - a)
else:
    print(a - b)


# __참고:__ 위 코드는 사실 두 수의 차이의 절댓값을 계산하며,
# `abs()` 함수가 동일한 기능을 수행한다.

# In[ ]:


abs(a - b)


# In[ ]:


abs(b - a)


# __참고:__ `if` 조건문의 보다 다양한 활용법은 나중에 자세히 다룬다.

# ### `None` 값

# `None`은 어떤 의미도 없는 값, 소위 널(null)값이며, 
# 문법적으로 `NoneType` 자료형의 유일한 값이다. 

# In[ ]:


type(None)


# In[ ]:


a = None


# In[ ]:


a is None


# In[ ]:


b = 5


# In[ ]:


b is not None


# #### `None`을 반환하는 함수

# 함수 중에 반환값이 `None` 인 경우가 많이 있다.
# 대표적으로 `print()` 함수가 아무 것도 반환하지 않는다.
# 즉, 화면에 출력되는 문자열은 `print()` 함수의 반환값이 아니라, 
# 추가 기능의 결과, 즉 부수 효과이다.

# In[ ]:


none_value = print("파이썬이 좋아요!")


# In[ ]:


none_value


# In[ ]:


none_value == None


# ### 형변환

# 아래 세 함수는 인자로 들어온 값을 각각 정수, 부동소수점, 부울 자료형의 값으로 변환한다.
# 단, 세 함후 모두 인자로 사용되는 값에 따라 오류를 발생시킬 수 있다.
# 
# * `int()`
# * `float()`
# * `bool()`
# 

# __주의사항:__ 자료형과 형변환 함수의 이름이 동일하다.
# 예를 들어, `int`는 정수 자료형과 정수 자료형으로 형변환하는 함수를 동시에 가리킨다.
# 따라서 여기서는 함수는 항상 소괄호와 함께 표기한다.
# 즉, `int`는 정수 자료형을, `int()`는 정수로 형변환하는 함수를 가리킨다.

# #### `int()` 함수

# 정수와 실수 사이에 강제로 자료형을 변환시킬 수 있다.
# 실수를 정수로 변환하고자 할 경우 `int()` 함수를 사용한다. 
# 그러면 소수점 이하는 버려진다. 

# In[ ]:


int(4.8)


# 정수 모양의 문자열을 진짜 정수로 형변환시킬 수 있다.

# In[ ]:


an_int = int('238')
an_int


# In[ ]:


type(an_int)


# 정수 모양의 문자열이 아니면 오류가 발생한다.

# In[ ]:


an_int = int('238.0')
an_int


# #### `float()` 함수

# 정수를 실수로 형변환하려면 `float()` 함수를 사용한다.

# In[ ]:


float(2)


# 변수를 대상으로 형변환을 하면 변수가 가리키는 값 자체가 변하는 것은 아니다.

# In[ ]:


an_int = 2

float(an_int)


# In[ ]:


an_int


#  다만, 형변환된 값을 다른 변수에 저장해서 활용할 수는 있다.

# In[ ]:


a_float = float(an_int)

a_float


# 부동소수점 모양의 문자열을 진짜 부동소수점으로 형변환시킬 수 있다.

# In[ ]:


a_float = float('2.38')
a_float


# In[ ]:


type(a_float)


# 부동소수점

# In[ ]:


a_float = float('238f0')
a_float


# #### `bool()` 함수

# `bool()` 함수는 0처럼 없거나 비어있다는 의미를 가리키는 값에 대해서만 `False`를 반환한다.

# In[ ]:


bool(0)


# In[ ]:


bool(1.2)


# In[ ]:


bool(-21.7)


# ## 연습문제

# ### 연습 

# 두 숫자의 평균값을 구하는 코드는 다음과 같다.
# 예를 들어, 234와 453의 평균값은 343.5이다.
# 두 변수 `a`, `b`의 값을 변경하면서 여러 번 실행하라.

# In[ ]:


a = 234
b = 453

mean_a_b = (a + b) / 2

print(mean_a_b)


# ### 연습
# 
# 반지름이 `r`인 원의 넓이를 계산하는 코드는 다음과 같다.
# 단, 원주율은 3.14로 계산한다.

# 견본답안:

# In[ ]:


r = 3

pi = 3.14
circle_area = pi * r ** 2

print(circle_area)


# ### 연습
# 
# 변의 길이가 각각 `a`, `b`, `c`인 삼각형의 면적 `A`는 아래 식으로 계산된다.
# 
# $$
# A = \sqrt{s  (s - a)  (s - b)  (s - c)}
# $$
# 
# 단, 
# $$
# s = (a + b + c) / 2
# $$
# __참고:__ [위키백과: 삼각형](https://ko.wikipedia.org/wiki/%EC%82%BC%EA%B0%81%ED%98%95)

# In[ ]:


a = 2
b = 2
c = 3

s = (a + b + c) / 2.0
A = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # 0.5승은 제곱근에 해당함

print(A)

