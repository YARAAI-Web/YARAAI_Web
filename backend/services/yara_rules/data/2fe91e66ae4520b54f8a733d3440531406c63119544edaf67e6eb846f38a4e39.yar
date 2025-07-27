rule auto_rule_20250726082746_0423 {
  strings:
    $o0 = "dword_77F1C" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}