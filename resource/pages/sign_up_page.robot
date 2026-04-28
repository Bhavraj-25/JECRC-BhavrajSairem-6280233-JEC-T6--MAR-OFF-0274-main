*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/sign_up_locators.robot
*** Keywords ***
Sign Up To The Application
    [Documentation]    This is for signing up to the application
    [Arguments]    ${first_name}    ${last_name}    ${email}    ${pwd}
    Click Element    ${sign_up_link}
    Log    Clicking on sign up link
    Input Text    ${first_name_field}    ${first_name}
    Log    Entering first name
    Input Text    ${last_name_field}    ${last_name}
    Log    Entering last name
    Input Text    ${email_field}    ${email}
    Log    Entering email id
    Input Text    ${pwd_field}    ${pwd}
    Log    Entering password
    Click Element    ${create_btn}
    Log    Clicking on create button