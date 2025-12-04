import yo


def test_yoint_with_name():
    assert yo.yoint("bitch") == "Welcome, bitch nigga."


def test_yoint_without_name():
    assert yo.yoint() == "Welcome,  nigga."
