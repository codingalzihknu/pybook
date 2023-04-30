#!/usr/bin/env python
# coding: utf-8

# (ch:files)=
# # 파일

# 열 명의 5미터 다이빙 경기의 점수를 저장한 텍스트 파일에서 
# 필요한 정보를 추출하는 과정을 살펴본다.
# 파일의 내용은 다음과 같이 첫째 줄엔 '이름'과 '점수'라는 구분이 표시되어 있으며,
# 둘째 줄부터 총 열 명의 이름과 점수가 기록되어 있다.
# 이름과 점수는 공백<font size='2'>space</font>로 구분된다.
# 
# ```
# 이름  점수
# 권준기  7.13
# 김세윤  8.55
# 나진서  9.02
# 마동탁  8.35
# 서길석  7.86
# 이준용  8.17
# 이차승  9.33
# 차승연  7.11
# 표방호  8.57
# 한석준  8.93
# ```

# ## 파일의 종류와 경로

# **텍스트 파일과 바이너리 파일**
# 
# 파일은 **텍스트**<font size='2'>text</font> 파일과 
# **바이너리**<font size='2'>binary</font> 파일 두 가지로 나뉜다.
# 
# 바이너리 파일은 한컴 오피스의 한글 파일, MS 워드 파일과 파워포인트 파일,
# jpg, png, gif 등의 사진 파일 등 특정 소프트웨어를 사용해야만 
# 내용을 확인할 수 있는 파일이다.
# 그리고 exe 확장자를 갖는 앱 설치 파일 등도 바이너리 파일이다.
# 
# 반면에 텍스트 파일은 내용을 확인하기 위해 특별한 기능이 필요 없고
# 임의의 텍스트 편집기로 내용을 바로 확인할 수 있다.
# 예를 들어 파이썬 편집기로 열 수도 있다.
# 여기서는 텍스트 파일만을 대상으로 파일 다운로드, 열기, 수정하기 등을 살펴본다.

# **디렉토리와 폴더**
# 
# 디렉토리<font size='2'>directory</font>와 폴더<font size='2'>folder</font>는 동일한 개념이다. 
# 다만 리눅스 계열 운영체제에서는 디렉토리를, 윈도우 운영체제에서는 폴더를 선호한다.
# 그리고 리눅스 계열 운영체제에서는 디렉토리를 파일이라고 부르기도 한다.
# 하지만 여기서는 디렉토리를 폴더 개념으로만 사용하며 파일과는 구분한다.

# **경로**
# 
# 경로는 특정 디렉토리 또는 파일의 위치를 나타내는 문자열이다. 
# 사용하는 운영체제마다 표현 방법이 다르기에 조심해야 한다.
# 예를 들어 현재 파이썬 코드가 실행되는 디렉토리의 경로는 
# 리눅스와 윈도우의 경우 다음과 같이 다르게 표현된다.
# 
# - 리눅스의 경우: '/home/gslee/Documents/GitHub/pybook/jupyter-book'
# - 윈도우의 경우: 'C:\Users\gslee\Documents\GitHub\pybook\jupyter-book'
# 
# 하지만 `pathlib` 모듈의 `Path` 자료형을 이용하면 운영체제를 신경쓰지 않고 경로를 다룰 수 있다.

# **현재 작업 디렉토리**
# 
# 보통 `cwd` 라고 줄여서 사용되는 **현재 작업 디렉토리**<font size='2'>current working directory</font>는
# 현재 파이썬이 실행되는 디렉토리를 가리킨다. 
# 현재 작업 디렉토리를 다음과 같이 확인할 수 있다.

# In[1]:


import os

os.getcwd()


# **절대경로와 상대경로**
# 
# 앞서 언급한 두 개의 경로는 
# 운영체제의 맨 상위 디렉토리를 기준으로 하는 경로라는 의미에서 **절대경로**라 부른다.
# 반면에 **상대경로**는 현재 작업 디렉토리(cwd)를 기준으로 경로를 작성한다. 
# 만약에 cwd가 `Documents` 라면, 위 두 개의 경로의 상대경로는 다음과 같다.
# 
# - 리눅스의 경우: 'GitHub/pybook/jupyter-book'
# - 윈도우의 경우: 'GitHub\pybook\jupyter-book'
# 
# 아래와 같이 사용할 수 있다. 점(`.`)이 현재 작업 디렉토리를 가리킨다.
# 
# - 리눅스의 경우: './GitHub/pybook/jupyter-book'
# - 윈도우의 경우: '.\GitHub\pybook\jupyter-book'

# ## 파일 준비

# 먼저 위에서 언급된 파일을 다운 받아서 파이썬 코딩을 실습하는 디렉토리에 저장한다.
# 여기서는 `data`라는 하위디렉토리에 `results5m.txt`라는 파일로 저장한다.

# **`pathlib.Path` 클래스: 디렉토리 지정**
# 
# 파일을 저장할 디렉토리를 지정한다.
# 이를 위해 `pathlib` 모듈의 `Path` 클래스를 이용한다.
# `Path` 클래스는 지정된 디렉토리 또는 파일의 경로를 담은 객체를 생성한다.
# 
# - `Path()` : 현재 작업 디렉토리를 나타내는 객체. `Path('.')` 과 동일한 의미임.
# - 슬래시 연산자 `/`: 두 개의 경로를 이어붙히는 연산자. 왼쪽 인자는 `Path` 객체, 둘째 인자는 문자열.

# In[2]:


from pathlib import Path

data_path = Path() / "data"


# `Path` 객체는 다양한 정보를 다루는 메서드와 속성을 제공한다.
# 예를 들어, 현재 작업 디렉토리(cwd)의 경로를 확인하려면 `cwd()` 메서드를 실행한다.

# In[3]:


data_path.cwd()


# `name` 속성은 경로가 가리키는 디렉토리 또는 파일 이름을 가리킨다. 

# In[4]:


data_path.name


# `parent` 속성은 지정되 경로가 가리키는 디렉토리 또는 파일이 저장된 부모 디렉토리의 이름을 가리킨다.
# `data_path` 가 현재 디렉토리의 하위 디렉토리인 `data`를 가리키기에
# 그것의 부모 디렉토리인 현재 디렉토리를 가리키는 점(`'.'`) 이 저장된다.

# In[5]:


data_path.parent


# **`Path.mkdir()` 메서드: 디렉토리 생성**
# 
# `Path` 객체의 `mkdir()` 메서드를 이용하여 지정된 경로에 해당하는 디렉토리를 실제 생성한다. 
# 다음 두 개의 옵션 인자를 사용한다.
# 
# - `parent=True`: 부모 디렉토리가 필요하면 생성할 것. 즉, 파일이 여러 개의 중첩된 폴더 안에 위치하는 경우 사용.
# - `exist_ok = True`: 디렉토리가 이미 존재하면 그대로 사용할 것. 지정된 디렉토리가 이미 존재하는데 `False`로 설정하면 오류 발생.

# In[6]:


data_path.mkdir(parents=True, exist_ok=True)


# **`urllib.request.urlretrieve()` 함수: 파일 다운로드**
# 
# 인터넷에 존재하는 파일을 지정된 이름으로 다운로드 한다.
# 이를 위해 `urllib.request` 모듈의 `urlretrieve()` 함수를 이용한다.
# 
# - 첫째 인자: 다운로드할 파일 주소
# - 둘째 인자: 저장할 디렉토리와 파일명으로 구성된 경로
# - 반환값: 저장된 파일의 경로와 다운로드에 사용된 웹브라우저 등에 대한 정보로 구성된 튜플.
#     파일 경로에 표시되는 `PosixPath` 또는 `WindowsPath` 는 
#     각각 리눅스 계열 방식의 경로와 윈도우 방식의 경로를 가리키며
#     사용하는 운영체제에 따라 결정된다.

# In[7]:


from urllib.request import urlretrieve

# 파일 서버 기본 주소
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
# 파일명
file_name_5m = "results5m.txt"
# 파일 주소 전체
file_url_5m = base_url + file_name_5m

# 저장위치와 저장 파일명
target_path_5m = data_path / "results5m.txt"

# 다운로드와 저장 실행
urlretrieve(file_url_5m, target_path_5m)


# **파일 다운로드 함수**
# 
# 앞으로 파일의 이름만 달리하면서 동일한 웹 사이트에서 여러 파일을 다운로드 할 것이다.
# 따라서 다운로드할 파일의 이름만 지정하면 지정된 경로에 동일한 이름으로
# 다운로드하여 저장하는 함수를 선언하는 것이 좋다.
# 
# 아래 `myWget()` 함수의 인자는 다운로드할 파일명을 사용할 것이기에 위 코드에서 파일명을 제외한 
# 나머지는 거의 동일하게 사용된다.

# In[8]:


def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장위치 지정과 생성
    data_path = Path() / "data"
    data_path.mkdir(parents=True, exist_ok=True)
    
    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)


# 앞서의 긴 코드가 다음 한 줄 코드로 대체된다.

# In[9]:


myWget("results5m.txt")


# **`open()` 함수: 저장된 파일 불러오기**

# 컴퓨터에 저장된 파일을 활용하려면 먼저 파일 객체로 불러와야 한다.
# 가장 기본적인 방식으로 `open()` 함수를 이용하여
# 불러온 파일 객체를 변수에 할당한다.
# 
# ```python
# f = open(파일경로) 
# ```
# 
# 다운로드가 잘못 되었거나 다른 곳에 저장되어 있다면 오류가 발생한다.
# 따라서 코드의 안전할 실행을 위해 많은 경우 다음처럼 `try-except` 명령문을 
# 이용하여 예외처리를 하기도 한다. 
# `FileNotFoundError` 는 지정된 파일이 존재하지 않을 때 발생하는 오류를 가리킨다.
# 
# ```python
# try:
#     f = open(파일경로) 
# except FileNotFoundError:
#     print("열고자 하는 파일이 존재하지 않습니다.")
# ```
# 
# 하지만 여기서는 그냥 간단한 버전을 사용한다.

# In[10]:


f = open(target_path_5m, encoding='utf-8')


# 위 코드에서 `encoding='utf-8'`은 한글, 스페인어 등 영어 등에서 사용하지 않는 특수 문자를 사용하는 언어로
# 작성된 문서를 불러올 때 사용한다.

# **파일 내용 확인**

# `f` 변수가 가리키는 값의 자료형은 `_io.TextIOWrapper` 라는 
# 이름도 생소한 자료형이다.

# In[11]:


type(f)


# 자료형은 전혀 중요하지 않다.
# 대신 파일에 저장된 내용을 확인하려면 아래와 같이 `for` 반복문을 
# 사용해야 한다는 점은 기억해야 한다.

# In[12]:


for line in f:                   # 한줄씩 내용 출력하기
    print(line)


# 불러온 파일 객체는 한 번만 사용할 수 있는 {ref}`이터레이터 <sec:iterators>`이다. 

# In[13]:


from collections.abc import Iterator

isinstance(f, Iterator)


# `for` 반복문을 다시 실행하면 더 이상 보여주는 게 없다.
# 이유는 이터레이터의 내용을 모두 보여줬기 때문이다.

# In[14]:


for line in f:
    print(line)


# 불러온 파일을 다 사용했으면 닫아 주어야 한다.

# In[15]:


f.close()


# **`with-as` 키워드 활용**
# 
# 파일을 불러오고 할 일을 다하면 파일 닫기를 자동으로 처리하는 다음 방식으로 진행하는 것이 권장된다.

# In[16]:


with open("./data/results5m.txt") as f:
    for line in f: 
        print(line)


# **줄 간격 조절**

# 줄 간격이 넓은 이유는 파일을 작성하면서 줄바꾸기를 할 때 사용하는 엔터에 의해 줄바꾸기 기호(`\n`)가
# 각 줄의 맨 끝에 포함되어 있기 때문이다. 
# `print()` 함수 자체가 출력할 때마다 기본적으로 줄바꿈을 수행하기에 이로 인해 
# 결국 줄바꿈이 두 번 이뤄진다.
# 
# 줄바꾸기를 한 번 더 하는 것을 방지하기 위해서 문자열 자료형의 `strip()` 메소드를 활용하여
# 문자열의 양 끝에 있는 공백과 줄바꿈 기호를 없앨 수도 있다.
# 그리고 `mode='r'` 옵션인자를 이용하여 읽기 모드임을 명시하는 게 좋다.
# 
# 언급한 것을 모두 반영하여 파일을 불러오고 내용을 확인하는 코드는 다음과 같다.

# In[17]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    for line in f: 
        print(line.strip())


# **`read()`, `readline()`, `readlines()` 메서드**
# 
# `read()` 메서드는 파일 내용을 전체를 하나의 문자열로 불러온다.

# In[18]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    lines = f.read()
    
lines


# `print()` 함수를 이용하면 줄바꿈 기호 등을 해석하여 보다 예쁘게 출력한다.

# In[19]:


print(lines)


# `readline()` 메서드는 한 줄씩 반환한다. 일종의 이터레이터의 `__next__()` 메서드와 유사하다.

# In[20]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    for _ in range(11):
        print(f.readline().strip())


# `readlines()` 메서드는 파일 내용 전체를 리스트로 반환한한다.
# 리스트의 각 항목은 한 줄씩 채워진다.

# In[21]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    
lines


# In[22]:


for line in lines:
    print(line.strip())


# **`Path.open()` 메서드: 저장된 파일 불러오기**
# 
# `Path` 객체의 `open()` 메서드를 이용하여 파일을 열 수도 있다.
# 사용법은 기본적으로 동일하다.
# 실제로 `Path` 객체의 `open()` 메서드를 호출하면 `open()` 함수가 실행된다.

# In[23]:


with target_path_5m.open(mode='r', encoding='utf-8') as f:
    for line in f: 
        print(line.strip())


# **`mode` 옵션 인자**

# 파일을 열 때 기본적으로 읽기 모드로 열린다.
# 그러면 파일 내용을 읽을 수는 있지만 수정, 추가 등은 불가능하다.
# 수정 및 추가 등을 지원하려면 파일을 열 때 읽기 모드가 아닌 다른 모드로 열어야 한다.
# 지원되는 모드는 다음과 같다.
# 
# | 모드 옵션 | 기능 |
# | :--- | :--- |
# | 'r' | 파일 처음부터 읽기 |
# | 'w' | 새 파일 생성 후 쓰기 또는 기존 파일 내용 삭제 후 새로 쓰기 |
# | 'a' | 기존 파일 끝에 추가하기 |
# | 'r+' | 기존 파일 처음부터 읽기 및 쓰기. 기존 파일 없으면 새로 생성|
# | 'w+' | 새 파일 생성 후 쓰기 및 읽기. 기존 파일 내용 삭제 후 새로 쓰기 및 읽기 |
# | 'a+' | 기존 파일 끝에 추가와 읽기 |

# ## 텍스트 파일 생성

# 10명 선수들의 5미터 다이빙 기록 이외에 아래 10미터 다이빙 기록이 담긴 `results10m.txt` 파일이 존재한다.
# 
# ```
# 이름  점수
# 권준기  9.11
# 김세윤  8.35
# 나진서  7.12
# 마동탁  8.65
# 서길석  9.31
# 이준용  8.71
# 이차승  7.33
# 차승연  9.11
# 표방호  8.75
# 한석준  8.39
# ```

# 아래 방식으로 5미터 기록과 10미터 기록을 함께 담은 `diving_results.txt` 파일을 생성해보자.
# 
# ```
# 이름  5m점수  10m점수
# 권준기  7.13  9.11
# 김세윤  8.55  8.35
# 나진서  9.02  7.12
# 마동탁  8.35  8.65
# 서길석  7.86  9.31
# 이준용  8.17  8.71
# 이차승  9.33  7.33
# 차승연  7.11  9.11
# 표방호  8.57  8.75
# 한석준  8.93  8.39
# ```

# 먼저 `results10m.txt` 파일을 `results5m.txt` 와 동일한 방식으로 다운로드하여 저장한다.

# In[24]:


myWget("results10m.txt")


# `diving_results.txt` 텍스트 파일에 채울 내용을 준비하자.
# 그러기 위해 파일로부터 이름과 점수를 키와 값으로 사용하는 사전을 생성한다.
# 이를 위해 파일을 불러오기 위해 `open()` 함수 또는 `Path` 객체의 메서드 둘 다 이용할 수 있지만 
# 여기서는 메서드를 사용한다.

# In[25]:


with target_path_5m.open() as f:
    results_5m_dict = {}
    for line in f:
        name, score = line.strip().split()
        if score != '점수':
            results_5m_dict[name] = score
        
results_5m_dict


# In[26]:


with open("data/results10m.txt") as f:
    results_10m_dict = {}
    for line in f:
        name, score = line.strip().split()
        if score != '점수':
            results_10m_dict[name] = score
        
results_10m_dict


# 두 개의 점수로 이루어진 튜플을 값으로 사용하는 사전을 생성한다. 

# In[27]:


diving_results_dict = {}

for name in results_5m_dict:
    score_5m = results_5m_dict[name]
    score_10m = results_10m_dict[name]
    diving_results_dict[name] = (score_5m, score_10m)


# In[28]:


diving_results_dict


# **파일 객체의 `write()` 메서드**

# 이제 `diving_results.txt` 텍스트 파일을 생성할 수 있다.
# 이를 위해 `open()` 함수를 `'w'` 모드로 연 다음에 
# 앞서 생성된 사전의 키와 값을 적적히 조합하여 파일에 한 줄씩 추가한다.
# 파일에 한 줄을 추가하는 기능은 `write()` 메서드를 이용한다.

# In[29]:


with open(data_path / "diving_results.txt", "w") as f:
    f.write("이름  5m점수  10m점수\n")
    for key, scores in diving_results_dict.items():
        score1, score2 = scores
        line = key + "  " + score1 + "  " + score2 + "\n"
        f.write(line)


# In[30]:


with open("data/diving_results.txt", 'r') as f:
    for line in f:
        print(line.strip())


# (sec:exp-diving-5m)=
# ## 활용 예제: 종목별 등수 확인

# 선수들의 5미터 다이빙 점수를 기준으로 등수를 확인해보자.

# **리스트 활용**

# 단순히 몇 등 점수를 확인하려면 점수만으로 구성된 리스트를 생성한 후에 정렬하면 된다.
# 첫째줄은 점수가 아니기에 `float()` 함수를 적용하면 오류가 발생한다.
# 따라서 `try-except`, `continue` 두 명령문을 이용하여 무시하도록 한다.
# 
# 아래 코드의 `scores_5m` 변수가 선수들의 5미터 다이빙 경기의 점수를 담는다.

# In[31]:


# 5m 점수 저장
scores_5m = []

with open("data/diving_results.txt", 'r') as f:
    for line in f:
        s_5m = line.split()[1]
        try:
            scores_5m.append(float(s_5m))
        except:
            continue


# 모든 선수의 5미터 다이빙 점수는 다음과 같다.

# In[32]:


scores_5m


# 점수를 내림차순으로 정렬하면 쉽게 1, 2, 3 등의 점수를 얻는다.

# In[33]:


scores_5m.sort(reverse=True)             # 리스트를 크기 기준 내림차순으로 정렬

print("1, 2, 3등의 점수는 다음과 같습니다.\n") 
print(f"1등: {scores_5m[0]}")             # 1등 점수 = 0번 인덱스 값
print(f"2등: {scores_5m[1]}")             # 2등 점수 = 1번 인덱스 값
print(f"3등: {scores_5m[2]}")             # 3등 점수 = 2번 인덱스 값


# 위 코드는 어떤 선수가 몇 등인가를 얘기해주진 않는다. 
# 선수 이름과 점수 사이의 관계를 담은 정보가 리스트에 포함되지 않기 때문인데,
# 사전을 이용하면 해당 정보를 함께 담을 수 있다.

# In[34]:


# 5m 다이빙 점수 저장. 
# 키: 선수 이름
# 값: 점수

scores_5m = {}

with open("data/diving_results.txt", 'r') as f:
    for line in f:
        name, s_5m = line.split()[:2]  # 리스트 해체 활용
        
        try:
            scores_5m[name] = float(s_5m)
        except:
            continue


# 모든 선수의 5미터 다이빙 점수는 다음과 같다.

# In[35]:


scores_5m


# 이제 점수 기준으로 사전을 정렬해보자. 
# 그런데 사전 자체는 정렬 기능을 제공하지 않는다.
# 반면에 `items()` 메서드의 반환값에 대해 `sorted()` 함수를 적용한 결과를 응용할 수는 있다.
# `key` 키워드 인자를 이용해서 아이텀의 둘째 인자인 점수를 기준으로 정렬하려면
# 다음과 같이 정의된 익명 함수를 지정한다.

# In[36]:


sorted_scores_5m = sorted(scores_5m.items(), key = lambda item: item[1], reverse=True)
sorted_scores_5m


# 5미터 다이빙 경기 결과는 다음과 같다.

# In[37]:


print("5미터 다이빙 경기 결과\n")

count = 1
for item in sorted_scores_5m:
    print(f"{count:>3}등: {item[0]} {item[1]}")
    count += 1


# ## 연습문제

# 참고: [(실습) 파일](https://colab.research.google.com/github/codingalzi/pybook/blob/master/practices/practice-files.ipynb)
