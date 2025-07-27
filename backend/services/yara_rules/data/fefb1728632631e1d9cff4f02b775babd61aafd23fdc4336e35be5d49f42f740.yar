rule auto_rule_20250726194709_4915 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "TargetIp" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
    $o3 = "dword_410000" wide ascii nocase
  condition:
    4 of ($o*)
}