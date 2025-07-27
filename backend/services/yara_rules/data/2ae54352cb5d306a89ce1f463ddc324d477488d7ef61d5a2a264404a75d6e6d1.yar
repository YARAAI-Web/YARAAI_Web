rule auto_rule_20250726100332_2815 {
  strings:
    $o0 = "dword_44C11C" wide ascii nocase
    $o1 = "strcat" wide ascii nocase
    $o2 = "ActiveWindow" wide ascii nocase
    $o3 = "TargetIp" wide ascii nocase
  condition:
    4 of ($o*)
}