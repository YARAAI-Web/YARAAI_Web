rule auto_rule_20250726130208_4911 {
  strings:
    $o0 = "CoGetCallerTID" wide ascii nocase
  condition:
    all of them
}