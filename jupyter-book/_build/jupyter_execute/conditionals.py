#!/usr/bin/env python
# coding: utf-8

# # 조건문

# **조건문**<font size="2">conditional statement</font>은
# 특정 조건의 성립여부에 따라 다른 일을 하게 만드는 명령문이다.
# 조건문의 가장 간단한 형식은 다음과 같다.
# 
# ```python
# if x < 0:
#     print('x는 음수')
# ```
# 
# 위 조건문이 실행되는 순간 변수 `x`가 가리키는 값이 0보다 작으면 `'x는 음수'` 
# 라는 문장을 출력하고, 그렇지 않으면 다음 명령문으로 넘어간다. 
# 
# 조건문의 헤더<font size="2">header</font>는 
# `if` 키워드와 **조건**<font size="2">condition</font>으로 구성된다.
# 조건은 참 또는 거짓을 가리키는 **논리식**({numref}`%s절 <sec:boolean_expression>`)으로
# 표현되며
# 조건이 참일 때 조건문의 본문이 실행된다.
# 
# ```python
# if 조건식:
#     명령문
# ```

# **슬라이드**

# 본문 내용을 요약한 [슬라이드](https://github.com/codingalzi/pybook/raw/master/slides/slides-conditionals.pdf)를 
# 다운로드할 수 있다.

# ## `if-else` 조건문

# 변수 `x`가 가리키는 값이 음수가 아닐 때에는 음수가 아니다 라는 내용도 출력하는
# 기능을 추가하려면 다음과 같이 조건문을 작성한다.

# In[1]:


from random import randint

x = randint(-5, 5)

if x < 0:
    print('x는 음수')
else:
    print('x는 음수 아님!')


# 이처럼 조건 제어문의 일반적인 형식은 다음과 같다.
# 
# ```python
# if 조건식:
#     명령문1
# else:
#     명령문2
# ```
# 
# - `명령문1`: 조건식이 참일 때 실행
# - `명령문2`: 조건식이 거짓일 때 실행

# ## 조건부 표현식

# `if-else` 조건문을 이용하여 값을 표현할 수 있으며 조건부 표현식이라 한다.
# 조건부 표현식의 형식은 다음과 같다.

# ```python
# 표현식1 if 조건식 else 표현식2
# ```

# 예를 들어, 아래 함수 `my_abs()`는 절댓값을 계산한다.
# 즉, 음수가 들어어면 양수로 변환해서, 양수는 그대로 반환한다.

# In[2]:


def my_abs(x):
    absolute = -x  if x < 0 else x
    return absolute


# In[3]:


my_abs(-2)


# In[4]:


my_abs(17)


# ## `elif` 키워드

# 세 개 이상의 경우를 다루고자 할 경우
# 다음과 같은 형식을 사용한다.

# In[5]:


x = randint(-5, 5)
y = randint(-5, 5)

if x < y:
    print('x가 y보다 작다')
elif x > y:
    print('x가 y보다 크다')
else:
    print('x와 y가 같다')


# `elif`는 영어의 ''else if''의 줄임말이며,
# 임의로 많이 사용될 수 있고,
# `else` 는 생략될 수 있지만 사용된다면 항상 마지막에 위치해야 한다.
# `if`와 `elif` 문에 사용된 조건은 위에서 차례대로 확인되어
# 참이되는 경우의 명령문이 실행되며 나머지 경우는 무조건 무시된다.

# 예를 들어 `y`를 5로 나눈 나머지에 따라 다른 명령문을 다음과 같이 지정할 수 있다.

# In[6]:


x = randint(-5, 5)
y = randint(-5, 5)

x = y % 5

if x == 0:
    print('나머지가 0')
elif x == 1:
    print('나머지가 1')
elif x == 2:
    print('나머지가 2')
elif x == 3:
    print('나머지가 3')
else:
    print('나머지가 4')


# `else`를 사용하지 않을 수도 있다.

# In[7]:


x = randint(-5, 5)
y = randint(-5, 5)

x = y % 5

if x == 0:
    print('나머지가 0')
elif x == 1:
    print('나머지가 1')
elif x == 2:
    print('나머지가 2')
elif x == 3:
    print('나머지가 3')
elif x == 4:
    print('나머지가 4')


# ## 중첩 조건문

# `elif` 키워드는 사실 없어도 된다.
# 예를 들어 크거나, 작거나, 같은 세 가지 경우를 다음과 같이 다룰 수 있다.

# In[8]:


x = randint(-5, 5)
y = randint(-5, 5)

if x < y:
    print('x가 y보다 작다')
else:
    if x > y:
        print('x가 y보다 크다')
    else:
        print('x와 y가 같다')


# 위와 같이 `if-else` 조건문을 중첩해서 사용하면
# 원하는 대로 경우를 나누어서 처리할 수 있다.
# 경우의 확인 순서는 바깥 쪽에 위치한 경우부터 시작해서
# 점차 `else` 문 안쪽으로 진행한다.
# 
# 일반적으로 3번 이상의 중첩을 사용하는 것은 권장되지 않는다.
# 이유는 경우의 구분이 너무 복잡해질 수 있기 때문이다.
# 가능하면 중첩 조건문 대신에 `elif` 문을 활용할 것이 권장된다.

# ## 논리연산자와 중첩 조건문

# 논리 연산자를 활용하여 중첩 조건문의 활용을 피할 수도 있다.
# 
# 아래 코드는 중첩 조건문을 사용하여 `x`가 0보다 크면서 동시에 10보다 작은 경우를 다룬다.

# In[9]:


x = randint(-5, 5)

if 0 < x:
    if x < 10:
        print('x가 0보다 크고 동시에 10보다 작은 경우')


# `print()` 함수가 `0 < x`와 `x < 10` 두 조건을 모두 만족하는 경우에만
# 실행되기에 아래와 같이 `and` 연산자를 이용하면 굳이 조건문을 
# 중첩으로 사용할 필요가 없다. 

# In[10]:


x = randint(-5, 5)

if 0 < x and x < 10:
    print('x가 0보다 크고 동시에 10보다 작은 경우')


# 참고로 `0 < x and x < 10` 을 `0 < x < 10`로 표현할 수 있다.

# In[11]:


x = randint(-5, 5)

if 0 < x < 10:
    print('x가 0보다 크고 동시에 10보다 작은 경우')


# ## 연습문제 

# 참고: [(실습) 조건문](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-conditionals.ipynb)
