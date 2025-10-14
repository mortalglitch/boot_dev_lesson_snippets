# boot_dev_lesson_snippets
Lessons from my boot.dev run through that produced some interesting code snippets.

## Python Notes:
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



## Git Notes:
TODO add notes about git flow and commands


```

