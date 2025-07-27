rule auto_rule_20250726075248_4526 {
  strings:
    $o0 = "byte_4845C4" wide ascii nocase
    $o1 = "byte_484A00" wide ascii nocase
    $o2 = "__add_12" wide ascii nocase
  condition:
    3 of ($o*)
}