rule auto_rule_20250726111522_2126 {
  strings:
    $o0 = "dword_418350" wide ascii nocase
  condition:
    all of them
}