*** Settings ***
Resource    ../../resource/pages/sign_up_page.robot
Resource    ../../resource/common_resources.robot

# Setup and teardown
# 1) suite setup and teardown :- common for one whole session,opens browser runs all test files and then closes
# 2) test setup and teardown :- similar to explicit wait :- applies to individual test ,open browser for each test case

##  in suite all the test cases it will open, run all test case, close
##  in test for each test case it will open, run that case, close. similarly for other test cases 
    ##    eg. if 10 test cases it will open, run, close 10 times

Suite Setup    Load Environment
Test Setup    Open Applications
Test Teardown    CLose Applications

*** Test Cases ***
TC01 Register User
    [Documentation]    Checking if the user can register or not
    [Tags]    functional
    Sign Up To The Application    Tony    Stark    tonylovescheeseburger@gmail.com    password123