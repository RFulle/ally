
def findmyboard(yloc, s1loc, s2loc, s3loc,):
       blankboard = '''

                 ______            ______          ______
                |      |          |      |        |      |
                |   1  |----------|   2  |--------|   3  |
                |______|          |______|        |______|
               /        \        /       \        /      \
        ______/          \______/         \______/        \______
       |      |          |      |         |      |        |      |
       |   4  |----------|   5  |---------|  6   |--------|   7  |
       |______|          |______|         |______|        |______|
              \          /       \        /      \        /
               \ ______ /         \______/        \______/
                |      |          |      |        |      |
                |   8  |----------|   9  |--------|  10  |
                |______|          |______|        |______|


       '''
       startbo = '''

                 ______            ______          ______
                |      |          |      |        |      |
                |      |----------|      |--------|  S   |
                |______|          |______|        |______|
               /        \        /       \        /      \
        ______/          \______/         \______/        \______
       |      |          |      |         |      |        |      |
       |  Y   |----------|      |---------|      |--------|   S  |
       |______|          |______|         |______|        |______|
              \          /       \        /      \        /
               \ ______ /         \______/        \______/
                |      |          |      |        |      |
                |      |----------|      |--------|  S   |
                |______|          |______|        |______|


       '''
       #yloc, s1loc, s2loc, s3loc

       if (yloc or s1loc or s2loc or s3loc) == s1:
              print("TEST COMPLETE")
              print(startbo)






















       myboard = '''
                 ______            ______          ______
                |      |          |      |        |      |
                |  {}  |----------|  {}  |--------|  {}  |
                |______|          |______|        |______|
               /        \        /       \        /      \
        ______/          \______/         \______/        \______
       |      |          |      |         |      |        |      |
       |  {}  |----------|  {}  |---------|  {}  |--------|  {}  |
       |______|          |______|         |______|        |______|
              \          /       \        /      \        /
               \ ______ /         \______/        \______/
                |      |          |      |        |      |
                |  {}  |----------|  {}  |--------|  {}  |
                |______|          |______|        |______|


       '''.format()
s1 = True
s1loc = True
s2loc = True
s3loc = True
findmyboard(s1, s1loc, s2loc, s3loc)