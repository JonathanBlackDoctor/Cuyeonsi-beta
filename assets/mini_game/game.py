import pygame
import random
import os
import sys
import math

# ==========================================
# 1. 게임 전역 설정 변수 (이곳의 숫자를 바꿔서 난이도를 조절해보세요!)
# ==========================================

# 화면 설정
SCREEN_WIDTH = 1920  # 화면 가로 크기 (Full HD 해상도)
SCREEN_HEIGHT = 1080 # 화면 세로 크기
FPS = 60             # 초당 프레임 수 (게임의 부드러움 정도)

# 색상 설정 (RGB 값)
COLOR_BG = (173, 216, 230)            # 파스텔 톤 하늘색 (배경)
COLOR_PLAYER_FALLBACK = (255, 105, 180) # 핑크색 (플레이어 이미지 없을 때 대체용 직사각형)
COLOR_CHUPA_FALLBACK = (255, 69, 0)   # 오렌지레드 (츄파츕스 이미지 없을 때 대체용 원)
COLOR_BOMB_FALLBACK = (50, 50, 50)    # 어두운 회색 (폭탄 이미지 없을 때 대체용 원)
COLOR_TEXT = (0, 0, 0)                # 검은색 (글자 색상)
COLOR_GAMEOVER = (255, 0, 0)          # 빨간색 (게임 오버 글자 색상)

# 플레이어 설정
PLAYER_WIDTH = 225    # 플레이어 가로 크기 (해상도에 맞춰 증가)
PLAYER_HEIGHT = 225   # 플레이어 세로 크기
PLAYER_SPEED = 18    # 플레이어 좌우 이동 속도 (해상도에 맞춰 증가)

# 아이템 (츄파츕스) 설정
ITEM_SIZE = 110      # 츄파츕스 크기 (해상도에 맞춰 증가)
INITIAL_ITEM_SPEED_MIN = 8  # 떨어지는 최소 속도
INITIAL_ITEM_SPEED_MAX = 14 # 떨어지는 최대 속도
INITIAL_ITEM_SPAWN_RATE = 60 # 생성 주기 (60프레임 = 1초마다 생성)

# 장애물 (폭탄) 설정
BOMB_SIZE = 110      # 폭탄 크기 (해상도에 맞춰 증가)
INITIAL_BOMB_SPEED_MIN = 10 # 폭탄 떨어지는 최소 속도
INITIAL_BOMB_SPEED_MAX = 15 # 폭탄 떨어지는 최대 속도
INITIAL_BOMB_SPAWN_RATE = 60 # 폭탄 생성 주기 (60프레임 = 1초마다 생성)

# 게임 규칙 설정
MAX_LIFE = 3         # 폭탄을 맞을 수 있는 최대 횟수 (라이프)
SCORE_PER_ITEM = 10  # 츄파츕스 획득 시 오르는 점수
SCORE_PENALTY_BOMB = 5 # 폭탄과 충돌 시 잃는 점수
MAX_GAME_TIME = 60  # 게임 제한 시간 (초)

# 난이도 조절 설정
DIFFICULTY_INCREASE_INTERVAL = 50 # 이 점수 단위마다 게임이 점점 빨라지고 아이템이 자주 떨어집니다.

# ==========================================
# [개발자 수정 구역] 등급 컷 및 호감도 보상 설정 (1분 기준 밸런스 조정)
# ==========================================
GRADE_THRESHOLDS = [
    {'grade': 'S', 'min_score': 700, 'reward': 20, 'color': (255, 215, 0)},   # 골드
    {'grade': 'A', 'min_score': 600, 'reward': 10, 'color': (192, 192, 192)}, # 실버
    {'grade': 'B', 'min_score': 500, 'reward': 0,  'color': (205, 127, 50)},  # 브론즈
    {'grade': 'C', 'min_score': 400, 'reward': -10, 'color': (100, 100, 100)},# 진회색
    {'grade': 'F', 'min_score': 300,  'reward': -20, 'color': (255, 0, 0)}     # 빨강
]
MAX_AFFECTION = 100 # 호감도 최대치 (100%)

# ==========================================
# 2. Pygame 초기화 및 기본 환경 세팅
# ==========================================
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("하늘에서 떨어지는 츄파츕스 받기!")
clock = pygame.time.Clock()

# 폰트 설정 (SCDream5.otf 사용)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(BASE_DIR, "SCDream5.otf")

try:
    if os.path.exists(font_path):
        font = pygame.font.Font(font_path, 36)
        large_font = pygame.font.Font(font_path, 72)
    else:
        # 파일이 없을 경우 시스템 폰트(맑은 고딕) 사용
        font = pygame.font.SysFont("malgungothic", 36)
        large_font = pygame.font.SysFont("malgungothic", 72)
except:
    font = pygame.font.Font(None, 36)
    large_font = pygame.font.Font(None, 72)


# ==========================================
# 이미지 미리 로드 및 충돌 판정 함수
# ==========================================
PLAYER_IMG = None
PLAYER_MASK = None
CHUPA_IMGS = []
CHUPA_MASKS = []
BOMB_IMG = None
BOMB_MASK = None
BG_IMG = None

# 현재 스크립트 파일이 위치한 폴더 경로 구하기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    img_path = os.path.join(BASE_DIR, '구윤모사탕.png')
    img = pygame.image.load(img_path).convert_alpha()
    PLAYER_IMG = pygame.transform.smoothscale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
    PLAYER_MASK = pygame.mask.from_surface(PLAYER_IMG)
except Exception as e:
    print(f"플레이어 이미지 로드 실패: {e}")

chupa_files = ['츄파춥스 딸기.png', '츄파춥스 초록색.png', '츄파춥스 초코.png']
for idx, file in enumerate(chupa_files):
    try:
        img_path = os.path.join(BASE_DIR, file)
        img = pygame.image.load(img_path).convert_alpha()
        if idx == 0: # 딸기 사탕은 크기를 1.5배 크게
            img = pygame.transform.smoothscale(img, (int(ITEM_SIZE * 1.5), int(ITEM_SIZE * 1.5)))
        else:
            img = pygame.transform.smoothscale(img, (ITEM_SIZE, ITEM_SIZE))
        CHUPA_IMGS.append(img)
        CHUPA_MASKS.append(pygame.mask.from_surface(img))
    except Exception as e:
        print(f"사탕 이미지 로드 실패 ({file}): {e}")

CLOCK_IMG = None
try:
    img_path = os.path.join(BASE_DIR, '하트시계.png')
    if os.path.exists(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        CLOCK_IMG = pygame.transform.smoothscale(img, (70, 70))
except Exception as e:
    pass

try:
    img_path = os.path.join(BASE_DIR, '전공서적.png')
    if os.path.exists(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        BOMB_IMG = pygame.transform.smoothscale(img, (BOMB_SIZE, BOMB_SIZE))
        BOMB_MASK = pygame.mask.from_surface(BOMB_IMG)
except Exception as e:
    pass

try:
    bg_path = os.path.join(BASE_DIR, '배경.png')
    if os.path.exists(bg_path):
        img = pygame.image.load(bg_path).convert()
        BG_IMG = pygame.transform.smoothscale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except Exception as e:
    print(f"배경 이미지 로드 실패: {e}")

def check_collision(obj1, obj2):
    # 두 객체 모두 마스크(투명도 기반 히트박스)가 있으면 정밀 충돌 판정
    if hasattr(obj1, 'mask') and obj1.mask and hasattr(obj2, 'mask') and obj2.mask:
        offset_x = obj2.rect.x - obj1.rect.x
        offset_y = obj2.rect.y - obj1.rect.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None
    # 마스크가 없으면 기존의 사각형 충돌 판정 사용
    return obj1.rect.colliderect(obj2.rect)


# ==========================================
# 3. 객체 클래스 정의 (플레이어, 파티클, 츄파츕스, 폭탄)
# ==========================================
class HeartParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.lifetime = random.randint(20, 40)
        self.max_lifetime = self.lifetime
        self.size = random.randint(15, 30)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, surface):
        if self.lifetime > 0:
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            heart_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            color = (255, 105, 180, alpha)
            r = self.size // 4
            if r > 0:
                pygame.draw.circle(heart_surf, color, (self.size//4, self.size//3), r)
                pygame.draw.circle(heart_surf, color, (self.size*3//4, self.size//3), r)
                pygame.draw.polygon(heart_surf, color, [(self.size//4 - r + 1, self.size//3), (self.size*3//4 + r - 1, self.size//3), (self.size//2, self.size*5//6)])
            surface.blit(heart_surf, (int(self.x), int(self.y)))

class FloatingText:
    def __init__(self, text, color, x, y):
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.vy = -2
        self.lifetime = 40
        self.max_lifetime = 40

    def update(self):
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, surface):
        if self.lifetime > 0:
            alpha = int(255 * (self.lifetime / self.max_lifetime))
            text_surf = font.render(self.text, True, self.color)
            text_surf.set_alpha(alpha)
            surface.blit(text_surf, (self.x - text_surf.get_width()//2, int(self.y)))

class BokehParticle:
    def __init__(self):
        self.radius = random.randint(10, 40)
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT + 200)
        self.vy = random.uniform(-0.5, -2.0)
        self.alpha = random.randint(20, 80)
        self.color = random.choice([(255, 182, 193), (255, 255, 255), (240, 248, 255)])

    def update(self):
        self.y += self.vy
        if self.y < -50:
            self.y = SCREEN_HEIGHT + 50
            self.x = random.randint(0, SCREEN_WIDTH)
            
    def draw(self, surface):
        circle_surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(circle_surf, (*self.color, self.alpha), (self.radius, self.radius), self.radius)
        surface.blit(circle_surf, (int(self.x) - self.radius, int(self.y) - self.radius))

class RainParticle:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, 0)
        self.vy = random.uniform(15.0, 25.0)
        self.length = random.randint(20, 50)
        self.alpha = random.randint(100, 200)

    def update(self):
        self.y += self.vy
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-50, 0)
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        pygame.draw.line(surface, (150, 180, 200, self.alpha), (self.x, self.y), (self.x, self.y + self.length), 2)

class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        # 화면 아래쪽 정중앙에 배치
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = PLAYER_SPEED
        
        # 전역 이미지 및 투명도 기반 히트박스(마스크) 설정
        self.image = PLAYER_IMG
        self.mask = PLAYER_MASK

        # 충돌 판정에 사용할 투명한 사각형(Hitbox) 영역
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dx):
        self.x += dx
        # 플레이어가 화면 밖으로 나가지 못하게 막기
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
        
        # 이동한 위치를 충돌 사각형(rect)에도 똑같이 반영
        self.rect.x = self.x

    def draw(self, surface):
        # 부드러운 타원형 그림자
        shadow_surf = pygame.Surface((self.width, self.height // 3), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow_surf, (0, 0, 0, 80), shadow_surf.get_rect())
        surface.blit(shadow_surf, (self.x, self.y + self.height - self.height // 4))

        if self.image:
            surface.blit(self.image, (self.x, self.y)) # 이미지가 있으면 이미지 그리기
        else:
            pygame.draw.rect(surface, COLOR_PLAYER_FALLBACK, self.rect) # 없으면 분홍색 사각형 그리기


class FallingItem:
    def __init__(self, speed_multiplier=1.0):
        self.size = ITEM_SIZE
        # X좌표는 화면 너비 안에서 랜덤하게 결정
        self.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.y = -self.size # 화면 맨 위 보이지 않는 곳에서 시작
        
        # 떨어지는 속도 = (기본 최소~최대 랜덤값) * 난이도 배율
        self.speed = random.randint(INITIAL_ITEM_SPEED_MIN, INITIAL_ITEM_SPEED_MAX) * speed_multiplier
        
        # 전역 츄파츕스 이미지 중 랜덤 선택 및 마스크 설정
        if CHUPA_IMGS:
            rand_val = random.random()
            if rand_val < 0.1: # 딸기는 10% 확률로 출현 (희귀)
                idx = 0
            elif rand_val < 0.55:
                idx = 1
            else:
                idx = 2
                
            self.image = CHUPA_IMGS[idx]
            self.mask = CHUPA_MASKS[idx]
            self.is_strawberry = (idx == 0)
            self.size = int(ITEM_SIZE * 1.5) if self.is_strawberry else ITEM_SIZE
        else:
            self.image = None
            self.mask = None
            self.is_strawberry = False

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def fall(self):
        self.y += self.speed # 아래로 이동
        self.rect.y = int(self.y)

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, int(self.y)))
        else:
            # 이미지가 없으면 츄파츕스 대체용 원형 그리기
            pygame.draw.circle(surface, COLOR_CHUPA_FALLBACK, (self.rect.centerx, self.rect.centery), self.size // 2)


class Bomb:
    def __init__(self, speed_multiplier=1.0):
        self.size = BOMB_SIZE
        self.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.y = -self.size
        self.speed = random.randint(INITIAL_BOMB_SPEED_MIN, INITIAL_BOMB_SPEED_MAX) * speed_multiplier
        
        # 전역 폭탄 이미지 및 마스크 설정
        self.image = BOMB_IMG
        self.mask = BOMB_MASK

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def fall(self):
        self.y += self.speed
        self.rect.y = int(self.y)

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (self.x, int(self.y)))
        else:
            # 폭탄 느낌이 나게 어두운 원형 그리기
            pygame.draw.circle(surface, COLOR_BOMB_FALLBACK, (self.rect.centerx, self.rect.centery), self.size // 2)
            # 폭탄 꼭지점(심지) 디테일 추가
            pygame.draw.rect(surface, (20, 20, 20), (self.rect.centerx - 5, self.rect.y - 5, 10, 10))


# ==========================================
# 4. 메인 게임 루프 함수
# ==========================================
def main(current_affection=0):
    player = Player()
    items = []  # 화면에 떠있는 츄파츕스들을 담을 리스트
    bombs = []  # 화면에 떠있는 폭탄들을 담을 리스트
    particles = [] # 파티클을 담을 리스트
    floating_texts = [] # 플로팅 텍스트 리스트
    bokeh_particles = [BokehParticle() for _ in range(30)] # 배경 보케 입자 리스트
    rain_particles = [RainParticle() for _ in range(100)] # 비 입자 리스트 (C, F 등급용)
    
    score = 0
    life = MAX_LIFE
    frame_count = 0 # 시간을 재기 위한 프레임 카운트
    remaining_time = MAX_GAME_TIME # 초기 남은 시간
    
    # 정산 및 호감도 시스템을 위한 변수
    post_game_started = False
    target_affection = current_affection
    animating_affection = float(current_affection)
    grade_info = None
    post_game_timer = 0
    
    # 난이도 관리를 위한 변수
    difficulty_level = 1
    current_item_spawn_rate = INITIAL_ITEM_SPAWN_RATE
    current_bomb_spawn_rate = INITIAL_BOMB_SPAWN_RATE
    speed_multiplier = 1.0 # 속도 증가 배율

    game_over = False
    running = True

    while running:
        clock.tick(FPS) # 설정한 FPS(60)에 맞춰 게임 속도를 일정하게 유지
        frame_count += 1

        # --- 1. 이벤트 처리 (키보드 클릭, 창 닫기 등) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 창의 'X' 버튼을 눌렀을 때
                running = False
            
            if event.type == pygame.KEYDOWN:
                # 게임 오버 (정산) 상태일 때 'Enter' 키를 누르면 게임 종료 및 호감도 반환
                if event.key == pygame.K_RETURN and game_over:
                    running = False

        # --- 2. 플레이어 조작 처리 (방향키 꾹 누르고 있을 때 부드러운 이동) ---
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-player.speed) # 왼쪽으로 이동
            if keys[pygame.K_RIGHT]:
                player.move(player.speed)  # 오른쪽으로 이동

            # --- 3. 게임 로직 업데이트 (난이도, 생성, 충돌 판정) ---
            
            # 남은 시간 계산
            remaining_time = MAX_GAME_TIME - (frame_count // FPS)
            if remaining_time <= 0:
                remaining_time = 0
                game_over = True

            # 난이도 조절 로직: 점수가 일정 구간(DIFFICULTY_INCREASE_INTERVAL)을 넘을 때마다 레벨 업
            new_difficulty = 1 + (score // DIFFICULTY_INCREASE_INTERVAL)
            if new_difficulty > difficulty_level:
                difficulty_level = new_difficulty
                speed_multiplier += 0.1 # 아이템이 떨어지는 속도가 10%씩 증가
                
                # 아이템/폭탄 생성 주기 감소 (더 자주 떨어짐). 단, 너무 빨리 떨어지는 것을 방지하기 위해 하한선 설정
                current_item_spawn_rate = max(15, INITIAL_ITEM_SPAWN_RATE - (difficulty_level * 3))
                current_bomb_spawn_rate = max(20, INITIAL_BOMB_SPAWN_RATE - (difficulty_level * 5))

            # 설정된 주기마다 새로운 츄파츕스와 폭탄 생성
            if frame_count % current_item_spawn_rate == 0:
                items.append(FallingItem(speed_multiplier))
            if frame_count % current_bomb_spawn_rate == 0:
                bombs.append(Bomb(speed_multiplier))

            # 츄파츕스 이동 및 충돌 판정
            for item in items[:]: # 리스트 복사본[:]을 순회하며 안전하게 요소 삭제
                item.fall()
                
                # 츄파츕스를 무사히 받았을 때
                if check_collision(player, item):
                    items.remove(item)
                    earned_score = 30 if hasattr(item, 'is_strawberry') and item.is_strawberry else SCORE_PER_ITEM
                    score += earned_score
                    floating_texts.append(FloatingText(f"+{earned_score}", (255, 105, 180), player.x + player.width//2, player.y))
                    # 파티클 생성
                    for _ in range(random.randint(5, 8)):
                        particles.append(HeartParticle(player.x + player.width//2, player.y + player.height//2))
                
                # 츄파츕스를 놓쳐서 화면 바닥 아래로 떨어졌을 때
                elif item.y > SCREEN_HEIGHT:
                    items.remove(item)

            # 폭탄 이동 및 충돌 판정
            for bomb in bombs[:]:
                bomb.fall()
                
                # 폭탄을 맞았을 때 (감점 및 라이프 감소)
                if check_collision(player, bomb):
                    bombs.remove(bomb)
                    score -= SCORE_PENALTY_BOMB
                    if score < 0: 
                        score = 0 # 점수가 마이너스가 되지 않게 처리 (원하지 않으시면 이 줄을 지우세요)
                    floating_texts.append(FloatingText(f"-{SCORE_PENALTY_BOMB}", (255, 0, 0), player.x + player.width//2, player.y))
                    life -= 1
                    if life <= 0:
                        game_over = True # 라이프가 0이 되면 게임 오버
                
                # 폭탄이 바닥으로 떨어졌을 때 (패널티 없이 그냥 사라짐)
                elif bomb.y > SCREEN_HEIGHT:
                    bombs.remove(bomb)

        # --- 4. 화면 그리기 ---
        if BG_IMG:
            screen.blit(BG_IMG, (0, 0)) # 배경 이미지 그리기
        else:
            screen.fill(COLOR_BG) # 배경 이미지 없으면 배경색 채우기
            
        # 보케(Bokeh) 입자 배경 업데이트 및 그리기
        for b in bokeh_particles:
            b.update()
            b.draw(screen)

        # 게임 오버 전환 시 잔상 유지를 위해 일정 시간(50프레임) 동안 오브젝트 렌더링 유지
        if not game_over or post_game_timer < 50:
            player.draw(screen)
            for item in items:
                item.draw(screen)
            for bomb in bombs:
                bomb.draw(screen)

            # 파티클 업데이트 및 그리기
            for p in particles[:]:
                p.update()
                if p.lifetime <= 0:
                    particles.remove(p)
                else:
                    p.draw(screen)
                    
            # 플로팅 텍스트 업데이트 및 그리기
            for ft in floating_texts[:]:
                ft.update()
                if ft.lifetime <= 0:
                    floating_texts.remove(ft)
                else:
                    ft.draw(screen)

        if not game_over:
            # 시간 부족 붉은 펄스 (비네팅) 효과
            if remaining_time <= 10:
                pulse_alpha = int((math.sin(pygame.time.get_ticks() / 150.0) + 1) * 20) # 0 ~ 40 alpha
                pulse_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                pygame.draw.rect(pulse_surf, (255, 0, 0, pulse_alpha), pulse_surf.get_rect(), width=60)
                screen.blit(pulse_surf, (0, 0))

            # 상단 가로 바 형태의 글래스모피즘 HUD
            hud_width = SCREEN_WIDTH
            hud_height = 80
            hud_surf = pygame.Surface((hud_width, hud_height), pygame.SRCALPHA)
            pygame.draw.rect(hud_surf, (0, 0, 0, 150), hud_surf.get_rect()) # 반투명 블랙 바
            screen.blit(hud_surf, (0, 0))
            
            # 왼쪽: 레벨 & 점수
            info_text = font.render(f"Lv.{difficulty_level}  |  SCORE: {score}", True, (255, 255, 255))
            screen.blit(info_text, (30, 20))
            
            # 시간 텍스트 설정
            time_color = (255, 20, 147)
            shake_x, shake_y = 0, 0
            if remaining_time <= 10:
                time_color = (255, 0, 0) # 10초 이하일 때 빨간색으로 변경
                shake_x = random.randint(-5, 5)
                shake_y = random.randint(-5, 5)
                
            time_text = font.render(f"남은 시간: {remaining_time}초", True, time_color)
            
            # 시간 텍스트 중앙 출력
            time_x = SCREEN_WIDTH // 2 - time_text.get_width() // 2 + 20
            time_y = 20
            screen.blit(time_text, (time_x + shake_x, time_y + shake_y))
            
            if CLOCK_IMG:
                clock_x = time_x - CLOCK_IMG.get_width() - 10 + shake_x
                clock_y = time_y - 5 + shake_y
                screen.blit(CLOCK_IMG, (clock_x, clock_y))
                
            # 오른쪽: 라이프
            life_label = font.render("LIFE:", True, (255, 255, 255))
            life_hearts = font.render("♥" * life, True, (255, 105, 180))
            screen.blit(life_label, (SCREEN_WIDTH - 250, 20))
            screen.blit(life_hearts, (SCREEN_WIDTH - 150, 20))
            
        else:
            # 게임 오버 (정산) 상태
            if not post_game_started:
                # 등급 계산 (위에서부터 조건 확인)
                grade_info = GRADE_THRESHOLDS[-1] # 기본 F
                for g in GRADE_THRESHOLDS:
                    if score >= g['min_score']:
                        grade_info = g
                        break
                
                target_affection = current_affection + grade_info['reward']
                target_affection = min(max(target_affection, 0), MAX_AFFECTION) # 0 ~ 100 범위 제한
                post_game_started = True
                post_game_timer = 0
                
            post_game_timer += 1

            # 애니메이션 업데이트
            if animating_affection < target_affection:
                animating_affection += 0.5
                if animating_affection > target_affection: animating_affection = target_affection
            elif animating_affection > target_affection:
                animating_affection -= 0.5
                if animating_affection < target_affection: animating_affection = target_affection
            
            # 1. 2단계 페이드 아웃/인 및 등급별 새로운 배경 렌더링
            if post_game_timer <= 50:
                # Phase 1: 기존 게임 화면 위로 까맣게 페이드 아웃 (0~50 프레임)
                bg_alpha = min(post_game_timer * 5, 255)
                fade_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                fade_surf.fill((15, 15, 15, bg_alpha))
                screen.blit(fade_surf, (0, 0))
            else:
                # Phase 2: 등급별 배경 그리기 후 까만 장막이 걷힘 (페이드 인)
                if grade_info['grade'] in ['S', 'A']:
                    if BG_IMG: screen.blit(BG_IMG, (0, 0))
                    else: screen.fill(COLOR_BG)
                    # 활기차고 영광스러운 따뜻한 오버레이
                    warm_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                    warm_surf.fill((255, 180, 100, 80))
                    screen.blit(warm_surf, (0, 0))
                    for b in bokeh_particles:
                        b.update()
                        b.draw(screen)
                        
                elif grade_info['grade'] == 'B':
                    if BG_IMG: screen.blit(BG_IMG, (0, 0))
                    else: screen.fill(COLOR_BG)
                    
                else: # C, F
                    if BG_IMG: screen.blit(BG_IMG, (0, 0))
                    else: screen.fill(COLOR_BG)
                    # 차갑고 우울한 오버레이
                    gloomy_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                    gloomy_surf.fill((20, 30, 50, 180))
                    screen.blit(gloomy_surf, (0, 0))
                    # 우울하게 비 내리는 연출
                    for r in rain_particles:
                        r.update()
                        r.draw(screen)

                # 까만 장막 걷히기 (255 -> 0)
                bg_alpha = max(0, 255 - (post_game_timer - 50) * 5)
                if bg_alpha > 0:
                    fade_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                    fade_surf.fill((15, 15, 15, bg_alpha))
                    screen.blit(fade_surf, (0, 0))

            # 타이머 50 (암전 완료 지점) 이후부터 정산창 UI 슬라이드 업 표시
            if post_game_timer >= 50:
                slide_offset = max(0, 100 - (post_game_timer - 50) * 5) # 아래에서 위로 올라오는 오프셋
                
                # 2. 결과 및 랭크 텍스트 (위쪽, 넓은 간격)
                title_text = large_font.render("결과 정산", True, (255, 255, 255))
                score_text = font.render(f"최종 점수: {score}점", True, (220, 220, 220))
                grade_text = large_font.render(f"랭크: {grade_info['grade']}", True, grade_info['color'])
                
                screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100 + slide_offset))
                screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 200 + slide_offset))
                screen.blit(grade_text, (SCREEN_WIDTH//2 - grade_text.get_width()//2, 300 + slide_offset))
                
                # 3. 수직 호감도 게이지 (온도계 스타일)
                gauge_width = 24
                gauge_height = 300
                gauge_x = SCREEN_WIDTH // 2 - gauge_width // 2
                gauge_y = 400 + slide_offset
                
                # 배경 게이지 (어두운 회색)
                pygame.draw.rect(screen, (60, 60, 60), (gauge_x, gauge_y, gauge_width, gauge_height), border_radius=12)
                
                # 채워진 게이지 (핑크색, 아래에서 위로)
                fill_height = int(gauge_height * (animating_affection / MAX_AFFECTION))
                if fill_height > 0:
                    pygame.draw.rect(screen, (255, 182, 193), (gauge_x, gauge_y + gauge_height - fill_height, gauge_width, fill_height), border_radius=12)
                
                # 게이지 하단 동그란 프로필 원 표시
                circle_y = gauge_y + gauge_height
                pygame.draw.circle(screen, (255, 182, 193), (SCREEN_WIDTH // 2, circle_y), 40)
                
                # 원 테두리 반투명 효과 (사진 참고)
                circle_border = pygame.Surface((100, 100), pygame.SRCALPHA)
                pygame.draw.circle(circle_border, (255, 182, 193, 80), (50, 50), 50)
                screen.blit(circle_border, (SCREEN_WIDTH // 2 - 50, circle_y - 50))
                
                # 캐릭터 이름 (하얀색)
                name_text = font.render("호감도", True, (255, 255, 255))
                screen.blit(name_text, (SCREEN_WIDTH//2 - name_text.get_width()//2, circle_y + 60))
                
                # 호감도 증감 수치 (핑크색)
                sign = "+" if grade_info['reward'] >= 0 else ""
                delta_text = large_font.render(f"{sign}{grade_info['reward']}", True, (255, 20, 147))
                screen.blit(delta_text, (SCREEN_WIDTH//2 - delta_text.get_width()//2, circle_y + 100))
                
                # 달성 메시지
                if int(animating_affection) >= 100:
                    msg_text = font.render("💖 호감도 100% 달성! 공략 완료! 💖", True, (255, 182, 193))
                    screen.blit(msg_text, (SCREEN_WIDTH//2 - msg_text.get_width()//2, circle_y + 180))
                elif int(animating_affection) >= 50:
                    msg_text = font.render("✨ 호감도 50% 돌파! 특별 이벤트 개방! ✨", True, (255, 182, 193))
                    screen.blit(msg_text, (SCREEN_WIDTH//2 - msg_text.get_width()//2, circle_y + 180))
                    
                # 4. 버튼 스타일 '계속하기' (사진의 핑크 버튼 벤치마킹)
                btn_width = 450
                btn_height = 80
                btn_x = SCREEN_WIDTH // 2 - btn_width // 2
                btn_y = SCREEN_HEIGHT - 150 + slide_offset
                
                # 핑크색 배경
                pygame.draw.rect(screen, (255, 182, 193), (btn_x, btn_y, btn_width, btn_height), border_radius=40)
                # 흰색 얇은 테두리
                pygame.draw.rect(screen, (255, 255, 255), (btn_x, btn_y, btn_width, btn_height), width=2, border_radius=40)
                
                # 버튼 안의 텍스트
                exit_text = font.render("엔터(Enter)로 계속하기", True, (40, 40, 40))
                screen.blit(exit_text, (btn_x + btn_width//2 - exit_text.get_width()//2, btn_y + btn_height//2 - exit_text.get_height()//2))

        pygame.display.flip() # 완성된 화면을 모니터에 업데이트

    # 루프를 빠져나오면(창을 닫거나 엔터 입력 시) Pygame 종료
    pygame.quit()
    return grade_info['reward'] if post_game_started else 0 # 획득한 호감도 증감량(delta) 반환

# 이 스크립트가 직접 실행될 때만 메인 함수 호출
if __name__ == "__main__":
    delta = main(current_affection=40) # 테스트용 초기 호감도 40
    print(f"획득한 호감도 증감량: {delta}")
    import sys
    sys.exit()
