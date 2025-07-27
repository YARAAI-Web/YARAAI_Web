rule auto_rule_20250726175730_3579 {
  strings:
    $o0 = "dword_42EED0" wide ascii nocase
    $o1 = "dword_42EEB0" wide ascii nocase
  condition:
    all of them
}