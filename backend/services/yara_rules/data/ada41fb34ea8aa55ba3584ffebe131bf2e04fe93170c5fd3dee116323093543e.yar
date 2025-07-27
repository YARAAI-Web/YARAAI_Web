rule auto_rule_20250726144347_0023 {
  strings:
    $o0 = "dwExStyle" wide ascii nocase
    $o1 = "dword_41D990" wide ascii nocase
  condition:
    all of them
}