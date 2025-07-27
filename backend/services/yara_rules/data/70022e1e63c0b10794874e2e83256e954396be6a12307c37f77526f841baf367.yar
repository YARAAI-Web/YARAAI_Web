rule auto_rule_20250726132902_9702 {
  strings:
    $o0 = "byte_7CE8C3" wide ascii nocase
    $o1 = "dword_7CEE6C" wide ascii nocase
  condition:
    all of them
}