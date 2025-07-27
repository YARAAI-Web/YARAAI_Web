rule auto_rule_20250726203949_4301 {
  strings:
    $o0 = "dword_640303F4" wide ascii nocase
  condition:
    all of them
}