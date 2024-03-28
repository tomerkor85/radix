
# Radix Home Assignment

**Install Requirements (local use):** 

* To install the requirements please type in terminal: `pip install -I requirements.txt`

**Run Tests (local use)**
* To run the tests you should type in terminal: `pytest --junitxml=report.xml`

## **About The Task** 

- We asked to check the login page for sanity tests.
- Login page URL : https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- GitHub Project Files: https://github.com/tomerkor85/radix
- Jenkins Server: http://ec2-51-21-73-91.eu-north-1.compute.amazonaws.com/job/radix_project/
  - Username: demo
  - Password: Radix2024
- Connect to Jenkins link and click "Build Now"
- Logs will display in the running job -> Test Results


## Tests Coverage
* Credentials:
  * Valid credentials.
  * Invalid credentials
  * Correct Username and Incorrect Password.
  * Incorrect Username and Correct Password.
  * Incorrect Username and Empty Password.
  * Empty Username and correct Password.
  * Empty Username and Empty Password.
* Elements:
  * Verify "Reset password" exists and redirect to reset page.
  * Make sure the UI username and password are display as expected.