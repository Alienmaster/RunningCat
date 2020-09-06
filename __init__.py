from color import Color
import display
import utime
import buttons
import bhi160
import leds
import utime
import interrupt
import vibra


# HCOLORS = {
#     1: Color.from_hex(0x010101),
#     2: Color.from_hex(0xa9a9a9),
#     3: Color.from_hex(0x575757),
#     4: Color.from_hex(0xffbbd3),
# }

# HPIXELS = [
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 2, 3, 1, 1, 1, 1, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
#     [0, 1, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1],
#     [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1],
#     [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 3, 1, 1, 1, 1, 0, 0, 0, 1, 3, 1],
#     [1, 2, 4, 2, 2, 1, 2, 1, 2, 2, 4, 2, 2, 3, 2, 3, 2, 1, 0, 0, 1, 2, 1],
#     [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2, 2, 1, 1, 1, 3, 1],
#     [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0],
#     [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0],
#     [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
#     [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
#     [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
#     [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 0, 0],
#     [0, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 0, 0, 0],
#     [0, 0, 1, 3, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 3, 3, 2, 3, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],   
# ]

HCOLORS = {
    1: Color.from_hex(0x010101),
    2: Color.from_hex(0xa9a9a9),
    3: Color.from_hex(0xffffff),
    4: Color.from_hex(0xde4c8a),
}

HPIXELS = [
    [0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,],
    [0,1,2,1,0,0,0,0,0,0,0,1,2,2,1,0,],
    [0,1,2,2,1,0,0,0,0,0,1,2,2,2,1,0,],
    [0,1,2,2,2,1,1,1,1,1,2,2,2,2,1,0,],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,],
    [1,2,2,2,3,1,2,2,2,2,2,3,1,2,2,1,],
    [1,2,2,2,1,1,2,2,2,1,2,1,1,2,2,1,],
    [1,2,4,4,2,2,2,2,2,2,2,2,2,4,4,1,],
    [1,2,4,4,2,1,2,2,1,2,2,1,2,4,4,1,],
    [0,1,2,2,2,1,1,1,1,1,1,1,2,2,1,0,],
    [0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,],
]

displayWidth = 160
displayHeight = 80
size = 1
catWidth = len(HPIXELS[0]) * size
catHeight = len(HPIXELS) * size
midpointX = int(displayWidth/2) - int(catWidth/2)
midpointY = int(displayHeight/2) - int(catHeight/2)
right = True
samples = []

def bhiData(_samples):
    global samples
    samples = _samples

bhi = bhi160.BHI160Orientation(sample_rate=10, callback=bhiData)

DispPosition = [midpointX,midpointY] # x,y
Orientation = [0,0,0] #x,y,z?
counter = 0
game = True


def scale(size):
    result = []
    for row in HPIXELS:
        cl = []
        for p in row:
            for i in range(size):
                cl.append(p)
        for i in range(size):
            result.append(cl)
    return result

SIZER = scale(size)

def draw_cat(X, Y):
    with display.open() as disp:
        disp.clear()
        for y, row in enumerate(SIZER):
            if (right == True):
                for x, p in enumerate(row):
                    if p:
                        disp.pixel(X+x, Y+y, col=HCOLORS[p])
            else:  
                for x, p in enumerate(row[::-1]):
                    if p:
                        disp.pixel(X+x, Y+y, col=HCOLORS[p])
        disp.update()

def run():
    global right
    i = 0
    while True:
        draw_cat(i, 10)
        if (i == (displayWidth - catWidth)):
           while (i != 0):
               right = False
               draw_cat(i, 0)
               i-= 1
        right = True
        i += 1

def runbutton():
    i = 10

    while True:
        while True:
            pressed = buttons.read(
                buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT
            )
            if pressed != 0:
                break

        while True:

            if pressed & buttons.BOTTOM_LEFT != 0:
                i-=1
                draw_cat(i, 10)
                break
        
            if pressed & buttons.BOTTOM_RIGHT != 0:

                i+=1
                draw_cat(i, 10)
                break

def set_X(shift):
    global DispPosition
    realshift = Orientation[0] + shift
    new_position = DispPosition[0] + realshift
    if (new_position < 0):
        DispPosition[0] = 0
    elif (new_position + catWidth > 159):
        DispPosition[0] = 159 - catWidth
    else:
        DispPosition[0] = new_position

def set_Y(shift):
    global DispPosition
    new_position = DispPosition[1] + shift
    if (new_position < 0):
        DispPosition[1] = 0
    elif (new_position + catHeight > 79):
        DispPosition[1] = 79 - catHeight
    else:
        DispPosition[1] = new_position

def check_Border():
    # Q = [0,0]
    # Q[0] = DispPosition[0]/6 # Berrechnung des X Quadranten
    # Q[1] = DispPosition[1]/6 # Berrechnung des Y Quadranten
    # ColorValues = [[255,186,255], [222,135,255], [164,85,255], [104,29,255], [16,0,202], [0,0,152]]
    # if (Q[0] >= 0 and Q[0] <= 3.34):
    #     leds.prep(14, [])
    if DispPosition[0] > 120:
        leds.prep(12,[255,0,0])
        leds.prep(13,[255,0,0])
    elif DispPosition[0] < 10:
        leds.prep(11,[255,0,0])
        leds.prep(14,[255,0,0])
    else:
        leds.prep(12,[0,0,0])
        leds.prep(13,[0,0,0])

    if DispPosition[1] < 10:
        leds.prep(13,[255,0,0])
        leds.prep(14,[255,0,0])
    elif DispPosition[1] > 60:
        leds.prep(11,[255,0,0])
        leds.prep(12,[255,0,0])
    else:
        leds.prep(12,[0,0,0])
        leds.prep(14,[0,0,0])

    leds.update()

def calibrate():
    global Orientation
    # samples = sensors[sensor]["sensor"].read()
    if len(samples) > 0:
        vibra.vibrate(40)
        sample = samples[0]
        Orientation[2] = sample.z
        Orientation[1] = sample.y
        with display.open() as disp:
            disp.clear()
            disp.print("Calibration successful", posy=20)
            disp.update()
    utime.sleep(1)

def runorientation():
    global right
    global DispPosition
    global Orientation
    global samples
    while True:
        pressed = buttons.read(
                buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT
            )
        
        if pressed & buttons.BOTTOM_LEFT != 0:
            DispPosition[0] = midpointX
            DispPosition[1] = midpointY

        if pressed & buttons.BOTTOM_RIGHT != 0:
            calibrate()
            vibra.vibrate(10)

        if len(samples) > 0:
            Value = [0,0,0]
            sample = samples[0] # take the first sample
            Value[1] = -(Orientation[1]) + sample.y # + (int(counter/10))# y
            Value[2] = -(Orientation[2]) + sample.z # + (int(counter/10))# x
            if Value[2] < -2: # Check if orientation is right and normalize x data
                set_X(int(-Value[2]))
                right = True
            if Value[2] > 2: # Check if orientation is left and normalize x data
                set_X(int(-Value[2]))
                right = False
            if (sample.y < -2) or (sample.y > 2): # normalize y data
                set_Y(int(-Value[1]))

        draw_cat(DispPosition[0], DispPosition[1])
        # check_Border()
        play()

def play():
    global counter
    global game
    global DispPosition
    if ((DispPosition[0] + catWidth) == 159 or (DispPosition[0] == 0) or 
        (DispPosition[1] == 0) or (DispPosition[1] + catHeight == 79)):
        print(counter)
        game = False
        while not game:
            with display.open() as disp:
                disp.clear()
                disp.print("Game Over", fg=[255,0,0], posy=0, posx=20)
                disp.print("Your Score:%s" % str(counter), posy=20, font=2)
                disp.print("<-New Game", posy = 60, font=2)
                disp.update()
            utime.sleep(1)
            if buttons.read(buttons.BOTTOM_LEFT | buttons.BOTTOM_RIGHT) & buttons.BOTTOM_LEFT != 0:
                counter = 0
                game = True
                DispPosition[0] = midpointX
                DispPosition[1] = midpointY 

    else:
        if game:
            counter = counter + 1
        


# def orientation_interrupt():
#     interrupt.set_callback(interrupt.RTC_ALARM, Testing)
#     interrupt.enable_callback(interrupt.RTC_ALARM)
# sensors = [{"sensor": bhi160.BHI160Orientation(sample_rate=10), "name": "Orientation"}]
# orientation_interrupt()
timer = utime.monotonic_ms()
runorientation()
