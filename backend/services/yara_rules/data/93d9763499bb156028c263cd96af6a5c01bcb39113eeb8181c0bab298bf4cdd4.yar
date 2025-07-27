rule auto_rule_20250726191822_1185 {
  strings:
    $o0 = "dword_42FCDD" wide ascii nocase
    $o1 = "IsChild" wide ascii nocase
  condition:
    all of them
}