rule auto_rule_20250726195643_3739 {
  strings:
    $o0 = "lpFatTime" wide ascii nocase
    $o1 = "lpdwHighByteSeeked" wide ascii nocase
  condition:
    all of them
}