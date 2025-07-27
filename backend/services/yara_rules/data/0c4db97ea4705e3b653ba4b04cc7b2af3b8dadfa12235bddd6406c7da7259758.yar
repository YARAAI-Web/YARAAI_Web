rule auto_rule_20250726195858_6782 {
  strings:
    $o0 = "nLower" wide ascii nocase
    $o1 = "CompletionKey" wide ascii nocase
  condition:
    all of them
}