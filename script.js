//toggleButtonParent(id)안에 toggleButton(class) 누르면 popUpWindow(class)가 튀어나옴
function togglePopUpWindow(toggleButtonParent,toggleButton,popUpWindow){
    //요소 불러오기
    const contentsWrapper = document.getElementById(toggleButtonParent);
    const subTheme = document.getElementsByClassName(toggleButton);
    const toggleWindow = document.getElementsByClassName(popUpWindow);

    // subThemeList 만들기
    let subThemeList = []
    for (let i=0;i<subTheme.length;i++){//subTheme
        subThemeList.push(subTheme[i].innerText)
    }

    console.log(contentsWrapper)
    console.log(subTheme)
    console.log(toggleWindow)
    console.log(subThemeList)

    if(contentsWrapper !== null){//contentsWrapper
        contentsWrapper.addEventListener("click",(event)=>{
            if (event.target.id !== "contents_wrapper"){
                let subTitle = event.target.innerText;//subTitle 내용 파악
                let subTitleIndex = subThemeList.indexOf(subTitle);//몇번째 subTitle인지 파악

                if (toggleWindow[subTitleIndex].style.display == 'block') {//toggleWindow
                    toggleWindow[subTitleIndex].style.display = 'none';//팝업 없애기
                    subTheme[subTitleIndex].style.color = 'white'; //font-color를 흰색으로
                } else {
                    toggleWindow[subTitleIndex].style.display = 'block';//팝업 띄우기
                    subTheme[subTitleIndex].style.color = '#EB7725'; //font-color를 흰색으로
                };
            };
        });
    };
};

//masterHeader(html)코드를 tergetHeader(id)에 삽입
function fetchHeader(masterHeader,targetHeader){
    // 1. 삽입할 대상 요소 (placeholder)를 찾습니다.
    const placeholder = document.getElementById(targetHeader);

    // 2. fetch API를 사용하여 header.html 파일을 불러옵니다.
    fetch(masterHeader) // 파일 경로가 다르면 '../header.html' 등으로 수정해야 합니다.
        .then(response => {
            // 응답이 성공적인지 확인
            if (!response.ok) {
                throw new Error('Header file not found or failed to load.');
            }
            return response.text(); // 응답 본문을 HTML 텍스트로 읽습니다.
        })
        .then(htmlText => {
            // 3. 가져온 HTML 텍스트를 placeholder의 innerHTML에 삽입합니다.
            placeholder.innerHTML = htmlText;
            console.log("Header master code successfully loaded.");
        })
        .catch(error => {
            console.error("Error loading header:", error);
        });
};

//기능부

togglePopUpWindow("mainContext","sub_theme","toggle_window")