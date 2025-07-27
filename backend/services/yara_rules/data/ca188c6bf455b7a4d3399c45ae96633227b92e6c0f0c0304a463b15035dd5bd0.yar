rule auto_rule_20250726132840_9227 {
  strings:
    $o0 = "dword_457780" wide ascii nocase
    $o1 = "cause" wide ascii nocase
  condition:
    all of them
}