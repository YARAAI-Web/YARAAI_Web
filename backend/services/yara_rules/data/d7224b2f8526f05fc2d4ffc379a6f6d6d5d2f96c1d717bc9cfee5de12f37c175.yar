rule auto_rule_20250727011117_2937 {
  strings:
    $o0 = "dword_4C1698" wide ascii nocase
  condition:
    all of them
}