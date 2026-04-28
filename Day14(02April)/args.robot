*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser    ${url}    chrome
    Maximize Browser Window
    ## number of args should be same as what is defined in the keyword section
    Login Success    cheeseburger@gmail.com    ## This line works as a function here with positional arg in keyword section
    Sleep    5s
    Close Browser
    
*** Keywords ***
Login Success
    [Arguments]    ${email}    ${pwd}=iamironman    ## Positional argument, Default argument     ---> in this line
    Input Text    id=customer_email    ${email}
    Input Text    id=customer_password    ${pwd}