from .Pottery import Pottery, NonFunctionalPottery

class Decorative (NonFunctionalPottery):
    """A superclass that contains different classes of decorative pottery,
    its class_category dict contains each of these classes under its individual category id, 
    str_categories is a str version of this dictionary.

    This class' category_id is the number of classes contained (index+1)"""

    category_id = 00
    str_categories = {}
    class_categories = {}

class Vase (Decorative):
    """Category_id is this class' id in the superclass' class_categories dict, 
    class counter is the n+1 of instances of this class"""
    class_counter = 000
    class_path = "NonFunctional/Decorative/Vase/"
    cat_name = "Vase"

    def __init__(self, name):
        self.id = Vase.class_counter
        Vase.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = Decorative.category_id
    Decorative.category_id += 1
    Decorative.str_categories [category_id] = cat_name

class Jewelry (Decorative):
    class_counter = 000
    class_path = "NonFunctional/Decorative/Jewelry/"
    cat_name = "Jewelry"
    def __init__(self, name):
        self.id = Jewelry.class_counter
        Jewelry.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = Decorative.category_id
    Decorative.category_id += 1
    Decorative.str_categories [category_id] = cat_name

class Ashtray (Decorative):
    class_counter = 000
    class_path = "NonFunctional/Decorative/Ashtray/"
    cat_name = "Ashtray"
    def __init__(self, name):
        self.id = Ashtray.class_counter
        Ashtray.class_counter += 1
        Pottery.__init__(self, name)
    
    category_id = Decorative.category_id
    Decorative.category_id += 1
    Decorative.str_categories [category_id] = cat_name

Decorative.class_categories = {0: Vase, 1: Jewelry, 2:Ashtray}
