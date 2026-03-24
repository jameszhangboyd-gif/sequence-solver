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
    
    print("--- Palantir Valley Forge Prep: Math Logic Tool ---")
    
    # Example 1: Your earlier problem (a1=4, d=7, n=5)
    term_5 = engine.get_arithmetic_term(4, 7, 5)
    print(f"Arithmetic 5th term (a1=4, d=7): {term_5}")

    # Example 2: Checking the quadratic sequence 2, 5, 10, 17, 26
    my_list = [2, 5, 10, 17, 26]
    print(f"Analyzing {my_list}: {engine.check_quadratic_pattern(my_list)}")
