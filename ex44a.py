# ex44: Inheritance Versus Composition - Implicit Inheritance

class Parent(object):

  def implicit(self):
    print "PARENT implicit()"

class Child(Parent):
  pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


# pass under class Child - tell python you want an empty block.
