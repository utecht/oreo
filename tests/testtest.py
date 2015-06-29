def unittest_test():
    assert True == True


from nose.tools import assert_equals

def nosetest_test():
    assert_equals(True, True)


from nose import with_setup

def setup_function():
    global a
    a = 5

def teardown_function():
    global a
    a = None

@with_setup(setup_function, teardown_function)
def test_setup():
    assert_equals(a, 5)
