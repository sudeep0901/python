import cv2
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
print(kivy.__version__)


class MyGrid(GridLayout):

    def show_webcam(mirror=False):
        cap = cv2.VideoCapture(0)
        if not (cam.isOpened()): 
            print("Could not open video device")
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
        
        while(True):
            # Capture frame-by-frame
            et, frame = cap.read()
        
            # Display the resulting frame
        
            cv2.imshow('preview',frame)
        
            #Waits for a user input to quit the application
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cap.release()
            cv2.destroyAllWindows()
        
        
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Button(text="Start Camera"))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Button(text="Stop Camera"))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Start Camera", font_size=40)
        self.submit.bind(on_press=self.show_webcam)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()