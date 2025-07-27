rule auto_rule_20250726184747_3629 {
  strings:
    $o0 = "vsprintf" wide ascii nocase
    $o1 = "DevCapsA" wide ascii nocase
  condition:
    all of them
}