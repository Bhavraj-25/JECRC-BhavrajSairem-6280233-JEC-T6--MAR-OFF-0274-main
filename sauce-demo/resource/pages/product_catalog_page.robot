## from search till before add to cart

*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/prod_catalog_locator.robot

*** Keywords ***
Product Search
    [Documentation]    this is for searching and clicking on the product
    [Arguments]    ${search}

    Click Element    ${search_link}
    Log    clicking on search field
    
    Input Text    ${search_link}    ${search}
    Log    searching item in search field
    
    Click Element    ${search_button}
    Log    clicking on the search button

    Wait Until Element Is Visible    ${item_1}    10s
    Click Element    ${item_1}
    Log    clicking on the first item

    Sleep    5s