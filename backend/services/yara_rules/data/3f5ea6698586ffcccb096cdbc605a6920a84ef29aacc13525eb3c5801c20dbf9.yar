rule auto_rule_20250726225720_4937 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "dword_4119AC" wide ascii nocase
  condition:
    all of them
}