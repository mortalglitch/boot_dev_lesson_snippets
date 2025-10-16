# boot_dev_lesson_snippets

Lessons from my boot.dev run through that produced some interesting code snippets.

## Python Notes

Classes are a sort of template. Objects are a instance of a class.

```
class monkey:
  body_type= "hairy" # This is a class level variable and will change all impact all objects if changed
  def __init__(self, name):
    self.name = name  # This is a instance variable and will be unique to the object which set it up. So monkeys can each have a different name but are all hairy.
```

Public vs. Private
All properties and methods within a class are public. To make one private you need use "__" (double underscore) to their name.
Example:
>self.__weapon = weapon

you could no longer call class.__weapon outside of the class definition

### Abstraction vs. Encapsulation

Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed (public).
Encapsulation is about hiding internal state. It focuses on tucking away the implementation details (private).
Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.

### Inheritance

Inheritance makes a new class out of an old class without duplicating the code. The new child class can have their own methods and variables while still using the variables and methods of the parent.
Example

```

class computer:
  def __init__(self, cpu, gpu):
  etc.. etc..

class laptop(computer):
  def __init__(self, cpu, gpu):
    super().__init__(cpu, gpu)   #note the super it calls the parents init
    self.battery = 5000mah

```

### Polymorphism

Polymorphism means many forms. It allows for a common interface for inherited classes. It allows a variable, function or object to take on multiple forms.
Example:

```

class animal():
  def make_sound(self):
    pass
  
class dog(animal):
  def make_sound(self):
    print("Bark")

```

You can even overload operators such as def __add__ can override how a class is added '+'.

```

Operation Operator Method
Addition + __add__
Subtraction - __sub__
Multiplication * __mul__
Power ** __pow__
Division / __truediv__
Floor Division // __floordiv__
Remainder (modulo) % __mod__
Bitwise Left Shift << __lshift__
Bitwise Right Shift >> __rshift__
Bitwise AND & __and__
Bitwise OR | __or__
Bitwise XOR ^ __xor__
Bitwise NOT ~ __invert__

```

You can also override a built in method like print() by using __str__

TODO:

Need a breakdown of list, dict's, tuples list of dictionaries and more.

## Git Notes

TODO add notes about git flow and commands

```

