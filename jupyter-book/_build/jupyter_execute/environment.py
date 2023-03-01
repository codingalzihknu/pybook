#!/usr/bin/env python
# coding: utf-8

# # 프로그래밍 개발 환경

# 파이썬으로 프로그래밍을 하려면 적절한 개발환경을 준비해야 한다.
# 파이썬 프로그래밍 개발 환경은 크게 오프라인 환경과 온라인 환경으로 나뉜다.
# 
# - 온라인 개발 환경: 인터넷 브라우저를 이용하여 특정 서버에 접속해서 편집기와 파이썬 실행기를 활용하는 환경
# - 오프라인 개발 환경: 편집기와 파이썬 실행기를 PC에 직접 설치해서 활용하는 환경
# 
# 프로그래밍이 처음이라면 먼저 온라인 방식을 사용해서 파이썬과 어느 정도 친숙해진 다음에 오프라인 방식을 시도할 것을 추천한다.

# ## 온라인 개발 환경: 구글 코랩

# [구글 코랩<font size="2">Google Colab</font>](https://colab.research.google.com/?hl=ko)은 
# 구글에서 제공하는 파이썬 전용 온라인 주피터 노트북이다.
# 웹브라우저를 이용하여 어떤 준비 없이 바로 파이썬 프로그래밍을 시작할 수 있다.

# 구글 코랩의 간단한 사용법은 [유튜버 봉수골 개발자 이선비의 동영상](https://www.youtube.com/watch?v=91E0qenm7W4)을 참고한다.
# 그리고 입문용은 아니지만 구글 코랩만이 지원하는 유용한 고급 기능을 
# [TensorFlow 팀의 동영상](https://www.youtube.com/watch?v=rNgswRZ2C1Y)에서 확인할 수 있다.

# 구글 코랩을 사용하다 보면 
# 특정 라이브러리를 설치해야하는 경우가 발생할 수 있는데 그럴 때는 `pip` 파이썬 라이브러리 관리자를 
# 이용하여 설치하면 된다.
# 예를 들어 `beautifulsoup4` 라이브러리를 추가 설치하려면 아래 명령문을 주피터 노트북 코드셀에서 실행한다.
# 
# ```bash
# !pip install beautifulsoup4
# ```

# `pip`은 파이썬 명령어가 아니라 컴퓨터 운영체제 관리에 사용되는 쉘<font size='2'>shell</font> 명령어이다. 
# 이런 쉘 명령어를 터미널이 아닌 주피터 노트북 셀에서 실행하려면 느낌표(`!`)를 함께 사용한다.

# :::{admonition} 쉘과 터미널
# :class: info
# 
# 쉘<font size='2'>shell</font>은 컴퓨터 운영체제의 기능과 서비스를 관리하거나 
# 구현하는 데에 사용되는 명령문<font size='2'>command lines</font>을 실행하는 
# 실행기<font size='2'>interpreter</font>이다.
# 즉, 사용자와 컴퓨터 커널<font size='2'>kernel</font>을 연결하는 다리 역할을 수행한다.
# 쉘이 실행하는 명령문을 쉘 스크립트<font size='2'>shell script</font>라 부른다.
# 다양한 종류의 쉘이 존재하지만, 
# 리눅스의 기본 쉘인 bash(배시)와 맥 OSX의 zsh(Z 쉘)이 가장 많이 사용된다.
# 
# 반면에 터미널<font size='2'>terminal</font>은 쉘 스크립트를 작성하고 실행시킬 수 있는 
# 사용자 인터페이스<font size='2'>user interface</font>(UI)이며
# 콘솔<font size='2'>console</font>이라고도 불린다.
# 윈도우 사용자의 경우 아나콘다 패키지와 함께 설치된 `Anaconda Prompt (anaconda3)` 터미널을 이용할 수 있다.
# 
# - Anaconda Prompt (anaconda3) 실행하기
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/anaconda_prompt.jpg" style="width:750px"></div>
# 
# <br>
# 
# - Anaconda Prompt (anaconda3) 터미널
# 
# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/anaconda_prompt_start.jpg" style="width:750px"></div>
# :::

# ## 오프라인 개발 환경: 아나콘다

# ### 파이썬 설치

# 파이썬 개발환경 설치가 처음이라면 
# 데이터 분석 관련 중요 라이브러리, 스파이더 편집기, 주피터 노트북을 모두 포함하는
# [아나콘다<font size='2'>Anaconda</font> 파이썬 패키지](https://www.anaconda.com)를 추천한다.
# 자세한 설치 요령은 [아나콘다 설치](https://codingalzi.github.io/pybook/environment_setting.html#sec-anaconda-install)를
# 참고한다.

# ### 주피터 노트북 실행

# `Anaconda Prompt (anaconda3)` 등 임의의 터미널에서 아래 명령을 차례대로 실행하면 주피터 노트북<font size="2">Jupyter notebook</font>을 열거나 새로 작성할 수 있다.

# ```bash
# (base) $ jupyter notebook
# ```

# 윈도우 사용자는 아래 명령도 사용할 수 있다.

# ```bash
# (base) $ jupyter-notebook.exe
# ```

# 인터넷 브라우저에서 아래와 같이 주피터 서버가 실행되면 원하는 폴더에서 기존의 노트북을 실행, 수정하거나 새로운 주피터 노트북을 생성할 수 있다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/JupyterServer.jpg" style="width:750px"></div>

# :::{admonition} 주피터 노트북 사용법
# :class: info
# 
# [주피터 노트북 실행법](https://codingalzi.github.io/pybook/environment_setting.html#sec-jupyter-notebook)에서
# 간단한 사용법을 확인할 수 있다. 
# 아나콘다의 설치 과정과 주피터 노트북의 기초 사용법에 대한 보다 상세한 설명은 
# [유튜버 나도코딩의 동영상](https://www.youtube.com/watch?v=dJfq-eCi7KI&t=2298s)을 참고하면 좋다.
# :::

# ## 오프라인 통합 개발 환경(IDE)

# 시스템 개발 프로젝트를 진행하면 많은 코드 파일을 
# 작성하고 관리해야 한다.
# 이때 코드 편집과 실행, 디버깅, 파일 관리 등 
# 프로그래밍 관련 모든 작업을 통합해서 지원하는 
# 통합 개발 환경을 사용한다.
# 일명 **IDE**<font size="2">Interactive Development Environment</font>라고 불리는
# 통합 개발 환경을 지원하는 대표적인 상용 앱과 무료 앱은 다음과 같다.
# 
# * [파이참<font size="2">Pycharm</font>](https://www.jetbrains.com/pycharm): 가장 인기있는 상용 프로그램.
#     Pro 와 Community 두 버전을 지원하며 입문자는 무료 버전인 Community 추천.
# * [비주얼 스튜디오 코드<font size="2">Visual Studio Code</font>](https://code.visualstudio.com/docs/languages/python): 
#     마이크로소프트에서 지원하며, 현재 가장 인기 있는 무료 프로그램.
#     파이썬 뿐만 아니라 거의 모든 프로그래밍 언어를 위한 통합 개발 환경 지원.
# 
# 여기서는 일명 **VS Code**라 불리는 
# 비주얼 스튜디오 코드를 사용할 것을 추천한다.
# VS Code의 설치 과정과 사용법은 {ref}`sec:vs_code`와
# [생활코딩의 동영상](https://www.youtube.com/watch?v=K8qVH8V0VvY&t=337s)을
# 참고한다.

# ## IPython 소개

# ### 대화식 프로그래밍

# 주피터 노트북의 코드 셀<font size="2">code cell</font>은 
# 대화식 프로그래밍<font size="2">interactive programming</font>을 지원하는 
# [IPython](https://ipython.org)을 활용한다.
# Anaconda Prompt (anaconda3) 터미널에서 IPython 콘솔을 사용하는 방식은 다음과 같다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/anaconda_prompt-4.jpg" style="width:750px"></div>

# 아래 사진은 주피터 노트북의 코드 셀에서 IPython이 작동하는 형식을 보여준다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/jupyter-1.png" style="width:750px"></div>

# 반면에 파이썬이 기본으로 지원하는 python 콘솔은 다음 모양의 대화식 코딩을 지원한다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/anaconda_prompt-5.jpg" style="width:750px"></div>

# ### 매직 명령어

# IPython 콘솔은 파이썬 프로그래밍 이외에 보다 다양한 기능을 지원한다.
# 예를 들어 매직 명령어<font size='2'>magic commands</font>라는 명령어를
# 이용하여 파이썬 프로그래밍을 도와주는 특별한 기능을 수행할 수 있다.
# 
# 아래 사진은 무작위로 생성된 1000x1000 크기의 넘파이 행렬의 각 항목을 두 배하는 코드의 실행시간을 측정하는 `%timeit` 매직 명령문의 활용을 보여준다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/jupyter-2.png" style="width:750px"></div>

# 보다 다양한 매직 명령어와 주피터 노트북에서 사용할 수 있는 단축키에 대한 간략한 설명은 
# [IPython 기초](https://compmath.korea.ac.kr/appmath/PythonIPythonJupyterBasics.html#Jupyter-노트북)를 참고한다. 여기서는 앞으로 필요할 때 하나씩 소개한다.

# ### matplotlib 통합

# IPython은 주피터 노트북과 함께 사용될 때 장점이 극대화된다. 
# 특히 `matplotlib` 라이브러리를 이용한 데이터 시각화가 바로 지원된다.

# <div align="center"><img src="https://raw.githubusercontent.com/codingalzi/datapy/master/jupyter-book/images/jupyter-matplotlib-1.png" style="width:750px"></div>
