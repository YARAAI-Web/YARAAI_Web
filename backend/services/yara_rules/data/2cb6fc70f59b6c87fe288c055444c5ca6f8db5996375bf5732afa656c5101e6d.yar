rule auto_rule_20250726133412_7912 {
  strings:
    $o0 = "dword_41824C" wide ascii nocase
    $o1 = "flProtect" wide ascii nocase
  condition:
    all of them
}