rule auto_rule_20250727015539_4723 {
  strings:
    $o0 = "SetThreadContext" wide ascii nocase
    $o1 = "psapi" wide ascii nocase
    $o2 = "dword_1E407110" wide ascii nocase
    $o3 = "LibraryA" wide ascii nocase
  condition:
    4 of ($o*)
}