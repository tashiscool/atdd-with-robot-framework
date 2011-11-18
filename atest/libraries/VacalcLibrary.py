import os
import tempfile
import datetime

from vacalc.employeestore import EmployeeStore, Employee


def get_employee_names():
    default_db = os.path.join(tempfile.gettempdir(), 'vacalcdb.csv')
    db_file= os.environ.get('VACALC_DB', default_db)
    return [emp.name for emp in EmployeeStore(db_file).get_all_employees()]


def application_should_have_employees(expected):
    expected = [name.strip() for name in expected.split(',')]
    actual = get_employee_names()
    if actual != expected:
        raise AssertionError('Expected employees: %s\nActual employees: %s'
                             % (', '.join(expected), ', '.join(actual)))


def vacation_should_be_calculated_correctly(startdate_str, vacation_year,
                                            exp_vacation_days):
    startdate = _create_date(startdate_str)
    vacation_year = int(vacation_year)
    exp_vacation_days = int(exp_vacation_days)
    actual_days = Employee('Test Employee', startdate).count_vacation(vacation_year)
    if actual_days != exp_vacation_days:
        raise AssertionError('%s != %s' % (exp_vacation_days, actual_days))

def _create_date(startdate_str):
    try:
        year, month, day = startdate_str.split('-')
        return datetime.date(int(year), int(month), int(day))
    except Exception, err:
        raise AssertionError('Invalid time format %s' % err)
