rule auto_rule_20250726192316_8856 {
  strings:
    $o0 = "dword_4D0174" wide ascii nocase
  condition:
    all of them
}