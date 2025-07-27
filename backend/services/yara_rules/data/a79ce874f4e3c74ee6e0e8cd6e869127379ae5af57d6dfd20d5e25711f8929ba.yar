rule auto_rule_20250727035534_1253 {
  strings:
    $o0 = "x5FF0u" wide ascii nocase
    $o1 = "x4E77" wide ascii nocase
    $o2 = "x7FB4u" wide ascii nocase
    $o3 = "x39ABu" wide ascii nocase
  condition:
    4 of ($o*)
}