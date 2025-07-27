rule auto_rule_20250726120654_3328 {
  strings:
    $o0 = "SourceString" wide ascii nocase
    $o1 = "dword_78114" wide ascii nocase
  condition:
    all of them
}