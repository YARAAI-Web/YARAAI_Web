rule auto_rule_20250726194105_3449 {
  strings:
    $o0 = "dword_7830C" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}