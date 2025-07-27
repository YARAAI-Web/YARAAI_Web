rule auto_rule_20250726084001_4332 {
  strings:
    $o0 = "KeGetCurrentThread" wide ascii nocase
    $o1 = "dword_78990" wide ascii nocase
    $o2 = "dword_788F8" wide ascii nocase
    $o3 = "KeInitializeMutex" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}