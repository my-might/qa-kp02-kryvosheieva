*** Variables ***
${BASE_URL}   http://127.0.0.1:5000

*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           DirectoryLibrary.py

*** Keywords ***
Create Directory
    [Arguments]    ${path}  ${name}  ${max_elements}
    create_new_directory    ${BASE_URL}    ${name}    ${path}    ${max_elements}

Delete Directory
    [Arguments]    ${path}
    delete_existing_directory    ${BASE_URL}    ${path}

Expect Directory Content
    [Arguments]    ${path}    ${expected_content}
    list_existing_directory    ${BASE_URL}    ${path}
    compare_with_directory_content    ${expected_content}
    status_should_be    Match

Reset
    reset_db    ${BASE_URL}