*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Test Shadow DOM
    Open Browser    ${URL}    Chrome
    Maximize Browser Window
    ${shadow_text_element}=    Get Shadow Element    div[id='shadow_host']    input[type='text']
    Input Text    ${shadow_text_element}    Sera
    ${shadow_button_element}=    Get Shadow Element    div[id='shadow_host']    input[type='checkbox']
    Click Element    ${shadow_button_element}

    Sleep    5s
    Close All Browsers
    
*** Keywords ***
Get Shadow Element
    [Arguments]    ${parent_locator}    ${child_locator}
    ${element}=     Execute Javascript
    ...    return document.querySelector('${parent_locator}')    ## JS query selector line that returns element of specified locator
    ...    .shadowRoot.querySelector('${child_locator})
    RETURN    ${element}