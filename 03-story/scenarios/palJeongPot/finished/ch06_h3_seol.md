---
module: ch06_h3_seol (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/ch06_h3_seol.md
outputs:
  - Ch.6 "한설 분기" 압축본 (3개 메인 씬 + 9개 분기 씬 + 평가 + 3종 엔딩 — H3는 BAD 없음)
  - KEY 3개 + IF 체인 평가 + 3종 엔딩 100% 보존
  - CG cg_seol_festival/late_night/true + VIDEO video_true_seol 보존
status: review
---

# 03-story/scenarios/compressed/ch06_h3_seol.md

> 풀 `scenarios/ch06_h3_seol.md`의 압축 버전. NARRATION/MONOLOGUE 50% 삭감, DIALOGUE 약 20% 가볍게 합치기, KAKAO/CHOICE/IF/FLAG/INC/JUMP/ENDING/BG/BGM/SFX/CHARACTER/CG/VIDEO 100% 보존.
> 변태 망상 페어 0회 (Ch.6 0회 PM 결정 동일).
> H3는 BAD 자리 NORMAL이 흡수 (시그니처 — IF 체인 풀과 동일).

---

# Scene: ch06_h3_01_festival_booth
# Hint: chapter=6, heroine=H3, time="2026-06-02 afternoon"

[BG: bg_festival fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 6월 2일 오후. 축제 주간 둘째 날.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 한설 right outfit_casual fade]

[지문] 한설. 베이지 카디건에 블라우스. 안경 그대로.

[구윤모] 어, 한설 선생님?
[한설] 나은영 교수님이 부스 들르라고 하셔서요.

[본과1 후배] 선생님, 트리스 완충액 실험대 위에 두고 나왔어요.
[한설] 한두 시간은 괜찮아요. 다음엔 점검 한 번 더 하세요.

[CHARACTER_HIDE: 본과1 후배 fade]

[INC: H3 +5]

[한설] 오늘 몇 시까지예요?
[구윤모] 6시까지요.
[한설] 잠깐만 부스 분위기 익히고 갈게요.

[CHOICE]
- "선생님, 길게 안 머무셔도 돼요. 짧게 인사만 하시고요" (본업 챙김) → next: ch06_h3_01b_care  {tone:warm_supportive, key:true, descriptor:ch6_h3_booth_care}
- "선생님 같이 부스 한 시간 도와주실래요?" (합류 권유) → next: ch06_h3_01b_invite  {tone:direct_friendly}
- "선생님도 부스 굴려보세요ㅋㅋ" (가볍게) → next: ch06_h3_01b_join  {tone:playful_casual}
[/CHOICE]

---

# Scene: ch06_h3_01b_care

[FLAG: flag_h3_booth=care]

[구윤모] 부스는 본과 1학년 자리니까 길게 안 머무셔도 돼요. 박사 5년차 본업 챙기시는 게 우선이에요.

[CHARACTER: 한설 right smile_slight fade]

[한설] 학생이 그렇게 챙겨주는 거 의외예요. 그럼 십 분만 더 있다 갈게요.

[JUMP: ch06_h3_01_close]

---

# Scene: ch06_h3_01b_invite

[FLAG: flag_h3_booth=invite]

[구윤모] 같이 한 시간 도와주실래요?
[한설] 실험 데이터 정리가 있어서 좀 무리일 것 같아요.
[구윤모] 아, 죄송해요.

[JUMP: ch06_h3_01_close]

---

# Scene: ch06_h3_01b_join

[FLAG: flag_h3_booth=join]

[구윤모] 선생님도 부스 굴려보세요ㅋㅋ

[CHARACTER: 한설 right concerned fade]

[한설] 부스 굴려보라는 게 어떤 의미인지 잠깐 헷갈려서요.
[구윤모] 아, 죄송해요. 분위기 못 맞췄네요.

[JUMP: ch06_h3_01_close]

---

# Scene: ch06_h3_01_close

[한설] 오늘 6시 끝나면 본관 옆 산책로 같이 걸어도 돼요? 머리 식히는 시간 있어도 좋을 것 같아서요.
[구윤모] 어, 네. 같이 가요.
[한설] 그럼 6시에 본관 1층 로비에서 봬요.

[CHARACTER_HIDE: 한설 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h3_02_walk]

---

# Scene: ch06_h3_02_walk
# Hint: chapter=6, heroine=H3, time="2026-06-02 evening"

[BG: bg_campus_night_blossom fade]
[BGM: 로맨틱 fade=3 volume=0.4]

[지문] 오후 6시 10분. 산책로.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 한설 right default fade]

[한설] 부스 잘 끝났어요?
[구윤모] 네, 잘 정리됐어요.

[구윤모] 십 분이 짧았어도 들러주신 것 자체에 무게가 있는 거니까요.
[한설] 그렇게 풀어주니까 마음이 좀 가볍네요.

[INC: H3 +5]

[한설] 안경 잠깐 벗어도 돼요? 좀 흐려서요.

[CHARACTER: 한설 right no_glasses fade]

[CG: cg_seol_festival show]
[지문] 산책로. 한설. 카디건에 블라우스. 안경 벗은 채. 부드러운 분위기.
[CG_HIDE]

[CHOICE]
- "와 한설쌤 너무 몸매가 좋으세요." (망상톤 솔직 감탄) → next: ch06_h3_02b_admire  {tone:warm_supportive, key:true, descriptor:ch6_h3_no_glasses_admire}
- "선생님은 늘 멋지세요" (정중) → next: ch06_h3_02b_polite  {tone:warm_supportive}
- "(말없이 옅게 미소)" (말 없음) → next: ch06_h3_02b_silent  {tone:mature_serious}
[/CHOICE]

---

# Scene: ch06_h3_02b_admire

[FLAG: flag_h3_admire=warm]

[구윤모] 와... 진짜 다른 사람 같으세요. 사복에 안경 없는 모습이 한층 부드러우세요.

[CHARACTER: 한설 right blush fade]

[한설] 그렇게 정색하고 그런 말 꺼내는 거 의외예요. 사복이 어색했는데 좀 풀리네요.

[JUMP: ch06_h3_02_close]

---

# Scene: ch06_h3_02b_polite

[FLAG: flag_h3_admire=polite]

[구윤모] 선생님은 늘 멋지세요.
[한설] 정중하게 받아주시네요. 어색함이 살짝 풀리네요.

[JUMP: ch06_h3_02_close]

---

# Scene: ch06_h3_02b_silent

[FLAG: flag_h3_admire=silent]

[지문] 윤모가 옅게 미소 짓는다.

[한설] 표정으로만 답하는 건가요?
[구윤모] 어떻게 풀어야 할지 잠깐 멈췄어요.

[JUMP: ch06_h3_02_close]

---

# Scene: ch06_h3_02_close

[한설] 오늘 실험실에서 데이터 정리할 예정이에요. 도서관 가는 길에 생화학실험실 한 번 들러도 돼요.
[구윤모] 네, 11시쯤 들를게요.
[한설] 네. 그래요.

[CHARACTER_HIDE: 한설 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]

[JUMP: ch06_h3_03_late_night_lab]

---

# Scene: ch06_h3_03_late_night_lab
# Hint: chapter=6, heroine=H3, time="2026-06-03 dawn 1am"

[BG: bg_biochem_lab_night fade]
[BGM: 일상 fade=3 volume=0.3]

[지문] 새벽 1시. 도서관 한 챕터 끝내고 실험실로.

[CHARACTER: 윤모 center default fade]

[SFX: 카톡_알림]

[KAKAO]
- {speaker:김규민} 야 윤모 어디
- {speaker:구윤모} 편의점
- {speaker:김규민} 새벽인데
- {speaker:구윤모} 야식 사러
- {speaker:김규민} ㅋㅋㅋㅋ 비밀ㅋ
[/KAKAO]

[지문] 편의점에서 김밥 두 줄, 캔커피, 컵라면.

[BG: bg_biochem_lab_night fade]
[BGM: 일상 fade=2 volume=0.4]

[CHARACTER: 한설 right tired fade]

[지문] 실험실. 한설. 안경 내려놓은 채.

[한설] 11시쯤이라 했는데 1시 넘었네요.
[구윤모] 한 챕터 더 정리하다 늦었어요.
[구윤모] 김밥 6줄, 컵라면 4개, 족발 2개, 핫바 4개 규민이랑 사고왔어요.
[한설] 어떻게 알았어요. 끓이다 그릇만 두고 데이터로 돌아간 거.
[구윤모] 컵라면 모양이 끓이다 만 모양이고요.

[INC: H3 +5]

[한설] 박사 5년차한테 학생이 야식 챙겨주는 거 처음이에요.
[구윤모] 선생님이랑 키스하고싶어서 미리 뇌물좀 드릴려고요 ㅎㅎ

[INC: H3 +5]

[BGM: 로맨틱 fade=2 volume=0.4]

[CG: cg_seol_late_night show]
[지문] 새벽 1시 실험실. 한설. 머그잔을 두 손으로. 안경 없이. 풀어진 표정.
[CG_HIDE]

[한설] 저도 윤모씨 보면 끌어안고 싶다는 생각이 맨날 들어요.

[CHOICE]
- "학생이 아니라 사람으로 옆에 있고 싶어요" (솔직 호감) → next: ch06_h3_03b_honest  {tone:warm_supportive, key:true, descriptor:ch6_h3_late_night_honest}
- "선생님 풀어진 모습 의외로 자연스러우세요" (정중) → next: ch06_h3_03b_safe  {tone:warm_supportive}
- "학생-조교 자리는 학생-조교니까요" (거리 두기) → next: ch06_h3_03b_distant  {tone:mature_serious}
[/CHOICE]

---

# Scene: ch06_h3_03b_honest

[FLAG: flag_h3_late_night=honest]

[구윤모] 선생님 옆에 있는 게. 학생이 아니라 사람으로 있고 싶어요.

[CHARACTER: 한설 right blush fade]

[한설] 박사 5년차한테 그런 말 흘리는 거 처음 받아봐요. ...사람으로 옆에 있는 거. 잠깐 마음에 두고 갈게요.
[한설] 오늘은 늦었으니까 자취방 가서 자고요. 시간 두고 정리해요.

[JUMP: ch06_h3_03_close]

---

# Scene: ch06_h3_03b_safe

[FLAG: flag_h3_late_night=safe]

[구윤모] 풀어진 모습 의외로 자연스러우세요.
[한설] 그렇게 받아주니까 마음이 가벼워지긴 하네요.

[JUMP: ch06_h3_03_close]

---

# Scene: ch06_h3_03b_distant

[FLAG: flag_h3_late_night=distant]

[구윤모] 학생-조교 사이는 학생-조교니까요.

[CHARACTER: 한설 right concerned fade]

[한설] 학생이 그렇게 정리하면 거기서부터 시작하는 거고요.

[JUMP: ch06_h3_03_close]

---

# Scene: ch06_h3_03_close

[한설] 야식 정말 고마워요.
[구윤모] 네, 선생님도 무리 마세요.

[CHARACTER_HIDE: 한설 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h3_04_evaluate]

---

# Scene: ch06_h3_04_evaluate
# Hint: chapter=6, heroine=H3, time="branch evaluation"

[EVALUATE_TIER: H3]

[IF: H3 < 40]
[JUMP: ch06_h3_normal]
[ELSE]
  [IF: H3 < 60]
  [JUMP: ch06_h3_normal]
  [ELSE]
    [IF: H3 < 80]
      [IF: key_count_H3 >= 2]
      [JUMP: ch06_h3_happy]
      [ELSE]
      [JUMP: ch06_h3_normal]
      [/IF]
    [ELSE]
      [IF: key_count_H3 >= 3]
      [JUMP: ch06_h3_true]
      [ELSE]
      [JUMP: ch06_h3_happy]
      [/IF]
    [/IF]
  [/IF]
[/IF]

---

# Scene: ch06_h3_true
# Hint: chapter=6, heroine=H3, ending=TRUE, time="2026-06-26 evening"

[BG: bg_anatomy_lab fade=4]
[BGM: 클라이맥스 fade=4 volume=0.6]

[지문] 6월 26일 저녁. 박사 논문실. 예심 발표 직후.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 한설 right warm_smile fade]

[VIDEO: video_true_seol]

[CG: cg_seol_true show]
[지문] 한설. 안경 벗고 미소. 화분 두 개 옆에 식물 일지.
[CG_HIDE]

[한설] 학생.
[구윤모] 축하드려요.

[구윤모] 화분 일지 봤어요. 예심 끝난 날 잎 한 장 새로 났다는 거. 정말 잘 어울리네요.
[한설] 학생이 그것까지 챙겨주니까 마음이 따뜻하네요.

[INC: H3 +5]

[한설] 새벽 1시 실험실에서 사람으로 옆에 있고 싶다고 한 그 답. 오늘이 정리하기 좋은 날이에요.

[한설] 학생... 이제 윤모씨. 사람으로 옆에 있는 거, 같이 가요. 박사 논문실 화분 옆에 학생 꽃다발 하나 자연스럽게 두는 자리 하나 더. 그게 사람으로 옆에 있는 모먼트고요.

[구윤모] 네, 선생님. 사람-사람 자리 하나 더. 그렇게 가요.
[한설] ...윤모씨. 그 말 정말 잘 받았어요.

[지문] (식물 일지) "2026.06.26 저녁. 화분 옆 꽃다발 하나 더. 윤모씨가."

[BGM: 클라이맥스 fade=2 volume=0.7]
[BG: black fade=4]

[지문] — 끝.
[지문] **한설 트루 엔딩 — 박사 논문의 늦은 봄**

[ENDING: END_H3_TRUE]

---

# Scene: ch06_h3_happy
# Hint: chapter=6, heroine=H3, ending=HAPPY, time="2026-06-14 night"

[BG: bg_biochem_lab_night fade=3]
[BGM: 일상 fade=3 volume=0.4]

[지문] 6월 14일 밤. 실험실.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 한설 right tired fade]

[CG: cg_seol_late_night show]
[CG_HIDE]

[한설] 사람으로 옆에 있고 싶다고 한 말. 아직 답이 정리되진 않았어요.
[구윤모] 네. 답은 답대로 두시고요. 다음 학기에도 잘 부탁드린다는 한마디면 충분합니다.
[한설] 학생이 흘려보낸 그 한마디, 마음에 두고 갈게요.

[BGM: 로맨틱 fade=2 volume=0.5]
[BG: black fade=3]

[지문] — 끝.
[지문] **한설 해피 엔딩 — 실험실의 밤**

[ENDING: END_H3_HAPPY]

---

# Scene: ch06_h3_normal
# Hint: chapter=6, heroine=H3, ending=NORMAL, time="2026-06-08 afternoon"

[BG: bg_anatomy_lab fade=3]
[BGM: 슬픔 fade=4 volume=0.4]

[지문] 6월 8일 오후. 생화학실험실 정기 점검.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 한설 right default fade]

[한설] 학생, 저는 학생이랑은 좀 안 맞아요.
[구윤모] 네, 선생님. 잘 받았습니다.
[한설] 학생-조교 사이 그대로 가요. 다음 학기에도 잘 부탁해요.
[한설] 6월 2일 야식 정말 고마웠어요. 그 일은 마음에 두고 갈게요.

[CHARACTER_HIDE: 한설 fade]
[CHARACTER_HIDE: 윤모 fade]

[BGM: 일상 fade=2 volume=0.4]
[BG: black fade=3]

[지문] — 끝.
[지문] **한설 노멀 엔딩 — 조교와 학생**

[ENDING: END_H3_NORMAL]
