from math_tools import SequenceEngine

def test_arithmetic():
    assert SequenceEngine.get_arithmetic_term(4, 7, 5) == 32
    print("Test Passed: Arithmetic logic is correct.")

if __name__ == "__main__":
    test_arithmetic()
