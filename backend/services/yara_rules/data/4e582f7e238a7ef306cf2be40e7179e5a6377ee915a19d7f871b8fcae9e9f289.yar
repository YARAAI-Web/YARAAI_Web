rule auto_rule_20250726214306_3314 {
  strings:
    $o0 = "dword_4588F4" wide ascii nocase
  condition:
    all of them
}