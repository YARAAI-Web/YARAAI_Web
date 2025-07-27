rule auto_rule_20250726092441_6929 {
  strings:
    $o0 = "dword_42EC53" wide ascii nocase
  condition:
    all of them
}