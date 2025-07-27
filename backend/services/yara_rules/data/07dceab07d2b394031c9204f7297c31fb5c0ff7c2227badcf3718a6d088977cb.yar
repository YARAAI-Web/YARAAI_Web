rule auto_rule_20250726201704_6765 {
  strings:
    $o0 = "dword_45CAD4" wide ascii nocase
    $o1 = "__freetlocinfo" wide ascii nocase
    $o2 = "dword_45CABC" wide ascii nocase
  condition:
    3 of ($o*)
}