rule auto_rule_20250726103755_6142 {
  strings:
    $o0 = "dword_100433D8" wide ascii nocase
  condition:
    all of them
}