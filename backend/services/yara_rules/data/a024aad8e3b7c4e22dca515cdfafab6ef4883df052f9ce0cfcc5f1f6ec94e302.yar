rule auto_rule_20250726200234_0646 {
  strings:
    $o0 = "off_4533C4" wide ascii nocase
    $o1 = "_ZeroTail" wide ascii nocase
  condition:
    all of them
}