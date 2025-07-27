rule auto_rule_20250727001208_5985 {
  strings:
    $o0 = "dword_787E8" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}