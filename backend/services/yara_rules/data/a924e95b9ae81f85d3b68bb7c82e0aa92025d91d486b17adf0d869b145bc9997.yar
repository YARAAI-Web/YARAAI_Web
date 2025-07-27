rule auto_rule_20250727020332_6677 {
  strings:
    $o0 = "overrun" wide ascii nocase
    $o1 = "byte_42BB88" wide ascii nocase
    $o2 = "dword_45CF18" wide ascii nocase
  condition:
    3 of ($o*)
}