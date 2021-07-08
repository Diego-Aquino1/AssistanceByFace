from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_student(self, CUI):
        params = {'CUI' : CUI}
        rv = self.mysql_pool.execute("SELECT * from estudiantes where CUI=%(CUI)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'CUI': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Correo': result[3], 'Ciudad': result[4], 'Foto': result[5]}
            data.append(content)
            content = {}
        return data

    def get_students(self):  
        rv = self.mysql_pool.execute("SELECT * from estudiantes")  
        data = []
        content = {}
        for result in rv:
            content = {'CUI': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Correo': result[3], 'Ciudad': result[4]}
            data.append(content)
            content = {}
        return data

    def add_student(self, Apellidos, Nombres, Correo, Ciudad, Foto):    
        params = {
            'Apellidos' : Apellidos,
            'Nombres' : Nombres,
            'Correo' : Correo,
            'Ciudad' : Ciudad,
            'Foto' : Foto,
        } 
        query = """INSERT INTO estudiantes (Apellidos, Nombres, Correo, Ciudad, Foto) 
            values (%(Apellidos)s, %(Nombres)s, %(Correo)s, %(Ciudad)s, %(Foto)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'CUI': cursor.lastrowid, 'Apellidos': Apellidos, 'Nombres': Nombres, 'Correo': Correo, 'Ciudad': Ciudad, 'Foto': Foto}
        return data

    def delete_student(self, CUI):    
        params = {'CUI' : CUI}      
        query = """delete from estudiantes where CUI = %(CUI)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


###################################################


    def get_teacher(self, CUI):    
        params = {'CUI' : CUI}      
        rv = self.mysql_pool.execute("SELECT * from profesores where CUI=%(CUI)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'CUI': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Correo': result[3], 'Ciudad': result[4]}
            data.append(content)
            content = {}
        return data

    def get_teachers(self):  
        rv = self.mysql_pool.execute("SELECT * from profesores")  
        data = []
        content = {}
        for result in rv:
            content = {'CUI': result[0], 'Apellidos': result[1], 'Nombres': result[2], 'Correo': result[3], 'Ciudad': result[4]}
            data.append(content)
            content = {}
        return data

    def add_teacher(self, Apellidos, Nombres, Correo, Ciudad):    
        params = {
            'Apellidos' : Apellidos,
            'Nombres' : Nombres,
            'Correo' : Correo,
            'Ciudad' : Ciudad
        }  
        query = """INSERT INTO profesores (Apellidos, Nombres, Correo, Ciudad) 
            values (%(Apellidos)s, %(Nombres)s, %(Correo)s, %(Ciudad)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'CUI': cursor.lastrowid, 'Apellidos': Apellidos, 'Nombres': Nombres, 'Correo': Correo, 'Ciudad': Ciudad}
        return data

    def delete_teacher(self, CUI):    
        params = {'CUI' : CUI}      
        query = """delete from profesores where CUI = %(CUI)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


###################################################

    def get_assistance_date(self, Fecha): 
        params = {'Fecha' : Fecha} 
        rv = self.mysql_pool.execute("SELECT * from asistencias where Fecha=%(Fecha)s", params) 
        data = []
        content = {}
        for result in rv:
            content = {'ASISTENCIA': result[0], 'Fecha': result[1]}
            data.append(content)
            content = {}
        return data

    def get_assistance_ID(self, ID): 
        params = {'ID' : ID} 
        rv = self.mysql_pool.execute("SELECT * from asistencias where ID=%(ID)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'ASISTENCIA': result[0], 'ID': result[1]}
            data.append(content)
            content = {}
        return data

    def get_assistances(self):  
        rv = self.mysql_pool.execute("SELECT * from asistencias")  
        data = []
        content = {}
        for result in rv:
            content = {'ASISTENCIA': result[0], 'Fecha': result[1], 'Asistencias': result[2], 'Faltas': result[3]}
            data.append(content)
            content = {}
        return data

    def add_assistance(self, ASISTENCIA, Fecha, Asistencias, Faltas):    
        params = {
            'ASISTENCIA' : ASISTENCIA,
            'Fecha' : Fecha,
            'Asistencias' : Asistencias,
            'Faltas' : Faltas
        }  
        query = """INSERT INTO asistencias (ASISTENCIA, Fecha, Asistencias, Faltas)
            values (%(ASISTENCIA)s, %(Fecha)s, %(Asistencias)s, %(Faltas)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True)
        
        data = {'ID': cursor.lastrowid, 'ASISTENCIA': ASISTENCIA, 'Fecha': Fecha, 'Asistencias': Asistencias, 'Faltas': Faltas}
        return data

    def delete_assistance(self, ID):    
        params = {'ID' : ID}      
        query = """delete from asistencias where ID = %(ID)s""" 
        self.mysql_pool.execute(query, params, commit=True) 

        data = {'result': 1}
        return data


##################################################


    def get_courses(self):  
        rv = self.mysql_pool.execute("SELECT * from cursos")  
        data = []
        content = {}
        for result in rv:
            content = {'Curso': result[0]}
            data.append(content)
            content = {}
        return data

    def add_course(self, Nombre):    
        params = {
            'Nombre' : Nombre
        }  
        query = """INSERT INTO cursos (Nombre) 
            values (%(Nombre)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True) 
        cursor.lastrowid

        data = {'Nombre': Nombre}
        return data

    def delete_course(self, Nombre):    
        params = {'Nombre' : Nombre}      
        query = """delete from cursos where Nombre = %(Nombre)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'Delete': 1}
        return data


##################################################


    def get_groups(self):  
        rv = self.mysql_pool.execute("SELECT * from grupos")  
        data = []
        content = {}
        for result in rv:
            content = {'Grupo': result[0]}
            data.append(content)
            content = {}
        return data

    def add_group(self, Grupo):    
        params = {
            'Grupo' : Grupo
        }  
        query = """INSERT INTO grupos (Grupo) 
            values (%(Grupo)s)"""
                
        cursor = self.mysql_pool.execute(query, params, commit=True) 
        cursor.lastrowid

        data = {'Grupo': Grupo}
        return data

    def delete_group(self, Grupo):    
        params = {'Grupo' : Grupo}      
        query = """delete from grupos where Grupo = %(Grupo)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'Delete': 1}
        return data


###################################################


if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(tm.delete_task(67))
    print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))