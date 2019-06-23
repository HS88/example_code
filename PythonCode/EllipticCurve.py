#
# A very simple implementation of ECC for Homework-2
# It was written to solve the questions given in hw-2.
#
#
import math
class NoneDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key)

class ECC:
    y_sqrt_table = NoneDict()#{} #y^2,y pair
    def __init__(self, a,b,p):
        self.a = a
        self.b = b    # creates a new empty list for each dog
        self.p = p
        self.points = []
        for i in range(0,self.p):
            y_sqr = (i*i)%self.p
            if ECC.y_sqrt_table[y_sqr] is None:
                ECC.y_sqrt_table[y_sqr] = i
    
    def GetDiscriminant(self):
        d = (4 * (self.a**3)) + (27*(self.b**2))
        if ( d == 0 ):
            print('Curve is Singular')
        else:
            print( 'Curve is Smooth')
        return( d )

    def GetRange( self ):
        lower = self.p + 1 - 2*math.sqrt(self.p)
        upper = self.p + 1 + 2*math.sqrt(self.p)
        print( str(lower) + " <= Order(E) <= " + str(upper))
        print( str(math.ceil(lower)) + " <= Order(E) <= " + str(math.floor(upper)))
        
    def subtract(self,x1,x2):
        return (x1-x2)%self.p
    def add(self,x1,x2):
        return (x1+x2)%self.p
    def multiply(self,x1,x2):
        return (x1*x2)%self.p
    def inverse(self,x):
        return x**(self.p-2)%self.p
    
    def GetPoints(self):
        self.points.append((float('inf'),float('inf')))
        for i in range(0, self.p):
            x = i
            y_sq = (x*x*x + self.a*x + self.b)%self.p
            if y_sq == 0:
                self.points.append((i,0))
                continue
            if ECC.y_sqrt_table[y_sq] is not None:
                self.points.append((i,ECC.y_sqrt_table[y_sq]))
                self.points.append((i,self.p-ECC.y_sqrt_table[y_sq]))

    def NegatePoint( self, point ):
        x,y = point
        return (x,-y)
    
    def AddPoints(self, point1, point2):
        x1,y1=point1
        x2,y2=point2
        if( x1 == float('inf') and y1 == float('inf')):
            return point2
        if( x2 == float('inf') and y2 == float('inf')):
            return point1
        if( y2 == (self.p - y1) and x1 == x2 ):
            return( float('inf'),float('inf') )
        if( x1 != x2):
            slope = self.multiply(self.subtract(y2,y1),self.inverse(self.subtract(x2,x1)))
        else:
            slope = self.multiply(self.add((3*x1*x1)%self.p,self.a),self.inverse(self.multiply(2,y1)))
        x3 = self.subtract(self.subtract(self.multiply(slope,slope),x1),x2)
        y3 = self.subtract(self.multiply(slope,self.subtract(x1,x3)),y1)
        return(x3,y3)

    def AddPointSelf(self, n, point):
        if(n < 0):
            n = self.p + n
        result = point
        point1 = point
        for i in range(n-1):
            point2 = self.AddPoints(point,point1)
            point1 = point2
        return point1
        
ecc = ECC(3,4,37)
print('y^2 = x^3 + ' + str(ecc.a)+'x + ' + str(ecc.b))
print('Disriminant = ' + str(ecc.GetDiscriminant()))
ecc.GetPoints()
print(ecc.points)
G_order = len(ecc.points)
print('\nOrder of elliptic curve = ' + str(G_order))
p = ()
for i in range(G_order):
    pointsGenerated = []
    point1 = ecc.points[i]
    point2 = ecc.points[i]
    for j in range(G_order):
        point3 = ecc.AddPoints( point1, point2 );
        point2 = point3
        if point3 not in pointsGenerated:
            pointsGenerated.append(point3)
        else:
            break
    if(len(pointsGenerated) == len(ecc.points)):
        print(str(point1) +' is Primitive element')
        p = point1
        break

print('\n')
for i in [2,3,6,7,14,15,30,31]:
    o = ecc.AddPointSelf(i,p)
    print('['+str(i)+']'+str(p)+' = ' + str(o))
print('\n')
for i in [2,4,8,16,32,31]:
    o = ecc.AddPointSelf(i,p)
    print('['+str(i)+']'+str(p)+' = ' + str(o))
