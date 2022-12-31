*** Variables ***
${BASE_URL}   http://127.0.0.1:5000

*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           LogTextLibrary.py

*** Keywords ***
Create Logtext File
    [Arguments]    ${path}    ${name}
    create_new_logtext_file    ${BASE_URL}    ${name}    ${path}

Delete Logtext File
    [Arguments]    ${path}
    delete_existing_logtext_file    ${BASE_URL}    ${path}

Find Logtext File
    [Arguments]    ${path}
    find_existing_logtext_file    ${BASE_URL}    ${path}


Move Logtext File
    [Arguments]    ${move_from}    ${move_to}
    move_existing_logtext_file    ${BASE_URL}    ${move_from}    ${move_to}