rule auto_rule_20250726181512_1856 {
  strings:
    $o0 = "dword_10003144" wide ascii nocase
  condition:
    all of them
}