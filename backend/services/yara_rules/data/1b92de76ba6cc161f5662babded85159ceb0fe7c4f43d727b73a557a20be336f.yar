rule auto_rule_20250726164254_1189 {
  strings:
    $o0 = "dword_640303E8" wide ascii nocase
    $o1 = "dword_64030294" wide ascii nocase
  condition:
    all of them
}