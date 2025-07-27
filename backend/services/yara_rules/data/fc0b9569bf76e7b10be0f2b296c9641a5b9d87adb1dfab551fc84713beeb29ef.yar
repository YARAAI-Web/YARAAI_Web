rule auto_rule_20250726084040_8791 {
  strings:
    $o0 = "bInitialState" wide ascii nocase
    $o1 = "x54FCu" wide ascii nocase
    $o2 = "x20B6" wide ascii nocase
  condition:
    3 of ($o*)
}