import mysql.connector

from config import DB_HOST, DB_USER, DB_PASS, DB_NAME
from models import Parafia, Pogrzeb, Intencja, UserInDB

class Database:
    def __init__(self, database: mysql.connector.MySQLConnection | None = None) -> None:
        if database is None:
            self.mydb = mysql.connector.connect(
                host = DB_HOST,
                user = DB_USER,
                password = DB_PASS,
                database = DB_NAME
            )
        else:
            self.mydb = database

        self.mydb.autocommit = True
        self.mycursor = self.mydb.cursor()

class ParafieDB(Database):
    def get_all(self) -> list[Parafia]:
        self.mycursor.execute("SELECT id,nazwa FROM Parafie")
        db_output = self.mycursor.fetchall()
        output = []
        for parafia in db_output:
            output.append(Parafia(id=parafia[0],nazwa=parafia[1]))
        return output
    
    def add(self, name: str):
        self.mycursor.execute("INSERT INTO Parafie (nazwa) VALUES (%s)", (name,))

    def remove(self, id: int):
        self.mycursor.execute("DELETE FROM Parafie WHERE id = %s", (id,))

    def getById(self, id: int):
        if self.contains_id(id=id):
            self.mycursor.execute("SELECT id,nazwa FROM Parafie WHERE id = %s", (id,))
            res = self.mycursor.fetchone()
            return Parafia(id=res[0],nazwa=res[1])
        else:
            None
    def contains_id(self, id: int):
        self.mycursor.execute("SELECT * FROM Parafie WHERE id = %s", (id,))
        return self.mycursor.fetchone() is not None

class PogrzebyDB(Database):
    def get_all(self) -> list[Pogrzeb]:
        self.mycursor.execute("SELECT id,imię,nazwisko,data,data_mszy,parafia_id FROM Pogrzeby")
        db_output = self.mycursor.fetchall()
        output = []
        for row in db_output:
            output.append(Pogrzeb(
                    id=row[0],
                    imie=row[1],
                    nazwisko=row[2],
                    date=row[3],
                    date_mszy=row[4],
                    parafia_id=row[5]
                )
            )
        return output
    
    def getById(self, id: int) -> Pogrzeb:
        if self.contains_id(id=id):
            self.mycursor.execute("SELECT id,imię,nazwisko,data,data_mszy,parafia_id FROM Pogrzeby WHERE id = %s", (id,))
            row = self.mycursor.fetchone()
            return Pogrzeb(
                    id=row[0],
                    imie=row[1],
                    nazwisko=row[2],
                    date=row[3],
                    date_mszy=row[4],
                    parafia_id=row[5]
                )
        else:
            None

    def contains_id(self, id: int):
        self.mycursor.execute("SELECT * FROM Pogrzeby WHERE id = %s", (id,))
        return self.mycursor.fetchone() is not None
    
    def add(self, data: Pogrzeb):
        parafiaDB = ParafieDB()
        if parafiaDB.contains_id(data.parafia_id):
            self.mycursor.execute("INSERT INTO Pogrzeby (imię,nazwisko,data,data_mszy,parafia_id) VALUES (%s,%s,%s,%s,%s)", (data.imie,data.nazwisko,data.date,data.date_mszy,data.parafia_id))

    def update(self, data: Pogrzeb):
        if self.contains_id(data.id):
            self.mycursor.execute("UPDATE Pogrzeby SET imię = %s, nazwisko = %s, data = %s, data_mszy = %s, parafia_id = %s WHERE id = %s", (data.imie,data.nazwisko,data.date,data.date_mszy,data.parafia_id,data.id))
    
    def remove(self, id: int):
        self.mycursor.execute("DELETE FROM Pogrzeby WHERE id = %s", (id,))

    def contains_id(self, id: int):
        self.mycursor.execute("SELECT * FROM Pogrzeby WHERE id = %s", (id,))
        return self.mycursor.fetchone() is not None

class IntencjeDB(Database):
    def get_all(self) -> list[Intencja]:
        self.mycursor.execute("SELECT id,od_kogo,kwota,id_pogrzebu FROM Intencje")
        db_output = self.mycursor.fetchall()
        output = []
        for intencja in db_output:
            output.append(Intencja(id=intencja[0],
                                   od_kogo=intencja[1],
                                   kwota=intencja[2],
                                   id_pogrzebu=intencja[3]))
        return output
    
    def get_for(self, id: int) -> list[Intencja]:
        self.mycursor.execute("SELECT id,od_kogo,kwota,id_pogrzebu FROM Intencje WHERE id_pogrzebu = %s", (id,))
        db_output = self.mycursor.fetchall()
        output = []
        for intencja in db_output:
            output.append(Intencja(id=intencja[0],
                                   od_kogo=intencja[1],
                                   kwota=intencja[2],
                                   id_pogrzebu=intencja[3]))
        return output
    
    def add(self, data: Intencja):
        pogrzebyDB = PogrzebyDB()
        if pogrzebyDB.contains_id(data.id_pogrzebu):
            self.mycursor.execute("INSERT INTO Intencje (od_kogo, kwota, id_pogrzebu) VALUES (%s,%s,%s)", (data.od_kogo,data.kwota,data.id_pogrzebu))

    def remove(self, id: int):
        self.mycursor.execute("DELETE FROM Intencje WHERE id = %s", (id,))

    def contains_id(self, id: int):
        self.mycursor.execute("SELECT * FROM Intencje WHERE id = %s", (id,))
        return self.mycursor.fetchone() is not None

class UsersDB(Database):
    def get_all(self) -> list[UserInDB]:
        self.mycursor.execute("SELECT username,password FROM Users")
        db_output = self.mycursor.fetchall()
        output = []
        for user in db_output:
            output.append(UserInDB(username=user[0],
                                   hashed_password=user[1]))
        return output
    def add(self, data: UserInDB):
        self.mycursor.execute("INSERT INTO Users (username,password) VALUES (%s,%s)", (data.username,data.hashed_password))
