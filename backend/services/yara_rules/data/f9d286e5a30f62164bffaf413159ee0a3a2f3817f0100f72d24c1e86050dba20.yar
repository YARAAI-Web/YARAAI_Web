rule auto_rule_20250726094537_5626 {
  strings:
    $o0 = "dword_4C146C" wide ascii nocase
  condition:
    all of them
}