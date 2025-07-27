rule auto_rule_20250726094059_7033 {
  strings:
    $o0 = "dword_4183F4" wide ascii nocase
    $o1 = "uSize" wide ascii nocase
  condition:
    all of them
}