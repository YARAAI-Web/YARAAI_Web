rule auto_rule_20250726104707_8047 {
  strings:
    $o0 = "OpenMutexA" wide ascii nocase
    $o1 = "dword_475E94" wide ascii nocase
    $o2 = "dword_476AB8" wide ascii nocase
  condition:
    3 of ($o*)
}