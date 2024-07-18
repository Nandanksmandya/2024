class Bird:

    def intro(self):
        print("there are so many types Birds...")

    def flight(self):
        print("most of the birds can fly but some can not.")


class Sparrow(Bird):

    def flight(self):
        print("Sparrow can fly..!")


class Ostrich(Bird):
    def flight(self):
        print("Ostrich can not fly..!")


obj_bird = Bird()
obj_spar = Sparrow()
obj_ostri = Ostrich()

obj_bird.flight()
obj_bird.intro()

obj_spar.intro()
obj_spar.flight()

obj_ostri.intro()
obj_ostri.flight()
