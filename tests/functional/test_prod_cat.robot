*** Settings ***
Resource    ../../resource/pages/product_catalog_page.robot
Resource    ../../resource/common_resources.robot

Suite Setup    Load Product Environment
Test Setup    Open Product Applications
Test Teardown    CLose Applications

*** Test Cases ***
TC03 Product Catalog
    [Documentation]    this is for product catalog testing
    [Tags]    functional
    Product Search    ${SEARCH}