#!/usr/bin/env python
# coding: utf-8

# # 파일

# ## 파일 생성 및 저장

# ...

# ## 매직 커맨드와 주피터 노트북

# repl.it 에서 코드 작성후 RUN 한 후에 콘솔 창에서 파일 내용을 실행할 수 있는 기능을
# 주피터 노트북에서는 아래 예제에서 설명하는 방식으로 구현할 수 있다.

# :::{prf:example}
# :label: my_file
# 
# 아래 내용을 담은 *my_file.py* 파일을 작성하고 저장하라.
# 여기서는 *codes* 라는 하위 디렉터리(폴더)에 저장되어 있다고 가정한다.
# 
# ```
# s = 'Hello world'
# print(s)
# ```
# 
# 이제 주피터 노트북의 코드 셀에서 아래 명령문을 실행해보자.
# 
# ```python
# In [1]: %run codes/my_file.py
# 파이썬 안녕
# ```
# 
# `%run my_file.py`은 IPython에서 *my_file.py* 파일에 포함된 모든 코드를 실행한다.
# 그리고 이제는 코드에서 정의된 변수와 변수가 가리키는 값을 확인할 수 있다.
# 
# ```python
# In [2]: s
# Out[2]: 'Hello world'
# ```
# 
# `%whos`는 선언된 변수에 대한 정보를 보여준다.
# 여기서는 변수 `s`는 `'파이썬 안녕'` 이라는 문자열(`str`)을 가리키고 있음을 확인해준다. 
# 
# ```python
# In [3]: %whos
# Variable   Type    Data/Info
# ----------------------------
# s          str     파이썬 안녕
# ```
# :::
# 
# :::{admonition} 매직 커맨드
# :class: info
# 
# 퍼센트 기호 `%`로 시작하는 명령어는 파이썬 명령어가 아니며,
# 파이썬 코드 파일 및 디렉터리 경로 관리 등에 사용하는 IPython 전용 명령어이다.
# **매직 커맨드**<font size="2">magic command</font>라 불리며,
# 앞으로 기회될 때마다 하나씩 소개될 것이다.
# 매직 커맨드에 자세한 정보는 [IPython 공식 문서](https://ipython.readthedocs.io/en/stable/interactive/magics.html)에서 확인할 수 있다.
# :::
