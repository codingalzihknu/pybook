#!/usr/bin/env python
# coding: utf-8

# # 마크다운과 주피터 노트북

# ```{note}
# kgkgk
# ```

# ```{admonition} 참고
# 변수 할당은 **컴퓨터 메모리** 상에서 이루어지며,
# 변수들과 변수들에 할당된 값들 사이의 관계는 **프레임**(frames)을 통해 관리된다.
# 즉, 변수 할당 명령문을 실행하면 컴퓨터 메모리 상에서 변수들과 변수들에 할당된 값들 사이의 관계에
# 변화가 발생하며, 이는 프레임에 변화를 초래한다.
# 
# 컴퓨터 메모리 상에서 일어나는 변화를 사람이 직접 눈으로 볼 수는 없다. 
# 하지만 파이썬 튜터([https://pythontutor.com/](https://pythontutor.com/))가 프레임의 변화를 시각적으로 보여주는 기능을 지원한다.
# 앞서 변수 세 개의 할당을 실행하면 프레임이 어떻게 변화하는지를
# [pythontutor.com: 변수 할당](https://pythontutor.com/visualize.html#code=greetings%20%3D%20'%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94!'%0An%20%3D%2017%0Api%20%3D%203.1415926535897932&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)에 
# 접속해서 확인할 수 있다.
# 
# 파이썬튜터 사용법은 다음과 같다.
# 
# * 해당 사이트에 접속해서 코드 확인 및 수정 후 <kbd>Visualize Execution</kbd> 버튼을 누른다.
# 
# * 이후 화면에서 <kbd>Next></kbd> 버튼을 반복해서 누르면 
#     각각의 명령문이 차례대로 실행되는 과정에서 발생하는 프레임의 변화를 확인할 수 있다.
#     Global frame은 전역 변수를 담당하는 전역 프레임을 가리킨다.
#     전역 변수에 대한 정의는 이후에 다룬다.
# ```

# ```{list-table} 테이블 만들기
# :header-rows: 1
# :name: 테이블 예제
# 
# * - Training
#   - Validation
# * - 0
#   - 5
# * - 13720
#   - 2744
# ```

# You can also create content with Jupyter Notebooks. This means that you can include
# code blocks and their outputs in your book.
# 
# ## Markdown + notebooks
# 
# As it is markdown, you can embed images, HTML, etc into your posts!
# 
# ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# 
# You can also $add_{math}$ and
# 
# $$
# math^{blocks}
# $$
# 
# or
# 
# $$
# \begin{aligned}
# \mbox{mean} la_{tex} \\ \\
# math blocks
# \end{aligned}
# $$
# 
# But make sure you \$Escape \$your \$dollar signs \$you want to keep!
# 
# ## MyST markdown
# 
# MyST markdown works in Jupyter Notebooks as well. For more information about MyST markdown, check
# out [the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
# or see [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).
# 
# ## Code blocks and outputs
# 
# Jupyter Book will also embed your code blocks and output in your book.
# For example, here's some sample Matplotlib code:

# In[1]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# In[2]:


# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
