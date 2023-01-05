class Circle:
    radius = int(input("Enter radius of circle: "))
    

    def perimeter(self):
        perimeter = 2*3.14*self.radius
        print("Perimeter of circle is",perimeter)

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("area of circle is ",area)
