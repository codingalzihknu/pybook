#!/usr/bin/env python
# coding: utf-8

# # 컴퓨터 프로그래밍

# ## 컴퓨터 프로그램

# **컴퓨터 프로그램**<font size='2'>computer program</font>은 주어진 문제를 해결하기 위해
# 컴퓨터가 수행해야 할 작업 목록을 특정 프로그래밍 언어로 작성한 
# **명령문**<font size='2'>command</font>의 모음이다. 
# 명령문의 모음을 일반적으로 **소프트웨어**<font size="2">software</font>라 부른다.
# 프로그램의 핵심은 문제 해결을 위한 알고리즘이며, 
# 사용되는 알고리즘에 따라 결과는 같지만 내부적으로는 다르게 작동하는 프로그램이 구현된다. 
# 또한 동일한 알고리즘이더라도 사용하는 프로그래밍 언어에 따라 다르게 
# 기본적으로 다르게 구현해야 한다. 
# 이처럼 문제 해결을 위한 컴퓨터 프로그램을 구현하는 과정이
# **컴퓨터 프로그래밍**<font size="2">computer programming</font>이다.
# 일상적으로 **프로그래밍**이라 하며 **코딩**<font size="2">coding</font>이 동의어로 사용된다.
# 다만 프로그래밍은 전문 프로그래머<font size="2">programmer</font>의 직업과 관련된 개념으로,
# 코딩은 "코드를 작성한다"는 보다 구체적인 일의 의미로 구분해서 사용하기도 한다.

# :::{admonition} 소프트웨어, 프로그램, 소스 코드, 코드, 명령문
# :class: tip
# 
# 소프트웨어, 프로그램, 소스 코드(원시 코드), 코드, 명령문 등이 특별한 구분 없이 
# 사용되곤 한다. 
# 언급된 다섯 개념을 엄밀히 구분하는 기준은 없지만 일반적인 용도를 살펴 보았을 때
# 다음과 같이 구분할 수 있다.
# 
# - 소프트웨어: 하드웨어를 이용하여 특정 기능을 수행하도록 하는 컴퓨터 프로그램 일반.
# - 프로그램: 특정 문제를 해결하는 컴퓨터 프로그램.
# - 소스 코드: 프로그램 구현에 사용된 명령문 모음집. 원시 코드라고도 불림.
# - 코드: 소스 코드의 일부 또는 전체.
# - 명령문: 소스 코드의 구성 요소 또는 일부.
# :::

# ## 프로그래밍 언어

# **프로그래밍 언어**<font size="2">programming language</font>는 
# 컴퓨터 프로그램을 구현할 때 사용하는 언어다. 
# 한국어, 영어 등 자연어와 마찬가지로 다양한 언어가 있으며,
# 일반적으로 저수준 언어와 고수준 언어로 나눈다.
# **저수준 언어**는 기계어<font size="2">machine language</font>, 
# 어셈블리어<font size="2">assembly language</font> 등
# 컴퓨터가 이해하기 쉽게 작성되어 사람은 이해하기 어려운 프로그래밍 언어를 가리킨다. 
# 반면에 **고수준 언어**/high-level language</font>는
# 사람이 이해하기 쉽게 이해할 수 있는 명령문과 
# **구문**<font size='2'>syntax</font>을 제공하는 프로그래밍 언어다.
# 파이썬<font size="2">python</font>, C, C++, C#, 자바<font size="2">Java</font>, 
# 자바스크립트<font size="2">Javascript</font>, 스위프트<font size="2">Swift</font>  등 
# 사람들에게 잘 알려진 대부분의 프로그래밍 언어들이 고수준 언어다.
# 고수준 언어로 만들어진 프로그램은 번역기 또는 실행기를 이용하여
# 기계어로 변경해야만 컴퓨터에서 실행될 수 있다.

# ### 번역기

# 보통 **컴파일러**<font size="2">compiler</font>로 불리는 **번역기**는 
# 특정 프로그래밍 언어를 다른 프로그래밍 언어로 변환하는 언어 번역 프로그램을 말한다.
# 변환 과정을 **컴파일**<font size="2">compilation</font>이라 하며,
# 주로 고수준 언어를 컴퓨터가 이해할 수 있는 기계어로 변역하는 데에 사용된다.
# C, C++, C#, 자바 등이 번역기를 사용하는 대표적인 프로그래밍 언어이며,
# 해당 언어로 구현된 프로그램은 먼저 소스코드 전체가 기계어로 변역된 후에야 컴퓨터로 실행될 수 있다.

# ### 실행기

# 번역기와 달리 **실행기**<font size="2">interpreter</font>(인터프리터)는 
# 소스코드를 한 줄씩 해석하여 컴퓨터에 의해 바로 실행되도록 하는 소프트웨어다. 
# 파이썬, 루비, 자바스크립트, R 등과 같은 실행기를 사용하는 고수준 언어는
# 코드를 한 줄씩 실행하는
# **대화식 프로그래밍**<font size="2">interactive programming</font>을 지원한다.

# ## 파이썬

# 파이썬<font size="1">Python</font> 은 1991년 
# 귀도 반 로섬<font size="1">Guido van Rossum</font>이 개발한 
# 고수준 프로그래밍 언어이며
# 거의 모든 운영체제에서 동작하는 
# 실행기 방식의 범용 프로그래밍 언어<font size="1">general-purpose programming language</font>이다.
# 기존 프로그래밍 언어들의 한계를 극복하고자 만들어진 파이썬은 
# 자연어와 유사할 정도로 간결하고 쉬운 문법을 가지고 있다. 

# 예를 들어, 아래의 파이썬 코드는 `name`이 `members` 리스트에 없다면 
# 회원가입을 하라는 문구를 출력하는 코드이다. 
# 
# ```python
# name = '강현'
# members = ['민경', '재석', '윤진', '태연']
# 
# if name not in members :
#     print('회원가입 하세요.')
# ```
# 
# 위 파이썬 코드는 프로그래밍에 대한 경험이 전혀 없는 사람도 
# 대략적으로 의미를 유추하는 것이 가능하다.
# 이렇듯 파이썬 언어는 자연어와 유사하여
# 입문자 교육용으로도 많이 사용된다.
# 또한 파이썬의 간결하고 쉬운 문법은 오류가 발생할 가능성을 낮춰
# 프로그램 개발 속도와 생산성을 높일 수 있다.
# 이에 삼성, LG, 네이버, 다음, 구글<font size="1">Google</font>, 드롭박스<font size="1">Dropbox</font>, 
# 인스타그램<font size="1">Instagram</font> 등 많은 IT 기업에서 소프트웨어 개발에 파이썬을 사용한다.

# 이뿐만 아니라 파이썬은 다양한 분야에서 사용할 수 있는 수많은 라이브러리를 제공하고 있다.
# 
# - 데이터 과학: Numpy, Pandas, Matplotlib, Keras, TensorFlow, PyTorch 등
# - 웹 프레임워크: Django, Flask 등
# 
# 파이썬이 제공하는 강력한 라이브러리는 더 적은 코드로 더 많은 프로그램을
# 효율적으로 구현할 수 있도록 한다. 
# 즉, 프로그래머의 생산성을 향상시킨다.
# 
# 이외에도 파이썬은 C 나 C++ 와 연동이 가능하다.
# 예를 들어 C 또는 C++ 로 구현된 프로그램을 파이썬에서 활용할 수 있다.
# 대표적으로 데이터 분석에서 가장 중요한 라이브러리 중에 하나인 
# 넘파이<font size="2">NumPy</font>는 C 로 구현되어 있지만
# 사용자는 파이썬 라이브러리로 사용한다.

# ### 객체 지향 프로그래밍

# 파이썬은 C++, C#, 자바 등과 같이 OOP,  즉
# **객체 지향 프로그래밍**<font size="1">Object-Oriented Programming</font>을 지원한다.
# OOP는 프로그램을 구성하는 객체와 객체들 사이의 관계를 구현하는 
# 프로그래밍 기법이다. 
# 파이썬은 모든 것이 객체로 설계되어 있으며 
# OOP를 쉽게 적용할 수 있는 매우 편리하고 강력한 기능을 제공한다. 
# 따라서 데이터 분석, 머신러닝, 데이터베이스 관리, 웹 개발, 웹 스크래핑, 
# GUI 프로그래밍<font size="1">Graphical User Interface programming</font> 등 
# 다양한 분야에서 유용하게 활용된다.
# 
# 보통 OOP와 대비하여 **절차 지향 프로그래밍**<font size="2">procedural programming</font>을 언급한다. 
# 절차 지향 프로그래밍은 문제 해결과정의 순차적 묘사가 가장 중요하다.
# 대표적인 절차 지향 프로그래밍 언어로 C와 HTML이 있다.

# ### 동적 타이핑

# 파이썬은 **동적 타이핑**<font size="2">dynamic typing</font>을 지원한다. 
# 동적 타이핑은 선언되는 변수의 자료형을 미리 지정하지 않고
# 변수에 할당된 값을 실행기가 확인하여 프로그램 실행 중에
# 허용되는 것과 그러지 않는 것이 구분되도록 한다.

# 반면에 변수를 사용하기 전 미리 할당받을 수 있는 값의 자료형을 지정해야 하는 것을
# **정적 타이핑**<font size="2">static typing</font>이라 한다.
# C, C++, C#, 자바 등 주로 번역기를 사용하는 언어가 정적 타이핑을 사용한다.

# ### 파이썬 인기도

# 지금까지 살펴본 파이썬의 특징으로 인해  파이썬의 인기는 날이 갈수록 높아지고 있다. 
# 프로그래밍 언어들의 인기도를 측정하는 
# [TIOBE 인덱스](https://www.tiobe.com/tiobe-index)에 
# 따르면, 2022년 2월 기준으로 파이썬은 가장 인기있는 프로그래밍 언어이다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/images/tiobe_index2202.jpg" style="width:500px;">
# </div>
