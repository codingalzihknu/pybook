#!/usr/bin/env python
# coding: utf-8

# (ch:module)=
# # 모듈

# 한 번 구현한 함수, 상수, 변수, 클래스, 객체 등을 
# 다른 파이썬 파일 또는 코드에서 공유하여 사용하면 프로그램을 보다 효율적으로 구현할 수 있다.
# 이를 위해 **모듈**<font size='2'>module</font>을 활용한다.
# 파이썬의 모듈은 간단하게 말하면 하나의 파이썬 소스코드 파일이며, 확장자로 ".py" 가 사용된다.
# 하나의 모듈은 서로 연관된 함수, 클래스 등을 포함한다. 
# 
# 예를 들어 `math` 모듈은 다양한 수학 함수를,
# `random` 모듈은 무작위수를 생성하는 많은 함수를,
# `turtle` 모듈은 간단한 그래픽 관련 함수와 클래스를 제공한다.

# ## 모듈, 패키지, 라이브러리, 프레임워크

# 하나의 모듈이 독립적으로 제공되기도 하지만 다른 모듈과 함께 하나의 모음집으로 제공되기도 한다.
# 모음의 크기와 용도에 따라 패키지, 라이브러리, 프레임워크 등 다양한 이름으로 불린다. 

# **패키지**<font size='2'>package</font>는 모듈을 모아놓은 디렉토리(폴더)이며, 
# `__init__.py` 모듈을 반드시 포함해야 한다.
# 패키지 안에 하위 패키지가 포함될 수 있으며, 각 하위 패키지 모두 `__init__,py` 모듈을 
# 포함해야 한다. 
# `__init__.py` 모듈은 해당 패키지가 사용될 때 필요한 기본 설정을 담당한다. 

# <div align="center"><img src="https://pythongeeks.org/wp-content/uploads/2021/12/structure-of-packages.webp" style="width:450px;"></div>
# 
# <그림 출처: [Python Packages with Examples](https://pythongeeks.org/python-packages/)>

# **라이브러리**<font size='2'>library</font>는
# 모듈, 패키지 등 재사용이 가능한 코드의 모음을 통칭헤서 부르는 이름이다.
# 패키지가 하위 패키지를 포함하기에 라이브러리로 불리기도 하지만
# 라이브러리는 여러 개의 패키지로 이루어진 모음집으로 하나의 패키지와 구분된다.
# [파이썬 표준 라이브러리](https://docs.python.org/3/library/)에서 
# 기본으로 제공되는 패키지와 모듈을 확인할 수 있다.
# 
# 반면에 게임 프로그래밍에 사용되는 Pygame, 데이터 분석에 필수인 Numpy, Pandas, Matplotlib,
# 웹에서 필요한 데이터 수집에 유용한 BeautifulSoup,
# 머신러닝/딥러닝 분야의 Tensorflow, Keras, PyTorch 등이
# 대표적인 제3자 파이썬 라이브러리다.

# **프레임워크**<font size='2'>framework</font>는 라이브러리 보다 포괄적인 개념이다.
# 라이브러리가 필요한 도구와 도구 모음집을 제공하는 반면에
# 프레임워크는 라이브러리를 적용하는 전반적인 틀<font size='2'>frame</font>과 
# 기본 구조<font size='2'>architecture</font>를 제공한다.
# 
# 예를 들어, 플라스크<font size='2'>Flask</font> 프레임워크는 웹서버 개발에 적절한 틀과 구조를,
# 장고<font size='2'>Django</font> 프레임워크는 웹 어플리케이션 구현에 최적의 틀과 구조를 제공한다.
# 사용자는 해당 프레임워크가 제공하는 틀과 구조에 맞춰 적절한 코드를 작성하면 원하는 결과를
# 프레임워크를 사용하지 않을 때에 비해 훨씬 쉽고 빠르게 구현한다.

# 파이썬 표준 라이브러리에 포함되지 않은 제3자가 제공하는 모듈, 패키지, 라이브러리, 프레임워크 등을 
# 이용하려면 추가적으로 설치해야 한다. 
# 설치는 일반적으로 `pip` 이라는 파이썬 패키지 인스톨러를 
# 터미널에서 실행하는 방식을 사용한다.
# 예를 들어 넘파이 모듈을 설치하려면 다음 명령을 실행한다.
# 달러 기호(`$`) 터미널의 프롬프트를 가리키며 실제로 입력하지는 않음에 주의하라.
# 
# ```bash
# $ pip install numpy
# ```
# 
# 주피터 노트북에서도 동일한 방식으로 설치할 수 있다.
# 단, 아래 처럼 느낌표로 시작해야 한다.
# 
# ```
# >>> !pip install numpy
# ```

# 모듈, 패키지, 라이브러리, 프레임워크 중에서 가장 작은 단위인 모듈만 
# 불러와서<font size='2'>import</font> 모듈에 포함된 함수, 클래스 등을 사용할 수 있다.
# 모듈을 불러오는 기본 방식은 다음과 같다.
# 
# ```python
# >>> import 모듈명
# ```
# 
# 반면에 모듈이 아닌 패키지를 불러올 수도 있지만 그러려면 패키지 폴더에 있는 `__init__.py` 모듈에 
# 해당 패키지를 불러올 때 기본적으로 함께 불러오는 모듈이 지정되어 있어야 한다. 
# 보다 자세한 사항은 
# [코딩도장: 패키지에서 from import 응용하기](https://dojang.io/mod/page/view.php?id=2450)를 참고할 수 있다.

# 모듈은 크게 세 종류로 나뉜다.
# 
# * 내장 모듈: 
#     `math`, `urllib.request`, `random`, `turtle`, `os`, `sys` 등 
#     파이썬을 설치할 때 기본으로 제공되는 모듈
# * 제3자 라이브러리<font size='2'>third-party library</font> 모듈: 
#     `numpy.random`, `matplotlib.pyplot`, `pygame.mixer` 등 
#     제3자가 제공한 라이브러리에 포함된 모듈
# * 사용자 정의 모듈: 
#     개인 프로젝트를 위해 직접 작성한 파이썬 코드 파일

# ## 모듈 불러오기

# 예를 들어, `math` 모듈을 활용하는 방식은 다음과 같다.

# **방식 1: `import ...`**

# 먼저 `math` 모듈 불러온 다음에 모듈에 포함된 임의의 함수를 사용한다.

# In[1]:


import math


# `log()` 함수를 호출하려면 다음처럼 모듈과 함수를 점(`.`)으로 구분해서 함께 사용한다.

# In[2]:


math.log(2)


# `sin()`, `cos()` 함수 사용법도 동일하다.

# In[3]:


math.sin(90)


# In[4]:


math.cos(90)


# **방식 2: `from ... import ...`**

# 모듈에 포함된 특정 함수만 뽑아와서 사용할 수도 있다.
# 그러려면 `from-import` 키워드를 사용한다.
# 아래 코드는 `math` 모듈에 `log()` 함수와 `sin()` 함수 두 개만 불러온다.

# In[5]:


from math import log, sin


# 이제 `log()`, `sin()` 두 함수는 독립적으로 사용된다.

# In[6]:


log(2)


# In[7]:


sin(90)


# 하지만 `cos()` 함수는 모듈 이름없이 독립적으로 사용할 수 없다.

# ```python
# >>> cos(90)
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_305/157168676.py in <module>
# ----> 1 cos(90)
# 
# NameError: name 'cos' is not defined
# ```

# 아래 방식으로 `math` 모듈에 포함된 모든 함수, 클래스 등을 한꺼번에 불러올 수 있다.
# 
# ```python
# from math import *
# ```
# 
# 하지만 이 방식은 권장되지 않는다. 
# 이유는 기존에 사용된 함수, 변수 등의 이름과 충돌이 발생할 수 있기 때문이다.

# :::{admonition} 별표(`*`) 의 의미
# :class: tip
# 
# 프로그래밍 분야에서 별표(`*`)는 모든 파일, 모든 이름 등을 가리킬 때 사용한다. 
# :::

# **방식 3: `import ... as ...`**

# 모듈이나 패키지를 불러올 때 별칭을 지정하여 활용할 수 있다.
# 많이 사용되는 모듈이나 패키지는 많은 사람들이 관습적으로 사용하는 별칭이 있다.
# `numpy` 패키지의 경우 보통 `np`로 줄여 부른다.
# 별칭을 사용하는 방식은 다음과 같다.

# In[8]:


import numpy as np


# 넘파이 패키지에 `random` 모듈이 포함되어 있으며
# 파이썬의 기본 라이브러리인 `random` 보다 많은 기능을 갖춘 함수를 포함한다.

# In[9]:


np.random.random()


# 패키지나 모듈을 불러올 때 별칭을 지정하면 반드시 별칭으로 사용해야 한다.
# 그렇지 않으면 오류가 발생한다.

# ```python
# >>> numpy.random.random()
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_3215/3003934882.py in <module>
# ----> 1 numpy.random.random()
# 
# NameError: name 'numpy' is not defined
# ```

# ## 사용자 정의 모듈

# ### 파이썬 파일 저장

# 아래 코드를 담고 있는 `wc.py` 파일을 모듈로 불러와서 활용해보자. 

# ```python
# def linecount(filename):
#     count = 0
#     with open(filename) as f:
#         for line in f:
#             count += 1
#     return count
# ```

# `wc.py` 파일을 직접 생성하거나 아래 `myWget`파일을 이용하여 다운로드한다.

# In[10]:


from urllib.request import urlretrieve
from pathlib import Path

# 서버 기본 주소
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/codes/"
# 파일 저장 위치
code_path = Path() / "codes"

def myWget(filename):
    file_url = base_url + filename
    code_path.mkdir(parents=True, exist_ok=True)
    target_path = code_path / filename

    return urlretrieve(file_url, target_path)


# 아래 코드를 실행하면 현재 디렉토리에 `codes` 라는 하위 디렉토리가 생성되고
# 그 안에 `wc.py` 파일이 저장된다.

# In[11]:


myWget('wc.py')


# 다운로드된 파일의 내용을 확인하면 다음과 같이 앞서 언급한 내용과 동일하다.

# In[12]:


with open(code_path / "wc.py") as f:
    print(f.read())


# :::{admonition} `cat` 명령어
# :class: info
# 리눅스와 맥 OSX 운영체제에선 파이썬 명령문이 아닌 `cat` 터미널 명령문을 이용할 수도 있다.
# 윈도우에서는 추가 설정을 해주어야 하며, 주피터 노트북에서는 느낌표(`!`)를 앞쪽에 추가하는 것에 주의하라.
# 
# ```bash
# >>> !cat "./codes/wc.py"
# def linecount(file_name):
#     count = 0
#     with open(file_name) as f:
#         for line in f:
#             count += 1
#     return count
# ```
# :::

# ### 사용자 정의 모듈 불러오기

# 만약에 `wc.py` 파일이 `codes` 폴더가 아닌 현재 작업 디렉토리에 저장되어 있다면
# 단순히 아래 방식을 사용하면 된다.
# 
# ```python
# import wc
# ```
# 
# 하지만 여기서는 그렇지 않기에 좀 더 복잡하다. 
# 이유는 앞서 패키지를 설명했던 것처럼 `codes` 디렉토리를 패키지로 지정한 다음에
# 파이썬 실행기<font size='2'>interpreter</font>에 해당 패키지의 존재를 알려야 하기 때문이다.

# **패키지 지정**
# 
# 특정 폴더를 파이썬 패키지로 지정하려면 해당 폴더에 `__init__.py` 파일명을 가진 파일이 존재하면 된다.
# `__init__.py` 파일은 해당 패키지를 불러올 때 사용할 설정을 담은 모듈인데
# 아무 설정도 하지 않는다면 비어두어도 된다.
# 여기서는 아무 설정도 하지 않는 빈 파일로 사용한다.
# 
# 비어 있는 `__init__.py` 파일을 생성해서 `codes` 디렉토리에 저장하거나 아래 명령문을 실행해서
# 해당 파일을 다운로드 한다.

# In[13]:


myWget('__init__.py')


# `os` 모듈의 `listdir()` 함수를 이용하여
# `codes` 디렉토리에 두 개의 파일이 있음을 확인한다.

# In[14]:


import os

os.listdir(code_path)


# **라이브러리 경로**

# 현재 작업 디렉토리가 아닌 디렉토리에 포함된 파이썬 파일을 모듈로 불러오는 기본적인
# 방법은 **라이브러리 경로**<font size='2'>library path</font>에 해당 디렉토리를 
# 임시로 추가하는 것이다.

# :::{admonition} 영구적 라이브러리 경로 추가
# :class: warning
# 
# 특정 디렉토리를 라이브러리 경로에 영구적으로 추가하는 방법은 여기서는 다루지 않는다.
# 필요하다면 [파이썬 경로 추가 방법](https://pybasall.tistory.com/201)를 참고할 수 있다.
# :::

# 파이썬이 기본적으로 지원하는 라이브러리들의 경로들의 리스트를 `sys.path` 변수가 가리킨다.

# In[15]:


import sys

sys.path


# 따라서 `sys.path` 가 가리키는 리스트에 원하는 디렉토리의 경로를 추가만 하면 된다.
# `Path` 객체의 `absolute()` 메서드가 지정된 경로의 절대경로를 반환한다.

# In[16]:


code_path.absolute()


# 위 경로를 문자열로 변환한 다음에 라이브러리 경로에 추가하지.

# In[17]:


sys.path.append(str(code_path.absolute()))


# 이제 새로운 경로가 추가된 것을 확인할 수 있다.

# In[18]:


sys.path


# 라이브러리 경로에 포함된 디렉토리의 파이썬 파일은 
# 바로 불러올 수 있다.

# In[19]:


import wc


# 이제 `linecount()` 함수를 사용하면 된다.
# 아래 코드는 `wc.py` 파일이 총 6개의 줄을 담고 있음을 확인해준다.

# In[20]:


wc.linecount(code_path / "wc.py")


# ## 모듈 실행

# 모듈은 보통 자주 사용될 함수, 클래스, 상수 등을 저장한다.
# 그런데 모듈에 명령문이 포함되어 있으면 파일을 불러올 때 명령문이 실행된다.
# 따라서 재사용을 위한 파이썬 파일인 경우 실행 명령문을 코드에 추가하는 일은 삼가해야 한다.
# 
# 반면에 파일에서 정의된 함수, 클래스 등의 사용법, 성능 등의 설명을 위한 실행 예제로 지정하거나,
# 파이썬 파일을 하나의 프로그램으로 작동하게 하기 위해서 
# 파일의 맨 아래에 아래 형식의 코드가 추가된다.
# 
# ```python
# if __name__ == '__main__':
#     명령문
# ```
# 
# `__name__` 은 현재 실행되는 파일의 이름을 가리키는 속성 변수이며,
# `__main__` 은 자신을 가리키는 값이다.
# 
# 위 형식의 코드는 다른 파이썬 파일에서 해당 모듈을 불러올 때는 실행되지 않지만
# 아래와 같이 터미널에서 해당 파일을 실행하면 지정된 명령문이 실행된다.
# 
# ```bash
# $ python 파일명.py
# ```

# ## 연습문제 

# 참고: [(실습) 모듈](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-modules.ipynb)
