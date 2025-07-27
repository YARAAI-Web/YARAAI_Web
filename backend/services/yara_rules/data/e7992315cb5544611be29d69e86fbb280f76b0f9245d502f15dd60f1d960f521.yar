rule auto_rule_20250726170248_2935 {
  strings:
    $o0 = "old_esp" wide ascii nocase
    $o1 = "dword_449E30" wide ascii nocase
  condition:
    all of them
}