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
# 
# bob = turtle.Turtle()    # bob 란 이름의 거북이 하나 생성. 기본 모양은 화살촉
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

# ## 캡슐화

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

# ## 일반화

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
#     n = 50
#     length = circumference / n       # 다각형의 길이
#     
#     polygon(t, n, length)            # 다각형 그리기
# ```

# 반지름이 200 픽셀인 원은 다음과 같다.
# 
# ```python
# circle(bob, 200)
# ```

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/turtle04.png" width="300"/></div>

# The first line computes the circumference of a circle with radius r using the formula 2 π r. Since we use math.pi, we have to import math. By convention, import statements are usually at the beginning of the script.
# 
# n is the number of line segments in our approximation of a circle, so length is the length of each segment. Thus, polygon draws a 50-sided polygon that approximates a circle with radius r.
# 
# One limitation of this solution is that n is a constant, which means that for very big circles, the line segments are too long, and for small circles, we waste time drawing very small segments. One solution would be to generalize the function by taking n as a parameter. This would give the user (whoever calls circle) more control, but the interface would be less clean.

# The interface of a function is a summary of how it is used: what are the parameters? What does the function do? And what is the return value? An interface is “clean” if it allows the caller to do what they want without dealing with unnecessary details.
# 
# In this example, r belongs in the interface because it specifies the circle to be drawn. n is less appropriate because it pertains to the details of how the circle should be rendered.
# 
# Rather than clutter up the interface, it is better to choose an appropriate value of n depending on circumference:

# ```python
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 3
#     length = circumference / n
#     polygon(t, n, length)
# ```

# Now the number of segments is an integer near circumference/3, so the length of each segment is approximately 3, which is small enough that the circles look good, but big enough to be efficient, and acceptable for any size circle.
# 
# Adding 3 to n guarantees that the polygon has at least 3 sides.

# ## 4.7  Refactoring

# When I wrote circle, I was able to re-use polygon because a many-sided polygon is a good approximation of a circle. But arc is not as cooperative; we can’t use polygon or circle to draw an arc.
# 
# One alternative is to start with a copy of polygon and transform it into arc. The result might look like this:

# ```python
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#     
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)
# ```

# The second half of this function looks like polygon, but we can’t re-use polygon without changing the interface. We could generalize polygon to take an angle as a third argument, but then polygon would no longer be an appropriate name! Instead, let’s call the more general function polyline:

# ```python
# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# ```

# Now we can rewrite polygon and arc to use polyline:
# 
# ```python
# def polygon(t, n, length):
#     angle = 360.0 / n
#     polyline(t, n, length, angle)
# 
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)
# ```

# Finally, we can rewrite circle to use arc:
# 
# ```python
# def circle(t, r):
#     arc(t, r, 360)
# ```

# This process—rearranging a program to improve interfaces and facilitate code re-use—is called refactoring. In this case, we noticed that there was similar code in arc and polygon, so we “factored it out” into polyline.
# 
# If we had planned ahead, we might have written polyline first and avoided refactoring, but often you don’t know enough at the beginning of a project to design all the interfaces. Once you start coding, you understand the problem better. Sometimes refactoring is a sign that you have learned something.

# # 4.9  docstring

# A docstring is a string at the beginning of a function that explains the interface (“doc” is short for “documentation”). Here is an example:

# ```python
# def polyline(t, n, length, angle):
#     """Draws n line segments with the given length and
#     angle (in degrees) between them.  t is a turtle.
#     """    
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# ```

# By convention, all docstrings are triple-quoted strings, also known as multiline strings because the triple quotes allow the string to span more than one line.
# 
# It is terse, but it contains the essential information someone would need to use this function. It explains concisely what the function does (without getting into the details of how it does it). It explains what effect each parameter has on the behavior of the function and what type each parameter should be (if it is not obvious).
# 
# Writing this kind of documentation is an important part of interface design. A well-designed interface should be simple to explain; if you have a hard time explaining one of your functions, maybe the interface could be improved.

# ## 4.10  Debugging

# An interface is like a contract between a function and a caller. The caller agrees to provide certain parameters and the function agrees to do certain work.
# 
# For example, polyline requires four arguments: t has to be a Turtle; n has to be an integer; length should be a positive number; and angle has to be a number, which is understood to be in degrees.
# 
# These requirements are called preconditions because they are supposed to be true before the function starts executing. Conversely, conditions at the end of the function are postconditions. Postconditions include the intended effect of the function (like drawing line segments) and any side effects (like moving the Turtle or making other changes).
# 
# Preconditions are the responsibility of the caller. If the caller violates a (properly documented!) precondition and the function doesn’t work correctly, the bug is in the caller, not the function.
# 
# If the preconditions are satisfied and the postconditions are not, the bug is in the function. If your pre- and postconditions are clear, they can help with debugging.

# ## 4.12  Exercises

# **문제 1**

# Download the code in this chapter from http://thinkpython2.com/code/polygon.py.
# 
# 1. Draw a stack diagram that shows the state of the program while executing circle(bob, radius). You can do the arithmetic by hand or add print statements to the code.
# 
# 1. The version of arc in Section 4.7 is not very accurate because the linear approximation of the circle is always outside the true circle. As a result, the Turtle ends up a few pixels away from the correct destination. My solution shows a way to reduce the effect of this error. Read the code and see if it makes sense to you. If you draw a diagram, you might see how it works.
# 
# Figure 4.1: Turtle flowers.

# **문제 2**

# Write an appropriately general set of functions that can draw flowers as in Figure 4.1.
# 
# Solution: http://thinkpython2.com/code/flower.py, also requires http://thinkpython2.com/code/polygon.py.
# 
# 
# Figure 4.2: Turtle pies.

# **문제 3**

# Write an appropriately general set of functions that can draw shapes as in Figure 4.2.
# 
# Solution: http://thinkpython2.com/code/pie.py.

# **문제 4**

# The letters of the alphabet can be constructed from a moderate number of basic elements, like vertical and horizontal lines and a few curves. Design an alphabet that can be drawn with a minimal number of basic elements and then write functions that draw the letters.
# 
# You should write one function for each letter, with names draw_a, draw_b, etc., and put your functions in a file named letters.py. You can download a “turtle typewriter” from http://thinkpython2.com/code/typewriter.py to help you test your code.
# 
# You can get a solution from http://thinkpython2.com/code/letters.py; it also requires http://thinkpython2.com/code/polygon.py.

# **문제 6**

# Read about spirals at http://en.wikipedia.org/wiki/Spiral; then write a program that draws an Archimedian spiral (or one of the other kinds). Solution: http://thinkpython2.com/code/spiral.py.
# 
# Buy this book at Amazon.com
