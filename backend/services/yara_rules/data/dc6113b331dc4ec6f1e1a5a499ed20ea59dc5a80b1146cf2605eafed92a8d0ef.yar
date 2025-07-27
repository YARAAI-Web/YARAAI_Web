rule auto_rule_20250726123539_3012 {
  strings:
    $o0 = "j_j__free" wide ascii nocase
    $o1 = "byte_64030190" wide ascii nocase
    $o2 = "EF8h" wide ascii nocase
  condition:
    3 of ($o*)
}