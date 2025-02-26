# Static methods don't operate on either instance or class. 
# They're defined using the @staticmethod decorator and don't take self or cls parameters.
# Static methods are often used to create utility functions that don't need access to instance data.
class Math:
    @staticmethod
    def add(*args):
        sum=0
        for i in range(len(args)):
            sum += int(args[i])
        return sum

print(Math.add(10,10,10,10,3))

# In this example, the add method is a static method of the Math class.
# The method can be called on the class itself, without the need to create an instance of the class.

# static methods shouldn't have a 'self' parameter since they don't have access to instance attributes.

# In Python, static methods can be called both from the class itself and from any instance of the class.

inst = Math()
print(inst.add(4,5))