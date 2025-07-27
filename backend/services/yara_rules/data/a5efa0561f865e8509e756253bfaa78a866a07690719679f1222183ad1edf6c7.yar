rule auto_rule_20250726230622_8098 {
  strings:
    $o0 = "byte_64030190" wide ascii nocase
    $o1 = "dword_6402E98C" wide ascii nocase
  condition:
    all of them
}