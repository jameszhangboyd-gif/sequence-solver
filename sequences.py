import math

class SequenceEngine:
    """
    A collection of tools for analyzing and solving discrete 
    mathematics patterns, specifically focusing on Precalculus Chapter 9.
    """

    @staticmethod
    def get_arithmetic_term(a1, d, n):
        """Calculates the nth term: a_n = a1 + (n-1)d"""
        return a1 + (n - 1) * d

    @staticmethod
    def get_geometric_term(a1, r, n):
        """Calculates the nth term: a_n = a1 * r^(n-1)"""
        return a1 * (r ** (n - 1))

    @staticmethod
    def get_arithmetic_partial_sum(a1, an, n):
        """Calculates the sum of first n terms: S_n = n/2 * (a1 + an)"""
        return (n / 2) * (a1 + an)

    @staticmethod
    def check_quadratic_pattern(sequence):
        """
        Uses finite differences to check if a pattern is quadratic (n^2).
        Returns the second difference if constant.
        """
        first_diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        second_diffs = [first_diffs[i+1] - first_diffs[i] for i in range(len(first_diffs)-1)]
        
        # Check if all second differences are the same
        if len(set(second_diffs)) == 1:
            return f"Quadratic Pattern Detected. Second Difference: {second_diffs[0]}"
        return "Not a simple quadratic pattern."

# --- TEST SUITE ---
if __name__ == "__main__":
    engine = SequenceEngine()
    
    while True:
        print("\n--- CHAPTER 9 MATH ENGINE ---")
        print("1. Find nth term (Arithmetic)")
        print("2. Find nth term (Geometric)")
        print("3. Analyze a pattern (Quadratic Check)")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            a1 = float(input("Enter starting number (a1): "))
            d = float(input("Enter the jump (d): "))
            n = int(input("Which term number do you want? "))
            print(f"Result: The {n}th term is {engine.get_arithmetic_term(a1, d, n)}")

        elif choice == '2':
            a1 = float(input("Enter starting number (a1): "))
            r = float(input("Enter the multiplier (r): "))
            n = int(input("Which term number do you want? "))
            print(f"Result: The {n}th term is {engine.get_geometric_term(a1, r, n)}")

        elif choice == '3':
            print("Enter your numbers separated by commas (e.g., 2, 5, 10, 17, 26)")
            user_input = input("Sequence: ")
            # This line converts the text "2, 5, 10" into a list of numbers [2, 5, 10]
            num_list = [float(x.strip()) for x in user_input.split(",")]
            print(f"Analysis: {engine.check_quadratic_pattern(num_list)}")

        elif choice == '4':
            print("Closing engine. Good luck with Precalc!")
            break
        else:
            print("Invalid choice, try again.")
