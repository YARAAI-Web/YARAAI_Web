rule auto_rule_20250726074612_4569 {
  strings:
    $o0 = "dword_464404" wide ascii nocase
    $o1 = "write_string" wide ascii nocase
  condition:
    all of them
}