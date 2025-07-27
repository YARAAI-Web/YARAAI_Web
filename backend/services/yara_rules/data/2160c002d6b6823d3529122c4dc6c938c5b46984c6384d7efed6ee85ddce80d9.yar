rule auto_rule_20250726121350_6887 {
  strings:
    $o0 = "_global_unwind2" wide ascii nocase
    $o1 = "dword_46E910" wide ascii nocase
    $o2 = "dword_46F0A0" wide ascii nocase
    $o3 = "off_46E000" wide ascii nocase
  condition:
    4 of ($o*)
}