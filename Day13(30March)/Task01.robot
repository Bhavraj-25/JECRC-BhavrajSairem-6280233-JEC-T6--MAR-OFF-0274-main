*** Settings ***
Documentation    Handling window
Library    SeleniumLibrary

*** Variables ***
${url1}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Task 1
    Open Browser    ${url1}    chrome
    Maximize Browser Window
    Sleep    2s
    Execute Javascript    window.scrollBy(0,500)
    Sleep    3s

    Click Element    xpath = //button[@id='PopUp']
    Sleep    2s

    @{windows1}    Get Window Handles

    Switch Window    NEW
    @{titles1}    Get Window Titles
    Log To Console    ${titles1}

    Switch Window    ${windows1}[0]

    Page Should Contain Element    xpath = //h1[@class='title']

    Sleep    5s
    Close Browser