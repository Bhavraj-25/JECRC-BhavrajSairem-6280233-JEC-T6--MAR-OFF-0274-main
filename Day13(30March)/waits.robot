*** Settings ***
Documentation    wait handling
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/
${url1}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling Waits
    Open Browser    ${url}    chrome
#    Maximize Browser Window
    ${before}    Get Selenium Implicit Wait
    Log To Console    ${before}
    
    Set Selenium Implicit Wait    5s
    ${after}    Get Selenium Implicit Wait
    Log To Console    ${after}

    Close Browser
    
Handling Alerts
    Open Browser    ${url1}    chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath = //button[@onclick='jsAlert()']
    Sleep    2s
    Handle Alert
    Sleep    5s

    Click Element    xpath = //button[@onclick='jsConfirm()']
    Sleep    2s
    Handle Alert    action=DISMISS    ## to dismiss or cancel the alert; else remove the action part
    Sleep    5s

    Click Element    xpath = //button[@onclick='jsPrompt()']
    Sleep    2s
    Input Text Into Alert    Dirty Dirty Dirty
#    Handle Alert
    Sleep    5s

    Close Browser