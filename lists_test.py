import pytest

from lists import NumberList


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def list2():
    return [10, 10]

def testListsAverages(list1, list2): 
    numsList = NumberList(list1, list2)
    assert numsList.getList() == (3, 10)

#Наличие пустых списков тест
@pytest.mark.parametrize("lst1, lst2, result", [
    ([], [1, 2, 3], (0, 2)),
    ([1, 2, 3], [], (2, 0)),
    ([], [], (0, 0))])

def testEmptyLists(lst1, lst2, result):
    numList = NumberList(lst1, lst2)
    assert numList.getList() == result

#Наличие только 1 элемента тест
@pytest.mark.parametrize("lst1, lst2, result", [
    ([1], [1, 2, 3], (1, 2)),
    ([1, 2, 3], [1], (2, 1)),
    ([1], [1], (1, 1))])
def test_EmptyLists(lst1, lst2, result):
    numList = NumberList(lst1, lst2)
    assert numList.getList() == result


def testAverageValueGreater(list1, list2, capfd):
    numList = NumberList(list2, list1)
    numList.listComparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'У первого списка среднее значение больше'


def testAverageValue_Greater(list1, list2, capfd):
    numList = NumberList(list1, list2)
    numList.listComparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'У второго списка среднее значение больше'


def testAverage_Value_Greater(list1, list2, capfd):
    numList = NumberList(list1, list1)
    numList.listComparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == "У списков равное среднее значение"


def test_init(list1, list2):
    numsList = NumberList(list1, list2)
    assert numsList.lst1 == list1
    assert numsList.lst2 == list2