rule auto_rule_20250726084609_6484 {
  strings:
    $o0 = "dword_4C18AC" wide ascii nocase
  condition:
    all of them
}