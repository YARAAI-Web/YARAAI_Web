rule auto_rule_20250726230843_7063 {
  strings:
    $o0 = "DumpManager" wide ascii nocase
    $o1 = "Writer" wide ascii nocase
  condition:
    all of them
}