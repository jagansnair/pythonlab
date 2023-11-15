import graphics.circle
import graphics.rectangle
import graphics.graphics3d.cuboid
import graphics.graphics3d.sphere
r=int(input("Enter the radius of circle:"))
r1=int(input("Enter the radius of sphere:"))
leng=int(input("Enter the length of rectangle:"))
bread=int(input("Enter the breadth of rectangle:"))
length=int(input("Enter the length of cuboid:"))
height=int(input("Enter the height of cuboid:"))
width=int(input("Enter the width of cuboid:"))
print("Area of a circle is : ",graphics.circle.area(r))
print("Perimeter of a circle is : ",graphics.circle.perimeter(r))
print("Area of a rectangle is : ",graphics.rectangle.area(leng,bread))
print("Perimeter of a rectangle is : ",graphics.rectangle.perimeter(leng,bread))
print("Area of a cuboid is : ",graphics.graphics3d.cuboid.area(length,width,height))
print("Perimeter of a cuboid is : ",graphics.graphics3d.cuboid.perimeter(length,width,height))
print("Area of a sphere is : ",graphics.graphics3d.sphere.area(r1))
print("Perimeter of a sphere is : ",graphics.graphics3d.sphere.perimeter(r1))
