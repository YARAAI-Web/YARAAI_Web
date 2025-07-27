rule auto_rule_20250726062205_1743 {
  strings:
    $o0 = "HeapCreate_30" wide ascii nocase
  condition:
    all of them
}