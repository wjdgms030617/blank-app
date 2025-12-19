import streamlit as st
import random

st.set_page_config(initial_sidebar_state="expanded")

# 초등학교 수학 스타일 CSS
st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background: #fce4ec;
    }
    
    /* 메인 컨테이너 */
    .main .block-container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem auto;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    /* 제목 스타일 */
    h1, h2, h3 {
        color: #000000 !important;
        font-family: 'Comic Sans MS', 'Arial Rounded MT Bold', sans-serif !important;
        font-size: 2.5em !important;
    }
    
    /* 버튼 스타일 - 메인 영역 (다음문제 버튼: 연한 하늘색) */
    .main .stButton > button {
        background: linear-gradient(45deg, #b3e5fc, #81d4fa) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(129, 212, 250, 0.3) !important;
        transition: all 0.3s ease !important;
        font-family: 'Comic Sans MS', sans-serif !important;
    }
    
    .main .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(129, 212, 250, 0.4) !important;
        background: linear-gradient(45deg, #90caf9, #64b5f6) !important;
    }
    
    /* 사이드바 버튼 스타일 (토너먼트 시작 버튼: 연보라) */
    .sidebar .stButton > button {
        background: linear-gradient(45deg, #e1bee7, #ba68c8) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(186, 104, 200, 0.3) !important;
        transition: all 0.3s ease !important;
        font-family: 'Comic Sans MS', sans-serif !important;
    }
    
    .sidebar .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(186, 104, 200, 0.4) !important;
        background: linear-gradient(45deg, #ce93d8, #ab47bc) !important;
    }
    
    /* 성공 메시지 */
    .stSuccess {
        background: linear-gradient(45deg, #4ecdc4, #44a08d) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3) !important;
    }
    
    /* 에러 메시지 */
    .stError {
        background: linear-gradient(45deg, #ff6b6b, #ff8e53) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    }
    
    /* 정보 메시지 */
    .stInfo {
        background: linear-gradient(45deg, #74b9ff, #0984e3) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(116, 185, 255, 0.3) !important;
    }
    
    /* 경고 메시지 */
    .stWarning {
        background: linear-gradient(45deg, #fdcb6e, #e17055) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        box-shadow: 0 4px 15px rgba(253, 203, 110, 0.3) !important;
    }
    
    /* 사이드바 스타일 */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
    }
    
    /* 프로그레스 바 */
    .stProgress > div > div > div {
        background: linear-gradient(45deg, #ff6b6b, #ffa500) !important;
    }
    
    /* 텍스트 입력 */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #ddd !important;
        padding: 10px !important;
        font-family: 'Comic Sans MS', sans-serif !important;
    }
    
    /* 선택 박스 */
    .stSelectbox > div > div {
        border-radius: 15px !important;
        border: 2px solid #ddd !important;
        font-family: 'Comic Sans MS', sans-serif !important;
    }
    
    /* 숫자 입력 */
    .stNumberInput > div > div > input {
        border-radius: 15px !important;
        border: 2px solid #ddd !important;
        font-family: 'Comic Sans MS', sans-serif !important;
    }
    
    /* 컬럼 스타일 */
    .element-container .stHorizontalBlock {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* 캡션 스타일 */
    .stCaption {
        color: #666 !important;
        font-family: 'Comic Sans MS', sans-serif !important;
        font-style: italic !important;
    }
    
    /* 마크다운 스타일 */
    .stMarkdown {
        color: #333 !important;
        font-family: 'Comic Sans MS', sans-serif !important;
    }
    
    /* 풍선 애니메이션 강화 */
    @keyframes balloonFloat {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    
    .balloon {
        animation: balloonFloat 3s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

def generate_decimals(n, decimals=3, seed=None):
    if seed is not None:
        random.seed(seed)
    max_val = 10 ** decimals
    vals = set()
    while len(vals) < n:
        v = random.randint(0, max_val - 1)
        vals.add(v)
    fmt = lambda x: f"0.{str(x).zfill(decimals)}"
    return [fmt(x) for x in sorted(vals)]


st.title("소수점 월드컵")
st.markdown("가장 작은 소수점을 찾아라! 🎆")
st.markdown(
    """
**게임 방법**  

1. 원하는 대진표 크기를 설정합니다.  
2. 둘 중 더 작은 소수점을 찾아서 버튼을 클릭하세요.  


속닥속닥) 🐰 🐫 🐬 🐧 각 대진마다 부화할 수 있는 캐릭터가 있습니다. 모든 캐릭터를 부화시킬 수 있도록 도전해보세요! 🐰 🐫 🐬 🐧
    """
)

if "current_round" not in st.session_state:
    st.session_state.current_round = []
if "next_winners" not in st.session_state:
    st.session_state.next_winners = []
if "match_index" not in st.session_state:
    st.session_state.match_index = 0
if "decimals" in st.session_state:
    del st.session_state["decimals"]
if "size" not in st.session_state:
    st.session_state.size = 36
if "score" not in st.session_state:
     st.session_state.score = 0
if "wrong_matches" not in st.session_state:
     st.session_state.wrong_matches = []
if "last_wrong" not in st.session_state:
     st.session_state.last_wrong = None

with st.sidebar:
    st.header("설정")
    stage_labels = {
        8: ("숲", "🌲"),
        16: ("사막", "🏜️"),
        32: ("바다", "🌊"),
        36: ("얼음", "❄️"),
    }
    size_options = [8, 16, 32, 36]
    size_labels = [f"{n}강 - {stage_labels[n][0]} {stage_labels[n][1]}" for n in size_options]
    size_idx = 3
    size_label = st.selectbox("대진표 크기", options=size_labels, index=size_idx)
    size = size_options[size_labels.index(size_label)]
    seed = st.number_input("난수 시드 (선택)", value=0, step=1)
    if seed == 0:
        seed = None
    if st.button("토너먼트 시작 / 초기화"):
        try:
            st.session_state.size = size
            nums = []
            per = size // 3
            remain = size - per * 3
            
            # decimals=1의 최대 고유 개수 고려
            if size == 36:
                # 36강 특별 처리: 1자리 10개, 2자리 13개, 3자리 13개
                nums.extend(generate_decimals(10, decimals=1, seed=(seed+1 if seed is not None else None)))
                nums.extend(generate_decimals(13, decimals=2, seed=(seed+2 if seed is not None else None)))
                nums.extend(generate_decimals(13, decimals=3, seed=(seed+3 if seed is not None else None)))
            else:
                for d in range(1, 4):
                    nums.extend(generate_decimals(per, decimals=d, seed=(seed+d if seed is not None else None)))
                if remain > 0:
                    for i in range(remain):
                        d = random.randint(1, 3)
                        nums.extend(generate_decimals(1, decimals=d, seed=(seed+100+i if seed is not None else None)))
            
            random.shuffle(nums)
            st.session_state.current_round = nums
            st.session_state.next_winners = []
            st.session_state.match_index = 0
            advance_round()
            st.session_state.score = 0
            st.session_state.wrong_matches = []
            st.session_state.last_wrong = None
            st.rerun()
        except Exception as e:
            st.error(f"토너먼트 시작 중 오류 발생: {e}")


def advance_round():
    # 마감된 라운드 처리: 잔여 항목(홀수 개)은 부전승
    cur = st.session_state.current_round
    winners = st.session_state.next_winners
    total_matches = len(cur) // 2
    
    # 라운드가 끝났을 때 부전승 처리 및 다음 라운드로
    if st.session_state.match_index >= total_matches:
        if len(cur) % 2 == 1:
            # 홀수 개면 마지막 항목이 자동 승리
            winners.append(cur[-1])
        if winners:
            # 스테이지 완료 축하 메시지 표시
            current_round_size = len(cur)
            if current_round_size > 2:  # 결승 제외
                # 스테이지별 축하 메시지
                stage_animals = {
                    8: ("토끼", "🐰"),    # 32강 완료
                    16: ("낙타", "🐫"),   # 16강 완료  
                    32: ("돌고래", "🐬"),  # 8강 완료
                    36: ("펭귄", "🐧")    # 9강 완료 (최종)
                }
                
                if current_round_size in [8, 16, 32]:
                    # 8강, 16강, 32강 완료
                    animal_name, animal_emoji = stage_animals[current_round_size]
                    st.success(f"🎉 스테이지 클리어! {animal_name} 부화 완료!")
                    st.markdown(f"## {animal_emoji}")
                    st.info("다른 스테이지도 도전해보세요!")
                    st.balloons()
                elif current_round_size == 36:
                    # 최종 스테이지 완료
                    st.success("🎉 모든 스테이지 완료! 축하합니다!")
                    st.balloons()
                
                import time
                time.sleep(2.0)  # 축하 메시지 표시 시간
            
            # 다음 라운드로 진행
            st.session_state.current_round = winners
            st.session_state.next_winners = []
            st.session_state.match_index = 0
            advance_round()
            return
    
    # 진행중인 매치 계산
    if len(cur) == 1:
        # 최종 동물 이모지
        stage_labels = {
            8: ("토끼", "🐰"),
            16: ("낙타", "🐫"),
            32: ("돌고래", "🐬"),
            36: ("펭귄", "🐧"),
        }
        animal_name, animal_emoji = stage_labels.get(int(st.session_state.size), ("동물", "🐣"))
        
        # 최종 결과 표시 (180초 동안 유지)
        import time
        if "final_display_start" not in st.session_state:
            st.session_state.final_display_start = time.time()
        
        st.success(f"최종 승자: {cur[0]}")
        st.markdown(f"## {animal_emoji} {animal_name} 부화 완료!")
        st.balloons()
        st.balloons()  # 추가 풍선 효과
        st.info("최종 부화 완료!")
        max_score = int(st.session_state.size) * 5 // 2
        st.markdown(f"### 🏆 내 최종 점수: {st.session_state.score}점 / 만점: {max_score}점")
        
        if st.session_state.wrong_matches:
            st.warning(f"총 {len(st.session_state.wrong_matches)}개의 오답이 있습니다.")
            if st.button("오답 다시 보기"):
                idx = st.session_state.last_wrong or 0
                wrong = st.session_state.wrong_matches[idx]
                st.info(f"[오답 라운드: {wrong['round']}강] {wrong['left']} vs {wrong['right']}")
                st.error(f"내 선택: {wrong['selected']} / 정답: {wrong['answer']}")
                if st.button("다음 오답", key="next_wrong"):
                    st.session_state.last_wrong = (idx + 1) % len(st.session_state.wrong_matches)
        
        # 50초 후에만 재시작 옵션 표시
        if time.time() - st.session_state.final_display_start >= 50.0:
            st.info("다른 대진도 도전!")
            if st.button("다른 대진도 도전하기", key="retry_tournament"):
                st.session_state.current_round = []
                st.session_state.next_winners = []
                st.session_state.match_index = 0
                st.session_state.score = 0
                st.session_state.wrong_matches = []
                st.session_state.last_wrong = None
                if "speed_start" in st.session_state:
                    del st.session_state["speed_start"]
                if "speed_timeout" in st.session_state:
                    del st.session_state["speed_timeout"]
                if "final_display_start" in st.session_state:
                    del st.session_state["final_display_start"]
        else:
            remaining_time = int(50.0 - (time.time() - st.session_state.final_display_start))
            st.info(f"🎉 축하합니다! {remaining_time}초 후에 다른 대진을 도전할 수 있습니다.")
    else:
        total_matches = len(cur) // 2
        mi = st.session_state.match_index
        # 자동으로 홀수 부전승 처리
        if total_matches == 0:
            # 예: 1개만 남음
            st.session_state.current_round = cur

        else:
            left = cur[mi * 2]
            right = cur[mi * 2 + 1]

            # 함정 카드: 값은 같지만 소숫점 자리수가 다른 경우
            def float_eq_str(a, b):
                try:
                    return float(a) == float(b) and a != b
                except:
                    return False

            if float_eq_str(left, right):
                st.warning("헷갈림 주의! 두 숫자의 값은 같지만 소숫점 자리수가 다릅니다.")

            col1, col2 = st.columns(2)
            # 한 번만 클릭해도 바로 반응하도록 매치별 클릭 상태 관리
            if "clicked_match" not in st.session_state:
                st.session_state.clicked_match = None
            if st.session_state.clicked_match != mi:
                left_clicked = right_clicked = False
                with col1:
                    if st.button(left, key=f"L-{mi}"):
                        st.session_state.clicked_match = mi
                        left_clicked = True
                with col2:
                    if st.button(right, key=f"R-{mi}"):
                        st.session_state.clicked_match = mi
                        right_clicked = True

                # 정답/오답 처리 및 점수
                selected = None
                if left_clicked or right_clicked:
                    selected = left if left_clicked else right
                    def is_correct(selected, a, b):
                        try:
                            return float(selected) == min(float(a), float(b))
                        except:
                            return False
                    correct = is_correct(selected, left, right)
                    import time

                    if correct:
                        st.session_state.score += 5
                        st.session_state.show_correct = True
                        st.session_state.correct_time = time.time()
                        st.session_state.next_winner_buffer = selected
                        st.rerun()
                    else:
                        # 오답 처리: 오답 기록 저장 및 정답 표시
                        correct_answer = min(left, right, key=lambda x: float(x))
                        st.session_state.wrong_matches.append({
                            'round': len(st.session_state.current_round),
                            'left': left,
                            'right': right,
                            'selected': selected,
                            'answer': correct_answer
                        })
                        st.session_state.show_wrong = True
                        st.session_state.wrong_time = time.time()
                        st.session_state.correct_answer = correct_answer  # 정답 저장
                        st.session_state.next_winner_buffer = correct_answer  # 정답을 승자로 설정
                        st.rerun()

            # 정답시 배너 유지 후 수동 진행
            if st.session_state.get("show_correct"):
                st.success("정답입니다!")
                if st.button("다음 문제", key="next_after_correct"):
                    selected = st.session_state.get("next_winner_buffer")
                    st.session_state.next_winners.append(selected)
                    st.session_state.match_index += 1
                    st.session_state.show_correct = False
                    st.session_state.next_winner_buffer = None
                    st.rerun()
            elif st.session_state.get("show_wrong"):
                correct_answer = st.session_state.get("correct_answer")
                st.error(f"오답입니다. 정답은 {correct_answer}입니다.")
                if st.button("다음 문제", key="next_after_wrong"):
                    selected = st.session_state.get("next_winner_buffer")
                    st.session_state.next_winners.append(selected)
                    st.session_state.match_index += 1
                    st.session_state.show_wrong = False
                    st.session_state.next_winner_buffer = None
                    st.session_state.correct_answer = None
                    advance_round()
                    st.rerun()
            # 문제가 처음 표시될 때는 아무 메시지도 표시하지 않음

            # 라운드가 끝났을 때 다음 라운드로 자동 이동
            if st.session_state.match_index >= total_matches:
                st.session_state.clicked_match = None
                advance_round()


# 토너먼트 시작 후 게임 화면 표시
if st.session_state.current_round:
    advance_round()


st.markdown("---")
st.caption("제작: 소수점 월드컵 — 0.xxx 형식의 숫자들을 비교해서 최종 승자를 찾습니다.")
