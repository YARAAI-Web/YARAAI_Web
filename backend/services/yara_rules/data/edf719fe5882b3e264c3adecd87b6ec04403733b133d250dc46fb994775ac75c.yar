rule auto_rule_20250726161554_6284 {
  strings:
    $o0 = "dword_42EED0" wide ascii nocase
    $o1 = "dword_42EEAC" wide ascii nocase
  condition:
    all of them
}