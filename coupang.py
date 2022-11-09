import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    layout='wide',
    initial_sidebar_state='collapsed',
    page_title='historical people',
    page_icon='👨‍🎓'
)
btn1 = st.button('클릭')
if btn1:
    st.snow()
data = [
    {   'category': '공학자',
        'url' : 'data:image/jpeg;base64,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',
        'name' : '이름 : 마이클 패러데이',
        'content': '업적 : 전기와 자기의 연관성을 밝혀냄<br>'
                   '      전자기 유도를 발견<br>'
                   '      상대성 이론에도 영향을 미침'
                   ,
    },
    {
        'category': '공학자',
        'url' : 'https://w.namu.la/s/9544923e8e13f484ece84d729beab7f9cd84bc323068b4aa6125eba302fb6c265ac601b5ea2278c8a49351c78a3a9716258a8faf03f70e1b1fb9a0b860ffc2699ce68fd0752309e9482348926a70f831364fd2e56eeac47493a3e49dca4386a093b4677817ca932a4032317ffe0ba773',
        'name' : '이름 : 알베르트 아인슈타인',
        'content': '업적 : 광전효과<br>'
                   '      상대성이론<br>'
                   '      브라운 운동<br>'
                   '      중력파 존재 제시<br>'
                   '      로젠 다리<br>'
                   '      카르탕 이론<br>'
                   '      통일장 이론<br>'
                   '      우주 상수',
    },
    {
        'category': '공학자',
        'url' : 'https://search.pstatic.net/common/?src=https%3A%2F%2Fdbscthumb-phinf.pstatic.net%2F4876_000_1%2F20170419174902773_YMQQ5X68K.jpg%2Fca30_32_i9.jpg%3Ftype%3Dm4500_4500_fst&type=a340',
        'name' : '이름 : 찰스 휘트스톤',
        'content': '업적 : 휘트스톤 브릿지 개량 및 발전<br>'
                   '      휘트스톤 플레이페어 암호 발명<br>'
                   '      휘트스톤 ABC 전신기 발명<br>'
                   '      전위차계 개량 및 발전<br>'
                   '      입체경 발명 '
                   ,
    },
    {
        'category': '공학자',
        'url' : 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MDlfMSAg%2FMDAxNTk0MjQ5MTQwNTIy.3B7zJTxllEwKqYHaJ4XlW_uclk_m7QtHwAi4NCYMH4sg._ZYrF9DyPZ9XHUKt2XC0-5BmkZ1dp7IK2y7Fm-6jOT0g.JPEG.csibears01%2FClaudeShannon_MFO3807.jpg&type=a340',
        'name' : '이름 : 클로드 엘우드 섀넌',
        'content': '업적 : 균형 복원 포트폴리오 투자 이론<br>'
                   '      논리 게이트 개념 적립과 합성의 방법론 제시<br>'
                   '      새넌 분해<br>'
                   '      디지털 논리 회로 이론 창시<br>'
                   '      정보 엔트로피 제시<br>'
                   '      정보 이론 안전성 도입',
    },
    {
        'category': '공학자',
        'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MTBfMTk4%2FMDAxNjQ5NTg2NjA1NzU3.R1AgzimU1x31nRC8zr9tr4HlepPXk_uEUBmkpyZorLgg.dX1VvP8PXoeE_aHygQnv7NOqKK4cHlxwSDsYmbAi7CEg.JPEG.g_comics%2Fca780a8ec702a1d56edf38490aec7be8_11407621785.jpg&type=a340',
        'name': '이름 : 니콜라 테슬라',
        'content': '업적 : 테슬라 코일<br>'
                   '      레이더 초기 단걔 구상<br>'
                   '      전자보다 작은 입자가 존재할 것이라고 예측<br>'
                   '      무선 충전 기술 원리',
    },
    {
        'category': '물리학자',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUrLpIwe3st29NPFXsNAIQCMHfUDmNcuaySQ&usqp=CAU',
        'name': '이름 : 앙드레마리 앙페르',
        'content': '업적 : 앙페르 업칙 확립'
                   '      물지르이 자성을 설명하는 가설 설정<br>'
                   '      미분방정식 연구',
    },
    {
        'category': '물리학자',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA2EJCXvJzoTO0aV-TNDZ5CNF7s0dxoVMfIw&usqp=CAU',
        'name': '이름 : 필립 워런 앤더슨',
        'content': '업적 : 고온 초전도체 연구<br>'
                   '      응집물질물리학',
    },
    {
        'category': '물리학자',
        'url': 'https://t1.daumcdn.net/cfile/tistory/1408B8434F4444B43A',
        'name': '이름 : 하인리히 루돌프 헤르츠',
        'content': '업적 : 전자기파의 존재 확인<br>'
                   '      맥스웰 방정식 이론 고찰<br>'
                   '      질량과 시공에 의해서만 역학을 건설하려 시도',
    },
   {
        'category': '물리학자',
        'url': 'data:image/jpeg;base64,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',
        'name': '이름 : 루트비히 볼츠만',
        'content': '업적 : 기체운동론 확립<br>'
                   '      볼츠만 방정식<br>'
                   '      에너지 불연속 주장',
    },
    {
        'category': '물리학자',
        'url': 'https://w.namu.la/s/f3011a10a140c7125e134a2fd2bee79cda64df5270c5c3683fe8c850dfae70ab9b0f9914bf2b5f661bde0c3cb16313f970579bdab008e2b4657edcea28b875b4be3d159c8bbdc8027a3387d9a2314b3d29fe94e8570609f04ab848a16a65fc70ed88fb2121f7d7883c9f113ac53a9775',
        'name': '이름 : 리처드 파인만',
        'content': '업적 : 양자전기역학 완성<br>'
                   '      쿼크 모델이 창안되는 과정에서 업적 남김<br>'
                   '      나노머신 이론 최초 제창<br>'
                   '      양자 컴퓨터 고안자',
    }
    ]




def card_list(menu):
    result = ''
    for value in data:
        if value ['category'] == menu:
            result = result + f"""
    <div class="col">
    <div class="card" style="width: 18rem;">
  <img src="{value['url']}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">{value['name']}</h5>
    <p class="card-text">{value['content']}</p>
  </div>
  <ul class="list-group list-group-flush">
    </ul>
    </div>
    </div>
    """
    return result
menu = st.sidebar.selectbox('선택',('공학자','물리학자'))
components.html(
    f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script> 
<div class="container">
      <div class="row">
        
          {card_list(menu=menu)}
      </div>
    </div>
   """,height=1500
 )

