class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, newname):
        self.name = newname
        print("My name is: ", self.name)

    def change_age(self, newage):
        self.age = newage
        print("My age is: ", self.age)

    def add_tracks(self, newname):
        self.tracks.append(self.tracks)
        print("I am on the tracks: ", self.tracks)

    def get_score(self):
        print("I got the score: ", self.score)
        pass



Bob = Student(name="Peter", age=19, tracks=["FE","BE", "UI/UX"],score=20.90)
#print(Bob.name)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("UI/UX")
Bob.get_score()
