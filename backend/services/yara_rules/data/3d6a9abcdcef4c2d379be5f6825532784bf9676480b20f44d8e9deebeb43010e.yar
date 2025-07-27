rule auto_rule_20250726125748_6931 {
  strings:
    $o0 = "aVirtualalloc" wide ascii nocase
  condition:
    all of them
}