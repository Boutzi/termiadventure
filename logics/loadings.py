import time
import sys
from tqdm.auto import tqdm

class Loadings:
    def __init__(self):
        self.frames = ['◐', '◓', '◑', '◒']
        self.current_frame = 0

    def animate(self):
        while True:
            # Afficher le frame courant et le faire tourner
            sys.stdout.write('\r' + self.frames[self.current_frame])
            sys.stdout.flush()
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            time.sleep(0.1)

    def loadingBar(self, data):
        #loop = tqdm(total=10000, position=1, leave=False)
        for k in tqdm(range(data)):
            print(" ", end="\r")
            #loop.set_description("Loading...".format(k))
            #loop.update(1)
        #loop.close()
        time.sleep(0.8)

    def loadingCircle(self):
        loading_object = "|"
        while loading_object == "|":
            loading_object = "/"
            time.sleep(0.1)
            print("\r" + loading_object, end="")
            loading_object = "-"
            time.sleep(0.1)
            print("\r" + loading_object, end="")    
            loading_object = "\\"
            time.sleep(0.1)
            print("\r" + loading_object, end="")
            loading_object = "|"
