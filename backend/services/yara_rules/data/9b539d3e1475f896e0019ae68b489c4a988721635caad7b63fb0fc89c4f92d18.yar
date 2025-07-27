rule auto_rule_20250727030023_1815 {
  strings:
    $o0 = "dword_45525C" wide ascii nocase
    $o1 = "cause" wide ascii nocase
  condition:
    all of them
}