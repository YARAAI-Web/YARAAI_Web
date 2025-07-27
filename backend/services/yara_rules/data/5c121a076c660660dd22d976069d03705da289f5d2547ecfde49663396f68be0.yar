rule auto_rule_20250726233143_3897 {
  strings:
    $o0 = "byte_64030190" wide ascii nocase
    $o1 = "dword_640303F8" wide ascii nocase
  condition:
    all of them
}