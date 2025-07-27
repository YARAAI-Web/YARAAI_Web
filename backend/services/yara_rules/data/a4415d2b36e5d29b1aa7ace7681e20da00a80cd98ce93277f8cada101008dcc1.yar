rule auto_rule_20250726065531_7144 {
  strings:
    $o0 = "x4E1Au" wide ascii nocase
    $o1 = "dword_438088" wide ascii nocase
  condition:
    all of them
}