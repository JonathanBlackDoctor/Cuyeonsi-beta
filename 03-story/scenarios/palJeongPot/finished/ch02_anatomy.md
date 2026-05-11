---
module: ch02_anatomy (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/ch02_anatomy.md
outputs:
  - Ch.2 "카데바" 압축본 (6개 메인 씬 + 4개 분기 — 분기 그래프 풀과 동일)
  - 변태 망상 페어 #2 보존 (Scene 04, 한설 안경 닦는 모먼트)
  - CG 트리거 cg_hajeong_anatomy / cg_seol_lab_first 보존
status: review
---

# 03-story/scenarios/compressed/ch02_anatomy.md

> 풀 `scenarios/ch02_anatomy.md`의 압축 버전. NARRATION/MONOLOGUE 50~60% 삭감, DIALOGUE/KAKAO/CHOICE/FLAG/BG/BGM/SFX/CHARACTER/CG/VIDEO/JUMP 100% 보존.
> 변태 망상 페어 (Scene 04, `(망상 시작)` × 3 → `(자기자각)` × 3 → `(정상복귀)` × 2) 한 줄도 손대지 않음.
> 12세 가드레일 동일: 카데바 시각 묘사 0건.
> 씬 ID·CHOICE next 그래프 풀과 동일.

---

# Scene: ch02_01_anatomy_morning
# Hint: chapter=2, time="2026-03-16 morning", active=H2

[BG: bg_studio_room fade]
[BGM: 긴장 fade=2 volume=0.4]

[지문] 3월 16일 아침. 자취방. 언제나 그랬듯, 나체

[CHARACTER: 윤모 center serious fade]

[BG: bg_kmu_main fade]
[SFX: 발자국 volume=0.3]

[지문] 의대 본관 앞.

[CHARACTER: 김규민 right default fade]

[김규민] (작게) 윤모. 같이 가자.
[구윤모] 어. 가자.

[CHARACTER_HIDE: 김규민 fade]

[BG: bg_anatomy_lab variant=entrance fade]

[지문] 실습실 입구. 50명이 흰 가운에 마스크.

[CHARACTER: 윤하정 left outfit_lab_coat fade]

[윤하정] 어. 왔어.
[구윤모] 어. 다들 일찍 왔네.

[이태호] 모였죠? 오늘 만날 분들은 본인 의지로 몸을 내어주신 분들입니다.
[이태호] 들어가서 묵념 같이 합시다. 사진, 영상, 카톡 절대 안 됩니다.
[이태호] 자, 뭐 빨리 끝내드릴 테니까 조원들끼리 술한잔 하세요

[CHARACTER_HIDE: 이태호 fade]
[CHARACTER_HIDE: 윤하정 fade]
[CHARACTER_HIDE: 윤모 fade]

[SFX: 실습실_문_열림 volume=0.4]

[JUMP: ch02_02_cadaver_first]

---

# Scene: ch02_02_cadaver_first
# Hint: chapter=2, time="2026-03-16 morning, anatomy lab", active=H2

[BG: bg_anatomy_lab variant=entrance]
[BGM: 긴장 volume=0.5]

[지문] 실습실 안. 5조가 실습대 옆에 자리 잡는다. 음침하게 하정의 옆으로 자리잡는 구씨.

[CHARACTER: 윤모 center serious fade]

[이태호] 예쁜애들 많네.

[구윤모 모놀로그] 하정이 손잡고싶다. 그 말밖에 안 떠오른다.

[이태호] 됐습니다. 시작합시다.

[CHARACTER: 윤하정 right outfit_lab_coat fade]

[지문] 윤하정의 손이 실습대 모서리를 잡고 있다. 살짝 떨린다.

[CHOICE]
- "괜찮아? 천천히 해" 작게 말한다 {tone:direct_friendly, key:true, descriptor:ch2_cadaver_calm} → next: ch02_02b_steady
- 같이 침묵하며 옆에 선다 {tone:warm_supportive} → next: ch02_02b_silent

[/CHOICE]

---

# Scene: ch02_02b_steady

[FLAG: flag_h2_cadaver_response=calm]

[구윤모] (낮게) ...괜찮아? 천천히 해.

[CHARACTER: 윤하정 right smile_small fade]

[윤하정] ...어. 너야말로 괜찮아 보이네.
[구윤모] 나도 떨려. 같이 가면 되지.
[윤하정] ...그래. 같이.

[JUMP: ch02_02_after_choice]

---

# Scene: ch02_02b_silent

[FLAG: flag_h2_cadaver_response=silent]

[지문] 윤모는 말 없이 윤하정 옆으로 한 발짝 더 다가선다.

[지문] 윤하정의 손 떨림이 한참 뒤에야 멎는다.

[JUMP: ch02_02_after_choice]

---

# Scene: ch02_02_after_choice

[CG: cg_hajeong_anatomy show]

[지문] 마스크 흘러내린 채로 윤하정이 옆을 흘끗 본다. 경멸하는 듯한 시선이 잠시 마주친다.

[CG_HIDE]

[이태호] 자, 5조부터 차례로 봅시다.

[구윤모 모놀로그] 봤다. 마음에 새겼다.

[지문] 한 시간 뒤. 첫 실습 끝.

[이태호] 일찍 마쳐드렸으니 조원들끼리 술 한잔 하세요 ^^

[BGM_STOP fade=3]
[BG: bg_kmu_main fade=3]

[CHARACTER: 윤모 center serious fade]
[CHARACTER: 윤하정 right serious fade]

[지문] 본관 앞. 햇볕.

[윤하정] 야. ...자꾸 말걸지 말아줄래. 태호쌤 생각나잖아.
[구윤모] 너는나를존중해야한다6년연임과대를할남자이며동기들을다재끼고메니스회장에등극한(생략)

[CHARACTER_HIDE: 윤하정 fade]
[CHARACTER_HIDE: 윤모 fade]

[JUMP: ch02_03_biochem_lab]

---

# Scene: ch02_03_biochem_lab
# Hint: chapter=2, time="2026-03-17 afternoon", active=H2+H3

[BG: bg_anatomy_lab variant=biochem fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 다음 날 오후. 첫 생화학 실험.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 한설 right default fade]

[한설] 여러분 이 experiment 하는 법 알아요 몰라요? 배웠어요? 아직은 question mark가 있어요? 빨리 말해주세요.
[한설] 이거 잘못 넣으면 실험 results가 잘못 나오니 꼭 label을 두번 확인해줘요.

[CHARACTER: 한설 right serious fade]

[한설] (5조 앞에서) 시약병 두 손으로 받쳐서 들어주세요.
[구윤모] 네, 알겠습니다.

[지문] 윤모가 시약을 마신다. 이를 하은설 교수님이 저지하려다 시약병이 부딪친다.

[SFX: 유리병_떨어짐 volume=0.6]

[지문] 시약병이 바닥에 깨진다.

[CHARACTER: 윤모 center panic fade]
[CHARACTER: 한설 right serious fade]

[한설] 조심한다고 했어요 안했어요? 실험실 수칙 알아요 몰라요?
[구윤모] 네... 죄송합니다.
[오준혁] 아오 윤모시치야!!

[CHOICE]
- "정말 죄송합니다. 생화학 교실에 들어가서 갚을게요." (진심 사과 + 자처) → next: ch02_03b_apologize  {tone:warm_supportive, key:true, descriptor:ch2_apology}
- "죄송합니다." (간단 사과 후 물러남) → next: ch02_03b_quick  {tone:mature_serious}
[/CHOICE]


---

# Scene: ch02_03b_apologize

[FLAG: flag_h3_apology=sincere]

[구윤모] (한 발 앞으로) 정말 죄송합니다. 청소도 도와드릴게요.

[CHARACTER: 한설 right smile_slight fade]

[한설] 아니에요. 유리 처리는 제가 할게요. 가운 끝자락 시약 묻은 거 닦고 와요.
[구윤모] 네, 정말 죄송합니다.
[한설] 괜찮아요. 첫 실험이라 그래요. 다음부터 두 손 다 비워두세요.

[JUMP: ch02_04_seol_recover]

---

# Scene: ch02_03b_quick

[FLAG: flag_h3_apology=quick]

[구윤모] 죄송합니다.

[CHARACTER: 한설 right serious fade]

[한설] 괜찮아요. 첫 실험이니까. 가운 끝자락 닦아요.

[JUMP: ch02_04_seol_recover]

---

# Scene: ch02_04_seol_recover

[CHARACTER: 한설 right smile_slight fade]

[VIDEO: video_meet_seol]

[CG: cg_seol_lab_first show]

[지문] 하은설이 정리를 마치고 자리로 돌아간다. 니트 + 마이크 + 옅은 미소.

[CG_HIDE]

[CHARACTER: 윤하정 left pout fade]

[윤하정] 야 너 개폐급이다.
[구윤모] 알겠다고.
[윤하정] 그래도 은설누나 침착하시네.

[지문] 하은설이 안경을 벗어 가운 자락으로 닦는다.

[BGM: 코믹 fade=1 volume=0.4]
[CHARACTER: 윤모 center perv fade]

[구윤모 모놀로그] (망상 시작) ...어. 안경.
[구윤모 모놀로그] (망상 시작) 안경 벗으셨을 때 표정이 평소랑 다른데... 풀어지시기도 하는구나.
[구윤모 모놀로그] (망상 시작) 야간 실험 끝나고 안경 닦으시는 순간을 옆에서 보면, 또 다른 표정이 있을 것도 같고...

[CHARACTER: 윤모 center recover fade]

[구윤모 모놀로그] (자기자각) 아 진짜. 시약 깬 학생이 무슨 망상을.
[구윤모 모놀로그] (자기자각) 감싸주신 분께 무슨 짓이야.
[구윤모 모놀로그] (자기자각) 정신 차려라 구윤모.

[CHARACTER: 윤모 center default fade]
[BGM: 일상 fade=1 volume=0.5]

[구윤모 모놀로그] (정상복귀) 가방 챙기자.
[구윤모 모놀로그] (정상복귀) 다음엔 꼭 마셔본다.

[CHARACTER: 한설 right default fade]

[한설] 다음 주에 마저 이어서 할게요. 시험범위 빡빡합니다.
[구윤모] 네. 다음 주에 뵙겠습니다.

[CHARACTER_HIDE: 한설 fade]
[CHARACTER_HIDE: 윤하정 fade]
[CHARACTER_HIDE: 윤모 fade]

[BGM_STOP fade=2]

[JUMP: ch02_05_kakao_night]

---

# Scene: ch02_05_kakao_night
# Hint: chapter=2, time="2026-03-17 night", active=H2+H3

[BG: bg_studio_room fade]
[BGM: 카톡 fade=3 volume=0.4]

[지문] 같은 날 밤. 자취방.

[CHARACTER: 윤모 center default fade]

[SFX: 카톡_알림]

[지문] 5조 단톡방.

[KAKAO]
- {speaker:오준혁} 윤모 살아 있냐
- {speaker:구윤모} ㅇㅇ 살아는 있음
- {speaker:오준혁} (움하하하하 이모티콘)
- {speaker:이문규} 윤모 은설누나랑 사귀냐?
- {speaker:윤하정} 잘 어울리네
- {speaker:구윤모} 아잇 이문규 미친거 아니야
- {speaker:정욱} 우우 나는 헬스하는 남자
- {speaker:오준혁} 낄낄낄
[/KAKAO]

[SFX: 카톡_알림]

[지문] 1:1 카톡방. "윤하정".

[KAKAO]
- {speaker:윤하정} 자?
- {speaker:구윤모} 깨어 있어. 너도?
- {speaker:윤하정} 말 걸지 말랬지
- {speaker:구윤모} 어제 + 오늘 두 콤보
- {speaker:윤하정} 어제는 진짜 ...너 옆에 있어줘서 더 무서웠음
- {speaker:구윤모} 너 마저도 그러면 3회 솔로총회가 열려
- {speaker:윤하정} (읽지 않는다)
- {speaker:구윤모} (눈물)
[/KAKAO]

[CHARACTER: 윤모 center smile fade]

[BGM_STOP fade=2]

[JUMP: ch02_06_close]

---

# Scene: ch02_06_close

[BG: bg_studio_room]
[BGM: 메인_테마 fade=4 volume=0.5]

[지문] 침대에서 현타를 느끼는 윤모

[구윤모 모놀로그] 카데바 첫 대면. 첫 실험. 첫 실수. 다음 주는 동산병원 견학.

[지문] — 끝 → Ch.3 "동산"

[JUMP: ch03_01_dongsan_lobby]

---

## 압축 메모

- 풀 대비 NARRATION/MONOLOGUE 약 55% 삭감, 그 외 100% 보존.
- **변태 망상 페어 (Scene 04, 한설 안경) 한 줄도 안 건드림** — 시그니처 보존.
- 톤 매트릭스 메타(`{tone:..., key:..., descriptor:...}`) 풀과 1:1 동일.
- CG 트리거 cg_hajeong_anatomy / cg_seol_lab_first 보존.
- 12세 가드레일: 카데바 시각 묘사 0건 그대로 (학생 표정/숨/지문만).
- 분기 그래프: 02b 2분기 / 03b 2분기 동일.
- DIALOGUE 100% 보존 — 이태호 교수/한설/윤하정/오준혁/김규민/윤모 모두.
