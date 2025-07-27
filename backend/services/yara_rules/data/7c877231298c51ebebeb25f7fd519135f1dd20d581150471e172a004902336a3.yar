rule auto_rule_20250726233204_2077 {
  strings:
    $o0 = "byte_40BEA0" wide ascii nocase
    $o1 = "dword_40BC94" wide ascii nocase
  condition:
    all of them
}