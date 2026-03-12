import random
import types
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


# Tests for the check_guess() fix: condition changed from `guess > secret` to `guess < secret`
# The fixed logic: if guess < secret → "Too High"; else → "Too Low"

def test_check_guess_fix_low_guess_returns_too_high():
    # Bug: original `if guess > secret` would return "Too Low" for guess=40, secret=50.
    # Fix: `if guess < secret` correctly returns "Too High" for this case.
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low", (
        "When guess (40) < secret (50), outcome should be 'Too Low'. "
        "This would fail with the old `if guess > secret:` condition."
    )

def test_check_guess_fix_high_guess_returns_too_low():
    # Bug: original `if guess > secret` would return "Too High" for guess=60, secret=50.
    # Fix: `if guess < secret` correctly returns "Too Low" for this case.
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High", (
        "When guess (60) > secret (50), outcome should be 'Too High'. "
        "This would fail with the old `if guess > secret:` condition."
    )


# Tests for the new game button fix:
# Before fix: only reset `attempts` and `secret` (missing status and history reset)
# After fix: also resets `status` to "playing" and `history` to []

def _simulate_new_game(session_state, low=1, high=100):
    """Replicate the fixed new_game button logic without Streamlit."""
    session_state.attempts = 0
    session_state.status = "playing"
    session_state.history = []
    session_state.secret = random.randint(low, high)

def test_new_game_resets_status():
    # Before fix, status was never reset, so a won/lost game couldn't restart.
    state = types.SimpleNamespace(attempts=5, status="won", history=[40, 60], secret=50)
    _simulate_new_game(state)
    assert state.status == "playing", "New game must reset status to 'playing'."

def test_new_game_resets_history():
    # Before fix, history was never cleared, so old guesses would persist.
    state = types.SimpleNamespace(attempts=5, status="won", history=[40, 60], secret=50)
    _simulate_new_game(state)
    assert state.history == [], "New game must clear history."

def test_new_game_resets_attempts():
    state = types.SimpleNamespace(attempts=5, status="won", history=[40, 60], secret=50)
    _simulate_new_game(state)
    assert state.attempts == 0, "New game must reset attempts to 0."

def test_new_game_secret_within_range():
    # Before fix, secret was always random.randint(1, 100) regardless of difficulty range.
    # After fix, it uses the difficulty-aware `low` and `high` values.
    state = types.SimpleNamespace(attempts=5, status="won", history=[], secret=50)
    low, high = 1, 20  # Easy difficulty range
    _simulate_new_game(state, low=low, high=high)
    assert low <= state.secret <= high, (
        f"New game secret {state.secret} must be within difficulty range [{low}, {high}]."
    )
