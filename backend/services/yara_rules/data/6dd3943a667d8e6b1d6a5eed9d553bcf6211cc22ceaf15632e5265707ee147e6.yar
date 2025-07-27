rule auto_rule_20250726151257_8280 {
  strings:
    $o0 = "dword_46F0B4" wide ascii nocase
  condition:
    all of them
}