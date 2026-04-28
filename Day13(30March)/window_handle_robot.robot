*** Settings ***
Documentation    Handling window
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/windows
${url1}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Windows
    Open Browser    ${url}    chrome
    Maximize Browser Window
    SLeep    2s

    Click Element    xpath = //a[text()='Click Here']
    Sleep    2s
    
    @{windows}    Get Window Handles
    @{titles}    Get Window Titles
    Log To Console    ${titles}
    Switch Window    NEW
    
    Page Should Contain    New Window
    Page Should Contain Element    xpath = //h3[text()='New Window']
    
    Switch Window    ${windows}[0]
    Switch Window    ${windows}[1]

    Sleep    5s
    Close Browser
    
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