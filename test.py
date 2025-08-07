import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
@pytest.mark.skip(reason="this feature is not ready yet")
def test_openbrowser():
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        driver.quit()
def add(a,b):
        return a+b
def sub(a,b):
        return a-b

def test_add():
        print(add(1,2))
@pytest.mark.xfail(reason="this is known bug, test is expected to fail")
def test_sub():
         print(sub(7,1))
@pytest.mark.smoke
def test_smoke():
        print("running smoke test")
@pytest.mark.regression
def test_testing():
        print("running regression cases")

@pytest.mark.parametrize("name",["ali","sana","charlie"])
def test_parametrization_example(name):
        print(f"Testing with {name}")



@pytest.fixture()
def helo_name():
        data={"name":"iqra"}
        yield data
        print("Teardown:cleansing data")


def test_1(helo_name):
        print("test1 running with :",helo_name["name"])
def test_2(helo_name):
        print("test2 running with :",helo_name["name"])



@pytest.fixture(params=[1,2,3])
def sample_data(request):
        return request.param

def test_eg(sample_data):
        result=sample_data*2
        print(f"result={result}")



# equality assertion
def test_addition():
        a=5
        b=3
        assert a+b ==9

def test_subtraction():
        a=5
        b=3
        assert a-b !=8



#         Boolean assertion
def test_positive_number():
        num=-7
        assert num>0
# membership assertion
def test_fruit():
        fruit={"apple","orange","banana"}
        assert "n" in fruit
# length assertion
def   test_length():
        item={1,2,3}
        assert len(item)==3






#multiply assertion
def test_mul():
        num=6
        assert num>0
        assert num%2==0
        assert isinstance(num,int)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
@pytest.mark.xfail(reason="Known bug: This test is expected to fail")
def test_add():
   print(add(1, 2))
@pytest.mark.smoke
def test_subtract():
    print(subtract(8,6))
    print("running smoke test")
@pytest.mark.regression
def test_regression_example():
    print("Running a regression test.")
@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_parametrize_example(name):
    print(f"Testing with: {name}")

# fixture plus text example
@pytest.fixture()
def helo_name():
       data={"name":"iqra"}
       yield data
       print("tearing down : Using this data in upcoming functions")

def test_1(helo_name):
        print("test1 running with :",helo_name["name"])

def test_2(helo_name):
       print("test2 running with :",helo_name["name"])
# fixture plus parametrization

@pytest.fixture(params=[2,4,6])
def  sampledata(request):
    return request.param

def test_multiplication(sampledata):
    result = sampledata*2
    print(f"result={result}")
# Assertions -equality assertion

def test_add_():
    a=5
    b=2
    assert a+b==7
def test_sub():
    a=6
    b=3
    assert a-b!=3
# Boolean Assertions
def test_positive_number():
    num=-5
    assert num>0
# membership assertion
def test_fruit():
    fruit={"apple","orange","banana"}
    assert "Mango" in fruit
def test_length():
    items={1,2,3,4,5,6,7,8,9,10}
    assert len(items)==7
# multiply assertion
def test_mul():
        num=-6
        assert num>0
        assert num%2==0
        assert isinstance(num,int)