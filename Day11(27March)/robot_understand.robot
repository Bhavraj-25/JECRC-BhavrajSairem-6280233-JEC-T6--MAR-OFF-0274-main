#Robot is a keyword driven testing framework developed by nokia
#similar to coffee machine - press a single button and all the things will work automatically
#
#all import and packages from other files will come under:- settings section
#variables will come under where we will declare:-variables section
#scripts containing test cases will come under :- Test Cases section
#when we create user defined keyword will come under :- keyword section
#
#Close Window :- closes a tab of the recent browser
#Close Browser :- closes the recent browser all tabs
#Close All Browser :- closes all browser
#
#Tage are used for grouping the test cases
#For grouping of test cases we use:- [Tags]  Smoke
#-i -> include
#-e -> exclude
#robot -d reports -i "smoke" open_browser.robot


# robot -d reports -t "msg" TestCase.robot to run a single test case one

# open browser
*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***
## This is Scalar variable
${url}  https://www.formula1.com/
## List variables
@{f1_cars}  mercedes  redbull  ferrari  mclaren  williams  audi  cadillac  racing-bulls    ## Double space is between the list items
## Dictionary variables
&{fighter_jet}  boeing=f18  lockheed=f16  hal=tejas  ge=c130  airbus=c295    ## Key pair use '=' not ':' from like python

*** Test Cases ***
Opening Chrome Browser               # Test Case Name
    [Documentation]  Chrome browser navigating to https://www.youtube.com
    # open browser  URL  ChromeType
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Log    navigated to youtube     # Will give output in log file
    Log To Console    navigated to youtube     # gives output in terminal
    Log To Console    ${fighter_jet.boeing}
    Log To Console    ${f1_cars}[1]
    Sleep  3s

    Close Browser

#Opening FireFox Browser
#    [Documentation]  FireFox browser navigated to youtube.com
#    Open Browser  https://www.youtube.com
#    Maximize Browser Window
#    Log  navigated to youtube
#    Log To Console  navigated to youtube
#    Sleep  1000ms
#
#    Close Browser
#
#Opening Edge Browser
#    [Documentation]  Edge Browser navigated to youtube.com
#    Open Browser  https://www.youtube.com
#    Maximize Browser Window
#    Log  navigated to youtube
#    Log To Console  navigated to youtube
#    Sleep  5s
#
#    Close Browser

Opening Chrome headless Browser               # Test Case Name
    [Documentation]  Chrome browser navigating to https://www.youtube.com
    [Tags]  smoke reg
    Open Browser  https://www.youtube.com/  chrome headlesschrome     # works only for chrome
    Maximize Browser Window
    Log    navigated to youtube     # Will give output in log file
    Log To Console  navigated to youtube     # gives output in terminal
    Sleep  3s

    Close Browser