rule auto_rule_20250726221933_6397 {
  strings:
    $o0 = "dword_457A48" wide ascii nocase
    $o1 = "_fptrap" wide ascii nocase
  condition:
    all of them
}