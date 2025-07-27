rule auto_rule_20250726235744_7742 {
  strings:
    $o0 = "lprcItem" wide ascii nocase
    $o1 = "OpenInputDesktop" wide ascii nocase
    $o2 = "lpTemplate" wide ascii nocase
  condition:
    3 of ($o*)
}