rule auto_rule_20250726125236_4216 {
  strings:
    $o0 = "x5B24u" wide ascii nocase
    $o1 = "aClsid13709620C" wide ascii nocase
  condition:
    all of them
}