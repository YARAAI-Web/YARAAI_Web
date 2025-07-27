rule auto_rule_20250726113853_4758 {
  strings:
    $o0 = "pclsid" wide ascii nocase
    $o1 = "_ltoa" wide ascii nocase
    $o2 = "x1388" wide ascii nocase
  condition:
    3 of ($o*)
}