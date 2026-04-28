*** Settings ***
Documentation  Handling Checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://https://testautomationpractice.blogspot.com/

*** Keywords ***
Opening TA site
    [Documentation]    TA site selection
    Open Browser  ${url1}  chrome
    Maximize Browser Window
    Sleep    2s
    ## Click Element is from selenium library and locates and clicks at the element
    Click Element    xpath = //input[@id='male']
    ## To check whether the page contains the checkbox or not, these are assert type keywords and work like assert
#    Page Should Contain Checkbox    xpath = (//input[@type="checkbox"])
    ## Selects the checkbox mentioned as per the xpath
    Select Checkbox    xpath = //input[@id='sunday']
    Sleep    5s
    Unselect Checkbox    xpath = //input[@id='monday']
    Sleep    5s

*** Test Cases ***
Handle TA
    Opening TA Site

Handling Checkbox
    [Documentation]    This test case is to handle the checkbox selection
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    ## Click Element is from selenium library and locates and clicks at the element
    Click Element    xpath = //a[text()="Checkboxes"]
    ## To check whether the page contains the checkbox or not, these are assert type keywords and work like assert
    Page Should Contain Checkbox    xpath = (//input[@type="checkbox"])
    ## Selects the checkbox mentioned as per the xpath
    Select Checkbox    xpath = (//input[@type="checkbox"])[1]
    Sleep    5s
    Unselect Checkbox    xpath = (//input[@type="checkbox"])[1]
    Sleep    5s