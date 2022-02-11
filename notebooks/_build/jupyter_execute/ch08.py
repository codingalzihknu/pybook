#!/usr/bin/env python
# coding: utf-8

# # 재귀

# 재귀란 ...

# ## 재귀함수

# 봉 감독의 영화(Movies by Bong, moBong)를 담고 있는 리스트가 아래와 같이 있다.

# In[1]:


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

# In[2]:


for item in moBong:
    print(item)


# 그런데 위와 같이 하면 중첩으로 되어 있는 영화들을 제대로 풀어헤칠 수 없다.
# 2중 `for` 반복문을 활용해보자.
# 
# **주의:** 아래 코드에서 `isinstance(item, list)`는 `item` 변수가 가리키는 항목이 
# 리스트 자료형 여부를 확인한다.

# In[3]:


for item in moBong:
    if isinstance(item, list):
        for itemN in item:
            print(itemN)
    else:
        print(item)


# 여전히 삼중 리스트의 모든 항목을 나열하진 못한다. 
# 3중 `for` 반복문을 활용해보자.

# In[4]:


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

# In[5]:


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

# In[6]:


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

# In[7]:


def collatzWhile(num):
    count = 0
    while (num != 1):
        if num%2 == 0:
            num = num//2
        else:
            num = num*3+1
        count = count+1
    return count


# In[8]:


collatzWhile(7)


# In[9]:


collatzWhile(128)


# In[10]:


collatzWhile(129)


# 반면에 재귀를 이용할 경우 아래와 같이 구현한다.

# In[11]:


def collatz_(num):
    if num == 1:
        return 0
    elif num%2 == 0:
        return collatz_(num//2) + 1
    else:
        return collatz_(num*3 + 1) + 1


# In[12]:


collatz_(7)


# In[13]:


collatz_(128)


# In[14]:


collatz_(129)


# 반복되는 과정을 보고 싶으면 반복될 때마다 숫자를 출력하면 된다.

# In[15]:


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


# In[16]:


collatzWhile_(7)


# In[17]:


collatzWhile_(128)


# In[18]:


collatzWhile_(129)


# In[19]:


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


# In[20]:


collatz(7)


# In[21]:


collatz(128)


# In[22]:


collatz(129)


# ## 재귀 함수 호출과 스택 다이어그램

# 재귀함수의 실행과정 동안 많은 프레임의 생성과 소멸이 발생한다.
# 스택 다이어그램의 변화가 경우에 따라 매우 복잡해지기도 한다.
# 
# 예를 들어,
# [PythonTutor: 콜라츠 추측](http://pythontutor.com/visualize.html#code=def%20collatz%28num%29%3A%0A%20%20%20%20if%20num%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20print%28num%29%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20elif%20num%252%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20print%28num,%20end%3D',%20'%29%0A%20%20%20%20%20%20%20%20return%20collatz%28num//2%29%20%2B%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28num,%20end%3D',%20'%29%0A%20%20%20%20%20%20%20%20return%20collatz%28num*3%20%2B%201%29%20%2B%201%0A%20%20%20%20%20%20%20%20%0Acollatz%287%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에서
# 재귀함수 호출 과정 동안 메모리에서 벌어지는 프레임의 생성과 소멸 과정,
# 즉, 스택 다이어그램의 변화를 살펴볼 수 있다.

# ## 연습문제 

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
