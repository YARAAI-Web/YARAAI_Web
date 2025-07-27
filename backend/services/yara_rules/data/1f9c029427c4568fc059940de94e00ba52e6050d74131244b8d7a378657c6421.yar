rule auto_rule_20250726074355_5934 {
  strings:
    $o0 = "dword_464440" wide ascii nocase
  condition:
    all of them
}