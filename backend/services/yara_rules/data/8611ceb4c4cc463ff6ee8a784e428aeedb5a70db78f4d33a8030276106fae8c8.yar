rule auto_rule_20250726205909_3104 {
  strings:
    $o0 = "xC4AA" wide ascii nocase
    $o1 = "off_42FE03" wide ascii nocase
    $o2 = "x2929u" wide ascii nocase
  condition:
    3 of ($o*)
}