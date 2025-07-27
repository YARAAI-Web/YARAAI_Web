rule auto_rule_20250727040552_6676 {
  strings:
    $o0 = "lpdwPartition" wide ascii nocase
  condition:
    all of them
}