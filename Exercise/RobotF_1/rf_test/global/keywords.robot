*** Settings ***
Resource       vars.robot
Library  SeleniumLibrary

*** Keywords ***
Start App
  Open Browser  ${URL}  ${BROWSER}
  Maximize Browser Window
  