import streamlit as st

st.set_page_config(
    page_title="Turorial",
    page_icon="🎮",
)

st.write("# Opensource SW Final Project - 8조")

st.sidebar.success("위에서 원하는 게임을 선택하세요.")

st.markdown(
    """
    2024년 2학기, "오픈소스SW의이해" 8조 기말 프로젝트. <br>
    **👈 사이드 바에서 게임 선택**할 수 있습니다.<br>

    

    ## 1. 팀원 🧑‍🤝‍🧑
    팀원 | 학번 | 역할
    ---- | ---- | ----
    박건웅 | 20205164 | 문서 작성(요구사항 명세서, WBS)
    박성민 | 20215155 | 문서 작성(화면 설계서), 발표 자료 준비
    엄주성 | 20205202 | 게임 개발 감독
    정진영 | 20205252 | 프로젝트 계획 및 GitHub Repository 정리

    **※게임 개발(코드 작성)은 협력 활동 기록을 위해 공동 제작**
    <br><br>



    ## 2. 프로젝트 소개 📋
    - 미니 게임들을 모아서 플레이할 수 있도록 **파이썬 & Streamlit**을 사용.
    - **파이썬 언어로 개발**을 진행하며, 플레이어와 상호작용 시스템 구축을 위해 **프론트 엔드는 Streamlit**을 사용.
    - 랭킹, 업적 기능을 추가하여 플레이어가 게임 플레이에 대한 흥미를 끌어올리도록 구현.
    - 플레이 가능한 게임은 실시간으로 계속 추가 예정(2048, 스도쿠 등).
    <br><br>



    ## 3. 게임 플레이 방법 🎮
    1. 원하는 게임을 사이드바에서 선택하면, 해당 게임 페이지로 이동
    2. 게임 플레이는 키보드 입력 없이 마우스 클릭으로만 진행
    3. (게임 클리어 후 재시작, 메인 화면 이동, 업적 확인 가능하도록 구현 예정)
    <br>
    """,
    unsafe_allow_html=True
)