rule auto_rule_20250726145825_4430 {
  strings:
    $o0 = "dword_4C1138" wide ascii nocase
    $o1 = "dword_4C12F4" wide ascii nocase
    $o2 = "dword_4C12C0" wide ascii nocase
    $o3 = "byte_4BBC18" wide ascii nocase
  condition:
    4 of ($o*)
}