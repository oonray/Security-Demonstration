import sqlite3

db = None

def open(db):
    db = sqlite3.connect("Attack_module/Database/Player/DB.db")


def updateTimeint(self, time):
    try:
        updatePlayerint("timeUser", time, self.name)
    except:
        print("[PLAYER ERROR] could not add player time")


def updateTimestr(self, time):
    try:
        updatePlayerstr("timeRoot", time, self.name)
    except:
        print("[PLAYER ERROR] could not add player time")

def createTable():
    try:
        """Generates the tables unless they are allreaddy created"""
        print("[SQL] Creating Tables")
        cursor = db.getCursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS "users" (
                                    `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
                                    `name`	TEXT,
                                    `phone`	INTEGER,
                                    `email`	TEXT,
                                    `timeWeb`	INTEGER,
                                    `timeUser`	INTEGER,
                                    `timeRoot`	TEXT,
                                    `points`	INTEGER
                                )''')
        db.commit()
        cursor.close()
    except db.Error as er:
        print("[SQL ERROR] " + er.message)

def connect(db):
    try:
        db.close()
    except:
        pass
    open(db)


def getCursor(db):
    connect(db)
    return db.cursor()


def addPlayerToDb(db, self, player):
    """adds a SPECIFIED PLAYERS NAME phone number and emil to database"""
    try:
        print("[SQL] inserting " + player.name)
        string = 'INSERT INTO users(name,phone,email,points,timeRoot,timeUser) VALUES("{}",{},"{}",{},"{}",{})'.format(
            player.name, player.phone, player.email, 0, 0, 0)
        cursor = getCursor()
        cursor.execute(string)
        cursor.execute('select id from users where name = "{}"'.format(player.name))
        player.id = cursor.fetchall()
        self.db.commit()
        cursor.close()
    except db.Error as er:
        print("[SQL ERROR] " + er.message)


def updatePlayerstr(db, table, value, user):
    """updates a value in the database usually this is points"""
    try:
        cursor = db.getCursor()
        stri = 'update users set {}="{}" where name = "{}"'.format(table, value, user)
        cursor.execute(stri)
        db.commit()
        cursor.close()
    except db.Error as er:
        print("[SQL ERROR] " + er.message)


def updatePlayerint(db, table, value, user):
    """updates a value in the database usually this is points"""
    try:
        cursor = db.getCursor()
        stri = 'update users set {}={} where name = "{}"'.format(table, value, user)
        cursor.execute(stri)
        db.commit()
        cursor.close()
    except db.Error as er:
        print("[SQL ERROR] " + er.message)


def GetTopPlayers(db):
    """gets the top n players in the databse based on time"""
    selectStatement = """SELECT name,timeRoot,points,timeUser from users WHERE points >= 50 ORDER BY timeUser ASC, points DESC LIMIT 5"""
    c = db.getCursor()
    c.execute(selectStatement)
    response = c.fetchall()
    c.close()
    return response