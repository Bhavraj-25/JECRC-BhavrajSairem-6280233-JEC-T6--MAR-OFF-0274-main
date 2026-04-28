*** Settings ***
Documentation    wait handling
Library    SeleniumLibrary

*** Variables ***
${url}    https://testautomationpractice.blogspot.com/
${url1}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling TA alerts
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Sleep    2s
    Click Element    xpath = //button[@id='alertBtn']
    Sleep    2s
    Handle Alert
    ${print}    Get Text    //p[@id="demo"]
    Log To Console    ${print}
    Sleep    5s

    Click Element    xpath = //button[@id='confirmBtn']
    Sleep    2s
    Handle Alert
    Page Should Contain    You pressed OK!
    ${print}    Get Text    //p[@id="demo"]
    Log To Console    ${print}
    Sleep    5s

    Click Element    xpath = //button[@id='promptBtn']
    Sleep    2s
    Input Text Into Alert    Amaze Amaze Amaze
    Page Should Contain    Hello Amaze Amaze Amaze! How are you today?
    ${print}    Get Text    //p[@id="demo"]
    Log To Console    ${print}
    Sleep    5s
    