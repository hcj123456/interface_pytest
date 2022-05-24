import pytest


@pytest.fixture(scope='function', params=[1,2,3], autouse=True)
def function1(request):
    return request.param


# @pytest.mark.usefixtures('function1')
class Test_22:
    @pytest.mark.usefixtures('function1')   #不需要使用fixture中得返回值，则直接使用这个@pytest.mark.usefixtures调用
    def test_function2(self, function1):    #需要使用fixture中得返回值，则在方法中直接调用
        print(function1)

