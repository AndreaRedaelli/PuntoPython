class Punto:
    """Classe Punto"""
    #region attributes
    x = 0;
    y = 0;
    #endregion

    #region costructor
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    #endcostructor

    #region override add +
    def __add__(self, AltroPunto):
        newX = self.x + AltroPunto.x;
        newY = self.y + AltroPunto.y;
        return Punto(newX,newY)
    #endregion

    #region override minus -
    def __sub__(self, AltroPunto):
        newX = self.x - AltroPunto.x;
        newY = self.y - AltroPunto.y;
        return Punto(newX,newY)       
    #endregion

    #region override string
    def __str__(self):
        return "("+str(self.x) + ","+str(self.y) + ")"
    #endregion