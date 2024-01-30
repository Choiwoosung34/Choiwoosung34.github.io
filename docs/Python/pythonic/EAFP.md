---
layout: default
parent: Pythonic
grand_parent: Python
permalink: /docs/python/pythonic/eafp

title: "EAFP (허락보다 용서가 쉽다)"
description: "용서를 구하는게 허락을 받는것 보다 쉽다"
keywords: python, pythonic, EAFP
tags: [python, pythonic, EAFP]
---
![pythonic](/assets/images/pythonic/EAFP.jpg){: width="400" height="400"} 
## "Easier to Ask Forgiveness than Permission"
{: .text-yellow-200 }
나는 타 언어로 개발을 시작하여 사실 LBYL 스타일이 더 익숙했었지만,  
파이썬 개발자들에게는 EAFP 코딩 스타일이 꽤 유명하며 일반적인 방법이다.  
왜 그럴까? 그에 대한 내용을 다룬다.  

마지막에 정리하겠지만, 당연히 모든 상황에 반드시 EAFP 가 적용되야 하는 것은 아니다!
{: .fs-2 .text-grey-dk-000 }

### 1. 어디에서 유례된 개념인가
{: .text-green-000 }
> "용서를 구하는게 허락을 받는것 보다 쉽다" - 그레이스 호퍼 [[source]](https://en.wikiquote.org/wiki/Grace_Hopper){:target="_blank"}

초기 프로그래밍 세계에서 뛰어난 공헌을 한 컴퓨터 과학자인  
Grace Hopper는 위와 같은 명언과 지혜를 남겼다.

EAFP는 위 명언에서 출발한 개념으로 볼 수 있다.

해당 명언에 대한 자세한 의미등은 본 문서의 주제와 다르므로 다루지 않는다.  
다만 유례는 Grace Hopper 에게서 왔다.
{: .fs-2 .text-grey-dk-000 }

### 2. 코드 스타일에서의 EAFP
{: .text-green-000 }
파이썬 [공식 문서](https://docs.python.org/3.11/glossary.html#term-duck-typing){:target="_blank"}에서 설명하는 EAFP 의 설명은 아래와 같다. 
> Easier to ask for forgiveness than permission. This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.

한마디로 예외를 처리하는 방법에 대한 내용이다.  
많은 타언어의 기본적인 스타일인 *LBYL 스타일과 대조된다고 하는데,  
두 스타일의 차이는 아래 예시로 보면 이해하기 쉽다.  

\* look before you leap: 넘어가기 전에 돌아봐라
{: .fs-2 .text-grey-dk-000 }

#### LBYL 스타일 예시 
{: .fs-2 .text-red-000 }
```python
if "some_key" in data_dict:
    value = data_dict["some_key"]
else:
    # Handle Error in here
```

#### EAFP 스타일 예시
{: .fs-2 .text-red-000 }
```python
try:
    value = data_dict["some_key"]
except KeyError:
    # Handle Error in here
```
차이점이 보이는가?  
즉 에러나 예외적인 상황을 처리하는 방법에 대한 차이이다.  

### 3. 에러나 예외 상황에서의 처리. Prevent or Handling
{: .text-green-000 }

오류나 예외적인 상황을 처리하는것은 프로그래밍에서 흔히 있는 상황이다.  
기본적으로 아래의 두 가지 전략을 취할 수 있다.  

1. <span style="color: #ffd700;">**Prevent**</span>: 오류나 예외 상황이 발생하지 않도록 <span style="color: #ffd700;">**방지한다**</span>
2. <span style="color: #ffd700;">**Handle**</span>: 오류나 예외가 발생한 후 <span style="color: #ffd700;">**처리한다**</span>

전통적으로 에러를 <span style="color: #ffd700;">**방지**</span>하는게 대부분의 언어에서 에러에 대한 접근 방법이었다.  

C 언어나 Java 에서는 예외 처리시 비용이 많이 들어갈 수 있다.  
그래서 이러한 언어들은 오류를 <span style="color: #ffd700;">**처리**</span>하기보다 오류를 <span style="color: #ffd700;">**방지**</span>하는 경향이 있다.  

### 4. 그럼 파이썬 개발자들은 왜 EAFP를 더 선호하는 경향이 있을까
{: .text-green-000 }
즉 EAFP 는 항상 전제 조건을 확인하는 대신,  
원하는 작업을 실행하고 성공할것으로 기대하는 것이다.  
이를 선호하는 이유에는 적어도 두가지 이유가 있을 수 있다.  

1. 파이썬에서 Exception Handling 은 매우 빠르고 효과적이다.
    > 참고: 파이썬 3.11 의 여러 최적화 업데이트 중 하나는 비용이 거의 들지 않는 예외처리다.  
즉 예외가 발생하지 않으면 비용의 거의 없다는 것을 의미한다.  
[참고: Zero cost exception handling](https://github.com/python/cpython/issues/84403){:target="_blank"}

2. 잠재적인 문제에 대해 필요한 검사는 일반적으로 언어 자체에 있다.
```python
try:
    value = data_dict["some_key"]
except KeyError:
    # Handle Error in here
```
아까 이 예시를 보자.  
이 예시에서는 키를 사용하기 전에 있는지 확인하지 않는다.  
그저 키에 엑세스 해보는 것이다.  
어짜피 키가 없다면 KeyError 가 발생할 것이다.

### 5. 파이썬스러운 EAFP
{: .text-green-000 }
당연하게도 모든 상황에 EAFP 를 적용해야 한다는건 아니다.  
그러면 EAFP의 장점과, 어떻게 써야 파이썬스러운지 이해해보자.  

#### 5.1 오브젝트의 타입이나 속성 확인
{: .fs-3 .text-red-000 }
파이썬은 보통 객체 유형을 미리 확인하지 않고,  
메서드를 직접 호출하거나 속성에 접근하여 객체와 상호작용한다.

이런 경우 EAFP는 올바른 방법이다. 아래 함수를 보자.
```python
def add_messages(message, message_list):
    if isinstance(message_list, list):
        message_list.append(message)
    ...
```
message_list 가 리스트 인스턴스일경우 message 을 추가해주는 함수이다.    
하지만 파이썬에서는 타입을 검사하는건 일반적인 안티패턴이다.  

이 함수는 파이썬의 2가지 핵심 원칙을 해친다.  

1. 다형성(Polymorphism)
2. 덕 타이핑(Duck Typing)

파이썬은 덕타이핑 언어이다.  
파이썬은 일반적으로 객체의 타입보다는 객체의 동작(행동?)에 의존한다.  

한마디로 list 를 기대하는게 아니라, .append() 가 동작할것으로 기대해야된다.  

아래 예시로 좀 더 이해해보자.  

내가 만약 요구사항에 변경으로 message_list를  
[collections.deque()](https://docs.python.org/3.11/library/collections.html#collections.deque){:target="_blank"} 로 사용하게 되었다고 해보자.  
그럼 코드는 아래와 같이 수정해야 동작할것이다. 
즉 변화에 취약하다.   
```python
def add_messages(message, message_list):
    if isinstance(message_list, list):
        message_list.append(message)
    if isinstance(message_list, deque):
        message_list.append(message)
    ...
혹은 
def add_messages(message, message_list):
    if isinstance(message_list, list) or isinstance(message_list, deque):
        message_list.append(message)
    ...
```

객체의 타입 검사로 덕타이핑을 희생하지 않으려면,  
아래와 같이 EASP 스타일로 코딩하면 된다.
```python
def add_messages(message, message_list):
    try:
        message_list.append(message)
    except AttributeError:
        pass
```
add_messages 구현은 넘어오는 객체의 타입이 아니라,  
객체의 .append()라는 동작에 의존하게 된다.  

객체의 타입에 이어 속성을 체크할때도 마찬가지이다.  
```python
# anti-pattern
def get_message_receiver(receiver):
    if hasattr(message, "receiver"):
        return message.receiver
    return None

# Pythonic
def get_message_receiver(receiver):
    try:
        return message.receiver
    except AttributeError:
        return None
```
더 명확하고 간단해보이며,  
hasattr 을 지속적으로 호출하지 않기때문에 더 효율적일 수도 있다.

#### 5.2 불필요하게 많이 체크하는거 방지  
{: .fs-3 .text-red-000 }
아래와 같은 함수를 예시로 보자.  

아마 이런 함수를 만드는 경우는 거의 없겠지만...
{: .fs-2 .text-grey-dk-000 }

```python
def sum_two_string_to_int(n1: str, n2: str):
    if n1.isdigit():
        n1 = int(n1)
    else:
        return None
    if n2.isdigit():
        n2 = int(n2)
    else:
        return None
    return n1 + n2

>>> sum_two_string_to_int("1", "10")
10

>>> sum_two_string_to_int("1", "ten") is None
True
```

이런경우도 EAFP 스타일이 훨씬 명확하고 깔끔하다.  
```python
def sum_two_string_to_int(n1: str, n2: str):
    try:
        return int(n1) + int(n2)
    except ValueError:
        return None

>>> sum_two_string_to_int("1", "10")
10

>>> sum_two_string_to_int("1", "ten") is None
True
```

그리고 한가지 더!  
처음 버전 함수는 괜찮아보이지만 오류가 하나 숨어있다.  
```python
def sum_two_string_to_int(n1: str, n2: str):
    if n1.isdigit():
        n1 = int(n1)
    else:
        return None
    if n2.isdigit():
        n2 = int(n2)
    else:
        return None
    return n1 + n2

>>> sum_two_string_to_int("-1", "-4")
None # ???
```
우리는 -5 를 기대했겠지만 isdigit 은 음수는 False 를 반환한다.  
![pythonic](/assets/images/pythonic/eafp_2.png) 

하지만 아래와 같이 했다면?
```python
def sum_two_string_to_int(n1: str, n2: str):
    try:
        return int(n1) + int(n2)
    except ValueError:
        return None

>>> sum_two_string_to_int("-1", "-4")
-5
```

한마디로 모두 예외처리를 하려면 우리가 놓치는 부분이 있을 수 있다.  
EAFP 스타일을 적절하게 활용한다면,  
<span style="color: #ffd700;">잘못된 부분은 언어 자체에서 잡아줄것이다.</span>

#### 5.3 가독성과 명확성
{: .fs-3 .text-red-000 }
또한 가독성과 명확성 또한 개선 될 수 있다. 

아래 두 함수를 비교해보자

```python
# LBYL
def divide_a_by_b(a: int, b: int, default: int = None):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return default
    return a / b

# EAFP
def divide_a_by_b(a: int, b: int, default: int = None):
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        return default
```
처음 코드를 보면 위 함수는 왜 b가 0 인지 체크하는지 보고 
해당 함수의 동작이 눈에 들어온다.  

하지만 아래 함수는 동작이 먼저 보이기때문에 어떤 동작을 하는지 쉽게 이해할 수  있다.

<span style="color: #ffd700;">가독성과 명확성은 비단 파이썬뿐 아니라 모든 언어에서 중요시 되는 요소이다.</span>

#### 5.4 Race Condition 방지
{: .fs-3 .text-red-000 }
레이스 컨디션은 많이 들어봤을 것이다.  
![pythonic](/assets/images/pythonic/race_cond.webp){: width="200" height="200"}   

Race Condtion 에 대한 설명은 생략.
{: .fs-2 .text-grey-dk-000 }

다중 쓰레드 환경에서는 예측하기 어려운 문제들이 발생할 수 있다.
```python
if key in my_dict:
    ...
    return my_dict[key]
```
위 예시에서 극단적으로는 `if key in my_dict` 를 조회한 후에,  
`return my_dict[key]` 사이에 다른 쓰레드에서 값을 지운다면 에러가 발생한다.  

```python
if connection.is_active():
    # 처리 작업
    connection.commit()
else:
    ...
```
좀더 현실적으로 위 예시는 어떨까?  
`connection.is_active()` 와 `connection.commit()` 사이에  
만약 네트워크 문제로 연결이 끊긴다면 체크를 했지만서도 에러가 발생한다.  

위와같은 위험을 방지하려면 아래와 같이 EAFP 스타일로 할 수 있다.
```python
try:
    # 처리 작업
    connection.commit()
except ConnectionError:
    pass
```
이렇게 하면 연결이 활성화된 상태인지 확인하지 않고 그저 commit 을 실행할 뿐이므로,  
확인과 실제 작업 사이에 Race Condition이 발생할 위험이 사라진다.  
이러한 방식을 사용하면 <span style="color: #ffd700;">더욱 안정적인 코드가 되어 디버그하기 어려운 Race Condition 상황을 피할 수 있다.</span>

\+ 위 케이스 외에도 대표적으로 파일 관련 작업에도 Race Condition 이 발생할 수 있음

위 멀티쓰레드 환경 Race Condition 상황에서 나온 에러를  
우리가 디버깅 해본다고 가정해보자.  
~~???: 제가 해보니깐 잘 되는데요??~~  
벌써부터 어질어질하다.
{: .fs-2 .text-grey-dk-000 }


#### 5.5 성능 향상
{: .fs-3 .text-red-000 }
성능은 개발할 때 가장 중요한 요소 중 하나이다.  

파이썬은 예외 처리를 저렴한 작업으로 만들기 위해 열심히 노력해왔다.  
그래서 예외 비용에 대해 크게 걱정할 필요가 없다.  
많은 경우에 예외는 조건문보다 더 빠를 수 있다.  

아래 예시를 만들어보자.  
text 를 받아서 각 문자가 얼마나 등장했는지 dict 로 반환해주는 함수를  
두 방식으로 만들어보자.  
```python
def LBYL(text):
    char_count_map = {}
    for c in text:
        if c in char_count_map:
            char_count_map[c] += 1
        else:
            char_count_map[c] = 1
    return char_count_map

def EAFP(text):
    char_count_map = {}
    for c in text:
        try:
            char_count_map[c] += 1
        except KeyError:
            char_count_map[c] = 1
    return char_count_map
```

아래와 같은 텍스트로 실행시켜보자.
```python
# https://www.python.org/about/gettingstarted/ 여기서 긁어옴 ㅋㅋ
text = """
Python For Beginners
Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to get started with Python. Fortunately an experienced programmer in any programming language (whatever it may be) can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!

Installing
Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers (notably those from HP) now come with Python already installed. If you do need to install Python and aren't confident about the task you can find a few notes on the BeginnersGuide/Download wiki page, but installation is unremarkable on most platforms.

Learning
Before getting started, you may want to find out which IDEs and text editors are tailored to make Python editing easy, browse the list of introductory books, or look at code samples that you might find helpful.

There is a list of tutorials suitable for experienced programmers on the BeginnersGuide/Tutorials page. There is also a list of resources in other languages which might be useful if English is not your first language.

The online documentation is your first port of call for definitive information. There is a fairly brief tutorial that gives you basic information about the language and gets you started. You can follow this by looking at the library reference for a full description of Python's many libraries and the language reference for a complete (though somewhat dry) explanation of Python's syntax. If you are looking for common Python recipes and patterns, you can browse the ActiveState Python Cookbook

Looking for Something Specific?
If you want to know whether a particular application, or a library with particular functionality, is available in Python there are a number of possible sources of information. The Python web site provides a Python Package Index (also known as the Cheese Shop, a reference to the Monty Python script of that name). There is also a search page for a number of sources of Python-related information. Failing that, just Google for a phrase including the word ''python'' and you may well get the result you need. If all else fails, ask on the python newsgroup and there's a good chance someone will put you on the right track.

Frequently Asked Questions
If you have a question, it's a good idea to try the FAQ, which answers the most commonly asked questions about Python.

Looking to Help?
If you want to help to develop Python, take a look at the developer area for further information. Please note that you don't have to be an expert programmer to help. The documentation is just as important as the compiler, and still needs plenty of work!
"""
print(LBYL(text))
>>> {'\n': 22, 'P': 22, 'y': 71, 't': 196, 'h': 90, 'o': 219, 'n': 174, ' ': 447, 'F': 5, 'r': 134, 'B': 4, 'e': 228, 'g': 53, 'i': 138, 's': 115, 'W': 2, 'l': 98, 'c': 50, 'm': 52, '!': 3, 'A': 4, 'u': 75, 'p': 48, 'w': 35, 'a': 173, '?': 3, 'I': 13, 'f': 61, 'b': 29, 'k': 25, 'd': 57, '.': 19, 'x': 8, '(': 4, 'v': 12, ')': 4, 'q': 4, "'": 11, ',': 16, 'j': 3, 'L': 4, 'U': 1, 'N': 1, 'X': 1, 'E': 3, 'H': 2, 'G': 3, '/': 2, 'D': 2, 'T': 8, 'Y': 1, 'S': 4, 'C': 2, 'M': 1, '-': 1, 'Q': 2}
```

결과가 잘 나온다.

이제 컴퓨터를 좀 고생시켜 보자.

```python
import timeit
text *= 100

eafp_time = min(
    timeit.repeat(
        stmt="EAFP(text)",
        number=100,
        repeat=5,
        globals=globals(),
    )
)

lbyl_time = min(
    timeit.repeat(
        stmt="LBYL(text)",
        number=100,
        repeat=5,
        globals=globals(),
    )
)

print(f"이 경우 LBYL 이 {lbyl_time / eafp_time:.3f}배 만큼 EAFP 보다 느리다")
>>> 이 경우 LBYL 이 1.244배 만큼 EAFP 보다 느리다
```
약 24% 성능 차이를 보인다.  
많은 처리를 할수록 더 벌어질것이다.  

다만 위 케이스는 알파벳 숫자가 정해져있어서 많은 예외가 발생하진 않았지만,  
많은 예외가 발생하는 경우 LBYL 이 성능이 더 잘나온다.
{: .fs-2 .text-grey-dk-000 }


## 6. EAFP 적용시 주의할 점
{: .text-green-000 }
#### 6.1 사이드 이펙트를 체크해야 된다.  
{: .fs-3 .text-red-000 }

```python
names = ["우성", "오이", "아토"]

with open("hello.txt", mode="a", encoding="utf-8") as hello:
    try:
        for index in range(4): # 0, 1, 2, 3
            hello.write("안녕: ")
            hello.write(f"{names[index]}!\n")
    except IndexError:
        pass
```
위와 같은 코드가 있다고 생각해보자.  
위 코드를 실행하면 아래와 같은 파일이 나올것이다.  

```bash
안녕: 우성!
안녕: 오이!
안녕: 아토!
안녕: 
```
index 가 3 일 때  
`hello.write("안녕: ")` 여기 구문은 정상적으로 실행되고,  
`hello.write(f"{names[index]}!\n")` 이 부분에서는 에러가 나서  
파일에 불완전한 내용으로 남아있다.

한번더 이 코드를 실행한다면?
```bash
안녕: 우성!
안녕: 오이!
안녕: 아토!
안녕: 안녕: 우성!
안녕: 오이!
안녕: 아토!
안녕: 
```
파일 내용(형식)이 깨져버린다.

이를 방지하기 위해선 아래처럼 하면 된다.
```python
names = ["우성", "오이", "아토"]

with open("hello.txt", mode="a", encoding="utf-8") as hello:
    for index in range(4): # 0, 1, 2, 3
        try:
            name = names[index]
        except IndexError:
            pass
        else:
            hello.write("안녕: ")
            hello.write(f"{name}!\n")
```

try 문에는 예외가 발생하는 `name = names[index]` 만 둔다.  
else 문으로 except 가 없을 경우에만 실행시켜주면 된다.  
이렇게 하면 파일 형식이 망가지지 않는 것을 볼 수 있다.

```bash
안녕: 우성!
안녕: 오이!
안녕: 아토!
```

#### 6.2 모든 예외를 짬처리(?) 하지 마라
{: .fs-3 .text-red-000 }

```python
try:
    do_something()
except Exception:
    pass
```
위와 같은 처리는 피하자.  
`do_something` 함수에서는 다양한 유형의 예외가 발생할 수 있다.  
알 수 없는 오류를 포함하여 모든 오류를 이렇게 조용히 넘겨서 실행하는것은  
<span style="color: red;">나중에 다 업보로 돌아온다.</span>

또한 이는 [Zen of Python](https://peps.python.org/pep-0020/){:target="_blank"}의 철학에 벗어난다.
```bash
Errors should never pass silently. 오류를 조용히 보내서는 안된다.
Unless explicitly silenced. 알고도 침묵하지 않는 한.
```
대신 아래와 같이 각 예외를 적절하게 처리하자.  
```python
try:
    do_something()
except ValueError:
    # ValueError 핸들링
except IndexError:
    # IndexError 핸들링
except MyCustomError:
    # MyCustomError 핸들링
```
또 이렇게 하면 디버깅이 더 쉬워진다.  
do_something 에서 문제가 생기면 바로 실패되기 때문이다.  

즉 조용히 알 수 없는 오류를 전달하지 않을 수 있다.

## 결론
{: .text-yellow-200 }

대부분의 경우에 값이 올바르게 오거나,  
단순히 몇가지의 예외만 포함할 수 있거나,  
전제조건 체크에 비용이 많이 들어간다면,  

EAFP 스타일을 쓰면 된다.  

올바르게 사용할 수 있다면
{: .fs-2 .text-grey-dk-000 }

아래에 종합해서 내용을 정리해놨는데,  
아래 내용을 보고 상황에 따라 사용할 전략을 정해볼 수 있을 것이다.

| LBYL 사용 | EAFP 사용 |
|---------------------------------|-------------------------------------------------------|
| 실패할 가능성이 높은 작업 | 실패할 가능성이 낮은 작업 (대부분 성공한다 가정될 때)|
| 되돌릴 수 없는 작업이나 부작용이 있을 수 있는 작업 (에러 발생시 크리티컬할 경우) | 입력 및 출력(IO) 작업, 주로 파일 및 네트워크 작업 (Race Condition 이 유발될 수 있을 경우)|
| 사전에 가볍게 체크할 수 있을때, 사전 체크에 오버헤드가 작을때| 에러 발생후 빠르게 처리할 수 있을 때 (오래 걸린다면 방지해야죠) e.g. 빠르게 롤백할 수 있는 데이터베이스 작업  |

끝!
