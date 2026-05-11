---
module: ch06_h5_yuna (compressed)
hierarchy: 2
depends-on:
  - 00-master/MASTER-PLAN.md
  - 03-story/scenarios/ch06_h5_yuna.md
outputs:
  - Ch.6 "장윤영 분기" 압축본 (5개 메인 씬 + 12개 분기 + 1종 엔딩 — H5는 TRUE만 정식, 미달 시 SOLO 폴백)
  - KEY 3개 + IF 체인 평가 + TRUE/SOLO 폴백 100% 보존
  - CG cg_yuna_festival/true + VIDEO video_true_yuna 보존
status: review
---

# 03-story/scenarios/compressed/ch06_h5_yuna.md

> 풀 `scenarios/ch06_h5_yuna.md`의 압축 버전. NARRATION/MONOLOGUE 50% 삭감, DIALOGUE 약 20% 가볍게 합치기, KAKAO/CHOICE/IF/FLAG/INC/JUMP/ENDING/BG/BGM/SFX/CHARACTER/CG/VIDEO 100% 보존.
> 변태 망상 페어 0회 (Ch.6 0회 PM 결정 동일).
> 씬 ID·CHOICE next 그래프·IF 평가 체인 풀과 동일.

---

# Scene: ch06_h5_01_festival_booth
# Hint: chapter=6, heroine=H5, time="2026-06-01 afternoon"

[BG: bg_festival fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 6월 1일 오후. 축제 주간 첫날. 본관 앞 광장.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 장윤영 right smile_big fade]

[장윤영] 선배~~! 선배~~~!

[CG: cg_yuna_festival show]
[지문] 장윤영. 행사 유니폼. 응원 막대 두 개. 환한 미소.
[CG_HIDE]

[장윤영] 5조 부스 응원하러 왔거든요! ✨
[장윤영] 이거 한 개 드릴게요! 두 개 가져왔으니까 하나씩 흔들어요!

[CHARACTER: 김규민 left default fade]

[김규민] (작게) 의예과 동아리 손님이냐?
[조나단] 손님이 아니라 응원단 수준이네.

[CHARACTER_HIDE: 김규민 fade]

[CHOICE]
- "그 마음 가볍지 않은 거 알아, 조심히 사용할게" → next: ch06_h5_01b_take  {tone:bright_forward, key:true, descriptor:ch6_h5_appeal_take}
-
- "네가 무슨 전진이냐? 너무 나한테 직진만 하는 거 아냐?" → next: ch06_h5_01b_light  {tone:mature_serious}
[/CHOICE]

---

# Scene: ch06_h5_01b_take

[FLAG: flag_h5_open=take]

[구윤모] 윤영아.

[CHARACTER: 장윤영 right blush fade]

[장윤영] 선배... 이름 불러주셨어요!
[구윤모] 쉬는 시간 통째로 써준 거잖아. 그 마음 정중히 받을게.
[장윤영] 헉... 직진하는 거 부담된다는 분도 계셔서 잠깐 망설였거든요.
[구윤모] 진심이 들어 있는 응원이잖아. 받는 게 맞지.
[장윤영] 알겠어요! 신나게 응원해드릴게요! ✨

[INC: H5 +5]

[JUMP: ch06_h5_01_close]

---

# Scene: ch06_h5_01b_quick

[FLAG: flag_h5_open=quick]

[구윤모] 어, 응원 막대 잘 받을게.
[장윤영] 네! 두 개니까 하나씩 흔들어요! ✨

[JUMP: ch06_h5_01_close]

---

# Scene: ch06_h5_01b_light

[FLAG: flag_h5_open=light]

[구윤모] 너 너무 직진하잖아. 너희 부스부터 챙겨야지.

[CHARACTER: 장윤영 right pout fade]

[장윤영] 쉬는 시간 맞는데요. 잠깐만요.
[구윤모] 어, 미안. 분위기 못 맞췄네.

[JUMP: ch06_h5_01_close]

---

# Scene: ch06_h5_01_close

[BGM_STOP fade=2]
[CHARACTER_HIDE: 장윤영 fade]
[CHARACTER_HIDE: 윤모 fade]
[BG: black fade=3]

[JUMP: ch06_h5_02_club_event]

---

# Scene: ch06_h5_02_club_event
# Hint: chapter=6, heroine=H5, time="2026-06-03 afternoon"

[BG: bg_kmu_main fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 6월 3일 오후. 축제 셋째 날. 의예과 동아리 행사.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 장윤영 right outfit_festival fade]

[장윤영] [장윤영] 선배~~! 정말 와주셨네요 고마워요!
[구윤모] 응원 막대 받았으니까 한 번 와보는 게 맞지.
[장윤영] 풍선 정리 도와주실 수 있어요? 30분만요!

[CHOICE]
- "내가 계명의 정리왕이야 어디로 갈까" → next: ch06_h5_02b_help  {tone:bright_forward}
- "어, 30분만이면...뭐 그래 도와줄 수 있지" → next: ch06_h5_02b_help_quick  {tone:direct_friendly}
-
[/CHOICE]

---

# Scene: ch06_h5_02b_help

[FLAG: flag_h5_event=help]

[구윤모] 30분 같이 갈게. 의예과 회원들이 본과 한 명 와줘서 신난다는데.

[CHARACTER: 장윤영 right warm_smile fade]

[장윤영] 선배 그렇게까지 풀어주시는 거 의외예요!
[구윤모] 의예과 1·2학년 입장에선 본과 보기 힘드니까.
[장윤영] 그럼 풍선 정리 + 사진까지 같이 해요!
[구윤모] 사진까지면 35분 아니야?
[장윤영] 헉! 들켰다! 35분이요! ✨

[JUMP: ch06_h5_02_close]

---

# Scene: ch06_h5_02b_help_quick

[FLAG: flag_h5_event=help_quick]

[구윤모] 어, 30분만이지. 도와줄게.
[장윤영] 감사해요! 풍선 정리 같이 시작해요!

[JUMP: ch06_h5_02_close]

---

# Scene: ch06_h5_02b_partial

[FLAG: flag_h5_event=partial]

[구윤모] 5조 부스도 챙겨야 해서 잠깐만.
[장윤영] 네! 풍선 한 묶음만 같이요!

[JUMP: ch06_h5_02_close]

---

# Scene: ch06_h5_02_close

[지문] 30분 후. 부스 정리 마무리.

[장윤영] 사진 같이 찍어주신 거 감사해요! 의예과 단톡에 올려도 돼요?
[구윤모] 부스 분위기 사진이라면 괜찮지.
[장윤영] 부스 분위기 사진으로 올릴게요! ✨

[CHARACTER_HIDE: 장윤영 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h5_03_morning_library]

---

# Scene: ch06_h5_03_morning_library
# Hint: chapter=6, heroine=H5, time="2026-06-05 morning"

[BG: bg_kmu_main fade]
[BGM: 일상 fade=2 volume=0.5]

[지문] 6월 5일 오전 9시. 도서관 앞.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 장윤영 right smile_big fade]

[장윤영] 선배~~!

[장윤영] 어제 단톡에 사진 올렸는데, 1학년 후배들이 "본과 선배 멋있다" 댓글 남겼거든요. 부담될까 싶어서 짧게만요.
[구윤모] 부담될 걸 알고 짧게 끝낸 거 의외다. 직진하면서도 배려해줘서 고마워.
[장윤영] 헉 선배 그것까지 알아주시는 거 감사해요!

[CHOICE]
- "그 배려해주는 마음 잘 알아둘게" → next: ch06_h5_03b_distance  {tone:bright_forward}
- "사진 같이 찍은 건 같이 간 것 뿐이야, 부담 없어" → next: ch06_h5_03b_quick  {tone:direct_friendly}
[/CHOICE]

---

# Scene: ch06_h5_03b_distance

[FLAG: flag_h5_morning=distance]

[구윤모] 거리감 챙겨주는 마음 잘 받을게.

[CHARACTER: 장윤영 right blush fade]

[장윤영] 사실 단톡 자랑 안 한 것도 그 마음의 일부예요.
[구윤모] 그 마음이 한 학기 동안 깊어진 거지.

[장윤영] 선배. 6월 마지막 주에 인천 본가 갔다 와요. 의예과 2학기 전에요.
[구윤모] 인천 본가 잘 챙기고 와.

[INC: H5 +5]
[FLAG: flag_h5_incheon=mentioned]

[JUMP: ch06_h5_03_close]

---

# Scene: ch06_h5_03b_quick

[FLAG: flag_h5_morning=quick]

[구윤모] 어, 부담은 안 둬도 돼.
[장윤영] 알겠어요! 강의 가볼게요!

[JUMP: ch06_h5_03_close]

---

# Scene: ch06_h5_03_close

[CHARACTER_HIDE: 장윤영 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h5_04_late_kakao]

---

# Scene: ch06_h5_04_late_kakao
# Hint: chapter=6, heroine=H5, time="2026-06-06 late night"

[BG: bg_studio_room fade]
[BGM: 카톡 fade=3 volume=0.4]

[지문] 6월 6일 자정 12시 30분. 축제 마지막 날 끝난 후.

[CHARACTER: 윤모 center default fade]
[SFX: 카톡_알림]

[KAKAO]
- {speaker:장윤영} 선배~~~ 안 자세요?? ✨
- {speaker:장윤영} 부스 마무리 잘 하셨어요?
- {speaker:장윤영} 의대 축제 마지막 날 진짜 신났어요!! 😃😄
[/KAKAO]

[KAKAO]
- {speaker:구윤모} 응 안 잤지.
- {speaker:장윤영} 사흘 동안 마주친 순간들 다 마음에 두고 있거든요
- {speaker:장윤영} 학기 마무리 직전이라 한 번 더 얘기하는 거예요!
- {speaker:장윤영} 🥹
[/KAKAO]

[CHOICE]
- "마음 잘 받을게, 이제 자야 돼. 너도 자" → next: ch06_h5_04b_sleep  {tone:bright_forward, key:true, descriptor:ch6_h5_late_kakao}
- "마무리 잘 됐다는 거 잘 알겠어, 잘 자" → next: ch06_h5_04b_quick  {tone:direct_friendly}
- "직진 또 시작이네, 미치겠다 너때문에." → next: ch06_h5_04b_avoid  {tone:mature_serious}
[/CHOICE]

---

# Scene: ch06_h5_04b_sleep

[FLAG: flag_h5_late_kakao=sleep]

[KAKAO]
- {speaker:구윤모} 윤영아. 마음 잘 받을게
- {speaker:구윤모} 이제 자야 돼. 너도 자
- {speaker:장윤영} 헉 선배 두 번째예요. 자야 돼 너도 자
- {speaker:장윤영} 같은 말 두 번째라 더 무거워요 🥹
- {speaker:장윤영} 알겠어요. 두 번 받았으니까 두 번 잘게요
- {speaker:장윤영} 🥹🥹
- {speaker:구윤모} 잘 자
- {speaker:장윤영} 네!! 선배도 잘 주무세요!! ✨🥹
[/KAKAO]

[INC: H5 +5]
[FLAG: flag_h5_late_breath=on]

[JUMP: ch06_h5_04_close]

---

# Scene: ch06_h5_04b_quick

[FLAG: flag_h5_late_kakao=quick]

[KAKAO]
- {speaker:구윤모} 어 의대 축제 마무리 잘 됐다는 거 받을게. 너도 잘 자
- {speaker:장윤영} 네... 선배도 잘 자세요 ✨
[/KAKAO]

[JUMP: ch06_h5_04_close]

---

# Scene: ch06_h5_04b_avoid

[FLAG: flag_h5_late_kakao=avoid]

[KAKAO]
- {speaker:구윤모} 마음 받았는데 학기 마무리는 마무리로 두자
- {speaker:장윤영} ... 알겠어요 선배. 잘 자요 ✨
[/KAKAO]

[JUMP: ch06_h5_04_close]

---

# Scene: ch06_h5_04_close

[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h5_05_blossom_path]

---

# Scene: ch06_h5_05_blossom_path
# Hint: chapter=6, heroine=H5, time="2026-06-07 evening"

[BG: bg_campus_night_blossom fade]
[BGM: 로맨틱 fade=3 volume=0.5]

[지문] 6월 7일 저녁. 캠퍼스 벚꽃길.

[CHARACTER: 윤모 center default fade]
[CHARACTER: 장윤영 right warm_smile fade]

[장윤영] 선배. 한 학기 동안 선배 호칭. 처음부터 "선배~!"였잖아요. 한 학기 지나서 진심 한 줄씩 풀어 가는 사이가 됐는데, 호칭은 그대로네요.
[장윤영] 선배 호칭, 그만할까 싶어서요. 한 마디 조언 좀 해주세요!ㅎㅎ

[CHOICE]
- "선배 그만하고 '윤모'라고 불러도 돼" (호칭 변경) → next: ch06_h5_05b_call  {tone:bright_forward, key:true, descriptor:ch6_h5_call_yunyoung}
- "윤영, 호칭은 너 편한 대로." → next: ch06_h5_05b_call_partial  {tone:warm_supportive}
- "선배면 선배라 해야지." → next: ch06_h5_05b_keep  {tone:mature_serious}
[/CHOICE]

---

# Scene: ch06_h5_05b_call

[FLAG: flag_h5_call=full]

[구윤모] 선배 그만하고 "윤모"라고 불러도 돼. 먼저 꺼낸 마음에 답해주는 게 맞지.

[CHARACTER: 장윤영 right blush fade]

[장윤영] ...윤모. (옅은 미소) 윤모. 헉 두 번 부른 거 어색해요. 그런데 진짜 좋아요. ✨
[구윤모] 부르다 보면 익숙해질 거고.

[장윤영] 윤모. 인천 본가 갔다 와서 한 번 더 봬도 돼요?
[구윤모] 어. 한 번 더 보자. 인천 본가 잘 챙기고 와.
[장윤영] 알겠어요! 인천 갔다 와서 한 번 더 봐요!

[INC: H5 +5]
[FLAG: flag_h5_relationship=deep]

[JUMP: ch06_h5_05_close]

---

# Scene: ch06_h5_05b_call_partial

[FLAG: flag_h5_call=partial]

[구윤모] 윤영아. 호칭은 너 편한 대로.
[장윤영] 한 학기 더 선배 호칭으로 갈게요. 천천히요.

[JUMP: ch06_h5_05_close]

---

# Scene: ch06_h5_05b_keep

[FLAG: flag_h5_call=keep]

[구윤모] 선배 호칭 한 학기 더 가도 자연스러운데.
[장윤영] 네... 알겠어요, 선배. 한 학기 더 그대로 가요.

[JUMP: ch06_h5_05_close]

---

# Scene: ch06_h5_05_close

[장윤영] (옅게) 윤... 아니, 선배. 호칭 풀어주신 거 시간 좀 더 필요할 것 같아요.
[구윤모] 어 그래 너한테 맞출게.

[CHARACTER_HIDE: 장윤영 fade]
[CHARACTER_HIDE: 윤모 fade]
[BGM_STOP fade=2]
[BG: black fade=3]

[JUMP: ch06_h5_06_evaluate]

---

# Scene: ch06_h5_06_evaluate
# Hint: chapter=6, heroine=H5, time="branch evaluation"

[EVALUATE_TIER: H5]

[IF: H5 < 70]
[JUMP: ch06_h5_solo_fallback]
[ELSE]
  [IF: key_count_H5 >= 3]
  [JUMP: ch06_h5_true]
  [ELSE]
  [JUMP: ch06_h5_solo_fallback]
  [/IF]
[/IF]

---

# Scene: ch06_h5_true
# Hint: chapter=6, heroine=H5, ending=TRUE, time="2026-06-27 afternoon"

[BG: bg_campus_night_blossom fade=4]
[BGM: 클라이맥스 fade=4 volume=0.6]

[지문] 6월 27일 토요일 오후. 캠퍼스 벚꽃길. 인천 본가 다녀온 다음 날.

[CHARACTER: 윤모 center smile fade]
[CHARACTER: 장윤영 right outfit_dress fade]

[VIDEO: video_true_yuna]

[CG: cg_yuna_true show]
[지문] 벚꽃길. 장윤영. 가방 어깨에 메고 환한 미소.
[CG_HIDE]

[장윤영] 윤모...오빠!
[장윤영] (잠깐 멈춤) ...어. 선배. (다시) 오빠?!

[CHARACTER: 윤모 center blush fade]

[구윤모] 오빠라니 우리 더 가까워진 것 같다.
[장윤영] [장윤영] 인천 본가에서 연습했거든요! "선배" 안 붙이고 "윤모 오빠" 부르는 게 어렵더라고요!

[장윤영] 오빠! 본가에서 엄마랑 부스 사진 봤는데, "본과 선배랑 사진 같이 찍었네" 하시더라고요. 엄마가 저희 잘 어울린다 하던데요 ㅎㅎ
[장윤영] 이 말 듣고 집에서 생각해보니, "선배“ 호칭을 풀어가기로 결심했어요.

[INC: H5 +5]

[구윤모] 윤영아. 봄 내내 직진해 와준 마음 진짜 잘 받을게. 다섯 명 중에 너만 다른 결로 깊어졌어. 우리 함께 가자.
[장윤영] 헉 그렇게 말해주시면 제 심장이...너무 크게 뛰고 있어요...! 그런데 진짜 좋아요.🥰

[장윤영] 여름방학에 한 번 더 봐요. 인천 본가 한 번 와도 돼요.
[구윤모] 어. 갈게. 분당에서 인천이면 가까운 거리네. 그정도면 매일 왕복도 가능하겠는걸?
[장윤영] 헉! 진짜요?

[장윤영] 오빠. 다음 학기도 저와 같이 놀러가요! 여름에도. 의예과 2학기에도.
[구윤모] 어. 한 학기 더 가자, 윤영아.

[BGM: 클라이맥스 fade=2 volume=0.7]
[BG: black fade=4]

[지문] — 끝.
[지문] **장윤영 트루 엔딩 — 벚꽃길 너머**

[ENDING: END_H5_TRUE]

---

# Scene: ch06_h5_solo_fallback
# Hint: chapter=6, heroine=H5, fallback=SOLO, time="branch fallback to end_solo_summer"

[지문] — H5 1위이지만 트루 진입 조건 미달. SOLO 폴백 라우팅.

[JUMP: end_solo_summer_main]
