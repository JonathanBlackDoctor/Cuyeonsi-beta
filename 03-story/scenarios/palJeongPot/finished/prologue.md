---
module: prologue (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/prologue.md
outputs:
  - 프롤로그 압축본 (3개 씬, 분당→KTX→대구 성서 — 분기 그래프 풀과 동일)
status: review
---

# 03-story/scenarios/compressed/prologue.md

> 풀 `scenarios/prologue.md`의 압축 버전. NARRATION/MONOLOGUE 50~60% 삭감, DIALOGUE/KAKAO/CHOICE/FLAG/BG/BGM/SFX/CHARACTER/JUMP 100% 보존.
> 씬 ID·CHOICE next 그래프 풀과 동일.

---

# Scene: prologue_01_home
# Hint: chapter=0, time="2026-02-25 night", active=mom

[BG: bg_bundang_home fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 2026년 2월 25일 밤. 분당 본가 거실.

[CHARACTER: 윤모 center default fade]

[어머니] 윤모야, 짐 다 챙겼어?
[구윤모] 어. 거의 다 했어.
[어머니] 컵라면만 쌓아두지 말고. 무리는 마.
[구윤모] 응.

[SFX: 카톡_알림]

[KAKAO]
- {speaker:김규민} 야 윤모야 너 언제 내려오냐
- {speaker:구윤모} 모레
- {speaker:김규민} 와 ㅋㅋ 본과 시작 5일 전이노 ㅋㅋ
- {speaker:조나단} 윤모 과대던데 ㄷㄷ
- {speaker:김규민} 과대가 맨 마지막에 내려오는거 맞나 ㅋㅋ
- {speaker:구윤모} 아잇 분당 좀 더 누리다 갈래
- {speaker:표경민} 김규민 너 짐 정리는 했냐
- {speaker:김규민} ㅇㅇ 거의
- {speaker:표경민} 거의를 어떻게 믿냐
- {speaker:조나단} ㄹㅇㅋㅋ
[/KAKAO]

[CHARACTER: 윤모 center smile fade]

[BGM_STOP fade=2]

[JUMP: prologue_02_train]

---

# Scene: prologue_02_train
# Hint: chapter=0, time="2026-02-28 day", active=mom

[BG: bg_ktx_window fade]
[BGM: 일상 fade=3 volume=0.4]
[SFX: ktx_주행음 volume=0.6 loop]

[지문] 2월 28일 낮. 동대구행 KTX.

[CHARACTER: 윤모 center default fade]

[구윤모 모놀로그] 휴학 1년. 이제 진짜 시작이다.

[CHOICE]
- "본과는 빡세겠지만 재밌을 거다" {tone:bright_forward} → next: prologue_02b_positive
- "소문으로만 듣던 본과 생활.. 솔직히 좀 두렵다" {tone:warm_supportive} → next: prologue_02b_serious
- "어떻게든 되겠지 ㅋ" {tone:playful_casual} → next: prologue_02b_chill
[/CHOICE]

---

# Scene: prologue_02b_positive

[FLAG: flag_prologue_tone=positive]

[구윤모 모놀로그] 빡세겠지만 재밌을 거다. 어차피 가야 할 길.

[JUMP: prologue_02_after_choice]

---

# Scene: prologue_02b_serious

[FLAG: flag_prologue_tone=serious]

[구윤모 모놀로그] 솔직히 좀 두렵다. 갈리는 학년이라던데.

[JUMP: prologue_02_after_choice]

---

# Scene: prologue_02b_chill

[FLAG: flag_prologue_tone=chill]

[구윤모 모놀로그] 어떻게든 되겠지 ㅋ

[JUMP: prologue_02_after_choice]

---

# Scene: prologue_02_after_choice

[SFX: 카톡_알림]

[KAKAO]
- {speaker:표경민} 윤모 KTX임?
- {speaker:구윤모} ㅇㅇ 한 시간 남음
- {speaker:표경민} 도착하면 알려줘
- {speaker:김규민} 야 윤모 도착 하면 방학 최후의 한 잔 ㄱ?
- {speaker:구윤모} 내일 ㄱㄱ
- {speaker:조나단} 윤모 짐 풀고 OT 준비해야지
- {speaker:김규민} 아니그게중요해?
- {speaker:구윤모} 본과 1학년 OT 실감 안 남
- {speaker:표경민} 내일이면 실감 날걸
[/KAKAO]

[BGM_STOP fade=2]

[JUMP: prologue_03_studio]

---

# Scene: prologue_03_studio
# Hint: chapter=0, time="2026-02-28 evening", active=friend

[BG: bg_studio_room fade]
[BGM: 일상 fade=3 volume=0.5]

[지문] 같은 날 저녁. 대구 성서 자취방.

[CHARACTER: 윤모 center default fade]

[SFX: 카톡_알림]

[KAKAO]
- {speaker:김규민} 윤모 도착했나?
- {speaker:구윤모} ㅇㅇ 짐 풀고 있음
- {speaker:조나단} 윤모 OT 자료 봤나
- {speaker:구윤모} 어. 내일 9시 본관
- {speaker:표경민} 8시 50분까지는 가야한다던데
- {speaker:김규민} 윤모 과대 인사말 준비됐냐
- {speaker:구윤모} 즉흥.
- {speaker:김규민} ㄷㄷ
- {speaker:조나단} 그게 멋이지 ㅋ
- {speaker:김규민} 내일 보자
- {speaker:구윤모} ㅇㅋ
[/KAKAO]

[CHOICE]
- "내일 잘 해보자" {tone:direct_friendly} → next: prologue_03b_steady
- "일찍 자야겠다" {tone:mature_serious} → next: prologue_03b_practical
[/CHOICE]

---

# Scene: prologue_03b_steady

[FLAG: flag_prologue_close=steady]

[구윤모 모놀로그] 내일 잘 해보자. 첫 단추는 잘 끼워야지.

[JUMP: prologue_03_close]

---

# Scene: prologue_03b_practical

[FLAG: flag_prologue_close=practical]

[구윤모 모놀로그] 일찍 자야겠다. 첫날부터 졸리면 안 되지.

[JUMP: prologue_03_close]

---

# Scene: prologue_03_close

[CHARACTER: 윤모 center smile fade]

[구윤모 모놀로그] 본과 1학년. 시작이다.

[BGM: 메인_테마 fade=4 volume=0.6]
[SFX: 불_끄는_소리]

[지문] 윤모가 등을 끄고 침대로 향한다.

[JUMP: ch01_01_ot_intro]

---

## 압축 메모

- 풀 대비 NARRATION/MONOLOGUE 약 55% 삭감, 그 외 100% 보존.
- 씬 ID·CHOICE next 그래프·KAKAO 메시지·FLAG·BGM/SFX/BG 큐 풀과 1:1 동일.
- 어머니 대사 10개 100% 보존(가족 톤이 짧으면 무뚝뚝해 보임).
- 분기 그래프: 02b 3분기 → after_choice / 03b 2분기 → 03_close 동일.
