rule auto_rule_20250726202350_8086 {
  strings:
    $o0 = "dword_45DAF4" wide ascii nocase
    $o1 = "TrailDown1_0" wide ascii nocase
    $o2 = "dword_45DD84" wide ascii nocase
    $o3 = "dword_45D430" wide ascii nocase
  condition:
    4 of ($o*)
}