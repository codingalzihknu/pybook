#!/usr/bin/env python
# coding: utf-8

# # 반복문

# 특정 명령문을 반복<font size="2">iteration</font> 실행하는 장치인 
# 반복문<font size="2">loop statement</font>을 소개한다.
# 파이썬은 세 종류의 반복문을 제공한다. 
# 
# - 재귀
# - `for` 반복문
# - `while` 반복문
# 
# 이 중에 재귀는 {numref}`%s장 <ch:recursion>`에서,
# `for` 반복문의 간단한 활용법은 {numref}`%s절(?) <sec:for_loop>` 에서 살펴보았다.
# 여기서는 `while` 반복문을 소개한다.
# `while` 반복문의 작동 과정을 이해하려면 먼저 변수가 가리키는 값을 변경하는 변수 재할당과
# 변수 업데이트를 이해해야 한다. 
# 
# 
# **`for` 반복문과 데이터분석 예제 추가!**

# ## 변수 재할당과 변수 업데이트

# 변수 재할당<font size="2">variable reassignment</font>은
# 변수가 가리키는 값은 변경하는 것이다.
# 예를 들어 아래 코드는 변수 `x`가 가리키는 값을 5에서 7로 재할당한다.
# 반면에 변수 `y`는 계속해서 5를 가리킨다.
# 
# ```python
# >>> x = 5
# >>> y = x
# >>> x = 7
# >>> x + y
# 12
# ```

# 반복문의 핵심은 특정 변수가 가리키는 이전에 가리키던 값을 이용하여 생성된 다른 값으로 재할당하는
# 하는 것이며, 이를 
# **변수 없데이트**<font size="2">variable update</font>라 한다. 
# 대표적으로 아래와 같은 표현식이 많이 사용된다.
# 
# ```python
# >>> x = x + 1
# ```
# 
# 위 할당문은 변수 `x`가 가리키던 값에 1을 더한 값을 다시 
# 변수 `x`에 할당하라고 명령한다. 
# 만약에 변수 `x` 가 0을 가리키고 있었다면 위 명령문이 반복 실행될 때마다
# `x`가 가리키는 값은 1, 2, 3 등으로 계속해서 변한다.
# 
# 반면에 아래 명령문은 변수 `x`가 가리키는 값을 
# 1만큼 줄여서 재할당한다.
# 
# ```python
# >>> x = x - 1
# ```
# 
# 반복문의 핵심중의 하나가 바로 변수 업데이트이다. 

# ## while 반복문

# 동일한 작업을 반복....

# ## for 반복문
