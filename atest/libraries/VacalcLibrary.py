import os
import tempfile

from vacalc.employeestore import EmployeeStore

def get_all_employee_names():
    default_db = os.path.join(tempfile.gettempdir(), 'vacalcdb.csv')
    db_file= os.environ.get('VACALC_DB', default_db)
    return [emp.name for emp in EmployeeStore(db_file).get_all_employees()]
