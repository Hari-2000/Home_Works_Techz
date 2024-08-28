class Triangle :
    def __init__(shape,length,breadth) :
        shape.length = length
        shape.breadth = breadth

    def area(shape) :
        shape.a = shape.length*shape.breadth
        print("The Area of a Rectangle = ",shape.a)
    def perimeter(shape) :
            shape.p = 2*(shape.length+shape.breadth)
            print("The Perimeter of a Rectangle = ",shape.p)

t1 = Triangle(20,30)
t1.area()            
t1.perimeter()