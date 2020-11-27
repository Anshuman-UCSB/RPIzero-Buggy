from pynput import keyboard
from time import sleep

class Keyboard():
    
    def __init__(self):
        self.keys = []
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()
        self.live = True
        
    def on_press(self,key):
        try:
            if key == keyboard.Key.esc:
        # Stop listener
                print("Killed keyboard.")
                self.live = False
                return False        
            if key.char not in self.keys:
                self.keys.append(key.char.lower())
                print('alphanumeric key {0} pressed'.format(
                key.char))
                print(self.keys)
        except AttributeError:
            pass
                
    def on_release(self,key):
        try:
            self.keys.remove(key.char.lower())
        except AttributeError:
            pass
        except ValueError:
            print("removed invalid key: {}".format(key))
        print(self.keys)
    
    def isPressed(self, key):
        return key[0].lower() in self.keys
        
            
if __name__=="__main__":
    kb = Keyboard()
    while True:
        print(kb.isPressed('w'))
        sleep(1)