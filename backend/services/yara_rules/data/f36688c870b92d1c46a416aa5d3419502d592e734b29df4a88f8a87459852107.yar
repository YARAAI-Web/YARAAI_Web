rule auto_rule_20250726214958_2270 {
  strings:
    $o0 = "byte_45D040" wide ascii nocase
    $o1 = "dword_45CADC" wide ascii nocase
  condition:
    all of them
}