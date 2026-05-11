---
module: ch06_h1_serin (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/ch06_h1_serin.md
outputs:
  - Ch.6 "차세린 분기" 압축본 (3개 메인 씬 + 11개 분기 씬 + 평가 + 4종 엔딩)
  - KEY 3개 + IF 체인 평가 + 4종 엔딩 100% 보존
  - CG cg_serin_festival/cafe_late/first_meet/true + VIDEO video_true_serin 보존
status: review
---

# 03-story/scenarios/compressed/ch06_h1_serin.md

> 풀 `scenarios/ch06_h1_serin.md`의 압축 버전. NARRATION/MONOLOGUE 50% 삭감, DIALOGUE 약 20% 가볍게 합치기, KAKAO/CHOICE/IF/FLAG/INC/JUMP/ENDING/BG/BGM/SFX/CHARACTER/CG/VIDEO 100% 보존.
> 변태 망상 페어 0회 (Ch.6 0회 PM 결정 동일).
> 씬 ID·CHOICE next 그래프·IF 평가 체인 풀과 동일.

---

# Scene: ch06_h1_01_festival_visit
# Hint: chapter=6, heroine=H1, time="2026-06-01 afternoon"

[BG: bg_festival fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 6월 1일 오후. 축제 주간 첫날. 본과 1학년 부스.

[CHARACTER: 윤모 center default fade]

[이문규] (작게) 야. 누구냐 저분.

[CHARACTER: 차세린 right outfit_casual fade]

[이문규] 윤모, 너 가서 인사해. 부스는 우리가 굴릴게.

[CHARACTER_HIDE: 이문규 fade]
[CHARACTER: 차세린 right outfit_casual fade]

[차세린] 학생. 외래 끝나고 잠깐 빠져나왔어요. 30분 비어서.

[CG: cg_serin_festival show]
[지문] 차세린. 베이지 셔츠 원피스에 카디건. 입가에 어색한 미소.
[CG_HIDE]

[차세린] (종이가방 건네며) 동산병원 카페에서 산 쿠키예요. 부스 사람들 나누세요.

[INC: H1 +5]

[차세린] 저는 들어가야겠어요. 당직이 6시부터라.

[CHOICE]
- "30분 시간 내주신 거 가볍지 않아요. 감사히 받을게요" (시간 무게 진중) → next: ch06_h1_01b_thanks  {tone:mature_serious, key:true, descriptor:ch6_h1_visit_take_care}
- "감사해요, 잘 챙겨갈게요" (담담히) → next: ch06_h1_01b_quick  {tone:warm_supportive}
- "선생님 직접 오시니까 분위기 살아나네요ㅋㅋ" (가볍게) → next: ch06_h1_01b_light  {tone:playful_casual}
[/CHOICE]

---

# Scene: ch06_h1_01b_thanks

[FLAG: flag_h1_visit=thanks]

[구윤모] 30분 시간 내서 와주신 거. 가볍지 않아요. 감사히 받을게요.

[CHARACTER: 차세린 right smile fade]

[차세린] ...학생, 정색하면서 그런 말 처음 듣네요.
[차세린] 와본 보람이 있다는 마음이 드네요. ...잘 받았어요. 진짜로.

[JUMP: ch06_h1_01_close]

---

# Scene: ch06_h1_01b_quick

[FLAG: flag_h1_visit=quick]

[구윤모] 감사해요. 잘 챙겨갈게요.
[차세린] 네, 부스 잘 마무리하세요.

[JUMP: ch06_h1_01_close]

---

# Scene: ch06_h1_01b_light

[FLAG: flag_h1_visit=light]

[구윤모] 선생님 직접 오시니까 분위기 살아나네요ㅋㅋ

[CHARACTER: 차세린 right concerned fade]

[차세린] ...학생. ㅋ 같은 건 카톡에서만 쓰는 거고요.
[구윤모] 아, 죄송해요. 톤을 못 맞췄네요.

[JUMP: ch06_h1_01_close]

---

# Scene: ch06_h1_01_close

[차세린] 학생. 새벽 1시쯤 동산병원 24시간 카페에 잠깐 들를게요. Ch.4 때 그 자리에서 한 번 더 봐도 좋고요.
[구윤모] 네, 도서관 정리하고 새벽쯤 갈게요.
[차세린] 그러면 거기서 봬요.

[CHARACTER_HIDE: 차세린 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h1_02_late_cafe]

---

# Scene: ch06_h1_02_late_cafe
# Hint: chapter=6, heroine=H1, time="2026-06-02 dawn 1am"

[BG: bg_campus_cafe_night fade]
[BGM: 잔잔 fade=3 volume=0.4]

[지문] 새벽 1시. 동산병원 24시간 카페.

[CHARACTER: 윤모 center default fade]

[SFX: 카톡_알림]

[KAKAO]
- {speaker:김규민} 야 윤모 어디
- {speaker:구윤모} 동산병원 카페
- {speaker:김규민} 누구 만나러 가는 거임
- {speaker:구윤모} 답 못 함
- {speaker:김규민} ㅋㅋ 잘 갔다와라
[/KAKAO]

[CHARACTER: 차세린 left tired fade]

[CG: cg_serin_cafe_late show]
[지문] 차세린. 창가에서 머그잔. 흰 가운에 청록 스크럽. 옅은 피로.
[CG_HIDE]

[구윤모] 선생님.
[차세린] ...진짜 왔네요.
[구윤모] 자연스러운 동선이라.

[차세린] 남희석 선배가 새벽 1시쯤엔 머그잔 정도는 있어야지, 하고 권하셨어요.

[INC: H1 +5]

[BGM: 로맨틱 fade=2 volume=0.4]

[차세린] 학생. 오후에 30분 시간 낸 게 가볍지 않다고 했던 거. 새벽까지 남아 있네요. 7살 차이인데 그렇게 받아주는 학생, 흔치 않거든요.

[CHOICE]
- "새벽 1시까지 버티시는 거 가볍지 않아요. 본인부터 챙기세요" → next: ch06_h1_02b_care  {tone:mature_serious, key:true, descriptor:ch6_h1_late_cafe_care}
- "선생님 오늘도 수고하셨네요" (담담히) → next: ch06_h1_02b_neutral  {tone:warm_supportive}
- "7살 차이는 7살 차이고요" (거리 두기) → next: ch06_h1_02b_distant  {tone:direct_friendly}
[/CHOICE]

---

# Scene: ch06_h1_02b_care

[FLAG: flag_h1_late_cafe=care]

[구윤모] 새벽 1시까지 버티시는 거, 가볍지 않아요. 본인부터 챙기세요.

[CHARACTER: 차세린 left smile fade]

[차세린] ...잘 받았어요. 진짜로.

[JUMP: ch06_h1_02_close]

---

# Scene: ch06_h1_02b_neutral

[FLAG: flag_h1_late_cafe=neutral]

[구윤모] 선생님 오늘도 수고 많으셨네요.
[차세린] 네, 학생도 도서관 잘 마무리해요.

[JUMP: ch06_h1_02_close]

---

# Scene: ch06_h1_02b_distant

[FLAG: flag_h1_late_cafe=distant]

[구윤모] 7살 차이는 7살 차이고요.

[CHARACTER: 차세린 left concerned fade]

[차세린] ...어, 그래요. 학생-선생님 사이. 그게 맞는 거지요.

[JUMP: ch06_h1_02_close]

---

# Scene: ch06_h1_02_close

[차세린] 토요일 6일은 외래 없는 날이에요. 6시쯤 본관 옆 산책로에서 봬요.
[구윤모] 네, 잘 챙기겠습니다.

[CHARACTER_HIDE: 차세린 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h1_03_walk]

---

# Scene: ch06_h1_03_walk
# Hint: chapter=6, heroine=H1, time="2026-06-06 evening"

[BG: bg_campus_night_blossom fade]
[BGM: 로맨틱 fade=3 volume=0.5]

[지문] 6월 6일 저녁. 본관 옆 산책로.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 차세린 right default fade]

[차세린] 학생, 정시네요.

[차세린] Ch.3 의국 복도에서 처음 봤던 거 기억나요? 정중하게 인사했잖아요. 의대생 중에 그렇게 정중한 사람 잘 없거든요.

[INC: H1 +5]

[차세린] 학생. 7살 차이가 가볍지 않아요. 학생이 자연스러운 사람이라는 건 알겠는데... 한 걸음 더 들어가는 데서 멈칫하게 되네요. ...괜찮을까요?

[INC: H1 +5]

[CHOICE]
- "누나" (처음 호칭) → next: ch06_h1_03b_noona  {tone:mature_serious, key:true, descriptor:ch6_h1_call_noona}
- "선배요" (선배 호칭) → next: ch06_h1_03b_sunbae  {tone:warm_supportive}
- "선생님이 편해요" (유지) → next: ch06_h1_03b_teacher  {tone:mature_serious}
[/CHOICE]

---

# Scene: ch06_h1_03b_noona

[FLAG: flag_h1_call=noona]

[구윤모] ...누나.

[CHARACTER: 차세린 right blush fade]

[구윤모] 7살이 가볍지 않다는 거 알아요. 누나라고요. 학생-선생님으로 끝내지 말고, 한 걸음만 풀어보고 싶어서요.

[차세린] ...한 학기 동안 못 들었던 말이에요. 그러면 저도 윤모로 풀어볼게요.
[차세린] ...잘 받았어요. 누나라는 호칭.

[JUMP: ch06_h1_03_close]

---

# Scene: ch06_h1_03b_sunbae

[FLAG: flag_h1_call=sunbae]

[구윤모] 선배요.
[차세린] ...선배도 한 걸음 풀린 호칭이긴 해요. 그쪽이 자연스럽다면 거기서 시작해도 좋고요.

[JUMP: ch06_h1_03_close]

---

# Scene: ch06_h1_03b_teacher

[FLAG: flag_h1_call=teacher]

[구윤모] 선생님이 편해요.

[CHARACTER: 차세린 right concerned fade]

[차세린] ...어, 그래요. 그게 편하다면 그쪽으로 가는 거지요.

[JUMP: ch06_h1_03_close]

---

# Scene: ch06_h1_03_close

[차세린] 8일 동산병원 회식 끝나면 빡빡해질 거예요. 카톡으로 안부 주고받으면서 마무리 잘 하세요.
[구윤모] 네, 누나도 무리하지 마시고요.

[CHARACTER_HIDE: 차세린 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h1_04_evaluate]

---

# Scene: ch06_h1_04_evaluate
# Hint: chapter=6, heroine=H1, time="branch evaluation"

[지문] — 부스, 새벽 카페, 산책. 7살의 거리와 호칭 변화.

[EVALUATE_TIER: H1]

[IF: H1 < 40]
[JUMP: ch06_h1_bad]
[ELSE]
  [IF: H1 < 60]
  [JUMP: ch06_h1_normal]
  [ELSE]
    [IF: H1 < 80]
      [IF: key_count_H1 >= 2]
      [JUMP: ch06_h1_happy]
      [ELSE]
      [JUMP: ch06_h1_normal]
      [/IF]
    [ELSE]
      [IF: key_count_H1 >= 3]
      [JUMP: ch06_h1_true]
      [ELSE]
      [JUMP: ch06_h1_happy]
      [/IF]
    [/IF]
  [/IF]
[/IF]

---

# Scene: ch06_h1_true
# Hint: chapter=6, heroine=H1, ending=TRUE, time="2026-07-04 morning"

[BG: bg_cafe_serin fade=4]
[BGM: 클라이맥스 fade=4 volume=0.6]

[지문] 7월 4일 오전. 분당 본가 근처 카페. 차세린의 짧은 휴가 첫날.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 차세린 right outfit_winter_coat fade]

[VIDEO: video_true_serin]

[CG: cg_serin_true show]
[지문] 분당 카페 창가. 차세린이 머그잔을 감싸고 시선을 들어 윤모를 본다. 7월 햇살. 따뜻한 미소.
[CG_HIDE]

[구윤모] 누나.
[차세린] ...산책로 말고는 처음. 어색한 게 아니라 한 번 더 듣고 싶었던 것 같아요.

[차세린] 사실 저 누나아니에요.
[구윤모] 네?? 그게 무슨 말이에요

[INC: H1 +5]

[차세린] 사실 저… 남자에요. 말 못해서 미안해 윤모야. 말 편하게 할게. 그래도 널 향한 마음은 진심이야♂

[구윤모] 네?? 잠시만요 전 준비가 안됐어요!!
[차세린] 윤모야 일로와 ♂

[BGM: 클라이맥스 fade=2 volume=0.7]

[지문] 머그잔 두 개가 나란히.

[BG: black fade=4]

[지문] — 끝.
[지문] 차세린 트루 엔딩 — 깨달은 성 정체성

[ENDING: END_H1_TRUE]

---

# Scene: ch06_h1_happy
# Hint: chapter=6, heroine=H1, ending=HAPPY, time="2026-06-27 evening"

[BG: bg_dongsan_hallway fade=3]
[BGM: 로맨틱 fade=3 volume=0.5]

[지문] 6월 27일 저녁. 동산병원 의국 휴게실.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 차세린 right tired fade]

[CG: cg_serin_first_meet show]
[지문] 의국 휴게실. 차세린. 흰 가운에 청록 스크럽. 옅은 미소.
[CG_HIDE]

[차세린] 윤모 학생.
[구윤모] 누나, 당직 수고하셨어요.

[차세린] 누나-동생 사이까지는 시간이 필요한 것 같아요. 다음 단계는 정리할 시간이 필요해요.
[구윤모] 네. 천천히 가는 게 맞아요. 다음 학기에 의국 한 번씩 들러도 돼요?
[차세린] ...다음에도 와줄래요? 자연스러워지면 그때 다음 단계 가요.

[차세린] ...한 학기 잘 와줬어요.

[BGM: 로맨틱 fade=2 volume=0.6]
[BG: black fade=3]

[지문] — 끝.
[지문] **차세린 해피 엔딩 — 내과 의국의 늦봄**

[ENDING: END_H1_HAPPY]

---

# Scene: ch06_h1_normal
# Hint: chapter=6, heroine=H1, ending=NORMAL, time="2026-06-10 afternoon"

[BG: bg_campus_cafe fade=3]
[BGM: 일상 fade=3 volume=0.4]

[지문] 6월 10일 오후. 본관 옆 카페.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 차세린 right default fade]

[차세린] 학생. 6일 산책로에서 호칭 권한 게 좀 빨랐던 것 같아요. 학생-선생님으로 한 학기 더. 그게 자연스러운 거리예요.
[구윤모] 네, 선생님. 잘 받았습니다. 천천히 가는 게 맞아요.

[차세린] 본과 1학년 마무리 잘 챙겨요. 다음 학기 견학에서 봬요.

[CHARACTER_HIDE: 차세린 fade]
[CHARACTER_HIDE: 윤모 fade]

[BGM: 일상 fade=2 volume=0.4]
[BG: black fade=3]

[지문] — 끝.
[지문] **차세린 노멀 엔딩 — 선후배의 거리**

[ENDING: END_H1_NORMAL]

---

# Scene: ch06_h1_bad
# Hint: chapter=6, heroine=H1, ending=BAD, time="2026-06-05 afternoon"

[BG: bg_dongsan_hallway fade=3]
[BGM: 슬픔 fade=4 volume=0.4]

[지문] 6월 5일 오후. 동산병원. 단체 견학.

[CHARACTER: 윤모 center sad fade]
[CHARACTER: 표경민 left default fade]

[표경민] 야, 윤모. 아까 자판기 앞에서 무슨 일 있었냐.

[CHARACTER_HIDE: 표경민 fade]

[구윤모 모놀로그] 본과 1학년 다 보는 앞에서 "선생님 새벽 카페 약속 또 있어요?" 한마디. 새벽 카페라는 단어를 꺼낸 거다.

[CHARACTER: 차세린 right concerned fade]

[차세린] 학생. 동기들 다 듣는 데서 새벽 카페라는 말 꺼낸 건 좀 곤란했어요. 견학 마무리 잘 하세요.

[CHARACTER_HIDE: 차세린 fade]

[SFX: 카톡_알림]

[KAKAO]
- {speaker:차세린} 학생 견학 마무리 잘 하세요
- {speaker:차세린} 한 학기 챙겨주신 거 마음에 두고 갈게요
- {speaker:차세린} 다만 동산병원 안에선 학생-선생님 자리로 정리하는 게 자연스러울 것 같아요
[/KAKAO]

[CHARACTER_HIDE: 윤모 fade]

[BGM: 슬픔 fade=2 volume=0.5]
[BG: black fade=3]

[지문] — 끝.
[지문] **차세린 배드 엔딩 — 잘못 짚은 마음**

[ENDING: END_H1_BAD]
