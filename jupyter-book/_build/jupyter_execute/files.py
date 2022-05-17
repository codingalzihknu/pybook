#!/usr/bin/env python
# coding: utf-8

# (ch:files)=
# # 파일

# 데이터의 양이 많아지면 데이터를 처리하는 일도 어려워진다.
# 일단 처리 시간이 기하급수적으로 늘 수 있으며,
# 무엇보다도 **데이터셋**에서 원하는 정보를 얻어내기도 보다 복잡해진다.
# 
# **참고:** 데이터셋은 데이터의 모음(set)을 가리키는 전문용어이다.
# 
# 여기서는 다량의 데이터를 하나로 묶어서 처리할 수 있는 방법 두 가지를 소개한다.
# 
# * 데이터를 파일에 저장하고 불러오기
# * 리스트로 다량의 데이터 다루기

# ## 데이터셋 준비하기

# [results5m.txt](https://raw.githubusercontent.com/liganega/ProgInPython/master/notebooks/data/results5m.txt) 파일은
# 다이빙 선수 열 명의 5m 경기 점수를 담고 있다.
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

# 첫째 줄은 선수이름과 점수라는 구분이 표시되어 있으며,
# 둘째 줄부터 총 열 명의 이름과 점수가 기록되어 있다.
# 위 파일의 내용을 아래와 같이 파이썬 코드로 확인할 수 있다.
# 
# **주의:** `results5m.txt` 파일이 `data`라는 하위 디렉토리에 저장되어 있다고 가정한다.
# 
# 먼저 위에서 언급된 파일을 다운 받아서 파이썬 코딩을 실습하는 폴더에 저장한다.
# 여기서는 `data`라는 하위폴더에 `results5m.txt`라는 파일로 저장하는 방식은 두 가지이다.
# 
# * 첫째 방식: 위 링크를 눌러 해당 파일을 다운로드 한 후 현재 폴더에 위치한 `data` 폴더에 저장한다.
# * 둘째 방식: [인터넷에서 정보구하기](https://github.com/liganega/ProgInPython/blob/master/notebooks/PiPy02A-InfoFromInternet.ipynb)에서 사용했던 기법을 똑같이 사용할 수 있으며,
#     단순히 아래 코드를 실행하면 된다. 
#     아래 코드에 사용된 명령문 설명은 이후 차차 설명될 것이다.   

# In[1]:


import urllib.request
import os

def myWget(dirPath, fileURL, fileName):
    # dirPath 디렉토리 생성. 이미 존재하면 건너 뜀.
    try:
        os.mkdir(dirPath)
    except FileExistsError:
        pass

    # 파일 저장 주소에서 파일 내용을 가져오기.
    contents = urllib.request.urlopen(fileURL).read().decode("utf8")

    # 가져온 파일 내용을 텍스트 파일로 저장하기.
    # words.txt 파일이 이미 존재할 경우 새파일로 생성됨.
    # 즉, 기존 파일 내용을 덮어 씀.
    with open(dirPath+'/'+fileName, 'w') as f_out:
        for line in contents:
            f_out.write(line)    
            


# In[2]:


path = './data'
url = 'https://raw.githubusercontent.com/liganega/ProgInPython/master/notebooks/data/results5m.txt'
fName = 'results5m.txt'

myWget(path, url, fName)


# ## 파일에 저장된 데이터 불러오기

# 파일에 저장된 내용을 불러와서 확인하는 자세한 방법은 
# [파일 다루기](https://github.com/liganega/ProgInPython/blob/master/notebooks/PiPy04B-Files.ipynb)를 참조한다.
# 무엇보다도 파일 자료형의 `close` 메서드를 활용하여 
# 더 이상 사용하지 않는 파일을 닫아주어야 하는 것을 명심해야 한다.
# 그렇지 않으면 파일이 의도치 않게 오염될 수 있기 때문이다.

# In[3]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")
        


# **주의:** 
# 저장된 파일 내용을 불러오는 `open` 함수를 적용할 때,
# 지정된 파일이 존재하지 않은 경우을 대비해서
# [예외처리](https://github.com/liganega/ProgInPython/blob/master/notebooks/PiPy04D-ErrorsAndExceptions.ipynb)를
# 사용하였다. 
# 열고자 하는 파일이 존재하지 않는다는 정보를 전달하는 것이 단순히 오류가 발생하면서 실행이 멈추는 것보다 훨씬 유익하기에
# 이런 경우 보통 예외처리를 사용한다.

# ### 불러온 데이터 확인하기

# `result_f` 변수가 가리키는 값의 자료형은 `_io.TextIOWrapper` 라는 
# 이름도 생소한 자료형이다.

# In[4]:


type(result_f)


# 하지만 자료형은 전혀 중요하지 않다.
# 다만 텍스트 파일의 내용을 저장하고 있다와
# 저장된 내용을 확인하려면 아래와 같이 `for` 반복문을 
# 사용해야 한다는 점을 기억해야 한다.

# In[5]:


for line in result_f:                   # 각 줄 내용 출력하기
    print(line)

result_f.close()                        # 파일 닫기


# 줄 사이가 넓은 이유는 파일을 작성하면서 줄바꾸기를 할 때 사용하는 엔터에 의해 줄바꾸기 기호(`\n`)이
# 각 줄의 맨 끝에 포함되어 있는데, `print` 함수 자체가 출력할 때마다 기본적으로 줄바꿈을 수행하기에
# 줄바꿈을 결국 두 번하기 때문이다. 
# 
# 따라서 줄바꾸기를 한 번 더 하는 것을 방지하기 위해서 문자열 자료형의 `strip` 메소드를 활용하여
# 문자열의 양 끝에 있는 공백과 줄바꿈 기호를 없애는 것이 좋다.

# In[6]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")
        
for line in result_f: 
    print(line.strip())              # strip 메소드 활용하기

result_f.close() 


# **주의:** `strip` 메소드를 활용하여 데이터를 보다 깔끔하게 정리하는 것은 좋은 버릇이다.
# 하지만 반드시 필요한 것은 아닐 수도 있기 때문에 사용여부를 판단해야 한다.

# ## 리스트 활용

# 앞서 파일 내용을 확인해 보았듯 각 줄마다 선수이름과 점수가 공백을 사이로 두고 각 줄에 적혀 있다.
# 따라서 아래와 같이 문자열 자료형의 `split` 메소드를 활용하여 각 줄을 쪼개어 두 번째 항목을 확인할 수 있다.
# 
# 예를 들어, 둘째줄의 내용은 다음과 같다.

# In[7]:


secondLine = '권준기 7.13\n'


# 해당 줄을 `strip` 하면 줄바꿈 기호가 사라진다.

# In[8]:


secondLine.strip()


# 이제 `split` 메서드를 사용하여 공백 기준으로 쪼개면 다음과 같다.

# In[9]:


secondLine.strip().split()


# 그런데 `strip` 메서드는 이제 굳이 필요없다.
# `split` 메소드가 공백 기준으로 쪼개기 때문에 
# 끝에 있는 줄바꿈도 함께 제거하기 때문이다.
# 
# **주의:** 줄바꿈도 공백으로 간주된다.

# In[10]:


secondLine.split()


# ### 리스트 자료형 간략 소개

# 위에서 얻어지 값은 두 개의 항목으로 이루어진 **리스트**(`list`)이다.
# 리스트는 여러 개의 항목을 하나로 묶어서 들고 다닌다. 
# 리스트 자료형에 대한 자세한 소개는 
# [기본 자료형: 리스트](https://github.com/liganega/ProgInPython/blob/master/notebooks/PiPy04C-Lists.ipynb)를
# 참조한다.
# 
# 지금 당장 리스트에 알아야 할 사항은 다음과 같다.
# 
# * 여러 개의 값들을 담고 있는 모음 자료형
# * 문자열처럼 왼편 항목에서부터 0, 1, 2, 3, ... 등의 인덱스 부여

# 리스트의 둘째 항목, 즉 1번 인덱스의 값이 바로 점수이다.

# In[11]:


secondLine.split()[1]


# 확인된 점수가 숫자가 아니라 실수 모양의 문자열임에 주의해야 한다.
# 따라서 숫자로 다루고 싶다면 `float` 함수를 적용해야 한다.

# In[12]:


float(secondLine.split()[1])


# ## 점수 확인하기

# 이제 모든 줄이 동일한 모양을 갖고 있다는 점에 착안하여 아래와 같이 각각의 줄에 담긴 
# 내용 중에서 점수에 해당하는 부분을 아래와 같이 확인할 수 있다.
# 
# **주의:** 리스트의 색인도 문자열의 경우처럼 0부터 시작한다. 
# 따라서 리스트의 둘째 항목의 색인은 1인다.

# In[13]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

for line in result_f: 
    record = line.split()          # 공백으로 쪼개기
    print(record[1])

result_f.close() 


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

# In[14]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

highst_score = 0                   # 1등 점수 저장

for line in result_f: 
    record = line.split()

    try:                           # 첫째 줄 제외
        score = float(record[1])
    except ValueError:
        continue                   # 오류가 발생하는 줄 무시

    if highst_score < score:       # 1등 점수와 비교
        highst_score = score       # 1등 점수 갱신

result_f.close() 

print(f"1등은 {highst_score}점 입니다.")


# **주의:** `else` 명령문은 필요하지 않은 경우 생략이 가능하다.

# ### 2등, 3등 점수 확인하기

# 이제 2등 점수까지 확인해보자.
# 2등 점수를 기억할 변수가 하나 더 필요하며
# 확인된 점수가 기존의 1등 점수보다 큰지, 2등 점수보다 큰지 여부에 따라 
# 1, 2등 점수를 기억하는 변수의 값들을 
# 업데이트 해야 한다.

# In[15]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

highst_score = 0
second_highst_score = 0                    # 2등 점수 저장

for line in result_f: 
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

result_f.close() 

print(f"1등은 {highst_score}점 입니다.")
print(f"2등은 {second_highst_score}점 입니다.")


# 그런데 위와 같은 식으로 3등 점수까지 확인하려면 더 많은 변수와 조건문을 사용해야 하며,
# 코드가 점점 길어진다.

# In[16]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

highst_score = 0
second_highst_score = 0
third_highst_score = 0                          # 3등 점수 저장

for line in result_f: 
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

result_f.close() 

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

# ### 리스트 풀어 헤치기

# 각각의 줄을 `split` 메서드로 쪼개면 길이가 2인 문자열들의 리스트가 된다.
# 따라서 각 항목의 값을 동시에 서로 다른 변수에 할당할 수 있다.
# 이것을 **리스트 풀어헤치기**(list unpacking)이라 부른다.
# 
# 예를 들어, 권주기 선수의 경우 쪼개면 아래 결과이다.

# In[17]:


secondLine.split()


# 따라서 리스트의 두 항목을 각각 두 개의 변수에 할당할 수 있다.

# In[18]:


nameKwon, scoreKwon = secondLine.split()
print(f"이름: {nameKwon}, 점수: {scoreKwon}")


# ### 리스트 정렬

# 리스트의 항목들을 크기로 비교할 수 있다면 크기 순서대로 정렬할 수 있다.
# 예를 들어, 숫자와 문자열은 크기 비교가 가능하다. 

# In[19]:


2.3 < 3.5


# In[20]:


2.3 > 3.5


# 문자열의 경우 사전식으로 크기비교를 한다.

# In[21]:


'hello' < 'python'


# 소문자가 대문자보다 크다고 판단한다.

# In[22]:


'a' < 'A'


# In[23]:


'Za' < 'b' 


# 따라서 숫자, 문자열 등으로 구성된 리스트는 정렬이 가능하다.
# 이를 위해, `sort` 메서드를 활용하며, 기본은 오름차순 정렬이다.

# In[24]:


numList = [3, 7, 1, 10, 6.3, -3.1, -7]
numList.sort()
print(numList)


# In[25]:


strList = ['python', 'languag', 'is', 'good', 'for', 'data', 'science']
strList.sort()
print(strList)


# 내림차순으로 정렬하려면, `sort` 메서드의 옵션변수 `reverse`의 인자값으로 `True`를 사용하면 된다.

# In[26]:


numList = [3, 7, 1, 10, 6.3, -3.1, -7]
numList.sort(reverse=True)
print(numList)


# In[27]:


strList = ['python', 'languag', 'is', 'good', 'for', 'data', 'science']
strList.sort(reverse=True)
print(strList)


# ### 1, 2, 3 등 확인하기

# 리스트 풀어헤치기와 리스트 정렬 기법을 이용하여 1, 2, 3등을 아래와 같이 확인할 수 있다.

# In[28]:


try:
    result_f = open("./data/results5m.txt", 'r') 
except FileNotFoundError:
    print("열고자 하는 파일이 존재하지 않습니다.")

score_list = []                           # 점수 저장 용도 리스트 선언

for line in result_f: 
    name, score = line.split()            # 각 줄을 두 단어의 리스트로 쪼갠 후 풀어헤치기
    try:
        score_list.append(float(score))   # 첫째 줄 제외. 숫자만 scores 리스트에 추가
    except ValueError:
        continue

result_f.close() 

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
#     result_f = open("./data/results5m.txt", 'r') 
# except FileNotFoundError:
#     print("열고자 하는 파일이 존재하지 않습니다.")
# 
# score_list = []
# 
# for line in result_f: 
#     name, score = line.split()
#     try:
#         score_list.append(float(score))
#     except ValueError:
#         continue
# 
# result_f.close() 
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

# In[29]:


def ranking(n):                                     # n등 점수 요구
    try:
        result_f = open("./data/results5m.txt", 'r') 
    except FileNotFoundError:
        print("열고자 하는 파일이 존재하지 않습니다.")

    score_list = [] 

    for line in result_f: 
        name, score = line.split() 
        try:
            score_list.append(float(score)) 
        except:
            continue
    result_f.close() 

    score_list.sort(reverse=True) 
    
    return score_list[n-1]                          # n등 점수 내주기


# 이제 모든 등수의 점수를 쉽게 확일할 수 있다.

# In[30]:


ranking(1)


# In[31]:


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

# In[32]:


def ranking(n, fileName):                         # fileName 기록파일의 n등 점수 요구
    try:
        result_f = open(fileName, 'r') 
    except FileNotFoundError:
        print("열고자 하는 파일이 존재하지 않습니다.")

    score_list = [] 

    for line in result_f: 
        name, score = line.split() 
        try:
            score_list.append(float(score)) 
        except:
            continue
    result_f.close() 

    score_list.sort(reverse=True) 
    
    return score_list[n-1]                        # fileName 기록파일의 n등 점수 내주기


# 이제 `results5m.txt` 기록파일의 1등, 7등 점수는 다음과 같다.
# 
# **주의:** 기록파일이 `data`라는 하위폴더에 들어있다고 가정한다.

# In[33]:


ranking(1,'./data/results5m.txt')


# In[34]:


ranking(7,'./data/results5m.txt')


# [results10m.txt](https://raw.githubusercontent.com/liganega/ProgInPython/master/notebooks/data/results10m.txt)는
# 동일한 선수들의 10m 다이빙 기록을 담고 있다.

# In[35]:


path = './data'
url = 'https://raw.githubusercontent.com/liganega/ProgInPython/master/notebooks/data/results10m.txt'
fName = 'results10m.txt'

myWget(path, url, fName)


# 그러면 10m 다이빙 시합에서 1등과 7등의 점수는 다음과 같다.

# In[36]:


ranking(1,'./data/results10m.txt')


# In[37]:


ranking(7,'./data/results10m.txt')


# ## 심화예제

# 다이빙 대회에 참가한 선수들의 기록을 다룬 파일보다 좀 더 많은 정보를 포함한
# 데이터 파일을 분석하고자 한다.
# 파일에 좀 더 많은 내용이 담겨있지만 데이터 분석 방법은 거의 동일하다.

# 안내: [SciPy Lecture: Basic Reductions](https://scipy-lectures.org/intro/numpy/operations.html#basic-reductions)
# 내용을 참조합니다.

# 1900년부터 1920년까지 매년 토끼(rabbit), 스라소니(lynx), 당근(carrot)의 개체수를 조사한 자료가 
# [populations.txt](https://raw.githubusercontent.com/liganega/ProgInPython/master/notebooks/data/populations.txt)
# 파일에 저장되어 있다.
# 파일 내용을 확인하면 다음과 같다.
# 
# **주의:** `populations.txt` 파일이 `data`라는 하위 디렉토리에 저장되어 있다고 가정하며,
# 아래 코드를 실행하면 자동으로 지정된 폴더에 저장된다.

# In[38]:


path = './data'
url = 'https://raw.githubusercontent.com/liganega/ProgInPython/master/notebooks/data/populations.txt'
fName = 'populations.txt'

myWget(path, url, fName)


# 이제 저장된 파일을 열어보자. 이전과는 달리 아래 형식을 사용한다. 
# 
# ```python
# with open(파일명) as 변수이름:
#     명령문
# ```
# 
# 위와같이 하면 지정된 명령문이 실행된 후 자동으로 파일을 닫는다.
# 따라서 위 형식은 아래 형식과 동일한 의미이다.
# 
# ```python
# 변수이름 = open(파일명)
#     명령문
# 변수이름.close()
# ```
# 
# 먼저 파일 내용을 확인해보자.

# In[39]:


with open('./data/populations.txt', 'r') as pop_file:
    for line in pop_file:
        print(line.strip())            # strip 메소드로 양끝 공백 및 줄바꿈 기호 제거


# 위 코드에서, 예를 들어, `47.2e3`는 47.2 곱하기 10의 3승이다.
# 즉,

# In[40]:


47.2e3


# In[41]:


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

# In[42]:


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

# In[43]:


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


# In[44]:


rabbitNumber(1900)


# In[45]:


rabbitNumber(1920)


# In[46]:


rabbitNumber(1911)


# ## 연습문제

# 1. 2등 점수를 확인하는 코드를 아래와 같이 구현할 경우 어떤 문제가 발생하는지 설명하라.
# ```python
# result_f = open("./data/results5m.txt") 
# highst_score = 0
# second_highst_score = 0                    # 2등 점수 저장
# for line in result_f: 
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
# result_f.close() 
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
