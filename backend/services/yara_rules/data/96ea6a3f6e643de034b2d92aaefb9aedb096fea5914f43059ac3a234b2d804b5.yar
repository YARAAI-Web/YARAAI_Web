rule auto_rule_20250726204133_0349 {
  strings:
    $o0 = "TlsAlloc_11" wide ascii nocase
  condition:
    all of them
}