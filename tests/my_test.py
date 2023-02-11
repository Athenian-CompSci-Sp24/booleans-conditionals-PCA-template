import src.my_code


def test_inc():
    assert 660 == src.my_code.pay_calculator(40)
    assert 907.50 == src.my_code.pay_calculator(50)
    assert 330 == src.my_code.pay_calculator(20)
