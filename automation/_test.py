import pytest
import string

@pytest.mark.parametrize("password, digit, lower, upper, symbl",
					    [("mah12@", 2, 3, 0, 1),
	                     ("dJJB%^", 0, 1, 3, 2),
						 ("", 0, 0, 0, 0),
						 ("", 0, 0, 0, 1),
						 ("@", 1, 1, 1, 0),
						 ("mAhdi", 1, 4, 1, 0),
						 ("سالمون", 0, 0, 0, 6),
						 ("سالمون", 0, 0, 6, 0),
						 ("سالمون", 0, 6, 0, 0),
						 ("سالمون", 6, 0, 0, 0)])
def test_multiplication_rigix(password: str, digit: int, lower: int, upper: int, symbl: int):
    
	d, l, u, s = 0, 0, 0, 0
	for p in password:
		if p in string.digits:
			d += 1
		elif p in string.ascii_lowercase:
			l += 1
		elif p in string.ascii_uppercase:
			u += 1
		else : s += 1
	
	assert d == digit and l == lower and u == upper and s == symbl
		