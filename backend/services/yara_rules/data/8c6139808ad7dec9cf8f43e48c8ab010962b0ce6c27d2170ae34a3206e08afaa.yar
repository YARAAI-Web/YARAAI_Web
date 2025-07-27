rule auto_rule_20250727024645_4233 {
  strings:
    $o0 = "dbgheap" wide ascii nocase
  condition:
    all of them
}