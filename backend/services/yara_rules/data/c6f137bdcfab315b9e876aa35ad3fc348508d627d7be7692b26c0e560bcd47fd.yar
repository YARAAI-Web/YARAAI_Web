rule auto_rule_20250726182431_7322 {
  strings:
    $o0 = "aPng6s6db" wide ascii nocase
    $o1 = "dword_781C0" wide ascii nocase
  condition:
    all of them
}