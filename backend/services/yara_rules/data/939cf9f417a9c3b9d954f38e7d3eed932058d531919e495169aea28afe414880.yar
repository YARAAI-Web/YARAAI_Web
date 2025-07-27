rule auto_rule_20250726124932_6756 {
  strings:
    $o0 = "CurrentThread" wide ascii nocase
    $o1 = "xF2A9" wide ascii nocase
  condition:
    all of them
}