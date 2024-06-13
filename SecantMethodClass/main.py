
class SecantMethod:

    def __init__(self, f, tolerance=1e-6, max_iterations=50):  # Constructor with boot lines
        self.f = f
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def find_root(self, x0, x1):  # A general function for finding a root with the secant method
        p = None
        print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "xo", "x1", "p"))
        for i in range(self.max_iterations):
            if self.f(x1) - self.f(x0) == 0:
                print("Derivative is zero at x0, method cannot continue")
                return None

            p = x0 - self.f(x0) * ((x1 - x0) / (self.f(x1) - self.f(x0)))

            if abs(p - x1) < self.tolerance:
                return p  # Procedure completed successfully
            print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1, p))
            x0 = x1
            x1 = p
        return p  # Method reached maximum iterations without convergence


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x + 2
    x0 = 80
    x1 = 100
    TOL = 1e-6
    N = 20
    root_finder = SecantMethod(f, TOL, N)  # Creating an object from class SecantMethod
    roots = root_finder.find_root(x0, x1)  # Calling the function 'find_root' of the object 'root_finder'
    print(f"\n The equation f(x) has an approximate root at x = {roots}")
