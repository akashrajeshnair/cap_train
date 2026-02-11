class Student:
    def __init__(self, sid, deptid):
        self.sid = sid
        self.deptid = deptid

    def get_info(self):
        return f"Student ID: {self.sid}, Department ID: {self.deptid}"
    
class Faculty:
    def __init__(self, eid, deptid):
        self.eid = eid
        self.deptid = deptid

    def get_info(self):
        return f"Employee ID: {self.eid}, Department ID: {self.deptid}"
    
class PHDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        Student().__init__(sid, deptid)
        Faculty().__init__(eid, deptid)

    def get_info(self):
        return f"Student ID: {self.sid}, Employee ID: {self.eid}, Department ID: {self.deptid}"
    
p = PHDStudent(101, 555, 42)
print(p.get_info())
    