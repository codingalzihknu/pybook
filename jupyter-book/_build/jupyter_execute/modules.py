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

# **패키지**
# 
# 패키지<font size='2'>package</font>는 모듈을 모아놓은 디렉토리(폴더)이며, 
# `__init__.py` 모듈을 반드시 포함해야 한다.
# 패키지 안에 하위 패키지가 포함될 수 있으며, 각 하위 패키지 모두 `__init__,py` 모듈을 
# 포함해야 한다. 
# `__init__.py` 모듈은 해당 패키지가 사용될 때 필요한 기본 설정을 담당한다. 

# <div align="center"><img src="https://pythongeeks.org/wp-content/uploads/2021/12/structure-of-packages.webp" style="width:500px;"></div>
# 
# <그림 출처: [Python Packages with Examples](https://pythongeeks.org/python-packages/)>

# **라이브러리**
# 
# 라이브러리<font size='2'>library</font>는
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

# **프레임워크**
# 
# 프레임워크<font size='2'>framework</font>는 라이브러리 보다 포괄적인 개념이다.
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
# 설치 방법은 해당 

# 여기서는 모듈의 종류와 설치, 사용법을 간단한 예제를 이용하여 설명한다.
# 
# 모듈은 크게 세 종류로 나뉜다.
# 
# * 내장 모듈<font size='2'>built-in module</font>: 
#     `math`, `urllib.request`, `random`, `turtle`, `os`, `sys` 등 
#     파이썬을 설치할 때 기본으로 제공되는 모듈
# * 제3자 라이브러리<font size='2'>third-party library</font> 모듈: 
#     `numpy.random`, `matplotlib.pyplot`, `pygame.mixer` 등 
#     제3자가 제공한 라이브러리에 포함된 모듈
# * 사용자 정의 모듈: 
#     개인 프로젝트를 위해 직접 작성한 파이썬 코드 파일

# ## 내장 모듈

# 파일썬을 설치하면 다양한 모듈이 함께 설치되며, 그런 모듈을 내장 모듈(built-in modules)이라 부른다.
# 지금까지 사용한 모듈은 `random`, `math`, `os`, `sys` 등이며, `import 모듈명` 형식으로 모듈을 불러왔다.
# 단, `.py` 확장자는 생략한다.
# 
# 예를 들어, `math` 모듈을 불러오려면 다음과 같이 한다.

# In[1]:


import math


# 그러면 `math` 모듈에서 정의된 많은 수학 관련 함수들을 사용할 수 있다.
# 예를 들어, 로그(`log`) 함수의 사용은 다음과 같다.

# In[2]:


math.log(2)


# 무작위 수 생성 함수들을 모아놓은 `random` 모듈에 0과 1사이의 실수를 무작으로 
# 생성하는 함수 `random`을 아래와 같이 사용한다.

# In[3]:


import random

random.random()


# `random` 함수는 실행할 때마다 새로운 수를 무작위로 생성한다.

# In[4]:


random.random()


# ## 제3자 라이브러리 모듈

# 제3자에 의해  제공된 라이브러리에 포함된 모듈을 사용하려면 먼저 추가 패키지를 설치해야 한다.
# 예를 들어, 단순한 2차원 그래프를 그리는 도구가 필요하면 맷플롯립(`matplotlib`)을,
# 데이터분석을 위한 다양한 도구가 필요하면 넘파이(`numpy`)를 기본적으로 설치해야 한다.
# 제3자 제공 파이썬 패키지를 설치하는 방법은 해당 패키지의 홈페이지를 참고해야 한다.
# 보통은 파이썬을 설치할 때 함께 제공되는 파이썬 패키지 매니저인 pip 명령어를 활용한다.
# 
# 파이썬과 관련된 주요 패키지를 함께 제공하는 앱이나 웹서버 등이 있어서 
# 개인적으로 추가하고 관리하기 어려운 경우 사용할 수 있다.
# 예를 들어, 아나콘다 패키지는 `matplotlib`, `numpy` 등 파이썬 
# 데이터분석과 관련된 다수의 패키지를 함께 제공한다.
# 또한 Repl.it, 구글 코랩 등도 파이썬 기본 이외에 다양한 패키지를 함께 제공한다. 
# 
# 현재 이 노트북을 실행하는 서버 또한 `matplotlib`, `numpy` 등을 포함해서 
# 다양한 제3자 제공 라이브러리가 함께 설치되어 있다. 
# Repl.it 및 구글 코랩에서 문제없이 작동하는 코드만 여기에서 사용한다. 

# ### 제3자 라이브러리 모듈 불러오기

# 예를 들어, 고차원 어레이를 편하게 다룰 수 있도록 도와주는 많은 도구를 담고 있는 넘파이 패키지를 활용하려면
# 아래와 같이 `numpy` 패키지를 불러와야 한다. 그러면 관련된 많은 모듈과 도구들을 활용할 수 있다.

# #### 별칭 사용하기

# 모듈이나 패키지를 불러올 때 별칭을 지정하여 활용할 수 있다.
# 많이 사용되는 모듈이나 패키지는 많은 사람들이 관습적으로 사용하는 별칭이 있다.
# `numpy` 패키지의 경우 보통 `np`로 줄여 부른다.
# 별칭을 사용하는 방식은 다음과 같다.

# In[5]:


import numpy as np


# 넘파이 패키지에 `random` 모듈이 포함되어 있다. 
# 파이썬에서 기본으로 제공하는 내장 모듈인 `random` 보다 많은 기능을 갖춘 도구들이
# 넘파이 `random` 모듈이 제공한다.
# 
# 앞서 언급했던 파이썬 내장 모듈 `random`에서 정의된 `random` 함수에 해당하는 함수가
# 넘파이 `random` 모듈에 동일한 이름으로 정의되어 있다. 
# 하지만 넘파이 `random` 모듈을 사용하려면 반드시 `np`를 아래와 같이 추가해야 한다.
# 그렇지 않으면 파이썬 내장 모듈과 이름이 혼동되어 문제가 발생할 수 있다.

# In[6]:


np.random.random()


# In[7]:


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

# 원래의 패키지 또는 모듈의 이름을 사용하려면 한 번 불러와야 한다.
# 그러면 원래 이름과 별칭 모두 사용할 수 있다.

# In[8]:


import numpy


# In[9]:


numpy.random.random()


# In[10]:


np.random.random()


# ## 사용자 정의 모듈

# 먼저, 아래 코드를 담고 있는 `wc.py` 파일을 먼저 작성한다.
# `wc.py` 파일을 이용하여 사용자가 임의로 작성한 파이썬 코드 파일을 모듈로 활용하는 법을 설명한다.
# 
# **주의:**
# 설명을 위해 `wc.py` 파일이 현재 작업 디렉토리의 하위 디렉토리인 `codes` 디렉토리에 저장되어 있다고 가정한다.
# 
# 파일의 내용은 아래와 같다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/wc1.png" style="width:600px;"></div>

# ### `__init__.py` 파일 작성
# 
# 현재 작업 디렉토리가 아닌 다른 디렉토리에 포함된 모듈을 불러오려면 
# 해당 디렉토리에 `__init__.py` 파일이 생성되어 있어야 한다.
# 따라서 `codes` 라는 하위 디렉토리에 포함된 파일들의 리스를 확인하면 `wc.py` 와 `__init__.py` 
# 두 개의 파일이 포함되어 있어야 한다.
# 
# **주의:** `__init__.py` 파일은 아무 내용이 없는 빈 파일이어도 된다. 다른 용도는 여기서 다루지 않는다.

# #### 현재 작업 디렉토리 확인

# 파이썬 명령어를 이용하여 현재 작업 디렉토리(current working directory, 줄임말: cwd)를
# 확인하는 방법은 다음과 같다.

# In[11]:


import os
cwd = os.getcwd()
print(cwd)


# 현재 작업 디렉토리에 `codes`라는 디렉토리 포함여부 확인은 다음과 같다.

# In[12]:


'codes' in os.listdir(cwd)


# `codes` 디렉토리에 포함된 파일들의 리스트 확인하면 `wc.py`와 `__init__.py` 두 파일이
# 포함되어 있음을 볼 수 있다.

# In[13]:


# os.listdir("./codes") # 해결 필요


# ### 사용자 정의 모듈 불러오기

# `wc.py` 모듈에 포함되어 있는 `linecount` 함수를 활용하기 위해서
# 먼저 `wc.py` 모듈을 불러와야 한다.

# #### 현재 작업 디렉토리 모듈 불러오기

# 만약 `wc.py` 모듈이 현재 디렉토리에 포함되어 있다면 아래와 같이 불러오면 된다.
# 
# ```
# import wc
# ```
# 
# 또한 `wc.py`에 작성된 코드 마지막 줄을 아래와 같이 작성해야 오류가 발생하지 않는다.
#     
# ```python
# print(linecount('wc.py'))
# ```

# #### 경로 설정 문제

# 그런데 `wc.py` 모듈이 현재 디렉토리의 하위 디렉토리인 `codes` 에 포함되어 있기 때문에 
# 불러오기 과정이 좀 더 복잡하다. 
# 단순히 `import wc` 명령어를 사용하면 모듈을 찾을 수 없다는 오류(`ModuleNotFoundError`)가 발생한다.

# ```python
# import wc
# ModuleNotFoundError                       Traceback (most recent call last)
# /tmp/ipykernel_3243/816188502.py in <module>
# ----> 1 import wc
# 
# ModuleNotFoundError: No module named 'wc'
# ```

# 이와 같이 현재 작업디렉토리가 아닌 곳에 포함된 사용자 정의 모듈은 다른 방식으로 불러와야 한다.
# 다양한 방식이 있지만 여기서는 __라이브러리 경로(library path)__에 특정 디렉토리를 추가하는 방식을 사용한다.
# 
# **주의:** 여기서 라이브러리 경로에 특정 경로를 추가하는 방식은 임시적이다.
# 라이브러리 경로를 영구적으로 변경하려면 다른 방식을 따라야 한다.

# #### 파이썬 라이브러리 경로 확인하기

# 먼저 파이썬이 기본적으로 사용하는 라이브러리들의 경로를 확인해보자.
# `sys.path` 변수에 파이썬이 기본적으로 지원하는 라이브러리들의 경로가 리스트로 저장되어 있다.

# In[14]:


import sys
sys.path


# #### 파이썬 라이브러리 경로에 임시 경로 추가하기

# `sys.path` 에 저장된 라이브러리들의 경로들의 리스트에 원하는 경로를 추가한다.
# 
# 여기서는 현재 작업디렉토리의 하위 폴더인 `codes`를 경로에 추가하며, 
# 리스트에 항목을 추가하는 `append` 메소드를 활용한다.

# In[15]:


sys.path.append(cwd + "/codes")


# 이제 새로운 경로가 추가된 것을 확인할 수 있다.

# In[16]:


sys.path


# #### 라이브러리 경로에 포함된 디렉토리의 모듈 불러오기

# 라이브러리 경로에 포함된 디렉토리의 모듈은 현재 디렉토리에 포함된 모듈을 불러오는 것처럼 하면 된다.

# In[17]:


import wc


# 이제 `wc`가 누군지를 물으면 아래와 같이 답한다.

# In[ ]:


wc


# 즉, `wc`는 모듈이라는 정보와 `wc.py` 파일이 저장된 위치 정보를 보여준다.

# ### `__name__` 속성과 `__main__` 함수

# #### `__name__` 속성

# 파이썬에서 함수, 클래스, 모듈 등은 `__name__`이라는 특별한 속성을 가지며,
# 항상 자기 자신을 가리킨다.
# 
# 예를 들어, 아래 함수를 살펴보자.

# In[ ]:


def myName():
    pass


# 이제 `myName` 함수의 `__name__` 속성을 확인해보자.
# 속성 확인은 자료형의 메서드를 호출하는 방식과 비슷하다.
# 다만, 속성은 함수가 아니기에 괄호를 사용하지 않는다.

# In[ ]:


myName.__name__


# 모듈도 `__name__` 속성을 갖는다. `wc.py` 모듈의 `__name__` 속성을 확인해보자.

# In[ ]:


wc.__name__


# 앞으로 좀 더 구체적으로 배우게 될 클래스 역시 `__name__` 속성을 갖는다.
# 사실 지금까지 살펴본 모든 자료형 역시 클래스이다. 
# 예를 들어, 사전 자료형의 `__name__` 속성은 아래와 같다.

# In[ ]:


dict.__name__


# #### `__main__` 함수

# `wc.py` 모듈을 임포트할 때 앞서 `os`와 `sys` 모듈을 임포트할 때와는 달리 숫자 `7`을 출력한다.
# 이유는 모듈을 임포트할 때 모듈 안에 포함된 코드가 실행되기 때문인데, 
# `wc.py` 파일의 경우에는 마지막 줄에 있는 아래 명령어가 실행되기 때문이다.
# 
# ```python
# print(linecount('./codes/wc.py'))
# ```
# 
# `linecount` 함수는 인자로 지정된 파일에 포함된 내용의 줄 수(line number)를 계산해서 내준다.
# 따라서 위 명령문은 `wc.py` 파일에 포함된 내용이 몇 줄인가를 확인해준다.
# 
# 그런데 사실 `print(linecount('./codes/wc.py'))` 명령문은 `linecount` 함수가 
# 제대로 작동하는가를 확인하는 용도로 작성된 코드이며, 
# 모듈을 불러와서 활용하기 위해서는 굳이 실행할 필요가 없다.
# 이런 경우에 모듈의 `__name__` 속성을 이용하여 아래와 같이 작성하면 모듈을 임포트할 때 굳이 실행할 필요가 
# 없는 코드를 모듈에 포함시킬 수 있다.
# 
# ```python
# if __name__ == '__main__':
#     print(linecount('./codes/wc.py'))
# ```
# 
# 위와 같이 작성하면 `import wc`를 실행해도 `if __name__ == '__main__':`에 포함된 코드는 실행되지 않는다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/wc5.png" style="width:600px;"></div>

# 반면에 터미널을 이용해서 현재 작업 디렉토리에서  `python codes/wc.py` 형태로 `wc.py` 코드를 직접 실행하면 
# `if __name__ == '__main__'` 조건문의 본체가 실행된다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/pybook/master/notebooks/images/wc4.png" style="width:600px;"></div>

# `__main__` 함수의 이런 기능은 C, Java 등에서 의무적으로 사용되는 `main` 함수와 유사한 기능을 수행한다. 
# `Repl.it` 사이트에서 main 모듈이 기본적으로 실행되는 이유가 이런 전통에서 유래한다.

# ### 모듈 다시 불러오기

# 한 번 불러온 모듈을 다시 불러오면 모듈 내용이 또 실행되지는 않는다.

# In[ ]:


import wc


# ### 불러온 모듈 활용하기

# 어떤 종류의 모듈이든 한 번 불러온 모듈을 활용하는 방법은 동일하다.
# 우리가 작성하고 불러온 `wc` 모듈에 포함된 `linecount` 함수를 활용하는 방법도 동일하다.
# 예를 들어, `wc.py` 파일에 포함된 코드의 줄의 수를 알고자 하면 아래와 같이 실행한다.

# In[ ]:


wc.linecount('./codes/wc.py')


# 반면에 `codes` 디렉토리에 포함된 `__init__.py` 파일은 비어있음을 아래와 같이 확인할 수 있다.

# In[ ]:


wc.linecount('./codes/__init__.py')


# ### 별칭 사용

# 패키지나 모듈 또한 종류에 상관없이 별칭을 사용할 수 있다.
# 예를 들어, `wc` 모듈을 `wordCount` 라고 별칭을 지정하면서 불러올 수 있다.

# In[ ]:


import wc as wordCount


# 이제는 `wc` 대신에 `wordCount`를 사용할 수 있다.

# In[ ]:


wordCount.linecount('./codes/wc.py')


# In[ ]:


wordCount.linecount('./codes/__init__.py')


# ## 연습문제 

# 1. ...
