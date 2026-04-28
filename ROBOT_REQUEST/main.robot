*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Pet Inventory Store
    [Documentation]    Get your pet inventory by status
    Create Session    petApi    ${BASE_URL}
    
    ${response}=    GET On Session    petApi    /store/inventory
    
    ## .status_code returns the status code of the response in INT and compares it with 200
    Should Be Equal As Integers    ${response.status_code}    200
    
    ## Converts the raw string response to JSON format and stores it in the variable ${body}
    ${body}=    Set Variable    ${response.json()}
    
    Log To Console    ${body}
    Log To Console    ${response.status_code}

Place Holder
    [Documentation]    Place an order for pet
    Create Session    petApi    ${BASE_URL}    verify=True
    
    ${payload}=    Create Dictionary
    ...    id=123
    ...    petId=12345
    ...    quantity=1
    ...    shipDate=2024-06-01T12:00:00.000
    ...    status=placed
    ...    complete=true
    
    ## payload body is being sent in JSON format and the response is stored in the variable ${response}
    ${response}=    POST On Session    petApi    /store/order    json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    
    Should Be Equal As Integers    ${body}[id]    123
    Should Be Equal As Strings    ${body}[status]    placed

    Log To Console    ${body}
    Log To Console    ${response.status_code}

Get Order By ID
    [Documentation]    Getting order by the ID
    Create Session    petApi    ${BASE_URL}    verify=True
    
    ${response}=    GET On Session    petApi    /store/order/123
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    
    Log To Console    ${response.status_code}
    Log To Console    ${body}

Delete Order By ID
    [Documentation]    Deleting order by the ID
    Create Session    petApi    ${BASE_URL}    verify=True
    ${response}=    DELETE On Session    petApi    /store/order/123
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.status_code}
    
E2E
    Create Session    e2e    ${BASE_URL}    verify=True
    ${payload}=    Create Dictionary
    ...    id=123
    ...    petId=12345
    ...    quantity=1
    ...    shipDate=2024-06-01T12:00:00.000
    ...    status=placed
    ...    complete=true
    
    ${res1}=    POST On Session    e2e    /store/order    json=${payload}
    Should Be Equal As Integers    ${res1.status_code}    200
    ${body}=    Set Variable    ${res1.json()}
    ${ORDER_ID}=    Set Variable    ${body}[id]
    Log To Console    Created an order
    
    ${res2}=    GET On Session    e2e    /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res2.status_code}    200
    Log To Console    Got the order

    ${res3}=    DELETE On Session    e2e    /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res3.status_code}    200
    Log To Console    Deleted the order by ID

