*** Variables ***
${BASE_URL}   http://127.0.0.1:5000

*** Settings ***
Documentation     This is a resource file, that can contain variables and keywords.
...               Keywords defined here can be used where this Keywords.resource in loaded.
Library           BufferLibrary.py

*** Keywords ***
Create Buffer
    [Arguments]    ${path}  ${name}  ${max_size}
    create_new_buffer    ${BASE_URL}    ${name}    ${path}    ${max_size}

Delete Buffer
    [Arguments]    ${path}
    delete_existing_buffer    ${BASE_URL}    ${path}

Move Buffer File
    [Arguments]    ${move_from}    ${move_to}
    move_buffer_to_new_folder    ${BASE_URL}    ${move_from}    ${move_to}

Expect Buffer Content
    [Arguments]    ${path}    ${expected_content}
    consume_existing_buffer    ${BASE_URL}    ${path}
    compare_with_buffer_content    ${expected_content}
    buffer_status_should_be    Match