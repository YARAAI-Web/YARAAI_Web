rule auto_rule_20250726185802_5653 {
  strings:
    $o0 = "ReadFile_1" wide ascii nocase
    $o1 = "unknown_libname_25" wide ascii nocase
    $o2 = "LocalAlloc_0" wide ascii nocase
  condition:
    3 of ($o*)
}