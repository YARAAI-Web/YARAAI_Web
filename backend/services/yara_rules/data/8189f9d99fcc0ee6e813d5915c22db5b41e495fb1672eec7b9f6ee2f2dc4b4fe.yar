rule auto_rule_20250726134448_3329 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "dword_41190C" wide ascii nocase
    $o2 = "byte_40F994" wide ascii nocase
  condition:
    3 of ($o*)
}