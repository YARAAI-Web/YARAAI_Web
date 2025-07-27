rule auto_rule_20250726220434_3308 {
  strings:
    $o0 = "dword_78204" wide ascii nocase
  condition:
    all of them
}