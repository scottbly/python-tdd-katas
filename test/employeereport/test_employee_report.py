from src.employeereport import employeereport


def test_return_all_employees():
    assert (employeereport.employee_report_for_day("Monday")) == ["Max", "Sepp", "Tom", "Nina", "Mike"]