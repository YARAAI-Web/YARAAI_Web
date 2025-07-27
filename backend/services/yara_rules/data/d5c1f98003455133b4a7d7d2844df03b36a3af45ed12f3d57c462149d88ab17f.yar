rule auto_rule_20250726101628_0627 {
  strings:
    $o0 = "SetTextColor" wide ascii nocase
    $o1 = "byte_40917B" wide ascii nocase
  condition:
    all of them
}