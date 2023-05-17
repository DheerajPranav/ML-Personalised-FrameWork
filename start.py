__author__ = 'Dheeraj'

# import relevant libraries
from tests.RegressionValidation import Validations


sample_trigger = True

if __name__ == '__main__':
    print('Info: Begin Performing Tasks.')

    """Test Regression Tasks"""
    Validations().regression_tasks()

    """Test Classification Tasks"""
    Validations().classification_tasks()
