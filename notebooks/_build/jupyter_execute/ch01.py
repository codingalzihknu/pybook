#!/usr/bin/env python
# coding: utf-8

# # 프로그래밍이란?

# ## 하드웨어와 소프트웨어

# 컴퓨터는 데이터를 입력받아 처리하고 그 결과를 저장하거나 출력하는 기기로, 
# **하드웨어**(hardware)와 **소프트웨어**(software)로 구성된다. 

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/hardware-vs-software.jpg" style="width:500px;"></div>

# 하드웨어는 컴퓨터의 물리적 부품을 일컫는 말로, 크게
# 보통 CPU라 불리는 중앙처리장치(Central Processing Unit),
# 기억장치, 입출력장치로 구성된다. 
# 
# - **CPU**: 컴퓨터에서 가장 핵심적인 부분으로,
#     주기억장치에 저장된 명령들을 읽고 해석하고, 
#     해석된 명령에 따라 각 장치에 조작을 지시하는 제어 장치(Control Unit)와 
#     산술 연산이나 논리 연산 등을 담당하는 연산장치(Arithmetic & Logic Unit), 
#     그리고 CPU에서 사용하는 데이터를 빠르게 일시적으로 저장하는 
#     레지스터(Register)로 구성된다. 일반적으로 레지스터의 용량은 작아 
#     큰 용량의 기억장치가 필요하다. 
# 
# - **기억장치**: 데이터나 프로그램을 저장하는 장치로, 
#     주로 주기억장치(Main Memory 또는 메모리)와 
#     보조기억장치(Auxiliary Memory)로 나눈다. 
#     입력 장치로부터 들어온 데이터는 주기억장치에 저장되며, 
#     주기억장치에 저장되어 있어야 CPU에서 처리될 수 있다. 
#     보조기억장치는 그 이름처럼 주기억장치를 보조해주는 장치로, 
#     예를 들어 USB, SSD 등이 있다. 
# 
# - **입출력장치**: 데이터를 컴퓨터가 이해할 수 있는 형태로 변환하여 
#     전달하는 장치로 예를 들어, 키보드, 마우스, 마이크, 센서, 
#     터치 스크린 등이 있다. 
#     출력장치는 CPU가 처리한 결과를 출력하는 장치로, 
#     예를 들어, 모니터, 스피커, 프린터 등이 있다. 

# ::::{admonition} 참고
# :class: info
# 
# 참고) 마이크로프로세서(Microprocessor) : CPU를 하나의 칩으로 만든 것을 말한다. 컴퓨터에도 마이크로프로세서가 사용된다. 
# ::::

# 반면 소프트웨어는 하드웨어를 사용하여 특정 기능을 수행하도록 하는 명령문의 모음으로, 크게 응용 소프트웨어(application software 또는 어플, 앱)과 시스템 소프트웨어(system software)로 구분된다. 
# 
# - **시스템 소프트웨어**: 하드웨어와 응용소프트웨어를 효율적으로 
#     운영, 관리하기 위해 만들어진 소프트웨어로, 
#     대표적인 시스템 소프트웨어로는 윈도우(window), 우분투(ubuntu) 등과 
#     같은 운영 체제(Operating System, OS)가 있다.
# 
# - **응용 소프트웨어**: 운영 체제 위에서 특정한 일을 처리하기 위해 
#     실행되는 소프트웨어로, 예를 들어 웹브라우저, 워드프로세서, 엑셀 등이 있다. 

# ## 프로그램, 프로그래밍, 프로그래밍 언어 

# 컴퓨터 **프로그램**(program)이란, 어떤 주어진 문제를 해결하기 위해서 특정 프로그래밍 언어를 이용하여 컴퓨터가 수행해야 할 작업들을 모아 놓은 명령문의 모음이라고 볼 수 있다. 
# 
# 프로그램의 핵심은 문제해결을 위한 특정 알고리즘이며, 동일한 알고리즘을 이용하더라도 서로 다르게 보이는 프로그램을 구현할 수 있고, 사용하는 프로그래밍 언어와 작성자에 따라 여러 종류의 프로그램이 존재한다. 
# 
# **프로그래밍**(programming)은 특정 목적을 달성하기 위해 컴퓨터가 실행할 수 있는 컴퓨터 프로그램을 디자인하는 과정을 말한다. 
# 
# **프로그래밍 언어**(programming language)는 컴퓨터 프로그램을 만들 때 사용하는 언어를 말한다. 자연어와 마찬가지로 다양한 프로그래밍 언어가 있으며, 보통 저수준 언어(low-level language)와 고수준 언어(high-level language)로 나눈다.
# 
# - 저수준 언어는 컴퓨터가 이해하기 쉽게 작성된 프로그래밍 언어로, 일반적으로 기계어(machine language)와 어셈블리어(assembly language)를 말한다. 이때 기계어는 CPU가 직접 해석하고 실행할 수 있는 숫자로만 구성된 언어를 말하는데, 이를 보고 사람이 이해하기는 어렵다. 어셈블리어는 기계어를 사람이 이해할 수 있는 문자 형태로 변경한 것을 말하는데, 숫자를 문자로 바꾸기 만한 것이라 여전히 사람이 이해하기는 어렵다. 어셈블리어를 기계어로 변경해주는 프로그램을 어셈블러(assembler)라고 말한다.  
# 
# - 고수준 언어는 사람이 이해하기 쉽게 작성된 프로그래밍 언어로, 파이썬, C언어, 자바 등 대부분의 프로그래밍 언어들이 고수준 언어다. 고수준 언어는 저수준 언어보다 가독성이 높고 사용이 편리하여 프로그래머들은 주로 고수준 언어를 사용한다. 반면, 컴퓨터는 기계어만 이해할 수 있기 때문에, 고수준 언어로 만들어진 프로그램은 기계어로 변경해야만 컴퓨터에서 실행할 수 있다. 이때 컴파일러(compiler) 또는 인터프리터(interpreter)를 사용한다. 

# ::::{admonition} 참고
# :class: info
# 
# **원시 코드** 또는 **소스 코드**(source code)는 
# 특정 프로그래밍 언어로 작성된 작성된 프로그램을 말한다. 
# 반면에 **목적 코드** 또는 **오브젝트 코드**(object code)는 
# 어셈블러나 컴파일러가 소스 코드를 어셈블 또는 컴파일하여 만든 코드이다.
# ::::

# ## 컴파일러와 인터프리터

# 컴퓨터는 기계어만 인식하기 때문에 고수준 언어를 사용하여 만든 코드는 컴퓨터가 이해할 수 있도록 변경하는 작업이 필요하다. 이를 위해 컴파일러(compiler) 또는 인터프리터(interpreter 또는 해석기)를 이용한다. 
# 
# **컴파일러**(compiler)는 특정 프로그래밍 언어를 다른 프로그래밍 언어로 변환하는 언어 번역 프로그램을 말하며, 변환하는 과정을 **컴파일**(compile)이라 부른다. 주로 고수준 언어를 컴퓨터가 이해할 수 있는 기계어로 변경하는 데 사용된다. 컴파일과정은 아래 그림과 같다. 
#  

# <div align="center"><img src="https://greenteapress.com/thinkpython/html/thinkpython002.png" style="width:450px;"></div>

# 그림과 같이 컴파일러 방식에서는 컴파일러로 소스코드 전체를 훑은 다음, 한꺼번에 오브젝트코드로 변환하고 이를 일괄 실행한다.  C언어나 자바 등과 같은 대부분의 고수준 언어가 컴파일러 방식을 사용하고 있다. 
# 
# 컴파일러와 달리 **인터프리터**(interpreter)는 소스코드를 한 줄씩 해석하여 바로 실행되게 하는 프로그램을 말한다. 인터프리터 작동 방식은 아래 그림과 같다. 

# <div align="center"><img src="https://greenteapress.com/thinkpython/html/thinkpython001.png" style="width:300px;"></div>

# 그림과 같이 인터프리터 방식에서는 명령어를 만날 때마다 즉시 인터프리터로 번역하여 실행하기 때문에 대화형 프로그래밍(Interactive programming)도 가능하다.  파이썬, 루비, 자바스크립트, R 등과 같은 고수준 언어가 인터프리터 방식을 사용하고 있다.  

# 인터프리터 방식은 코드의 실행 결과를 바로 확인해 볼 수 있기 때문에 프로그램 테스트나 교육용으로도 많이 사용되고 있다. 
# 
# 반면 컴파일러 방식은 컴파일하는 과정에서 상당히 많은 시간이 필요할 수도 있지만 일단 컴파일되면 빠르게 실행하기 때문에 일반적으로 인터프리터 방식보다 빠르다. 또, 컴파일러 방식은 소스코드 전체를 훑으며 불필요한 코드를 삭제하거나 코드의 중복을 방지할 수 있기 때문에 프로그래밍에서 많이 사용하고 있다. 

# ::::{admonition} 참고
# :class: info
# 
# **프로그램, 소스 코드, 코드, 명령문**
# 
# - 프로그램: 완성된 형태
# - 소스 코드: 
# - 코드: 소스코드의 일부분
# - 명령문: 한 줄 한 줄
# 
# **프로그래밍과 코딩**
# - 프로그래밍:
# - 코딩:
# ::::

# ## 파이썬 프로그래밍 언어

# 파이썬<font size="1">Python</font> 은 1991년 귀도 반 로섬<font size="1">Guido van Rossum</font>이 개발한 고수준 프로그래밍 언어로, 거의 모든 운영체제에서 동작하는 인터프리터 방식의 범용 프로그래밍 언어<font size="1">general-purpose programming language</font>이다.
# 
# 기존 프로그래밍 언어들의 한계를 극복하고자 만들어진 파이썬은 자연어와 유사할 정도로 간결하고 쉬운 문법을 가지고 있다. 
# 예를 들어, 아래의 파이썬 코드는 `you`가 `members` 리스트에 없다면 
# 회원가입을 하라는 문구를 출력하는 코드이다. 

# ```python
# you = ‘강현’
# members = [‘민경’, ‘재석’, ‘윤진’, ‘태연’]
# 
# if you not in members :
#     print(‘회원가입을 하세요.’’)
# ```

# 위 파이썬 코드는 프로그래밍에 대한 경험이 전혀 없는 사람도 대략적으로 의미를 유추하는 것이 가능할 정도로 자연어와 유사하다. 파이썬은 들여쓰기로 코드 블록을 구분하는 데, 이는 코드의 가독성을 높인다. 또, 파이썬의 간결하고 쉬운 문법은 오류가 발생할 가능성을 낮춰 프로그램 개발 속도와 생산성을 높일 수 있다.
# 
# 이에 구글<font size="1">Google</font>, 드롭박스<font size="1">Dropbox</font>, 인스타그램<font size="1">Instagram</font> 등 많은 회사에서 소프트웨어 개발에 파이썬을 사용하고 있다. 반면, 실무에서 사용하는 프로그래밍 언어는 다루기 어려워서 보통 프로그래밍 입문자에게 추천하지 않는데, 파이썬은 상대적으로 배우기 쉬운 프로그래밍 언어라 실무에서뿐만 아니라 입문자 교육용으로도 많이 사용되고 있다. 

# ::::{admonition} 참고
# :class: info
# 
# 귀도 반 로섬은 어느 인터뷰에서 당시 프로그램 개발에 사용했던 C언어의 생산성이 낮아 새로운 언어의 필요성을 느꼈다고 말하였다. 
# ::::

# 이러한 파이썬의 특징을 몇 가지 살펴보면, 다음과 같다.
#  
# - 범용 프로그래밍 언어
# - 인터프리터 언어
# - 거의 모든 운영체제에서 동작
# - 객체 지향 언어
# - 동적 타이핑 지원
# - 수많은 표준 라이브러리 제공
# - C, C++와 연동 

# 파이썬은 C언어나 자바 등과 같이 범용 프로그래밍 언어로, 
# 데이터 분석, 머신러닝, 데이터베이스 관리, 웹 개발, 웹 스크래핑, 
# GUI 프로그래밍<font size="1">Graphical User Interface programming</font> 등 
# 다양한 용도로 사용할 수 있다. 
# 
# 그리고 파이썬은 인터프리터 언어라서 코드를 작성한 후에 바로 실행시킬 수 있기 때문에 코드 수정이 간단하며 대화형 프로그래밍도 가능하다. 또, 운영체제별로 컴파일할 필요가 없기 때문에 윈도우, 우분투, macOS 등 거의 모든 운영체제 위에서 작동한다. 
# 
# 또한 파이썬은 C++이나 자바(Java) 등과 같은 OOP,  즉
# **객체 지향 언어**<font size="1">Object-Oriented Programming</font>이다.
# 파이썬은 모든 것이 객체로 잘 설계되어 있어서 매우 편리하고 강력한 기능을 제공한다. 

# :::{admonition} 참고
# :class: info
# 
# OOP는 구현해야 할 객체들을 선택하고, 객체들 사이의 유기적인 관계를 논리적으로 묘사하는 것을 중요하게 여기는 프로그래밍 기법으로, 프로그램 전체를 하나로 묶어서 구현하는 것이 아니라 프로그램을 구성하는 객체들을 중심으로 하여 구현해야 할 프로그램을 완성시키는 방식으로 프로그래밍을 진행하는 것을 말한다. OOP를 잘 활용하면 코드의 재사용성을 높이고, 유지보수하기 좋은 코드를 작성할 수 있다.
# 
# 보통 OOP와 대비하여 절차 지향 프로그래밍(Procedural Programming)을 언급한다. 절차 지향 프로그래밍에서는 수행해야 할 일을 순차적으로 처리하는 과정을 묘사하는 것을 중요하게 여기며, 프로그램 전체가 유기적으로 연결되도록 만드는 프로그래밍 기법이다. 대표적인 절차 지향 프로그래밍 언어로는 C와 HTML이 있다.
# :::

# 파이썬은 **동적 타이핑**<font size="1">Dynamic typing</font>을 지원한다. 
# 동적 타이핑은 변수를 미리 선언하지 않고, 변수를 생성하고자 할 때 
# 값을 초기화하여 사용하는 것을 말한다. 
# 변수의 자료형은 파이썬이 알아서 판단하기 때문에 
# 동적 타이핑은 프로그래밍을 처음 접하는 사람들에게 편리하다. 

# :::{admonition} 참고
# :class: info
# 
# 동적 타이핑과는 달리 변수를 사용하기 전 미리 선언해야 하는 
# **정적 타이핑**<font size="1">Static Typing</font>도 있다. 
# C나 자바처럼 주로 컴파일 방식의 언어가 정적 타이핑을 지원한다. 
# 이처럼 사용할 변수와 변수에 할당될 값의 자료형을 미리 선언하는 것은 
# 불편해 보일 수도 있다. 
# 하지만 정적 타이핑은 컴파일하는 과정에서 선언한 자료형에 맞는 값을 할당하였는지, 
# 선언 후 사용하지 않는 변수가 있는지를 확인하여 버그 발생 확률을 
# 낮출 수 있다는 장점이 있다. 
# 이에 동적 타이핑을 지원하는 파이썬에서도 타입 힌트를 명시하기도 한다. 

# 이뿐만 아니라 파이썬은 다양한 분야에서 사용할 수 있는 수많은 라이브러리를 제공하고 있다. 예를 들어, 데이터과학에서 유용한 파이썬 라이브러리로는 Numpy, Pandas, TensorFlow, Keras, Matplotlib등이 있고, 웹 프레임워크 라이브러리로는 Django, Flask 등이 있다. 라이브러리의 사용은 쉽게 다양한 기능을 사용할 수 있게 하고 더 적은 코드를 작성하여 더 많은 일을 할 수 있도록 한다. 즉, 적절히 라이브러리를 사용하면 빠른 개발 속도로 생산성을 높일 수 있다. 
# 
# 이외에도 파이썬은 C나 C++와 연동가능하다. 즉, C나 C++로 만든 프로그램을 파이썬에서 사용할 수 있다. 파이썬은 다루기 쉬운 반면 컴파일러 방식의 언어에 비해 처리 속도가 느리다는 단점이 있는데 C나 C++과 연동함으로써 이러한 단점을 보완할 수 있다. 대표적인 예로는 넘파이(Numpy)가 있다. C언어로 만든 넘파이의 사용은 파이썬으로도 빠르고 효율적인 방법으로 데이터를 처리하고 저장할 수 있게 한다. 

# 지금까지 살펴본 파이썬의 특징으로 인해  파이썬의 인기는 날이 갈수록 높아지고 있다. 
# 프로그래밍 언어들의 인기도를 측정하는 
# TIOBE 인덱스<font size="1">https://www.tiobe.com/tiobe-index//</font>에 
# 따르면, 2022년 1월 기준으로 파이썬은 가장 인기있는 프로그래밍 언어이다. 
# 이에 지금 당장 프로그래밍을 배우고자 한다면, 파이썬을 추천한다. 

# <div align="center">
#     <img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/tiobe-index.jpg" style="width:500px;">
# </div>
