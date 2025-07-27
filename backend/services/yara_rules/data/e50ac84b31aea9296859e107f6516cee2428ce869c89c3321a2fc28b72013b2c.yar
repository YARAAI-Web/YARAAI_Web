rule auto_rule_20250727030828_7583 {
  strings:
    $o0 = "GetInputDesktop" wide ascii nocase
    $o1 = "dwShareMode" wide ascii nocase
    $o2 = "DlgDirListComboBoxA" wide ascii nocase
    $o3 = "SendInput" wide ascii nocase
    $o4 = "DdeDisconnect" wide ascii nocase
  condition:
    4 of ($o*)
}