

class Garden:
    def __init__(self, diagram, students=None):
        self.garden = diagram.splitlines()
        self.plant_names = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }
        self.students = [
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Eve",
                "Fred",
                "Ginny",
                "Harriet",
                "Ileana",
                "Joseph",
                "Kincaid",
                "Larry"] if students is None else sorted(students)

    def plants(self,student):
        student_slot = self.students.index(student)*2
        return [
            self.plant_names[garden_row[plant_column]] for garden_row in self.garden for plant_column in (student_slot,student_slot+1)]
        
        return(plants())
        print(plants("Alice"))
        print(plants("Ginny"))
        print(plants("Joseph"))