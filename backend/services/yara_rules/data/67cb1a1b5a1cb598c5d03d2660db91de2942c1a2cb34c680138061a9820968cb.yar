rule auto_rule_20250726162113_8761 {
  strings:
    $o0 = "dword_413C84" wide ascii nocase
  condition:
    all of them
}