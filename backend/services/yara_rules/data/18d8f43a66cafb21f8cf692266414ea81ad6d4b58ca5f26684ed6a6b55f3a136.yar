rule auto_rule_20250726095811_5731 {
  strings:
    $o0 = "xF89C85A5" wide ascii nocase
    $o1 = "x744Du" wide ascii nocase
    $o2 = "x5A5Fu" wide ascii nocase
    $o3 = "x75108AF" wide ascii nocase
    $o4 = "dword_428453" wide ascii nocase
  condition:
    4 of ($o*)
}