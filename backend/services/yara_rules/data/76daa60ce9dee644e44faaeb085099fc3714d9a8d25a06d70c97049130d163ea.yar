rule auto_rule_20250727020943_4412 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "_cpinfo" wide ascii nocase
    $o2 = "word_46EE90" wide ascii nocase
    $o3 = "dodwords" wide ascii nocase
  condition:
    4 of ($o*)
}