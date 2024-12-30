from manim import *

class CameraFollowArray(MovingCameraScene):
    def construct(self):
        # Initial array
        array = [1, 2, 3]
        array_mob = VGroup(*[Integer(num) for num in array])
        array_mob.arrange(RIGHT, buff=0.5)
        self.add(array_mob)
        
        # Camera follows the array
        for i in range(4, 11):
            new_num = Integer(i)
            new_num.next_to(array_mob, RIGHT, buff=0.5)
            self.play(FadeIn(new_num))
            array_mob.add(new_num)
            self.play(self.camera.frame.animate.move_to(new_num))
            self.play(self.camera.frame.animate.set(width=array_mob.width / 2))
            self.wait(0.5)
