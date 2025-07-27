rule auto_rule_20250726163156_8095 {
  strings:
    $o0 = "dword_6402F96C" wide ascii nocase
  condition:
    all of them
}