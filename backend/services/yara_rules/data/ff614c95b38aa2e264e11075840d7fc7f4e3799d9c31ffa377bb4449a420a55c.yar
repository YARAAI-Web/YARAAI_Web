rule auto_rule_20250726131330_8019 {
  strings:
    $o0 = "dword_46D5DC" wide ascii nocase
  condition:
    all of them
}