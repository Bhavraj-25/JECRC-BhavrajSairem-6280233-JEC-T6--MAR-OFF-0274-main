*** Settings ***
Documentation    Handling window
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/windows
${url1}    https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Handle Iframes
    Open Browser    ${url1}    chrome
    Maximize Browser Window
    Sleep    2s
    Select Frame    id = singleframe
    Input Text    xpath = //input[@type='text']    Grace & Rocky Save Stars
    Sleep    5s
    Unselect Frame

    Click Element    xpath = (//a[@data-toggle='tab'])[2]
    Select Frame    xpath = //iframe[@src='MultipleFrames.html']
    Select Frame    xpath = /html/body/section/div/div/iframe
    Input Text    xpath = /html/body/section/div/div/div/input    Amaze Amaze Amaze

    Sleep    5s
    Close Browser