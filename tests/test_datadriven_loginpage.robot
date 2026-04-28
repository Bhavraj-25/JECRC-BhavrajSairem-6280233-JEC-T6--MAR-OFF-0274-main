## Test data is using data from external data file and using it test on our test cases

*** Settings ***
Resource    ../resource/common_resources.robot
Library    DataDriver    ../testdata/login_credentials_sauce_data.xlsx    sheet_name=Sheet1    
## DataDriver is a python module that reads the excel file and treats each row as a test case

Test Setup    Open Applications    https://www.saucedemo.com/
Test Teardown    CLose Applications
Test Template    Login to application using excel    
## (Test Template) this is used to run the keyword multiple times like for loop to run the test cases in the excel sheet

*** Variables ***
${USERNAME}    id=user-name
${PASSWORD}    id=password
${LOGINBTN}    id=login-button

*** Test Cases ***
Excel Data Driven Testing    ${user_creds}    ${pass_creds}
    ## passing headers: it is mandatory to pass these headers to identify it from excel sheet
    [Documentation]    This test case is to perform data driven testing from excel
    [Tags]    data_driven

*** Keywords ***
Login to application using excel
    [Arguments]    ${user_creds}    ${pass_creds}
    ## this portion should be present in this section of this test file always so that it can access the values from excel
    ## so each values from the excel sheet is taken and passed on
    Input Text    ${USERNAME}    ${user_creds}
    Input Text    ${PASSWORD}    ${pass_creds}
    Click Button    ${LOGINBTN}
    
    
## Parallel execn is running multiple test cases parallely
## To run test cases parallely, cmd is:
    ## pabot --processes 4 --testlevelsplit -d reports tests    : will run 4 at a time, coz "--processes 4" is given

