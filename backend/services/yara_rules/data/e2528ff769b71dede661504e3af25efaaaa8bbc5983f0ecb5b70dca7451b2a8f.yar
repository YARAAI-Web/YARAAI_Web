rule auto_rule_20250726102829_2253 {
  strings:
    $o0 = "dword_4C16B8" wide ascii nocase
    $o1 = "TrayIconHide" wide ascii nocase
  condition:
    all of them
}