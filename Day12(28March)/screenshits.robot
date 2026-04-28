*** Settings ***
Documentation    javascript executor
Library    SeleniumLibrary

*** Variables ***
${url}    https://in.bookmyshow.com/explore/home/jaipur

*** Test Cases ***
Screenshots
#    Set Screenshot Directory    ${CURDIR}/../Screenshots    ## To go back from current directory; create Screenshot folder; save images there
    ## We can also use absolute path and set it
    Set Screenshot Directory    ${CURDIR}/Screenshots
    
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Sleep    2s
    Capture Page Screenshot    fullpage.png    ## Captures Whole page Screenshot
    Sleep    2s
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]    Dhurandhar.png
    Sleep    2s

    Close Browser