rule auto_rule_20250726174257_1679 {
  strings:
    $o0 = "WINNLSGetIMEHotkey" wide ascii nocase
    $o1 = "piRet" wide ascii nocase
    $o2 = "CallMsgFilter" wide ascii nocase
    $o3 = "paccel" wide ascii nocase
  condition:
    4 of ($o*)
}