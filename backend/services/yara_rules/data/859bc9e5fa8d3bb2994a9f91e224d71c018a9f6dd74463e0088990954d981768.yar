rule auto_rule_20250726225235_4483 {
  strings:
    $o0 = "dword_42E9D0" wide ascii nocase
  condition:
    all of them
}