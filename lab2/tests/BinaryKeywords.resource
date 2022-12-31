*** Variables ***
${BASE_URL}   http://127.0.0.1:5000

*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           BinaryLibrary.py

*** Keywords ***

Create Binary File
    [Arguments]    ${name}    ${path}    ${content}
    create_new_binary_file    ${BASE_URL}    ${name}    ${path}    ${content}

Move Binary File
    [Arguments]    ${move_from}    ${move_to}
    move_existing_binary_file    ${BASE_URL}    ${move_from}    ${move_to}

Delete Existing Binary File
    [Arguments]    ${path}
    delete_binary_file    ${BASE_URL}    ${path}

Find Existing Binary File
    [Arguments]    ${path}
    find_binary_file    ${BASE_URL}    ${path}

Binary File Has Content Equal To
    [Arguments]    ${path}    ${expected_content}
    find_binary_file    ${BASE_URL}    ${path}
    status_should_be    200
    expect_binary_file_content    ${expected_content}