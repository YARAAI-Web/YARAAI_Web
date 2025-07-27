rule auto_rule_20250726152024_4781 {
  strings:
    $o0 = "dword_64031414" wide ascii nocase
  condition:
    all of them
}