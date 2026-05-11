/**
 * MiniGameGate — 팔정팟 각색본 엔딩 도달 시 점수 계산 직전에 CandyCatch 미니게임 모달 표시.
 * 게임 완료 시 raw 점수를 보너스(-50..+50)로 변환해 gameStore.minigameBonus에 저장.
 *
 * 비-팔정팟 모드에선 호출부에서 마운트 자체를 안 함 (EndingScreen 조건부).
 */

import { useState } from 'react';
import { useGameStore } from '@/stores/gameStore';
import { CandyCatch } from './CandyCatch';
import { rawToBonus, gradeFromRaw } from './scoring';

export function MiniGameGate({ onDone }: { onDone: () => void }) {
  const setMinigameBonus = useGameStore((s) => s.setMinigameBonus);
  const [phase, setPhase] = useState<'intro' | 'play' | 'result'>('intro');
  const [rawScore, setRawScore] = useState<number | null>(null);

  if (phase === 'intro') {
    return (
      <div
        style={{
          position: 'fixed', inset: 0, background: 'rgba(8,4,16,0.92)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          zIndex: 9999, color: '#fff', textAlign: 'center', padding: '24px',
        }}
      >
        <div style={{ maxWidth: 640 }}>
          <h2 style={{ fontSize: 36, marginBottom: 16 }}>
            🍭 보너스 라운드 — 사탕 받기
          </h2>
          <p style={{ fontSize: 18, lineHeight: 1.6, marginBottom: 24, color: '#ddd' }}>
            팔정팟 각색본 한정! 60초 동안 떨어지는 츄파춥스를 받아라.
            <br />
            결과에 따라 엔딩 최종 점수에 <b>-50 ~ +50</b> 보너스가 가산됩니다.
            <br />
            <span style={{ fontSize: 15, color: '#bbb' }}>
              조작: ← → 또는 A/D, 또는 마우스/터치 드래그. 전공서적(폭탄) 주의!
            </span>
          </p>
          <button
            type="button"
            onClick={() => setPhase('play')}
            style={{
              fontSize: 22, padding: '14px 36px', borderRadius: 999,
              background: '#ff5c95', color: '#fff', border: 'none', cursor: 'pointer',
              fontWeight: 700,
            }}
          >
            시작하기
          </button>
        </div>
      </div>
    );
  }

  if (phase === 'play') {
    return (
      <CandyCatch
        onComplete={(raw) => {
          setRawScore(raw);
          setPhase('result');
        }}
      />
    );
  }

  // result
  const raw = rawScore ?? 0;
  const bonus = rawToBonus(raw);
  const grade = gradeFromRaw(raw);
  const sign = bonus >= 0 ? '+' : '';

  return (
    <div
      style={{
        position: 'fixed', inset: 0, background: 'rgba(8,4,16,0.94)',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        zIndex: 9999, color: '#fff', textAlign: 'center', padding: '24px',
      }}
    >
      <div style={{ maxWidth: 640 }}>
        <h2 style={{ fontSize: 32, marginBottom: 12 }}>미니게임 결과</h2>
        <div style={{ fontSize: 22, color: '#ddd', marginBottom: 8 }}>
          점수 <b>{raw}</b> · 랭크 <b>{grade}</b>
        </div>
        <div
          style={{
            fontSize: 56, fontWeight: 800, marginBottom: 28,
            color: bonus >= 0 ? '#7cffb0' : '#ff8888',
          }}
        >
          엔딩 보너스 {sign}{bonus}
        </div>
        <button
          type="button"
          onClick={() => {
            setMinigameBonus(bonus);
            onDone();
          }}
          style={{
            fontSize: 22, padding: '14px 36px', borderRadius: 999,
            background: '#ff5c95', color: '#fff', border: 'none', cursor: 'pointer',
            fontWeight: 700,
          }}
        >
          최종 결과 보기
        </button>
      </div>
    </div>
  );
}
