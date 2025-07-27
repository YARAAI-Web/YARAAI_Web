rule auto_rule_20250726183502_8430 {
  strings:
    $o0 = "dword_4118F8" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "dword_40E000" wide ascii nocase
  condition:
    3 of ($o*)
}