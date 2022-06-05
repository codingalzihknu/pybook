#!/usr/bin/env python
# coding: utf-8

# (ch:oop)=
# # 사례 연구: 객체 지향 프로그래밍

# **감사의 글** 
# 
# 아래 내용은 [(유튜브) Python Game Coding: Introduction to Collision Detection](https://www.youtube.com/watch?v=bFURdsszto0)의 내용을 참고합니다.
# 자료의 공유를 허가한 [TokyoEdtech](https://www.youtube.com/c/TokyoEdTech)에게 감사드립니다.

# **소스코드**
# 
# 여기서 사용하는 코드는 두 객체의 충돌을 감지하는 다양한 방법을 보여준다. 
# 소스코드와 코드에 사용된 이미지는 아래 링크에서 다운로드할 수 있다.
# [TokyoEdtech의 깃허브](https://github.com/wynand1004/Projects/tree/master/Collision%20Detection)에서
# 다운로드할 수 있다.

# **`turtle` 모듈**
# 
# `turtle` 모듈의 간단한 사용법은 {ref}`ch:casestudy-function-interface`를 참고하기 바란다.
# `turtle` 모듈을 사용하는 소스코드의 실행이 오프라인 환경에서 어려운 경우
# [레플릿](https://replit.com/~) 이용을 권장한다. 
# 여기서 사용하는 코드 또한
# [(레플릿) 충돌 감지](https://replit.com/@codingrg/collisiondetection#main.py)에서
# 확인하고 직접 실행할 수 있다.

# ## OOP 정의

# **객체 지향 프로그래밍**<font size='2'>Object-Oriented Programming</font>은
# 객체들 사이의 유기적인 관계를 묘사하는 프로그래밍 기법이며,
# 줄여서 보통 **OOP**라고 부른다.
# OOP를 지원하는 **객체 지향 언어**로
# 파이썬, 자바, C++, C#, 루비, 자바스크립트 등 많은 컴퓨터 프로그래밍 언어가
# 사용된다.
# 
# OOP와 대비되는 개념으로 절차 지향 프로그래밍이 주로 언급된다. 
# **절차 지향 프로그래밍**은 수행해야 할 일을 순차적으로 처리하는 과정을 묘사하는 것을 가장 중요하게 여기며 
# 프로그램 전체가 유기적으로 연결되도록 만드는 프로그래밍 기법이다. 
# C, HTML 등이 대표적인 절차 지향 프로그래밍언어다. 
# 
# "해야 할 일을 순차적으로 처리한다"는 표현은 가장 기본적인 프로그래밍 기법이며,
# 모든 프로그램은 원하는 결과를 얻기 위한 과정을 논리적이며 순차적으로 
# 처리하도록 구현되어야 한다. 
# OOP 역시 예외가 아니다. 
# 하지만 OOP는 구현해야 할 객체들을 선택하고 객체들 사이의 유기적인 관계를
# 이용하는 과정을 논리적으로 묘사하는 데에 보다 많은 방점을 둔다. 
# 즉, 프로그램 전체를 하나로 묶어서 구현하는 방식이 아니라 프로그램을 구성하는 객체들을 중심으로 해서
# 구현해야 할 프로그램을 완성시키는 방식으로 프로그래밍을 진행한다.

# ## OOP와 객체

# OOP에 대한 이해는 아래 두 가지 질문과 관련되어 있다.
# 
# 1. 객체(object)란 무엇인가?
# 1. "객체를 중심으로 프로그래밍한다" 라는 말의 의미는 무엇인가?
# 
# 위 질문들에 대한 직접적인 설명 대신에
# 객체가 어떻게 활용되는가를 실전 예제를 통해 소개한다.

# ## OOP 예제: 객체 충돌 감지

# 여기서는 두 객체가 충돌하는 것을 서로 어떻게 감지하는가를 이용하여 객체 지향 프로그래밍의 
# 기본 아이디어를 전달한다.

# **기본 설정**
# 
# 캔버스(`wn`)와 펜(`pen`)을 준비한다.
# 또한 스프라이트에 사용될 7개의 이미지를 이미지 라이브러리에 추가한다.

# ```python
# import turtle
# import math
# 
# wn = turtle.Screen()
# wn.bgcolor("black")
# wn.title("Collision Detection by @TokyoEdtech")
# wn.tracer(0)
# 
# pen = turtle.Turtle()
# pen.speed(0)
# pen.hideturtle()
# 
# shapes = ["wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]
# 
# for shape in shapes:
#     wn.register_shape(shape)
# ```

# **스프라이트 클래스 선언**
# 
# 아래 그림에 있는 스프라이트 객체 생성에 사용될 클래스를 선언한다.

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/collision_detection1.png" width="600"/></div>

# 각 스프라이트 객체는 지정된 위치로의 이동 및 자신의 이미지를 보여주는 기능을
# 수행하는 `render()` 메서드와 함께
# 다른 스프라이트와의 충돌을 감지하는 기능을 갖는 세 종류의 메서드를 갖는다.

# ```python
# class Sprite():
#     
#     ## 생성자: 스프라이트의 위치, 가로/세로 크기, 이미지 지정
#     
#     def __init__(self, x, y, width, height, image):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.image = image
# 
#     ## 스프라이트 메서드
#     
#     # 지정된 위치로 스프라이트 이동 후 도장 찍기
#     def render(self, pen):
#         pen.goto(self.x, self.y)
#         pen.shape(self.image)
#         pen.stamp()
#             
#     # 충돌 감지 방법 1: 두 스프라이트의 중심이 일치할 때 충돌 발생
#     def is_overlapping_collision(self, other):
#         if self.x == other.x and self.y == other.y:
#             return True
#         else:
#             return False
#             
#     # 충돌 감지 방법 2: 두 스프라이트 사이의 거리가 두 객체의 너비의 평균값 보다 작을 때 충돌 발생
#     def is_distance_collision(self, other):
#         distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
#         if distance < (self.width + other.width)/2.0:
#             return True
#         else:
#             return False
#         
#     # 충돌 감지 방법 3: 각각의 스프라이트를 둘러썬 경계상자가 겹칠 때 충돌 발생
#     # aabb: Axis Aligned Bounding Box
#     def is_aabb_collision(self, other):
#         x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
#         y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
#         return (x_collision and y_collision)
# ```

# **스프라이트 객체 생성**
# 
# 위 그림에 포함된 6 종류의 스프라이트 객체를 생성한다.
# 스프라이트 중심의 x, y 좌표, 길이와 너비, 이미지 등이 지정된다.

# ```python
# wizard = Sprite(-128, 200, 128, 128, "wizard.gif")
# goblin = Sprite(128, 200, 108, 128, "goblin.gif")
# 
# pacman = Sprite(-128, 0, 128, 128, "pacman.gif")
# cherry = Sprite(128, 0, 128, 128, "cherry.gif")
# 
# bar = Sprite(0, -400, 128, 24, "bar.gif")
# ball = Sprite(0,-200, 32, 32, "ball.gif")
# 
# # 스프라이트 모음 리스트
# sprites = [wizard, goblin, pacman, cherry, bar, ball]
# ```

# **이벤트와 콜백 함수**
# 
# 마우스 클릭, 버튼 누루기, 키 입력 등을 사용하여 
# 영향을 미치는 사건을 **이벤트**<font size='2'>event</font>라 부르며, 
# 이벤트에 반응하도록 프로그램을 작성하는 것이 
# **이벤트 처리**다.
# 여기서는 `goblin`, `pacman`, `ball` 객체를 각각 왼쪽, 오른쪽, 아래 방향으로
# 움직이도록 하는 이벤트를 설정한다.
# 
# 이벤트 처리에 사용되는 함수를 **콜백**<font size='2'>callback</font>라 부르는데
# 사용하는 패키지, 모듈 등에 따라 콜백 함수가 사용되는 방식이 달라진다.
# `turtle` 모듈의 경우 `Screen.listen()` 메서드를 이용한다.

# ```python
# # 고블린 이동
# def move_goblin():
#     goblin.x -= 64
# 
# # 팩맨 이동
# def move_pacman():
#     pacman.x += 30
#     
# # 야구공 이동
# def move_ball():
#     ball.y -= 24
# 
# # 이벤트 처리
# wn.listen()
# wn.onkeypress(move_goblin, "Left")  # 왼쪽 방향 화살표 입력
# wn.onkeypress(move_pacman, "Right") # 오른쪽 방향 화살표 입력
# wn.onkeypress(move_ball, "Down")    # 아래방향 화살표 입력
# ```

# **게임 실행**
# 
# 게임 실행 중에 화살표 키가 입력될 때마다 지정된 콜백 함수가 실행되어
# 의도된 스프라이트가 이동한다.
# 이동하다가 다른 스프라이트와 충돌하면 해당 스프라이트가 X 모양의 이미지로 변경된다.

# <div align="center" border="1px"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/collision_detection2.png" width="600"/></div>

# ```python
# while True:
#     
#     # 각 스프라이트 위치 이동 및 도장 찍기
#     for sprite in sprites:
#         sprite.render(pen)
#         
#     # 충돌 여부 확인
#     if wizard.is_overlapping_collision(goblin):
#         wizard.image = "x.gif"
#         
#     if pacman.is_overlapping_collision(cherry):
#         cherry.image = "x.gif"
#         
#     if bar.is_overlapping_collision(ball):
#         ball.image = "x.gif"
#         
#     wn.update() # 화면 업데이트
#     pen.clear() # 스프라이트 이동흔적 삭제
# ```

# :::{admonition} 프레임
# :class: info
# 
# 앞선 코드의 `while` 반복문이 한 번 실행되는 과정을 **프레임**<font size='2'>frame</font>이라 부른다.
# 1초 길이의 동영상에 사용된 사진의 수로 동영상의 프레임을 지정하는 방식과 유사한 개념이다.
# 컴퓨터의 경우 초당 훨씬 많은 수의 프레임이 돌아갈 수 있지만 '
# 프레임에 포함된 코드의 실행 시간에 따라 다르다.
# :::

# ## OOP의 핵심

# 매 프레임마다 아래 코드가 반복적으로 실행된다.
# 
# ```python
# if wizard.is_overlapping_collision(goblin):
#         wizard.image = "x.gif"
# ```
# 
# 즉, `wizard` 가 `goblin` 과 충돌하면 마법사의 이미지를 X 모양으로 변경한다.
# 그런데 마법사가 고블린과 충돌하는지를 어떻게 감지하는가?
# `wizard` 객체의 `is_overlapping_collision()` 메서드가
# 자신과 `goblin` 객체의 위치, 길이, 너비 정보를 이용하여 알아낸다.
# 즉, 두 객체 사이에 정보를 주고 받는다.
# 
# 이처럼 객체들 사이에 주고 받을 수 있는 정보를 이용하여 객체의 상태와 행동을
# 결정하는 프로그래밍 기법이 바로 객체 지향 프로그래밍이다.

# ## 연습문제

# 참고: [(실습) 사례 연구: 객체 지향 프로그래밍](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-casestudy_oop.ipynb)
