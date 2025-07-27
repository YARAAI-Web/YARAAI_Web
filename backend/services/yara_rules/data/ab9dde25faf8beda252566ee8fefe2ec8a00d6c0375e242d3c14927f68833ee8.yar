rule auto_rule_20250726212700_7794 {
  strings:
    $o0 = "dword_432AD4" wide ascii nocase
    $o1 = "dword_43648A" wide ascii nocase
  condition:
    all of them
}