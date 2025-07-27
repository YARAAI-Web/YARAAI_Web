rule auto_rule_20250726105347_6044 {
  strings:
    $o0 = "xB23u" wide ascii nocase
    $o1 = "dword_42C881" wide ascii nocase
    $o2 = "wParam_4c" wide ascii nocase
    $o3 = "dword_42C74D" wide ascii nocase
  condition:
    4 of ($o*)
}