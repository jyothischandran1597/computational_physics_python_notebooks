## Roots of a Quadratic Equation

# Quadratic equation: 𝑎𝑥+𝑏𝑥+𝑐=0

# Discriminant, D = (𝑏2−4𝑎𝑐)

# If D > 0, two unique and real roots.
# If D = 0, two equal and real roots.
# If D < 0, two unique and imaginary roots.

print("\nRoots of a Quadratic Equation\n")


a = int(input("Please enter value of 'a' in Quadratic Equation : "))
b = int(input("Please enter value of 'b' in Quadratic Equation : "))
c = int(input("Please enter value of 'c' in Quadratic Equation : "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant) / (2 * a))
    root2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("Two Distinct Real Roots Exists: root1 = {} and root2 = {}".format(root1, root2))
elif discriminant == 0:
    root = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root = {}".format(root))
elif discriminant < 0:
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    print("Two Distinct Complex Roots Exists: root 1 = ({:.2f}) + i ({:.2f}) and root 2 = ({:.2f}) - i ({:.2f})".format(root1, imaginary, root2, imaginary))