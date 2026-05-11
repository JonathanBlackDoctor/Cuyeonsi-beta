/**
 * 미니게임(CandyCatch) → 엔딩 점수 보너스 변환.
 *
 * 매핑 (사용자 결정 2026-05-12):
 *   raw 300 → -50, raw 500 → 0, raw 700 → +50 (선형, [-50, +50] clamp)
 *   - 원본 game.py GRADE_THRESHOLDS의 B(500) reward=0과 0 보너스 지점 일치.
 *   - S(700) / F(300) 컷에서 ±50 도달.
 */

export type MinigameGrade = 'S' | 'A' | 'B' | 'C' | 'F';

export function rawToBonus(raw: number): number {
  const x = ((raw - 500) / 200) * 50;
  const clamped = Math.max(-50, Math.min(50, Math.round(x)));
  return clamped;
}

export function gradeFromRaw(raw: number): MinigameGrade {
  if (raw >= 700) return 'S';
  if (raw >= 600) return 'A';
  if (raw >= 500) return 'B';
  if (raw >= 400) return 'C';
  return 'F';
}
