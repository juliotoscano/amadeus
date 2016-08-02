from rolepermissions.roles import AbstractUserRole

class Teacher(AbstractUserRole):
    available_permissions = {
        'create_module':True,
        'create_course':True
    }

class Student(AbstractUserRole):
    available_permissions = {
        'look_module':True,
        'look_course':True
    }


