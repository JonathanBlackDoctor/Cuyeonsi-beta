---
module: ch06_h2_hajeong (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/ch06_h2_hajeong.md
outputs:
  - Ch.6 "윤하정 분기" 압축본 (5개 메인 씬 + 13개 분기 씬 + 4종 엔딩 — 분기 그래프 풀과 동일)
  - KEY 3개 + IF 체인 평가 + 4종 엔딩 100% 보존
  - CG cg_hajeong_drunk(HAPPY 재활용) + cg_hajeong_true + VIDEO video_true_hajeong 보존
status: review
---

# 03-story/scenarios/compressed/ch06_h2_hajeong.md

> 풀 `scenarios/ch06_h2_hajeong.md`의 압축 버전. NARRATION/MONOLOGUE 50% 삭감, DIALOGUE 약 20% 가볍게 합치기, KAKAO/CHOICE/IF/FLAG/INC/JUMP/ENDING/BG/BGM/SFX/CHARACTER/CG/VIDEO 100% 보존.
> 변태 망상 페어 0회 (Ch.6 0회 PM 결정 동일).
> 씬 ID·CHOICE next 그래프·IF 평가 체인 풀과 동일.

---

# Scene: ch06_h2_01_festival_booth
# Hint: chapter=6, heroine=H2, time="2026-06-01 afternoon"

[BG: bg_kmu_main fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 6월 1일 오후. 축제 주간 첫날. 5조 부스 운영.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 윤하정 right default fade]

[윤하정] 야, 윤모. 늦었네.
[구윤모] 5분 전인데?
[윤하정] 5분 전 = 늦은 거.

[CHARACTER: 오준혁 right_back default fade]

[정욱] 풍선 받아왔어.
[구윤모] 어제 집에서 키스연습하느라 좀 늦었어
[윤하정] 야..너무 앞서나가는거 아니야?

[INC: H2 +5]

[윤하정] 아니지아니지 이상한 소리하지마 구윤모
[구윤모] 미안 ㅎㅎ
[윤하정] ...뭐, 알면 됐어.

[CHOICE]
- "5조 든든해, 디테일 챙겨줘서 고마워" → next: ch06_h2_01b_thanks  {tone:direct_friendly, key:true, descriptor:ch6_h2_booth_team}
- "어, 부스 잘 굴리자" (담담히) → next: ch06_h2_01b_quick  {tone:direct_friendly}
- "윤하정 너 너무 빡세게 안 가도 돼ㅋㅋ" (가볍게) → next: ch06_h2_01b_light  {tone:playful_casual}
[/CHOICE]

---

# Scene: ch06_h2_01b_thanks

[FLAG: flag_h2_booth=thanks]

[구윤모] 5조 든든하다. 디테일 챙겨준 거, 고마워.

[CHARACTER: 윤하정 right blush fade]

[윤하정] ...너 답지 않잖아.
[구윤모] 가끔 보여야 분위기 돌아오지.
[윤하정] ...너도 잘 보고 있거든? 오늘 처음 한 말이니까.

[JUMP: ch06_h2_01_close]

---

# Scene: ch06_h2_01b_quick

[FLAG: flag_h2_booth=quick]

[구윤모] 어, 부스 잘 굴리자.
[윤하정] 어.

[JUMP: ch06_h2_01_close]

---

# Scene: ch06_h2_01b_light

[FLAG: flag_h2_booth=light]

[구윤모] 윤하정 너 너무 빡세게 안 가도 돼.

[CHARACTER: 윤하정 right pout fade]

[윤하정] 부스 운영 기본이거든? ...뭐, 됐어.

[JUMP: ch06_h2_01_close]

---

# Scene: ch06_h2_01_close

[CHARACTER_HIDE: 정욱 fade]
[CHARACTER_HIDE: 오준혁 fade]
[CHARACTER_HIDE: 이문규 fade]
[CHARACTER_HIDE: 윤하정 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h2_02_dongseong]

---

# Scene: ch06_h2_02_dongseong
# Hint: chapter=6, heroine=H2, time="2026-06-01 evening"

[BG: bg_dongseong_street fade]
[BGM: 일상 fade=2 volume=0.6]
[SFX: 술집_왁자지껄 volume=0.4]

[지문] 저녁. 동성로 술집. 단체 합석.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 윤하정 right outfit_party fade]

[윤하정] 어, 윤모. 옆자리 비었어.

[김규민] (단체 자리) 5조 부스 폼 미쳤다고 단톡에 풀렸다!

[INC: H2 +3]

[윤하정] 야, 윤모. 단체 한 시간이면 충분하지 않아? ...너랑 잠깐 갈라져서 더 걸어도 될 것 같고.
[구윤모] 연습한거 보여달라는 뭐 그런 의미인가?
[윤하정] …조용히 해

[CHOICE]
- "잠깐 같이 나가자" (산책 응답) → next: ch06_h2_02b_walk  {tone:direct_friendly}
- "윤하정 한 잔 더 받는 거 받아주자" (머무름) → next: ch06_h2_02b_stay  {tone:warm_supportive}
[/CHOICE]

---

# Scene: ch06_h2_02b_walk

[FLAG: flag_h2_dongseong=walk]

[구윤모] 같이 나가자.
[김규민] (작게) 윤모 윤하정 잠깐 나간다.

[CHARACTER_HIDE: 윤모 fade]
[CHARACTER_HIDE: 윤하정 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h2_03_walk]

---

# Scene: ch06_h2_02b_stay

[FLAG: flag_h2_dongseong=stay]

[구윤모] 한 잔 더 같이 받아주자.

[지문] 30분 후.

[윤하정] 윤모, 이제 갈래?

[CHARACTER_HIDE: 윤모 fade]
[CHARACTER_HIDE: 윤하정 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h2_03_walk]

---

# Scene: ch06_h2_03_walk
# Hint: chapter=6, heroine=H2, time="2026-06-01 night"

[BG: bg_dongseong_street fade]
[BGM: 로맨틱 fade=3 volume=0.4]

[지문] 밤 10시. 동성로.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 윤하정 right default fade]

[윤하정] 본과 1학년 한 학기 끝났네.
[윤하정] ...너 도서관에서 새벽 4시까지 옆자리 있어 준 거. 두 번 고맙다고 했는데, 두 번째는 아직 답 못 받았어.
[구윤모] 답이 뭐였더라.
[윤하정] ...뭐, 됐어. 잊어.

[CHOICE]
- "잊을 수 없지, 네 옆에서 한 페이지씩 넘긴 시간" → next: ch06_h2_03b_recall  {tone:direct_friendly}
- "그런 답 한 줄로 정리할 게 아니지" (담담히) → next: ch06_h2_03b_neutral  {tone:warm_supportive}
[/CHOICE]

---

# Scene: ch06_h2_03b_recall

[FLAG: flag_h2_recall=warm]

[구윤모] 잊을 수 없지. 너 옆에서 한 페이지씩 더 넘긴 시간이라.

[CHARACTER: 윤하정 right smile_small fade]

[윤하정] ...너 답지 않잖아.
[구윤모] 너 답지 않은 모습도 가끔 보여야지.
[윤하정] ...나도 너 옆자리 있는 거 보면서 한 페이지 더 넘긴 거야.

[JUMP: ch06_h2_03_extend]

---

# Scene: ch06_h2_03b_neutral

[FLAG: flag_h2_recall=neutral]

[구윤모] 그런 답 한 줄로 정리할 게 아니지.
[윤하정] ...어, 그래.

[JUMP: ch06_h2_03_extend]

---

# Scene: ch06_h2_03_extend

[윤하정] 야. 도서관 옥상 알아? 밤에 한 번도 안 가봤어.
[구윤모] 첫 야경?
[윤하정] ...뭐, 됐어. 다음에.

[CHOICE]
- "잠깐 더 걸을까, 옥상 같이 가자" → next: ch06_h2_03b_extend_warm  {tone:direct_friendly, key:true, descriptor:ch6_h2_walk_extend}
- "어, 다음에 가자" (담담) → next: ch06_h2_03b_extend_quick  {tone:warm_supportive}
- "너 술 한 잔 더 한 거 같은데 옥상은 좀 그렇지 않냐" (거절) → next: ch06_h2_03b_extend_light  {tone:playful_casual}
[/CHOICE]

---

# Scene: ch06_h2_03b_extend_warm

[FLAG: flag_h2_walk=extend]

[구윤모] 옥상 같이 가자. 첫 야경 옆에 누구 있는 게 의미 있지.

[CHARACTER: 윤하정 right blush fade]

[윤하정] ...알겠어. 같이 가자.

[JUMP: ch06_h2_03_close]

---

# Scene: ch06_h2_03b_extend_quick

[FLAG: flag_h2_walk=quick]

[구윤모] 어, 다음에 가자.
[윤하정] ...뭐, 그래도 잠깐 더 걷긴 하자.

[JUMP: ch06_h2_03_close]

---

# Scene: ch06_h2_03b_extend_light

[FLAG: flag_h2_walk=light]

[구윤모] 야 너 술 한 잔 더 한 거 같은데 옥상은 좀 그렇지 않냐.

[CHARACTER: 윤하정 right pout fade]

[윤하정] ...됐어. 자취방 방향이라 같이 걸어는 갈게.

[JUMP: ch06_h2_03_close]

---

# Scene: ch06_h2_03_close

[CHARACTER_HIDE: 윤모 fade]
[CHARACTER_HIDE: 윤하정 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h2_04_rooftop]

---

# Scene: ch06_h2_04_rooftop
# Hint: chapter=6, heroine=H2, time="2026-06-01 night, 11pm"

[BG: bg_library_night fade]
[BGM: 로맨틱 fade=3 volume=0.5]

[지문] 밤 11시. 본관 4층 도서관 옥상. 캠퍼스 야경.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 윤하정 right default fade]

[윤하정] ...야경이 이런 거구나.

[BGM: 로맨틱 fade=2 volume=0.5]

[윤하정] 야. 한 가지 할 말 있는데.
[윤하정] ...OT 때 너 처음 봤을 때부터, 신경 쓰였거든? 5조 같이 배정 받은 거 듣고 잠깐 멈췄던 게 그거.

[CHOICE]
- "너랑 있으면 내 가슴이 두근거려. 너의 입술을 탐하고 싶다는 생각밖에 안들어." (직설+망상) → next: ch06_h2_04b_honest  {tone:direct_friendly, key:true, descriptor:ch6_h2_rooftop_honest}
- "나도 너 좋아해" (직설) → next: ch06_h2_04b_direct  {tone:direct_friendly}
- "친구로 좋은데?" (회피) → next: ch06_h2_04b_friend  {tone:warm_supportive}
[/CHOICE]

---

# Scene: ch06_h2_04b_honest

[FLAG: flag_h2_rooftop=honest]

[구윤모] 너랑 있으면... 머리가 멍해져.

[CHARACTER: 윤하정 right blush fade]

[윤하정] ...그게 무슨 답이야.
[구윤모] 진심의 답이지.
[윤하정] ...너 그렇게 말하는 거 너 답지 않다.
[구윤모] 너 답지 않은 모습도 보여야지.
[윤하정] ...나도 그래.

[JUMP: ch06_h2_04_close]

---

# Scene: ch06_h2_04b_direct

[FLAG: flag_h2_rooftop=direct]

[구윤모] 나도 너 좋아해.

[CHARACTER: 윤하정 right blush fade]

[윤하정] 직설은 직설이네. ...뭐, 직설로 받을게.

[JUMP: ch06_h2_04_close]

---

# Scene: ch06_h2_04b_friend

[FLAG: flag_h2_rooftop=friend]

[구윤모] 친구로 좋은데?

[CHARACTER: 윤하정 right pout fade]

[윤하정] ...어, 그래. 친구로.

[JUMP: ch06_h2_04_close]

---

# Scene: ch06_h2_04_close

[윤하정] ...이제 가자.

[CHARACTER_HIDE: 윤모 fade]
[CHARACTER_HIDE: 윤하정 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h2_05_evaluate]

---

# Scene: ch06_h2_05_evaluate
# Hint: chapter=6, heroine=H2, time="branch evaluation"

[EVALUATE_TIER: H2]

[IF: H2 < 40]
[JUMP: ch06_h2_bad]
[ELSE]
  [IF: H2 < 60]
  [JUMP: ch06_h2_normal]
  [ELSE]
    [IF: H2 < 80]
      [IF: key_count_H2 >= 2]
      [JUMP: ch06_h2_happy]
      [ELSE]
      [JUMP: ch06_h2_normal]
      [/IF]
    [ELSE]
      [IF: key_count_H2 >= 3]
      [JUMP: ch06_h2_true]
      [ELSE]
      [JUMP: ch06_h2_happy]
      [/IF]
    [/IF]
  [/IF]
[/IF]

---

# Scene: ch06_h2_true
# Hint: chapter=6, heroine=H2, ending=TRUE, time="2026-06-27 morning"

[BG: bg_dongdaegu_station fade=4]
[BGM: 클라이맥스 fade=4 volume=0.6]

[지문] 6월 27일 오전. 동대구역. 부산행 KTX.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 윤하정 right warm_smile fade]

[VIDEO: video_true_hajeong]

[CG: cg_hajeong_true show]
[지문] 동대구역 플랫폼. 윤하정이 캐리어 옆에서 한 손을 든다. 햇살에 머리가 흩날리고, 따뜻한 미소.
[CG_HIDE]

[윤하정] 야.
[구윤모] 11시 정각.
[윤하정] 5분 늦게 와도 됐는데.
[구윤모] 오늘은 키스연습 좀 덜했다 ㅎㅎ
[윤하정] …연습좀 더 하고오지

[윤하정] 여름방학 끝나고 보자. 같이 견디는 식으로 가자.
[구윤모] 어. 같이 가자.
[윤하정] ...부산 한 번 와줘.
[구윤모] 그래. 갈게.

[윤하정] 갈게. 윤모.
[구윤모] 어. 잘 다녀와.

[BGM: 클라이맥스 fade=2 volume=0.7]
[BG: black fade=4]

[지문] — 끝.
[지문] **윤하정 트루 엔딩 — 동기의 봄**

[ENDING: END_H2_TRUE]

---

# Scene: ch06_h2_happy
# Hint: chapter=6, heroine=H2, ending=HAPPY, time="2026-06-14 afternoon"

[BG: bg_campus_cafe fade=3]
[BGM: 일상 fade=3 volume=0.5]

[지문] 6월 14일 오후. 본관 옆 카페.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 윤하정 right default fade]

[CG: cg_hajeong_drunk show]
[지문] 카페 창가. 윤하정이 따뜻한 음료를 감싸고 있다.
[CG_HIDE]

[윤하정] 야. 옥상에서 답한 거, 살짝 빨랐던 거 같아.
[구윤모] 살짝 빨랐지.
[윤하정] 친구에서 시작하자. 5조 동기로.
[구윤모] 그래. 친구에서 시작하자.

[BGM: 일상 fade=2 volume=0.6]
[BG: black fade=3]

[지문] — 끝.
[지문] **윤하정 해피 엔딩 — 해부 5조의 둘**

[ENDING: END_H2_HAPPY]

---

# Scene: ch06_h2_normal
# Hint: chapter=6, heroine=H2, ending=NORMAL, time="2026-06-08 evening"

[BG: bg_studio_room fade=3]
[BGM: 일상 fade=3 volume=0.4]

[지문] 6월 8일 저녁. 자취방.

[CHARACTER: 윤모 center default fade]

[SFX: 카톡_알림]

[KAKAO]
- {speaker:윤하정} 야 5조 다음 주 회식 있다. 윤모도 와
- {speaker:구윤모} 어 갈게
[/KAKAO]

[SFX: 카톡_알림]

[KAKAO]
- {speaker:윤하정} 야. 옥상 일은 5조 동기로 두자. 너랑 친구잖아
- {speaker:구윤모} 어 알겠어
[/KAKAO]

[BGM: 일상 fade=2 volume=0.5]
[BG: black fade=3]

[지문] — 끝.
[지문] **윤하정 노멀 엔딩 — 동기로 남은 봄**

[ENDING: END_H2_NORMAL]

---

# Scene: ch06_h2_bad
# Hint: chapter=6, heroine=H2, ending=BAD, time="2026-06-03 evening"

[BG: bg_lecture_day fade=3]
[BGM: 슬픔 fade=4 volume=0.4]

[지문] 6월 3일 오후. 부스 후속 회의. 5조 분위기 굳어 있다.

[CHARACTER: 윤모 center sad fade]
[CHARACTER: 윤하정 right pout fade]

[구윤모] 윤하정. 어제 옥상에서 내가 어설프게 한 게 있었던 거 같아.
[윤하정] ...뭐, 됐어. 후속 정리 끝내고 갈래.

[CHARACTER: 오준혁 left default fade]

[오준혁] (작게) 형, 윤하정 누나 컨디션 안 좋대요. 살살 가요.

[CHARACTER_HIDE: 윤하정 fade]

[BG: black fade=3]

[지문] — 끝.
[지문] **윤하정 배드 엔딩 — 굳어버린 5조**

[ENDING: END_H2_BAD]
