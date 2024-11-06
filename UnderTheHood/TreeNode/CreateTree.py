from ..Classes.Compile import Pottery, NonFunctionalPottery, Decorative, Planter, FunctionalPottery
from .TreeNode import TreeNode

pottery = TreeNode(Pottery, "Do you eat or drink in it?")
funcpottery = TreeNode (FunctionalPottery, "What shape is it?", True)
nonfuncpottery = TreeNode(NonFunctionalPottery, "Will it house growing plants?")

pottery.add_child(nonfuncpottery)
pottery.add_child(funcpottery)

plant = TreeNode(Planter, "What kind of planter do you want?", True)
deco = TreeNode(Decorative, "What type of piece would you like?", True)

nonfuncpottery.add_child(deco)
nonfuncpottery.add_child(plant)

