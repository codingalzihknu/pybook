#!/usr/bin/env python
# coding: utf-8

# # 사례 연구: 함수 인터페이스

# `turtle` 모듈을 이용하여 다양한 그림을 그리는 함수를 직접 구현하면서
# 반복문과 함수의 활용을 좀 더 자세히 살펴본다.
# 또한 클래스, 인스턴스, 메서드 등을 활용하는 객체 지향 프로그래밍(OOP)의
# 기본 구성 요소를 소개한다.

# ## `turtle` 모듈

# `turtle` 모듈은 간단한 그림을 그리는 다양한 도구를 제공하며, 
# 파이썬에 기본 모듈로 포함되어 있다. 
# [IDLE 를 이용](https://aisw.tistory.com/5)하여 아래 명령문을 실행하면 그림 창이 하나 새로 나타나고 
# 그 안에 정해진 그림이 그려져야 한다.

# ```python
# import turtle
# 
# wn = turtle.Screen()      # 캔버스 하나 생성
# bob = turtle.Turtle()    # bob 란 이름의 거북이 하나 생성. 기본 모양은 화살촉
# 
# bob.forward(150)         # 바라보는 방향으로 150 픽셀 전진
# bob.left(90)             # 왼쪽으로 90도 회전
# bob.forward(75)          # 바라보는 방향으로 75 픽셀 전진
# 
# wn.exitonclick()          # 캔버스에 클릭할 때까지 대기
# # wn.mainloop()             # X 버튼을 눌러 창을 닫을 때까지 대기
# ```

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/turtle01.png" width="300"/></div>

# :::{admonition} Trinket 사이트
# :class: info
# 
# 반면에 구글 코랩 등 대부분의 온라인 사이트에서는 지원되지 않는다. 
# 하지만 다행히도 [트링킷<font size="2">Trinket</font>](https://trinket.io)이 거북이 그래픽스를 지원한다.
# :::

# **캔버스와 거북이 객체**
# 
# `turtle.Screen()` 은 `Screen` 클래스의 인스턴스, 즉 캔버스 객체를 하나 생성한다.
# 단, 캔버스 객체는 하나만 생성할 수 있다. 
# 이렇게 하나의 인스턴스만 허용하는 클래스를 **싱글톤 클래스**<font size='2'>singleton class</font>라 한다.
# 
# 반면에 `Turtle` 클래스를 포함하여 파이썬의 클래스는 일반적으로 임의의 개수의 인스턴스 생성을 허용한다.

# **거북이 메서드**
# 
# 거북이를 움직이게 하거나 거북이의 상태를 지정하는 많은 
# [`Turtle` 클래스의 메서드](https://docs.python.org/3/library/turtle.html)가 존재한다.
# 그중 일부는 단축어를 갖는데 가장 많이 사용되는 메서는 다음과 같다.
# 
# | 메서드 | 단축어 | 의미 |
# | :---   | :---   | :--- |
# | forward() | fd()    | 전진 |
# | left()   | lt()     | 반시계방향 회전 |
# | backward() | bd()   | 후진 |
# | right()  | rt()     | 시계방향 회전 |
# | pendown() | pd()/down() | 펜 내리기 |
# | penup() | pu()/up() | 펜 들기 |
# | showturtle() | st() | 거북이 보이기 |
# | hideturtle() | ht() | 거북이 숨기기 |
# 
# 

# ## 단순 반복

# 아래 명령문은 정사각형을 그린다.
# 
# ```python
# bob.fd(100)
# bob.lt(90)
# 
# bob.fd(100)
# bob.lt(90)
# 
# bob.fd(100)
# bob.lt(90)
# 
# bob.fd(100)
# bob.lt(90)
# ```

# 하지만 다음과 같이 `for` 반복문을 이용하면 보다 효율적인 코드를 얻는다.
# 
# ```python
# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
# ```

# ## 캡슐화와 일반화

# 프로그램을 구현에 가장 필수적인 요소는 
# **캡슐화**<font size="2">encapsulation</font>와 
# **일반화**<font size="2">generalization</font>이다.
# 
# 1. 함수를 사용하지 않는 간단한 프로그램 작성
# 1. (캡슐화) 작성한 프로그램이 잘 작동하면 변수에 의존하지 않는 부분을 함수로 감싸 하나의 캡슐처럼 만든다.
# 1. (일반화) 함수에 적절한 매개변수<font size='2'>parameter</font>를 
#     추가하여 함수가 보다 다양한 기능을 갖도록 한다.
# 1. 원하는 수준의 함수를 얻을 때까지 위 과정을 반복한다.
# 1. (리팩토링) 프로그램에서 중복되는 부분을 캡슐화하여 함수로 만들 수 있는지 잘 살펴본다.

# 앞서 다룬 코드에서 출발하여 캡슐화와 일반화를 연습한다. 

# ### 캡슐화

# 거북이를 지정해서 사각형을 그리도록 하는 함수는 다음과 같다.
# 
# ```python
# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
# ```
# 
# 그러면 `square()` 함수를 `bob` 과 함께 호출하면 `bob` 지정된 크기의 정사각형을 그린다.
# 
# ```
# square(bob)
# ```

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/turtle02.png" width="300"/></div>

# 다른 거북이를 지정하면 해당 거북이가 정사각형을 그린다.
# 
# ```python
# alice = turtle.Turtle()
# square(alice)
# ```

# ### 일반화

# **길이 매개변수 추가**
# 
# 정사각형의 길이를 지정할 수 있도록 하기위해 `length` 매개변수를 추가한다.
# 위 함수와 다른 점은 한 변의 길이를 나타냈던 100 대신에 `length` 매개변수를 사용한다는 것 뿐이다.
# 
# ```python
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
# ```
# 
# 그러면 다양한 크기의 정사각형을 그릴 수 있다.
# 
# ```python
# square(bob, 100)
# square(bob, 50)
# ```

# **다각형 그리기**
# 
# 다각형을 그리는 함수는 거북이와 길이를 지정하는 매개변수 이외의 몇 각형인가를 결정하는
# 매개변수도 필요하다.
# 다음 `polygon()` 함수가 `square()` 함수를 일반화한다.

# ```python
# def polygon(t, n, length):
#     angle = 360 / n
# 
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# ```
# 
# 다음은 정7각형을 그린다.
# 
# ```python
# polygon(bob, 7, 70)
# ```

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/turtle03.png" width="300"/></div>

# **키워드 인자 활용**
# 
# 만약에 기본적으로 한 변의 길이가 70인 정7각을 그리고 경우에 따라 다른 값을 사용하고자 한다면
# `n=7` 과 `length=70` 을 키워드 인자로 지정하면 된다.
# 
# ```python
# def polygon(t, n=7, length=70):
#     angle = 360 / n
# 
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# ```
# 
# 그러면 `n` 과 `length` 에 대한 값을 지정하지 않아도 동일한 정7각형을 얻는다.
# 
# ```python
# polygon(bob)
# ```

# ## 함수의 인터페이스

# 함수의 인터페이스는 함수 사용법의 요약문이다. 
# 
# - 어떤 매개변수 사용?
# - 함수가 하는 일은?
# - 함수의 반환값은?
# 
# 사용자가 함수를 적절하게 사용하기 위해 전혀 불편함이 없도록 인터페이스를 구현해야 한다.

# 예를 들어, 반지름이 주어졌을 때 지정된 거북이가 원을 그리는 `circle()` 함수를 다음과 같이 구현할 수 있다.
# 거북이는 원둘레를 50등분한 길이로 이루어진 다각형으로 표현한다.
# 다각형은 `polygon()` 함수를 이용하여 그린다.
# 
# ```python
# import math
# 
# def circle(t, r):
#     circumference = 2 * math.pi * r  # 원둘레의 길이
#     
#     n = 50                           # 50-각형 그리기
#     length = circumference / n       # 50-각형의 한 변의 길이
#     
#     polygon(t, n, length)            # 다각형 그리기
# ```

# 반지름이 200 픽셀인 원은 다음과 같다.
# 
# ```python
# circle(bob, 200)
# ```

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/turtle04.png" width="300"/></div>

# 원을 매우 큰 n 을 이용하여 n-각형으로 표현한다.
# 다만 위 코드에서는 n=50 을 사용하며, 
# n-각형 한 변의 길이를 원둘레를 50 등분한 값으로 지정한다.
# 하지만 이렇게 하면 n-각형의 한 변의 길이가 반지름이 큰 원에 대해서는 너무 크고,
# 작은 원에 대해서는 너무 작다.
# 
# n 을 함수의 매개변수로 지정하여 따로 입력받게할 수도 있지만
# 그보다는 다각형의 변의 개수를 반지름에 의존하게 하고,
# n-각형의 한 변의 길이는 3 정도로 제한하는 게 보다 좋다.
# 3픽셀은 부드러운 곡선을 갖는 원을 그리는 데 충분히 작으면서
# 동시에 원을 효율적으로 그리는데 적절하다.
# 
# 아래 코드에 사용된 `circumference / n` 약 3 정도의 값을 갖는다.
# 또한 n 값에 사용된 `+3`은 최소 3각형을 그리도록 보장하기 위함이다.

# ```python
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     
#     n = int(circumference / 3) + 3  # 원둘레의 1/3 정도에 해당하는 선분 수
#     length = circumference / n      # 약 3 정도의 값
#     
#     polygon(t, n, length)
# ```

# ## 리팩토링

# 프로그램을 개선하기 위해 코드를 재배치 하거나 재구성 하는 기법이 
# **리팩토링**<font size='2'>refactoring</font>이다. 
# 
# 프로젝트를 시작할 때 모든 것을 고려할 수 있다면 처음부터 모든 상황에 유연하게
# 대처하는 프로그램을 작성할 수 있을 것이다.
# 하지만 일반적으로는 그렇게 일이 진행되지는 못한다.
# 따라서 문제에 대한 이해가 깊어지면서 처음에 구현된 프로그램을 개선하기 위해
# 리팩토링을 진행하게 된다. 
# 
# 여기서는 `circle()` 함수를 리팩토링 과정을 통해 원의 호<font size='2'>arc</font>를
# 그리는 함수를 구현환다. 
# 
# 먼저 `circle()` 함수의 본문에 `polygon()` 함수가 사용됨에 주의한다.
# 이유는 다각형은 원의 호를 그리는 데에 별로 도움되지 않기 때문이다.
# 즉, `circle()` 과 `polygon()` 을 원의 호를 그리는 데에 사용할 수 없다. 

# 원의 호는 원의 일부이다.
# 따라서 원의 둘레를 그리는 과정을 호의 크기에 맞춰 멈추도록 해야 하며,
# 이 방식으로 `circle()` 함수를 수정하면 
# 다음 `arc()` 함수를 얻는다.
# `angle` 매개변수는 호와 두 지름으로 구성된 부채꼴의 중심각을 입력받는다.
# 
# ```python
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1   # 호의 길이의 1/3 에 해당
#     step_length = arc_length / n  # 선분의 길이
#     step_angle = angle / n        # 호의 중심각의 1/n 에 해당
#     
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)
# ```

# `arc()` 함수의 본체에 사용된 `for` 반복문은 
# `polygon()` 함수의 본체와 매우 닮았다.
# 차이점은 `n` 이 호의 길이, 즉 중심각에 의존한다는 점 뿐이다. 
# 
# 이 점에 착안하여 아래 폴리라인 함수 `polyline()` 를 구현한다.
# 
# ```python
# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# ```

# 이제 `arc()` 함수와 `polygon()` 함수 모두 `polyline` 함수를 이용하여 다시 구현할 수 있다.
# 
# ```python
# def polygon(t, n, length):
#     angle = 360.0 / n
# 
#     polyline(t, n, length, angle)  # 360 도를 n 등분하여 n 번 회전하면 360도 회전함
# 
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     
#     polyline(t, n, step_length, step_angle)
# ```

# `circle()` 함수는 `arc()` 함수의 특별한 경우이다.
# 
# ```python
# def circle(t, r):
#     arc(t, r, 360)
# ```

# ## 문서화 문자열

# 함수의 인터페이스를 설명하는 주석을 **문서화 문자열**, 
# 영어로는 독스트링<font size='2'>docstring</font>이라 한다.
# 문서화 문자열은 함수의 본체가 시작되기 전에 세 개의 큰 따옴표로 감싼 주석으로 작성된다.

# ```python
# def polyline(t, n, length, angle):
#     """t: 거북이 객체
#     n: 선분 그리기 반복 횟수
#     length: 선분의 길이
#     angle: 회전 각도. 즉, 두 선분 사이의 각도
#     
#     지정된 크기와 각도를 이용하여 거북이 t 가 n 개의 선분을 그린다.
#     """    
# 
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# ```

# 문서화 문자열은 함수의 정보를 확인하는 데에 사용된다.
# 
# ```python
# >>> help(polyline)
# ```
# 
# ```python
# t: 거북이 객체
# n: 선분 그리기 반복 횟수
# length: 선분의 길이
# angle: 회전 각도. 즉, 두 선분 사이의 각도
# 
# 지정된 크기와 각도를 이용하여 거북이 t 가 n 개의 선분을 그린다.
# ```

# ## 사전조건 대 사후조건

# 함수를 호출하려면 적절한 인자를 사용해야 하며,
# 그렇지 않으면 실행중에 오류가 발생한다.
# 예를 들어, `arc()` 함수의 `t` 매개변수에는 거북이 객체를,
# `n` 은 양의 정수,
# `length` 와 `angle` 은 양수 이어야 한다.
# 
# 이런 조건들이 `arc()` 함수의 **사전 조건**<font size='2'>pre-condition</font>이다.
# 즉, 선조건이 만족되게 하는 인자들을 사용해야만 함수가 제대로 실행된다.
# 반면에 함수의 실행이 끝나면 만족해야 하는 조건은 **사후 조건**<font size='2'>post-condition</font>이다.
# 
# 만약에 사전 조건을 충족하는 인자가 사용되었지만 사후 조건이 성립하지 않는 결과를 얻게 된다면,
# 함수가 제대로 구현되지 않았음을 의미한다.

# ## 연습 문제

# 참고: [(실습) 사례 연구: 함수 인터페이스](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-casestudy_function_interfaces.ipynb)
