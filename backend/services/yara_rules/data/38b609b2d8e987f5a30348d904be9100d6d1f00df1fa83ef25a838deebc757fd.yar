rule auto_rule_20250726174730_6704 {
  strings:
    $o0 = "dword_428603" wide ascii nocase
  condition:
    all of them
}