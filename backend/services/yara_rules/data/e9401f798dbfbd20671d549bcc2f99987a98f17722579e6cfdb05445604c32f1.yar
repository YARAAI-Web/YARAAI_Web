rule auto_rule_20250726091019_1099 {
  strings:
    $o0 = "UnwindUp4_0" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "StringTypeW" wide ascii nocase
    $o3 = "dword_44E450" wide ascii nocase
  condition:
    4 of ($o*)
}