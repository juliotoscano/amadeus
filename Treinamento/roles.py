from rolepermissions.roles import AbstractUserRole

class Teacher(AbstractUserRole):
    available_permissions = {
        'create_module':True,
        'create_course':True,
        'create_category':False,
        'create_teacher':False
    }

class Student(AbstractUserRole):
    available_permissions = {
        'create_module':False,
        'create_course':False,
        'create_category':False,
        'create_teacher':False
    }

class SystemAdmin(AbstractUserRole):

    pass



