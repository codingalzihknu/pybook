#!/usr/bin/env python
# coding: utf-8

# # 모음 자료형

# (sec:string)=
# ## 문자열

# (sec:list)=
# ## 리스트

# - 변수 재할당을 다시 한 번 설명할 것.
#     - {numref}`%s절 <sec:variable_reassignment>` 참고
#     - 아래 코드 참고
#     
#         ```python
#         >>> x = [0, 1, 2]
#         >>> y = x
#         >>> x[0] = 5
#         >>> y[0]
#         5
#         ```

# ### 영화 감독 봉준호

# 봉준호 영화 감독의 영화를 담고 있는 리스트가 아래와 같이 있다.

# In[1]:


movie_Bong = ["기생충", 2019, ["설국열차", 2013, ["살인의 추억", 2003]]]


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

# In[2]:


for item in movie_Bong:
    print(item)


# 그런데 위와 같이 하면 중첩으로 되어 있는 영화들을 제대로 풀어헤칠 수 없다.
# 2중 `for` 반복문을 활용해보자.
# 
# **주의:** 아래 코드에서 `isinstance(item, list)`는 `item` 변수가 가리키는 항목이 
# 리스트 자료형 여부를 확인한다.

# In[3]:


for item in movie_Bong:
    if isinstance(item, list):
        for itemN in item:
            print(itemN)
    else:
        print(item)


# 여전히 삼중 리스트의 모든 항목을 나열하진 못한다. 
# 3중 `for` 반복문을 활용해보자.

# In[4]:


for item in movie_Bong:
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


printItems(movie_Bong)


# ## 튜플

# ## 사전

# ## 집합

# ## 조건제시법

# ## 연습문제 

# 1. `printItems` 수정하여 `movie_Bong`에 포함된 항목들을 아래와 같이 
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
#         그러면 `printItems2(movie_Bong, 0)`을 실행하면 원하는 결과가 나와야 한다.
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
