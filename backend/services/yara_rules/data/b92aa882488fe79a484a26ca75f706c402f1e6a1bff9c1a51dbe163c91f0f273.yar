rule auto_rule_20250726060146_3582 {
  strings:
    $o0 = "ExitTime" wide ascii nocase
    $o1 = "off_436030" wide ascii nocase
  condition:
    all of them
}