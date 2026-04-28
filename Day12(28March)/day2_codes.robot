*** Settings ***
Documentation  Day 2 codes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
handle dropdown
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[text()="Dropdown"]
    
    Page Should Contain List    id=dropdown
    ${options}=    Get List Items    id=dropdown    ## Fetches the drop down items and store it in options with the specified locator
    Log To Console    ${options}
    
    Select From List By Label    id=dropdown  Option 1    ## Two arguments: locator and the label
    
    ${select_option}=    Get Selected List Label    id=dropdown
    Log To Console    ${select_option}
    
    List Selection Should Be    id=dropdown    Option 1
    
    Sleep    3s
    Close Browser

##    ${variable} takes single variable
##    @{variable} takes list of multiple variables
##    &{variable} takes dictionary of variables
##    Log to Console prints only single values, so it won't accept @{var} and throw error.
##    And if we write ${var} (var is a list), list will be printed as "[blue, white, green, ....]"
    
Handle TA    ## Task 1
    Open Browser    ${url1}  chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//select[@id="colors"]
    
    Select From List By Value    id=colors  blue
    Select From List By Label    id=colors  Green
    
    ${sel_options}  Get Selected List Labels    id=colors
    Log To Console    ${sel_options}

    Sleep    3s
    Close Browser