rule auto_rule_20250726121637_8866 {
  strings:
    $o0 = "HeapCreate_3" wide ascii nocase
  condition:
    all of them
}