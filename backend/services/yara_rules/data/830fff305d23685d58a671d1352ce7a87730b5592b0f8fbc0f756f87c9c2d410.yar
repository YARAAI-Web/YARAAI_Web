rule auto_rule_20250726233807_0118 {
  strings:
    $o0 = "dword_44C7AC" wide ascii nocase
    $o1 = "dword_44C13C" wide ascii nocase
    $o2 = "dword_44C3D4" wide ascii nocase
  condition:
    3 of ($o*)
}