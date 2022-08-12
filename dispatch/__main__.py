from dispatch import subscribers  # <- here utils.REGISTRY gets populated
import utils

print("import utils               :", utils.REGISTRY)  # <- Why is this empty?

from dispatch import utils

print("from dispatch import utils :", utils.REGISTRY)  # <- And this is not?
