#!/usr/bin/env python
# coding: utf-8

# # 기본 자료형

# 참고: [SciPy 2.2장](https://scipy-lectures.org/intro/language/basic_types.html)
# 
# 1. 기본자료형이란?
# 2. 정수 자료형(int)
# 3. 부동소수점 자료형(float)
# 4. 부울 자료형(bool) (간단히, 나중에 if, for 명령문과 함께 자세히.)
# 5. 문자열 자료형(str) (간단히, 나중에 모음 자료형 다룰 때 보다 자세히.) 
#     - input() 함수 소개 및 활용. print() 명령문과 함께.\
#     - whitespace 언급할 것: [여기](https://www.unf.edu/~cwinton/html/cop3601/s10/class.notes/C4-PurgeBlnkLns.pdf)와 [여기](https://www.geeksforgeeks.org/string-whitespace-in-python/) 참고.
#     - 다음 사항고 언급

# :::{admonition} 문자열 `''` 와 문자의 `' '` 차이점
# :class: info
# 
# 빈 문자열<font size="2">empty string</font> `''` 는 
# 아무런 문자를 포함하지 않으며 따라서 문자열의 길이, 즉 문자열에 포함된 문자의 개수가 0이다.
# 반면에 `' '` 는 눈에 보이지는 않지만 공백 문자 하나를 포함하는 문자열이며 길이가 1이다.
# 
# 참고: {numref}`%s 절<sec:string>`
# :::
