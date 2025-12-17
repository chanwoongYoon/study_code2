import re

text = r"""<가상 클래스 선택자:요소의 특정 상태에 스타일 적용>
    form : 선택자:가상클래스 {속성:속성값;}
        :hover - 마우스가 요소위에 있는 상태일 때
        :active - 요소가 사용자에 의해 활성화
        :focus - 입력필드,링크등의 요소가 포커스 받은 상태
        :checked - 라디오,체크박스 등의 입력필드가 선택된 상태

<선택자>
    1.전체      * {}
    2.타입      span {}
    3.클래스    .price {}
    4.아이디    #container {}
    5.속성      button[type] {}

<선택자 하위요소>
    1.선택자 선택자 {}
    2.선택자 > 선택자 {} - 직계자식요소 선택

<글자 조정>
    1.font-family: 폰트지정
        font-family:"궁서체","돋움",sans-serif;
    2.font-size: 글자 크기 지정
        font-size:절대단위(px,pt)/상대단위(em,rem);
            백분율: 부모요소의 폰트크기에 상대적인 단위
            em:부모 요소의 폰트크기에 상대적 단위
            rem:최고 부모 요소의 폰트크기에 상대적 단위
    3.font-style: 스타일 정의
        font-style: normal/italic(이탤릭체)/oblique(폰트 그냥 기울임 처리)
    4.font-weight: 폰트의 두께 설정
        font-weight: 키워드(normal{400},bold{700})/숫자(100,200...900)
    5.색상:
        color:색상명/hex코드/rgb/rgba

<텍스트 레이아웃>
    1.line-height: 텍스트 줄 간격
        line-height:숫자(배수)/백분율(%)/크기단위(px,em)등
        line-height값에서 text세로 크기 뺀 값을 위아래에 배치
    2.text-align: 텍스트 수평 정렬 방식
        text-align:left/right/center/justify/start/end
    3.letter-spacing:"글자"간 간격
        letter-spacing:크기단위(px,em)
    4.word-spacing:"단어"사이의 간격
        word-spacing:크기단위(px,em)
    5.background-color:배경색
        background-color:#00FF00;
    6.background-image:배경이미지
        background-image:url('PIA_sad.jpg')
    7.background-size:배경 맞춤
        background-size:auto/cover/container

<요소 움직이기>
    1.translate(x, y):요소를 X축(수평)과 Y축(수직)으로 이동합니다.
        transform: translate(50px, 100px);
    2.translateX(x):요소를 X축으로만 이동합니다.
        transform: translateX(-50%); - [자기 자신의 크기의 50%이동]
    3.translateY(y):요소를 Y축으로만 이동합니다.
        transform: translateY(2rem);
    4.translateZ(z):요소를 Z축(깊이)으로 이동합니다. (3D)
        transform: translateZ(20px);
    5.translate3d(x, y, z):요소를 3차원 공간에서 이동합니다.
        transform: translate3d(10px, 5px, -5px);

<블록 꾸미기>
    1.border-width:테두리
        border-width:크기단위(px,em)/thin/medium/whick
    2.border-style:테두리
        border-style:none/solid/dotted/double
    3.box-sizing:컨텐츠 크기 = 패딩,보더
        box-sizing:content-box/border-box
    4.display:요소의 배치방식 정의
        display:block/inline/inline-block/none/grid
    5.position:요소의 배치방식 정함
        position:static/relative/absolute/fixed/sticky
    6.z-index:z축 설정
        z-index:숫자(클수록 앞)
    7.float:요소를 페이지 특정위치 떠오르게
        float:left/right/none
            main::after{
                content:"";
                display:block;
                clear:both;
            }
    가상요소: 실제로 존재하지 않는 새로운 요소 만들어 냄
    8.overflow: hidden;
        박스안의 요소들이 경계 넘지 않도록 조정
    9.box-shadow:박스 그림자
        box-shadow:[그림자 수평위치(우로)][그림자 수직 위치(아래로)][블러][번짐정도][그림자 색상]

<플렉스 박스 부모>
    1.container:아이템 담는 컨테이너
        display:flex; 로 선언
    2.flex-direction:정렬 방향 설정
        flex-direction:row/column/row-reverse/column-reverse
    3.flex-wrap:한 줄 유지,여러 줄 가능 설정
        flex-wrap:nowrap/wrap
    4.justify-content:기본축 정렬(flex-direction에 의해 결정)
        justify-content:flex-start/flex-end/center/space-between/space-around/space-evenly
            space-between:자식요소의 첫번째 요소와 마지맏 요소는 양끝, 사이에 여백은 균등히 분배
            space-around:모든요소의 "좌우"여백 균등히 분배 (맨 끝의 여백이 X라면, 사이 여백 2X)
            space-evenly:모든 여백 균등히 분배
    5.align-items:반대축으로 요소 정리
        align-items:flex-start/flex-end/center/stretch/baseline
            stretch:부모 높이에 맞춰 늘어남
            baseline:폰트 기준선에 맞춰 늘어남
    6.gap:"아이템들"의 행 또는 열 사이의 간격을 설정하는 속성
        gap:(숫자)px

<플렉스 박스 자식>
    1.order:(숫자)
        숫자가 작을 수록 앞 순서를 유지
    2.flex:컨테이너 크기에 따른 아이템의 크기
        flex-grow:아이템 얼마나 커질 지
        flex-shrink:아이템 얼마나 작아질 지
        flex-basis:아이템 기본 크기 정함
        flex:flex-grow flex-shirnk flex-basis
    3.align-self:반대축 정렬
        align-self:auto/flex-start/flex-end/center/space-between/space-around/space-evenly
            space-between:자식요소의 첫번째 요소와 마지맏 요소는 양끝, 사이에 여백은 균등히 분배
            space-around:모든요소의 "좌우"여백 균등히 분배 (맨 끝의 여백이 X라면, 사이 여백 2X)
            space-evenly:모든 여백 균등히 분배

<그리드 부모>
    <container - [grid]>
    1.grid-template-rows:크기단위(px,em,%)/repeat()/fr
        grid-template-rows:1fr 2fr 1fr (그리드 비율 1:2:1)
    2.grid-template-columns:크기단위(px,em,%)/repeat()/fr
        grid-template-columns:1fr 2fr 1fr  == repeat(3,1fr)    (그리드 비율 1:2:1)
    3.gap:"아이템들"의 행 또는 열 사이의 간격을 설정하는 속성
        gap:(숫자)px
    4.grid-row,column-start,end:start~end부분 점유 가능
        grid-row,column-start,end:숫자(grid-template-rows.columns 이내)
        gird-row:2/3 = grid-row:2/span1(span1 == 2+1 == 3)
        gird-column:1/4 = grid-column:1/span3(span3 == 1+3 == 4)
    5.grid-template-areas:지정 부분 이름 붙여주는 거

<효과와 애니메이션>
    1.filter
    2.opacity
    3.box-shadow
    4.transform
    5.animation
    6.transition
    7.타이밍 함수

<엔티티>
    저작권 기호 다이아모양 등을 안전하게 구현가능
    & #####;

<시멘틱 태그>
    article : 반복되는 요소
    aside : 필요조건 아님, 사이드바나 말풍선 
    time ; 시간 ,날짜 나타냄
    figure:독립적 요소 나타냄,일러,다이어그램 같은거 - 사람들 시선 끝고 캡션이 달림"""

def tab_number(paragraph):
    tab_one = '    '
    tab_two = tab_one * 2
    tab_three = tab_one * 3
    tab_four = tab_one * 4
    if (tab_four in paragraph):
        return 4
    elif (tab_three in paragraph):
        return 3
    elif (tab_two in paragraph):
        return 2
    elif (tab_one in paragraph):
        return 1
    else:
        return 0

def text_debri_to_html(text):
    text = text.split('\n\n')
    print(text)
    real_result_dict = {}
    result_lst_title = []
    for text_debri in text:
        result_dic = {}
        pattern = r'\n {4}(?![ ])'
        title = text_debri.split('>')
        title = title[0][1:]
        content = text_debri.split('>')[1]
        content = re.split(pattern, content)[1:]
        print(f'title : {title}')
        print(f'content : {content}')
        for i in content:
            key = i.split('\n')[0]
            print(f'key : {key}')
            if(len(i.split('\n')) > 1):
                description = i.split('\n')[1]
                print(f'description : {description}')
                result_dic[key] = description
            else:
                result_dic[key] = None
        print(result_dic)
        real_result_dict[title] = result_dic
    return real_result_dict

result_html = text_debri_to_html(text)
pass