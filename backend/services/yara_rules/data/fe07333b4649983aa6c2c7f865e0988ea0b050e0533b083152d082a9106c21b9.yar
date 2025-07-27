rule auto_rule_20250726234838_4641 {
  strings:
    $o0 = "off_47DE64" wide ascii nocase
    $o1 = "_fptrap" wide ascii nocase
    $o2 = "_heap_init" wide ascii nocase
  condition:
    3 of ($o*)
}