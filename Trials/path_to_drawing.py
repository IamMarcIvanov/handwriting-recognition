import pyautogui as pag

pag.hotkey('alt', 'tab')
with open(r'D:\LibraryOfBabel\Projects\HandwritingRecognition\Trials\path.txt', 'r') as f:
    for line_n, line in enumerate(f.readlines()):
        x, y, = list(map(float, line.strip().split()))
        x, y = int(x), int(y) + 200
        if line_n == 0:
            pag.moveTo(x, y)
        else:
            pag.dragTo(x, y)
pag.hotkey('alt', 'tab')

# pag.moveTo(500, 400)
# pag.dragTo(500, 600, 1)
# pag.dragTo(1000, 600, 1)
