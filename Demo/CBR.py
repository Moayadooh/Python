import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="root", db="DB_SCHEME"
)
cursor = db.cursor()


def LocalSimilarityContinuous(userBloodPressure, bloodPressure, range):
    sum = 1 - abs((userBloodPressure - bloodPressure)) / range
    return sum


def LocalSimilarityDiscrete(a, b):
    if a == b:
        return 1
    else:
        return 0


def GlobalSimilarity(bloodPressure, Albumin, Sugar, redBloodCell, anemia):
    sum = 0.2 * ((1 * bloodPressure) + (1 * Albumin) + (1 * Sugar) + (1 * redBloodCell) + (1 * anemia))
    return sum


userBloodPressure = 75
userAlbumin = 1
userSugar = 1
userRedBloodCell = "normal"
userAnemia = "no"
'''
userBloodPressure = int(input("Blood Pressure: "))
userAlbumin = int(input("Albumin: "))
userSugar = int(input("Sugar: "))
userRedBloodCell = input("Red Blood Cell: ")
userAnemia = input("Anemia: ")
'''

# Check if the problem is exist 'RETRIEVE'
sql = "select * from cbr where Blood_Pressure = %s and Albumin = %s and Sugar = %s and Red_Blood_Cell = %s and Anaemia = %s"
values = (userBloodPressure, userAlbumin, userSugar, userRedBloodCell, userAnemia)
cursor.execute(sql, values)
data = cursor.fetchone()
if data:
    result = data[6]
    print("Chronic Kidney Disease:", result)  # REUSE
else:
    # REVISE
    cursor.execute("select min(Blood_Pressure) from cbr")
    data = cursor.fetchone()
    minBloodPressure = data[0]
    cursor.execute("select max(Blood_Pressure) from cbr")
    data = cursor.fetchone()
    maxBloodPressure = data[0]
    rangeBloodPressure = maxBloodPressure - minBloodPressure

    cursor.execute("select min(Albumin) from cbr")
    data = cursor.fetchone()
    minAlbumin = data[0]
    cursor.execute("select max(Albumin) from cbr")
    data = cursor.fetchone()
    maxAlbumin = data[0]
    rangeAlbumin = maxAlbumin - minAlbumin

    cursor.execute("select min(Sugar) from cbr")
    data = cursor.fetchone()
    minSugar = data[0]
    cursor.execute("select max(Sugar) from cbr")
    data = cursor.fetchone()
    maxSugar = data[0]
    rangeSugar = maxSugar - minSugar

    cursor.execute("select * from cbr")
    column = cursor.fetchall()
    gsPatientHighest = 0
    for row in column:
        lsBloodPressure = LocalSimilarityContinuous(userBloodPressure, row[1], rangeBloodPressure)
        # print(lsBloodPressure)
        lsAlbumin = LocalSimilarityContinuous(userAlbumin, row[2], rangeAlbumin)
        # print(lsAlbumin)
        lsSugar = LocalSimilarityContinuous(userSugar, row[3], rangeSugar)
        # print(lsSugar)

        lsRedBloodCell = LocalSimilarityDiscrete(userRedBloodCell, row[4])
        # print(lsRedBloodCell)
        lsAnemia = LocalSimilarityDiscrete(userAnemia, row[5])
        # print(lsAnemia)

        gsPatient = GlobalSimilarity(lsBloodPressure, lsAlbumin, lsSugar, lsRedBloodCell, lsAnemia)
        # print("______________________")
        # print(gsPatient, "\n")

        if gsPatient > gsPatientHighest:
            gsPatientHighest = gsPatient
            result = row[6]

    # RETAIN
    sql = "insert into cbr values (%s, %s, %s, %s, %s, %s, %s)"
    values = (None, userBloodPressure, userAlbumin, userSugar, userRedBloodCell, userAnemia, result)
    cursor.execute(sql, values)
    db.commit()

    print("Chronic Kidney Disease:", result)
