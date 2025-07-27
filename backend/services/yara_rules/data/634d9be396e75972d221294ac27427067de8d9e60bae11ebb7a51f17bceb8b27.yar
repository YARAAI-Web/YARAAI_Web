rule auto_rule_20250726213731_1387 {
  strings:
    $o0 = "__add_12" wide ascii nocase
    $o1 = "dword_459BA8" wide ascii nocase
  condition:
    all of them
}