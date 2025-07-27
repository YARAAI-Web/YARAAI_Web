rule auto_rule_20250726133632_4775 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "dword_40B018" wide ascii nocase
  condition:
    all of them
}