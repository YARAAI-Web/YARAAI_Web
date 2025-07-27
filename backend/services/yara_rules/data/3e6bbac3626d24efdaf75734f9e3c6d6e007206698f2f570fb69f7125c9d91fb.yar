rule auto_rule_20250726092647_9154 {
  strings:
    $o0 = "dword_7F960" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}