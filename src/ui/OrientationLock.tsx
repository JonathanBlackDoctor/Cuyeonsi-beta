/**
 * 세로모드 안내 토스트 — UI-SPEC §10 + MASTER-PLAN §5.5 (모바일 QA 2026-05-11 2차 처방).
 *
 * 이력:
 * - 1차(2026-05-11): React state(useState + matchMedia 구독 + sessionStorage)로 세션당 1회 2초 토스트.
 *   → 안드로이드 실기기에서 OP 영상 진입 직전 회귀 의심(불특정 '툭'+▶️). 회귀 원인 무관 회피 위해 JS 의존 0으로.
 * - 2차(현재): React state 없음. JSX 정적, globals.css의 미디어 쿼리 + CSS animation이 portrait 매칭 시 자동 2초 페이드.
 *   매번 portrait 진입 시 표시(세션당 1회 제약 포기) — JS state 재진입 없음 → re-render 0.
 *
 * `pointer-events: none`로 세로에서도 게임 입력 차단 X.
 */

export function OrientationLock() {
  return (
    <div className="orientation-lock-overlay" role="status" aria-live="polite">
      <div className="orientation-lock-icon" aria-hidden="true">
        🔄
      </div>
      <div className="orientation-lock-message">가로 버전 플레이를 추천합니다</div>
    </div>
  );
}
