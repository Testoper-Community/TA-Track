from datetime import date, datetime
from robot.api.deco import keyword, library


def gettimenow():
    tm = str(datetime.now())
    return tm
