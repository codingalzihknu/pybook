#!/usr/bin/env python
# coding: utf-8

# (ch:files)=
# # 파일

# 다이빙 선수 열 명의 5m 다이빙 경기의 점수 데이터를 저장한 텍스트 파일에서 
# 필요한 정보를 추출하는 과정을 살펴본다.
# 파일의 내용은 다음과 같이 첫째 줄엔 '이름'과 '점수'라는 구분이 표시되어 있으며,
# 둘째 줄부터 총 열 명의 이름과 점수가 기록되어 있다.
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
# 파일은 텍스트<font size='2'>text</font> 파일과 
# 바이너리<font size='2'>binary</font> 파일 두 가지로 나뉜다.
# 
# 바이너리 파일은 한컴 오피스의 한글 파일, MS 워드 파일과 파워포인트 파일,
# jpg, png, gif 등의 사진 파일 등 특정 소프트웨어를 사용해야만 
# 내용을 확인할 수 있는 파일이다.
# 그리고 exe 확장자를 갖는 앱 설치 파일 등도 바이너리 파일이다.
# 
# 반면에 텍스트 파일은 내용을 확인하기 위해 특별한 기능이 필요 없고
# 임의의 텍스트 편집기를 사용해도 내용을 바로 확인할 수 있다.
# 여기서는 텍스트 파일만을 대상으로 파이썬 코드를 이용하여 
# 파일 다운로드, 열기, 수정하기 등을 살펴본다.

# **경로**
# 
# 경로는 특정 디렉토리(폴더) 또는 파일의 위치를 나타내는 문자열이다. 
# 사용하는 운영체제마다 표현 방법이 다르기에 조심해야 한다.
# 예를 들어 현재 파이썬 코드가 실행되는 디렉토리의 경로는 
# 리눅스와 윈도우의 경우 다음과 같이 다르게 표현된다.
# 
# - 리눅스의 경우: '/home/gslee/Documents/GitHub/pybook'
# - 윈도우의 경우: 'C:\Users\gslee\Documents\GitHub\pybook'
# 
# 하지만 `pathlib` 모듈의 `Path` 자료형을 이용하면 운영체제를 신경쓰지 않고 경로를 다룰 수 있다.

# **디렉토리와 폴더**
# 
# 디렉토리<font size='2'>directory</font>와 폴더<font size='2'>folder</font>는 동일한 개념이다. 
# 다만 리눅스 계열 운영체제에서는 디렉토리를, 윈도우 운영체제에서는 폴더를 선호한다.
# 그리고 리눅스 계열 운영체제에서는 디렉토리를 파일이라고 부르기도 한다.
# 하지만 여기서는 디렉토리를 폴더 개념으로만 사용하며 파일과는 구분한다.

# ## 파일 준비

# 먼저 위에서 언급된 파일을 다운 받아서 파이썬 코딩을 실습하는 디렉토리에 저장한다.
# 여기서는 `data`라는 하위디렉토리에 `results5m.txt`라는 파일로 저장한다.

# **`pathlib.Path` 클래스: 디렉토리 지정**
# 
# 파일을 저장할 디렉토리를 지정한다.
# 이를 위해 `pathlib` 모듈의 `Path` 클래스를 이용한다.
# `Path` 클래스는 지정된 디렉토리 또는 파일의 경로를 담은 객체를 생성한다.
# 
# - `Path()` : 현재 디렉토리를 나타내는 객체. `Path('.')` 과 동일한 의미임.
# - 슬래시 연산자 `/`: 두 개의 경로를 이어붙히는 연산자. 왼쪽 인자는 `Path` 객체, 둘째 인자는 문자열.

# In[1]:


from pathlib import Path

data_path = Path() / "data"


# `Path` 객체는 다양한 정보를 다루는 메서드와 속성을 제공한다.
# 예를 들어, 현재 작업 디렉토리(current working directory)의 경로를 확인하려면 `cwd()` 메서드를 실행한다.

# In[2]:


data_path.cwd()


# `name` 속성은 경로가 가리키는 디렉토리 또는 파일 이름을 저장한다. 

# In[3]:


data_path.name


# `parent` 속성은 지정되 경로가 가리키는 디렉토리 또는 파일이 저장된 부모 디렉토리의 이름을 저장한다.
# `data_path` 가 현재 디렉토리의 하위 디렉토리인 `data`를 가리키기에
# 그것의 부모 디렉토리인 현재 디렉토리를 가리키는 점(`'.'`) 이 저장된다.

# In[4]:


data_path.parent


# **`Path.mkdir()` 메서드: 디렉토리 생성**
# 
# `Path` 객체의 `mkdir()` 메서드를 이용하여 지정된 경로에 해당하는 디렉토리를 실제 생성한다. 
# 다음 두 개의 옵션 인자를 사용한다.
# 
# - `parent=True`: 부모 디렉토리가 필요하면 생성할 것.
# - `exist_ok = True`: 디렉토리 이미 존재하면 그대로 사용할 것. 

# In[5]:


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
#     사용하는 운영체제 마다 둘 중에 한 방식으로 보여질 것이다.

# In[6]:


import urllib.request

# 파일 서버 기본 주고
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
# 파일명
file_name_5m = "results5m.txt"
# 파일 주소
file_url_5m = base_url + file_name_5m

target_path_5m = data_path / "results5m.txt"

urllib.request.urlretrieve(file_url_5m, target_path_5m)


# **파일 다운로드 함수**
# 
# 앞으로 파일의 이름만 달리하면서 동일 사이트에서 여러 파일을 다운로드 할 것이다.
# 따라서 위 코드를 다운로드할 파일의 이름만 지정하면 지정된 경로에 동일한 이름으로
# 다운로드하여 저장하는 함수를 선언하는 것이 좋다.
# 즉, 위 코드를 `myWget()` 함수로 캡슐화해보자.
# 
# 함수의 인자는 다운로드할 파일명을 사용할 것이기에 위 코드에서 파일명을 제외한 
# 나머지는 거의 동일하게 사용된다.

# In[7]:


def myWget(filename):
    base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
    file_url = base_url + filename

    target_path = data_path / filename

    return urllib.request.urlretrieve(file_url, target_path)


# **`open()` 함수: 저장된 파일 불러오기**

# 저장된 파일을 활용하려면 먼저 불러와야<font size='2'>loading</font> 한다.
# 가장 기본적인 방식으로 `open()` 함수를 이용하여
# 불러온 파일 객체를 변수에 할당한다.
# 
# ```python
# file = open(파일경로) 
# ```
# 
# 하지만 다운로드가 잘못 되었거나 다른 곳에 저장되어 있다면 오류가 발생한다.
# 따라서 코드의 안전할 실행을 위해 많은 경우 다음처럼 `try-except` 명령문을 
# 이용하여 예외처리를 하기도 한다. 
# `FileNotFoundError` 는 지정된 파일이 존재하지 않을 때 발생하는 오류를 가리킨다.
# 
# ```python
# try:
#     file = open(파일경로) 
# except FileNotFoundError:
#     print("열고자 하는 파일이 존재하지 않습니다.")
# ```
# 
# 여기서는 그냥 간단한 버전을 사용한다.

# In[8]:


f = open(target_path_5m)


# **파일 내용 확인**

# `f` 변수가 가리키는 값의 자료형은 `_io.TextIOWrapper` 라는 
# 이름도 생소한 자료형이다.

# In[9]:


type(f)


# 하지만 자료형은 전혀 중요하지 않다.
# 다만 파일에 저장된 내용을 확인하려면 아래와 같이 `for` 반복문을 
# 사용해야 한다는 점은 기억해야 한다.

# In[10]:


for line in f:                   # 각 줄 내용 출력하기
    print(line)


# 불러온 파일 객체는 한 번만 사용할 수 있는 이터레이터이다. 

# In[11]:


from collections.abc import Iterator

isinstance(f, Iterator)


# `for` 반복문을 다시 실행하면 더 이상 보여줄게 없다.

# In[12]:


for line in f:
    print(line)


# 불러온 파일을 다 사용했으면 닫아 주어야 한다.

# In[13]:


f.close()


# **`with-as` 키워드 활용**
# 
# 파일을 불러오고 할 일을 다하면 파일 닫기를 자동으로 처리하는 다음 방식으로 진행하는 것이 권장된다.

# In[14]:


with open("./data/results5m.txt") as f:
    for line in f: 
        print(line)


# 줄 사이가 넓은 이유는 파일을 작성하면서 줄바꾸기를 할 때 사용하는 엔터에 의해 줄바꾸기 기호(`\n`)가
# 각 줄의 맨 끝에 포함되어 있기 때문이다. 
# `print()` 함수 자체가 출력할 때마다 기본적으로 줄바꿈을 수행하기에 이로 인해 
# 결국 줄바꿈을 두 번한다.
# 
# 줄바꾸기를 한 번 더 하는 것을 방지하기 위해서 문자열 자료형의 `strip()` 메소드를 활용하여
# 문자열의 양 끝에 있는 공백과 줄바꿈 기호를 없앨 수도 있다.
# 또한 파일이 한글 문서를 담고 있다면 `open()` 메서드에 `encoding='utf-8'` 옵션 인자를 사용할 것을 추천한다.
# 그리고 `mode='r'` 옵션인자를 이용하여 읽기 모드임을 명시하는 게 좋다.
# 
# 언급한 것을 모두 반영하여 파일을 불러오고 내용을 확인하는 코드는 다음과 같다.

# In[15]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    for line in f: 
        print(line.strip())


# **`read()`, `readline()`, `readlines()` 메서드**
# 
# `read()` 메서드는 파일 내용을 전체를 하나의 문자열로 불러온다.

# In[16]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    lines = f.read()
    
lines


# `print()` 함수를 이용하면 줄바꿈 기호 등을 해석하여 보다 예쁘게 출력한다.

# In[17]:


print(lines)


# `readline()` 메서드는 한 줄씩 반환한다. 일종의 이터레이터의 `__next__()` 메서드와 유사하다.

# In[18]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    for _ in range(11):
        print(f.readline().strip())


# `readlines()` 메서드는 파일 내용 전체를 리스트로 반환한한다.
# 리스트의 각 항목은 한 줄씩 채워진다.

# In[19]:


with open("./data/results5m.txt", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    
lines


# In[20]:


for line in lines:
    print(line.strip())


# **`Path.open()` 메서드: 저장된 파일 불러오기**
# 
# `Path` 객체의 `open()` 메서드를 이용하여 파일을 열 수도 있다.
# 기본 사용법은 기본적으로 동일하다.
# 실제로 `Path` 객체의 `open()` 메서드를 호출하면 `open()` 함수가 실행된다.

# In[21]:


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
# | 'r+' | 새파일 생성 후 쓰기와 읽기. 기존 파일 내용 삭제 |
# | 'a+' | 기존 파일 끝에 추가와 읽기 |

# ## 텍스트 파일 생성

# 10명 선수들의 5m 다이빙 기록 이외에 아래 10m 다이빙 기록이 담긴 `results10m.txt` 파일이 존재한다.
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

# 아래 방식으로 5m 기록과 10m 기록을 함께 담은 `diving_results.txt` 파일을 생성해보자.
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

# In[22]:


myWget("results10m.txt")


# `diving_results.txt` 텍스트 파일에 채울 내용을 준비하자.
# 그러기 위해 파일로부터 이름과 점수를 키와 값으로 사용하는 사전을 생성한다.
# 이를 위해 파일을 불러오기 위해 `open()` 함수 또는 `Path` 객체의 메서드 둘 다 이용할 수 있지만 
# 여기서는 메서드를 사용한다.

# In[23]:


with target_path_5m.open() as f:
    results_5m_dict = {}
    for line in f:
        name, score = line.strip().split()
        if score != '점수':
            results_5m_dict[name] = score
        
results_5m_dict


# In[24]:


with open("data/results10m.txt") as f:
    results_10m_dict = {}
    for line in f:
        name, score = line.strip().split()
        if score != '점수':
            results_10m_dict[name] = score
        
results_10m_dict


# 두 개의 점수로 이루어진 튜플을 값으로 사용하는 사전을 생성한다. 

# In[25]:


diving_results_dict = {}

for name in results_5m_dict:
    score_5m = results_5m_dict[name]
    score_10m = results_10m_dict[name]
    diving_results_dict[name] = (score_5m, score_10m)


# In[26]:


diving_results_dict


# **파일 객체의 `write()` 메서드**

# 이제 `diving_results.txt` 텍스트 파일을 생성할 수 있다.
# 이를 위해 `open()` 함수를 `'w'` 모드로 연 다음에 
# 앞서 생성된 사전의 키와 값을 적적히 조합하여 파일에 한 줄씩 추가한다.
# 파일에 한 줄을 추가하는 기능은 `write()` 메서드를 이용한다.

# In[27]:


with open(data_path / "diving_results.txt", "w") as f:
    f.write("이름  5m점수  10m점수\n")
    for key, scores in diving_results_dict.items():
        score1, score2 = scores
        line = key + "  " + score1 + "  " + score2 + "\n"
        f.write(line)
    


# In[28]:


with open("data/diving_results.txt", 'r') as f:
    for line in f:
        print(line.strip())


# ## 점수 확인하기

# 이제 모든 줄이 동일한 모양을 갖고 있다는 점에 착안하여 아래와 같이 각각의 줄에 담긴 
# 내용 중에서 점수에 해당하는 부분을 아래와 같이 확인할 수 있다.
# 
# **주의:** 리스트의 색인도 문자열의 경우처럼 0부터 시작한다. 
# 따라서 리스트의 둘째 항목의 색인은 1인다.

# In[29]:


try:
    f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

for line in f: 
    record = line.split()          # 공백으로 쪼개기
    print(record[1])

f.close() 


# ### 1등 점수 확인하기

# 그런데 첫째 줄 내용은 점수를 비교하는 데에 필요없다. 
# 따라서 무시하는 방법을 사용하도록 하자.
# 특정 줄을 무시하려면 그 줄이 갖지 않는 특성을 활용해야 한다.
# 실제로 첫째 줄은 `Score`라는 문자열이고
# 둘째 줄부터는 부동소수점 모양의 문자열이다.
# 
# 1등 점수를 확인하려면 부동소수점 모양의 문자열이 아니라
# 진짜로 부동소수점을 다뤄야 한다.
# 따라서 `float` 함수를 이용하여 부동소수점 모양의 문자열을 
# 진짜 부동소수점으로 변환해야 하는데,
# 첫째줄에서 다음과 같은 `ValueError` 오류가 발생할 것이다.

# ```python
# >>> float('Score')
# ValueError                                Traceback (most recent call last)
# /tmp/ipykernel_3317/564178523.py in <module>
# ----> 1 float('Score')
# 
# ValueError: could not convert string to float: 'Score'
# ```

# 따라서 첫째 줄에서 이와같은 오류가 발생할 것을 예상하고
# 이를 예외처리 기법으로 다루면 첫째줄을 무시할 수 있으며,
# 예를 들어 다음과 같이 할 수 있다.
# 
# **참고:** `for` 또는 `while` 반복문에서 `continue` 명령문이 실행되면
# 실행을 정지하고 바로 해당 반복문의 처음으로 돌아가서 다음 반복을 실행한다.
# `continue`에 대한 보다 자세한 설명은 
# [처음코딩: break와 continue](https://opentutorials.org/course/2991/18056)를
# 참조한다.

# In[30]:


try:
    f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

highst_score = 0                   # 1등 점수 저장

for line in f: 
    record = line.split()

    try:                           # 첫째 줄 제외
        score = float(record[1])
    except ValueError:
        continue                   # 오류가 발생하는 줄 무시

    if highst_score < score:       # 1등 점수와 비교
        highst_score = score       # 1등 점수 갱신

f.close() 

print(f"1등은 {highst_score}점 입니다.")


# **주의:** `else` 명령문은 필요하지 않은 경우 생략이 가능하다.

# ### 2등, 3등 점수 확인하기

# 이제 2등 점수까지 확인해보자.
# 2등 점수를 기억할 변수가 하나 더 필요하며
# 확인된 점수가 기존의 1등 점수보다 큰지, 2등 점수보다 큰지 여부에 따라 
# 1, 2등 점수를 기억하는 변수의 값들을 
# 업데이트 해야 한다.

# In[31]:


try:
    f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

highst_score = 0
second_highst_score = 0                    # 2등 점수 저장

for line in f: 
    record = line.split()

    try: 
        score = float(record[1])
    except ValueError:
        continue

    if highst_score < score:
        second_highst_score = highst_score
        highst_score = score
    elif second_highst_score < score:      # 2등 점수와 비교
        second_highst_score = score        # 2등 점수 갱신

f.close() 

print(f"1등은 {highst_score}점 입니다.")
print(f"2등은 {second_highst_score}점 입니다.")


# 그런데 위와 같은 식으로 3등 점수까지 확인하려면 더 많은 변수와 조건문을 사용해야 하며,
# 코드가 점점 길어진다.

# In[32]:


try:
    f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

highst_score = 0
second_highst_score = 0
third_highst_score = 0                          # 3등 점수 저장

for line in f: 
    record = line.split()

    try: 
        score = float(record[1])
    except ValueError:
        continue

    if highst_score < score:
        third_highst_score = second_highst_score
        second_highst_score = highst_score
        highst_score = score
    elif second_highst_score < score:
        third_highst_score = second_highst_score
        second_highst_score = score
    elif third_highst_score < score:             # 3등 점수 확인
        third_highst_score = score               # 3등 점수 갱신

f.close() 

print(f"1등은 {highst_score}점 입니다.")
print(f"2등은 {second_highst_score}점 입니다.")
print(f"3등은 {third_highst_score}점 입니다.")


# ### 프로그램 구상 문제

# 4등, 5등, ... 점수는 어떻게 구하나?
# 위와 같은 방식으로 진행하면 유사한 명령문을 복사-붙이기 형식으로 
# 코드를 계속해서 수정해야 한다.
# 그런데 이렇게 원하는 등수에 따라 코드 자체가 수정되어야 한다면
# 프로그램 구상을 애초부터 잘못했다고 생각해야 한다.
# 
# 위 코드의 근본적인 문제는 선수들의 점수를 따라따로 관리하는 데에 있다.
# 각 선수의 점수를 다른 선수의 점수와 비교해야 하는데
# 선수들의 점수를 하나로 모아서 관리할 수 있으면 
# 선수들간의 비교를 보다 효율적으로 할 수 있다.
# 
# 따라서 선수의 기록을 모아서 한꺼번에 처리하는 기술이 요구된다.
# 여기서는 
# **[리스트](https://github.com/liganega/ProgInPython/blob/master/notebooks/PiPy04C-Lists.ipynb)** 
# 자료형을 활용하여 선수들의 점수를 모은 후
# 리스트 자료형의 메서드를 활용하여 선수들간의 점수를 비교하는 
# 보다 간단한 방법을 소개한다.

# ## 프로그램 업그레이드 1: 리스트 정렬 활용

# 몇 등 점수를 알아내야 하는가와 상관없이 동일하게 작동하는
# 프로그램을 구현한다.
# 
# 이를 위해 리스트를 활용하며, 프로그램 구상은 다음과 같다.
# 
# * 서핑 대회 참가선수들의 기록들을 모아 놓은 리스트를 생성한다.
# * 선수들의 기록을 점수 순으로 정렬한다.
# * 정렬된 점수에서 원하는 등수의 점수를 추출한다.

# ### 1, 2, 3 등 확인하기

# 리스트 풀어헤치기와 리스트 정렬 기법을 이용하여 1, 2, 3등을 아래와 같이 확인할 수 있다.

# In[33]:


try:
    f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

score_list = []                           # 점수 저장 용도 리스트 선언

for line in f: 
    name, score = line.split()            # 각 줄을 두 단어의 리스트로 쪼갠 후 풀어헤치기
    try:
        score_list.append(float(score))   # 첫째 줄 제외. 숫자만 scores 리스트에 추가
    except ValueError:
        continue

f.close() 

score_list.sort(reverse=True)             # 리스트를 크기 기준 내림차순으로 정렬

print("1, 2, 3등의 점수는 다음과 같습니다.\n") 
print(f"1등: {score_list[0]}")             # 1등 점수 = 0번 인덱스 값
print(f"2등: {score_list[1]}")             # 2등 점수 = 1번 인덱스 값
print(f"3등: {score_list[2]}")             # 3등 점수 = 2번 인덱스 값


# ## 프로그램 업그레이드 2: 함수 활용

# 앞서 살펴본 코드를 함수로 추상화하면 원하는 등수의 점수를 함수호출로 간단하게 확인할 수 있다.

# ### 프로그램 구상

# * 위 프로그램에서 변하는 부분은 등수와 관련된 부분이다.
# * 즉, 등수에 해당하는 것만 제외하면 다른 부분은 전혀 변하지 않는다.
# * 따라서 등수를 인자로 받는 함수로 추상화하면 된다.

# 따라서 함수의 본체에 해당하는 부분은 다음과 같다.
# 
# ```python
# try:
#     f = open("./data/results5m.txt", 'r') 
# except FileNotFoundError:
#     print("열고자 하는 파일이 존재하지 않습니다.")
# 
# score_list = []
# 
# for line in f: 
#     name, score = line.split()
#     try:
#         score_list.append(float(score))
#     except ValueError:
#         continue
# 
# f.close() 
# 
# score_list.sort(reverse=True)
# ```
# 
# n등의 점수는 `score_list[n-1]`이다.
# 따라서 함수의 리턴값은 아래와 같다.
# 
# ```python
# return score_list[n-1]
# ```

# 따라서 아래와 같이 랭킹(`ranking`) 함수를 정의할 수 있다.

# In[34]:


def ranking(n):                                     # n등 점수 요구
    try:
        f = open("./data/results5m.txt", 'r') 
    except FileNotFoundError:
        print("열고자 하는 파일이 존재하지 않습니다.")

    score_list = [] 

    for line in f: 
        name, score = line.split() 
        try:
            score_list.append(float(score)) 
        except:
            continue
    f.close() 

    score_list.sort(reverse=True) 
    
    return score_list[n-1]                          # n등 점수 내주기


# 이제 모든 등수의 점수를 쉽게 확일할 수 있다.

# In[35]:


ranking(1)


# In[36]:


ranking(5)


# ### 함수 일반화

# 위 함수를 좀 더 일반화할 수 있다.
# 예를 들어, `results5m.txt`에 포함된 내용의 형식과 동일한 어떤
# 분야의 점수기록 파일도 동일한 함수로 각 분야별 등수를 확인할 수 있도록 해보자.
# 
# 그러려면 먼저, `ranking` 함수에서 변하는 부분을 확인해야 하는데,
# 바로 점수기록을 담고 있는 파일명이 해당된다.
# 따라서 그 부분을 함수의 매개변수로 돌려 활용한다.
# 아래 `ranking` 함수의 정의에서 `fileName`이 파일명을 인자로 받아 함수 본체에
# 전달하는 매개변수이다.

# In[37]:


def ranking(n, fileName):                         # fileName 기록파일의 n등 점수 요구
    try:
        f = open(fileName, 'r') 
    except FileNotFoundError:
        print("열고자 하는 파일이 존재하지 않습니다.")

    score_list = [] 

    for line in f: 
        name, score = line.split() 
        try:
            score_list.append(float(score)) 
        except:
            continue
    f.close() 

    score_list.sort(reverse=True) 
    
    return score_list[n-1]                        # fileName 기록파일의 n등 점수 내주기


# 이제 `results5m.txt` 기록파일의 1등, 7등 점수는 다음과 같다.
# 
# **주의:** 기록파일이 `data`라는 하위폴더에 들어있다고 가정한다.

# In[38]:


ranking(1,'./data/results5m.txt')


# In[39]:


ranking(7,'./data/results5m.txt')


# 10m 다이빙 시합에서 1등과 7등의 점수는 다음과 같다.

# In[40]:


ranking(1,'./data/results10m.txt')


# In[41]:


ranking(7,'./data/results10m.txt')


# ## 심화예제

# 다이빙 대회에 참가한 선수들의 기록을 다룬 파일보다 좀 더 많은 정보를 포함한
# 데이터 파일을 분석하고자 한다.
# 파일에 좀 더 많은 내용이 담겨있지만 데이터 분석 방법은 거의 동일하다.

# 안내: [SciPy Lecture: Basic Reductions](https://scipy-lectures.org/intro/numpy/operations.html#basic-reductions)
# 내용을 참조합니다.

# 1900년부터 1920년까지 매년 토끼(rabbit), 스라소니(lynx), 당근(carrot)의 개체수를 조사한 자료가 
# [populations.txt](https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/populations.txt)
# 파일에 저장되어 있다.
# 파일 내용을 확인하면 다음과 같다.
# 
# **주의:** `populations.txt` 파일이 `data`라는 하위 디렉토리에 저장되어 있다고 가정하며,
# 아래 코드를 실행하면 자동으로 지정된 폴더에 저장된다.

# In[42]:


myWget("populations.txt")


# In[43]:


with open('./data/populations.txt', 'r') as pop_file:
    for line in pop_file:
        print(line.strip())            # strip 메소드로 양끝 공백 및 줄바꿈 기호 제거


# 위 코드에서, 예를 들어, `47.2e3`는 47.2 곱하기 10의 3승이다.
# 즉,

# In[44]:


47.2e3


# In[45]:


47.2e3 == 47.2 * 1000


# ### 당근 개체수의 최대값 구하기

# 이제 당근 개체수가 가장 많았을 때의 값을 알아내고자 하며, 
# 앞서 사용한 기술을 그대로 따라하기 위해 `split` 메소드를 활용한다. 
# 
# `results5m.txt` 파일과의 차이점은 두 가지이다.
# 
# * 맨 윗줄에 항목에 대한 설명이 있지만 주석을 의미하는 샵(`#`) 기호로 시작한다.
#     이 특징을 활용하여 예외처리 대신에 조건문을 사용할 수 있다.
# * 각 줄별로 세 개의 공백이 사용되어서, `split` 메소드를 실행하면 
#     네 개의 문자열로 쪼개질 것이다.
#     각각의 항목은 차례대로 연도, 토끼 개체수, 스라소니 개체수, 당근 개체수를 가리킨다.
#     따라서 길이가 4인 리스트가 생성되며, 
#     풀어헤치기를 하려면, 예를 들어, year, rabbit, lynx, carrot 등 
#     네 개의 변수를 사용해야 한다.

# In[46]:


with open('./data/populations.txt') as pop_file:
    populations = []                                   # 개체수 저장 리스트 선언

    for line in pop_file:
        if line.startswith('#'):                       # 샵으로 시작하는 맨 윗줄 건너뛰기
            continue
        else:
            year, rabbit, lynx, carrot = line.split()  # 각 줄은 네 개의 숫자로 쪼개짐
            populations.append(float(rabbit))           # 토끼 개체수만 저장함

populations.sort(reverse=True)                        

print(f"토끼 개체수의 최대값은 {populations[0]}이다.")


# ### 함수화

# 위 코드를 응용하여 연도별 토끼 개체수를 리턴하는 `rabbitNumber` 함수를 구현할 수 있다.
# 아래 사항에 주의해야 한다.
# 
# * 연도별로 토끼 개체수를 확인하려면 정렬(sorting)을 사용하지 말아야 한다.
# * 인자로 1900 ~ 1920 사이의 값이 사용된다.
#     * 1900년도 토끼의 개체수는 0번 색인을 가진다.
#     * 1920년도 토끼의 개체수는 20번 색인을 가진다.
#     * 따라서 특정 년도의 토끼 개체수가 위치하는 항목의 인덱스는 
#         해당 연도에서 1900을 빼야 한다.

# In[47]:


def rabbitNumber(yr):
    with open('./data/populations.txt') as pop_file:
        populations = []                          

        for line in pop_file:
            if line.startswith('#'):              
                continue
            else:
                year, rabbit, lynx, carrot = line.split() 
                populations.append(float(rabbit))           
    
    return populations[yr-1900]      # 연도에서 1900을 빼야 해당연도의 인덱스가 됨


# In[48]:


rabbitNumber(1900)


# In[49]:


rabbitNumber(1920)


# In[50]:


rabbitNumber(1911)


# ## 연습문제

# 1. 2등 점수를 확인하는 코드를 아래와 같이 구현할 경우 어떤 문제가 발생하는지 설명하라.
# ```python
# f = open("./data/results5m.txt") 
# highst_score = 0
# second_highst_score = 0                    # 2등 점수 저장
# for line in f: 
#      record = line.split()
#      try: 
#         score = float(record[1])
#      except:
#         continue
#      if highst_score < score:               # 1, 2등 점수 갱신 경우 확인
#         highst_score = score
#      elif second_highst_score < score:      # 2등 점수 갱신 경우 확인
#         second_highst_score = score
#      else:
#         continue
# f.close() 
# print("2등 점수는", second_highst_score, "입니다.")
# ```
# <br>
# 1. `max` 함수를 이용하여 `ranking` 함수를 구현하라.
# <br><br>
# 1. `rabbitNumber` 함수를 예를 들어 1921을 인자로 사용하여 호출하면 오류가 발생한다. 
#     `rabbitNumber` 함수를 아래 조건이 만족되도록 수정하라.
#     * 예외처리를 이용하여 1900~1920을 벗어나는 년도를 인자로 사용하면 아래 문자열이 출력되도록 한다. 
# 
#     > "해당년도 데이터가 존재하지 않습니다."
# 
# 1. `rabitNumber` 함수를 수정하여 연도와 함께 생물종류 또한 인자로 활용하는 함수 
#     `populationNumber` 함수를 구현하라.
#     예를 들어, 다음이 성립해야 한다.
#     
#     > populationNumber(1915, 'rabit') = rabitNumber(1915)
