rule auto_rule_20250726224922_2174 {
  strings:
    $o0 = "dword_45CEF4" wide ascii nocase
  condition:
    all of them
}