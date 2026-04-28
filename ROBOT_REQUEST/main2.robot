*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://petstore.swagger.io/v2

*** Test Cases ***
Add Pet
    Create Session    petApi    ${BASE_URL}    verify=True
    
    ${url}=    Create Dictionary    status=available

    ${payload}=    Load Json From File    ${CURDIR}/Data/add_pet.json
    
    ${response}=    POST On Session    petApi    /pet   json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Upload Image
    Create Session    petApi    ${BASE_URL}    verify=True
    
    ## Form data to be sent in the request body
    ${form_data}=    Create Dictionary    additionalMetadata=Jason Image
    
    ## Path to image file
    ${file_path}=    Set Variable    ${CURDIR}/Data/jason_image.jpg
    
    ## Evaluate reads the python code and converts it to robot framework format. 
    ## Here we are opening the file in binary mode and storing it in a dictionary with the key 'file'
#    ${file}=    Evaluate    {'file': open($file_path, 'rb')}

    ${file}=    Create Dictionary    file=${file_path}
    ${response}=    POST On Session    petApi    /pet/55/uploadImage
    ## The form data and the file are being sent in the request body and 
    ## the response is stored in the variable ${response}
    ...    data=${form_data}
    ...    files=${file}

    Should Be Equal As Integers    ${response.status_code}    200

Find Pet
    Create Session    petApi    ${BASE_URL}    verify=True

    ${response}=    GET On Session    petApi    /pet/55
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Update Pet
    Create Session    petApi    ${BASE_URL}    verify=True

    ${form_data}=    Create Dictionary    
    ...    name=Jason    
    ...    status=sold

    ${response}=    POST On Session
    ...    petApi
    ...    /pet/55
    ...    data=${form_data}

Delete Pet
    Create Session    petApi    ${BASE_URL}    verify=True

    ${response}=    DELETE On Session    petApi    /pet/55
    Should Be Equal As Integers    ${response.status_code}    200