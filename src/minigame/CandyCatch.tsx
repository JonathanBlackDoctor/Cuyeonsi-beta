/**
 * CandyCatch — game.py(Pygame)의 HTML5 Canvas/TypeScript 포팅.
 *
 * 룰 (game.py와 1:1):
 *   - 1920×1080 가상해상도, 60초 제한, MAX_LIFE 3
 *   - 일반 츄파춥스 +10, 딸기(10% 확률) +30, 폭탄 -5 & 라이프 -1
 *   - 50점마다 난이도 1단계 (속도 ×1.1, 스폰 간격 단축, 하한선 적용)
 *
 * 입력: 키보드(← →, A/D) + 마우스/터치 드래그.
 * onComplete(raw) — 게임 종료(시간 0 또는 라이프 0) 직후 호출.
 */

import { useEffect, useRef } from 'react';

const SCREEN_W = 1920;
const SCREEN_H = 1080;
const PLAYER_W = 200;
const PLAYER_H = 200;
const PLAYER_SPEED = 18;
const ITEM_SIZE = 110;
const BOMB_SIZE = 130;
const MAX_LIFE = 3;
const SCORE_PER_ITEM = 10;
const SCORE_PENALTY_BOMB = 5;
const MAX_GAME_TIME = 60;
const FPS = 60;
const INITIAL_ITEM_SPAWN = 35;
const INITIAL_BOMB_SPAWN = 80;
const INITIAL_ITEM_SPEED_MIN = 6;
const INITIAL_ITEM_SPEED_MAX = 11;
const INITIAL_BOMB_SPEED_MIN = 8;
const INITIAL_BOMB_SPEED_MAX = 13;
const DIFFICULTY_INCREASE_INTERVAL = 50;

const ASSET_BASE = `${import.meta.env.BASE_URL}minigame/`;
const ASSETS = {
  player: `${ASSET_BASE}구윤모사탕.png`,
  strawberry: `${ASSET_BASE}츄파춥스 딸기.png`,
  green: `${ASSET_BASE}츄파춥스 초록색.png`,
  choco: `${ASSET_BASE}츄파춥스 초코.png`,
  bomb: `${ASSET_BASE}전공서적.png`,
  bg: `${ASSET_BASE}배경.png`,
};

interface FallingItem {
  x: number;
  y: number;
  size: number;
  speed: number;
  imgKey: 'strawberry' | 'green' | 'choco';
  isStrawberry: boolean;
}

interface BombItem {
  x: number;
  y: number;
  size: number;
  speed: number;
}

interface FloatingTextEntity {
  text: string;
  color: string;
  x: number;
  y: number;
  vy: number;
  life: number;
  maxLife: number;
}

function loadImage(src: string): Promise<HTMLImageElement> {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(img);
    img.src = src;
  });
}

export interface CandyCatchProps {
  onComplete: (raw: number) => void;
}

export function CandyCatch({ onComplete }: CandyCatchProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const containerRef = useRef<HTMLDivElement | null>(null);
  const completedRef = useRef(false);

  useEffect(() => {
    let cancelled = false;
    let rafId = 0;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const keys = { left: false, right: false };
    let pointerX: number | null = null;

    function onKeyDown(e: KeyboardEvent) {
      if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') keys.left = true;
      if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') keys.right = true;
      if (e.key === 'Enter' && state.gameOver) finish();
    }
    function onKeyUp(e: KeyboardEvent) {
      if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') keys.left = false;
      if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') keys.right = false;
    }

    function getCanvasX(clientX: number): number {
      const rect = canvas!.getBoundingClientRect();
      const rel = (clientX - rect.left) / rect.width;
      return rel * SCREEN_W;
    }
    function onPointerMove(e: PointerEvent) {
      if (e.pointerType === 'mouse' && e.buttons === 0) {
        pointerX = getCanvasX(e.clientX);
        return;
      }
      pointerX = getCanvasX(e.clientX);
    }
    function onPointerDown(e: PointerEvent) {
      pointerX = getCanvasX(e.clientX);
      if (state.gameOver) finish();
    }

    window.addEventListener('keydown', onKeyDown);
    window.addEventListener('keyup', onKeyUp);
    canvas.addEventListener('pointermove', onPointerMove);
    canvas.addEventListener('pointerdown', onPointerDown);

    const state = {
      playerX: SCREEN_W / 2 - PLAYER_W / 2,
      items: [] as FallingItem[],
      bombs: [] as BombItem[],
      floaters: [] as FloatingTextEntity[],
      score: 0,
      life: MAX_LIFE,
      frameCount: 0,
      remaining: MAX_GAME_TIME,
      difficulty: 1,
      speedMul: 1.0,
      itemSpawnRate: INITIAL_ITEM_SPAWN,
      bombSpawnRate: INITIAL_BOMB_SPAWN,
      gameOver: false,
      postGameTimer: 0,
    };

    const images: Record<string, HTMLImageElement | null> = {
      player: null,
      strawberry: null,
      green: null,
      choco: null,
      bomb: null,
      bg: null,
    };

    function finish() {
      if (completedRef.current) return;
      completedRef.current = true;
      cancelAnimationFrame(rafId);
      onComplete(state.score);
    }

    function rand(min: number, max: number) {
      return Math.random() * (max - min) + min;
    }
    function randInt(min: number, max: number) {
      return Math.floor(rand(min, max + 1));
    }

    function spawnItem() {
      const r = Math.random();
      let imgKey: FallingItem['imgKey'];
      let isStrawberry = false;
      if (r < 0.1) {
        imgKey = 'strawberry';
        isStrawberry = true;
      } else if (r < 0.55) {
        imgKey = 'green';
      } else {
        imgKey = 'choco';
      }
      const size = isStrawberry ? Math.floor(ITEM_SIZE * 1.5) : ITEM_SIZE;
      state.items.push({
        x: randInt(0, SCREEN_W - size),
        y: -size,
        size,
        speed: rand(INITIAL_ITEM_SPEED_MIN, INITIAL_ITEM_SPEED_MAX) * state.speedMul,
        imgKey,
        isStrawberry,
      });
    }
    function spawnBomb() {
      state.bombs.push({
        x: randInt(0, SCREEN_W - BOMB_SIZE),
        y: -BOMB_SIZE,
        size: BOMB_SIZE,
        speed: rand(INITIAL_BOMB_SPEED_MIN, INITIAL_BOMB_SPEED_MAX) * state.speedMul,
      });
    }

    function rectsOverlap(
      ax: number, ay: number, aw: number, ah: number,
      bx: number, by: number, bw: number, bh: number,
    ): boolean {
      return ax < bx + bw && ax + aw > bx && ay < by + bh && ay + ah > by;
    }

    function tick() {
      state.frameCount += 1;

      if (!state.gameOver) {
        // 입력
        if (pointerX !== null) {
          const targetX = pointerX - PLAYER_W / 2;
          const dx = targetX - state.playerX;
          const step = Math.sign(dx) * Math.min(Math.abs(dx), PLAYER_SPEED * 1.5);
          state.playerX += step;
        } else {
          if (keys.left) state.playerX -= PLAYER_SPEED;
          if (keys.right) state.playerX += PLAYER_SPEED;
        }
        if (state.playerX < 0) state.playerX = 0;
        if (state.playerX > SCREEN_W - PLAYER_W) state.playerX = SCREEN_W - PLAYER_W;

        // 시간
        state.remaining = MAX_GAME_TIME - Math.floor(state.frameCount / FPS);
        if (state.remaining <= 0) {
          state.remaining = 0;
          state.gameOver = true;
        }

        // 난이도
        const newDiff = 1 + Math.floor(state.score / DIFFICULTY_INCREASE_INTERVAL);
        if (newDiff > state.difficulty) {
          state.difficulty = newDiff;
          state.speedMul += 0.1;
          state.itemSpawnRate = Math.max(15, INITIAL_ITEM_SPAWN - state.difficulty * 3);
          state.bombSpawnRate = Math.max(20, INITIAL_BOMB_SPAWN - state.difficulty * 5);
        }

        if (state.frameCount % state.itemSpawnRate === 0) spawnItem();
        if (state.frameCount % state.bombSpawnRate === 0) spawnBomb();

        // 아이템 업데이트
        const playerRect = {
          x: state.playerX + 30,
          y: SCREEN_H - PLAYER_H - 10,
          w: PLAYER_W - 60,
          h: PLAYER_H - 30,
        };
        for (let i = state.items.length - 1; i >= 0; i--) {
          const it = state.items[i];
          it.y += it.speed;
          if (rectsOverlap(playerRect.x, playerRect.y, playerRect.w, playerRect.h, it.x, it.y, it.size, it.size)) {
            const earned = it.isStrawberry ? 30 : SCORE_PER_ITEM;
            state.score += earned;
            state.floaters.push({
              text: `+${earned}`, color: 'rgb(255,105,180)',
              x: state.playerX + PLAYER_W / 2, y: playerRect.y,
              vy: -2, life: 40, maxLife: 40,
            });
            state.items.splice(i, 1);
          } else if (it.y > SCREEN_H) {
            state.items.splice(i, 1);
          }
        }
        for (let i = state.bombs.length - 1; i >= 0; i--) {
          const b = state.bombs[i];
          b.y += b.speed;
          if (rectsOverlap(playerRect.x, playerRect.y, playerRect.w, playerRect.h, b.x, b.y, b.size, b.size)) {
            state.score = Math.max(0, state.score - SCORE_PENALTY_BOMB);
            state.life -= 1;
            state.floaters.push({
              text: `-${SCORE_PENALTY_BOMB}`, color: 'rgb(255,0,0)',
              x: state.playerX + PLAYER_W / 2, y: playerRect.y,
              vy: -2, life: 40, maxLife: 40,
            });
            state.bombs.splice(i, 1);
            if (state.life <= 0) state.gameOver = true;
          } else if (b.y > SCREEN_H) {
            state.bombs.splice(i, 1);
          }
        }
      } else {
        state.postGameTimer += 1;
      }

      // 플로터
      for (let i = state.floaters.length - 1; i >= 0; i--) {
        const f = state.floaters[i];
        f.y += f.vy;
        f.life -= 1;
        if (f.life <= 0) state.floaters.splice(i, 1);
      }

      draw();

      if (!state.gameOver || state.postGameTimer < 180) {
        rafId = requestAnimationFrame(tick);
      } else {
        // 정산 화면 3초 표시 후 자동 종료 (사용자 클릭/Enter로도 종료 가능)
        rafId = requestAnimationFrame(tick);
        if (state.postGameTimer >= 240) finish();
      }
    }

    function draw() {
      if (!ctx) return;
      if (images.bg) {
        ctx.drawImage(images.bg, 0, 0, SCREEN_W, SCREEN_H);
      } else {
        ctx.fillStyle = '#fdd9e6';
        ctx.fillRect(0, 0, SCREEN_W, SCREEN_H);
      }

      // 플레이어
      const py = SCREEN_H - PLAYER_H - 10;
      if (images.player) {
        ctx.drawImage(images.player, state.playerX, py, PLAYER_W, PLAYER_H);
      } else {
        ctx.fillStyle = '#ff69b4';
        ctx.fillRect(state.playerX, py, PLAYER_W, PLAYER_H);
      }

      // 아이템
      for (const it of state.items) {
        const img = images[it.imgKey];
        if (img) ctx.drawImage(img, it.x, it.y, it.size, it.size);
        else {
          ctx.fillStyle = '#ff5e8a';
          ctx.beginPath();
          ctx.arc(it.x + it.size / 2, it.y + it.size / 2, it.size / 2, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      // 폭탄
      for (const b of state.bombs) {
        if (images.bomb) ctx.drawImage(images.bomb, b.x, b.y, b.size, b.size);
        else {
          ctx.fillStyle = '#222';
          ctx.beginPath();
          ctx.arc(b.x + b.size / 2, b.y + b.size / 2, b.size / 2, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      // 플로터
      ctx.font = 'bold 48px sans-serif';
      ctx.textAlign = 'center';
      for (const f of state.floaters) {
        const alpha = f.life / f.maxLife;
        ctx.globalAlpha = alpha;
        ctx.fillStyle = f.color;
        ctx.fillText(f.text, f.x, f.y);
        ctx.globalAlpha = 1;
      }

      // HUD
      ctx.fillStyle = 'rgba(0,0,0,0.6)';
      ctx.fillRect(0, 0, SCREEN_W, 90);
      ctx.fillStyle = '#fff';
      ctx.font = 'bold 40px sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(`Lv.${state.difficulty}  |  SCORE: ${state.score}`, 30, 58);
      ctx.textAlign = 'center';
      ctx.fillStyle = state.remaining <= 10 ? '#ff2222' : '#ff1493';
      ctx.fillText(`남은 시간: ${state.remaining}초`, SCREEN_W / 2, 58);
      ctx.textAlign = 'right';
      ctx.fillStyle = '#fff';
      ctx.fillText(`LIFE: ${'♥'.repeat(state.life)}`, SCREEN_W - 30, 58);

      if (state.gameOver) {
        const fade = Math.min(state.postGameTimer / 30, 1) * 0.78;
        ctx.fillStyle = `rgba(15,15,15,${fade})`;
        ctx.fillRect(0, 0, SCREEN_W, SCREEN_H);

        if (state.postGameTimer >= 30) {
          ctx.fillStyle = '#fff';
          ctx.textAlign = 'center';
          ctx.font = 'bold 96px sans-serif';
          ctx.fillText('결과 정산', SCREEN_W / 2, 280);
          ctx.font = 'bold 60px sans-serif';
          ctx.fillText(`최종 점수: ${state.score}점`, SCREEN_W / 2, 400);

          const grade =
            state.score >= 700 ? 'S' :
            state.score >= 600 ? 'A' :
            state.score >= 500 ? 'B' :
            state.score >= 400 ? 'C' : 'F';
          const gradeColor =
            grade === 'S' ? '#ffd700' :
            grade === 'A' ? '#c0c0c0' :
            grade === 'B' ? '#cd7f32' :
            grade === 'C' ? '#888' : '#ff3030';
          ctx.fillStyle = gradeColor;
          ctx.font = 'bold 120px sans-serif';
          ctx.fillText(`랭크: ${grade}`, SCREEN_W / 2, 540);

          // bonus 미리보기
          const bonus = ((state.score - 500) / 200) * 50;
          const clampedBonus = Math.max(-50, Math.min(50, Math.round(bonus)));
          const sign = clampedBonus >= 0 ? '+' : '';
          ctx.fillStyle = clampedBonus >= 0 ? '#7cffb0' : '#ff8888';
          ctx.font = 'bold 80px sans-serif';
          ctx.fillText(`엔딩 보너스: ${sign}${clampedBonus}`, SCREEN_W / 2, 680);

          ctx.fillStyle = '#fff';
          ctx.font = '40px sans-serif';
          ctx.fillText('Enter 또는 클릭으로 계속', SCREEN_W / 2, SCREEN_H - 120);
        }
      }
    }

    // 자산 로드 후 게임 시작
    Promise.all([
      loadImage(ASSETS.player).then((i) => (images.player = i)),
      loadImage(ASSETS.strawberry).then((i) => (images.strawberry = i)),
      loadImage(ASSETS.green).then((i) => (images.green = i)),
      loadImage(ASSETS.choco).then((i) => (images.choco = i)),
      loadImage(ASSETS.bomb).then((i) => (images.bomb = i)),
      loadImage(ASSETS.bg).then((i) => (images.bg = i)),
    ]).then(() => {
      if (cancelled) return;
      rafId = requestAnimationFrame(tick);
    });

    return () => {
      cancelled = true;
      cancelAnimationFrame(rafId);
      window.removeEventListener('keydown', onKeyDown);
      window.removeEventListener('keyup', onKeyUp);
      canvas.removeEventListener('pointermove', onPointerMove);
      canvas.removeEventListener('pointerdown', onPointerDown);
    };
  }, [onComplete]);

  return (
    <div
      ref={containerRef}
      style={{
        position: 'fixed', inset: 0, background: '#000',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        zIndex: 9999,
      }}
    >
      <canvas
        ref={canvasRef}
        width={SCREEN_W}
        height={SCREEN_H}
        style={{
          width: 'min(100vw, calc(100vh * 16 / 9))',
          height: 'min(100vh, calc(100vw * 9 / 16))',
          touchAction: 'none',
          imageRendering: 'auto',
        }}
      />
    </div>
  );
}
