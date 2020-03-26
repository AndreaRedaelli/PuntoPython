#region import
import Punto
#endregion

inputX = input("Please insert a value X \n");
inputY = input("Please insert a value Y \n");

punto = Punto.Punto(inputX,inputY)

print(punto)
puntoB = Punto.Punto(1,1)
punto = punto + puntoB

print(punto)