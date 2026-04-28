#Robot is a keyword driven testing framework
#similar to coffee machine - press a single button and all the things will work automatically
#all import and packages from other files will come under:- settings section
#variables will come under where we will declare:-variables section
#scripts containing test cases will come under :- Test Cases section
#when we create user defined keyword will come under :- keyword section

#Close Window :- closes a tab of the recent browser
#Close Browser :- closes the recent browser all tabs
#Close All Browser :- closes all browser

# open browser
*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Keywords ***
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.youtube.com
    # open browser  URL  ChromeType
    Open Browser  https://www.youtube.com/  chrome
    Maximize Browser Window
    Log    navigated to youtube     # Will give output in log file
    Log To Console  Level     # gives output in terminal
    Sleep  3s

    Close Browser

*** Test Cases ***
Opening Youtube in Chrome    ## In keywords, we can define the whole script section and becomes the custom keyword and use it in test case
    Opening Chrome Browser