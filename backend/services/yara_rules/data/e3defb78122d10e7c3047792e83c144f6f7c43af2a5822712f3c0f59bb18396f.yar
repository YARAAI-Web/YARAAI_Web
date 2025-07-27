rule auto_rule_20250726173900_4835 {
  strings:
    $o0 = "dword_463A38" wide ascii nocase
    $o1 = "Object" wide ascii nocase
  condition:
    all of them
}