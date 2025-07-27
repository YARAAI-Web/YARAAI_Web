rule auto_rule_20250726142418_7009 {
  strings:
    $o0 = "dword_427994" wide ascii nocase
    $o1 = "dword_42799C" wide ascii nocase
  condition:
    all of them
}