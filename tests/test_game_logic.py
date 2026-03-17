from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_high_with_string_secret_from_new_game():
    #FIX: Added this regression test with Copilot assistant to catch high/low bug when secret is str.
    # This replicates the bug where app sets secret as a string on certain attempts.
    outcome, _ = check_guess(100, "50")
    assert outcome == "Too High"

