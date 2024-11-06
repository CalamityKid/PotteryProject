from .Pottery import Pottery, NonFunctionalPottery

class Planter (NonFunctionalPottery):
    """A superclass that contains different classes of hanging and non hanging planters, 
    its class_category dict contains each of these classes under its individual category id, 
    str_categories is a str version of this dictionary.

    This class' category_id is the number of classes contained (index+1)"""
    category_id = 00
    str_categories = {}
    class_categories = {}

class NonHanging (Planter):
    class_counter = 000
    class_path = "NonFunctional/Planters/NonHanging/"
    cat_name = "NonHanging"
    def __init__(self, name, is_base=False):
        self.id = NonHanging.class_counter
        NonHanging.class_counter += 1
        self.is_base = is_base
        Pottery.__init__(self, name)


    category_id = Planter.category_id
    Planter.category_id += 1
    Planter.str_categories [category_id] = cat_name

class Hanging (Planter):
    """contains a is_base bool parameter that defaults to false"""
    class_counter = 000
    class_path = "NonFunctional/Planters/Hanging/"
    cat_name = "Hanging"

    def __init__(self, name, is_base=False):
        self.id = Hanging.class_counter
        Hanging.class_counter += 1
        self.is_base = is_base
        Pottery.__init__(self, name)

    category_id = Planter.category_id
    Planter.category_id += 1
    Planter.str_categories [category_id] = cat_name




Planter.class_categories = {0: NonHanging, 1: Hanging}


