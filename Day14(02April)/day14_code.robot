# 4 Levels of Login
# Log  Message  LoginType
# Info :- To get the normal information
# Debug :- To get Additional inforamtion
# Warn  :- To get Warning when a additional popup occurs or something like that
# Error :- used mainly in try,except and finally block

# robot -d reports --timestampoutputs abc.robot :- so that previous log dont get overwritten
# but there is a drawback if there are multiple log and reports files it will store in
# ascending order and we have to scroll to far to search so we use a diff command

# robot -d "reports/$(Get-Date-Format 'yyyy-MM-dd_HH_mm_ss')  :- we use months first bcoz
# if date is first then we will get it sorted like 1Apr2026 then 1May2026 and we don want to do that

*** Settings ***
Documentation    levels of login
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.cricbuzz.com/

*** Test Cases ***
handling login
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Log    navigated to cricbuzz    ERROR
    Log To Console    navigated to cricbuzz
    Sleep    3s
    Close Browser

## robot -d reports --timestampoutputs open_browser.robot    --> correct one
## robot -d reports/$(Get-Date-Format 'yyyy-MM-dd_HH-mm-ss') <filename>    --> correct one


## arguments in python:
## positional, default, keyword arguments
## whenever calling a function and passing arguments it becomes keyword arguments eg. name(first='abc', last='xyz')