from project import checkwin

def test_X_wins_row():
    xState = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert checkwin(xState, zState) == 0, "Test Failed: X should win with the top row."

def test_O_wins_column():
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 1, 0, 0, 1, 0, 0, 1, 0]
    assert checkwin(xState, zState) == 1, "Test Failed: O should win with the middle column."  # Corrected expected value to 1

def test_draw():
    xState = [1, 0, 1, 1, 1, 0, 0, 1, 0]
    zState = [0, 1, 0, 0, 0, 1, 1, 0, 1]
    assert checkwin(xState, zState) == 2, "Test Failed: The game should be a draw."  # Corrected expected value to 2

def test_no_winner():
    xState = [1, 0, 1, 0, 0, 0, 0, 0, 0]
    zState = [0, 1, 0, 1, 0, 0, 0, 0, 0]
    assert checkwin(xState, zState) == -1, "Test Failed: There should be no winner yet."

def run_tests():
    test_X_wins_row()
    test_O_wins_column()
    test_draw()
    test_no_winner()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()