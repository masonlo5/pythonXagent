######################匯入模組######################
import pygame
import sys
######################初始化######################
pygame.init() # 啟動pygame
clock = pygame.time.Clock() # create a clock object to manage the frame rate
width = 640 # create a width variable
height = 320 # create a height variable
######################建立視窗及物件######################
# create window's size
screen = pygame.display.set_mode((width, height))
# create window's title
pygame.display.set_caption("My Game")
######################建立畫布######################
# create a canvas
bg = pygame.Surface((width, height))
bg.fill((255, 255, 255)) # fill the canvas with white color
# store background color for eraser behavior
BG_COLOR = (255, 255, 255)
draw_color = (0, 0, 0)  # default drawing color (black)
drawing = False         # whether the user is currently drawing
draw_button = None      # which mouse button started the drawing (1=left,3=right)
brush_radius = 8        # radius of the brush/eraser
prev_pos = None         # previous mouse position (for smoothing)
######################繪製圖形######################

# 在 bg 畫布上繪製基本幾何圖形（不使用 math，使用固定常數）
# 以下每一行都保留原本的繪製行為，只是補上更詳細的註解，說明參數含義與用途。

# ------------------ 範例與參數說明 ------------------
# 常見 draw 函式簽名（簡化）:
#   pygame.draw.rect(surface, color, rect, width=0, border_radius=0)
#     - surface: 要在其上繪製的 Surface（這裡是 bg）
#     - color: RGB 顏色元組 (R, G, B)
#     - rect: 四元組或 Rect，格式為 (x, y, width, height)
#     - width: 線寬，預設 0 表示填滿；非 0 則為輪廓線的寬度
#     - border_radius: 整數，指定圓角半徑（選用參數）
#
#   pygame.draw.circle(surface, color, center, radius, width=0)
#     - center: 中心座標 (x, y)
#     - radius: 半徑（像素）
#     - width: 線寬，0 為實心
#
#   pygame.draw.ellipse(surface, color, rect, width=0)
#     - rect: 橢圓所佔的矩形範圍 (x, y, w, h)
#
#   pygame.draw.line(surface, color, start_pos, end_pos, width=1)
#   pygame.draw.aaline(surface, color, start_pos, end_pos)  # 反鋸齒線（非同步寬度參數）
#
#   pygame.draw.polygon(surface, color, pointlist, width=0)
#     - pointlist: [(x1,y1), (x2,y2), ...] 順序決定多邊形邊界
#
#   pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1)
#     - 角度以弧度表示；rect 指定圓弧所在的矩形區域
# ----------------------------------------------------

# 填充矩形 (實心)
# 參數說明: bg=畫布, color=(200,50,50) 為紅色系, rect=(20,20,120,60) -> 左上角 (20,20), 寬120 高60
pygame.draw.rect(bg, (200, 50, 50), (20, 20, 120, 60))

# 矩形輪廓
# 最後一個參數 4 表示線寬為 4px（非 0 表示只畫輪廓）
pygame.draw.rect(bg, (0, 0, 0), (160, 20, 120, 60), 4)

# 圓角矩形（使用 border_radius 產生圓角）
# border_radius=12 將四角圓滑化；若省略則為直角矩形
pygame.draw.rect(bg, (50, 150, 200), (300, 20, 120, 60), border_radius=12)

# 實心圓
# center=(80,140), radius=40 -> 在 (80,140) 畫一個半徑 40 的實心圓
pygame.draw.circle(bg, (50, 200, 100), (80, 140), 40)

# 圓形輪廓
# width=5 表示只畫輪廓，寬度為 5px
pygame.draw.circle(bg, (0, 0, 0), (320, 140), 40, 5)

# 橢圓
# rect=(420,20,180,80) 指定橢圓的外接矩形 (x, y, w, h)
pygame.draw.ellipse(bg, (150, 80, 200), (420, 20, 180, 80))

# 直線
# line(surface, color, start_pos, end_pos, width)
pygame.draw.line(bg, (0, 0, 0), (20, 220), (620, 220), 3)

# 抗鋸齒線 (aaline) - 視覺上比普通 line 平滑，但無 width 參數
pygame.draw.aaline(bg, (100, 100, 100), (20, 240), (620, 260))

# 三角形（多邊形）
# pointlist 為三個頂點座標，會自動閉合成多邊形
pygame.draw.polygon(bg, (255, 180, 50), [(160, 120), (200, 60), (240, 120)])

# 五邊形（多邊形）
pygame.draw.polygon(bg, (120, 180, 60), [(360, 120), (340, 80), (380, 60), (420, 80), (400, 120)])

# 弧線（半圓樣式）
# arc(surface, color, rect, start_angle, stop_angle, width)
# 這裡的角度以弧度為單位，0 到 3.14 (約 pi) 會畫出半圓狀弧線
pygame.draw.arc(bg, (0, 120, 180), (20, 260, 120, 80), 0, 3.14, 3)

# 小矩形輪廓 (線寬 2)
pygame.draw.rect(bg, (0, 0, 0), (160, 260, 60, 40), 2)

# 小圓 (實心)
pygame.draw.circle(bg, (180, 0, 180), (260, 290), 20)

######################循環偵測######################
while True:
    clock.tick(60)  # limit the frame rate to 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicked [x] button
            sys.exit() # quit the game

        # check for mouse button events to control drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in (1, 3):  # Left (1) or Right (3) mouse button starts drawing
                drawing = True
                draw_button = event.button
                prev_pos = event.pos
                # choose color based on which mouse button started the drawing
                # right button (3) acts as eraser -> use background color
                color_to_use = BG_COLOR if draw_button == 3 else draw_color
                pygame.draw.circle(bg, color_to_use, event.pos, brush_radius)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button in (1, 3):
                drawing = False
                draw_button = None
                prev_pos = None
        if event.type == pygame.MOUSEMOTION:
            # when moving while a drawing button is pressed, draw
            if drawing and draw_button in (1, 3):
                curr_pos = event.pos
                # choose color based on which mouse button is drawing
                # right button -> eraser (background color); left button -> current draw_color
                color_to_use = BG_COLOR if draw_button == 3 else draw_color
                # draw a circle at current position
                pygame.draw.circle(bg, color_to_use, curr_pos, brush_radius)
                # draw a line between previous and current to fill gaps
                if prev_pos is not None:
                    pygame.draw.line(bg, color_to_use, prev_pos, curr_pos, brush_radius * 2)
                prev_pos = curr_pos
        # keyboard: press 'c' to toggle between drawing color and background (eraser)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                # toggle between black and background color
                if draw_color == (0, 0, 0):
                    draw_color = BG_COLOR
                else:
                    draw_color = (0, 0, 0)

    # canvas will be drawn on the window at left top corner 
    screen.blit(bg, (0, 0))
    # update the window
    pygame.display.update()