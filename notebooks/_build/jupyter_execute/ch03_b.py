#!/usr/bin/env python
# coding: utf-8

# # 모음 자료형 1편

# **모음**<font size="2">collection</font> 자료형은
# 여러 개의 값을 하나로 묶어 놓은 값의 유형이다.
# 파이썬은 문자열, 리스트, 튜플, 집합, 사전 등의 모음 자료형을
# 기본으로 제공하며,
# 여러 값을 묶어 둔다는 의미로 모음 자료형의 값을
# **컨테이너**<font size="2">container</font>라고도 부른다.
# 
# 모음 자료형은 크게 두 종류로 나뉜다.
# 
# - 순차형<font size="2">sequence type</font>: 포함된 항목들의 순서를 가리는 모음 자료형
#     - 문자열
#     - 리스트
#     - 튜플
# - 집합형<font size="2">set type</font>: 포함된 항목들의 순서를 무시하는 모음 자료형
#     - 집합
#     - 사전
#     
# 먼저 순차형을 소개한다.

# ## 문자열

# **문자열**<font size="2">string</font>은 문자 기호로 이루어진 단어, 문장 등을 가리킨다.
# 키보드에 포함된 영문 알파벳, 한글 자음과 모음 등을 기본적으로 사용한다.
# 문자열은 세 가지 방식으로 작성될 수 있다.

# - 작은 따옴표 활용

# In[1]:


s = '안녕하세요.'
print(s)


# - 큰 따옴표 활용

# In[2]:


s = "안녕하세요."
print(s)


# - 연속된 세 개의 작은 또는 큰 따옴표 활용: 여러 줄로 이루어진 문자열 작성

# In[3]:


s = '''안녕.
잘 지내?'''

print(s)


# In[4]:


s = """안녕.
잘 지내?"""

print(s)


# 스페이스와 탭을 활용해서 생성된 여백<font size="2">white space</font>도 문자열로 처리된다.
# 또한 줄바꿈을 나타내는 문자는 `\n`이다.

# In[5]:


s = '''안녕.
    잘 지내?'''

print(s)


# In[6]:


s = """안녕.
    잘 지내?"""

print(s)


# :::{admonition} 유니코드
# :class: info
# 
# 키보드 상에 존재하지 않는 다른 기호나 문자도 **유니코드**<font size="2">unicode</font> 
# 형식으로 지원된다.
# 대표적으로 서유럽 언어에서 많이 사용되는 
# &#xE0;, &#xE2;, &#xE7;, &#xE8;,&#xFC; 등 특수 알파벳 등이
# 유니코드로 지원된다.
# 
# 또한 이모티콘도 지원된다. 
# 예를 들어 웃는 얼굴의 이모티콘을 나타내는 문자열은 다음과 같다. 
# 
# ```python
# >>> s = '\U0001f600'
# >>> s
# '😀'
# >>> s * 2
# '😀😀'
# ```
# 
# 유니코드로 지원되는 모든 이모티콘은 [Emoji Charts](https://unicode.org/emoji/charts/emoji-list.html)에서
# 확인할 수 있다. 단, `U+`로 시작하는 부분을 `U000` 으로 대체해서 사용해야 한다. 
# :::

# ### 백슬래시와 이스케이프 문자

# 문자열 자체에 따옴표가 포함되면 조심해야 한다.
# 예를 들어, 작은 따옴표가 포함된 문자열을 다음과 같이 지정하면 오류가 발생한다.
# 
# ```python
# >>> s = 'Python's grammar'
#   File "<stdin>", line 1
#     s = 'Python's grammar'
#                 ^
# SyntaxError: invalid syntax
# ```
# 
# 이유는 작은 따옴표로 문자열의 시작을 지정했기 때문에
# `Python's` 문장에 사용된 작은 따옴표가 
# 문자열의 끝을 의미하게 되는데
# 이후에도 문자열이 이어지게 되어 결국 문자열의 끝이 불분명해져서
# 구문 오류를 뜻하는 `SyntaxError`가 발생한다.
# 
# 이런 종류의 오류를 방지하는 다양한 방식이 존재하지만,
# 여기서는 **백슬래시**<font size="2">backslash</font> 기호 (`\`)를 
# 따옴표 바로 앞에 추가하는 방식만 소개한다.

# In[7]:


s = 'Python\'s grammer'
print(s)


# :::{admonition} 슬래시 기호(&#x5C;)와 원화 기호(&#x20a9;)
# :class: info
# 
# 백슬래시 키는 키보드의 <kbd>Enter</kbd> 키 바로 위에 위치하는데
# 한글 키보드의 경우 원화 기호 키 <kbd>&#x20a9;</kbd> 가 대신 
# 자리잡고 있을 수 있다.
# 그리고 모니터 화면에도 사용하는 운영체제의 언어 설정에 따라
# 원화 기호(&#x20a9;)와 백슬래시 기호(&#x5C;) 둘 중에 하나로만 보인다.
# 하지만 단순한 언어 설정의 차이일 뿐 기능은 동일하다.
# :::

# 백슬래시는 이처럼 특정 문자와 함께 사용되면 특별한 기능을 갖는
# **이스케이프 문자**<font size="2">escape character</font>를 구성한다.
# 가장 많이 사용되는 이스케이프 문자의 목록은 다음과 같다.
# 
# | 이스케이프 문자 | 의미 |
# | :---: | :---:    |
# | `\'` | 작은 따옴표 |
# | `\"` | 큰 따옴표 |
# | `\\` | 백슬래시 기호 |
# | `\n` | 줄바꿈 |
# | `\t` | 탭 |

# ### 문자열 포매팅

# f-포매팅 소개 필요!

# ### 문자열 메서드

# 참고: [https://hj617kim.github.io/pybook/ch11.html](https://hj617kim.github.io/pybook/ch11.html)

# ### 문자열 인덱싱 

# 참고: [https://hj617kim.github.io/pybook/ch11.html](https://hj617kim.github.io/pybook/ch11.html)

# ## 리스트

# 리스트<font size="2">list</font>는 여러 종류의 값을 순서지어 포함한다.
# 포함되는 항목의 개수에 제한이 없다.

# In[8]:


colors = ['red', 'blue', 'green', 'black', 'white']
type(colors)


# ## Tuples

# Tuples are basically immutable lists. The elements of a tuple are written
# between parentheses, or just separated by commas
# 
# ```python
# >>> t = 12345, 54321, 'hello!'
# >>> t[0]
# 12345
# >>> t
# (12345, 54321, 'hello!')
# >>> u = (0, 2)
# ```

# ## 인덱싱

# 순차형 컨테이너는 모두 정수를 이용하여 항목을 확인하고, 
# 경우에 따라 항목을 다른 값으로 변경하는
# **인덱싱**<font size="2">indexing</font> 기능을 갖는다.
# 
# 왼편에 위치한 항목으로부터 차례대로 0, 1, 2, ... 등의 
# **인덱스**<font size="2">index</font>를 다음과 같이 사용한다.

# ### 문자열 인덱싱 

# Strings are collections like lists. Hence they can be indexed and
# sliced, using the same syntax and rules.
# 
# Indexing
# 
# ```python
# >>> a = "hello"
# >>> a[0]
# 'h'
# >>> a[1]
# 'e'
# >>> a[-1]
# 'o'
# ```

# (Remember that negative indices correspond to counting from the right
# end.)

# Slicing
# 
# ```python
# >>> a = "hello, world!"
# >>> a[3:6] # 3rd to 6th (excluded) elements elements 3, 4, 5
# 'lo,'
# >>> a[2:10:2] # Syntax a[startstopstep]
# 'lo o'
# >>> a[3] # every three characters, from beginning to end
# 'hl r!'
# ```

# ### 리스트 인덱싱 

# In[9]:


colors[0]


# In[10]:


colors[1]


# In[11]:


colors[2]


# :::{admonition} 인덱스는 0부터 시작!
# :class: warning
# 
# 가장 왼편에 위치한 항목의 인덱스가 1이 아닌 0임에 주의해야 한다.
# 순차 자료형의 가장 왼편에 위치한 값으로부터 첫째, 둘째, 셋째 등으로 
# 언급하는 반면에 인덱스는 0, 1, 2 등으로 사용해야 해서 
# 익숙해질 때까지 시간이 조금 걸린다.
# 
# C 언어 계열의 언어를 비롯하여 자바, 자바스크립트 등 대부분의 
# 프로그래밍 언어가 0부터 인덱스를 시작한다.
# 반면에 포트란<font size="2">Fortran</font>, 매트랩 등
# 수치 계산 전용 프로그래밍 언어는 인덱스를 1부터 시작한다. 
# 
# 참고로 인덱스를 0부터 시작해야 하는 논리적 이유는 없다.
# 누군가 어떤 이유로 그렇게 정했고 나름 이유가 있었겠지만 
# 사용 면에서 보면 어떤 논리적인 장점도 없다.
# :::

# -1, -2, -3, ... 등 음의 정수를 인덱스로 사용하면 오른편에 위치한 항목부터 
# 차례대로 왼쪽으로 이동하면서 인덱싱을 실행할 수 있다.

# In[12]:


colors[-1]


# `colors` 변수가 가리키는 리스트에 5개의 문자열이 포함되어 있기 때문에
# 왼편에서 넷째, 오른편에 둘째 항목은 동일한 문자열이 된다.

# In[13]:


왼쪽에서셋째 = colors[3]
오른쪽에서둘째 = colors[-2]

왼쪽에서셋째 == 오른쪽에서둘째


# :::{admonition} 한글 변수 이름
# :class: warning
# 
# 한글을 변수와 함수의 이름으로 사용할 수도 있다. 
# 하지만 다른 버전 또는 타 언어와의 호환성 등의 문제가 발생할 수 있기에
# 아직은 일반적이지 않으며 추천되지 않는다.
# :::

# 포함된 항목의 개수를 벗어나는 인덱스는 오류를 유발한다.
# `colors` 리스트가 5개의 항목을 포함하기에 사용할 수 있는 인덱스는 
# 왼편에서 시작하는 경우엔 0부터 4까지이고
# 오른편에서 시작하면 -1부터 -5까지이다. 
# 
# 예를 들어 5를 인덱스로 사용하면 왼편에서 여섯째 항목을 확인하기 때문에
# 인덱스의 범위를 벗어난다.
# 따라서 `index out of range` 라는 설명과 함께 `IndexError`가 
# 다음과 같이 발생한다.
# 
# ```python
# >>> colors[5]
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-3-5976064932c2> in <module>
# ----> 1 colors[5]
# 
# IndexError: list index out of range
# ```

# ## 슬라이싱

# 인덱스의 구간을 지정하여 순차 자료형의 일부를 추출하는 것을
# **슬라이싱**<font size="2">slicing</font>이라 한다.
# 
# 예를 들어 `colors` 리스트의 둘째부터 넷째 까지의 항목으로
# 구성된 리스트를 생성하려면 다음과 같이 한다.

# In[14]:


colors[1:4]


# `[1:4]` 는 1번 인덱스, 즉 둘째부터 4번 인덱스 이전까지, 즉 3번 인덱스인 넷째 항목까지 
# 추출 대상으로 삼는다는 의미이다.

# 슬라이싱의 일반 형식은 다음과 같다.
# 
# ```python
# colors[시작:끝:보폭]
# ```
# 
# **시작**과 **끝**의 의 의미는 `colors[1:4]`의 경우에서 설명한 것과 동일하다.
# 반면에 **보폭**은 항목 추출법을 설명한다.
# 예를 들어 2를 보폭으로 사용하면
# 시작 인덱스로 부터 2씩 건너 뛰며 항목을 추출한다.
# `colors[1:4:2]`는 따라서 1번, 3번 두 개의 인덱스에 위치한 항목을 추출해서 
# 리스트를 생성한다.

# In[15]:


colors[1:4:2]


# 시작, 끝, 보폭 모두 생략될 수 있으며 각각에 대해 기본값이 사용된다.
# 
# - 시작의 기본값: 0
# - 끝의 기본값: 항목의 개수 + 1. 즉, 시작부터 끝까지.
# - 보폭의 기본값: 1

# In[16]:


colors[3:]


# In[17]:


colors[:3]


# In[18]:


colors[::2]

