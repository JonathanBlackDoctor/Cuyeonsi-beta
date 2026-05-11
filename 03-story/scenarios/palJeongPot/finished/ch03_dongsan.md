---
module: ch03_dongsan (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/ch03_dongsan.md
outputs:
  - Ch.3 "동산" 압축본 (6개 메인 씬 + 4개 분기 — 분기 그래프 풀과 동일)
  - 변태 망상 페어 #3 보존 (Scene 02, 차세린 가운/스크럽)
  - CG 트리거 cg_serin_first_meet / cg_yuna_booth 보존
  - VIDEO 트리거 video_meet_serin / video_meet_yuna 보존
status: review
---

# 03-story/scenarios/compressed/ch03_dongsan.md

> 풀 `scenarios/ch03_dongsan.md`의 압축 버전. NARRATION/MONOLOGUE 50~60% 삭감, DIALOGUE 약 20% 가볍게 합치기, KAKAO/CHOICE/FLAG/INC/BG/BGM/SFX/CHARACTER/CG/VIDEO/JUMP 100% 보존.
> 변태 망상 페어 (Scene 02, `(망상 시작)` × 3 → `(자기자각)` × 3 → `(정상복귀)` × 2) 한 줄도 손대지 않음.
> 씬 ID·CHOICE next 그래프 풀과 동일.

---

# Scene: ch03_01_dongsan_lobby
# Hint: chapter=3, time="2026-04-06 morning"

[BG: bg_kmu_main fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 4월 6일 아침. 동산병원 견학 날.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 김규민 right default fade]

[김규민] 야 윤모, 가운 안 입고 왔어?
[구윤모] 견학은 사복 가능이라 했잖아.

[CHARACTER: 표경민 left_back default fade]

[표경민] 가자, 시간 됐다.

[CHARACTER: 조나단 center_back laugh fade]

[조나단] 헉, 늦었다 ㅋ
[구윤모] 네가 마지막.

[지문] 50명이 셔틀버스로 동산병원.

[BG: bg_dongsan_lobby fade]
[CHARACTER_HIDE: 김규민 fade]
[CHARACTER_HIDE: 표경민 fade]
[CHARACTER_HIDE: 조나단 fade]

[지문] 동산병원 로비.

[남희석] 본과 1학년 견학생들이죠? 내과 남희석 펠로우입니다. 한 시간 외래·병동 코스 돌고 끝낼 거예요.
[남희석] (창문 너머 가리키며) 저쪽이 내과 외래. 진료 한 건당 5분 안 됩니다.
[조나단] (작게) 5분이라고요?
[남희석] 한국 외래 현실이에요.

[남희석] 자, 다음은 병동 쪽으로.

[JUMP: ch03_02_serin_meet]

---

# Scene: ch03_02_serin_meet
# Hint: chapter=3, time="2026-04-06 morning, dongsan hospital", active=H1

[BG: bg_dongsan_lobby]

[지문] 윤모가 화장실 갔다 길을 잃는다.

[CHARACTER: 윤모 center default fade]

[BG: bg_dongsan_hallway fade]

[지문] 의국 복도. 옆 사무실에서 흰 가운의 여자가 차트를 들고 나온다. 부딪힐 뻔하다.

[CHARACTER: 차세린 right default fade]

[VIDEO: video_meet_serin]

[차세린] ...아.
[구윤모] 죄송합니다, 길을 잃어서요.
[차세린] 견학생이죠?

[CG: cg_serin_first_meet show]

[지문] 차세린. 흰 가운 안 청록 스크럽, 미디엄 헤어. 부드러운 미소에 옅은 피로.

[CG_HIDE]

[BGM: 코믹 fade=1 volume=0.4]
[CHARACTER: 윤모 center perv fade]

[구윤모 모놀로그] (망상 시작) ...어. 가운 안에 청록 스크럽.
[구윤모 모놀로그] (망상 시작) 누나가 야간 당직 끝나고 의국 소파에서 잠들어 계시는 모습을 보게 된다면...
[구윤모 모놀로그] (망상 시작) 어른스러운 표정이 풀어진 모습을 처음 보게 될 수도.

[CHARACTER: 윤모 center recover fade]

[구윤모 모놀로그] (자기자각) 아 진짜. 처음 본 사람 앞에서 뭐 하냐.
[구윤모 모놀로그] (자기자각) 누나는 일하러 가시는 분이고, 너는 길 잃은 견학생.
[구윤모 모놀로그] (자기자각) 정신 차려라 구윤모.

[CHARACTER: 윤모 center default fade]
[BGM: 일상 fade=1 volume=0.5]

[구윤모 모놀로그] (정상복귀) 길 묻기. 정중하게.

[차세린] 학생? 괜찮아요?
[구윤모] 아, 죄송합니다. 견학 중에 길을 잘못 들었습니다.
[차세린] 의국 복도까지 들어왔으면 잘못 든 게 맞네요. 단체는 병동 쪽이에요. 같이 가요.
[구윤모] 감사합니다.

[CHOICE]
- "공부 열심히 할게요" (진중하게) → next: ch03_02b_serious  {tone:mature_serious, key:true, descriptor:ch3_first_intro}
- "오늘 견학 잘 부탁드립니다" (가볍게 인사) → next: ch03_02b_casual  {tone:warm_supportive}
[/CHOICE]

---

# Scene: ch03_02b_serious

[FLAG: flag_h1_first_tone=serious]

[구윤모] 공부 열심히 할게요.

[CHARACTER: 차세린 right smile fade]

[차세린] 갑자기 진중하시네요.
[구윤모] 길 알려주시는데, 인사가 가벼우면 좀 그래서요.
[차세린] 본과 1학년이 그렇게 진중한 거 흔치 않은데. 6년, 같이 갑시다.

[JUMP: ch03_03_card_exchange]

---

# Scene: ch03_02b_casual

[FLAG: flag_h1_first_tone=casual]

[구윤모] 오늘 견학 잘 부탁드립니다.
[차세린] 네, 잘 가요.

[JUMP: ch03_03_card_exchange]

---

# Scene: ch03_03_card_exchange

[BG: bg_dongsan_hallway]

[차세린] (명함 건네며) 의국 직통 번호예요. 무슨 일 있으면 연락해요.
[구윤모] (양손으로 받으며) 감사합니다.

[지문] 명함: "차세린 / 동산의료원 내과 전공의 2년차".

[남희석] 윤모 학생, 어디 갔다 오는 거예요.
[구윤모] 죄송합니다, 길을 잃었습니다.
[남희석] (차세린 보며) 차 선생, 챙겨주셨어요?
[차세린] 마침 같은 길이라서요.
[남희석] 차 선생 평소엔 잘 안 웃는 분인데.
[차세린] 평소에도 잘 웃거든요. 선배가 안 봐서 그렇지.

[CHARACTER_HIDE: 차세린 fade]
[CHARACTER_HIDE: 남희석 fade]
[CHARACTER_HIDE: 윤모 fade]

[BGM_STOP fade=2]

[JUMP: ch03_04_back_to_school]

---

# Scene: ch03_04_back_to_school
# Hint: chapter=3, time="2026-04-06 afternoon", active=H1+H5

[BG: bg_kmu_main fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 견학 마치고 학교 복귀. 동아리 신입 모집 부스.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 김규민 right default fade]
[CHARACTER: 표경민 left_back default fade]
[CHARACTER: 조나단 center_back laugh fade]

[김규민] 윤모 견학에서 어디 갔다 왔냐.
[구윤모] 길 잃었다. 의국까지 들어갔다.
[표경민] 그래서 누구 만났냐.
[구윤모] 차세린 선생. 내과 전공의 2년차.
[김규민] 명함 받았냐.
[구윤모] 어, 의국 직통.
[표경민] 사고 나면 연락하라고 주신 거지, 따로 연락하라고 주신 게 아니야.

[메니스 후배] (부스에서) 윤모 형! 잠깐만요! 신입 다섯 명 등록받았어요!
[구윤모] 잘했어. 저녁에 들를게.

[VIDEO: video_meet_yuna]

[CHARACTER: 김규민 left_back default fade]
[CHARACTER: 장윤영 right smile_big fade]

[장윤영] 선배~~! 잠깐만요!

[지문] 긴 갈색 머리에 환한 미소. 의예과 2학년 장윤영.

[CG: cg_yuna_booth show]
[지문] 부스 앞. 장윤영이 환하게 웃으며 전단지를 든 채 다가온다.
[CG_HIDE]

[장윤영] 본과 선배님들이시죠? 저 의예과 2학년 장윤영이라고 해요!
[조나단] (작게) 본과는 신입 모집 대상 아닌 거 모르나 봐.
[장윤영] 알아요! 그냥 인사드리고 싶어서요!
[장윤영] (윤모 보며) 선배님, 카톡 해도 될까요?
[김규민] (작게) 와.
[표경민] (작게) 직진.

[CHOICE]
- "활기차네, 너" (솔직 답변) → next: ch03_04b_honest  {tone:bright_forward, key:true, descriptor:ch3_first_intro}
- "어, 그럼" (담담히 응답) → next: ch03_04b_neutral  {tone:direct_friendly}
[/CHOICE]

---

# Scene: ch03_04b_honest

[FLAG: flag_h5_first_tone=honest]

[구윤모] (옅게 웃으며) 활기차네, 너.

[CHARACTER: 장윤영 right blush fade]

[장윤영] 헉! 선배님이 말씀하시니까 더 좋아요!
[김규민] (작게) 야, 윤모 너 무슨 마법사야.

[JUMP: ch03_04_after_yuna]

---

# Scene: ch03_04b_neutral

[FLAG: flag_h5_first_tone=neutral]

[구윤모] (담담히) 어, 그럼.
[장윤영] 어 그럼이라니~ 너무 짧으세요!
[구윤모] 짧은 게 내 스타일이라.
[장윤영] 알겠어요! 카톡으로 길게 할게요!

[JUMP: ch03_04_after_yuna]

---

# Scene: ch03_04_after_yuna

[지문] 장윤영과 번호를 주고받는다.

[장윤영] 선배님 카톡 바로 드릴게요! 만나서 반가웠어요!

[CHARACTER_HIDE: 장윤영 fade]

[김규민] 야. 오늘 레지던트 누나 만나고 의예과 후배까지 알게 됐네.
[조나단] 풍년이다.
[표경민] 풍년이긴 한데, 시험 임박이라는 거 잊지 마라.
[구윤모] (피식) 그냥 우연.

[CHARACTER_HIDE: 김규민 fade]
[CHARACTER_HIDE: 표경민 fade]
[CHARACTER_HIDE: 조나단 fade]

[BGM_STOP fade=2]

[JUMP: ch03_05_kakao_night]

---

# Scene: ch03_05_kakao_night
# Hint: chapter=3, time="2026-04-06 night", active=H1+H2+H5

[BG: bg_studio_room fade]
[BGM: 카톡 fade=3 volume=0.4]

[지문] 같은 날 밤. 자취방.

[CHARACTER: 윤모 center default fade]

[SFX: 카톡_알림]

[지문] 1:1 카톡방. "차세린 선생님".

[KAKAO]
- {speaker:차세린} 학생, 오늘 무사히 복귀했나요?
- {speaker:구윤모} 네 잘 도착했습니다. 감사했습니다
- {speaker:차세린} 별일 아니에요. 다음에 또 길 잃으면 의국으로 와요 ㅎ
- {speaker:구윤모} 네 명심하겠습니다
[/KAKAO]

[SFX: 카톡_알림]

[지문] 1:1 카톡방. "장윤영".

[KAKAO]
- {speaker:장윤영} 선배~~~ 오늘 진짜 신났어요!! ✨
- {speaker:구윤모} 아 그렇게까지
- {speaker:장윤영} 선배 답장 빠르시네요! 답장 빠른 사람 좋아하거든요 🥹
- {speaker:장윤영} 선배 점심 저랑 한 번 같이 드실래요?
- {speaker:구윤모} 직진 폼 미쳤네
- {speaker:장윤영} 헉 들켰다! 저 직진형이거든요!!
- {speaker:구윤모} 점심은 일정 보고
- {speaker:장윤영} 네!!! 일정 알려주시면 맞출게요!!! 🥹✨
[/KAKAO]

[SFX: 카톡_알림]

[지문] 5조 단톡방.

[KAKAO]
- {speaker:오준혁} 윤모 견학 길 잃었다며 ㅋㅋ
- {speaker:이문규} 레지던트 누나 만났다는 것까지 다 들음
- {speaker:구윤모} 그냥 길 알려주신 거임
- {speaker:윤하정} ㅋㅋ 됐고 다음 주 시험 임박인 건 알지
- {speaker:구윤모} 도서관 가야지
- {speaker:정욱} 5조 도서관 자리 미리 잡자
[/KAKAO]

[SFX: 카톡_알림]

[지문] 1:1 카톡방. "윤하정".

[KAKAO]
- {speaker:윤하정} 야 견학 진짜 어땠음
- {speaker:구윤모} 별거 없어. 길 잃은 거 빼고는 무난
- {speaker:윤하정} 의국까지 들어간 게 무난이냐 ㅋㅋ
- {speaker:구윤모} 됐음
- {speaker:윤하정} 됐고 자라
- {speaker:구윤모} 너두
[/KAKAO]

[INC: H2 +1]

[CHARACTER: 윤모 center smile fade]

[BGM_STOP fade=2]

[JUMP: ch03_06_close]

---

# Scene: ch03_06_close

[BG: bg_studio_room]
[BGM: 메인_테마 fade=4 volume=0.5]

[지문] 윤모가 등을 끄고 침대로 향한다.

[구윤모 모놀로그] 동산병원까지. 어른의 미소, 후배의 환한 인사. 같은 날에 다 봤네. 다음 주는 시험.

[지문] — 끝 → Ch.4 "도서관"

[JUMP: ch04_01_library_late]
