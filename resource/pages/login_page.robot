*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/login_locators.robot

*** Keywords ***
log In To The Application
    [Documentation]    This is for loging in to the application
    [Arguments]    ${login_email}    ${pwd}
    Input Text    ${login_link}    ${login_email}
    Log    Entering login mail
    Input Text    ${login_pw}    ${pwd}
    Log    Entering password
    Click Element    ${login_btn}
    Log    Clicking on login button
