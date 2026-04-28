*** Settings ***
Resource    ../../resource/pages/login_page.robot
Resource    ../../resource/common_resources.robot

Test Setup    Open Applications    https://sauce-demo.myshopify.com/account/login
Test Teardown    CLose Applications

*** Test Cases ***
TC02 Login User
    [Documentation]    Checking if the user can login or not
    [Tags]    functional
    Log In To The Application    tonylovescheeseburger@gmail.com    password123