rule auto_rule_20250726172021_2443 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "dword_449EE4" wide ascii nocase
  condition:
    all of them
}