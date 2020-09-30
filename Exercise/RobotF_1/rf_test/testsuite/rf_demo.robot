*** Settings ***
Library         SeleniumLibrary
Library         ${CURDIR}${/}..${/}Utility${/}lib.py
Resource        ${CURDIR}${/}..${/}global${/}keywords.robot
Force Tags      keyword-driven
#Test Setup      Start App
Test Teardown   Close Browser

*** Variables ***
${TITLE}      STORE

*** Keywords ***
Go To Home
  Start App
  Title Should Be  ${TITLE}

Login to the portal
  [Arguments]  ${user}  ${pass}
  Click Element     ${Login Link}
  Wait Until Element Is Visible    css:input#loginusername
  Input Text        ${Username TextBox}     ${user}
  Input Text        ${Password TextBox}     ${pass}
  Click Button      Log in
  Wait Until Element Is Visible    ${LogOut Link}

Open Browser to Login Page
  [Arguments]  ${user}  ${pass}
  Go To Home
  Page Should Contain Element  css:a#cat
  Element Should Contain  css:a#cat  CATEGORIES
  Login to the portal   ${USER}    ${PASS}
  [Teardown]    Close Browser

Open Browser to Login Page with ${loginuser} and ${password}
  Go To Home
  Page Should Contain Element  css:a#cat
  Element Should Contain  css:a#cat  CATEGORIES
  Login to the portal   ${loginuser}    ${password}
  [Teardown]    Close Browser

*** Test Cases ***
Verify Login
  [Tags]    logintest
  Go To Home
  Page Should Contain Element  css:a#cat
  Element Should Contain  css:a#cat  CATEGORIES
  Login to the portal   ${USER}    ${PASS}


Verify Login2
  [Tags]    logintest
  Go To Home
  Page Should Contain Element  css:a#cat
  Element Should Contain  css:a#cat  CATEGORIES
  Login to the portal   ${USER}    ${PASS}

Verify Multiple Logins
  [Tags]    logintest2
  [Template]    Open Browser to Login Page
  #user     pass
  demo      demo
  admin     admin
  test      test

Verify Login in arguments
  [Tags]    logintest3
  [Template]    Open Browser to Login Page with ${loginuser} and ${password}
  demo      demo
  admin     admin

Get Python Function Keyword
  [Tags]    logintest4
  ${result}=    gettimenow
  Log to console    ${result}