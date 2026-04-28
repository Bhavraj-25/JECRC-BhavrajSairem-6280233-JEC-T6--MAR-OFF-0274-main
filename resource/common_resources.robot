*** Settings ***
Library    SeleniumLibrary
Library    ../config/env_loader.py

*** Variables ***
${BROWSER}    chrome
#${ENV}    qa
${ENV}    prod

*** Keywords ***
Load Product Environment
    Load Env    ${ENV}
    ${BASEURL_P}    Get Env    BASEURL_PROD
    ${SEARCH}=    Get Env    SEARCH_TEXT
    Set Global Variable    ${SEARCH}
    Set Global Variable    ${BASEURL_P}
    
Load Environment
    Load Env    ${ENV}
    ${BASE_URL}=    Get Env    BASEURL
    ${FIRST_NAME}=  Get Env    FIRST_NAME
    ${LAST_NAME}=   Get Env    LAST_NAME
    ${EMAIL}=       Get Env    EMAIL
    ${PASSWORD}=    Get Env    PASSWORD

    Set Global Variable    ${BASE_URL}    ## Setting it to global variable
    Set Global Variable    ${FIRST_NAME}
    Set Global Variable    ${LAST_NAME}
    Set Global Variable    ${EMAIL}
    Set Global Variable    ${PASSWORD}
    
Open Product Applications
    [Documentation]    Opens the application for product testing
    Open Browser    ${BASEURL_P}    ${BROWSER}
    Maximize Browser Window

Open Applications
    [Documentation]    Opens the application
    [Arguments]    ${url}
    Open Browser    ${url}    ${BROWSER}
    Maximize Browser Window

CLose Applications
    Close All Browsers